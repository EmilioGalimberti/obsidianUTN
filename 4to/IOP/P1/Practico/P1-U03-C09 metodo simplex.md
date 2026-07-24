

Esta sesión fue puramente procedimental, enfocada en operar la matriz matemática, interpretar los resultados iterativos y evitar errores críticos de cálculo. A continuación, presento el resumen estructurado de cada tema bajo los estándares de preparación avanzada.

---

### 1. 🏗️ Armado y Lectura de la Tabla Inicial (0:00 - 4:40)

El primer eje abordó cómo volcar el modelo estandarizado a la primera matriz del algoritmo. El profesor explicó que las variables con valor positivo integran la base ([[Variables Básicas]]) y poseen un [[Vector Unitario]] exclusivo, mientras que el resto son [[Variables No Básicas]].

- **Identificación de Variables:** Las variables que asumen valor positivo se denominan **[[Variables Básicas]]**, y las que asumen valor nulo son las **[[Variables No Básicas]]**.
- **Estructura de Columnas:** Explica que la columna de valores (donde se lee el resultado) puede llamarse `vld`, $P_0$ o simplemente "solución" dependiendo del libro o software. Las variables en la base deben tener obligatoriamente un **[[Vector Unitario]]** (ej. $0, 1, 0$).
- **Fórmulas de Evaluación:**
    
> [!note] Fórmulas de la Tabla
> - **Cálculo de $Z_j$:** Se obtiene multiplicando la columna de coeficientes de la base ($C_b$) por cada una de las columnas de las variables.
>   $$ Z_j = \sum (C_b \times \text{Columna}_j) $$
>   
    > - **Fila $C_j - Z_j$:** Se calcula por diferencia directa entre el coeficiente de la función objetivo y el $Z_j$ obtenido.


### 2. 🔄 Criterio de Optimidad y [[Variable que Entra]] (4:41 - 6:53)

El segundo tema dictaminó las reglas matemáticas inflexibles para evaluar si el punto actual es la [[Solución Óptima]] y cómo moverse a un nuevo vértice si no lo es.

- **Evaluación del Óptimo:** En problemas de maximización, la solución es óptima únicamente si todos los valores de la fila $C_j - Z_j$ son menores o iguales a cero ($\leq 0$).
- **Criterio de Entrada:** Al notar que existen valores positivos, la solución se debe mejorar. Para elegir qué variable nula se hará positiva (ingresa a la base), el profesor dicta la regla de seleccionar la columna con el **mayor valor positivo** en la fila $C_j - Z_j$.

- **[[Variable que Entra]]:** Si hay valores positivos, ingresa a la base aquella columna que posea el mayor valor positivo en $C_j - Z_j$.
- **[[Variable que Sale]]:** Se elige calculando el cociente ($\theta$) entre la columna solución y los elementos de la variable que entra, seleccionando el menor resultado positivo.
	- Se debe dividir el valor de la columna solución ($\lambda_i$) por el valor respectivo en la columna de la variable que ingresa ($\lambda_{ij}$). La variable que sale es aquella que arroje el menor cociente positivo.

> [!danger] TRAMPA ALGEBRAICA: El Denominador Prohibido El profesor fue extremadamente tajante al explicar el cálculo del cociente. **Jamás** se debe calcular si el divisor es $0$ o negativo. Si se divide por $0$ no existe, y si se divide por un número negativo, la variable asumiría un valor negativo en la próxima tabla, violando la [[Restricción de No Negatividad]]. En esos casos, se coloca una raya y se descarta esa fila.

### 4. 🧮 Iteración mediante [[Operaciones Elementales de Fila]] (11:14 - 21:13)

El tercer bloque consistió en la actualización mecánica de la tabla aplicando el método de [[Gauss-Jordan]]. El objetivo es que la nueva variable que entró a la base adopte un [[Vector Unitario]] perfecto (un $1$ en la intersección y $0$ en el resto de la columna).

- **Generación del "1" ([[Elemento Pivot]]):** Se divide toda la fila saliente por el número de intersección (pivot) para convertirlo en $1$.
- **Generación de los "0":** Para el resto de las filas, se multiplica la fila pivot recién calculada por el opuesto del número que se desea anular, y el resultado se suma a la fila original.
- **Convergencia:** Este proceso se repitió hasta llegar a una tercera tabla donde todos los valores de $C_j - Z_j$ resultaron nulos o negativos, alcanzando así el óptimo final con $Z = 22800$.


### 5. 📝 Cuestionario en Vivo y la Trampa de los Decimales (21:14 - 41:41)

El tramo final combinó la corrección de un cuestionario de Moodle con una discusión crítica sobre la precisión matemática.

> [!question] Dudas de Concepto: El Error de Arrastre **Alumno:** _"Profe, el Z_j me da 34, no 27.27"_. 
> 
> **Respuesta del Profesor:** El profesor demostró que la diferencia radicaba en el redondeo de los decimales (usar $0.05$ en lugar del número periódico $0.04545...$). Recomendó trabajar analíticamente con fracciones para evitar estos errores de arrastre, aclarando que software como _PHP Simplex_ usa todos los decimales. Indicó que en los exámenes generalmente se exigirán dos o tres decimales de precisión.

> [!tip] Tip de Parcial: Variables Ocultas Durante la revisión del cuestionario, el profesor notó errores de lectura en las tablas. Recordó la regla de oro: si una variable no figura listada explícitamente en la base (columna lateral), es una [[Variable No Básica]] y su valor es matemáticamente **cero**.


### 📊 DIAGRAMA DE FLUJO: Algoritmo Operativo de la Clase

Para visualizar la estructura lógica que rigió esta clase, este es el bucle que el profesor aplicó sobre la tabla:

```
graph TD
    A(Armar Tabla Inicial) --> B(Calcular Z_j y C_j - Z_j)
    B --> C{¿Todos los C_j - Z_j son <= 0?}
    C -->|Sí| D(SOLUCIÓN ÓPTIMA ALCANZADA)
    C -->|No, hay positivos| E(Identificar Variable que Entra: Mayor Positivo)
    E --> F(Calcular cocientes Tita válidos)
    F --> G(Identificar Variable que Sale: Menor Cociente)
    G --> H(Aplicar Operaciones Elementales de Fila)
    H --> I(Generar 1 en el Pivot y 0 en el resto de la columna)
    I --> B
```

_Conceptos relacionados:_ [[Método Simplex]], [[Operaciones Elementales de Fila]], [[Variable que Entra]], [[Variable que Sale]], [[Criterio de Optimidad]].



# -----dudas y pregs

Como tu Tutor Académico de Élite, he sometido la transcripción de la clase a un escaneo minucioso. Mi objetivo no es solo resumir, sino aplicar ingeniería inversa sobre el discurso del profesor para detectar exactamente dónde marcó el "terreno de parcial" y cuáles fueron las confusiones reales de tus compañeros.

Aquí tienes el reporte dividido en los focos críticos de evaluación y el registro de intervenciones en vivo.

# 🚨 RADAR DE PARCIAL: Énfasis y Advertencias del Profesor

El profesor detuvo explícitamente su explicación para marcar dos temas como obligatorios, utilizando la frase _"es muy importante"_ y advirtiendo que son ejercicios típicos de evaluación.

### 1. El Ejercicio Fijo: Completar Tablas Intermedias

> [!danger] ZONA DE PELIGRO: La Tabla Incompleta Durante la corrección del cuestionario, el profesor notó que muchos alumnos dejaron el ejercicio en blanco y lanzó una advertencia directa: _"eso es importante nosotros varias veces le pedimos que complete en una tabla y creo que en algunos de los cuestionarios [...] tienen que completar otros valores"_. **Cómo prepararlo:** No basta con saber hacer el [[Método Simplex]] desde cero. Debes saber calcular analíticamente los valores de $Z_j$ y $C_j - Z_j$ a partir de una tabla a medio empezar, simplemente realizando el producto de vectores sin necesidad de iterar toda la matriz.

### 2. La Regla Innegociable del Cociente ($\theta$)

> [!tip] Tip de Trinchera: El Denominador Prohibido Al explicar el cálculo para determinar la [[Variable que Sale]], el profesor hizo un énfasis drástico: _"fíjense que es muy importante tener en cuenta este detalle... voy a calcular el cociente siempre y cuando los elementos sean mayores que 0"_. Jamás debes dividir por $0$ o por un número negativo, ya que eso rompería la [[Restricción de No Negatividad]] del modelo algebraico.

---

# 🗣️ PREGUNTAS DE LOS ALUMNOS Y RESPUESTAS DEL PROFESOR

La clase tuvo un alto nivel de participación. Los alumnos plantearon dudas operativas clave que el profesor utilizó para asentar la teoría algorítmica.

### Pregunta 1: Identificación de las Variables Nulas

> [!question] Dudas de Concepto en Clase **Alumno:** _"Profe, ¿cuáles son las variables no básicas de la tabla?"_. **Respuesta del Profesor:** El profesor aplicó la definición estricta. Señaló que las **[[Variables No Básicas]]** son aquellas que no figuran en la columna de solución (la base) y que carecen de un **[[Vector Unitario]]**. Puso como ejemplo a $x_1$ y $S_2$, reafirmando que el valor matemático que asumen en esa iteración es rigurosamente $0$.

### Pregunta 2: El Empate en el Menor Cociente

> [!question] Dudas del Algoritmo **Alumno:** _"Profe, si elegimos cualquiera de los dos (ante un empate en el cociente)... ¿qué pasa?"_. **Respuesta del Profesor:** Aclaró que es una _"situación especial"_ (degeneración), pero en la práctica resolutiva el alumno puede elegir cualquiera de las dos variables empatadas para que salga de la base. Comentó que, como convención estratégica, algunos prefieren expulsar primero a la [[Variable de Holgura]] para mantener las variables principales positivas, pero que matemáticamente ambas opciones son viables.

### Pregunta 3: División por Cero o Negativos

> [!question] Dudas del Criterio de Salida **Alumno:** _"¿Qué se hace ahora si simplemente no sigo el cálculo ni lo escribo al cociente? ¿Pongo una rayita nomás?"_. **Respuesta del Profesor:** Validó totalmente la afirmación del alumno. Confirmó que si el denominador es $\leq 0$, el cociente no se calcula, se coloca una raya y esa variable **no es candidata a salir de la base**.

### Pregunta 4: La "Trampa" del Menor vs. Mayor Positivo

> [!question] Corrección en Vivo (Concepto Crítico) **Alumno:** Argumentó incorrectamente la elección de la [[Variable que Entra]] diciendo _"es el menor valor positivo de todos los que estén en $C_j - Z_j$"_. **Respuesta del Profesor:** Lo corrigió inmediatamente. Al ser un problema de **Maximización**, la variable que ingresa a la base está dictaminada por el coeficiente que otorga la mayor tasa de crecimiento. La regla exige buscar en la fila $C_j - Z_j$ y elegir el **mayor** de los valores positivos, no el menor.

### Pregunta 5: Errores de Arrastre Decimal

> [!question] Dudas de Precisión Matemática **Alumno:** _"Profe, yo tengo una pregunta, vimos acá el $Z_j$ y da 27.27... a mí me da 34"_. **Respuesta del Profesor:** El profesor le demostró que esta desviación no era un error de fórmula, sino un "error de arrastre" causado por truncar decimales periódicos (como redondear $0.04545...$ a $0.05$) a lo largo de las tablas iterativas. _Nota para Parcial:_ Ante la consulta de cuántos decimales usar, indicó que en un contexto virtual se suele trabajar con 2 o 3 decimales, lo cual será especificado en las consignas para evitar estas diferencias.

---

### 📊 MAPA DE RESOLUCIÓN DE CONFLICTOS (Reglas Dictadas en Q&A)

```
graph TD
    A(Cálculo de Variables en Tabla Simplex) --> B{¿Está la variable en la columna solución?}
    B -->|Sí| C(Es Variable Básica = Leer su valor en la columna P0)
    B -->|No| D(Es Variable No Básica = Su valor es 0)
    A --> E(Cálculo del Cociente Tita)
    E --> F{¿El denominador es mayor a 0?}
    F -->|Sí| G(Calcular y comparar para buscar el menor)
    F -->|No| H(Poner raya. NO es candidata a salir)
    A --> I(Elegir Variable que Entra en Maximización)
    I --> J(Buscar en fila C_j - Z_j)
    J --> K(Seleccionar SIEMPRE el MAYOR valor positivo)
```

_Conceptos relacionados:_ [[Variable que Entra]], [[Variable que Sale]], [[Variables Básicas]], [[Variables No Básicas]].