# Analisis de sensibilidad
![[{76DC3665-557C-4143-8805-1CEC01C0A047}.png]]
El análisis de sensibilidad nos permite evaluar cuánto pueden variar los parámetros originales de un problema de Programación Lineal (como las ganancias o la disponibilidad de recursos) sin que la solución óptima actual cambie su estructura (es decir, sin que cambien las variables que están en la base).

Vamos a desglosar paso por paso la teoría y los cálculos para los dos parámetros solicitados, respetando la regla de **truncar a 3 decimales**.

## Análisis de Post-Optimidad: Cálculo de Intervalos

### 1. Variación en $C_3$ (Coeficiente de la Función Objetivo)

El parámetro $C_3$ es el coeficiente de la variable $X_3$ en la función objetivo. En la tabla óptima, vemos que $X_3$ es una **variable básica** (está en la columna "Base").

Si cambiamos el valor de $C_3$ por $C_3 + \Delta C_3$, este cambio afectará el cálculo de toda la fila $Z_j$ y, por ende, de la fila $C_j - Z_j$. Para que la solución siga siendo óptima en un problema de maximización, necesitamos que todos los valores de $C_j - Z_j$ de las variables no básicas sigan siendo menores o iguales a cero ($\le 0$).

La fórmula para encontrar el intervalo de variación ($\Delta C_3$) de una variable básica utiliza los valores de la fila $C_j - Z_j$ y los coeficientes $a_{ij}$ correspondientes a la fila de la variable básica en cuestión (en este caso, la fila de $X_3$).

> [!note] Fórmula del Intervalo de Optimidad Para un incremento $\Delta c_k$, se debe cumplir para toda variable no básica $j$: $$ (C_j - Z_j) - \Delta c_k \cdot \lambda_{kj} \le 0 $$ _(Donde $\lambda_{kj}$ son las `[[Tasas de Sustitución]]` en la fila de la variable analizada)_

Si despejamos $\Delta C_3$ de ahí, obtenemos:

$$(C_j - Z_j) \le \Delta C_3 \cdot a_{ij}$$

Aquí es donde los signos de $a_{ij}$ (los valores en la fila de $X_3$) dictan si estamos calculando el incremento o la disminución:

1. **Si $a_{ij}$ es positivo (como en $X_2$ y $S_2$):** Al despejar, pasas dividiendo un número positivo, por lo que el signo de la inecuación **se mantiene**.
    
    Como $(C_j - Z_j)$ es negativo, te queda un límite de la forma $\Delta C_3 \ge \text{Número Negativo}$.
    
    **Esto restringe cuánto puede disminuir el parámetro.** Yo te había dicho erróneamente que los positivos marcaban el incremento.
    
2. **Si $a_{ij}$ es negativo (como en $S_3$):** Al pasar dividiendo un número negativo, la inecuación **se invierte**.
    
    Te queda un límite de la forma $\Delta C_3 \le \text{Número Positivo}$.
    
    **Esto restringe cuánto puede incrementar el parámetro.**

Aplicamos la inecuación para las variables no básicas ($x_2, S_2, S_3$), leyendo la fila de $x_3$ ($\lambda_{3j}$):

- **Para $x_2$:** $-7.377 - \Delta c_3 \cdot (0.632) \le 0 \Rightarrow -7.377 \le 0.632 \cdot \Delta c_3 \Rightarrow \Delta c_3 \ge -\frac{7.377}{0.632} \Rightarrow \Delta c_3 \ge -11.672$
  
- **Para $S_2$:** $-0.458 - \Delta c_3 \cdot (0.053) \le 0 \Rightarrow -0.458 \le 0.053 \cdot \Delta c_3 \Rightarrow \Delta c_3 \ge -\frac{0.458}{0.053} \Rightarrow \Delta c_3 \ge -8.641$
- **Para $S_3$:** $-0.324 - \Delta c_3 \cdot (-0.021) \le 0 \Rightarrow -0.324 + 0.021 \cdot \Delta c_3 \le 0 \Rightarrow 0.021 \cdot \Delta c_3 \le 0.324 \Rightarrow \Delta c_3 \le \frac{0.324}{0.021} \Rightarrow \Delta c_3 \le 15.428$

Intersectando los resultados, la variación permitida es: **$-8.641 \le \Delta c_3 \le 15.428$**

- **Disminución máxima:** 8.641 (en valor absoluto) 
    
- **Incremento máximo:** 15.428


#### como sabes de elegir −8.641 y no −11.672?
¡Excelente pregunta! Esta es una de las dudas analíticas más frecuentes al calcular el **[[Intervalo de Sensibilidad]]**.

La clave matemática radica en comprender que estamos resolviendo un **sistema de inecuaciones simultáneas**. Para que la solución siga siendo óptima, la variación $\Delta c_3$ debe satisfacer **TODAS** las restricciones al mismo tiempo.

A continuación, te explico la lógica exacta de selección.


##### 1. La Lógica de las Inecuaciones Simultáneas

Cuando analizas una **[[Variable Básica]]**, generas una inecuación por cada **[[Variable No Básica]]** del modelo para garantizar que se mantenga la **[[Condición de Optimidad]]** ($C_j - Z_j \le 0$).

En nuestro cálculo, para el límite inferior (disminución), obtuvimos dos inecuaciones que exigen que la variación sea "mayor o igual a" un valor negativo:

1. Impuesta por $x_2$: $\Delta c_3 \ge -11.672$
2. Impuesta por $S_2$: $\Delta c_3 \ge -8.641$

##### 2. El Criterio del Límite Más Restrictivo

Para que ambas condiciones se cumplan a la vez, debes elegir siempre **el límite más restrictivo** (el "peor escenario" antes de que el sistema se rompa).

Si lo analizamos numéricamente con un ejemplo de prueba:

- **¿Qué pasa si el coeficiente disminuye en 10 ($\Delta c_3 = -10$)?**
    - Verificamos en $x_2$: $-10 \ge -11.672$ $\rightarrow$ ¡Se cumple! La variable $x_2$ sigue siendo óptima.
    - Verificamos en $S_2$: $-10 \ge -8.641$ $\rightarrow$ **¡FALSO!** Aquí se rompe la condición. Si el coeficiente cae en 10, la variable $S_2$ se volverá positiva en la fila $C_j - Z_j$ y la solución dejará de ser óptima.

Por lo tanto, la "caída" no puede llegar hasta $-11.672$. El sistema te "frena" antes, exactamente en **$-8.641$**.

> [!tip] Regla Rápida de Intersección Matemática
> 
> - **Para el Límite Inferior (Disminución permitida):** Tienes varios símbolos $\ge$. Debes elegir siempre el **MÁXIMO** de esos valores (el número negativo que esté más cerca del cero).
> - **Para el Límite Superior (Aumento permitido):** Tienes varios símbolos $\le$. Debes elegir siempre el **MÍNIMO** de esos valores (el número positivo más cercano al cero).

> [!danger] Trampa de Parcial: El "Número Más Grande" El error más común en los exámenes es mirar los resultados y decir: _"11 es más grande que 8, entonces la disminución permitida es 11"_. ¡Cuidado! Al trabajar con números negativos en una recta numérica, $-8.641$ es matemáticamente **mayor** que $-11.672$. Siempre debes elegir el que "corta el paso" primero.

##### Esquema Visual de Selección

```
graph TD
    A[Calculo de Multiples Inecuaciones] --> B{Sentido de la Desigualdad?}

    B -->|Mayor o igual >=| C[Limites Inferiores: Disminucion]
    C --> D[Tengo: -11.672 y -8.641]
    D --> E[Elegir el mas restrictivo o mas cercano al cero]
    E --> F[Resultado de la Disminucion: -8.641]

    B -->|Menor o igual <=| G[Limites Superiores: Incremento]
    G --> H[Tengo solo uno en este caso]
    H --> I[Resultado del Incremento: 15.428]
```

_Conceptos Relacionados:_ [[Condición de Optimidad]], [[Intervalo de Sensibilidad]], [[Variable Básica]], [[Variable No Básica]].

### 2. Variación en $b_2$ (Valor del Lado Derecho)

El parámetro $b_2$ corresponde al recurso de la segunda restricción, cuya variable de holgura asociada es $S_2$. Al observar la tabla, $S_2$ es una **`[[Variable No Básica]]`** (su valor es 0), lo que indica que estamos ante una **`[[Restricción Limitante]]`**.

> [!tip] Metodología para Lados Derechos Limitantes Cuando se altera el `[[Lado Derecho]]` de un recurso agotado, la base se mantiene pero cambian los valores de las variables. Debemos asegurar la condición de factibilidad (que ninguna variable básica se vuelva negativa).

> [!note] Fórmula de Factibilidad Para una variación $\Delta b_k$, se debe cumplir para toda variable en la base $i$: $$ VLD_i + \Delta b_k \cdot \lambda_{i,S_k} \ge 0 $$ _(Donde $\lambda_{i,S_k}$ son los elementos de la columna de la holgura asociada a $b_k$)_

Queremos asegurar que los nuevos valores de VLD sigan siendo mayores o iguales a cero ($VLD \ge 0$). La fórmula es:

$$VLD_{nuevo} = VLD_{actual} + (\Delta b_i \times \text{Columna } S_i) \ge 0$$

Despejando $\Delta b_2$:

- Si el valor en la columna $S_2$ es negativo, nos dará el límite de **incremento**.
    
- Si el valor en la columna $S_2$ es positivo, nos dará el límite de **disminución**.

Aplicamos la inecuación leyendo la columna de $S_2$ para las variables básicas actuales ($S_1, x_3, x_1$):

- **Fila $S_1$:** $285.965 + \Delta b_2 \cdot (-0.263) \ge 0 \Rightarrow 285.965 \ge 0.263 \cdot \Delta b_2 \Rightarrow \Delta b_2 \le \frac{285.965}{0.263} \Rightarrow \Delta b_2 \le 1087.319$
- **Fila $x_3$:** $29.474 + \Delta b_2 \cdot (0.053) \ge 0 \Rightarrow 0.053 \cdot \Delta b_2 \ge -29.474 \Rightarrow \Delta b_2 \ge -\frac{29.474}{0.053} \Rightarrow \Delta b_2 \ge -556.113$
- **Fila $x_1$:** $38.596 + \Delta b_2 \cdot (-0.026) \ge 0 \Rightarrow 38.596 \ge 0.026 \cdot \Delta b_2 \Rightarrow \Delta b_2 \le \frac{38.596}{0.026} \Rightarrow \Delta b_2 \le 1484.461$

Intersectando los resultados, la variación permitida es: **$-556.113 \le \Delta b_2 \le 1087.319$**

**Definiendo el intervalo:**

- Incremento permitido: Buscamos el mínimo entre los límites superiores $\min(1087.319, 1484.461) = \mathbf{1087.319}$
    
- Disminución permitida: El límite inferior es $-556.113$. Por lo tanto, la disminución máxima admisible en valor absoluto es $\mathbf{556.113}$.
---

### Diagrama de Decisión para Variaciones

```
graph TD
    A[Analisis de Sensibilidad] --> B{Que parametro varia?}
    B -->|C3| C[Coeficiente Objetivo de Variable Basica]
    B -->|b2| D[Lado Derecho de Restriccion Limitante]

    C --> E[Revisar Fila x3 y No Basicas]
    E --> F[Asegurar Condicion de Optimidad Cj-Zj <= 0]

    D --> G[Revisar Columna S2 y Variables Basicas]
    G --> H[Asegurar Condicion de Factibilidad VLD >= 0]
```

_Conceptos Relacionados:_ `[[Condición de Optimidad]]`, `[[Condición de Factibilidad]]`.

---

> [!danger] Atención al Formato Solicitado Has indicado explícitamente introducir el valor truncado a 3 decimales. Procedo a completar la tabla requerida con el formato exacto.

### Tabla de Resultados (Truncados a 3 decimales)

|Parámetro|Incremento|Disminución|
|:--|:--|:--|
|**C3**|15.428|8.641|
|**b2**|1087.319|556.113|

# ---
# El gráfico corresponde a un problema de PL de maximización

![[{CEC216AD-25BB-466A-855C-31FFA7AC413E}.png]]

## 1. ¿Cuántas variables principales tiene el problema Dual?

Para responder a esta pregunta, debes recordar la regla fundamental de simetría entre el **[[Problema Primal]]** y el **[[Problema Dual]]**:

> [!note] Regla Estructural de Cantidades El número de **[[Variables Principales]]** (o de decisión) del problema dual es exactamente igual al número de **[[Restricciones]]** funcionales del problema primal.

### ¿Qué mirar en el gráfico?

Debes **contar la cantidad de líneas rectas (ecuaciones)** trazadas en el plano que delimitan o forman parte del poliedro de soluciones, **excluyendo los ejes cartesianos**.

- Cada línea recta graficada representa una restricción estructural.
- Por lo tanto, si en el gráfico observas 3 líneas rectas cortándose, el primal tiene 3 restricciones y, en consecuencia, el dual tendrá exactamente 3 **[[Variables Principales]]** ($y_1, y_2, y_3$).

> [!danger] Trampa Visual NO cuentes los ejes de coordenadas ($x_1=0$ y $x_2=0$) como restricciones funcionales. Estos ejes representan la **[[Restricción de No Negatividad]]** y no generan variables duales; su única función es definir que el gráfico se ubica en el primer cuadrante.

---

### en este caso
Descartando los ejes cartesianos, nos quedan **3 rectas oblicuas** (las que forman los segmentos DC, CB y FG). Esto significa que el problema Primal tiene 3 restricciones estructurales.

**Conclusión:** Como el Primal tiene 3 restricciones, **el problema Dual tendrá 3 variables principales** (generalmente llamadas $Y_1, Y_2, Y_3$).
## 2. ¿Cuántas variables no positivas tiene el problema Dual?

Para responder a esta pregunta, debes aplicar la lógica de la **[[Forma Canónica]]** enseñada por el profesor para la **[[Dualidad Mixta]]**.

Sabemos que el problema primal es de **[[Maximización]]**. Por lo tanto, su dual asociado será de **[[Minimización]]**.

> [!tip] La Regla de la Normalidad (Canonicidad) El signo de una variable dual depende de si la restricción primal que la origina respeta o contradice el comportamiento "normal" del modelo:
> 
> - En un problema de **[[Maximización]]**, la **[[Restricción Canónica]]** es de menor o igual ($\le$). Esto genera una **[[Variable No Negativa]]** ($\ge 0$) en el dual.
> - En un problema de **[[Maximización]]**, la **[[Restricción No Canónica]]** es de mayor o igual ($\ge$). Esto genera una **[[Variable No Positiva]]** ($\le 0$) en el dual.

### ¿Qué mirar en el gráfico?

Para saber cuántas variables $\le 0$ hay en el dual, debes **contar cuántas restricciones de mayor o igual ($\ge$)** hay en el gráfico del primal.

¿Cómo identificas visualmente si una recta trazada es $\le$ o $\ge$? Observando hacia qué lado se encuentra el semiplano que apunta hacia la **[[Región Factible]]**:

1. **Restricciones de Menor o Igual ($\le$):** Generalmente (con coeficientes positivos), el semiplano que las verifica apunta "hacia abajo" o "hacia el origen" (el área sombreada se encuentra entre la recta y el origen).
2. **Restricciones de Mayor o Igual ($\ge$):** El semiplano que las verifica apunta "hacia arriba" o "alejándose del origen".

> [!tip] Tip Práctico del Profesor: El Punto de Prueba El profesor advirtió que mirar visualmente "hacia arriba" o "hacia abajo" puede ser engañoso si las rectas tienen inclinaciones confusas o coeficientes negativos. El método infalible es tomar un punto de prueba, preferentemente el origen $(0,0)$. Si el punto $(0,0)$ **no pertenece** al área sombreada definida por esa recta en particular, es casi seguro que se trata de una restricción de la forma $\ge$.

Por lo tanto, la respuesta a la pregunta será el número exacto de rectas en tu gráfico cuyo semiplano apunte "hacia afuera" (restricciones $\ge$).

---

### en este caso
|Restricción en el Primal (Max)|Variable en el Dual (Min)|
|---|---|
|Menor o igual (≤)|No negativa (≥ 0)|
|**Mayor o igual (≥)**|**No positiva (≤ 0)**|
|Igualdad (=)|Irrestricta en signo|

**Cómo identificarlo en el gráfico:** Debemos analizar hacia dónde "apunta" la región factible respecto a cada una de las 3 rectas estructurales que identificamos antes.

- **Rectas superiores (segmentos DC y CB):** La región verde se encuentra "por debajo" o "a la izquierda" de estas líneas, acercándose al origen (0,0). Esto indica que estas rectas actúan como topes máximos. Por lo tanto, son restricciones del tipo **menor o igual (≤)**. Según nuestra tabla, estas 2 restricciones generarán 2 variables duales **no negativas** (≥ 0).
    
- **Recta inferior (segmento FG):** Observa que la región verde está "por encima" o "a la derecha" de esta línea. Esta recta está "empujando" la región factible lejos del origen; no permite que la solución tome valores más bajos que esa frontera. Esto es la definición gráfica de una restricción de tope mínimo, es decir, del tipo **mayor o igual (≥)**.
    

**Conclusión:** Como hay exactamente 1 restricción en el Primal del tipo "mayor o igual" (la recta FG), esta generará **1 variable no positiva** en el problema Dual.

### Resumen Lógico Visual (Diagrama de Decisión)

```
graph TD
    A[Analisis del Grafico: Primal MAX] --> B[Pregunta 1: Variables Duales Totales]
    A --> C[Pregunta 2: Variables Duales No Positivas]

    B --> D[Contar total de rectas graficadas]
    D --> E[Ignorar los ejes cartesianos]
    E --> F[Total de Rectas = Total de Variables Duales]

    C --> G[Analizar el semiplano de cada recta]
    G --> H{Apunta hacia afuera del origen?}
    H -->|Si| I[Es una inecuacion >=]
    H -->|No| J[Es una inecuacion <=]
    I --> K[Es No Canonica: Genera Variable Dual No Positiva]
    J --> L[Es Canonica: Genera Variable Dual No Negativa]
    K --> M[Contar cuantas rectas cumplen esta condicion]
```

_Conceptos Relacionados:_ [[Problema Primal]], [[Problema Dual]], [[Maximización]], [[Región Factible]], [[Forma Canónica]], [[Variable No Positiva]].

# **Tasas de Sustitución**
![[{38D47674-FAD7-416B-A4BA-BD2E71F5F011}.png|482]]
## teoria tasas de sustitucion

### 1. Definición Conceptual y Matemática

En el contexto del **[[Método Simplex]]**, las tasas de sustitución (simbolizadas como $\lambda_{ij}$) son los valores numéricos que se encuentran en el cuerpo de la matriz óptima o en las tablas intermedias.

> [!note] Definición Formal Las **[[Tasas de Sustitución]]** indican el "sacrificio" que se deberá hacer de la **[[Variable Básica]]** $x_i$ (la que se encuentra en la fila) para poder incrementar en exactamente una unidad a la **[[Variable No Básica]]** $x_j$ (la que se encuentra en la columna).

Matemáticamente, cada $\lambda_{ij}$ mide la reducción que se debe realizar en el valor de las variables que actualmente están en la base a fin de liberar los recursos necesarios para introducir una unidad de una nueva actividad.

### 2. Interpretación Económica de los Signos

El profesor hizo muchísimo énfasis en que la interpretación de estos valores depende estrictamente de su signo, el cual funciona de manera contraria a la intuición matemática tradicional.

|Signo de $\lambda_{ij}$|Significado Económico|Impacto en la [[Variable Básica]] $x_i$|
|:--|:--|:--|
|**Positivo ($>0$)**|**Sacrificio**. Indica los recursos o producción que debo ceder para hacer una unidad de la nueva variable.|**Disminuye**.|
|**Negativo ($<0$)**|**Incremento**. Nos indica que, al fabricar una unidad del nuevo producto, la base actual se ve favorecida y crece.|**Aumenta**.|
|**Cero ($=0$)**|**Independencia**. No existe relación de consumo o intercambio directo entre ambas variables.|**Se mantiene igual**.|

> [!danger] Trampa de Signos ¡Cuidado en los exámenes! Por definición general, si la tasa es **positiva**, se debe **restar** al valor actual de la variable básica. Si la tasa es **negativa**, esto implica que en lugar de un sacrificio hay un incremento, por lo tanto, la variable básica **aumenta** su valor.

### 3. Uso Práctico: Fórmula de Actualización

Las tasas de sustitución son la herramienta principal para calcular cómo quedará el plan de producción si decidimos forzar la entrada de un producto que no era óptimo, o evaluar cambios en el sistema.

> [!tip] Fórmula de Actualización de Variables De acuerdo al Teorema Fundamental del Método Simplex, el nuevo valor de cualquier variable básica se calcula con la siguiente ecuación: $$ x_i^{nuevo} = \lambda_i - \theta \cdot \lambda_{ij} $$

Donde:

- $x_i^{nuevo}$: Es el valor actualizado de la **[[Variable Básica]]**.
- $\lambda_i$: Es el valor actual de la variable en la columna solución (**[[Valor del Lado Derecho]]** o $VLD$).
- $\theta$: Es la cantidad de unidades que decidimos fabricar (o introducir) de la **[[Variable No Básica]]**.
- $\lambda_{ij}$: Es la **[[Tasa de Sustitución]]** ubicada en la intersección de ambas variables.

### 4. Dinámica de Clase: Explicación del Profesor

Para fijar el concepto, el profesor utilizó el problema de "Fabricaciones Manuel" en clase y lo explicó con un ejemplo práctico en la matriz:

> [!question] El Ejemplo del Profesor en Clase **Situación:** En la tabla, la intersección entre la fila de la variable $x_2$ y la columna de la variable $x_1$ tenía un valor de $0.5$ positivo. **Explicación:** _"Esta tasa me está informando que si yo quiero producir una unidad de $x_1$ voy a tener que dejar de producir de $x_2$ media unidad. [...] Para fabricar una unidad del producto 1 debo dejar de fabricar o sea sacrificar media unidad del producto 2"_.

### 5. Diagrama Lógico de Interpretación

Para que asimiles rápidamente qué hacer con cada tasa al mirar una tabla, aquí tienes el árbol de decisión:

```
graph TD
    A[Lectura de Tasa de Sustitucion] --> B{Cual es su Signo?}
    B -->|Positivo > 0| C[Representa un Sacrificio]
    B -->|Negativo < 0| D[Representa un Incremento]

    C --> E[Se restara de la Variable Basica actual]
    E -.-> F[Formula: VLD - tasa]

    D --> G[Se sumara a la Variable Basica actual]
    G -.-> H[Formula: VLD - tasa negativa = VLD + tasa]
```

_Conceptos Relacionados:_ [[Tabla Simplex]], [[Variable Básica]], [[Variable No Básica]], [[Valor del Lado Derecho]].

## resumido
En tu tabla óptima, la variable $X_3$ (premezcla 3) es una **variable no básica**, lo que significa que actualmente no se está produciendo (su valor es 0).

Si el decisor dice "quiero fabricar algunas unidades de $X_3$ de todas formas", tenemos que ver cómo impacta eso en las variables que sí están en la base ($S_1$, $X_2$ y $X_1$). Para esto, leemos la columna $P_3$ en la tabla. Esos coeficientes se llaman **tasas de sustitución** ($a_{ij}$).

Las tasas de sustitución nos dicen cuánto debemos "sacrificar" de nuestras variables básicas actuales para fabricar una unidad de la nueva variable. La fórmula general que se deriva de las ecuaciones del Simplex es:

$$Valor\_Nuevo = Valor\_Actual - (\text{Tasa de Sustitución} \times \text{Cantidad a producir})$$

## Si decide producir 6 kilos de premezcla 3 ->X3, el nuevo valor de S1 es:?
**Si decide producir 6 kilos de premezcla 3, el nuevo valor de $S_1$ es:"**

1. **Identificar los datos en la tabla:**
    
    - **Valor Actual** de $S_1$ (mirando la fila de $S_1$, columna $P_0$): **148,75**
        
    - **Tasa de Sustitución** (mirando la intersección de la fila $S_1$ y la columna $P_3$): **3,725**. _(Esto significa que por cada kilo de $X_3$ que fabriquemos, consumiremos 3,725 horas de holgura de mano de obra)._
        
    - **Cantidad a producir** ($X_3$): **6**
        
2. **Aplicar la fórmula:**
    
    $$S_1 = 148,75 - (3,725 \times 6)$$
    
    $$S_1 = 148,75 - 22,35$$
    
    $$S_1 = 126,4$$
    

**Conclusión:** El nuevo valor correcto de $S_1$ es **126,4**.

## Si decide producir 4 kilos de premezcla 3 -> X3 , el nuevo valor de X1 es:?

### 1. Identificación de los Parámetros en la Tabla

Primero extraemos los datos exactos del reporte que la computadora (o la tabla manual) nos devuelve para las variables involucradas:

- **Variable a forzar ($X_3$):** Corresponde a la premezcla 3. Al no estar en la columna "Base", sabemos que es una `[[Variable No Básica]]` y su valor actual es $0$. Se desea forzar una producción de $\theta = 4$ kilos.
- **Variable a analizar ($X_1$):** Corresponde a la premezcla 1. Es una `[[Variable Básica]]`, y su valor actual en la columna solución ($VLD$) es $\lambda_1 = 11,25$.
- **[[Tasa de Sustitución]] ($\lambda_{1,3}$):** Es el valor ubicado en la intersección de la fila de la variable básica ($X_1$) y la columna de la variable que ingresa ($X_3$). En tu tabla, este valor es **$-0,425$**.

### 2. Interpretación Económica del Signo

El profesor hizo mucho énfasis en interpretar correctamente los signos de esta matriz para no cometer errores lógicos:

> [!tip] Regla de la Tasa de Sustitución Negativa Por definición general, una tasa de sustitución positiva indica el "sacrificio" (cuánto debo dejar de fabricar) de la variable básica para hacer una unidad de la nueva. Sin embargo, si la tasa es **negativa** (como nuestro $-0,425$), el significado se invierte: nos indica que por cada unidad que fabriquemos de $X_3$, la producción de $X_1$ **se incrementará**.

### 3. Cálculo Matemático del Nuevo Valor

Para conocer el impacto exacto, aplicamos la fórmula de actualización de variables dictada por el Teorema Fundamental del Método Simplex.

> [!note] Fórmula de Actualización de Variables Básicas $$ X_i^{nuevo} = \lambda_i - \theta \cdot \lambda_{ij} $$ _(Donde $\lambda_i$ es el $VLD$ actual, $\theta$ es la cantidad a producir, y $\lambda_{ij}$ la tasa de sustitución)_.

$$Valor\_Nuevo = Valor\_Actual - (\text{Tasa de Sustitución} \times \text{Cantidad a producir})$$

Reemplazando con los datos de nuestro problema:

1. Planteamos la ecuación: $X_1^{nuevo} = 11,25 - 4 \cdot (-0,425)$
2. Resolvemos el producto: $4 \cdot (-0,425) = -1,7$
3. Aplicamos regla de signos: $X_1^{nuevo} = 11,25 - (-1,7) \Rightarrow 11,25 + 1,7$
4. Resultado final: **$12,95$**

### Conclusión a tu Pregunta

**Respuesta:** Si decide producir 4 kilos de premezcla 3, el nuevo valor de $X_1$ es **$12,95$**.

```
graph TD
    A[Forzar Produccion de X3: 4 kilos] --> B[Identificar Tasa de Sustitucion en fila X1]
    B --> C[Tasa en columna X3 = -0,425]
    C --> D{Que significa el signo negativo?}
    D -->|Incremento| E[En lugar de restar, se suma a la produccion actual]
    E --> F[11,25 + 1,7]
    F --> G[Nuevo valor de X1: 12,95 kilos]
```

_Conceptos relacionados:_ `[[Tasas de Sustitución]]`, `[[Variable Básica]]`, `[[Variable No Básica]]`, `[[Solución Factible Básica]]`.