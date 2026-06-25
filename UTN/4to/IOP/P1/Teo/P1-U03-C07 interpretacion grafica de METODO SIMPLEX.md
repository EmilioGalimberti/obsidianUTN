 https://youtu.be/awHzTsGFKQY?si=YYfIGyKfMaTdNmmk&t=3953

Esta clase funcionó como un "puente" conceptual entre el Método Gráfico y el Método Simplex, enfocándose en la interpretación visual de cómo opera internamente el algoritmo antes de pasar a la matriz numérica.

Aquí tienes el resumen estructurado con el formato de estudio avanzado:

### 2. 📍 Fase 1 del Algoritmo: El Punto de Partida (1:06:13 - 1:08:40)

El profesor dedicó la primera parte a explicar cómo arranca el motor del algoritmo. El [[Método Simplex]] se apoya en el teorema que dictamina que la solución óptima siempre estará en al menos uno de los puntos extremos o vértices del poliedro de soluciones.


- **Identificación Inicial:** En su Fase 1, el algoritmo necesita obligatoriamente encontrar una primera **[[Solución Factible Básica]]**(las que estan en los verices) para usar como punto de partida. En problemas de maximización con formato canónico (menor o igual), este punto de inicio suele fijarse cómodamente en el origen (donde las variables de decisión valen cero y las holguras asumen todo el valor).
- **Prueba de Optimidad:** Evalúa la [[Función Objetivo]] ($Z$). En el origen $Z=0$, por lo que concluye que no es óptima y debe moverse.

### 3. 🔄 Fase 2 del Algoritmo: Iteración y Desplazamiento (1:08:40 - 1:13:57)
Si el punto inicial no es óptimo, el algoritmo comienza su iteración moviéndose exclusivamente hacia un **[[Vértice Adyacente]]** (el vértice conectado por el mismo lado o arista del poliedro).

- **Movimiento a Vértices Adyacentes:** El algoritmo no salta a cualquier lado; se mueve exclusivamente por los lados del poliedro hacia un [[Vértice Adyacente]].


- **Resumen:** El profesor explicó que el método usa dos criterios estrictos para este desplazamiento:
	- **Criterio de Dirección:** Analiza qué variable otorga el mayor incremento a la [[Función Objetivo]] ($Z$) por unidad producida para elegir sobre qué eje moverse.

	- **Criterio de Parada (El Freno):** Calcula hasta dónde puede avanzar sobre ese eje sin salirse de la región válida.
![[{3F0B1F00-F294-45B4-9FBA-55BA87C737FE}.png]]
> [!danger] ZONA DE PELIGRO: Salirse de la Región Factible El profesor explica gráficamente la trampa matemática del límite. El algoritmo debe calcular hasta dónde avanzar sobre el eje. Si avanza de más, la [[Variable de Holgura]] de la restricción cruzada se vuelve negativa, transformando el punto en una [[Solución Básica No Factible]].
    
- **El Intercambio Algebraico:** Al llegar al nuevo vértice, una variable que valía cero pasa a ser positiva, y una variable que era positiva (holgura) pasa obligatoriamente a valer cero.


### 4. 🛑 Convergencia y Límite de Pasos (1:13:57 - 1:16:22)

- **Bucle de Evaluación:** En el nuevo vértice, vuelve a preguntar: ¿Es óptima? Si la respuesta es sí, termina. Si es no, busca el siguiente [[Vértice Adyacente]].
- **Finitud del Algoritmo:**
	- El profesor abordó una duda conceptual clave: ¿El algoritmo podría quedarse iterando para siempre? La respuesta teórica es no, porque el número de vértices es finito.

- **Resumen:** El método salta de una [[Solución Factible Básica]] a otra sin repetir vértices. El profesor explicó que la cantidad máxima de soluciones básicas está rígidamente acotada por la fórmula del número combinatorio.

> [!note] Fórmula de Cota Superior y Rendimiento Real El techo máximo matemático se define como: $$ C = \frac{n!}{m!(n-m)!} $$ Sin embargo, el profesor aclaró un dato avanzado: en la práctica investigativa, el algoritmo rara vez explora todos esos puntos y suele encontrar el óptimo en una cantidad promedio de **$3m$ pasos** (donde $m$ es el número de restricciones).

---


### 5. 🧮 Vínculo Matemático y Cierre (1:16:22 - 1:24:46)
El último gran tema fue la revelación de la herramienta matemática que hace posible el movimiento entre vértices analizado gráficamente.

- **El Motor Algebraico:** El profesor confirmó que, en la Fase 2 (iterativa), el algoritmo Simplex utiliza una operatoria matricial que es prácticamente idéntica al método de **[[Gauss-Jordan]]**. Cada salto de vértice equivale a realizar operaciones elementales de fila en un sistema de ecuaciones para anular una variable y hacer aparecer otra.

> [!tip] Directiva Innegociable para el Práctico El profesor dio una instrucción estricta de estudio: antes de la próxima clase práctica de Simplex, es **obligatorio** repasar el Capítulo 12 del libro referido a la resolución de sistemas mediante [[Gauss-Jordan]]. Si no dominas las operaciones elementales de fila, "se les va a hacer una bola de nieve" y no entenderán la mecánica de la tabla Simplex.

### 📊 DIAGRAMA DE FLUJO (Resumen de la Lógica del Profesor)

```
graph TD
    A(Inicio: Fase 1) --> B(Identificar Solucion Factible Basica Inicial)
    B --> C(Fase 2: Evaluar Optimidad)
    C --> D{¿Es la solucion Optima?}
    D -->|Si| E(Fin del Procedimiento)
    D -->|No| F(Buscar Vertice Adyacente)
    F --> G(Criterio de Direccion: Mayor incremento de Z)
    G --> H(Criterio de Parada: Evitar Variables Negativas)
    H --> I(Realizar intercambio algebraico con Gauss-Jordan)
    I --> C
```

# ----dudas y pregs-
¡Entendido! Como tu Tutor Académico de Élite, he analizado la transcripción aplicando tácticas de ingeniería inversa para detectar exactamente dónde el profesor levantó la voz, qué temas marcó como obligatorios y cuáles fueron las dudas logísticas o conceptuales de tus compañeros.

Aquí tienes el reporte de alertas de la clase:

# 🚨 RADAR DE PARCIAL: Énfasis y Directivas Obligatorias del Profesor

El profesor no hizo un énfasis tradicional de "esto va al parcial", sino que lanzó **dos advertencias de supervivencia** para poder aprobar las próximas evaluaciones de [[Programación Lineal]].

> [!danger] ZONA DE PELIGRO: El Efecto "Bola de Nieve" El profesor fue extremadamente enfático (hasta el punto de pedir testimonios de alumnos recursantes) advirtiendo que las primeras unidades están "muy encadenadas entre sí".
> 
> - **La advertencia:** Si no estudias los conceptos básicos ahora, no entenderás el [[Método Simplex]]; si no entiendes Simplex, fracasarás en [[Dualidad]] y [[Análisis de Sensibilidad]]. Declaró explícitamente: _"si no le dedican un poco de tiempo se les va a hacer una bola de nieve... les va a ser muy difícil lograr la aprobación directa"_.

> [!tip] DIRECTIVA INNEGOCIABLE: Repaso de [[Gauss-Jordan]] El profesor indicó que el núcleo algebraico iterativo del [[Método Simplex]] es casi idéntico al método de resolución de sistemas de ecuaciones de Gauss.
> 
> - **Tarea obligatoria:** Exigió ir al Capítulo 12 del libro (Repaso de solución de sistemas de ecuaciones) y dominar las [[Operaciones Elementales de Fila]] antes de la próxima clase. Advirtió que, si recuerdan cómo usar esta herramienta, Simplex les resultará _"bastante bastante simple"_; si no, será un problema grave.

Además, dejó como **lectura obligatoria** la sección del libro referida a la _"Interpretación gráfica del método Simplex"_ y exigió ver un video explicativo antes de la siguiente clase práctica _"sí o sí, sin excusas"_.

---

# 🗣️ INTERVENCIONES Y PREGUNTAS DE LOS ALUMNOS

Durante los minutos finales, se abrió un espacio de consultas donde los alumnos plantearon dudas operativas e intervinieron sobre la dinámica de la materia.

> [!question] Pregunta 1: Sobre el material de repaso (Capítulo 12) **Alumno:** _¿Qué del capítulo 12 habría que repasar, que recomendó, perdón?_ **Respuesta del Profesor:** Aclaró que, si bien para la materia en general habrá que repasar estadística (valor esperado, tabla normal), para **este momento exacto** necesitan ir directo a la sección de **sistemas de ecuaciones** y recordar cómo resolver usando [[Gauss-Jordan]]. Remarcó que esto es vital para poder operar matemáticamente en la tabla Simplex.

> [!question] Pregunta 2: Sobre la repetición de clases (Comisiones cruzadas) **Alumno (de la comisión 3K3):** _¿La clase teórica del miércoles va a ser exactamente igual a esta?_ **Respuesta del Profesor:** _Exactamente así._ Confirmó que si el alumno ya asistió a esta explicación y completó el cuestionario, no hace falta que se conecte a la clase del miércoles.

> [!question] Pregunta 3: Confusión sobre un "Entregable" en el Aula Virtual **Alumno:** _Hay una entrega que aparece como pendiente llamada "clase virtual repaso del concepto básico y método gráfico"... ¿Hay que entregar algo?_ **Respuesta del Profesor:** Aclaró que **no hay que entregar nada**. Explicó que hubo un error de configuración en el aula virtual: otra profesora subió un video explicativo utilizando el recurso de "Tarea" (que genera una fecha de entrega) en lugar del recurso "Página". Es simplemente un video para ver.

> [!note] Intervención de Valor: El Testimonio del Alumno Recursante El profesor preguntó si había algún recursante que confirmara su advertencia sobre la dificultad de la materia. Un alumno (Facundo) tomó la palabra y confirmó la trampa de la procrastinación:
> 
> - **Alumno:** _"...no le di mucha bola de verdad y nada, como quise agarrarla se me complicó bastante... si lo dejás para una semana con él es medio complicado."_
> - **Profesor:** Validó el comentario, reiterando que _"las dudas te van a surgir al final"_ si no se lleva la lectura del libro al día.