¡Hola! Como tu Tutor Académico de Élite, he analizado detalladamente la transcripción de tu clase sobre formulación de modelos y he estructurado este índice cronológico.

Esta sesión fue sumamente práctica y la profesora se enfocó en desarrollar tu capacidad analítica a través de tres problemas con niveles de dificultad incremental. He diseñado este "esqueleto" utilizando sintaxis estricta, elementos visuales y enlaces [[Zettelkasten]] para maximizar tu retención de cara a los exámenes.

---

# Índice Cronológico de la Clase: Formulación Práctica en [[Programación Lineal]]


## 2. Modelización Básica: Problema 5 "Inversión en Acciones" (10:13 - 35:26)

[[✅Problema 1.5]]

Se aborda el primer ejercicio práctico: invertir 1 millón de pesos en acciones tipo A y tipo B, maximizando el rendimiento anual.

- **Identificación del Objetivo:** Maximizar el rendimiento del dinero invertido.
- **Definición de las [[Variables de Decisión]]:**
    - _El problema de los datos:_ No se conoce el precio unitario de cada acción, por lo tanto, no se pueden contar físicamente.
    - _Solución:_ Se definen en unidad monetaria como "Pesos a invertir en la acción tipo A" ($x_1$).
- **Notación de Variables:**
    - **[[Definición por Extensión]]:** Enumerar cada variable ($x_1, x_2$).
    - **[[Definición por Comprensión]]:** Usar notación general (Ej: $x_i = $ pesos a invertir en la acción tipo $i$, para $i=1, 2$).

> [!danger] Trampa de Definición (El uso de "Cantidad") La profesora corrigió un error conceptual gravísimo y frecuente: definir la variable usando la palabra "cantidad" (Ej: "Cantidad de acciones" o "Cantidad de dinero"). La palabra "cantidad" **no es una unidad de medida**. Se debe usar la unidad física o monetaria exacta ("Pesos", "Unidades", "Litros") para garantizar la coherencia del modelo.

> [!note] Fórmula: Modelo Matemático (Problema 5) **[[Función Objetivo]]:** $$Max Z = 0.30 x_1 + 0.10 x_2$$ **[[Restricciones]]:** $x_1 + x_2 \le 1000$ (Capital disponible en miles) $x_1 \le 600$ (Máximo en A) $x_2 \ge 200$ (Mínimo en B) $x_1 - x_2 \ge 0$ (Condición: A por lo menos igual a B) $x_1, x_2 \ge 0$ ([[Condición de No Negatividad]]).

---

## 3. Formulación Intermedia: Problema 12 "Constructor de Viviendas" (35:26 - 58:44)
[[✅Problema 1.12]]
Aumenta la complejidad con un problema de construcción de casas prefabricadas (1 y 2 dormitorios), donde se introducen proporciones.

- **Cálculo del Beneficio:** El objetivo es maximizar el beneficio, el cual se calcula restando el costo al precio de venta para cada tipo de vivienda.
- **[[Restricciones Proporcionales]]:** Cómo expresar que las casas de 1 dormitorio deben ser "por lo menos el 25% del total fabricado".
    - _Planteo lógico:_ $x_1 \ge 0.25 (x_1 + x_2)$.
- **Estandarización del Modelo:** La profesora indica que, para resolver el modelo posteriormente (mediante software o el [[Método Simplex]]), se debe aplicar propiedad distributiva y pasar todas las variables al lado izquierdo, dejando solo las constantes a la derecha.

> [!question] Pregunta de Clase: Mezcla de Unidades Un alumno preguntó si era correcto tener en una misma restricción "dinero" y "unidades de casa". _Respuesta de la Profesora:_ Explicó el [[Análisis Dimensional]]. Al multiplicar el coeficiente de costo (medido en $Pesos / Unidad$) por la variable de decisión (medida en $Unidades$), las unidades físicas se simplifican. El resultado neto queda en $Pesos$, lo cual es matemáticamente coherente con el límite de presupuesto.

---

## 4. Desafío Productivo Complejo: Problema "Fruits SA" (58:44 - 1:24:10)
[[▶️Problema 2.31]]

Se plantea un problema de destilación de jugos concentrados (Arándanos y Frambuesas) para introducir conceptos reales de manufactura.

- **Punto Crítico 1: [[Mermas]] y Rendimiento**
    - Al destilar, se pierde agua (35% en arándanos y 25% en frambuesas).
    - Si la variable se define como "Litros de pulpa a procesar" (Input), en la [[Función Objetivo]] se debe multiplicar por $0.65$ y $0.75$ respectivamente para reflejar el volumen real de concentrado que se va a vender.
- **Punto Crítico 2: [[Velocidad de Procesamiento]] vs. Disponibilidad**
    - La máquina procesa 60 litros por hora, pero el límite semanal es de 30 horas.

> [!tip] Metodología de Formulación (Inversión de Tasas) Cuando el recurso disponible (lado derecho) está medido en "Horas", los coeficientes de las variables deben ser "Horas por unidad". Para lograr esto, se debe invertir la velocidad de la máquina ($1 / Velocidad$). _Ejemplo:_ Si procesa 60 litros en 1 hora, demora $1/60$ horas por litro.

### Flujo Metodológico de Formulación de Restricciones

```
graph TD
    A[Identificar Límite del Recurso en Lado Derecho] --> B{¿En qué unidad está medido?}
    B -- Horas de Máquina --> C[El coeficiente debe ser: Horas / Unidad]
    C --> D[Invertir velocidad: 1 / Velocidad de procesamiento]
    B -- Dinero o Presupuesto --> E[El coeficiente debe ser: Costo Unitario]
    B -- Volumen Físico --> F[Aplicar factor de rendimiento o Merma]
```

_Conceptos relacionados:_ [[Restricciones]], [[Análisis Dimensional]], [[Lado Derecho]].

---



## 6. Revisión Final y Nomenclatura Avanzada (1:46:11 - 1:49:36)

La profesora proyecta la formulación correcta del problema de jugos y entrega un consejo final de modelado profesional.

- **Variables Nemotécnicas:** Recomienda dejar de usar las genéricas $x_1, x_2$ en modelos complejos y reemplazarlas por letras representativas (Ej: $PA$ para Pulpa de Arándano, $PF$ para Pulpa de Frambuesa). Esto facilita enormemente la lectura humana al momento de interpretar los resultados.

### Resumen Comparativo de los Modelos Analizados

|Aspecto del Modelo|Inversión (Problema 5)|Viviendas (Problema 12)|Fruits SA (Jugos)|
|:--|:--|:--|:--|
|**Meta del Decisor**|Maximizar Rendimiento|Maximizar Beneficio|Maximizar [[Contribución Marginal]]|
|**Unidad de la Variable**|Pesos ($) a invertir|Unidades a construir|Litros de pulpa a procesar|
|**Complejidad Introducida**|Falta de precio unitario|[[Restricciones Proporcionales]]|[[Mermas]] e Inversión de Tasas|

---

## 7. Cierre, Calendario y Próximos Pasos (1:49:36 - 1:54:32)

La sesión finaliza marcando la hoja de ruta para la semana asincrónica.

- **Lecturas Asignadas:** Capítulos del libro de texto sobre formulación y resolución gráfica (Páginas 51 a 68).
- **Ejercicios a Resolver:** Problemas número 6 y 14 de la guía de casos.
- **Próximo Tema:** La siguiente clase se enfocará en el [[Método Gráfico]] para resolver sistemas de inecuaciones de dos variables. Sugiere ver los videos grabados disponibles en la pestaña "Resolución Gráfica" del aula virtual.
-





# ----------------------------------------------Énfasis de la Profesora y "Trampas" Frecuentes en Exámenes

La profesora fue muy clara en señalar metodologías y conceptos teóricos que, de ser ignorados o confundidos, anulan la validez de todo tu [[Modelo Matemático]].

### 1. El Error Crítico de Usar la Palabra "Cantidad"

Este fue el punto de mayor énfasis en la clase, derivado de errores detectados en cuestionarios anteriores.

> [!danger] Trampa de Parcial (Definición de Variables) _"No es lo mismo decir cantidad de sillas que unidades de sillas... cantidad no es una unidad a la cual está medida"_. Definir una variable como "cantidad de dinero a invertir" o "cantidad de acciones" es un error conceptual grave. Siempre debes usar la unidad física o monetaria exacta (Pesos a invertir, Unidades a producir, Litros a procesar) para garantizar la coherencia del [[Análisis Dimensional]].

### 2. La Importancia del Análisis Verbal Previo

La profesora recalcó que no se debe saltar directamente a escribir ecuaciones matemáticas sin antes comprender el enunciado.

> [!tip] Metodología de Formulación _"No subestimen estos pasos de leer y analizar el problema e identificar con palabras qué es lo que tengo, es muy importante y en medida que los problemas se hacen más complicados más importantes se vuelven estos pasos"_. Regla de oro: Siempre escribe el objetivo y las restricciones en lenguaje verbal antes de traducirlos a funciones.

### 3. Diferencia Teórica: "Positivo" vs. "No Negativo"

Al momento de plantear el cierre del modelo matemático, se hizo hincapié en una confusión teórica recurrente:

> [!danger] Confusión Frecuente _"Recuerden por favor que no negatividad quiere decir mayor o igual a 0, no quiere decir positivo, recuerden la diferencia"_. Exigir que una variable sea estrictamente positiva ($> 0$) excluye el valor cero, lo cual alteraría el conjunto de soluciones factibles y los teoremas fundamentales de la [[Programación Lineal]].

---

# Consultas Relevantes de los Alumnos en Clase

La dinámica de taller permitió que los estudiantes plantearan dudas que aplican a casi cualquier problema complejo. Aquí tienes el resumen estructurado de las consultas y las respuestas académicas:

> [!question] Pregunta 1: Definición de Variables sin Precio Unitario (Problema 5) **Alumno:** Al definir las variables para el problema de inversiones, un alumno propuso "cantidad de acciones a comprar". **Respuesta de la Profesora:** Lo corrigió explicando que el enunciado **no daba el precio de cada acción**. Al no tener el precio, no se puede calcular el rendimiento del 30% sobre "una acción física". La profesora indicó que el rendimiento se calcula sobre el dinero invertido, por lo tanto, la variable correcta era _"pesos invertidos en la acción tipo A"_.

> [!question] Pregunta 2: Estructura de las Restricciones para Resolver **Alumno:** Al ver la restricción de que las casas de 1 dormitorio sean el 25% del total ($x_1 \ge 0.25(x_1 + x_2)$), un alumno consultó: _"¿Si la tendríamos que presentar con constantes a la derecha y variables a la izquierda?"_. **Respuesta de la Profesora:** Aclaró una doble metodología. Para **formular** el modelo y que el corrector lo entienda, es perfecto dejarlo expresado lógicamente. Pero, advirtió que para **resolver** el modelo matemáticamente después (mediante software o el [[Método Simplex]]), sí o sí se debe aplicar propiedad distributiva y pasar todas las variables a la izquierda, dejando un cero o constante en el [[Lado Derecho]].

> [!question] Pregunta 3: Confusión con el [[Análisis Dimensional]] **Alumno:** _"¿Siempre vamos a estar trabajando con dos tipos de unidades? Por ejemplo dinero y unidades de casa en una misma restricción..."_. Al alumno le generaba ruido visual mezclar "pesos" y "casas" en la misma inecuación. **Respuesta de la Profesora (y otro alumno):** Explicaron el mecanismo matemático de simplificación. Al multiplicar el costo ($Pesos/Casa$) por la variable ($Casas$), las unidades de "casa" se simplifican. El resultado neto queda en $Pesos$, lo cual es matemáticamente coherente con el límite de presupuesto (6 millones de pesos).

Para comprender mejor la explicación de la Pregunta 3, visualiza el siguiente esquema de simplificación de unidades:

```
graph LR
    A[Coeficiente de Costo] -->|Pesos / Unidades de Vivienda| C(Multiplicacion)
    B[Variable de Decision] -->|Unidades de Vivienda| C
    C --> D[Simplificacion de Unidades Fisicas]
    D --> E[Resultado Neto en Pesos]
    E -.->|Debe coincidir dimensionalmente con| F[Lado Derecho de la Restriccion en Pesos]
```

_Conceptos relacionados:_ [[Análisis Dimensional]], [[Lado Derecho]], [[Variables de Decisión]], [[Restricciones]].

> [!question] Pregunta 4: Incompatibilidad de Velocidad vs. Tiempo (Fruits SA) **Alumno:** En el problema de la destiladora, los alumnos se trabaron al ver que la máquina procesaba "60 litros por hora", pero el límite total de la máquina era de "30 horas". **Respuesta de la Profesora:** Explicó que no se podían mezclar litros con horas directamente. Como el límite está en horas, introdujo la necesidad de invertir la tasa para calcular _"cuánto tiempo demora en un litro"_. Así, se concluyó que demora $1/60$ horas por litro, unificando las unidades de la ecuación.

> [!note] Fórmula: Inversión de Velocidad de Procesamiento Si el recurso disponible está en horas, el coeficiente de la variable se calcula como: $$Coeficiente = \frac{1}{Velocidad~de~Procesamiento}$$ _Ejemplo: $\frac{1}{60}x_1$ horas._

> [!question] Pregunta 5: Temporalidad de las Restricciones de Capacidad **Alumno:** Durante el cuestionario, un alumno notó que una pregunta sobre los tanques de enfriamiento (650 litros) no especificaba si era un límite semanal o mensual, y no sabía cómo responder. **Respuesta de la Profesora:** Instruyó a los alumnos a analizar el "período de análisis" del sistema general. Dado que la máquina destiladora opera con una restricción explícita de "30 horas a la semana", todo el lote de producción y la capacidad de los tanques se debe considerar evaluado dentro de ese mismo bloque de tiempo (semanal).

### Síntesis de Correcciones Metodológicas

|Error / Duda del Alumno|Problema Analizado|Corrección Teórica Aplicada por la Profesora|
|:--|:--|:--|
|Definir como "Cantidad de acciones"|Inversiones (Prob. 5)|Modificar a **Unidad Monetaria** (Pesos a invertir) ante la falta de precio unitario.|
|Dejar variables a la derecha al resolver|Viviendas (Prob. 12)|**Estandarizar** la ecuación pasando todo término con [[Variables de Decisión]] al lado izquierdo.|
|Multiplicar "Litros/Hora" frente a un límite de "Horas"|Jugos Concentrados (Fruits SA)|Aplicar **Inversión de Tasa** para obtener un coeficiente en "Horas/Litro" que respete el [[Análisis Dimensional]].|
