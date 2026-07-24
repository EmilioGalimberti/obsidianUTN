# Guía Completa de Markdown y Obsidian

Esta guía contiene la sintaxis básica de Markdown, junto con las funciones avanzadas y específicas que hacen de **Obsidian** una herramienta tan potente para crear tu "Segundo Cerebro" y conectar ideas mediante el grafo.

---

## 1. Sintaxis Básica de Markdown

### Encabezados
Para crear títulos y subtítulos, usa el símbolo de numeral `#` seguido de un espacio.
```markdown
# Título 1 (H1 - El más grande)
## Título 2 (H2)
### Título 3 (H3)
#### Título 4 (H4)
```

### Formato de Texto
```markdown
**Texto en negrita**
*Texto en cursiva* o _Texto en cursiva_
~~Texto tachado~~
==Texto resaltado== (Específico de Obsidian)
```

### Listas
**Listas Desordenadas:** Usa `-`, `*` o `+` seguidos de un espacio.
```markdown
- Elemento 1
- Elemento 2
  - Subelemento (usa sangría/tabulador)
```

**Listas Ordenadas:** Usa números seguidos de un punto.
```markdown
1. Primer paso
2. Segundo paso
```

**Listas de Tareas (Checklists):**
```markdown
- [ ] Tarea pendiente
- [x] Tarea completada
- [/] Tarea en progreso (depende del tema visual que uses)
```

### Citas
Usa el signo mayor que `>`.
```markdown
> "El conocimiento es poder."
> — Francis Bacon
```

### Código
Para código en línea, usa comillas invertidas simples: ` ` `código` ` `
Para bloques de código, usa tres comillas invertidas:

```python
# Ejemplo de bloque de código en Python
def hola_mundo():
    print("¡Hola, Obsidian!")
```

---

## 2. El Poder de Obsidian: Conectando tu Grafo

La verdadera magia de Obsidian reside en cómo conecta la información. Aquí están las herramientas para construir tu red neuronal de notas.

### Enlaces Internos (Wikilinks)
Usa corchetes dobles para enlazar a otras notas. Esto es lo que construye las conexiones en tu **Vista de Grafo (Graph View)**.
```markdown
[[Nombre de otra nota]]
```
*Tip:* Si escribes `[[` Obsidian te sugerirá automáticamente notas existentes. Si escribes un nombre que no existe y haces clic en él, Obsidian creará la nota automáticamente.

### Alias en los Enlaces
A veces el nombre de la nota no encaja gramaticalmente en tu texto. Puedes usar un alias añadiendo `|`:
```markdown
[[Inteligencia Artificial|IA]]
```
*El texto mostrará "IA", pero te llevará a la nota "Inteligencia Artificial".*

### Enlaces a Encabezados y Bloques
Puedes enlazar a una sección específica de otra nota:
- **A un encabezado:** `[[Nombre de la nota#Nombre del encabezado]]`
- **A un bloque específico (párrafo):** `[[Nombre de la nota^...]]` (Obsidian generará un ID único para el bloque).

### Incrustación de Notas (Embeds)
Si quieres **ver el contenido** de otra nota (o imagen) dentro de la nota actual, añade un signo de exclamación `!` antes del enlace:
```markdown
![[Resumen de la reunión]]
```
*Esto mostrará el texto completo de "Resumen de la reunión" aquí mismo.*

### Etiquetas (Tags)
Las etiquetas sirven para categorizar notas transversalmente.
```markdown
#productividad #ideas #programacion/python
```
*Tip para el Grafo:* Las etiquetas anidadas como `#programacion/python` te permiten organizar tus temas jerárquicamente. En el grafo, puedes filtrar para ver solo las notas con ciertas etiquetas.

---

## 3. Elementos Avanzados en Obsidian

### Propiedades (Frontmatter)
En la parte superior de tu nota, puedes añadir metadatos usando YAML (encerrado entre tres guiones `---`). Obsidian usa esto de forma nativa para gestionar alias, etiquetas y otros datos.
```yaml
---
aliases: [Guía, Manual MD]
tags: [tutorial, obsidian]
date: 2026-04-25
---
```

### Callouts (Cuadros de llamada)
Los callouts son excelentes para resaltar información, advertencias o notas importantes. Se construyen usando la sintaxis de citas combinada con corchetes:

```markdown
> [!info] Información
> Este es un cuadro de información útil.

> [!warning] Advertencia
> Ten cuidado al borrar archivos.

> [!todo] Tareas pendientes
> - [ ] Revisar el grafo
> - [ ] Organizar etiquetas
```
*Puedes usar otros tipos como: `[!note]`, `[!tip]`, `[!danger]`, `[!question]`, `[!success]`, `[!bug]`.* 


>[!note] holas d como estas




---

## 4. Tips y Atajos de Flujo de Trabajo en Obsidian

Para moverte a la velocidad de la luz, memoriza estos atajos (Windows/Linux):

### Navegación y Creación
- **`Ctrl + N`**: Crear nueva nota.
- **`Ctrl + O`**: Abrir nota rápida (Abre un buscador donde escribes el nombre y saltas directo a ella). **(El atajo más útil)**
- **`Ctrl + Shift + F`**: Búsqueda global en toda tu bóveda.
- **`Alt + Flecha Izquierda/Derecha`**: Ir a la nota anterior/siguiente en tu historial (como en un navegador web).

### Edición
- **`Ctrl + E`**: Cambiar entre Modo Lectura y Modo Edición (Live Preview).
- **`Ctrl + Enter`**: Marcar/desmarcar una casilla de tarea `- [ ]`.
- **Seleccionar texto + `[[`**: Encierra el texto seleccionado en un enlace interno automáticamente.

### Interfaz
- **`Ctrl + P`**: Abrir la Paleta de Comandos. Desde aquí puedes buscar *cualquier* acción que Obsidian pueda hacer (ej: "Exportar a PDF", "Abrir vista de grafo", etc.).
- **Arrastrar pestañas**: Puedes dividir tu pantalla arrastrando la pestaña de una nota hacia la derecha, izquierda, arriba o abajo. Útil para leer una nota mientras escribes en otra.

### Consejos para un Grafo Saludable
1. **MOCs (Map of Content):** Crea "Notas Índice". Por ejemplo, una nota llamada `[[MOC Programación]]` que contenga enlaces a todas tus notas sobre lenguajes, proyectos y tutoriales. Esto crea nodos centrales fuertes en tu grafo.
2. **Notas Atómicas:** Trata de que cada nota contenga una sola idea principal (Zettelkasten). Es más fácil conectar 10 notas pequeñas y específicas que enlazar a un documento gigante de 20 páginas.
3. **No abuses de los tags:** Usa enlaces `[[ ]]` para conectar conceptos (ej. `[[Python]]`) y etiquetas `#` para el *estado* o *tipo* de nota (ej. `#borrador`, `#idea`, `#articulo`).
