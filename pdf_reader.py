#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
"""
=============================================================================
 PDF READER UNIVERSAL — Script completo para extracción de contenido PDF
=============================================================================
 Autor        : Script para uso general por IAs y humanos
 Versión      : 2.0
 Descripción  : Extrae texto, imágenes, metadatos, tablas, anotaciones,
                marcadores, formularios y más de archivos PDF.
 
 DEPENDENCIAS (instalar con pip):
 ---------------------------------
   pip install PyMuPDF pdfplumber pillow pdfminer.six camelot-py[cv] pandas

 USO BÁSICO:
 -----------
   python pdf_reader.py archivo.pdf
   python pdf_reader.py archivo.pdf --output resultado.json
   python pdf_reader.py archivo.pdf --pages 1-5
   python pdf_reader.py archivo.pdf --images --tables --full
   python pdf_reader.py --help

 INTEGRACIÓN PARA IAs:
 ---------------------
   from pdf_reader import PDFReader
   reader = PDFReader("mi_archivo.pdf")
   data = reader.extract_all()          # Extrae todo
   text = reader.extract_text()         # Solo texto
   meta = reader.extract_metadata()     # Solo metadatos
   imgs = reader.extract_images()       # Solo imágenes (base64)
   tbls = reader.extract_tables()       # Solo tablas (lista de listas)
   
=============================================================================
"""

import os
import sys
import json
import base64
import hashlib
import argparse
import traceback
from pathlib import Path
from datetime import datetime
from io import BytesIO
from typing import Any

# ─────────────────────────────────────────────────────────────────────────────
#  VERIFICACIÓN DE DEPENDENCIAS
# ─────────────────────────────────────────────────────────────────────────────

def check_dependencies() -> dict[str, bool]:
    """Verifica qué librerías están instaladas."""
    deps = {}
    try:
        import fitz  # PyMuPDF
        deps["pymupdf"] = True
    except ImportError:
        deps["pymupdf"] = False

    try:
        import pdfplumber
        deps["pdfplumber"] = True
    except ImportError:
        deps["pdfplumber"] = False

    try:
        from PIL import Image
        deps["pillow"] = True
    except ImportError:
        deps["pillow"] = False

    try:
        import pandas
        deps["pandas"] = True
    except ImportError:
        deps["pandas"] = False

    try:
        from pdfminer.high_level import extract_text_to_fp
        deps["pdfminer"] = True
    except ImportError:
        deps["pdfminer"] = False

    return deps


DEPS = check_dependencies()

# Importaciones opcionales según disponibilidad
if DEPS["pymupdf"]:
    import fitz

if DEPS["pdfplumber"]:
    import pdfplumber

if DEPS["pillow"]:
    from PIL import Image

if DEPS["pandas"]:
    import pandas as pd

if DEPS["pdfminer"]:
    from pdfminer.high_level import extract_text as pdfminer_extract
    from pdfminer.layout import LAParams


# ─────────────────────────────────────────────────────────────────────────────
#  CLASE PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────

class PDFReader:
    """
    Clase principal para extracción completa de contenido de PDFs.
    
    Usa múltiples backends (PyMuPDF, pdfplumber, pdfminer) para máxima
    cobertura y precisión.
    """

    def __init__(
        self,
        pdf_path: str,
        password: str | None = None,
        image_output_dir: str | None = None,
        image_format: str = "PNG",
        image_dpi: int = 150,
        verbose: bool = False,
    ):
        """
        Inicializa el lector de PDF.

        Args:
            pdf_path         : Ruta al archivo PDF.
            password         : Contraseña si el PDF está protegido.
            image_output_dir : Carpeta donde guardar las imágenes extraídas.
                               Si es None, las imágenes solo se devuelven en base64.
            image_format     : Formato de imagen ("PNG", "JPEG", "WEBP").
            image_dpi        : Resolución para renderizar páginas como imagen.
            verbose          : Mostrar mensajes de progreso.
        """
        self.pdf_path = Path(pdf_path).resolve()
        self.password = password
        self.image_output_dir = Path(image_output_dir) if image_output_dir else None
        self.image_format = image_format.upper()
        self.image_dpi = image_dpi
        self.verbose = verbose
        self._doc_fitz = None  # Documento PyMuPDF (lazy)

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {self.pdf_path}")
        if not self.pdf_path.suffix.lower() == ".pdf":
            raise ValueError(f"El archivo no es un PDF: {self.pdf_path}")

        if self.image_output_dir:
            self.image_output_dir.mkdir(parents=True, exist_ok=True)

        self._log(f"PDF cargado: {self.pdf_path}")

    # ──────────────────────────────────────────────────────────────────────────
    #  UTILIDADES INTERNAS
    # ──────────────────────────────────────────────────────────────────────────

    def _log(self, msg: str):
        if self.verbose:
            print(f"[PDF Reader] {msg}", file=sys.stderr)

    def _get_fitz_doc(self):
        """Obtiene (o reutiliza) el documento PyMuPDF."""
        if not DEPS["pymupdf"]:
            raise RuntimeError("PyMuPDF no está instalado. Ejecuta: pip install PyMuPDF")
        if self._doc_fitz is None:
            self._doc_fitz = fitz.open(str(self.pdf_path))
            if self._doc_fitz.needs_pass:
                if self.password:
                    if not self._doc_fitz.authenticate(self.password):
                        raise ValueError("Contraseña incorrecta para el PDF.")
                else:
                    raise ValueError("El PDF está protegido por contraseña. Usa el parámetro 'password'.")
        return self._doc_fitz

    def _parse_page_range(self, pages: str | None, total: int) -> list[int]:
        """
        Convierte un string de rango de páginas a lista de índices 0-based.
        Ejemplos: "1", "1-5", "1,3,5-7", "all"
        """
        if pages is None or pages == "all":
            return list(range(total))
        result = set()
        for part in pages.split(","):
            part = part.strip()
            if "-" in part:
                start, end = part.split("-", 1)
                result.update(range(int(start) - 1, int(end)))
            else:
                result.add(int(part) - 1)
        return sorted(p for p in result if 0 <= p < total)

    @staticmethod
    def _img_to_base64(img_bytes: bytes, fmt: str = "PNG") -> str:
        """Convierte bytes de imagen a string base64 con header data URI."""
        mime = {"PNG": "image/png", "JPEG": "image/jpeg", "WEBP": "image/webp"}.get(fmt, "image/png")
        b64 = base64.b64encode(img_bytes).decode("utf-8")
        return f"data:{mime};base64,{b64}"

    # ──────────────────────────────────────────────────────────────────────────
    #  METADATOS
    # ──────────────────────────────────────────────────────────────────────────

    def extract_metadata(self) -> dict[str, Any]:
        """
        Extrae metadatos completos del PDF.

        Retorna un diccionario con:
          - file_info    : info del archivo (tamaño, hash, etc.)
          - document     : metadatos del documento (autor, título, fechas...)
          - security     : información de seguridad y permisos
          - structure    : estructura del documento (páginas, capítulos...)
          - pdf_version  : versión del formato PDF
        """
        doc = self._get_fitz_doc()
        pdf_meta = doc.metadata or {}

        # ── Info del archivo ────────────────────────────────────────────────
        file_stat = self.pdf_path.stat()
        sha256 = hashlib.sha256(self.pdf_path.read_bytes()).hexdigest()

        file_info = {
            "path": str(self.pdf_path),
            "filename": self.pdf_path.name,
            "size_bytes": file_stat.st_size,
            "size_human": _human_size(file_stat.st_size),
            "created": datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
            "sha256": sha256,
        }

        # ── Metadatos del documento ─────────────────────────────────────────
        document_meta = {
            "title": pdf_meta.get("title") or None,
            "author": pdf_meta.get("author") or None,
            "subject": pdf_meta.get("subject") or None,
            "keywords": pdf_meta.get("keywords") or None,
            "creator": pdf_meta.get("creator") or None,
            "producer": pdf_meta.get("producer") or None,
            "creation_date": _parse_pdf_date(pdf_meta.get("creationDate")),
            "modification_date": _parse_pdf_date(pdf_meta.get("modDate")),
            "trapped": pdf_meta.get("trapped") or None,
        }

        # ── Seguridad ───────────────────────────────────────────────────────
        permissions = doc.permissions
        security_info = {
            "is_encrypted": doc.is_encrypted,
            "needs_password": doc.needs_pass,
            "permissions": {
                "print": bool(permissions & fitz.PDF_PERM_PRINT),
                "modify": bool(permissions & fitz.PDF_PERM_MODIFY),
                "copy": bool(permissions & fitz.PDF_PERM_COPY),
                "annotate": bool(permissions & fitz.PDF_PERM_ANNOTATE),
                "fill_forms": bool(permissions & fitz.PDF_PERM_FILLFORM),
                "extract": bool(permissions & fitz.PDF_PERM_ACCESSIBILITY),
                "assemble": bool(permissions & fitz.PDF_PERM_ASSEMBLE),
                "print_highres": bool(permissions & fitz.PDF_PERM_PRINT_HQ),
            },
        }

        # ── Estructura ──────────────────────────────────────────────────────
        toc = doc.get_toc()
        structure = {
            "page_count": doc.page_count,
            "has_toc": len(toc) > 0,
            "toc_entries": len(toc),
            "pdf_version": doc.pdf_version(),
            "is_pdf": doc.is_pdf,
            "is_reflowable": doc.is_reflowable,
            "language": pdf_meta.get("language") or None,
        }

        # ── Páginas individuales ────────────────────────────────────────────
        pages_info = []
        for i, page in enumerate(doc):
            rect = page.rect
            pages_info.append({
                "page": i + 1,
                "width_pt": round(rect.width, 2),
                "height_pt": round(rect.height, 2),
                "width_mm": round(rect.width * 25.4 / 72, 2),
                "height_mm": round(rect.height * 25.4 / 72, 2),
                "rotation": page.rotation,
            })

        self._log("Metadatos extraídos correctamente.")

        return {
            "file_info": file_info,
            "document": document_meta,
            "security": security_info,
            "structure": structure,
            "pages_info": pages_info,
            "installed_backends": DEPS,
        }

    # ──────────────────────────────────────────────────────────────────────────
    #  TEXTO
    # ──────────────────────────────────────────────────────────────────────────

    def extract_text(
        self,
        pages: str | None = None,
        mode: str = "full",
        include_page_numbers: bool = True,
        include_coordinates: bool = False,
    ) -> dict[str, Any]:
        """
        Extrae texto del PDF con múltiples niveles de detalle.

        Args:
            pages               : Rango de páginas. None = todas.
            mode                : "full" = texto plano completo
                                  "blocks" = bloques con coordenadas
                                  "words"  = palabras con coordenadas
                                  "rich"   = texto enriquecido (HTML)
                                  "layout" = preservar layout con pdfminer
            include_page_numbers: Agregar números de página al texto.
            include_coordinates : Incluir coordenadas (x,y) de cada elemento.

        Retorna diccionario con:
          - full_text    : texto completo concatenado
          - pages        : lista de páginas con texto individual
          - word_count   : conteo total de palabras
          - char_count   : conteo de caracteres
          - language_hint: idioma detectado (heurístico)
        """
        doc = self._get_fitz_doc()
        page_indices = self._parse_page_range(pages, doc.page_count)
        results = []
        full_text_parts = []

        for idx in page_indices:
            page = doc[idx]
            page_num = idx + 1
            self._log(f"Extrayendo texto — página {page_num}/{doc.page_count}")

            page_data: dict[str, Any] = {"page": page_num}

            if mode == "full":
                text = page.get_text("text")
                page_data["text"] = text
                full_text_parts.append(f"{'─'*60}\n[Página {page_num}]\n{text}" if include_page_numbers else text)

            elif mode == "blocks":
                blocks = page.get_text("blocks")
                block_list = []
                for b in blocks:
                    block_item = {
                        "text": b[4].strip(),
                        "type": "image" if b[6] == 1 else "text",
                    }
                    if include_coordinates:
                        block_item["x0"] = round(b[0], 2)
                        block_item["y0"] = round(b[1], 2)
                        block_item["x1"] = round(b[2], 2)
                        block_item["y1"] = round(b[3], 2)
                    block_list.append(block_item)
                page_data["blocks"] = block_list
                text = "\n".join(b["text"] for b in block_list if b["type"] == "text")
                page_data["text"] = text
                full_text_parts.append(text)

            elif mode == "words":
                words = page.get_text("words")
                word_list = []
                for w in words:
                    word_item = {"word": w[4], "block": w[5], "line": w[6]}
                    if include_coordinates:
                        word_item.update({"x0": round(w[0], 2), "y0": round(w[1], 2),
                                          "x1": round(w[2], 2), "y1": round(w[3], 2)})
                    word_list.append(word_item)
                page_data["words"] = word_list
                text = " ".join(w["word"] for w in word_list)
                page_data["text"] = text
                full_text_parts.append(text)

            elif mode == "rich":
                html = page.get_text("html")
                page_data["html"] = html
                page_data["text"] = page.get_text("text")
                full_text_parts.append(page_data["text"])

            elif mode == "layout":
                # Usa pdfminer para preservar mejor el layout
                if DEPS["pdfminer"]:
                    try:
                        text = pdfminer_extract(str(self.pdf_path), page_numbers=[idx], laparams=LAParams())
                        page_data["text"] = text
                        full_text_parts.append(text)
                    except Exception as e:
                        page_data["text"] = page.get_text("text")
                        page_data["layout_error"] = str(e)
                        full_text_parts.append(page_data["text"])
                else:
                    page_data["text"] = page.get_text("text")
                    page_data["warning"] = "pdfminer no instalado, usando PyMuPDF"
                    full_text_parts.append(page_data["text"])

            else:
                raise ValueError(f"Modo inválido: '{mode}'. Usa: full, blocks, words, rich, layout")

            # Estadísticas por página
            raw_text = page_data.get("text", "")
            page_data["stats"] = {
                "char_count": len(raw_text),
                "word_count": len(raw_text.split()),
                "line_count": raw_text.count("\n") + 1 if raw_text else 0,
            }
            results.append(page_data)

        full_text = "\n".join(full_text_parts)

        return {
            "mode": mode,
            "pages_extracted": len(page_indices),
            "full_text": full_text,
            "pages": results,
            "stats": {
                "total_chars": len(full_text),
                "total_words": len(full_text.split()),
                "total_lines": full_text.count("\n") + 1 if full_text else 0,
            },
        }

    # ──────────────────────────────────────────────────────────────────────────
    #  IMÁGENES
    # ──────────────────────────────────────────────────────────────────────────

    def extract_images(
        self,
        pages: str | None = None,
        include_base64: bool = True,
        min_width: int = 50,
        min_height: int = 50,
        render_pages: bool = False,
    ) -> dict[str, Any]:
        """
        Extrae imágenes embebidas en el PDF y (opcionalmente) renderiza páginas.

        Args:
            pages          : Rango de páginas. None = todas.
            include_base64 : Incluir imágenes codificadas en base64.
            min_width      : Ancho mínimo para filtrar imágenes pequeñas.
            min_height     : Alto mínimo para filtrar imágenes pequeñas.
            render_pages   : También renderizar cada página como imagen completa.

        Retorna:
          - images       : Lista de imágenes extraídas con metadata y base64.
          - rendered_pages: Lista de páginas renderizadas (si render_pages=True).
          - total_images : Total de imágenes encontradas.
        """
        doc = self._get_fitz_doc()
        page_indices = self._parse_page_range(pages, doc.page_count)
        all_images = []
        rendered = []
        seen_xrefs = set()

        for idx in page_indices:
            page = doc[idx]
            page_num = idx + 1
            self._log(f"Extrayendo imágenes — página {page_num}/{doc.page_count}")

            # ── Imágenes embebidas ─────────────────────────────────────────
            img_list = page.get_images(full=True)
            for img_info in img_list:
                xref = img_info[0]
                if xref in seen_xrefs:
                    continue
                seen_xrefs.add(xref)

                try:
                    base_img = doc.extract_image(xref)
                    if not base_img:
                        continue

                    img_bytes = base_img["image"]
                    w, h = base_img.get("width", 0), base_img.get("height", 0)
                    ext = base_img.get("ext", "png").lower()

                    # Filtrar imágenes demasiado pequeñas
                    if w < min_width or h < min_height:
                        continue

                    # Convertir a formato deseado si PIL está disponible
                    fmt_used = ext.upper()
                    if DEPS["pillow"] and self.image_format != ext.upper():
                        try:
                            pil_img = Image.open(BytesIO(img_bytes))
                            out = BytesIO()
                            save_fmt = self.image_format if self.image_format != "JPEG" else "JPEG"
                            if pil_img.mode in ("RGBA", "P") and save_fmt == "JPEG":
                                pil_img = pil_img.convert("RGB")
                            pil_img.save(out, format=save_fmt)
                            img_bytes = out.getvalue()
                            fmt_used = self.image_format
                        except Exception:
                            pass  # Mantener formato original si falla conversión

                    img_record: dict[str, Any] = {
                        "xref": xref,
                        "page": page_num,
                        "width": w,
                        "height": h,
                        "format": fmt_used,
                        "size_bytes": len(img_bytes),
                        "colorspace": base_img.get("colorspace", "unknown"),
                        "bpc": base_img.get("bpc", 8),
                        "sha256": hashlib.sha256(img_bytes).hexdigest()[:16],
                        "smask": img_info[1],        # máscara soft (transparencia)
                        "filter": base_img.get("filter", None),
                    }

                    if include_base64:
                        img_record["base64"] = self._img_to_base64(img_bytes, fmt_used)

                    # Guardar en disco si se configuró directorio
                    if self.image_output_dir:
                        fname = f"img_p{page_num:03d}_x{xref}.{fmt_used.lower()}"
                        fpath = self.image_output_dir / fname
                        fpath.write_bytes(img_bytes)
                        img_record["saved_path"] = str(fpath)

                    all_images.append(img_record)

                except Exception as e:
                    self._log(f"  Error en imagen xref={xref}: {e}")

            # ── Renderizado de página completa ────────────────────────────
            if render_pages:
                try:
                    mat = fitz.Matrix(self.image_dpi / 72, self.image_dpi / 72)
                    clip = page.rect
                    pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
                    img_bytes = pix.tobytes(self.image_format.lower())

                    rendered_record: dict[str, Any] = {
                        "page": page_num,
                        "width": pix.width,
                        "height": pix.height,
                        "dpi": self.image_dpi,
                        "format": self.image_format,
                        "size_bytes": len(img_bytes),
                    }
                    if include_base64:
                        rendered_record["base64"] = self._img_to_base64(img_bytes, self.image_format)
                    if self.image_output_dir:
                        fname = f"render_p{page_num:03d}.{self.image_format.lower()}"
                        fpath = self.image_output_dir / fname
                        fpath.write_bytes(img_bytes)
                        rendered_record["saved_path"] = str(fpath)

                    rendered.append(rendered_record)
                except Exception as e:
                    self._log(f"  Error al renderizar página {page_num}: {e}")

        result: dict[str, Any] = {
            "total_images": len(all_images),
            "images": all_images,
        }
        if render_pages:
            result["rendered_pages"] = rendered

        self._log(f"Total imágenes extraídas: {len(all_images)}")
        return result

    # ──────────────────────────────────────────────────────────────────────────
    #  TABLAS
    # ──────────────────────────────────────────────────────────────────────────

    def extract_tables(
        self,
        pages: str | None = None,
        output_format: str = "list",
    ) -> dict[str, Any]:
        """
        Extrae tablas del PDF usando pdfplumber.

        Args:
            pages        : Rango de páginas. None = todas.
            output_format: "list"    = lista de listas (raw)
                           "dict"    = lista de dicts (primera fila = cabeceras)
                           "markdown"= tabla en formato Markdown
                           "csv"     = tabla en formato CSV (texto)

        Retorna:
          - tables     : Lista de tablas con número de página y datos.
          - total_tables: Total de tablas encontradas.
        """
        if not DEPS["pdfplumber"]:
            return {"error": "pdfplumber no instalado. Ejecuta: pip install pdfplumber", "tables": []}

        all_tables = []
        total = 0

        with pdfplumber.open(str(self.pdf_path), password=self.password or "") as pdf:
            page_indices = self._parse_page_range(pages, len(pdf.pages))
            for idx in page_indices:
                page = pdf.pages[idx]
                page_num = idx + 1
                self._log(f"Extrayendo tablas — página {page_num}/{len(pdf.pages)}")

                tables = page.extract_tables()
                for t_idx, table in enumerate(tables):
                    total += 1
                    table_data: dict[str, Any] = {
                        "page": page_num,
                        "table_index": t_idx + 1,
                        "rows": len(table),
                        "cols": max(len(row) for row in table) if table else 0,
                    }

                    if output_format == "list":
                        table_data["data"] = table

                    elif output_format == "dict":
                        if table and len(table) > 1:
                            headers = [str(h or "").strip() for h in table[0]]
                            table_data["data"] = [
                                {headers[i]: str(cell or "").strip()
                                 for i, cell in enumerate(row) if i < len(headers)}
                                for row in table[1:]
                            ]
                        else:
                            table_data["data"] = table

                    elif output_format == "markdown":
                        table_data["data"] = _table_to_markdown(table)

                    elif output_format == "csv":
                        table_data["data"] = _table_to_csv(table)

                    else:
                        raise ValueError(f"Formato inválido: '{output_format}'. Usa: list, dict, markdown, csv")

                    all_tables.append(table_data)

        self._log(f"Total tablas extraídas: {total}")
        return {"total_tables": total, "tables": all_tables}

    # ──────────────────────────────────────────────────────────────────────────
    #  ANOTACIONES Y COMENTARIOS
    # ──────────────────────────────────────────────────────────────────────────

    def extract_annotations(self, pages: str | None = None) -> dict[str, Any]:
        """
        Extrae anotaciones, comentarios, resaltados y notas del PDF.

        Retorna:
          - annotations  : Lista de anotaciones con tipo, texto y posición.
          - total        : Total de anotaciones.
        """
        doc = self._get_fitz_doc()
        page_indices = self._parse_page_range(pages, doc.page_count)
        all_annots = []

        ANNOT_TYPES = {
            0: "Text", 1: "Link", 2: "FreeText", 3: "Line", 4: "Square",
            5: "Circle", 6: "Polygon", 7: "PolyLine", 8: "Highlight",
            9: "Underline", 10: "Squiggly", 11: "StrikeOut", 12: "Redact",
            13: "Stamp", 14: "Caret", 15: "Ink", 16: "Popup", 17: "FileAttachment",
            18: "Sound", 19: "Movie", 20: "Widget", 21: "Screen",
            22: "PrinterMark", 23: "TrapNet", 24: "Watermark", 25: "3D",
        }

        for idx in page_indices:
            page = doc[idx]
            page_num = idx + 1
            for annot in page.annots():
                info = annot.info
                rect = annot.rect
                annot_data: dict[str, Any] = {
                    "page": page_num,
                    "type": ANNOT_TYPES.get(annot.type[0], f"Unknown({annot.type[0]})"),
                    "type_code": annot.type[0],
                    "content": info.get("content", "") or None,
                    "author": info.get("title", "") or None,
                    "subject": info.get("subject", "") or None,
                    "creation_date": _parse_pdf_date(info.get("creationDate")),
                    "modification_date": _parse_pdf_date(info.get("modDate")),
                    "color": annot.colors,
                    "opacity": annot.opacity,
                    "flags": annot.flags,
                    "rect": {
                        "x0": round(rect.x0, 2), "y0": round(rect.y0, 2),
                        "x1": round(rect.x1, 2), "y1": round(rect.y1, 2),
                    },
                }
                # Texto subrayado/resaltado
                if annot.type[0] in (8, 9, 10, 11):  # Highlight, Underline, etc.
                    try:
                        annot_data["highlighted_text"] = page.get_text("text", clip=rect).strip()
                    except Exception:
                        pass
                all_annots.append(annot_data)

        self._log(f"Total anotaciones: {len(all_annots)}")
        return {"total": len(all_annots), "annotations": all_annots}

    # ──────────────────────────────────────────────────────────────────────────
    #  MARCADORES / TABLA DE CONTENIDOS
    # ──────────────────────────────────────────────────────────────────────────

    def extract_toc(self) -> dict[str, Any]:
        """
        Extrae la tabla de contenidos (marcadores/bookmarks) del PDF.

        Retorna:
          - toc    : Lista jerárquica de entradas TOC.
          - total  : Total de entradas.
          - has_toc: Si el PDF tiene TOC.
        """
        doc = self._get_fitz_doc()
        raw_toc = doc.get_toc(simple=False)

        def build_entry(item):
            level, title, page, dest = item[0], item[1], item[2], item[3] if len(item) > 3 else {}
            entry: dict[str, Any] = {
                "level": level,
                "title": title,
                "page": page,
            }
            if isinstance(dest, dict):
                entry["dest_type"] = dest.get("kind", "unknown")
                if "to" in dest:
                    entry["dest_y"] = round(dest["to"].y, 2) if hasattr(dest["to"], "y") else None
                if "uri" in dest:
                    entry["uri"] = dest["uri"]
            return entry

        entries = [build_entry(item) for item in raw_toc]
        return {
            "has_toc": len(entries) > 0,
            "total": len(entries),
            "toc": entries,
        }

    # ──────────────────────────────────────────────────────────────────────────
    #  ENLACES / HIPERVÍNCULOS
    # ──────────────────────────────────────────────────────────────────────────

    def extract_links(self, pages: str | None = None) -> dict[str, Any]:
        """
        Extrae todos los enlaces (internos y externos) del PDF.

        Retorna:
          - links      : Lista de enlaces con tipo, URL/destino y posición.
          - total      : Total de enlaces.
          - external   : Lista de URLs externas únicas.
        """
        doc = self._get_fitz_doc()
        page_indices = self._parse_page_range(pages, doc.page_count)
        all_links = []
        external_urls = set()

        LINK_KINDS = {0: "none", 1: "goto", 2: "gotor", 3: "launch",
                      4: "named", 5: "uri", 6: "xref"}

        for idx in page_indices:
            page = doc[idx]
            page_num = idx + 1
            for link in page.get_links():
                kind = link.get("kind", 0)
                entry: dict[str, Any] = {
                    "page": page_num,
                    "type": LINK_KINDS.get(kind, f"unknown({kind})"),
                    "rect": {k: round(v, 2) for k, v in zip(
                        ["x0", "y0", "x1", "y1"], link.get("from", [0, 0, 0, 0])
                    )},
                }
                if kind == 5:  # URI
                    uri = link.get("uri", "")
                    entry["url"] = uri
                    if uri:
                        external_urls.add(uri)
                elif kind == 1:  # Internal goto
                    entry["dest_page"] = link.get("page", -1) + 1
                    entry["dest_y"] = round(link.get("to", {}).get("y", 0), 2) if isinstance(link.get("to"), dict) else None
                elif kind == 4:  # Named
                    entry["name"] = link.get("name", "")
                elif kind in (2, 3):  # GoToR / Launch
                    entry["file"] = link.get("file", "")
                all_links.append(entry)

        return {
            "total": len(all_links),
            "links": all_links,
            "external_urls": sorted(external_urls),
        }

    # ──────────────────────────────────────────────────────────────────────────
    #  FORMULARIOS
    # ──────────────────────────────────────────────────────────────────────────

    def extract_forms(self) -> dict[str, Any]:
        """
        Extrae campos de formularios interactivos (AcroForms).

        Retorna:
          - fields     : Lista de campos con nombre, tipo y valor actual.
          - has_forms  : Si el PDF tiene formularios.
          - total      : Total de campos.
        """
        doc = self._get_fitz_doc()
        fields = []

        FIELD_TYPES = {
            0: "Button", 1: "CheckBox", 2: "RadioButton",
            3: "Text", 4: "ListBox", 5: "ComboBox",
            6: "Signature", 7: "Unknown",
        }

        for page in doc:
            for widget in page.widgets():
                if widget is None:
                    continue
                field_data: dict[str, Any] = {
                    "page": page.number + 1,
                    "name": widget.field_name,
                    "type": FIELD_TYPES.get(widget.field_type, "Unknown"),
                    "value": widget.field_value,
                    "flags": widget.field_flags,
                    "rect": {
                        "x0": round(widget.rect.x0, 2),
                        "y0": round(widget.rect.y0, 2),
                        "x1": round(widget.rect.x1, 2),
                        "y1": round(widget.rect.y1, 2),
                    },
                    "readonly": bool(widget.field_flags & 1),
                    "required": bool(widget.field_flags & 2),
                    "options": list(widget.choice_values) if widget.choice_values else [],
                }
                fields.append(field_data)

        return {
            "has_forms": len(fields) > 0,
            "total": len(fields),
            "fields": fields,
        }

    # ──────────────────────────────────────────────────────────────────────────
    #  FUENTES
    # ──────────────────────────────────────────────────────────────────────────

    def extract_fonts(self) -> dict[str, Any]:
        """
        Extrae información sobre las fuentes tipográficas usadas en el PDF.

        Retorna:
          - fonts  : Lista de fuentes únicas con nombre, tipo y embedding.
          - total  : Total de fuentes.
        """
        doc = self._get_fitz_doc()
        fonts_seen = {}

        for page in doc:
            for font in page.get_fonts(full=True):
                xref = font[0]
                if xref not in fonts_seen:
                    fonts_seen[xref] = {
                        "xref": xref,
                        "name": font[3],
                        "type": font[2],
                        "encoding": font[4] if len(font) > 4 else None,
                        "embedded": font[2] not in ("Type1", "MMType1", "TrueType"),
                        "pages": [page.number + 1],
                    }
                else:
                    pnum = page.number + 1
                    if pnum not in fonts_seen[xref]["pages"]:
                        fonts_seen[xref]["pages"].append(pnum)

        fonts_list = list(fonts_seen.values())
        return {"total": len(fonts_list), "fonts": fonts_list}

    # ──────────────────────────────────────────────────────────────────────────
    #  EXTRACCIÓN COMPLETA
    # ──────────────────────────────────────────────────────────────────────────

    def extract_all(
        self,
        pages: str | None = None,
        text_mode: str = "full",
        include_images: bool = True,
        include_tables: bool = True,
        include_annotations: bool = True,
        include_links: bool = True,
        include_toc: bool = True,
        include_forms: bool = True,
        include_fonts: bool = True,
        render_pages: bool = False,
        include_base64: bool = True,
        table_format: str = "list",
    ) -> dict[str, Any]:
        """
        Extrae TODO el contenido del PDF en una sola llamada.

        Args:
            pages             : Rango de páginas (None = todas).
            text_mode         : Modo de extracción de texto.
            include_images    : Extraer imágenes embebidas.
            include_tables    : Extraer tablas.
            include_annotations: Extraer anotaciones y comentarios.
            include_links     : Extraer hipervínculos.
            include_toc       : Extraer tabla de contenidos.
            include_forms     : Extraer campos de formulario.
            include_fonts     : Extraer información de fuentes.
            render_pages      : Renderizar páginas como imágenes.
            include_base64    : Incluir imágenes en base64.
            table_format      : Formato de tablas (list/dict/markdown/csv).

        Retorna:
            Un diccionario completo con toda la información extraída.
        """
        result: dict[str, Any] = {
            "extraction_timestamp": datetime.now().isoformat(),
            "source_file": str(self.pdf_path),
        }

        print(f"[PDF Reader] Iniciando extracción completa de: {self.pdf_path.name}")

        # 1. Metadatos
        print("[PDF Reader] (1/8) Extrayendo metadatos...")
        result["metadata"] = self.extract_metadata()

        # 2. Texto
        print(f"[PDF Reader] (2/8) Extrayendo texto (modo: {text_mode})...")
        result["text"] = self.extract_text(pages=pages, mode=text_mode)

        # 3. Imágenes
        if include_images:
            print("[PDF Reader] (3/8) Extrayendo imágenes...")
            result["images"] = self.extract_images(
                pages=pages,
                include_base64=include_base64,
                render_pages=render_pages,
            )
        else:
            print("[PDF Reader] (3/8) Imágenes: omitidas.")

        # 4. Tablas
        if include_tables:
            print("[PDF Reader] (4/8) Extrayendo tablas...")
            result["tables"] = self.extract_tables(pages=pages, output_format=table_format)
        else:
            print("[PDF Reader] (4/8) Tablas: omitidas.")

        # 5. Anotaciones
        if include_annotations:
            print("[PDF Reader] (5/8) Extrayendo anotaciones...")
            result["annotations"] = self.extract_annotations(pages=pages)
        else:
            print("[PDF Reader] (5/8) Anotaciones: omitidas.")

        # 6. TOC
        if include_toc:
            print("[PDF Reader] (6/8) Extrayendo tabla de contenidos...")
            result["toc"] = self.extract_toc()

        # 7. Links
        if include_links:
            print("[PDF Reader] (7/8) Extrayendo enlaces...")
            result["links"] = self.extract_links(pages=pages)

        # 8. Forms + Fonts
        if include_forms:
            print("[PDF Reader] (8/8) Extrayendo formularios y fuentes...")
            result["forms"] = self.extract_forms()

        if include_fonts:
            result["fonts"] = self.extract_fonts()

        total_images = result.get("images", {}).get("total_images", 0) if include_images else 0
        total_tables = result.get("tables", {}).get("total_tables", 0) if include_tables else 0
        total_annots = result.get("annotations", {}).get("total", 0) if include_annotations else 0

        print(
            f"\n[PDF Reader] ✓ Extracción completa.\n"
            f"  Páginas    : {result['metadata']['structure']['page_count']}\n"
            f"  Palabras   : {result['text']['stats']['total_words']:,}\n"
            f"  Imágenes   : {total_images}\n"
            f"  Tablas     : {total_tables}\n"
            f"  Anotaciones: {total_annots}\n"
        )

        return result

    def close(self):
        """Cierra el documento PDF y libera recursos."""
        if self._doc_fitz is not None:
            self._doc_fitz.close()
            self._doc_fitz = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        return f"PDFReader(path='{self.pdf_path}', pages={self._get_fitz_doc().page_count if DEPS['pymupdf'] else '?'})"


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCIONES AUXILIARES
# ─────────────────────────────────────────────────────────────────────────────

def _human_size(size_bytes: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def _parse_pdf_date(raw: str | None) -> str | None:
    """Convierte fecha PDF (D:YYYYMMDDHHmmSSOHH'mm') a ISO 8601."""
    if not raw:
        return None
    raw = raw.strip()
    if raw.startswith("D:"):
        raw = raw[2:]
    try:
        # Formato: YYYYMMDDHHmmSS
        dt = datetime.strptime(raw[:14], "%Y%m%d%H%M%S")
        return dt.isoformat()
    except ValueError:
        try:
            dt = datetime.strptime(raw[:8], "%Y%m%d")
            return dt.isoformat()
        except ValueError:
            return raw


def _table_to_markdown(table: list[list]) -> str:
    if not table:
        return ""
    lines = []
    headers = [str(c or "").strip() for c in table[0]]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in table[1:]:
        cells = [str(c or "").strip() for c in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def _table_to_csv(table: list[list]) -> str:
    import csv
    from io import StringIO
    output = StringIO()
    writer = csv.writer(output)
    for row in table:
        writer.writerow([str(c or "").strip() for c in row])
    return output.getvalue()


def _print_dependencies():
    print("\n[DEPS] Estado de dependencias:")
    for lib, ok in DEPS.items():
        status = "[OK] instalado" if ok else "[X]  NO instalado"
        print(f"   {lib:<15} {status}")
    missing = [k for k, v in DEPS.items() if not v]
    if missing:
        print(f"\n[!]  Para instalar todas las dependencias:")
        print("   pip install PyMuPDF pdfplumber pillow pdfminer.six pandas")
    print()


# ─────────────────────────────────────────────────────────────────────────────
#  INTERFAZ DE LÍNEA DE COMANDOS
# ─────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf_reader",
        description="📄 PDF Reader Universal — Extrae texto, imágenes, metadatos y más de PDFs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EJEMPLOS:
  # Extraer solo texto:
  python pdf_reader.py doc.pdf --text

  # Extracción completa a JSON:
  python pdf_reader.py doc.pdf --full --output resultado.json

  # Extraer páginas 1 a 5, solo metadatos:
  python pdf_reader.py doc.pdf --pages 1-5 --metadata

  # Extraer imágenes y guardarlas en una carpeta:
  python pdf_reader.py doc.pdf --images --image-dir ./imagenes

  # Tablas en formato Markdown:
  python pdf_reader.py doc.pdf --tables --table-format markdown

  # PDF con contraseña:
  python pdf_reader.py doc.pdf --password miClave --full

  # Verificar dependencias instaladas:
  python pdf_reader.py --check-deps
        """,
    )

    parser.add_argument("pdf", nargs="?", help="Ruta al archivo PDF.")
    parser.add_argument("--output", "-o", help="Archivo de salida JSON (default: stdout).")
    parser.add_argument("--pages", "-p", help='Páginas a procesar: "1", "1-5", "1,3,5-7", "all".')
    parser.add_argument("--password", help="Contraseña del PDF protegido.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Mostrar progreso detallado.")

    # Opciones de extracción
    group = parser.add_argument_group("Opciones de extracción")
    group.add_argument("--full", action="store_true", help="Extraer TODO (texto + imágenes + tablas + metadatos + etc.).")
    group.add_argument("--text", action="store_true", help="Extraer texto.")
    group.add_argument("--metadata", action="store_true", help="Extraer metadatos.")
    group.add_argument("--images", action="store_true", help="Extraer imágenes embebidas.")
    group.add_argument("--tables", action="store_true", help="Extraer tablas.")
    group.add_argument("--annotations", action="store_true", help="Extraer anotaciones y comentarios.")
    group.add_argument("--links", action="store_true", help="Extraer hipervínculos.")
    group.add_argument("--toc", action="store_true", help="Extraer tabla de contenidos.")
    group.add_argument("--forms", action="store_true", help="Extraer campos de formulario.")
    group.add_argument("--fonts", action="store_true", help="Extraer información de fuentes.")
    group.add_argument("--render", action="store_true", help="Renderizar páginas como imágenes.")

    # Opciones de texto
    tgroup = parser.add_argument_group("Opciones de texto")
    tgroup.add_argument(
        "--text-mode", default="full",
        choices=["full", "blocks", "words", "rich", "layout"],
        help="Modo de extracción de texto (default: full)."
    )
    tgroup.add_argument("--no-coords", action="store_true", help="No incluir coordenadas en bloques/palabras.")

    # Opciones de imágenes
    igroup = parser.add_argument_group("Opciones de imágenes")
    igroup.add_argument("--image-dir", help="Directorio donde guardar las imágenes extraídas.")
    igroup.add_argument("--image-format", default="PNG", choices=["PNG", "JPEG", "WEBP"], help="Formato de imagen.")
    igroup.add_argument("--image-dpi", type=int, default=150, help="DPI para renderizar páginas (default: 150).")
    igroup.add_argument("--no-base64", action="store_true", help="No incluir imágenes en base64 (ahorra espacio).")
    igroup.add_argument("--min-width", type=int, default=50, help="Ancho mínimo de imágenes a extraer.")
    igroup.add_argument("--min-height", type=int, default=50, help="Alto mínimo de imágenes a extraer.")

    # Opciones de tablas
    tabgroup = parser.add_argument_group("Opciones de tablas")
    tabgroup.add_argument(
        "--table-format", default="list",
        choices=["list", "dict", "markdown", "csv"],
        help="Formato de salida de tablas (default: list)."
    )

    # Utilidades
    ugroup = parser.add_argument_group("Utilidades")
    ugroup.add_argument("--check-deps", action="store_true", help="Verificar dependencias instaladas.")
    ugroup.add_argument("--indent", type=int, default=2, help="Indentación JSON (default: 2). Usa 0 para compacto.")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.check_deps:
        _print_dependencies()
        return

    if not args.pdf:
        parser.print_help()
        return

    try:
        reader = PDFReader(
            pdf_path=args.pdf,
            password=args.password,
            image_output_dir=args.image_dir,
            image_format=args.image_format,
            image_dpi=args.image_dpi,
            verbose=args.verbose,
        )

        result: dict[str, Any] = {}

        if args.full:
            result = reader.extract_all(
                pages=args.pages,
                text_mode=args.text_mode,
                include_images=True,
                include_tables=True,
                include_annotations=True,
                include_links=True,
                include_toc=True,
                include_forms=True,
                include_fonts=True,
                render_pages=args.render,
                include_base64=not args.no_base64,
                table_format=args.table_format,
            )
        else:
            # Extracción selectiva
            any_selected = False

            if args.metadata:
                result["metadata"] = reader.extract_metadata()
                any_selected = True

            if args.text:
                result["text"] = reader.extract_text(
                    pages=args.pages,
                    mode=args.text_mode,
                    include_coordinates=not args.no_coords,
                )
                any_selected = True

            if args.images:
                result["images"] = reader.extract_images(
                    pages=args.pages,
                    include_base64=not args.no_base64,
                    render_pages=args.render,
                )
                any_selected = True

            if args.tables:
                result["tables"] = reader.extract_tables(
                    pages=args.pages,
                    output_format=args.table_format,
                )
                any_selected = True

            if args.annotations:
                result["annotations"] = reader.extract_annotations(pages=args.pages)
                any_selected = True

            if args.toc:
                result["toc"] = reader.extract_toc()
                any_selected = True

            if args.links:
                result["links"] = reader.extract_links(pages=args.pages)
                any_selected = True

            if args.forms:
                result["forms"] = reader.extract_forms()
                any_selected = True

            if args.fonts:
                result["fonts"] = reader.extract_fonts()
                any_selected = True

            if not any_selected:
                # Por defecto: extraer texto y metadatos
                print("[PDF Reader] No se especificó qué extraer. Ejecutando extracción básica (texto + metadatos).")
                result["metadata"] = reader.extract_metadata()
                result["text"] = reader.extract_text(pages=args.pages, mode=args.text_mode)

        reader.close()

        # ── Salida ──────────────────────────────────────────────────────────
        indent = args.indent if args.indent > 0 else None
        json_output = json.dumps(result, ensure_ascii=False, indent=indent, default=str)

        if args.output:
            out_path = Path(args.output)
            out_path.write_text(json_output, encoding="utf-8")
            size = _human_size(out_path.stat().st_size)
            print(f"\n[OK] Resultado guardado en: {out_path} ({size})")
        else:
            print(json_output)

    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"[ERROR] Configuracion: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Interrumpido por el usuario.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] Inesperado: {e}", file=sys.stderr)
        if "--verbose" in sys.argv or "-v" in sys.argv:
            traceback.print_exc()
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
