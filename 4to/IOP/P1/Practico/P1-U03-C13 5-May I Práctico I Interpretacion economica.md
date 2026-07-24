https://www.youtube.com/watch?v=cE2ifz5vCDs&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=12


Esta clase es el núcleo de la unidad de análisis de resultados, marcando la transición entre saber "calcular" la [[Tabla Simplex]] y saber "interpretar" económicamente qué significa cada número para la toma de decisiones empresariales.

A continuación, te presento el esquema cronológico detallado, destacando las fórmulas, las advertencias del profesor y las lógicas operativas innegociables.
### 1. 🏗️ Reconstrucción de la Tabla y la Matriz Identidad (0:00 - 13:00)

La clase comenzó con un problema de producción de una fábrica de pinturas (látex, sintética, exterior) buscando maximizar utilidades. El profesor presentó una [[Tabla Simplex]] incompleta y enseñó cómo deducir los valores faltantes.

- **Identificación de la Base:** Explicó que las [[Variables Básicas]] se identifican localizando la **[[Matriz Identidad]]**. Si una variable tiene el vector $(1, 0, 0)$, su valor va en la primera fila de la base; si es $(0, 1, 0)$, en la segunda, y así sucesivamente.
- **Cálculo de $Z_j$ y $C_j - Z_j$:** Recordó la operatoria de suma-producto entre los coeficientes de la base ($C_b$) y los valores de cada columna.

> [!tip] Tip de Trinchera: El Despeje de Valores Faltantes El profesor advirtió que en las evaluaciones suelen dejar celdas en blanco (por ejemplo, un $\lambda_{ij}$ intermedio). En lugar de iterar toda la tabla desde cero, enseñó que se puede usar el resultado final de $Z_j$ para armar una ecuación simple y **despejar** el valor de $\lambda$ faltante utilizando álgebra básica.

---

> [!tip] Tip de Despeje Algebraico En los exámenes suelen dejar celdas vacías a propósito. El profesor enseñó que no hace falta recalcular toda la matriz. Si te falta un valor intermedio ($\lambda_{ij}$) pero tienes el resultado final de la fila $Z_j$ o $C_j - Z_j$, puedes armar la ecuación de suma-producto lineal y simplemente **despejar** la incógnita.

### 2. 📝 El Informe Económico y Clasificación de la Solución (13:00 - 18:00)

Una vez completa la tabla, el profesor exigió un cambio de mentalidad: el [[Vector Solución]] matemático ya no alcanza, se debe redactar un informe para la gerencia.

- **Redacción Obligatoria:** En un examen, poner "$X_1=2, X_2=30$" está mal. Se debe escribir el significado: _"se producen 2 litros de pintura látex, 30 de sintética..."_.
- **Lectura de Holguras:** Fue enfático en que las [[Variables No Básicas]] (que valen 0) también se informan. Si una holgura es cero, significa que _"se utilizan todos los recursos disponibles"_.
- **Clasificación:** Como el modelo tenía 3 restricciones y quedaron 3 variables estrictamente positivas en la base, clasificó el punto como una **[[Solución Factible Básica]] No Degenerada** y, al ser todos los $C_j - Z_j \leq 0$, confirmó que era la **[[Solución Óptima]]**.


### 3. ⚙️ El Núcleo Teórico: Las Tasas de Sustitución $\lambda_{ij}$ (18:00 - 38:00)

Este fue el bloque más largo e interactivo. El profesor explicó qué indican los coeficientes centrales del cuerpo de la matriz ($\lambda_{ij}$).

- **Regla Base:** Indican las modificaciones que sufre la variable básica (en fila) para poder **incrementar en una unidad** a la variable no básica (en columna).

> [!danger] ZONA DE PELIGRO: La Interpretación de los Signos El profesor remarcó la diferencia crítica al leer un $\lambda_{ij}$ en el cuerpo de la matriz:
> 
> - **Signo Positivo ($>0$):** Indica una **DISMINUCIÓN** en la variable básica. (Se sacrifica producción o se consume recurso).
> - **Signo Negativo ($<0$):** Indica un **AUMENTO** en la variable básica. (Se incrementa la producción).

Además, hizo un énfasis crítico sobre las [[Variables de Holgura]]. Al leer una tasa de sustitución ligada a una holgura, exigió utilizar obligatoriamente la frase **"sin utilizar"** (por ejemplo, "horas de máquina _sin utilizar_") para no confundirlo con el recurso disponible o el recurso total consumido.

|Tipo de Variable en Base|Impacto si $\lambda_{ij}$ es POSITIVO (+)|Impacto si $\lambda_{ij}$ es NEGATIVO (-)|
|:--|:--|:--|
|**[[Variables de Producción]]**|Disminuye la cantidad fabricada.|Aumenta la cantidad fabricada.|
|**[[Variables de Holgura]]**|Disminuye el recurso **sin utilizar**.|Aumenta el recurso **sin utilizar**.|

> [!danger] TRAMPA DE VOCABULARIO: El Estado de la Holgura Al interpretar tasas relacionadas a [[Variables de Holgura]], los alumnos suelen confundirse. El profesor exigió usar estrictamente la frase **"recurso sin utilizar"**. Si dices "recurso disponible" te refieres al lado derecho original ($P_0$), y si dices "recurso utilizado", te refieres a la diferencia. La holgura es EXCLUSIVAMENTE lo no utilizado.


### 4. 📈 Costos e Incremento Neto en Z (38:00 - 47:00)

El último tema conectó las tasas de sustitución con el impacto económico final y los límites del sistema.

- **La fila $Z_j$:** Indica el **costo** económico de las modificaciones que se deben hacer en el plan de producción actual para incorporar la nueva variable. (En la columna de solución, el $Z_j$ representa la utilidad total).
- **La fila $C_j - Z_j$:** El profesor exigió usar la palabra **"NETO"** para definir esta fila. Representa el _incremento o disminución neto_ de la función objetivo, balanceando lo que aporta la nueva variable menos el costo ($Z_j$) de hacerle lugar.


### 5. 🛑 Límite de Producción y el Cociente $\theta$ (47:00 - 53:00)

El profesor planteó: _"¿Qué pasa si queremos forzar la entrada de una variable aunque no convenga económicamente?"_.

- **El Tope Máximo:** Para saber cuántas unidades podemos forzar sin romper el sistema, se debe calcular el **[[Cociente Tita]] ($\theta$)**, dividiendo la solución actual sobre los $\lambda_{ij}$ estrictamente mayores a cero. El menor de los cocientes dicta el límite máximo.

> [!note] Fórmulas de Actualización sin iterar Para calcular el nuevo estado de la empresa al forzar una variable (sin hacer [[Gauss-Jordan]]), el profesor validó usar las siguientes fórmulas directas:
> 
> - Nueva Variable Básica = Valor Anterior - ($\theta \times \lambda_{ij}$)
> - Variable Entrante = $\theta$
> - Nuevo $Z$ = $Z$ anterior + ($\theta \times (C_j - Z_j)$)



### 6. 📝 Corrección de Cuestionario y Q&A (53:00 - 1:03:00)

La clase cerró con un trabajo grupal y la resolución de dudas teóricas avanzadas sobre la clasificación del nuevo punto forzado.

> [!question] Duda Analítica Nivel Examen **Alumno:** _Si forzamos la entrada de la variable $X_2$ con un valor de 5... ¿la nueva tabla pasaría a ser una Solución No Básica?_ **Respuesta del Profesor:** El profesor felicitó al alumno por el análisis. Validó que, al forzar la entrada de $X_2$ sin obligar a otra variable a salir de la base (anularse), la tabla queda con **4 variables positivas** para un sistema que solo tiene **3 restricciones**. Por definición matemática, esa anomalía se clasifica como una **[[Solución Factible No Básica]]**, porque tiene más variables positivas de las que permite el teorema.

---
> [!question] Duda Analítica de Clase: Forzar una Variable Durante la corrección del cuestionario final, un alumno preguntó qué pasaba teóricamente si se forzaba la entrada de una variable (asignándole un valor de $5$) sin sacar a otra de la base. **Respuesta del Profesor:** El profesor felicitó el análisis y dictaminó que, al no anular una variable para que entre otra, el sistema quedaría con 4 variables estrictamente positivas para un problema de solo 3 restricciones. Por definición matemática, esa solución rompe los vértices y pasa a clasificarse como una **[[Solución Factible No Básica]]**.
### 📊 DIAGRAMA DE FLUJO: Interpretación Económica de las Tasas ($\lambda_{ij}$)

```
graph TD
    A(Quiero incrementar 1 unidad de una Variable No Básica) --> B(Miro su columna en la Tabla Simplex)
    B --> C{¿Qué signo tiene el elemento en esa columna?}
    C -->|Positivo| D(DISMINUYE el valor de la variable de esa fila)
    C -->|Negativo| E(AUMENTA el valor de la variable de esa fila)
    D --> F(Costos Z_j: Calcula el impacto en utilidades)
    E --> F
    F --> G(C_j - Z_j: Arroja el Incremento/Disminución NETO en Z)
```

_Conceptos relacionados:_ [[Tasas de Sustitución]], [[Tabla Simplex]], [[Variables Básicas]], [[Variables No Básicas]], [[Función Objetivo]].

### 📊 MAPA DE FLUJO: Evaluación del Impacto de una Variable

Para sistematizar el análisis económico evaluado en clase, utiliza este esquema lógico:

```
graph TD
    A(Evaluar Variable No Básica a introducir) --> B(Leer su columna en Tabla Simplex)
    B --> C(Analizar signos de Tasas de Sustitución)
    C -->|Positivo +| D(Disminuye la variable de esa fila)
    C -->|Negativo -| E(Aumenta la variable de esa fila)
    D --> F(Costos en Z_j)
    E --> F
    F --> G(Cálculo de C_j - Z_j)
    G --> H{¿C_j - Z_j es Negativo en Maximización?}
    H -->|Sí| I(Disminución Neta: No conviene producirla)
    H -->|No| J(Incremento Neto: Conviene producirla)
```

_Conceptos relacionados:_ [[Tabla Simplex]], [[Tasas de Sustitución]], [[Variables Básicas]], [[Variables No Básicas]], [[Incremento Neto]].

> [!note] Fórmula de Actualización de Z El profesor recordó que para calcular el nuevo valor de la función si se ingresa una cantidad $\theta$ de la variable, la fórmula matemática es: $$ Z_{nueva} = Z_{anterior} + (\theta \times (C_j - Z_j)) $$


# --- dudas y pregs
# 🚨 RADAR DE PARCIAL: Énfasis y Advertencias del Profesor

A través de mi análisis riguroso de la transcripción, he detectado tres advertencias explícitas donde el profesor marcó exactamente qué estrategias evalúa en los parciales y qué errores considera inaceptables.

### 1. La Trampa de las Celdas Vacías en la [[Tabla Simplex]]

El profesor advirtió que en las evaluaciones no siempre te pedirán iterar desde cero, sino que evaluarán tu dominio algebraico ocultando valores.

> [!danger] ZONA DE PELIGRO: Elementos Ocultos _"Por ahí en los parciales bueno en algunas evaluaciones pedimos otros elementos por ejemplo supónganse que yo les digo determine y les dejo en blanco este valor"_. **Cómo resolverlo:** Si falta una [[Tasa de Sustitución]] ($\lambda_{ij}$) pero conoces el resultado de la fila $Z_j$, no entres en pánico. El profesor indicó que debes plantear la ecuación de la suma-producto y **despejar** la incógnita.

### 2. El Informe Económico Incompleto

Redactar el resultado es tan importante como calcularlo. El profesor hizo una pausa para dar una instrucción directa de examen:

> [!tip] Directiva Innegociable _"Tomen nota porque es muy importante que no me escriban en una evaluación solo los valores de las variables que las escriban a todas las variables en forma completa en el informe"_. Si no mencionas a las [[Variables No Básicas]] (las que valen $0$) para indicar que "se utilizan todos los recursos disponibles", tu informe estará mal.

### 3. El [[Análisis de Factibilidad]] Inverso (Pregunta Clásica de Examen)

El profesor alertó sobre un escenario contraintuitivo que suele desaprobar alumnos:

> [!tip] El Escenario de "Lo que no conviene" _"Hay veces que en los exámenes le pedimos que analicen lo mismo pero para una variable que no conviene ingresar a la base y por ahí no saben qué es lo que tienen que hacer"_. **La directiva:** Aunque el $C_j - Z_j$ indique que ingresar una variable disminuirá la [[Función Objetivo]], si el examen lo pide (por ejemplo, ante una falla de máquina), debes calcular el límite máximo (el [[Cociente Tita]] o $\theta$) y aplicar las fórmulas de actualización para proyectar el nuevo escenario económico.

---

# 🗣️ PREGUNTAS DE LOS ALUMNOS Y RESPUESTAS DEL PROFESOR

La clase tuvo un alto nivel de participación, especialmente para clarificar la redacción económica y corregir un cuestionario en vivo. Aquí están las intervenciones más relevantes:

### Pregunta 1: La Lógica de la "Unidad"

> [!question] Dudas de Concepto en Clase **Alumno:** _"Profe no termine de entender porque incrementar en una unidad..."_. **Respuesta del Profesor:** Aclaró que la información intrínseca que arroja el [[Método Simplex]] en sus tasas $\lambda_{ij}$ siempre está expresada a nivel unitario. Explicó que el método asume que si deseas fabricar _una_ unidad de un nuevo producto, debes modificar (disminuir o aumentar) la producción actual de los artículos en la base para "liberar recursos".

### Pregunta 2: Flexibilidad en la Redacción Económica

> [!question] Dudas de Semántica **Alumno (Facundo):** Preguntó si podía alterar la sintaxis de la interpretación: _"¿Se puede poner por ejemplo directamente para dejar de utilizar una hora de máquina mezcladora disminuir en 0.29 los litros...?"_. **Respuesta del Profesor:** Validó la propuesta. Aclaró que se puede cambiar el orden de la oración (_"se disminuyen 0.29 litros... por cada hora de máquina... "_) siempre y cuando el significado económico no se altere. Sin embargo, recomendó seguir la estructura estándar para no confundir qué variable se incrementa en una unidad (la de la columna) y cuál se modifica (la de la fila).

### Pregunta 3: El "Costo de Cambiar el Plan"

> [!question] Corrección de Cuestionario **Alumno:** Dudó sobre cómo calcular el costo total al introducir 5 unidades de un producto, ya que la plataforma marcaba $110$ como correcto. **Respuesta del Profesor:** El profesor le demostró que el "costo de cambiar el plan de producción" se lee exactamente en la fila $Z_j$ de esa columna. Al introducir 5 unidades, el costo total es simplemente multiplicar esas 5 unidades por el $Z_j$ unitario de esa variable.

### Pregunta 4: Forzar la Entrada y Romper la Matriz

> [!question] Duda Analítica Nivel Examen **Alumno:** Al analizar el ingreso de $X_2$ con un valor de 5 sin hacer el procedimiento estándar de salida, preguntó: _"¿no pasaría a ser una solución no básica?"_. **Respuesta del Profesor:** El profesor felicitó al alumno por su agudeza teórica. Confirmó que, al no forzar la anulación de una variable previa para que ingrese $X_2$, el sistema queda "sobrepoblado" con más valores positivos que el número de restricciones.

> [!note] Clasificación de Solución Forzada Por definición matemática, si un sistema tiene más variables positivas que su cantidad de restricciones $m$, abandona los vértices y se clasifica como una **[[Solución Factible No Básica]]**.

---

### 📊 DIAGRAMA DE FLUJO: El Protocolo de Examen para Variables "No Convenientes"

Memoriza este algoritmo de resolución si el profesor te exige evaluar una variable que da pérdida:

```
graph TD
    A(Consigna: Evaluar ingreso de variable NO conveniente) --> B(Ignorar el signo negativo en C_j - Z_j)
    B --> C(Calcular Cocientes Tita para esa columna)
    C --> D{¿Denominador es mayor a 0?}
    D -->|Sí| E(Calcular Tita y seleccionar el MENOR)
    D -->|No| F(Ignorar fila)
    E --> G(Aplicar Fórmulas de Actualización)
    G --> H(Proyectar Nueva Solución y Nuevo Z)
```

_Conceptos relacionados:_ [[Análisis de Factibilidad]], [[Variable que Entra]], [[Cociente Tita]], [[Función Objetivo]].

### ⚖️ CUADRO DE BATALLA: Las Fórmulas de Actualización Directa

Para no tener que iterar con Gauss-Jordan en el examen al forzar el ingreso de una variable con un valor $\theta$, el profesor exige usar estas reglas algebraicas:

| Elemento a Actualizar                | Fórmula / Criterio de Examen                                  |
| :----------------------------------- | :------------------------------------------------------------ |
| **Valor de Variables en la Base**    | $P_{0_nuevo} = P_{0_anterior} - (\theta \times \lambda_{ij})$ |
| **Valor de Variable que Entra**      | Adopta exactamente el valor de $\theta$.                      |
| **[[Variables No Básicas]]**         | Siguen siendo $0$.                                            |
| **Nueva [[Función Objetivo]] ($Z$)** | $Z_{nuevo} = Z_{anterior} + (\theta \times (C_j - Z_j))$      |