## 7. MÉTODO SIMPLEX

Este método, desarrollado por George Dantzig en 1947, permite encontrar la solución óptima de cualquier programa lineal, cualquiera sea el número de variables y ecuaciones que lo forman, e identificar aquellos problemas que no tienen solución, o cuya solución óptima es no acotada [^4].

El algoritmo parte de una solución básica inicial (SF en un vértice), y a través de sucesivas iteraciones, explora sistemáticamente los vértices del poliedro de soluciones del Programa Lineal hasta identificar la solución óptima.

Si bien con posterioridad, se han desarrollado métodos que teóricamente son más eficientes en tiempo computacional para problemas de gran tamaño, Simplex ha demostrado en la práctica, un mejor desempeño en la mayoría de los casos, razón por la cual es aún el de mayor difusión.

El método Simplex tiene en cuenta las siguientes propiedades de los puntos extremos o soluciones factibles básicas:

1. (a) Si existe exactamente una solución óptima, entonces debe ser una solución de punto extremo.
(b) Si existen soluciones óptimas múltiples, entonces al menos dos de ellas deben ser soluciones factibles en puntos extremos adyacentes (sólo se consideran las soluciones factibles).

[^3]: La demostración de este teorema puede consultarse en Gass (1979), Capítulo 3.
[^4]: El Teorema que fundamenta el Método Simplex se enuncia y demuestra en el Anexo 2 al final de este Capítulo.

---

*Página 68*

2. Existe sólo un número finito de puntos extremos (soluciones factibles básicas).
3. Si una solución en un vértice es igual o mejor (según el valor de la función objetivo) que todas las soluciones factibles en los vértices adyacentes a ella, entonces es igual o mejor que todas las demás soluciones en los vértices, es decir, es óptima.

Recordemos que gráficamente, cada vértice se forma por la intersección de las rectas representativas de las restricciones y que los valores de las variables para cada punto extremo, se encuentran resolviendo en forma simultánea las ecuaciones de restricción correspondientes a ese vértice.
A su vez, cada punto extremo o vértice corresponde a una solución posible básica del problema.

El método Simplex, basándose en estas conclusiones generales, analiza sistemáticamente los puntos extremos de la región factible hasta identificar el punto óptimo. Asegurándose en cada paso que el vértice analizado no es peor que el anterior, esto es, que le dé a la función objetivo un valor mejor o al menos igual que el anterior.

### UNA VISIÓN GRÁFICA DEL MÉTODO

Trabajemos un problema de fabricación de productos a los que llamamos PI y PII. Los datos del problema se muestran en la tabla.

Su formulación matemática:

**Definición de variables**
- $x_1$ : cantidad a producir del producto 1
- $x_2$ : cantidad a producir del producto 2

$$ \max Z = 4x_1 + 7x_2 $$
Sujetas las variables $x_j$ a:
$$ 10x_1 + 10x_2 \leq 980 \quad \text{(hrs. de mano de obra)} $$
$$ 12x_1 + 24x_2 \leq 1932 \quad \text{(hrs. máquina)} $$
$$ 15x_1 + 10x_2 \leq 1250 \quad \text{(unidades de material prima)} $$
$$ x_j \geq 0, \quad j = 1, 2 $$

---

*Página 69*

Resolvemos gráficamente

> 📊 [Gráfico 10 - Vértice óptimo del problema]

Si analizamos el poliedro de soluciones factibles podemos observar que para cualquier punto interior del mismo siempre habrá un punto de la frontera que le da a la función objetivo un mejor valor, cualquiera sea el objetivo y cualquiera sea la inclinación de la recta que lo representa.

Además, como las restricciones son lineales y la función objetivo también, el óptimo se dará en al menos un vértice del poliedro. Decimos en al menos un vértice porque la recta de isoutilidad (o isocosto) puede coincidir con dos vértices del poliedro de soluciones y en ese caso, tendríamos dos vértices óptimos y los infinitos puntos del segmento de recta que los une.

También, analizando las soluciones del gráfico, observamos que los vértices corresponden a soluciones factibles básicas, es decir que en ellas tenemos como máximo $m$ valores positivos y los restantes nulos, por lo que podemos concluir que la solución óptima (si existe) será una solución factible básica.

Esto que se observa en el gráfico está probado por el **Teorema Fundamental de la PL** que dice:
*Si un problema de Programación Lineal tiene solución óptima, existirá siempre por lo menos una solución factible básica (vértice) que también sea óptima.*

Justamente en este teorema se basa el algoritmo simplex. Simplex parte de una solución básica inicial y a través de sucesivas iteraciones, explora sistemáticamente los vértices del poliedro de soluciones del Programa Lineal hasta identificar la solución óptima.

Por otro lado, sabemos que el número máximo de soluciones factibles básicas está dado por $C_m^n$, entonces simplex identificará el óptimo en un número finito de pasos cuyo máximo está dado justamente por este combinatorio.

---

*Página 70*

El método consta de dos fases, en la primera identifica una solución factible básica (vértice) y la segunda fase corresponde al mejoramiento de esta hasta llegar al óptimo.

Analicemos el método en un gráfico.

> 📊 [Gráfico 11 - Trayectoria del Método Simplex]

Supongamos que se identifica como primer SFB de partida al vértice 0, lo primero que simplex analiza es si es solución óptima o no y lo hace a través de un criterio (criterio de optimidad), evidentemente que este vértice no es óptimo.

Si el vértice no es óptimo, entonces debe decidir hacia dónde se mueve. Siempre pasa de un vértice a otro adyacente (el otro vértice del mismo lado), en nuestro caso será al A o al B. Esto se debe a que solo cambia de una variable por vez, es decir que una variable que en ese vértice es igual a cero asumirá un valor positivo y por lo tanto una de las que son positivas asumirá el valor cero. Para decidir hasta que vértice conviene desplazarse, analiza la tasa de cambio de $Z$, es decir en cuánto se incrementa $Z$ si se mueve una unidad hacia el vértice A y cuál será el incremento si se mueve hacia B. Supongamos que se mueve hacia A, es decir se incrementa $x_2$, el incremento por cada unidad será de \$7 y si se mueve hacia B el incremento por unidad será de \$4, como se trata de un problema de maximización no tendremos dudas de que conviene desplazarse hacia el vértice A. Es necesario aclarar que partiendo del vértice 0 la tasa de crecimiento de $Z$ coincide con los coeficientes $c_j$ pero, como veremos al analizar en detalle el algoritmo, esta situación no se repite para los restantes vértices.

Ahora bien, por cada unidad que se mueva sobre el eje $x_2$, $Z$ crecerá en \$7 por lo que conviene desplazarse lo más posible, pero sin salir del poliedro de soluciones. Simplex utiliza también un criterio que le permite saber cuánto puede desplazarse sin salirse de la región factible, es decir que le indica cómo llegar al vértice A.

---

*Página 71*

Observe que el vértice A es un SFB ya que tiene tres variables positivas ($x_2$, $S_1$ y $S_3$) y dos variables nulas ($x_1$ y $S_2$). Si analizamos el punto F veremos que se trata de una Solución Básica No Factible (SBNoF) porque en este vértice $S_2$ es negativa porque está por encima de la recta que representa el máximo uso de ese recurso (R2), por esto se debe tener cuidado de no pasar de una SFB a una SBNoF.

Si analizamos cuáles variables son positivas y cuáles son iguales a cero, veremos que en A $x_2$ que antes era igual a cero ahora es positiva y la holgura correspondiente a las Hs. Máquina ($S_2$) que antes era positiva ahora es igual a cero. Gráficamente hemos pasado de un vértice a otro adyacente cambiando una variable, en este punto extremo las variables básicas (las que son positivas) son $x_2$, $S_1$ y $S_3$ y las no básicas (o variables nulas) $x_1$ y $S_2$.

Una vez que se llega al vértice A nuevamente se analiza si esta SFB es óptima y si no lo es a cuál vértice, de los adyacentes, conviene moverse. Continúa de esta manera hasta identificar a la solución óptima.

### PASOS DEL MÉTODO SIMPLEX

Teniendo en cuenta lo expresado en el Teorema 3, el algoritmo Simplex busca el óptimo de un problema de PL recorriendo algunos de los vértices del poliedro del conjunto de soluciones factibles de manera que el valor de la función objetivo mejore en cada desplazamiento.

Es decir que analiza las soluciones posibles básicas del problema hasta encontrar la óptima, resolviendo en cada paso un sistema de “m” ecuaciones con “n” variables, de las cuales “n-m” son iguales a cero.

El método consiste fundamentalmente en dos fases:
1. En la primera fase se identifica una solución posible básica que sirva de punto de partida.
2. En la segunda fase...


En la segunda fase o fase iterativa se analiza si dicha solución es o no óptima, y si no lo es, a partir de ella se encuentra una mejor.
El Simplex trabaja con tablas o cuadros, cada uno de ellos corresponde a un punto extremo o vértice del conjunto de soluciones factibles, es decir a una solución posible básica. Las tablas resumen toda la información necesaria de cada solución.

**Primera Fase: identificación de una solución factible básica.**

Los pasos a seguir en esta etapa son:
1. Convertir el modelo a su forma estándar. Esto se logra sumando una variable de holgura al lado izquierdo de las restricciones de $\leq$ y restando una variable de excedente en los primeros miembros de las restricciones de $\geq$. Estas variables deberán interpretarse de acuerdo al significado de la restricción de que se trate, sin embargo, en la función objetivo llevan un coeficiente nulo ya que no agregan nada al

---

*Página 72*

objetivo. En el caso de que en el vector del lado derecho exista algún valor negativo, deberán multiplicarse ambos miembros de la restricción por -1.
2. Analizar la matriz de coeficientes del sistema de ecuaciones de restricción y ver si en ella existen m vectores unitarios con configuración de matriz identidad [^5]. Las variables cuyos coeficientes técnicos ($a_{ij}$) se corresponden con la submatriz identidad, serán las variables consideradas básicas en la solución inicial y sus valores en la solución serán los términos independientes de las restricciones ($b_i$). El resto de las variables serán consideradas no básicas y, por tanto, su valor en la solución será cero. Si la matriz A no contiene una submatriz identidad o existe algún componente negativo en el vector B, no se puede determinar en esta instancia una solución factible básica inicial y por lo tanto no es posible comenzar con Simplex [^6].
3. Armar la tabla de partida, tomando como solución básica inicial la correspondiente a los vectores unitarios identificados en la etapa anterior.

**Segunda Fase: mejoramiento de la solución**

En esta segunda fase se analiza si la solución encontrada es óptima o no, y esto se hace a través de un criterio de optimidad, el que indica si es posible mejorar o no el valor de $Z$.
Si la solución no es óptima, entonces se debe pasar a otra SFB haciendo un cambio de variables en la base. Es decir que, alguna variable no básica –nula- pasa a ser básica –positiva- y alguna variable básica pasa a ser no básica. Esto se conoce como: “determinación de la variable que entra y la variable que sale de la base”.
A continuación se actualiza la tabla simplex y se analiza nuevamente la solución. El procedimiento continúa hasta que el criterio de optimidad indica que la solución hallada es óptima.

1. **Análisis de la solución:** investigar si la solución encontrada se puede mejorar, para ello analizar las diferencias $c_j - z_j$. Estos valores miden el incremento de la función objetivo ante un aumento unitario en el valor de cada una de las variables no básicas. Por lo tanto:
    - Si una variable no básica que tenga asociado un ($c_j - z_j$) > 0 ingresa a la base, el valor de $Z$ aumentará.
    - Si una variable no básica que tenga asociado un ($c_j - z_j$) < 0 ingresa a la base, el valor de $Z$ disminuirá.
    - Si una variable no básica que tenga asociado un ($c_j - z_j$) = 0 ingresa a la base, el valor de $Z$ no se alterará.

    Como consecuencia de lo anterior, la prueba de optimidad dice:

[^5]: O bien m vectores tal que permutando el orden de sus columnas tengan configuración de matriz identidad.
[^6]: Posteriormente se analizará la forma de solucionar este inconveniente a fin de hallar una solución básica de partida.

---

*Página 73*

    - En problemas de maximización, la solución es óptima si todas las diferencias ($c_j - z_j$) son $\leq 0$.
    - En problemas de minimización, la solución es óptima si todas las diferencias ($c_j - z_j$) son $\geq 0$.

2. **Variable de entrada:** determinar la variable que ingresará a la base. La variable que entra a la base debe ser aquella que tenga el mayor incremento positivo en el caso de maximización (o mayor incremento negativo en el caso de minimización), ya que ésta es la variable que aumenta (disminuye) más rápidamente el valor de la función objetivo. Entonces:
    - Si $Z$ es de Maximización, ingresa la variable que verifica mayor diferencia marginal ($c_j - z_j$) > 0.
    - Si $Z$ es de Minimización, ingresa la variable que verifica menor diferencia marginal ($c_j - z_j$) < 0.

3. **Variable de salida:** para determinar la variable que sale de la base, se selecciona aquella que tenga el menor cociente entre su valor en la solución actual ($\lambda_{i0}$) y el coeficiente $\lambda_{ik}$ (siendo $k$ la variable que entra) siempre y cuando dicho coeficiente sea estrictamente positivo, es decir:

$$ \theta = \min \frac{\lambda_{i0}}{\lambda_{ik}} \quad \forall \lambda_{ik} > 0 $$

> **Nota:** En general $\lambda_{ij}$ representa a los coeficientes de la columna de la variable $x_j$.

Este cociente representa el máximo valor que puede tomar la variable entrante, antes que viole las restricciones de no negatividad.
Si todos los $\lambda_{ij}$ son $\leq 0$ la solución es no acotada. Esto significa que la función objetivo podría incrementar (disminuir) infinitamente su valor. Esta situación es prácticamente imposible en la realidad, por lo cual corresponde detener el proceso de cálculo y revisar la modelización del problema.

4. **Actualización:** se debe actualizar la tabla, mediante operaciones elementales en filas.
5. **Criterio de detención:** el proceso se detiene cuando:
    - Si $Z$ es de Maximización: ($c_j - z_j$) $\leq 0$, $\forall j$
    - Si $Z$ es de Minimización: ($c_j - z_j$) $\geq 0$, $\forall j$
    - Para alguna variable no básica que pueda entrar a la base se verifica que todos los $\lambda_{ij}$ son $\leq 0$.

### EJEMPLO DE APLICACIÓN

Retomando nuestro problema de la fábrica de cerámicos, una vez agregadas las variables de holgura a su formulación, nos queda:

---

*Página 74*

$$ \max Z = 8x_1 + 6x_2 + 0S_1 + 0S_2 + 0S_3 $$
**s.a.**
$$ 5x_1 + 5x_2 + S_1 = 300 $$
$$ 4x_1 + 8x_2 + S_2 = 400 $$
$$ 6x_1 + 4x_2 + S_3 = 320 $$
$$ x_1, x_2, S_1, S_2, S_3 \geq 0 $$

Una primera solución posible básica puede encontrarse igualando a cero $x_1$ y $x_2$, de esta manera la solución será:
- $x_1 = 0$
- $x_2 = 0$
- $S_1 = 300$
- $S_2 = 400$
- $S_3 = 320$
y el valor de la función objetivo es, $Z = 0$

Como vemos, se trata de la solución posible básica que corresponde al punto $(0,0)$ en la solución gráfica.

Las variables que son iguales a cero en una SFB, se las denomina variables no básicas y las que asumen un valor positivo son las variables básicas.

Una forma de identificar las variables que serán básicas en la solución de partida, consiste en analizar la matriz A de coeficientes del sistema de ecuaciones de restricción:

$$ \begin{bmatrix} 5 & 5 & 1 & 0 & 0 \\ 4 & 8 & 0 & 1 & 0 \\ 6 & 4 & 0 & 0 & 1 \end{bmatrix} $$

Obsérvese que las columnas que corresponden a las variables básicas son vectores unitarios, esta es justamente, la característica que nos permite identificar las variables que estarán en la base en la primera solución.

Es conveniente expresar esta solución, útil como punto de partida para el Simplex, en una tabla (para facilitar los cálculos que el método requiere).

A continuación, se presenta la estructura de una tabla Simplex con su descripción:

---

*Página 75*

| | | $c_B$ | |
|---|---|---|---|
| $c_B$ | Base | VLD | NOMBRE DE LAS VARIABLES |
| | $z_j$ | | |
| | $c_j - z_j$ | | |

*Tabla 3*

- **Columna Base:** nombre de las variables básicas. Hay un renglón para cada variable básica y este renglón tiene un 1 en la columna que corresponde a dicha variable básica.
- **Columna $c_B$:** coeficientes que preceden a las variables básicas en la función objetivo.
- **Fila $c_j$:** coeficientes que tienen cada una de las variables en la función objetivo.
- **Columna VLD (vector del lado derecho):** contiene los valores de las variables básicas en la presente solución y el valor de la función objetivo.

El cuerpo de la tabla contiene tantas filas como ecuaciones de restricción tenga el problema más dos renglones, uno para $z_j$ y otro para $c_j - z_j$ y tantas columnas como variables tenga el problema.

- **Cálculo de la fila $z_j$:** se determina cada valor como la suma de los productos que se obtienen multiplicando los elementos de la columna $c_B$ por los elementos correspondientes de la j-ésima columna.
- **Cálculo de la fila $c_j - z_j$:** se determina cada valor restando $z_j$ de $c_j$.

Representamos la solución de partida en la tabla 4:

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 | |
|---|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | |
| 0 | $S_1$ | 300 | 5 | 5 | 1 | 0 | 0 | |
| 0 | $S_2$ | 400 | 4 | 8 | 0 | 1 | 0 | |
| 0 | $S_3$ | 320 | 6 | 4 | 0 | 0 | 1 | |
| | $z_j$ | 0 | 0 | 0 | 0 | 0 | 0 | |
| | $c_j - z_j$ | | 8 | 6 | 0 | 0 | 0 | |

*Tabla 4* (Vértice $(0,0)$ de la solución gráfica)

En la columna VLD se encuentra la primera solución, que es como ya lo habíamos dicho:
- $x_1 = 0$
- $x_2 = 0$
- $S_1 = 300$
- $S_2 = 400$
- $S_3 = 320$

En esta solución, $Z = 0$.

---

*Página 76*

Una vez identificada la solución de partida, pasamos a la segunda fase del método o fase iterativa. En ésta debemos analizar si la solución actual es óptima o no y en este último caso, hallar una nueva solución que le proporcione un mejor valor a la función objetivo.

Para saber si la solución encontrada en la tabla 2 es óptima o no, se utiliza el criterio de optimidad -para problema de maximización-: la solución será óptima cuando todas las diferencias $c_j - z_j$ sean menor o igual que cero. Podemos observar que para nuestro ejemplo, hay dos valores positivos, por lo tanto la solución no es óptima.

Para encontrar una nueva SFB, hay que tener en cuenta que, alguna de las variables no básicas en la solución actual, deberá ingresar a la base y, alguna de las variables básicas deberá salir de la base actual (esto es, asumir un valor nulo en la nueva solución).

Primero se selecciona la variable que ingresa a la base y luego la variable que sale. Se debe seguir el siguiente criterio:

**En caso de máximo:**
- **Ingresa a la base** la variable que verifica mayor diferencia marginal ($c_j - z_j$) > 0. En este caso la variable que entra es $x_1$, y a continuación marcamos la columna correspondiente.
- **Sale de la base** se selecciona la variable que tenga el menor cociente entre su valor actual ($\lambda_{i0}$) y el coeficiente $\lambda_{ij}$ (siendo $j=k$ la variable que entra) siempre y cuando dicho coeficiente sea estrictamente positivo, es decir:

$$ \theta = \min \frac{\lambda_{i0}}{\lambda_{ij}} \quad \forall \lambda_{ij} > 0 $$

Una vez determinada la variable que sale de la base, en este caso $S_3$, marcamos la fila correspondiente:

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 | |
|---|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | **$x_1$** | $x_2$ | $S_1$ | $S_2$ | $S_3$ | |
| 0 | $S_1$ | 300 | 5 | 5 | 1 | 0 | 0 | $300/5=60$ |
| 0 | $S_2$ | 400 | 4 | 8 | 0 | 1 | 0 | $400/4=100$ |
| **0** | **$S_3$** | **320** | **6** | **4** | **0** | **0** | **1** | **$320/6=53.33$** |
| | $z_j$ | 0 | 0 | 0 | 0 | 0 | 0 | |
| | $c_j - z_j$ | | 8 | 6 | 0 | 0 | 0 | |

*Tabla 5*

Seleccionadas la variable que ingresa y la que sale de la base, debemos calcular la nueva SFB (otro vértice). Esto se logra incorporando la variable que entra y eliminando la variable que sale. En esta nueva solución las variables básicas serán:
- $S_1, S_2$ y $x_1$

y las variables no básicas:
- $x_2$ y $S_3$.

---

*Página 77*

El valor de la FO en la nueva solución será:
$$ Z_{nuevo} = Z_0 + (C_j - Z_j) \theta $$

Como $x_1$ reemplaza a $S_3$, la columna correspondiente a $x_1$ en la nueva tabla deberá ser el vector unitario:
$$ \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} $$

por lo tanto, tendremos que hallar una matriz equivalente a la matriz A de la solución anterior. Para lograr esto se emplean las siguientes operaciones elementales en filas:
$\Rightarrow$ multiplicar una fila por un número distinto de cero.
$\Rightarrow$ sumarle a una fila otra multiplicada por un número.

Explicamos a continuación el procedimiento para obtener la nueva solución:

**1º.-** armamos nuevamente la tabla colocando a $x_1$ en la base, en lugar de $S_3$, con su correspondiente coeficiente en la columna $c_B$.

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | | | | | | |
| 0 | $S_2$ | | | | | | |
| 8 | $x_1$ | | | | | | |
| | $z_j$ | | | | | | |
| | $c_j - z_j$ | | | | | | |

*Tabla 6*

**2º.-** el número que se encuentra en la intersección entre la columna de la variable que entra y la fila de la variable que sale, se llama **elemento pivot** y en la nueva solución tiene que ser igual a uno.
Para esto multiplicamos toda la fila de $x_1$ por su recíproca, es decir $1/6$, obteniendo de esta manera la fila nueva de la variable $x_1$, como se muestra a en la tabla siguiente:

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | | | | | | |
| 0 | $S_2$ | | | | | | |
| 8 | $x_1$ | $320/6$ | 1 | $4/6$ | 0 | 0 | $1/6$ |
| | $z_j$ | | | | | | |
| | $c_j - z_j$ | | | | | | |

*Tabla 7*

---

*Página 78*

De esta manera, hemos encontrado el elemento unitario del vector $x_1$:
$$ \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} $$

**3º.-** Ahora debemos encontrar los elementos nulos del vector $x_1$. Para ello, usamos la segunda operación elemental en fila. El cero que corresponde a la fila de $S_2$ se obtiene sumando a la fila de $S_2$ (tabla 5), la fila nueva de $x_1$ (tabla 7) multiplicada por -4 (opuesto del número que se desea anular). Esto es:

| VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
|---|---|---|---|---|---|
| 400 | 4 | 8 | 0 | 1 | 0 |
| $+ (320/6) (-4)$ | $+ 1 (-4)$ | $+ (4/6)(-4)$ | $+ 0(-4)$ | $+ 0(-4)$ | $+ (1/6)(-4)$ |
| $1120/6$ | 0 | $32/6$ | 0 | 1 | $-4/6$ |

*Tabla 8*

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | | | | | | |
| 0 | $S_2$ | $1120/6$ | 0 | $32/6$ | 0 | 1 | $-4/6$ |
| 8 | $x_1$ | $320/6$ | 1 | $4/6$ | 0 | 0 | $1/6$ |
| | $z_j$ | | | | | | |
| | $c_j - z_j$ | | | | | | |

*Tabla 9*

**4º.-** A continuación obtenemos el cero correspondiente a la fila de $S_1$ haciendo: la fila $S_1$ más, la fila nueva de $x_1$ multiplicada por -5.

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | $200/6$ | 0 | $10/6$ | 1 | 0 | $-5/6$ |
| 0 | $S_2$ | $1120/6$ | 0 | $32/6$ | 0 | 1 | $-4/6$ |
| 8 | $x_1$ | $320/6$ | 1 | $4/6$ | 0 | 0 | $1/6$ |
| | $z_j$ | | | | | | |
| | $c_j - z_j$ | | | | | | |

*Tabla 10*

**5º.-** Una vez actualizada la tabla, corresponde calcular la fila de $z_j$ y la de $c_j - z_j$ conformando de esta manera la nueva tabla:

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | $200/6$ | 0 | $10/6$ | 1 | 0 | $-5/6$ |
| 0 | $S_2$ | $1120/6$ | 0 | $32/6$ | 0 | 1 | $-4/6$ |
| 8 | $x_1$ | $320/6$ | 1 | $4/6$ | 0 | 0 | $1/6$ |
| | $z_j$ | $1280/3$ | 8 | $32/6$ | 0 | 0 | $8/6$ |
| | $c_j - z_j$ | | 0 | $4/6$ | 0 | 0 | $-8/6$ |

*Tabla 11*

La nueva solución es:

---

*Página 79*

- $x_1 = 320/6$
- $x_2 = 0$
- $S_1 = 200/6$
- $S_2 = 1120/6$
- $S_3 = 0$
- $Z = 1280/3$

Podemos observar que aún no hallamos la solución óptima, ya que para la columna correspondiente a la variable $x_2$ se verifica un valor $c_j - z_j > 0$.

La variable que ingresa a la base en la próxima solución será $x_2$, ya que verifica la mayor diferencia marginal, ($c_2 - z_2$) = $4/6$.
Para determinar la variable que sale de la base calculamos los cocientes entre cada elemento de la columna VLD y los elementos correspondientes de la columna de $x_2$, pero sólo considerando los denominadores positivos. Los cálculos se pueden observar en la tabla 11.

Luego, para pasar a la nueva solución, debemos repetir los pasos 1 a 5. Obtenemos en este caso la siguiente tabla:

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 6 | $x_2$ | 20 | 0 | 1 | $6/10$ | 0 | $-5/10$ |
| 0 | $S_2$ | 80 | 0 | 0 | $-32/10$ | 1 | 2 |
| 8 | $x_1$ | 40 | 1 | 0 | $-4/10$ | 0 | $5/10$ |
| | $z_j$ | 440 | 8 | 6 | $4/10$ | 0 | 1 |
| | $c_j - z_j$ | | 0 | 0 | $-4/10$ | 0 | $-1$ |

*Tabla 12*

Como podemos observar se trata de la solución óptima ya que todas las diferencias marginales ($c_j - z_j$) son negativas o nulas.
La solución óptima es:
- $x_1 = 40$
- $x_2 = 20$
- $S_1 = 0$
- $S_2 = 80$
- $S_3 = 0$
- $Z = 440$

## 8. TÉCNICA DE LA BASE ARTIFICIAL

Al resolver algunos problemas con el método Simplex, muchas veces sucede que no podemos identificar la solución básica de partida.
En general, esto ocurre cuando en el planteo tenemos restricciones de igualdad o inecuaciones del tipo $\geq$. En el primer caso, no es necesario agregar variables de holgura y en el segundo las agregamos restando,


por lo cual no existirán en la matriz A los $m$ vectores unitarios necesarios para formar la primera solución básica.
Para solucionar este problema, se utiliza la técnica de la base artificial o simplemente variables artificiales. Se trata de un artificio matemático por medio del cual, se agregan al problema tantas variables artificiales como vectores unitarios nos falten en la matriz A. De este modo, modificamos el problema original de manera tal que nos permita identificar la solución de partida.
Es importante destacar que estas variables no son variables del problema original. Por ello decimos que, una solución del mismo, se obtiene una vez que se hayan eliminado de la base todas las variables artificiales. Para que el algoritmo Simplex las elimine de la base rápidamente, se deben agregar en la función objetivo precedidas de un coeficiente que deberá ser:
- en caso de maximización, muy grande en valor absoluto y negativo.
- si el problema es de mínimo, muy grande y positivo.

Si se verifica la condición de optimidad y en la base aún queda alguna variable artificial, puede suceder alguna de las siguientes dos cosas:
- Si la variable artificial quedó en la base con un valor positivo, entonces el problema original es no factible.
- Si la variable artificial quedó en la base pero con un valor nulo, entonces la solución encontrada sí es solución del problema original y será degenerada ya que tendrá menos de $m$ valores positivos.

### EJEMPLO DE APLICACIÓN

Supongamos al siguiente problema de PL:
$$ \max Z = 15x_1 + 25x_2 $$
**s.a.**
$$ 5x_1 + 6x_2 \leq 50 $$
$$ 8x_1 + 4x_2 \geq 30 $$
$$ x_2 \leq 5 $$
$$ x_1, x_2 \geq 0 $$

Para comenzar el método Simplex, primero debemos expresar el problema en forma estándar (agregamos las variables de holgura/excedente)

---

*Página 81*

$$ \max Z = 15x_1 + 25x_2 + 0S_1 + 0S_2 + 0S_3 $$
**s.a.**
$$ 5x_1 + 6x_2 + S_1 = 50 $$
$$ 8x_1 + 4x_2 - S_2 = 30 $$
$$ x_2 + S_3 = 5 $$
$$ x_1, x_2, S_1, S_2, S_3 \geq 0 $$

Calculamos el número de variables: $n=5$ y la cantidad de ecuaciones de restricción linealmente independientes: $m=3$. Luego, analizamos a la matriz A para identificar los m vectores unitarios que formen la matriz identidad.

| $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
|---|---|---|---|---|
| 5 | 6 | 1 | 0 | 0 |
| 8 | 4 | 0 | -1 | 0 |
| 0 | 1 | 0 | 0 | 1 |

Observemos que en la matriz A falta el vector unitario:
$$ \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} $$

Para generar este vector, se modifica el problema original agregando nuevas variables que, como no son parte del problema original, se las llama variables artificiales. Recordemos que estas variables se agregan solamente como un artificio matemático a los fines de generar una solución básica de partida, pero no son variables del problema original.
En este ejemplo, como el problema es de maximización, en la función objetivo deben agregarse restadas y precedidas de un coeficiente muy grande.

> **Nota:** Se utilizó –M como coeficiente de $A_1$, pero podría reemplazarse por un valor numérico negativo lo suficientemente grande como para asegurar que en valor absoluto sea mayor que el mayor $c_j$.

Recordemos además que, encontraremos una primera solución del problema original cuando la variable artificial ($A_1$) haya salido de la base.

El problema original modificado es el siguiente:
$$ \max Z = 15x_1 + 25x_2 + 0S_1 + 0S_2 + 0S_3 - MA_1 $$
**s.a.**
$$ 5x_1 + 6x_2 + S_1 = 50 $$
$$ 8x_1 + 4x_2 - S_2 + A_1 = 30 $$
$$ x_2 + S_3 = 5 $$
$$ x_1, x_2, S_1, S_2, S_3, A_1 \geq 0 $$

Si se analiza la matriz A, encontramos los $m$ vectores unitarios:

---

*Página 82*

| $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | $A_1$ |
|---|---|---|---|---|---|
| 5 | 6 | 1 | 0 | 0 | 0 |
| 8 | 4 | 0 | -1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 |

La primera solución básica estará formada por $S_1, S_3$ y $A_1$ como variables básicas y $x_1, x_2$ y $S_2$ como variables no básicas.

Tablas Simplex:

| | | $c_B$ | 15 | 25 | 0 | 0 | 0 | -M |
|---|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | $A_1$ |
| 0 | $S_1$ | 50 | 5 | 6 | 1 | 0 | 0 | 0 |
| -M | $A_1$ | 30 | **8** | 4 | 0 | -1 | 0 | 1 |
| 0 | $S_3$ | 5 | 0 | 1 | 0 | 0 | 1 | 0 |
| | $z_j$ | ---- | -8M | -4M | 0 | M | 0 | -M |
| | $c_j - z_j$ | | $15+8M$ | $25+4M$ | 0 | -M | 0 | 0 |

*Tabla 13*

La variable que entra es $x_1$ y sale $A_1$. Como la variable artificial no es parte del problema original, se puede eliminar su columna ya que no puede volver a entrar a la base, así la nueva tabla es:

| | | $c_B$ | 15 | 25 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | 31,25 | 0 | 3,5 | 1 | 0,625 | 0 |
| 15 | $x_1$ | 3,75 | 1 | 0,5 | 0 | -0,125 | 0 |
| 0 | $S_3$ | 5 | 0 | **1** | 0 | 0 | 1 |
| | $z_j$ | 56,25 | 15 | 7,5 | 0 | -1,875 | 0 |
| | $c_j - z_j$ | | 0 | 17,5 | 0 | 1,875 | 0 |

*Tabla 14*

Aún no llegamos a la solución óptima, la variable que entra es $x_2$ y la que sale es $S_3$.

| | | $c_B$ | 15 | 25 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | 13,75 | 0 | 0 | 1 | **0,625** | -3,5 |
| 15 | $x_1$ | 1,25 | 1 | 0 | 0 | -0,125 | -0,5 |
| 25 | $x_2$ | 5 | 0 | 1 | 0 | 0 | 1 |
| | $z_j$ | 143,75 | 15 | 25 | 0 | -1,875 | 17,5 |
| | $c_j - z_j$ | | 0 | 0 | 0 | 1,875 | -17,5 |

*Tabla 15*

> **Nota:** Para el cálculo de $\theta$ no se consideraron las filas de $x_1$ y $x_2$ porque los denominadores son negativo y nulo respectivamente.

Luego de una iteración más obtenemos la tabla óptima:

| | | $c_B$ | 15 | 25 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_2$ | 22 | 0 | 0 | 1,6 | 1 | -5,6 |
| 15 | $x_1$ | 4 | 1 | 0 | 0,2 | 0 | -1,2 |
| 25 | $x_2$ | 5 | 0 | 1 | 0 | 0 | 1 |
| | $z_j$ | 185 | 15 | 25 | 3 | 0 | 7 |
| | $c_j - z_j$ | | 0 | 0 | -3 | 0 | -7 |

*Tabla 16*

---

*Página 83*

La solución óptima es:
- $x_1 = 4$
- $x_2 = 5$
- $S_1 = 0$
- $S_2 = 22$
- $S_3 = 0$
- $Z = 185$

## 9. CASOS PARTICULARES

Al resolver un problema de PL, pueden presentarse situaciones especiales, las cuales se conocen con el nombre de “casos particulares”.

### 9.1. PROBLEMA CON SOLUCIONES DEGENERADAS

Analicemos la solución gráfica del siguiente PL:
$$ \max Z = 20x_1 + 14x_2 $$
**s.a.**
$$ 8x_1 + 4x_2 \leq 28 $$
$$ 2x_1 + 2x_2 \leq 10 $$
$$ 8x_1 + 2x_2 \leq 22 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 12 - Solución degenerada. En el vértice óptimo (A) se intersectan tres restricciones, el vértice A está sobre definido. Esto hace que en ese punto se anulen más de n-m variables y por lo tanto que la solución sea degenerada]

Veamos ahora las últimas dos tablas simplex para este problema:

| | | $c_B$ | 20 | 14 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | 8 | 4 | 0 | 1 | 0 | -2 |
| 0 | $S_2$ | 12 | 6 | 0 | 0 | 1 | -1 |
| 14 | $x_2$ | 5 | 1 | 1 | 0 | 0 | 0,5 |
| | $z_j$ | 70 | 14 | 14 | 0 | 0 | 0 |
| | $c_j - z_j$ | | 6 | 0 | 0 | 0 | -7 |

*Tabla 17*

Observe que existe un empate entre $S_1$ y $S_2$ al decidir la variable que sale de la base. En principio, se puede seleccionar como variable de salida a cualquiera de las dos. Si elegimos sacar $S_2$ (tabla 19) se observa que $S_1$ se hace nula en la columna VLD. En este caso la solución encontrada es una solución degenerada

---

*Página 84*

| | | $c_B$ | 20 | 14 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | 0 | 0 | 0 | 1 | -0,667 | -1,33 |
| 20 | $x_1$ | 2 | 1 | 0 | 0 | 0,167 | -0,167 |
| 14 | $x_2$ | 3 | 0 | 1 | 0 | -0,167 | 0,667 |
| | $z_j$ | 82 | 20 | 14 | 0 | 1 | 6 |
| | $c_j - z_j$ | | 0 | 0 | 0 | -1 | -6 |

*Tabla 18*

> **Nota:** A partir de la tabla 18, realice los cálculos con $S_1$ como variable de salida y observe qué sucede.

Una situación similar se presenta si se seleccionara $S_1$ como variable de salida.
La degeneración se observa cuando el vector solución verifica menos de $m$ valores positivos o más de ($n - m$) valores nulos.
Recordemos que también se presenta un caso de problema degenerado cuando en la solución óptima quedan variables artificiales nulas.

### 9.2. PROBLEMA CON MÚLTIPLES SOLUCIONES ÓPTIMAS

Observe el siguiente PL y su solución gráfica:
$$ \min Z = 80x_1 + 80x_2 $$
**s.a.**
$$ 5x_1 + 5x_2 \leq 500 $$
$$ x_1 \geq 40 $$
$$ x_2 \geq 25 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 13 - La recta z NO es paralela a una restricción limitante. Solución única en D]

Compare el gráfico anterior con el del PL que se da a continuación:
$$ \max Z = 80x_1 + 40x_2 $$
**s.a.**
$$ 5x_1 + 5x_2 \leq 350 $$
$$ 12x_1 + 6x_2 \leq 600 $$
$$ x_2 \leq 60 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 14 - En este caso la recta de isoutilidad (z) también es paralela a una de las restricciones. Solución múltiple en el segmento AB]

La diferencia entre los dos casos mostrados es que en el segundo, la recta z es paralela a una restricción limitante. Esto implica que existirán dos vértices que son óptimos, el A y el B, y además todos los puntos que forman el segmento de recta que los une.
La tabla óptima del simplex del problema de maximización es:


| | | $c_B$ | 80 | 40 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | 100 | 0 | 2,5 | 1 | 0 | -0,417 | $40 = \theta$ |
| 80 | $x_1$ | 50 | 1 | 0,5 | 0 | 0 | 0,083 | 100 |
| 0 | $S_2$ | 60 | 0 | 1 | 0 | 1 | 0 | 60 |
| | $z_j$ | 4000 | 80 | 40 | 0 | 0 | 6,67 |
| | $c_j - z_j$ | | 0 | 0 | 0 | 0 | -6,67 |

*Tabla 19*

Observe que la diferencia $c_2 - z_2$ es igual a cero y la variable $x_2$ no es básica.
Esto significa que si introducimos $x_2$ a la base y eliminamos la que corresponda, en este caso $S_1$, obtendremos otra solución que le dará a $Z$ el mismo valor. Esto es así, porque según el Teorema que fundamenta el Método Simplex [^7], el valor de una nueva solución se obtiene calculando:

$$ Z_{nuevo} = Z_0 + (c_j - z_j)\theta $$
$$ Z_{nuevo} = 4000 + 0(40) = 4000 $$

Luego, de acuerdo al Teorema 2, mediante combinaciones lineales convexas podemos obtener infinitas soluciones óptimas.
Este caso especial se origina cuando el conjunto de soluciones óptimas está formado por más de un elemento, por lo que, de acuerdo con el teorema 1 y 2 de combinaciones lineales convexas, decimos que el problema posee una infinidad de soluciones óptimas.

Una excepción a este caso particular se ve en el siguiente gráfico.
$$ \max Z = 240x_1 + 120x_2 $$
**s.a.**
$$ 8x_1 + 4x_2 \leq 28 $$
$$ 2x_1 + 2x_2 \leq 10 $$
$$ 8x_1 + 2x_2 \leq 22 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 15 - Observe que la recta Z es paralela a una de las restricciones limitantes, pero, al ser un óptimo degenerado no tiene múltiples soluciones óptimas.]

Sin embargo, esto no sucede en todos los problemas que tienen óptimo degenerado, como puede verse a continuación.

[^7]: Ver la demostración de este Teorema en el Anexo 2 al final de este Capítulo.

---

*Página 86*

$$ \max Z = 60x_1 + 60x_2 $$
**s.a.**
$$ 8x_1 + 4x_2 \leq 28 $$
$$ 2x_1 + 2x_2 \leq 10 $$
$$ 8x_1 + 2x_2 \leq 22 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 16 - La misma región factible del problema anterior, pero Z es paralela a otra de las restricciones limitantes y en este caso se puede observar que existen múltiples soluciones óptimas siendo una de ellas degenerada.]

### 9.3. PROBLEMA NO ACOTADO

A continuación se muestra un PL y su solución gráfica
$$ \max Z = 2x_1 + x_2 $$
**s.a.**
$$ x_1 - x_2 \geq 10 $$
$$ x_2 \leq 20 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 17 - Z crece indefinidamente. Observe que la recta Z puede ser desplazada en su sentido de optimidad sin llegar nunca al óptimo.]

Esta situación en la tabla simplex:

| | | $c_B$ | 2 | 1 | 0 | 0 |
|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ |
| 2 | $x_1$ | 30 | 1 | 0 | -1 | 0,5 |
| 1 | $x_2$ | 20 | 0 | 1 | 0 | 0,5 |
| | $z_j$ | 80 | 2 | 1 | -2 | 1,5 |
| | $c_j - z_j$ | | 0 | 0 | 2 | -1,5 |

*Tabla 20*

Es imposible seleccionar la variable que sale, ya que todos los elementos de la columna de $S_1$ son negativos y ceros. En este caso debe detenerse el proceso y revisar el planteo, puesto que esto surge justamente de un error en la modelización del problema.
Podemos decir que un PL es no acotado cuando el conjunto de soluciones factibles es un conjunto convexo abierto y el sentido de optimización del funcional se dirige hacia la zona no acotada del mismo.

### 9.4. PROBLEMA INCOMPATIBLE

$$ \max Z = 20x_1 + 30x_2 $$
**s.a.**
$$ 10x_1 + 5x_2 \leq 150 $$
$$ 5x_1 + 6x_2 \leq 100 $$
$$ x_2 \geq 20 $$
$$ x_1, x_2 \geq 0 $$

> 📊 [Gráfico 18 - En el gráfico se puede ver que no existe una región factible. El sistema de restricciones es incompatible.]


## 10. INTERPRETACIÓN ECONÓMICA DE LA TABLA SIMPLEX

Antes de comenzar con el análisis de post-optimidad, vamos a realizar una interpretación de cada uno de los elementos de la tabla simplex.
Este tema se conoce también como análisis económico del método Simplex.

Continuaremos con nuestro problema de la producción de cerámicos, recordemos los requerimientos de insumos, como así también la contribución a las utilidades de cada producto:

| | Cerámico Esmaltado | Cerámico Rústico | Disponibilidad hrs. mensuales |
|---|---|---|---|
| Horas de Mano de Obra / $m^2$ | 5 | 5 | 300 |
| Horas de Secado / $m^2$ | 4 | 8 | 400 |
| Horas de Cocción / $m^2$ | 6 | 4 | 320 |
| Contrib. a las utilidades / $m^2$ | 8 | 6 | |

*Tabla 22*

Objetivo: Maximizar la contribución total a las utilidades mensuales.
**Definición de variables:**
- $x_1$ = $m^2$ de cerámico esmaltado a producir mensualmente.
- $x_2$ = $m^2$ de cerámico rústico a producir mensualmente.

$$ \max Z = 8x_1 + 6x_2 $$
**S.a.**
$$ 5x_1 + 5x_2 \leq 300 \quad \text{Hrs. M O} $$
$$ 4x_1 + 8x_2 \leq 400 \quad \text{Hrs. Secado} $$
$$ 6x_1 + 4x_2 \leq 320 \quad \text{Hrs. Cocción} $$
$$ x_1, x_2 \geq 0 $$

Agregamos variables de holgura:
$$ \max Z = 8x_1 + 6x_2 + 0S_1 + 0S_2 + 0S_3 $$
**S.a.**
$$ 5x_1 + 5x_2 + S_1 = 300 \quad \text{Hrs. M O} $$
$$ 4x_1 + 8x_2 + S_2 = 400 \quad \text{Hrs. Secado} $$
$$ 6x_1 + 4x_2 + S_3 = 320 \quad \text{Hrs. Cocción} $$
$$ x_1, x_2, S_1, S_2, S_3 \geq 0 $$

- $S_1$ = cantidad de sobrante de horas de mano de obra.
- $S_2$ = cantidad de sobrante de horas de secado.
- $S_3$ = cantidad de sobrante de horas de cocción.

La tabla que se muestra a continuación es la que se obtiene luego de una iteración de Simplex:

---

*Página 89*

| | | $c_B$ | 8 | 6 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| $c_B$ | Base | VLD | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ |
| 0 | $S_1$ | $200/6$ | 0 | $10/6$ | 1 | 0 | $-5/6$ |
| 0 | $S_2$ | $1120/6$ | 0 | $32/6$ | 0 | 1 | $-4/6$ |
| 8 | $x_1$ | $320/6$ | 1 | $4/6$ | 0 | 0 | $1/6$ |
| | $z_j$ | $1280/3$ | 8 | $32/6$ | 0 | 0 | $8/6$ |
| | $c_j - z_j$ | | 0 | $4/6$ | 0 | 0 | $-8/6$ |

*Tabla 23*

Según esta solución, produciendo $320/6$ $m^2$ de cerámico esmaltado y nada de cerámico rústico, se tendrá un beneficio de \$ $1280/3$.
Con este plan de producción se usarán todas las horas de cocción, quedando un excedente de $200/6$ horas de mano de obra y $1120/6$ horas de secado.

Además podemos decir que el plan de producción no es el óptimo y por lo tanto no se obtiene la máxima contribución a las utilidades posible.
Vamos a analizar qué sucede si decidimos producir algunos $m^2$ de cerámico rústico, que según este plan no estamos fabricando.

Para producir un $m^2$ de rústico necesitamos 5 horas de mano de obra, 8 horas de secado y 4 horas de cocción. Con las HMO y horas de secado no hay inconvenientes, ya que en este momento tenemos excedentes; no ocurre lo mismo con las horas de cocción debido a que -para el plan de producción actual- se trata de un recurso limitante (variable de holgura nula).

Es decir que, si queremos producir un $m^2$ de cerámico rústico necesariamente deberemos dejar de fabricar algo del cerámico esmaltado, para así poder liberar horas de cocción.

Al disminuir la producción del cerámico esmaltado, para poder fabricar cerámico rústico, sufrirán también modificaciones los excedentes de los otros insumos.
Todo este análisis, como así también la modificación que se producirá en el objetivo, lo encontramos en la columna correspondiente a $x_2$.

| | | $c_B$ | 6 |
|---|---|---|---|
| $c_B$ | Base | VLD | $x_2$ |
| 0 | $S_1$ | $200/6$ | $10/6$ |
| 0 | $S_2$ | $1120/6$ | $32/6$ |
| 8 | $x_1$ | $320/6$ | $4/6$ |
| | $z_j$ | $1280/3$ | $32/6$ |
| | $c_j - z_j$ | | $4/6$ |

**Interpretación de los valores de la columna $x_2$:**
- **Tasa de sustitución $\lambda_{ij}$ (valores $10/6$, $32/6$, $4/6$):** Cuánto se deberá disminuir la producción de cerámico esmaltado (o excedentes) para poder producir 1 $m^2$ de cerámico rústico.
- **$z_2 = 32/6$:** contribución que se pierde por unidad que se fabrique.
- **$c_2 - z_2 = 4/6$:** incremento marginal unitario de $Z$.

---

*Página 90*

**Tasas de sustitución:** en general indican, si su signo es positivo, el "sacrificio" que se deberá hacer de la variable básica $x_i$ para incrementar en una unidad la variable no básica $x_j$. Si la tasa de sustitución es negativa indica el incremento que se producirá en la variable básica.

En nuestro ejemplo $4/6$ significa que, para poder fabricar un $m^2$ de cerámico rústico, deberemos dejar de producir $4/6$ de $m^2$ de cerámico esmaltado.
Esto se debe a que para poder producir un $m^2$ de cerámico rústico se necesitan 4 horas de cocción, mientras que para producir un $m^2$ del cerámico esmaltado se necesitan 6 horas de cocción; entonces si se dejan de fabricar $4/6$ $m^2$ del cerámico esmaltado, tendremos:

$$ 6 \cdot \frac{4}{6} = 4 $$
(horas de cocción por $m^2$ de cerámico esmaltado $\times$ $m^2$ de cerámico esmaltado a disminuir) = horas de cocción liberadas en la producción del cerámico esmaltado (que son las que necesitamos para producir un $m^2$ de cerámico rústico).

El valor $\lambda_{12} = 10/6$, nos dice que por cada $m^2$ que se incremente la producción de cerámico rústico, el excedente de HMO se reducirá en $10/6$.
Mientras que $\lambda_{22} = 32/6$, indica que por cada $m^2$ que se incremente la producción de cerámico rústico, el excedente de horas de secado se reducirá en $32/6$.

En cuanto a $z_j$ expresa la contribución que se pierde por $m^2$ que se fabrica de cerámico rústico – originado por la reducción de la producción de cerámico esmaltado-. Es decir, $z_2 = 32/6$ expresa que el cambio que se necesita realizar en el plan de producción, para poder fabricar un $m^2$ de cerámico rústico, disminuye la contribución a las utilidades en \$$32/6$.

Comparando este "costo" con la contribución unitaria de cerámico rústico, podremos decidir si nos conviene o no hacer dicha modificación en el plan de producción, es decir:

$$ c_2 - z_2 = 6 - \frac{32}{6} = \frac{4}{6} $$

Este valor representa el incremento neto unitario de la función objetivo, como es positivo, lógicamente nos convendrá fabricar el cerámico rústico, ya que por cada $m^2$, la contribución total a las utilidades crecerá en \$ $4/6$.
Si nos conviene fabricar un $m^2$, entonces nuestra intención será producir todos los $m^2$ que se puedan. Así el paso siguiente es determinar cuántas unidades podremos fabricar con los recursos que tenemos.

---

*Página 91*

Vamos a llamar $\theta$ a esa cantidad. Para encontrar el valor de $\theta$ usamos las tasas de sustitución de la siguiente manera:
Sabemos que por cada unidad en que se aumente $x_2$, $x_1$ disminuirá en $4/6$; la pregunta es:

¿Hasta cuántos $m^2$ se puede disminuir $x_1$?
Seguramente coincidiremos en que lo máximo que puede disminuirse es $320/6$ (la producción actual), ya que todas las variables deben respetar la restricción de no negatividad.
Podemos escribir esto de la siguiente manera:
$$ \frac{4}{6} \theta \leq \frac{320}{6} $$

Usando para los excedentes de horas de mano de obra ($S_1$) y horas de secado ($S_2$), el mismo razonamiento que para $x_1$, podemos escribir las siguientes inecuaciones:
$$ \frac{10}{6} \theta \leq \frac{200}{6} $$
$$ \frac{32}{6} \theta \leq \frac{1120}{6} $$

El valor de $\theta$ que cumpla con las tres inecuaciones, será el nuevo valor para $x_2$.

Resolviendo:
$$ \frac{10}{6} \theta \leq \frac{200}{6} \Rightarrow \theta \leq 20 $$
$$ \frac{32}{6} \theta \leq \frac{1120}{6} \Rightarrow \theta \leq 35 $$
$$ \frac{4}{6} \theta \leq \frac{320}{6} \Rightarrow \theta \leq 80 $$

Vemos que el nuevo valor de $x_2$ es 20 (el único valor que verifica las tres inecuaciones)

Utilizando todo lo que tenemos hasta ahora podemos conocer la solución completa.
Valores de las variables:
- $x_1 = \frac{320}{6} - \left(20 \cdot \frac{4}{6}\right) = 40$
- $x_2 = 20$
- $S_1 = \frac{200}{6} - \left(20 \cdot \frac{10}{6}\right) = 0$
- $S_2 = \frac{1120}{6} - \left(20 \cdot \frac{32}{6}\right) = 80$
- $S_3 = 0$

El nuevo valor de Z:
$$ Z = \frac{1280}{3} + \left(20 \cdot \frac{4}{6}\right) = 440 $$

---

*Página 92*

En forma general y de acuerdo a lo demostrado en el teorema fundamental del método simplex, podemos decir que los valores de las variables para la nueva solución se calculan como:

$$ x_i = \lambda_{i0} - \theta \lambda_{ij} \quad (i = 1...m) $$
$$ x_j = \theta $$
$$ x_k = 0 \quad (k \neq 1, 2, ...m, j) $$

Mientras que el nuevo valor del funcional es:
$$ Z_{nuevo} = Z_0 + \theta (c_j - z_j) $$

---

*Página 93*

## ANEXO 1
**MODELO DE PROGRAMACIÓN MATEMÁTICA**

Formalmente un modelo de Programación Matemática tiene la siguiente estructura:
**Óptimo** $Z = f(x)$
**Sujeto a:**
$$ g_i(x) \leq b_i \quad \text{para } i \in I_1 $$
$$ g_i(x) \geq b_i \quad \text{para } i \in I_2 $$
$$ g_i(x) = b_i \quad \text{para } i \in I_3 $$

Siendo $I_1, I_2, \text{e } I_3$ una partición del conjunto de índices $I = \{1, 2, \ldots, m\}$.
Donde $m$ representa el número total de ecuaciones y/o inecuaciones de restricción existentes en el modelo.

Podemos decir que estamos frente a un problema de Programación Matemática si el mismo trata de optimizar (maximizar o minimizar) una función donde las variables pueden asumir únicamente los valores que verifican un conjunto de restricciones expresadas como ecuaciones y/o inecuaciones.

De acuerdo a las características de la función objetivo y las restricciones, un modelo de Programación Matemática, puede ser de:
- **Programación Lineal:** cuando la función objetivo y todas las restricciones son lineales.
- **Programación Lineal Entera:** si algunas o todas las variables del modelo deben ser enteras.
- **Programación No Lineal:** cuando la función objetivo y/o alguna o todas las restricciones son no lineales.
- **Programación Multiobjetivo:** cuando existe más de una función objetivo.

---

*Página 94*

## ANEXO 2
**TEOREMA QUE FUNDAMENTA EL MÉTODO SIMPLEX**

Dantzig desarrolló el método Simplex basándose en el teorema fundamental de la PL que sostiene que: *“Si un problema de PL es resoluble, existe al menos una solución posible básica que será también óptima”*. Por esta razón es que sólo consideramos las soluciones de los vértices del poliedro y descartamos las de punto interior.

Partimos de un PL expresado en forma estándar vectorial:
$$ \max Z = c_1x_1 + c_2x_2 + \ldots + c_nx_n \quad (1) $$
**s.a.**
$$ P_1x_1 + P_2x_2 + \ldots + P_nx_n = P_0 \quad (2) $$
$$ x_j \geq 0 \quad (j = 1, 2, \ldots, n) $$

Consideramos conocida un solución factible (posible) básica (SFBND) de este problema, en la que suponemos que los $m$ valores positivos son los $m$ primeros (es decir que los nulos serán los $n-m$ restantes).
Llamaremos a cada elemento de este vector solución $\lambda_{i0}$, es decir:

$$ X = \begin{bmatrix} \lambda_{10} > 0 \\ \lambda_{20} > 0 \\ \vdots \\ \lambda_{m0} > 0 \\ \lambda_{m+1, 0} = 0 \\ \vdots \\ \lambda_{n0} = 0 \end{bmatrix} $$

Siendo una solución verificará (2) y le dará a Z un valor $Z_0$, es decir:
$$ Z_0 = c_1\lambda_{10} + c_2\lambda_{20} + \ldots + c_m\lambda_{m0} \quad (3) $$
**s.a.**
$$ P_1\lambda_{10} + P_2\lambda_{20} + \ldots + P_m\lambda_{m0} = P_0 \quad (4) $$

Al ser una SFB los vectores $P_1, P_2, \ldots, P_m$ son linealmente independientes (es decir constituyen una base en el espacio m-dimensional) por lo que podremos expresar cualquier vector no básico como combinación lineal de ellos.
Tomemos un vector no básico cualquiera ($P_j$ para $j = m+1, m+2, \ldots, n.$) y lo expresemos como combinación lineal de los vectores básicos ($P_i, i = 1, 2, \ldots, m$) mediante escalares que llamaremos $\lambda_{ij}$

$$ P_1\lambda_{1j} + P_2\lambda_{2j} + \ldots + P_m\lambda_{mj} = P_j \quad (5) $$


$$ \begin{bmatrix} \lambda_{12} \\ \lambda_{32} \\ \lambda_{42} \end{bmatrix} = \begin{bmatrix} 4/6 \\ 10/6 \\ 32/6 \end{bmatrix} $$

Resolviendo este sistema, obtenemos el valor de los escalares:
- $\lambda_{12} = 4/6$
- $\lambda_{32} = 10/6$
- $\lambda_{42} = 32/6$

Observemos que cada $\lambda_{ij}$ mide la reducción que se debe realizar en el valor de las variables básicas i (i= 1, 3, 4), a fin de liberar los recursos necesarios para introducir una unidad de $x_2$.

Calculamos además:
$$ z_2 = c_1\lambda_{12} + c_3\lambda_{32} + c_4\lambda_{42} = 8(4/6) + 0(10/6) + 0(32/6) = 32/6 $$

El valor $z_2$ mide el costo de introducir a la base la variable no básica $x_2$ (a nivel unitario), medido en términos de la reducción que debe efectuarse en las variables básicas.
A partir de este valor calculamos la contribución neta que se obtendrá por producir una unidad de $x_2$:
$$ c_2 - z_2 = 6 - 32/6 = 4/6 $$

De acuerdo al teorema que fundamenta el método Simplex, como $c_2 > z_2$, podemos mejorar la solución actual, si introducimos a la base la variable $x_2$.

Dado que producir a nivel unitario $x_2$ mejora el objetivo en $4/6$, es lógico intentar ingresar esta variable al mayor valor posible (es decir, aquel valor permitido por la disponibilidad de insumos). Llamaremos $\theta$ a ese valor y planteamos las siguientes relaciones que nos permitirán calcular el mayor valor al cual se puede ingresar $x_2$:

---

*Página 98*

$$ \lambda_{10} - \theta \lambda_{12} \geq 0 \Rightarrow 320/6 - (4/6 \theta) \geq 0 \Rightarrow \theta \leq 80 $$
$$ \lambda_{30} - \theta \lambda_{32} \geq 0 \Rightarrow 200/6 - (10/6 \theta) \geq 0 \Rightarrow \theta \leq 20 $$
$$ \lambda_{40} - \theta \lambda_{42} \geq 0 \Rightarrow 1120/6 - (32/6 \theta) \geq 0 \Rightarrow \theta \leq 35 $$

De donde $\theta = 20$, es el valor que verifica el sistema de inecuaciones y por lo tanto decimos que es el valor al cual ingresará la variable $x_2$ a la base en la próxima solución.

Para conocer cómo se modifican las variables básicas en la nueva solución, calculamos:
- $x_1 = \lambda_{10} - \theta \lambda_{12} = 320/6 - (20 \cdot 4/6) = 40$
- $x_3 = \lambda_{30} - \theta \lambda_{32} = 200/6 - (20 \cdot 10/6) = 0$
- $x_4 = \lambda_{40} - \theta \lambda_{42} = 1120/6 - (20 \cdot 32/6) = 80$

Resumiendo, el vector correspondiente a la nueva solución es:
$$ X = \begin{bmatrix} 40 \\ 20 \\ 0 \\ 80 \\ 0 \end{bmatrix} $$

El valor de Z para esta nueva solución lo calculamos como:
$$ Z_{nuevo} = Z_0 + \theta(c_2 - z_2) = 1280/3 + 20(4/6) = 440 $$

El proceso se repite hasta que $\forall j \therefore c_j \leq z_j$

---

*Página 99*
