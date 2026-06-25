https://www.youtube.com/watch?v=Vz9C3yZWklw&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=10

# 🗓️ ESQUEMA CRONOLÓGICO: SIMPLEX DE MINIMIZACIÓN, BASE ARTIFICIAL Y CASOS ESPECIALES

Esta sesión fue crítica, ya que marcó la transición del algoritmo básico hacia las anomalías y escenarios donde el modelo "se rompe".

Aquí tienes el resumen de cada tema estructurado bajo las métricas de dominio conceptual avanzado.

### 2. 📉 Adaptación del Algoritmo: Simplex para Minimización (6:00 - 12:00)

El profesor explicó cómo operar el algoritmo cuando el objetivo es reducir costos. Aunque mencionó que se puede multiplicar la [[Función Objetivo]] por $-1$ para resolverlo como un caso de maximización, se enfocó en explicar el método nativo adaptando los criterios iterativos para interpretar correctamente la [[Tasa de Crecimiento]].

> [!note] Reglas de Minimización (Inversión de Criterios)
> 
> - **Criterio de Optimidad:** Se alcanza el óptimo cuando todos los valores en la fila $C_j - Z_j$ son **mayores o iguales a cero** ($\geq 0$).
> - **[[Variable que Entra]]:** Ingresa a la base la variable que posea la **menor diferencia negativa** (el valor negativo más alejado del cero, con mayor valor absoluto).
>  **[[Variable que Sale]]:** El cálculo del [[Cociente Tita]] ($\theta$) **no cambia**. Se sigue buscando el cociente mínimo positivo, ya que esto garantiza no salirse de la región factible, independientemente de si se maximiza o minimiza.






### 3. 🛠️ La Técnica de la Base Artificial (12:00 - 22:00)

Este es el procedimiento exigido cuando el modelo no es canónico (contiene restricciones de $\geq$ o $=$) y, al pasarlo a su [[Forma Estándar]], carece de los vectores unitarios necesarios para armar la [[Matriz Identidad]].

Para solucionar esto
- **El Parche Matemático:** Se deben sumar [[Variables Artificiales]] para forzar la creación de la base inicial y poder arrancar la iteración.
- **La Penalización (El Castigo):** Como estas variables no existen en la realidad, el algoritmo debe expulsarlas. Se penalizan en la [[Función Objetivo]] con un coeficiente muy grande ($M$).
    - En Maximización: Se restan ($-M$).
    - En Minimización: Se suman ($+M$).

> [!danger] ZONA DE PELIGRO: Artificiales en la Solución Mientras exista una [[Variable Artificial]] en la base, el punto actual no es una solución de tu problema original. Si el algoritmo detecta que llegaste al óptimo, pero sobrevive una variable artificial con un valor positivo ($>0$), se concluye matemáticamente que el modelo original es un **[[Problema Incompatible]]**.

### 4. 🚨 Los 4 Casos Especiales de la Programación Lineal (22:25 - 36:54)

El profesor dedicó gran parte de la clase a enseñar cómo detectar anomalías tanto en el gráfico como en la matriz. Sugirió explícitamente armar un cuadro resumen para estudiar esto.

| Caso Especial                        | Identificación Gráfica                                                       | Identificación en Tabla [[Método Simplex]]                                                                                        |
| :----------------------------------- | :--------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **[[Problema Incompatible]]**        | No existe intersección válida (No hay [[Poliedro de Soluciones]]).           | Óptimo alcanzado, pero queda una [[Variable Artificial]] en la base con valor $> 0$.                                              |
| **[[Problema No Acotado]]**          | Área abierta **Y** la recta de $Z$ no encuentra límite en su desplazamiento. | La variable que entra tiene todos sus denominadores $\leq 0$ (no se puede calcular el [[Cociente Tita]]).                         |
| **[[Múltiples Soluciones Óptimas]]** | La función $Z$ es paralela a una restricción limitante.                      | En la tabla óptima, una **[[Variable No Básica]]** posee $C_j - Z_j = 0$ (excluyendo casos degenerados).                          |
| **[[Solución Degenerada]]**          | Más de 2 rectas se cruzan en el mismo vértice exacto.                        | Una variable básica toma el valor $0$. Se anticipa si en la iteración previa hubo un **empate** al calcular el [[Cociente Tita]]. |

> [!danger] El Falso Amigo del "Poliedro Abierto" Muchos alumnos asumen que un área abierta es siempre un problema no acotado. ¡Falso! El profesor demostró que un mismo poliedro abierto puede ser **no acotado para maximizar**, pero tener un **óptimo perfecto para minimizar**,.

### 5. 📝 Revisión del Cuestionario y Q&A (37:00 - 1:06:00)

La clase cerró con la corrección de un test en vivo, donde surgieron dudas de lógica abstracta evaluadas por el profesor.

> [!question] Duda de Clase: Conjuntos Vacíos y Soluciones _Alumno:_ Se confundió con la pregunta de teoría abstracta sobre los conjuntos de soluciones. _Respuesta del Profesor:_ Trazó una relación causa-efecto crítica: Si el **conjunto de soluciones óptimas es vacío** (no hay óptimo), solo puede ser por dos motivos:
> 
> 1. El conjunto de soluciones factibles también es vacío (Problema Incompatible).
> 2. El conjunto de soluciones factibles tiene infinitos elementos (Problema No Acotado).

---
A través de un cuestionario interactivo, el profesor cerró la clase evaluando la lógica abstracta que conecta a las [[Soluciones Factibles]] con las [[Soluciones Óptimas]] y [[Soluciones Básicas]].

> [!note] Fórmula de la Cota de Soluciones El profesor reiteró que si el conjunto factible es infinito, el conjunto de [[Soluciones Básicas]] sigue siendo obligatoriamente finito. Su techo máximo está dado por la fórmula combinatoria de $n$ elementos tomados de $m$ en $m$: $$ C_m^n = \frac{n!}{m!(n-m)!} $$.

> [!question] Dudas de Clase: El Vacío Óptimo **Alumno:** Se confundió al justificar por qué las [[Soluciones Óptimas]] pueden ser un conjunto vacío si hay infinitas soluciones factibles. **Respuesta del Profesor:** Trazó una relación directa. Explicó que si el conjunto de [[Soluciones Óptimas]] es vacío (no hay óptimo), esto deriva de dos escenarios excluyentes: o bien el conjunto de [[Soluciones Factibles]] es vacío (es un [[Problema Incompatible]]), o bien el conjunto factible tiene infinitos elementos y es un [[Problema No Acotado]].
### 📊 MAPA CONCEPTUAL: Flujo de Resolución y Casos Especiales

Para estructurar tu estudio de los escenarios que el profesor evaluará, memoriza este flujo de diagnóstico algorítmico:

```
graph TD
    A(Modelo Original a Resolver) --> B{¿Faltan vectores unitarios?}
    B -->|Sí| C(Aplicar Técnica de la Base Artificial)
    C --> D(Penalizar con M en la Función Objetivo)
    B -->|No| E(Aplicar Método Simplex Estándar)
    D --> E
    E --> F{¿Anomalías al Iterar?}
    F -->|Denominadores <= 0| G(Problema No Acotado)
    F -->|Empate de Cociente Tita| H(Solución Degenerada)
    F -->|Artificial positiva al final| I(Problema Incompatible)
    F -->|Cj-Zj=0 en No Básica| J(Múltiples Soluciones Óptimas)
```

_Conceptos relacionados:_ [[Técnica de la Base Artificial]], [[Problema No Acotado]], [[Solución Degenerada]], [[Problema Incompatible]], [[Múltiples Soluciones Óptimas]].

# ----duads y pregs

# 🚨 RADAR DE PARCIAL: Énfasis y Advertencias del Profesor

A través del análisis detallado de la transcripción, he identificado los puntos exactos donde el profesor marcó el terreno de evaluación y advirtió sobre errores que cuestan parciales.

### 1. La "Trampa" de la Modelización

El profesor fue tajante al advertir que el mayor riesgo de reprobar no está en calcular el [[Método Simplex]], sino en la formulación previa del modelo.

> [!tip] Directiva Innegociable de Estudio _"La parte de formulación del modelo requiere un poco más de ejercitación... hagan todos los problemas sobre todo de modelización"_. El profesor enfatizó que Simplex es un algoritmo mecánico sin secretos, pero si el modelo está mal planteado desde el inicio, todo el cálculo será inválido.

### 2. El Cuadro de [[Casos Especiales]]

Para la preparación del examen, el profesor dio una directiva táctica específica:

> [!tip] Tip de Trinchera: El Cuadro Resumen Sugirió armar explícitamente _"una especie de cuadro en donde ponen los casos particulares, cómo se identifica con gráfico, cómo se identifica con simplex y las observaciones"_. Afirmó que tener esta información organizada es vital para detectar anomalías rápidamente durante la evaluación sumativa (parcial).

### 3. El Falso Amigo del Poliedro Abierto

> [!danger] ZONA DE PELIGRO: Definición de Problema No Acotado El profesor advirtió sobre un error recurrente: asumir que si el [[Poliedro de Soluciones]] está abierto gráficamente, el problema es obligatoriamente "no acotado". Sentenció enfáticamente que esto es _"falso"_, ya que la condición de acotamiento depende estrictamente de la dirección de la función $Z$. Un mismo poliedro abierto puede ser no acotado para un caso de maximización, pero tener un óptimo perfecto si el problema es de minimización.

---

# 🗣️ PREGUNTAS DE LOS ALUMNOS Y RESPUESTAS DEL PROFESOR

La clase tuvo una alta interacción, especialmente durante la corrección del cuestionario. Aquí están las dudas conceptuales críticas que resolvió el profesor:

### Pregunta 1: La Base Artificial en el Óptimo

> [!question] Dudas de Concepto **Alumno:** _"Yo no entendí muy bien la última solución degenerada"_. **Respuesta del Profesor:** Trazó la diferencia exacta al evaluar las [[Variables Artificiales]] al final del algoritmo. Explicó que si llegas al óptimo y queda una variable artificial en la base con un valor **positivo ($>0$)**, el problema original no tiene solución (es un [[Problema Incompatible]]). Pero si queda en la base con un valor **nulo ($0$)**, sí es solución de tu problema, y se clasifica como una [[Solución Degenerada]].

### Pregunta 2: Ingreso a la Base en Minimización

> [!question] Dudas del Algoritmo **Alumno:** _"Cuando quiero ver cuál es la variable que entra a la base en un programa de minimización, ¿es el más negativo?"_. **Respuesta del Profesor:** Confirmó la regla matemática: la variable que ingresa es la que posee _"el menor de los negativos"_, lo cual aclaró que equivale a elegir aquel valor negativo que tenga el **mayor valor absoluto**.

### Pregunta 3: Conjuntos Vacíos (Cuestionario)

> [!question] Dudas de Teoría Abstracta **Alumno:** Se confundió con una pregunta teórica afirmando que las opciones "se contradecían" al preguntar qué pasa si el conjunto de soluciones óptimas es vacío. **Respuesta del Profesor:** El profesor demostró que no hay contradicción, trazando las únicas dos vías lógicas por las que un problema puede carecer de solución óptima:
> 
> 1. El conjunto de [[Soluciones Factibles]] también es vacío (es decir, el problema es **Incompatible**).
> 2. El conjunto de [[Soluciones Factibles]] tiene infinitos elementos, pero la función no tiene límite (es decir, el problema es **No Acotado**).

```
graph TD
    A(Conjunto de Soluciones Óptimas es VACÍO) --> B{¿Por qué no hay óptimo?}
    B -->|Causa 1: No hay área válida| C(Conjunto Factible es VACÍO)
    C --> D(Problema Incompatible)
    B -->|Causa 2: El área no tiene límite Z| E(Conjunto Factible tiene INFINITOS ELEMENTOS)
    E --> F(Problema No Acotado)
```

_Conceptos relacionados:_ [[Problema Incompatible]], [[Problema No Acotado]], [[Soluciones Factibles]], [[Soluciones Óptimas]].

### Pregunta 4: Identificación Gráfica de Degeneración

> [!question] Dudas Gráficas **Alumno:** Preguntó por qué un gráfico específico era considerado un problema degenerado, dudando de la cantidad de restricciones visuales. **Respuesta del Profesor:** Aplicó el conteo algebraico estricto. Demostró que en ese vértice se anulaban $3$ variables (las holguras de la restricción 1 y 3, más la variable $X_2$), dejando solo una variable positiva. Como el sistema tenía $m=3$ restricciones, se necesitaban $3$ variables positivas para ser normal; al haber menos, demostró matemáticamente que era una [[Solución Degenerada]].

### Pregunta 5: Alcance de la Evaluación

> [!question] Dudas Logísticas **Alumno:** _"¿En la evaluación estructurada entra hasta lo que vimos hoy?"_. **Respuesta del Profesor:** Aclaró que el [[Método Simplex]] matricial **no ingresaba** en esa evaluación específica. Los temas llegaban exclusivamente _"hasta casos particulares con gráfico"_.