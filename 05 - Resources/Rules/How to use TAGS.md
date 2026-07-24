### para estados 
Esta es la forma más productiva de usar etiquetas. Sirven para indicarte qué acción requiere una nota, independientemente de si es de la facultad o de un curso.

- `#incompleto`: Para notas que tomaste rápido en clase y necesitas pulir después.
    
- `#para_revisar`: Conceptos que no entendiste del todo y requieren que busques más información.
    
- `#refactorizar`: Si tienes un bloque de código que funciona pero sabes que puede mejorarse.
    

Al usar estos tags, puedes buscar `#para_revisar` un domingo por la tarde y Obsidian te mostrará exactamente en qué debes concentrarte, sin importar de qué materia sea.

### 2. Tags de Temática Transversal (El verdadero poder)

Aquí es donde los tags brillan en un estudiante de Ingeniería en Sistemas. Úsalos para agrupar grandes áreas de conocimiento que cruzan los límites de tus materias y proyectos personales.

Supongamos que estás viendo patrones de diseño en la universidad, pero también estás desarrollando una API por tu cuenta. No uses un tag para la materia, usa tags para el concepto global:

- `#backend`
    
- `#arquitectura`
    
- `#java` o `#spring_boot`
    
- `#seguridad`
    

Si mañana tienes un problema construyendo un microservicio y buscas el tag `#arquitectura`, vas a encontrar juntas las notas teóricas de la facultad, tus apuntes del curso de Google y las lecciones que aprendiste programando por tu cuenta.

### 3. Tags de Tipo de Recurso

Aunque las propiedades (YAML) que vimos antes son mejores para esto, a veces un tag rápido es útil para identificar la fuente original de una idea en tus _Fleeting_ o _Reference Notes_:

- `#video_youtube`
    
- `#libro`
    
- `#paper_academico`
    

### Cómo NO deberías usar los tags

- **No los uses como propiedades:** Si ya tienes una propiedad que dice `materia: DSI`, no agregues un tag que diga `#dsi`. Es redundante y Dataview ya hace ese trabajo mejor.
    
- **Evita la sobre-especificidad:** Un tag llamado `#metodo_newton_raphson` es inútil, porque para eso ya tienes el título del archivo o el buscador. Los tags deben ser categorías lo suficientemente grandes como para contener decenas de notas (`#matematica` o `#metodos_numericos`).