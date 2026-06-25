https://www.youtube.com/watch?v=aarVED0n18k&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=12


### 1. 📢 Repaso Algorítmico y Estandarización (0:00 - 12:00)

El profesor inicia la clase recordando los pasos universales del [[Método Simplex]] antes de abordar el ejercicio 18 (un problema de minimización).

- **Vector de Términos Independientes ($P_0$):** Reitera que si hay un valor negativo del lado derecho, se debe multiplicar por $-1$, invirtiendo el signo de la inecuación.
- **Transformación a [[Forma Estándar]]:** Para convertir inecuaciones a ecuaciones, se deben incorporar las **[[Variables de Holgura]]**.
    - Restricción de $=$ : No se agrega nada.
    - Restricción de $\geq$ : Se agrega restando (coeficiente $-1$).
    - Restricción de $\leq$ : Se agrega sumando (coeficiente $+1$).
- **Condición de Variables:** En la función objetivo, las holguras llevan coeficiente $0$. En la [[Restricción de No Negatividad]], **todas** deben ser $\geq 0$.
---
El primer gran tema fue la modificación de las reglas iterativas del [[Método Simplex]] cuando el objetivo es reducir costos. El profesor enfatizó que la estructura de la tabla es la misma, pero la toma de decisiones numéricas se invierte en la fila de control de $C_j - Z_j$.

> [!note] Reglas de Iteración para Minimización
> 
> - **Criterio de Optimidad (Parada):** Se alcanza la [[Solución Óptima]] cuando todos los valores en la fila $C_j - Z_j$ son **ceros o positivos** ($\geq 0$).
> - **[[Variable que Entra]]:** Si hay valores negativos (solución no óptima), ingresa a la base la variable que posea el valor negativo **mayor en valor absoluto** (es decir, "el más negativo").
> - **[[Variable que Sale]]:** Esta regla **NO CAMBIA** respecto a maximización. Se sigue calculando el menor [[Cociente Tita]] ($\theta$) entre $P_0$ y la columna entrante, descartando denominadores negativos o nulos.

### 2. 🛠️ Construcción de la Base y [[Variables Artificiales]] (12:00 - 18:50)

El profesor explicó que, al pasar el modelo a su [[Forma Estándar]], algunas restricciones (como las de $\geq$ o $=$) no aportan los vectores unitarios necesarios para armar la [[Matriz Identidad]] inicial

- **El Problema:** Al estandarizar, solo se encontraron 2 vectores unitarios ($x_3$ y $S_2$), faltando el vector $(1,0,0)$.
- **El Artilugio Matemático:** Se inventa y agrega una **[[Variable Artificial]]** ($A_1$) exclusivamente en la fila donde falta el vector unitario.
- **Penalización (Método de la Gran M):** Como la variable no existe en la realidad, el algoritmo debe ser forzado a expulsarla. En minimización, se agrega a la función objetivo sumando ($+M$), donde $M$ representa un coeficiente positivo infinitamente grande.

> [!danger] ZONA DE PELIGRO: El Exceso de Artificiales El profesor consideró un "error conceptual grave" agregar variables artificiales en filas que ya poseen su [[Vector Unitario]] (como la de $\geq$ si ya otra variable provee el vector). Declaró: _"es incorrecto agregar en la segunda restricción porque yo tengo ya por la base... el vector unitario. ¿Para qué voy a agregar una variable inventada? Es una iteración más del Simplex"_.



### 3. 🔄 Iteración: Criterios para [[Minimización]] (18:50 - 29:00)

Una vez armada la tabla, el profesor establece las reglas matemáticas invertidas para resolver el problema de mínimo.

| Acción del Algoritmo       | Regla en Problemas de Máximo   | Regla en Problemas de Mínimo (Clase Actual)                                                        |
| :------------------------- | :----------------------------- | :------------------------------------------------------------------------------------------------- |
| **Criterio de Optimidad**  | Todos los $C_j - Z_j \geq 0$   | Todos los **$C_j - Z_j \leq 0$** (es decir, ceros o positivos para estar en el óptimo).            |
| **[[Variable que Entra]]** | El mayor valor positivo.       | El valor **más negativo** (el negativo con mayor valor absoluto).                                  |
| **[[Variable que Sale]]**  | Menor [[Cociente Tita]] ($>0$) | **IDÉNTICO**. Sigue siendo el menor [[Cociente Tita]] entre elementos estrictamente mayores a $0$. |

### 4. 🧮 Operaciones de Fila y Clasificación de la Solución (29:00 - 47:00)

El profesor aplica [[Operaciones Elementales de Fila]] ([[Gauss-Jordan]]) para realizar el intercambio de variables.

- **Eliminación de la Artificial:** Una vez que la [[Variable Artificial]] sale de la base (se hace $0$), cumplió su función. El profesor aclara que su columna puede ser directamente eliminada de las siguientes tablas del Simplex para no confundir.
- **Clasificación del Óptimo:** Al llegar a la tabla donde todos los $C_j - Z_j$ son positivos, se lee la solución. Como había 3 restricciones y quedaron 3 variables estrictamente positivas, clasificó el punto como: **[[Solución Factible Básica No Degenerada]]**.

> [!note] Fórmula del Cociente de Salida Para calcular qué variable abandona la base, el profesor exige la fórmula: $$ \theta = \frac{\text{Vector } P_0}{\text{Vector Columna Entrante}} \quad \text{condición: denominador } > 0 $$

### 5. 📝 Cuestionario en Vivo y Tips de Trinchera (47:00 - 1:20:00)

La clase finaliza con un cuestionario práctico (Ejercicio 6) y un bloque de resolución de dudas críticas.

> [!question] Duda Práctica: ¿Cómo comparar las "M"? **Alumno:** _"¿Qué hacíamos cuando hay 2 M para calcular cuál es más chico o más grande?"_. 
> **Respuesta del Profesor (Tip de Trinchera):** Validó un atajo numérico. Si cuesta trabajar algebraicamente con las $M$ en la fila $C_j - Z_j$, sugirió reemplazar mentalmente la $M$ por un número real muy grande (por ejemplo, $10.000$) y multiplicar. Esto permite ver visualmente y sin error qué número es "más negativo" para saber cuál ingresa a la base.

> [!question] Duda de Modelización: Inecuaciones complejas **Alumno:** _"¿Cómo llevaríamos a la tabla de Simplex una restricción como $X_1 \geq 0.25(X_1+X_2)$?"_. 
> **Respuesta del Profesor:** Aclaró que la inecuación debe ser resuelta algebraicamente **antes** de agregar holguras. Se debe aplicar distributiva del lado derecho, pasar todos los términos con variables al lado izquierdo y agruparlos (ej. restando los coeficientes de $x_1$). Solo cuando queden las variables a la izquierda y un número independiente a la derecha, se estandariza.

---

### 📊 DIAGRAMA DE FLUJO: Simplex de Minimización con Base Artificial

```
graph TD
    A(Inicio: Modelo de Minimización) --> B(Estandarizar agregando Holguras)
    B --> C{¿Se forma la Matriz Identidad completa?}
    C -->|Sí| E(Armar Tabla Inicial Estándar)
    C -->|No| D(Agregar Variable Artificial y +M en Función Objetivo)
    D --> E
    E --> F(Calcular Z_j y C_j - Z_j)
    F --> G{¿Todos los C_j - Z_j son >= 0?}
    G -->|Sí| H(SOLUCIÓN ÓPTIMA)
    G -->|No| I(Entra Variable: El C_j - Z_j más negativo)
    I --> J(Sale Variable: Menor Cociente Tita > 0)
    J --> K(Aplicar Gauss-Jordan)
    K --> F
```

_Conceptos relacionados:_ [[Minimización]], [[Método Simplex]], [[Variables Artificiales]], [[Matriz Identidad]], [[Solución Factible Básica]].



---





# -------------- dudas y pregs
# 🚨 RADAR DE PARCIAL: Énfasis y Advertencias del Profesor

A través del análisis detallado de la transcripción de la clase práctica, he detectado los puntos exactos donde el profesor hizo un énfasis crítico, catalogando ciertos fallos metodológicos como "errores graves" que pueden costar la aprobación de un examen de [[Programación Lineal]].

### 1. La "Trampa" de la Matriz Identidad y el Exceso de Variables

El profesor detuvo la clase para marcar lo que él considera un error conceptual innegociable al armar la tabla inicial del [[Método Simplex]].

> [!danger] ERROR CONCEPTUAL GRAVE: Sobrepoblación Artificial El profesor fue categórico al advertir que agregar una **[[Variable Artificial]]** en una restricción que ya posee un **[[Vector Unitario]]** natural es un fallo crítico. Explicó: _"es incorrecto agregar en la segunda restricción porque yo tengo ya por la base... el vector unitario. ¿Para qué voy a agregar una variable inventada? [...] yo por ejemplo lo considero un error si agregan más variables de las que corresponde porque considero que no están analizando correctamente la matriz de coeficientes"_.

### 2. El Manejo de Inecuaciones vs. Igualdades

> [!danger] ZONA DE PELIGRO: Estandarización a Ciegas El profesor notó que los alumnos automatizan el proceso y cometen el error de agregar una **[[Variable de Holgura]]** a restricciones que ya nacen con el signo de igualdad ($=$). Enfatizó: _"esto es importante porque algunas veces ven les parece que en todas las restricciones hay que agregar variable de holgura pero si yo ya tengo la igualdad ya pierde el objetivo..."_.

### 3. La Naturaleza de las Variables de Holgura

> [!note] Regla de Signos Hizo un énfasis explícito en recordar que, independientemente de si la holgura se agrega sumando (en inecuaciones $\leq$) o restando (en inecuaciones $\geq$), el valor intrínseco de la variable está blindado por la restricción del modelo: _"acá es importante que remarquen que... la variable en sí siempre es 0 o positiva"_.

---

# 🗣️ PREGUNTAS DE LOS ALUMNOS Y RESPUESTAS DEL PROFESOR

La clase tuvo una alta interacción orientada a la operatoria de la tabla y a la modelización matemática previa. Aquí están las intervenciones más relevantes:

### Pregunta 1: La Falsa Apariencia del Vector Unitario

> [!question] Dudas de Concepto en Clase **Alumno:** _"¿Por qué se agrega variable artificial en la primera fila siendo que $X_1$ tiene un 1?"_. **Respuesta del Profesor:** Le aclaró que tener un coeficiente de $1$ no convierte automáticamente a la columna en un **[[Vector Unitario]]**. Le demostró que el vector que acompañaba a esa variable era el $(1, 3)$, y no el vector $(1, 0)$ requerido para armar la base. Si la columna tiene otros números distintos de cero, no sirve como base y se debe inventar la variable artificial.

### Pregunta 2: Confusión entre el Pivot y el Cociente de Salida

> [!question] Dudas del Algoritmo **Alumno:** Al determinar qué variable salía de la base, el alumno se confundió con las **[[Operaciones Elementales de Fila]]**, creyendo que debía dividir la fila por 1 para hacer ceros abajo. _"Pensé que había que dividir o sea la primera fila si había que dividirla por 1 y la de abajo había que hacerla 0"_. **Respuesta del Profesor:** El profesor lo frenó y le recordó que, antes de aplicar Gauss-Jordan, primero se debe calcular el **[[Cociente Tita]]** para determinar la variable saliente. Exigió hacer la división entre el valor actual (solución) y el valor de la variable entrante (ej. $15/1$ y $20/3$), y seleccionar estrictamente el menor de ellos.

### Pregunta 3: El Atajo de la "Gran M"

> [!question] Tip de Parcial Confirmado **Alumno (Recursante):** Recordó un truco de años anteriores y preguntó si seguía siendo válido: _"¿Qué hacíamos cuando hay 2 M para calcular cuál es más chico o más grande? [...] cambiar a M por un valor grande..."_. **Respuesta del Profesor (Tip de Trinchera):** Validó totalmente la técnica.
> 
> > [!tip] La Técnica Numérica Si al alumno le cuesta evaluar algebraicamente la letra $M$ en la fila $C_j - Z_j$, puede asignarle mentalmente un valor enorme (como $10.000$) y multiplicar. Esto permite visualizar inmediatamente qué celda arroja el número "más negativo" para saber qué variable debe ingresar a la base.

### Pregunta 4: Modelización de Inecuaciones con Variables Mezcladas

> [!question] Dudas de Formulación **Alumno:** _"¿Cómo llevaríamos a la tabla de Simplex una restricción como $X_1 \geq 0.25(X_1 + X_2)$?"_. **Respuesta del Profesor:** Dictaminó una regla innegociable de pre-procesamiento matemático. Aclaró que no se puede estandarizar directamente. Se deben seguir estos pasos:
> 
> 1. Resolver el lado derecho aplicando la propiedad distributiva ($0.25 X_1 + 0.25 X_2$).
> 2. Pasar todos los términos con variables al lado izquierdo de la inecuación.
> 3. Agrupar los coeficientes de las variables homólogas (ej. agrupar las $X_1$).
> 4. Una vez que queda la inecuación "limpia" (solo variables a la izquierda y un término independiente a la derecha), recién ahí se agregan las variables de holgura para llevarlo a su **[[Forma Estándar]]**.

---

### 📊 DIAGRAMA DE FLUJO: Lógica de la Variable Artificial Evaluada

Para que no cometas el error que el profesor catalogó como "grave", memoriza este árbol de decisión táctico al momento de armar tu tabla:

```
graph TD
    A(Transformar inecuación a ecuación con Holgura) --> B(Analizar columna de la variable agregada)
    B --> C{¿Se generó un Vector Unitario perfecto?}
    C -->|Sí| D(FIN. Esa variable entra a la base)
    C -->|No| E(Falta Base. Inventar Variable Artificial)
    E --> F(Penalizar con M en la Función Objetivo)
    D --> G(Error de Parcial: Agregar Artificial aquí)
```

_Conceptos relacionados:_ [[Matriz Identidad]], [[Vector Unitario]], [[Variable Artificial]], [[Variable de Holgura]].