### 1. Nomenclatura Estricta y Carpetas Globales

Al tomar la decisión de usar carpetas globales (`01 - Fleeting Notes`, `02 - References Notes`) para la universidad, el mayor riesgo era el caos de archivos. Lo neutralizaste a la perfección con tu regla de nombrado: `DSI-Parcial2-TEO-U02-`.

- **La ventaja:** Al forzar este prefijo, los archivos se ordenan alfabéticamente por materia, instancia (parcial/final) y unidad de forma automática. Te da un orden visual impecable sin tener que crear un laberinto de subcarpetas.
    

### 2. Un YAML Pensado para Rendir (imagen_6.png)

Las propiedades que definiste en tu _Note Template_ están optimizadas para la vida académica:

- **`subject` y `unit`:** Son el núcleo de tu base de datos. Te permiten aislar el material exacto que necesitas.
    
- **`type` (TEO/PRAC):** Separar la teoría de la práctica es vital en tu carrera. Si el final es muy teórico, filtras por `TEO` y el ruido desaparece.
    
- **`exam`:** Esta propiedad es brillante. Hoy dice "PARCIAL", pero te permite etiquetar material nuevo que solo entra en el "FINAL", ayudándote a priorizar qué estudiar.
    

### 3. El MOC como Panel de Control (Sin título_2.png)

Tu _Map Of Content_ de DSI no es solo un índice, es un tablero de gestión de estudio.

- Las tablas de Dataview te muestran exactamente qué apuntes de las unidades 2 y 3 están listos (`Estado: done`) y cuáles Permanent Notes (como `WorkFlow DISEÑO` o `Requerimientos No Funcionales`) están todavía `in progress`.
    
- Esto elimina la ansiedad de "qué me falta estudiar"; con un vistazo a este MOC, sabes exactamente dónde estás parado.
    

### Un detalle a tener en cuenta para el Final

Dado que estás enfocado en preparar este final y las carpetas son globales, asegúrate de que en tus bloques de Dataview dentro del MOC de DSI estés filtrando siempre por `WHERE subject = "DSI"`. A medida que vayas sumando archivos a la carpeta `4to`, esto garantizará que si alguna vez olvidas poner el prefijo en el título de una Fleeting Note, Dataview igual la atrape y no te la mezcle con otras materias.