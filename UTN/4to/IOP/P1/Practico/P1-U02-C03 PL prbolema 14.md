¡Hola! Como tu Tutor Académico de Élite, he estructurado el índice cronológico de esta clase práctica enfocada en la formulación avanzada de modelos de [[Programación Lineal]].

En esta sesión, la profesora trabajó con el **Problema 6 (Modelo de Transporte)** y el **Problema 14**, introduciendo el concepto de equilibrio artificial y analizando rigurosamente los errores más comunes de los alumnos en el aula virtual.

A continuación, te presento el esquema detallado con los enfoques técnicos y "trampas" de examen marcadas para tu estudio.

---

# Índice Cronológico de la Clase: [[Modelo de Transporte]] y Formulación de [[Programación Lineal]]

## 1. Introducción y Metodología de Estudio (0:00 - 8:41)

La clase inició con una advertencia metodológica muy clara: no se puede estandarizar una única forma de modelar en la [[Programación Lineal]]. Cada situación industrial o de servicios requiere un análisis particular.

- **El desafío de la Modelización:** Se advierte que no todos los problemas son iguales y no se puede estandarizar una única forma de modelar.
**La clave del éxito:** La profesora recomendó resolver tantos problemas diferentes como sea posible. Al hacerlo, tu cerebro construye un "registro de situaciones", lo que te permitirá identificar patrones rápidamente cuando te enfrentes a un escenario completamente nuevo en el parcial.

> [!tip] Tip Metodológico del Profesor La única forma de dominar el planteo es resolver muchas situaciones diferentes. Al practicar mucho, se adquiere un "registro de situaciones" que permite identificar rápidamente patrones cuando te enfrentas a un problema nuevo en el parcial.


> [!tip] Tip de la Profesora (Afrontar el Parcial) La mejor estrategia no es memorizar, sino enfrentarse a la hoja en blanco e intentar plantear problemas aunque estén "totalmente mal" al principio. Corregir esos errores es lo que realmente afianza la lógica matemática.

## 2. Formulación Compleja: Problema 6 "Energy S.A." (8:41 - 30:39)
[[problema 1.6]]

Se aborda un problema donde tres plantas generadoras de energía deben satisfacer la demanda de cuatro ciudades.

- **Objetivo y Limitaciones:** La meta es minimizar el costo total de envío de los kilowatts. Las limitaciones están dadas por la [[Oferta]] (producción máxima de cada planta) y la [[Demanda]] (consumo de cada ciudad).
- **Definición de Variables Genéricas:** En lugar de enumerar 12 variables, se introduce la [[Definición por Comprensión]].
    - $x_{ij}$: "Cantidad de kilowatts a enviar desde la planta $i$ a la ciudad $j$" (donde $i = 1,2,3$ y $j = 1,2,3,4$).

### El Concepto del [[Problema Desequilibrado]]

Este es el punto técnico más importante de la primera mitad de la clase. Al sumar la capacidad de las plantas ($160$ millones de kW) y compararla con el consumo total requerido ($195$ millones de kW), se observa que la demanda supera a la producción.

- **[[Planta Ficticia]]:** Para que el [[Modelo de Transporte]] pueda resolverse, debe estar estrictamente equilibrado. Se debe agregar una planta inventada (origen ficticio) que "produzca" los 35 millones de kilowatts faltantes.
- **Interpretación de Variables Ficticias:** Las variables asociadas a esta planta ficticia representan en realidad la **demanda insatisfecha** (los kilowatts que la ciudad no va a recibir).
- **Penalización en el Objetivo:** Como estas unidades en realidad no se envían, su costo de transporte en la [[Función Objetivo]] es exactamente $0$.

> [!note] Restricciones de Igualdad Estricta En un [[Modelo de Transporte]] equilibrado, las inecuaciones se transforman en ecuaciones. Las plantas envían exactamente todo lo que producen (incluida la planta ficticia) y las ciudades reciben exactamente todo lo que demandan, formulándose todas las restricciones con el signo de igualdad ($=$).

---

## 3. Actividad Práctica: Problema 14 en el Aula Virtual (30:39 - 1:09:45)

La profesora pausa la exposición y dirige a los estudiantes al Aula Virtual para responder un cuestionario estructurado sobre el planteo del Problema 14 (envasado de productos).

- El objetivo es que los alumnos identifiquen verbalmente el objetivo, las variables y distingan las restricciones antes de armar la matemática.

> [!question] Pregunta de Clase: Diferencia entre Dato y Restricción Un alumno se confundió al marcar como restricción "los minutos que se requieren para envasar el producto". _Respuesta del Profesor:_ Aclaró que eso es un **[[Parámetro]]** (un dato conocido). La verdadera [[Restricción]] limitante es "la disponibilidad máxima de 120 horas de la máquina". Los minutos por envase son simplemente los coeficientes que se usarán para construir la inecuación de las horas de máquina.

---

## 4. Puesta en Común y Análisis de Errores (1:09:45 - 1:48:00)

Al finalizar el tiempo, la profesora revisó las respuestas del cuestionario y corrigió conceptualmente las confusiones más graves.

### A. Diferencia Económica en el Objetivo

Muchos alumnos dudaron si el objetivo era maximizar producción o maximizar ganancias.

- **[[Ingreso Total Neto]]:** La profesora aclaró que el objetivo es maximizar ingresos por venta, no el "Beneficio" ni la "Contribución a las utilidades". Para hablar de [[Beneficio]], el enunciado debería haber proporcionado datos de los costos de producción, los cuales no existen en este problema.

### B. Errores Críticos en la Definición de Variables

Se analizó por qué varias definiciones presentadas en el múltiple choice eran incorrectas, remarcando lo siguiente:

|Definición Incorrecta|Motivo del Error (Justificación del Profesor)|
|:--|:--|
|_Gramos de producto a envasar_|Los gramos ya están definidos por el tipo de envase ($120g, 200g$). Es un dato fijo, no una variable a decidir.|
|_Producto a fabricar semanalmente_|La empresa **no fabrica** el producto, su función operativa es únicamente "envasarlo".|
|_Unidades de envase a producir_|La empresa **no produce los envases** plásticos, ya los tiene disponibles vacíos.|

### C. Coherencia en el [[Análisis Dimensional]]

Al evaluar las restricciones matemáticas, se descartó la opción `120 X1 + 200 X2 + 360 X3 <= 3` porque el lado izquierdo sumaba "Gramos" y el lado derecho establecía un límite de "3 Toneladas". Si se formulan coeficientes en gramos, el lado derecho debe ser $3,000,000$ de gramos (o convertir todo a kilos).

### D. Modificación del Modelo: Comprar Envases (Inciso B)

Se planteó un ensayo: ¿Qué hacer si un proveedor ofrece vender envases de $120g$ a $1$ cada uno?.

```
graph TD
    A[Nuevo Escenario: Comprar Envases Adicionales] --> B[Crear Nueva Variable de Decision]
    B --> C[X4 = Cantidad de envases vacios de 120g a comprar]
    C --> D[Modificar Restriccion Física]
    D --> E[Sumar X4 al limite original de 3000 envases disponibles]
    C --> F[Modificar Funcion Objetivo]
    F --> G[Restar el costo de 1 peso por X4 a los Ingresos Netos]
```

_Conceptos relacionados:_ [[Variable de Decisión]], [[Función Objetivo]], [[Restricciones]].

> [!note] Fórmula: Impacto del Costo en Z Como la compra de envases representa un costo que afecta al ingreso total, la variable $x_4$ debe restarse en la función a optimizar. $$Max Z = (\dots Ingresos \dots) - 1 \cdot x_4$$

---

## 5. Clasificación Final del Modelo (1:48:00 - Fin)

La sesión concluye respondiendo la última pregunta teórica del cuestionario sobre la clasificación del problema resultante.

- **[[Forma Mixta]]:** El modelo formulado es explícito mixto debido a que conviven en el mismo sistema restricciones con el signo $\le$ (disponibilidad de horas y recursos) y restricciones con el signo $\ge$ (demanda mínima comprometida con el supermercado).


# ----


### 3. Diferenciación Estructural: Errores Comunes de Planteo

A través del "Problema 14" (envasado de productos) abordado en el cuestionario del aula virtual, la profesora corrigió varios errores conceptuales frecuentes entre los alumnos:

- **Ingreso vs. Beneficio:** Muchos alumnos indicaron que la meta era maximizar "Beneficios". La profesora corrigió que era maximizar **[[Ingresos Netos]]**, ya que el problema carecía de información sobre los costos de producción. El beneficio se calcula estrictamente como Ingresos menos Costos.
- **[[Dato]] vs. [[Restricción]]:** Los minutos que demora la máquina en envasar un producto (Ej: $1~minuto$) son parámetros (datos conocidos) que acompañan a la variable. La verdadera limitación del sistema son las horas disponibles totales que tiene la máquina para trabajar.
- **[[Análisis Dimensional]]:** Se invalidó una restricción propuesta ($120 x_1 + 200 x_2 + 360 x_3 \le 3$) porque el lado izquierdo sumaba "Gramos" y el límite derecho ("3") representaba "Toneladas". Para ser correcta, el límite derecho debía expresar la disponibilidad en la misma unidad ($3,000,000$ de gramos).

> [!danger] Trampa de Definición de Variable Al igual que en clases anteriores, definir la variable como "gramos a envasar" fue catalogado como error grave. Los gramos por envase son un dato fijo ($120g, 200g$). La verdadera incógnita son las "unidades de envases a rellenar".

---

### 4. Modificación de Modelos: Incorporar un Nuevo Escenario (Inciso B)

El último tema importante consistió en evaluar cómo reacciona un [[Modelo Matemático]] base cuando el entorno cambia. El ensayo proponía que un proveedor ofrecía vender envases vacíos extra a $1 cada uno.

- **Metodología de Adaptación:** La profesora indicó que no se trata de "borrar" las restricciones originales, sino de expandir el sistema matemático.

Para lograr esto, se deben ejecutar tres pasos estrictos sobre el modelo formulado:

|Paso del Ajuste|Acción a realizar en el [[Modelo Matemático]]|
|:--|:--|
|**1. Variables**|Crear una nueva variable $x_4$ (Cantidad de envases vacíos a comprar).|
|**2. Restricciones**|Sumar $x_4$ en el lado izquierdo de la ecuación de disponibilidad física de envases.|
|**3. [[Función Objetivo]]**|Restar el costo de adquisición ($1 \cdot x_4$) a los ingresos totales proyectados.|

> [!question] Pregunta de Clase: ¿Cómo sé si me conviene comprar? Un alumno preguntó cómo hacer para saber matemáticamente si la propuesta es rentable. _Respuesta de la Profesora:_ Explicó que no es necesario pre-calcularlo mentalmente. Solo debes incrustar la nueva variable ($x_4$) y su costo en el modelo. Al resolverlo, el sistema dictaminará por sí solo la cantidad óptima a comprar, si es que conviene.



# --------------------------- dudas y pregs
¡Hola! Como tu Tutor Académico de Élite, he analizado rigurosamente la transcripción de tu última clase. Esta sesión fue fundamental, ya que la profesora no solo introdujo temas nuevos, sino que dedicó gran parte del tiempo a corregir **errores conceptuales graves** (las clásicas "trampas" de examen) a través de las dudas que plantearon tus compañeros.

A continuación, te estructuro los énfasis del profesor y las preguntas más relevantes de la clase, aplicando nuestra metodología de estudio.

---

## Énfasis de la Profesora y "Trampas" Metodológicas

La profesora fue muy enfática en advertir sobre las falencias críticas al momento de plantear un [[Modelo de Programación Lineal]]. Si el planteo inicial está mal, todo el ejercicio será considerado incorrecto.

### 1. El "Registro de Situaciones" (Importancia de la Práctica)

La profesora remarcó que **no se puede estandarizar una única forma de modelar**, ya que cada situación es diferente.

> [!tip] Tip de Estudio y Examen El profesor indicó que la única forma de dominar los planteos es hacer mucha ejercitación. Al resolver múltiples escenarios, el alumno genera un "registro de situaciones" mental que le permitirá identificar rápidamente cómo estructurar restricciones ante un problema completamente nuevo en el parcial.

### 2. El Error Fatal: Confundir un [[Dato]] con una [[Restricción]]

Al revisar el cuestionario, se detuvo a explicar una confusión generalizada. Los alumnos marcaban los "minutos que demora la máquina" como una restricción.

> [!danger] Trampa de Parcial: Parámetros vs. Limitaciones La profesora enfatizó que el tiempo unitario (ej. 1 minuto por envase) es un **[[Parámetro]]** o dato conocido. La verdadera [[Restricción Limitante]] es la **disponibilidad total** de ese recurso (las 120 horas semanales de la máquina).

### 3. Rigurosidad en la Definición de [[Variables de Decisión]]

Volvió a hacer hincapié en que definir variables de forma difusa arruina el modelo. Rechazó definiciones como "producto a fabricar semanalmente" o "gramos a envasar".

- **Motivo 1:** La empresa no "fabrica", solo "envasa".
- **Motivo 2:** Los gramos ya son un dato fijo del envase, no son la incógnita a decidir.
- **Motivo 3:** Faltaba especificar la unidad de medida exacta.

---

# Consultas Relevantes de los Alumnos en Clase

La interacción en esta clase fue altísima. Los alumnos plantearon dudas excepcionales que sirvieron para destrabar confusiones clásicas en la [[Programación Lineal]]. Aquí te presento el resumen de cada intercambio clave:

> [!question] Pregunta 1: Signo de la Restricción de Demanda (Problema 6) **Alumno:** Al ver que una ciudad tiene un "pico de consumo máximo" a las 2 PM, preguntó: _"¿No tendría que ser menor o igual ($\le$) en la restricción 3 porque es su pico máximo?"_. **Respuesta del Profesor:** Aclaró que **NO**. En un [[Modelo de Transporte]] equilibrado artificialmente, todas las restricciones son de igualdad estricta ($=$). La ciudad necesita recibir exactamente esos 45 millones de kilowatts. Si no se le pueden enviar físicamente, la diferencia será cubierta por la variable de la [[Planta Ficticia]], la cual registrará matemáticamente la demanda insatisfecha.

> [!question] Pregunta 2: Objetivo Económico (Beneficio vs. Ingreso) **Alumno:** En el Problema 14, un estudiante dudaba si la meta era maximizar la producción o el beneficio, argumentando: _"Según yo, una empresa desea planificar la producción..."_. **Respuesta del Profesor:** Le corrigió indicando que "planificar la producción" es lo que se busca hacer físicamente, pero el **objetivo económico** detrás de eso es maximizar el **[[Ingreso Neto]]**. Explicó enfáticamente que **no se puede hablar de [[Beneficio]]** porque el enunciado no proporciona ningún dato sobre los costos de producción.

> [!question] Pregunta 3: ¿Cómo se relaciona el [[Parámetro]] con la [[Restricción]]? **Alumno:** _"Si bien se distingue cuál es el dato y cuál es la restricción, ¿ese dato se corresponde con las restricciones?"_. **Respuesta del Profesor:** Confirmó que sí. Explicó que los minutos requeridos por cada producto (el parámetro) son los coeficientes tecnológicos que se multiplicarán por las variables para construir la inecuación que limitará el uso de las 120 horas de la máquina (la restricción).

> [!question] Pregunta 4: Simulación de Compra en el [[Modelo Matemático]] (Inciso B) **Alumno:** Al plantear el escenario donde un proveedor ofrece envases vacíos a $$1$, un estudiante propuso: _"Yo calcularía $Z$ con el modelo actual, y después calcularía un $Z$ haciendo una simulación restándole $$200$ si compro 200 unidades, modificando el límite a 3200..."_. **Respuesta del Profesor:** Le indicó que esa lógica es para hacerlo "a mano", pero el objetivo de la materia es que **el modelo resuelva el problema por sí solo**. La estrategia correcta es crear una nueva [[Variable de Decisión]] ($x_4$: envases a comprar) e incrustarla en el sistema.

### Síntesis Visual: Adaptación del Modelo (Respuesta a la Pregunta 4)

A partir de la corrección del profesor al alumno sobre cómo agregar la compra de envases, este es el flujo de impacto en el sistema de ecuaciones:

```
graph TD
    A[Nueva Variable: X4 = Envases a comprar a 1 peso] --> B[Impacto en Restricciones Físicas]
    A --> C[Impacto en la Meta Económica]
    B --> D[Se suma X4 al límite original de envases disponibles]
    C --> E[Se resta el costo unitario de 1 peso por X4 a los Ingresos]
    E -.-> F[La nueva Funcion Objetivo determinará si la compra es rentable]
```

_Conceptos relacionados:_ [[Variable de Decisión]], [[Restricciones Físicas]], [[Función Objetivo]], [[Ingreso Neto]].

> [!note] Fórmula de Adaptación de la Función Objetivo ($Z$) Tras la explicación de la profesora, la nueva meta se estructura así para reflejar el costo de adquisición: $$Max Z = (\dots Ingresos \dots) - 1 \cdot x_4$$ _(El coeficiente 1 representa el costo unitario del nuevo envase vacío)_.

### Tabla Resumen: Clasificación de Errores Vistos en Clase

|Concepto Erróneo del Alumno|Corrección del Profesor|Concepto Teórico Aplicado|
|:--|:--|:--|
|Usar signo $\le$ en demanda de transporte.|Se usa $=$ porque el modelo está equilibrado mediante variables ficticias.|[[Modelo de Transporte]], [[Planta Ficticia]]|
|Marcar el "tiempo de envasado" como restricción.|Es un dato que acompaña a la variable. La restricción es el tiempo total de la máquina.|[[Parámetro]], [[Restricción Limitante]]|
|Definir el objetivo como "Maximizar Beneficio".|Se maximizan Ingresos, ya que no hay datos de costos para calcular beneficios.|[[Ingreso Neto]], [[Beneficio]]|