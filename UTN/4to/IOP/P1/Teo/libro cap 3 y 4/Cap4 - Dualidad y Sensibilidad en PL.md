# CAPÍTULO 4 - DUALIDAD Y SENSIBILIDAD EN PL

## 1. INTRODUCCIÓN

En el capítulo anterior se describieron las características de los modelos de programación lineal, así como los diferentes caminos a partir de los cuales encontrar la solución: resolución gráfica y algoritmo Simplex.
En este capítulo, se describen dos técnicas relacionadas con la programación lineal: la dualidad y el análisis de sensibilidad.

En la primera parte se desarrolla la teoría asociada a la dualidad: cómo se obtiene el dual de un programa lineal, la interpretación del concepto de precio sombra y una serie de teoremas y resultados útiles para la interpretación de un modelo lineal.

En la segunda parte se muestran las posibilidades del análisis de sensibilidad en la programación lineal. Se tratará de analizar cómo varía la solución del modelo (tanto el valor de la función objetivo como el valor de las variables de decisión) en función de dos conjuntos de parámetros del modelo: los coeficientes de la función objetivo y los términos independientes de las restricciones.

## 2. LA DUALIDAD EN LA PROGRAMACIÓN LINEAL

Comenzaremos el tratamiento de este tema mediante el análisis de nuestro ejemplo de la fábrica de cerámicos. El modelo lineal de este problema era:
- $x_1$ : $m^2$ de cerámicos esmaltados a fabricar mensualmente.
- $x_2$ : $m^2$ de cerámicos rústicos a fabricar mensualmente.

$$ \max Z = 8x_1 + 6x_2 $$
**s.a.**
$$ 5x_1 + 5x_2 \leq 300 \quad \text{Hs de Mano de Obra} $$
$$ 4x_1 + 8x_2 \leq 400 \quad \text{Hs de Secado} $$
$$ 6x_1 + 4x_2 \leq 320 \quad \text{Hs de Cocción} $$
$$ x_1, x_2 \geq 0 $$

---

*Página 109*

Vamos a suponer que la empresa tiene la posibilidad de "vender" los insumos que utiliza para su producción; es lógico que en ese caso pretenda recibir como "mínimo" lo que obtiene si los usa en la fabricación de sus productos. Es decir que ella desea determinar el "precio" de los recursos, por debajo del cual ya no le conviene venderlos; en definitiva, quiere averiguar el "valor" de esos recursos.

Definimos a las variables $y_1, y_2$ y $y_3$ como los precios unitarios de los recursos Hs. de Mano de Obra, Hs. de Secado y Hs. de Cocción, respectivamente.
Como su objetivo es encontrar el precio mínimo al que debería vender estos recursos, entonces:

$$ \min G = 300 y_1 + 400 y_2 + 320 y_3 $$

Como dijimos, la empresa debería recibir como mínimo lo que obtiene si los usa en su producción, así la contribución a las utilidades de cada producto nos da un límite inferior para estos precios.

Es decir que si en lugar de fabricar un $m^2$ de cerámicos esmaltados, vendemos 5 horas de mano de obra, 4 horas de secado y 6 horas de Cocción, como mínimo debemos recibir la contribución a las utilidades que proporciona dicho producto. Podemos expresar esto de la siguiente manera:

$$ 5 y_1 + 4 y_2 + 6 y_3 \geq 8 $$

Usando el mismo razonamiento para el otro tipo de cerámico, obtenemos:

$$ 5 y_1 + 8 y_2 + 4 y_3 \geq 6 $$

Además, como estamos considerando precios:
$$ y_1, y_2, y_3 \geq 0 $$

Observemos que, con los mismos datos del problema original, hemos formulado otro PL que brindará información sobre el “valor” que los recursos tienen para la empresa, lo que en economía se conoce como precio sombra o valor marginal del recurso.

Si ahora resolvemos ambos problemas, observamos que los valores óptimos son iguales; esto era de esperarse ya que la empresa no aceptaría, por la venta de sus insumos, menos dinero del que podría obtener si los utiliza en la fabricación de sus productos.

### EL PROBLEMA DUAL

Decimos entonces que, para cada problema de programación lineal existe siempre asociado al mismo, otro problema lineal. A este nuevo programa, se lo puede emplear para obtener la solución del problema original y además sus variables proporcionan información útil acerca de la solución óptima del problema lineal original.

---

*Página 110*

A los fines del desarrollo de este tema, convendremos en llamar “primal” al programa original y “dual” al problema lineal asociado.

Existen varias formas de dualidad: canónica o simétrica, dualidad estándar y dualidad mixta, el nombre de cada una de ellas se origina de acuerdo con la forma en que se presente el problema original.

### Forma Canónica de la Dualidad

Si el problema primal esta dado en la forma:
**Maximizar** $CX$
$$ AX \leq B $$
$$ X \geq 0 $$

Entonces el problema dual asociado será de la forma:
**Minimizar** $B'Y$
$$ A'Y \geq C' $$
$$ Y \geq 0 $$

Por ejemplo, dado el problema primal:
$$ \max Z = 8x_1 + 6x_2 $$
**S.a.**
$$ 5x_1 + 5x_2 \leq 300 $$
$$ 4x_1 + 8x_2 \leq 400 $$
$$ 6x_1 + 4x_2 \leq 320 $$
$$ x_1, x_2 \geq 0 $$

El programa dual asociado es:
$$ \min G = 300y_1 + 400y_2 + 320y_3 $$
**S.a.**
$$ 5y_1 + 4y_2 + 6y_3 \geq 8 $$
$$ 5y_1 + 8y_2 + 4y_3 \geq 6 $$
$$ y_1, y_2, y_3 \geq 0 $$

Observemos que, cada restricción del primal se relaciona con una variable principal del dual, y viceversa. Es decir, la primera restricción primal se corresponde con la primera variable dual, la segunda restricción primal, con la segunda variable dual y así sucesivamente.
Razón por la cual decimos que, si el programa primal tiene $n$ variables principales y $m$ restricciones, el dual tendrá $m$ variables principales y $n$ restricciones.

### Forma Estándar de la Dualidad

Si el problema primal esta dado en la forma:
**Maximizar** $CX$
$$ AX = B $$
$$ X \geq 0 $$

---

*Página 111*

Entonces el problema dual asociado será de la forma:
**Minimizar** $B'Y$
$$ A'Y \geq C' $$
$$ Y \text{ sin restricción de signo} $$

Por ejemplo, dado el problema primal:

| Programa Primal | Programa Dual |
|---|---|
| $\max Z = 20x_1 + 60x_2$ | $\min G = 100y_1 + 20y_2 + 40y_3$ |
| **S.a.** | **S.a.** |
| $5x_1 + 10x_2 = 100$ | $5y_1 + y_2 + 2y_3 \geq 20$ |
| $x_1 + 8x_2 = 20$ | $10y_1 + 8y_2 + 12y_3 \geq 60$ |
| $2x_1 + 12x_2 = 40$ | |
| $x_1, x_2 \geq 0$ | $y_1, y_2, y_3 \text{ sin restricción}$ |

Cabe aclarar que Bazaraa et. al. (1981) demuestran que el dual del dual es el primal, por lo cual las definiciones dadas se pueden aplicar al revés y los términos “primal” y “dual” son relativos al marco de referencia que se seleccione.

### Forma Mixta de la Dualidad

A los fines de plantear el modelo dual de un programa lineal presentado en forma mixta, debemos tener en cuenta la relación que existe entre las restricciones de uno de los programas y las variables del otro. En el siguiente cuadro se resumen las diferentes situaciones que se pueden presentar:

| Problema de Máximo | | | Problema de Mínimo | |
|---|---|---|---|---|
| **Restricción** | Canónica | $\leq$ | $\rightarrow$ | $\geq 0$ | No Negativa | **Variable** |
| | No Canónica | $\geq$ | $\rightarrow$ | $\leq 0$ | No Positiva | |
| | Igualdad | $=$ | $\rightarrow$ | n/r | No Restringida | |
| **Variable** | No Negativa | $\geq 0$ | $\rightarrow$ | $\geq$ | Canónica | **Restricción** |
| | No Positiva | $\leq 0$ | $\rightarrow$ | $\leq$ | No Canónica | |
| | No Restringida | n/r | $\rightarrow$ | $=$ | Igualdad | |

---

*Página 112*

Veamos un ejemplo:

| Programa Primal | Programa Dual |
|---|---|
| $\max Z = 10x_1 + 18x_2$ | $\min G = 80y_1 + 120y_2 + 10y_3$ |
| **S.a.** | **S.a.** |
| $x_1 + 8x_2 \leq 80$ | $y_1 + 9y_2 + 2y_3 \geq 10$ |
| $9x_1 + 15x_2 \geq 120$ | $8y_1 + 15y_2 + y_3 = 18$ |
| $2x_1 + x_2 = 10$ | |
| $x_1 \leq 0, x_2 \geq 0$ | $y_1 \geq 0, y_2 \leq 0, y_3 \text{ s/r}$ |

### RELACIONES PRIMAL – DUAL

Existen entre ambos problemas dos tipos de relaciones:
**Relación entre variables y restricciones:** como podemos observar en lo desarrollado hasta aquí, las relaciones entre las variables de un programa y las restricciones en el otro programa son:
- Las restricciones de la forma “menor o igual que” en el problema de máximo dan origen a variables “$\geq 0$” en el problema de mínimo.
- Las restricciones “igual que” dan origen a variables “no restringidas” en el otro problema.
- Las restricciones “mayor o igual que” en el problema de máximo originan variables “$\leq 0$” en el programa de mínimo.

**Relación entre los valores objetivos:** se puede demostrar que: “el valor de la función objetivo, para cualquier solución factible del problema de máximo, es siempre menor o igual que el valor de la función objetivo, para cualquier solución factible del problema de mínimo, es decir:
$$ Z \leq G $$
En particular, la igualdad se verifica cuando ambos problemas están en el óptimo.

### TEOREMA FUNDAMENTAL DE LA DUALIDAD

Este teorema expresa que “con respecto a los programas lineales primal y dual, exactamente una de las siguientes proposiciones es cierta:
- Ambos problemas tienen solución óptima X* y Y*, siendo Z*= G*
- Uno de los problemas es no acotado, en cuyo caso el otro problema es no factible
- Ambos problemas son no factibles”

---

*Página 113*

### TEOREMA DÉBIL DE HOLGURA COMPLEMENTARIA

Este teorema (demostrado para el caso de la dualidad canónica) sostiene que en el óptimo “si una variable en uno de los problemas es positiva, entonces la restricción correspondiente en el otro problema es sin holgura, y si una restricción en uno de los problemas es con holgura, entonces la variable correspondiente en el otro problema debe ser nula”.

### INTERPRETACIÓN ECONÓMICA DE LAS VARIABLES DUALES

En el óptimo, la variable dual representa la cantidad que incrementa la función Z ante un incremento unitario en el i-ésimo valor del lado derecho ($b_i$). Esto se demuestra calculando en el óptimo:

$$ \frac{\partial Z^*}{\partial b_i} = \frac{\partial (B'Y^*)}{\partial b_i} = y_i^* $$

Por ejemplo, si la i-ésima restricción representa la disponibilidad de $b_i$ unidades de insumo para elaborar un producto y Z representa la contribución total a las utilidades, entonces $y_i$ (variable dual) representa el incremento en las utilidades por adicionar una unidad del i-ésimo insumo.

Si en cambio, la i-ésima restricción representa la demanda de al menos $b_i$ unidades producidas y Z representa el costo total de producción, entonces $y_i$ es el costo incremental de producir una unidad más del i-ésimo producto.

Económicamente puede interpretarse al vector de variables duales Y* como un vector de precios sombra para el vector del lado derecho, es decir que es el precio justo o valoración interna de los recursos.

## 3. ANÁLISIS DE SENSIBILIDAD

Uno de los supuestos sobre los que está basada la PL es el de certidumbre. Es decir que el modelo supone que todos los parámetros que en él intervienen se conocen con exactitud.

Nosotros sabemos que en los problemas que se nos presentan diariamente existe un grado de incertidumbre o aleatoriedad en los datos que poseemos. Por ejemplo, podemos estimar que la disponibilidad de horas de mano de obra mensuales es en promedio de 500, pero cada mes en particular la cantidad real de horas disponibles pueden no ser exactamente 500, aunque sí un valor muy aproximado.
En general, al modelizar, se utilizan estimaciones estadísticas de los parámetros del modelo y luego se los trabaja como valores ciertos.

Debido a esto se hace necesario realizar un análisis de la sensibilidad de la solución del problema. Esto es, estudiar los efectos que tienen en la solución óptima del problema, variaciones que puedan producirse en los valores de los parámetros.

---

*Página 114*

Esto es lo que se conoce como análisis de sensibilidad o análisis de post-optimidad.

El objetivo de este análisis es responder a preguntas tales como:
1. ¿Cómo afecta a la solución óptima un cambio en el coeficiente de costo de alguna variable no básica?
2. ¿Cuál es el efecto que tiene en la solución óptima un cambio en el coeficiente de costo de una variable básica?
3. ¿Qué efecto producirá en la solución óptima una variación en el lado derecho de alguna restricción?

En resumen, el análisis de post-optimidad se realiza sobre:

| Coeficientes de la función objetivo ($c_j$) | | Valores del lado derecho ($b_i$) | |
|---|---|---|---|
| De una variable No básica | De una variable Básica | Restricción No limitante | Restricción Limitante |
| $x_j = 0$ | $x_j > 0$ | $S_i > 0$ | $S_i = 0$ |

Estudiaremos este tema desde tres aspectos:
- un análisis gráfico
- estudio de los intervalos de sensibilidad
- cálculo de los intervalos.

### 3.1. UNA VISIÓN GRÁFICA

Se analizará gráficamente qué ocurre con la solución óptima y con el valor de la función objetivo ante cambios en los parámetros $c_j$ y $b_i$.

**Variaciones en los coeficientes de la función objetivo**

Si se incrementa o disminuye algún coeficiente de la función objetivo, cambiará la pendiente de la recta que la representa. Dependiendo de la magnitud del cambio, el vértice actual seguirá o no siendo óptimo.

Supongamos que tenemos el siguiente problema:
$$ \max Z = 12x_1 + 20x_2 $$
**S.a:**
$$ 10x_1 \leq 300 $$
$$ 12x_2 \leq 360 $$
$$ 15x_1 + 10x_2 \leq 600 $$
$$ x_1, x_2 \geq 0 $$

> La ecuación explícita de la recta de isoutilidad es:
> $x_2 = (Z/c_2) - (c_1/c_2) x_1$
> de donde, cualquier cambio en los coeficientes $c_j$, modificarán la pendiente de la recta.

---

*Página 115*

Su solución gráfica es:

> 📊 [Figura 1 - El vértice óptimo es A (20, 30) con Z = 840. La pendiente original es $-12/20 = -0.6$]

De acuerdo a la solución gráfica, vemos que el vértice óptimo es A.

Supongamos que el coeficiente de $x_1$ se incrementa a 20. Esto hace que la pendiente de Z cambie, como se observa en la figura 2, pero el vértice actual sigue siendo el óptimo.

> 📊 [Figura 2 - Z modificada a $20x_1 + 20x_2$. La pendiente cambia pero A (20, 30) sigue siendo el vértice óptimo, ahora con Z = 1000]

Observe ahora la figura 3, en este caso el coeficiente de $x_1$ se incrementó a 35 y como consecuencia, la pendiente de Z se modificó tanto que cambió el vértice óptimo, pasando de A a B.

> 📊 [Figura 3 - Z modificada a $35x_1 + 20x_2$. La pendiente cambió drásticamente y el nuevo vértice óptimo es B (30, 15) con Z = 1350]

En consecuencia, puede afirmarse que en tanto la pendiente de la recta z se mantenga entre las pendientes de las rectas que representan a las restricciones 1 y 3, el vértice óptimo no se modifica.

---

*Página 116*

A través de este sencillo ejemplo, se puede observar que las variaciones en los coeficientes de la función Z, producen una modificación en su pendiente. Por esta razón, lo que pretendemos al realizar el análisis de sensibilidad es determinar un rango o un intervalo de valores dentro del cual pueden variar los coeficientes de la función objetivo, sin que la solución (vértice actual) deje de ser óptima.

**Cambios en los valores del lado derecho**

Veamos, con el mismo ejemplo, que sucede cuando varían los valores del lado derecho.

Puede observarse en la figura 4, que si $b_3$ (valor del lado derecho de la restricción 3) se incrementa a 700, se amplía la región factible y el vértice actual deja de ser óptimo en este caso pasa del vértice A al C.

Pero si hacemos un análisis más detallado podemos observar que en el vértice A (solución factible básica anterior) y de acuerdo con la figura 1 las variables básicas eran $x_1, x_2$ y $S_2$, siendo las no básicas $S_1$ y $S_3$.
Si observamos ahora la figura 4, en el vértice C (óptimo actual) seguimos teniendo las mismas variables básicas y no básicas, sin embargo, es evidente que han cambiado sus valores.

> 📊 [Figura 4 - $b_3$ incrementado a 700. El vértice óptimo se mueve de A a C.]


---

*Página 118*

Si ahora disminuimos el valor del $b_i$ más allá de la holgura de esa restricción, el vértice A dejará de ser óptimo, esto es que el conjunto de variables básicas habrá cambiado y por lo tanto deberá resolverse nuevamente el problema. Observe esta situación en la figura 9.

> 📊 [Figura 9 - $b_1$ disminuido drásticamente (a 150). El vértice óptimo ya no es A, ahora es otro vértice (15, 30).]

En resumen, el cambio en $b_i$ tiene como efecto expandir o contraer la región de soluciones factibles. Al cambiar $b_i$ a $b_i'$ cambiarán al menos los valores de algunas de las variables básicas. Sin embargo, si $b_i$ se incrementa o disminuye más allá de ciertos límites, la base actual dejará de ser factible y deberá por lo tanto recalcularse la solución completa.
Por esta razón los valores admisibles para $b_i$ son aquellos para los que la nueva solución básica permanece factible. Es decir, para los que las variables básicas permanecen no negativas.

## 3.2. ANÁLISIS DE LOS INTERVALOS DE SENSIBILIDAD

**Cambios en los coeficientes de la función objetivo ($c_j$)**

1. **Cambio en $c_j$ de una variable no básica:**
   - En caso de maximización, si el coeficiente de $x_j$ disminuye, entonces no se produce ningún cambio en la solución óptima, lo mismo si aumenta en una cantidad menor o igual al límite superior del intervalo.
   - En caso de minimización, si el coeficiente de $x_j$ aumenta, entonces no se produce ningún cambio en la solución óptima, lo mismo si disminuye en una menor o igual al límite inferior del intervalo.

2. **Cambio en $c_j$ de una variable básica:**
   Si $x_k$ es una variable básica, la solución óptima no va sufrir ningún cambio siempre que la modificación en el coeficiente $c_k$ esté dentro del intervalo de sensibilidad. En este caso, el valor de la función objetivo aumentará o disminuirá en:
   $$ Z' = Z_0 + \Delta c_k x_k $$

**Variaciones en los valores del lado derecho ($b_i$)**

1. **Restricciones no limitantes (con holgura positiva)**

---

*Página 119*

El lado derecho de la restricción puede disminuir en una cantidad igual al valor de la variable de holgura y relajarse arbitrariamente, sin que la base actual sufra modificaciones. En estos casos no cambiará el valor de la función objetivo, pero sí el valor de la holgura correspondiente.

2. **Restricciones limitantes (sin holgura)**
El cambio que se produzca en algún valor del lado derecho siempre tendrá un efecto sobre la base óptima. Si el aumento o disminución está contenido dentro del intervalo, no cambiará la estructura de la base óptima -las variables básicas serán las mismas-, pero sí se modificarán los valores de las variables básicas y el valor de la función objetivo.

El nuevo valor de la función objetivo será:
$$ Z' = Z_0 + \Delta b_i y_i $$
donde $y_i$ es el valor de la variable dual.

Los nuevos valores de las variables básicas se recalculan usando las tasas de sustitución:
$$ x_i = \lambda_{i0} + \Delta b_i \lambda_{ij} \quad \text{si la restricción es de } \leq \text{ o } = $$
$$ x_i = \lambda_{i0} - \Delta b_i \lambda_{ij} \quad \text{si la restricción es de } \geq $$
donde $\lambda_{ij}$ representan a las tasas de sustitución de la variable de holgura/excedente asociada a $b_i$ en el caso de restricciones de $\leq$ ó $\geq$, o a las tasas de sustitución de la variable artificial en el caso de restricciones de igualdad.

**REGLA DE 100%**
La validez de los cambios informados por el análisis de sensibilidad son *ceteris paribus*, es decir, se deben analizar uno por vez. No obstante, existe una regla práctica, conocida como regla del 100%, la cual sostiene que "para considerar cambios simultáneos se deben sumar los porcentajes de cambio tanto de los incrementos como de las disminuciones permisibles; si la suma de los cambios porcentuales no excede el 100%, la solución óptima no se modificará". Esto es válido tanto para cambios en el vector de términos independientes de las restricciones como en los coeficientes que preceden a las variables en la FO.

## 3.3. CÁLCULO DE LOS INTERVALOS DE SENSIBILIDAD

**Cambios en los coeficientes de la función objetivo**

1. **Coeficiente de una variable no básica**
Para una variable no básica el intervalo de sensibilidad define los posibles valores del coeficiente de la función objetivo para los cuales esa variable sigue siendo no básica.

---

*Página 120*

Analizando para el caso de máximo, podemos decir que una variable, que en la solución óptima actual es no básica, tiene una diferencia $c_j - z_j$ negativa, es decir que su contribución neta unitaria al objetivo es negativa y por lo tanto para que sea conveniente introducirla a la base su contribución debe ser positiva. Por esta razón vamos a analizar la condición de optimidad para esta variable.

Como la variable no es básica analizamos sólo incrementos en dicho coeficiente, ya que, si la utilidad de esta variable disminuye, no habrá cambios en la solución óptima.
El intervalo de optimidad para un coeficiente de la función objetivo se determina mediante los valores de los coeficientes que mantienen:
$$ c_j - z_j \leq 0 \quad \text{para todos los valores de j} $$

Haciendo el análisis para una variable no básica $x_j$ cualquiera y si llamamos $\Delta c_j$ al incremento en el coeficiente de dicha variable tendremos que el nuevo coeficiente será:
$$ c_j' = \Delta c_j + c_j $$

Usando la condición de optimidad podemos decir que $x_j$ seguirá siendo no básica siempre que:
$$ c_j' - z_j \leq 0 $$

Reemplazando por el nuevo valor de $c_j'$ y realizando algunas operaciones:
$$ c_j' - z_j \leq 0 $$
$$ c_j + \Delta c_j - z_j \leq 0 $$
$$ \Delta c_j \leq -c_j + z_j $$
$$ \Delta c_j \leq -( c_j - z_j ) $$

En general para cualquier problema:
$$ \Delta c_j \leq z_j - c_j $$

Si, $\Delta c_j = z_j - c_j$ se obtiene una solución óptima alternativa.

Resumiendo, si se modifica el coeficiente de la función objetivo de una variable no básica:
- En caso de maximización $\Rightarrow$ si el coeficiente de $x_j$ disminuye, entonces no se produce ningún cambio en la solución óptima, lo mismo si aumenta en una cantidad inferior $c_j - z_j$.
Es decir, el intervalo de variación es: $[ -\infty , c_j - z_j ]$

---

*Página 121*

- En caso de minimización $\Rightarrow$ si el coeficiente de $x_j$ aumenta, entonces no se produce ningún cambio en la solución óptima, lo mismo si disminuye en una cantidad inferior $c_j - z_j$
Es decir, el intervalo de variación es: $[ c_j - z_j , \infty ]$

2. **Coeficiente de una variable básica**
Si se modifica el coeficiente $c_j$ de una variable básica, entonces puede producirse uno de dos resultados, es posible que la variable deje de ser básica o que aumente su valor. Es por esta razón, que se deben considerar tanto aumentos como disminuciones en los coeficientes de la función objetivo. Y también a diferencia de los casos de las variables no básicas, los cambios en los coeficientes de las variables básicas tendrán de alguna manera un impacto sobre el valor de la función objetivo.

Realizamos el análisis de la misma manera que para una variable no básica. Sin embargo, en este caso para determinar los límites de $\Delta c_j$ y por lo tanto el intervalo de sensibilidad, debemos considerar todos los valores $c_j - z_j$ que se ven afectados por $\Delta c_j$. Para hacer esto usamos las tasas de sustitución que relacionan a la variable que sufrió un cambio en su coeficiente, supongamos que sea $x_k$, con cada una de las variables no básicas.

Si llamamos $Z_0$ al valor de la función objetivo, el nuevo valor se puede determinar como:
$$ Z_0' = Z_0 + \lambda_{k0} \Delta c_k $$

La fila de $z_j$ puede determinarse como:
$$ z_j' = z_j + \lambda_{kj} \Delta c_k \quad \text{para j = 1, 2, ..., n} $$

Para que la solución actual siga siendo óptima, ningún valor $c_j - z_j$ debe hacerse positivo.
Puede calcularse la fila $c_j - z_j$ como:
$$ (c_j - z_j') = c_j - (z_j + \lambda_{kj} \Delta c_k) $$
$$ (c_j - z_j)' = (c_j - z_j) - \lambda_{kj} \Delta c_k \quad \text{para j = 1, 2, ..., n} $$

Para determinar la magnitud de la variación, despejamos $\Delta c_k$ del sistema de restricciones dado por:
$$ (c_j - z_j)' = (c_j - z_j) - \lambda_{kj} \Delta c_k \leq 0 \quad \text{para j = 1, 2, ..., n} $$

Resumiendo, si se modifica el coeficiente de la función objetivo de una variable básica, puede ocurrir que, si el cambio en el coeficiente que tiene la variable $x_k$ en la función objetivo está dentro del intervalo de

---

*Página 122*

sensibilidad, la solución óptima no va sufrir ningún cambio y el valor de la función objetivo aumentará o disminuirá. Sin embargo, si el cambio es tal que el nuevo coeficiente sale del intervalo determinado, la solución dejará de ser óptima.

**Variaciones en los valores del lado derecho**

El cambio en un $b_i$ tiene como efecto aumentar o disminuir la región de soluciones factibles. Al cambiar $b_i$ a $b_i'$ cambiarán al menos los valores de algunas de las variables básicas. Por esta razón los valores admisibles para $b_i$ son aquellos para los que la nueva base permanece factible. Es decir, para los que las variables básicas son no negativas.

1. **Restricciones no limitantes**
Si la restricción es del tipo $\leq$ el intervalo de variación de $b_i$ será $[S_i , \infty]$, donde $S_i$ es el valor de la variable de holgura correspondiente a la i-ésima restricción.
Si la restricción es del tipo $\geq$ el intervalo de variación de $b_i$ será $[-\infty , S_i]$, donde $S_i$ es el valor de la variable de excedente correspondiente a la i-ésima restricción.
En estos casos no cambiará el valor de la función objetivo, pero sí el valor de la holgura correspondiente.

2. **Restricciones limitantes**
Cuando hicimos el análisis de los elementos de la tabla simplex definimos a las tasas de sustitución ($\lambda_{ij}$) como el sacrificio que se debía hacer de la variable básica $x_i$ para poder incrementar en una unidad la variable no básica $x_j$.

Cuando la variable no básica analizada es una variable de holgura debemos interpretar ese incremento como dejar libre o dejar de usar una unidad del recurso ($b_i$) de la restricción a la cual corresponde dicha holgura. Es decir que, estas tasas nos mostrarán el sacrificio de cada variable básica si disminuimos en una unidad un valor del lado derecho.
Por el contrario, si aumentamos en una unidad un $b_i$, la interpretación de las $\lambda_{ij}$ será exactamente lo opuesto. De esta manera podemos usar a las tasas de sustitución de las variables de holgura correspondiente al lado derecho analizado, para determinar en cuánto puede aumentar o disminuir su valor sin que la solución actual deje de ser factible.

Para determinar el intervalo de sensibilidad usamos la condición de factibilidad de la solución y las tasas de sustitución de las variables de holgura. El procedimiento para determinar este intervalo en caso de restricciones del tipo $\leq$ es el siguiente:

---

*Página 123*

$$ \begin{bmatrix} \lambda_{10} \\ \lambda_{20} \\ \lambda_{30} \\ \vdots \\ \lambda_{m0} \end{bmatrix} + \Delta b_i \begin{bmatrix} \lambda_{1j} \\ \lambda_{2j} \\ \lambda_{3j} \\ \vdots \\ \lambda_{mj} \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix} \quad (1) $$

> Solución actual + $\Delta b_i \times$ Columna de la tabla simplex que corresponde a la variable de holgura asociada a la restricción i

Resolviendo nos queda un sistema de inecuaciones, y podemos determinar de esta manera un incremento y una disminución para $b_i$.

Para restricciones del tipo $\geq$ se pueden usar las tasas de sustitución de la variable artificial y hacerlo de la misma manera que en el caso anterior (1) o usar las tasas de sustitución de la variable de excedente, pero restando el incremento, es decir:

$$ \begin{bmatrix} \lambda_{10} \\ \lambda_{20} \\ \lambda_{30} \\ \vdots \\ \lambda_{m0} \end{bmatrix} - \Delta b_i \begin{bmatrix} \lambda_{1j} \\ \lambda_{2j} \\ \lambda_{3j} \\ \vdots \\ \lambda_{mj} \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix} \quad (2) $$

Determinándose al igual que en el caso anterior un incremento y una disminución para el valor del lado derecho analizado.

Para restricciones de =, se plantea un sistema de restricciones como (1), pero con las tasas de sustitución de la columna de la variable artificial correspondiente a la restricción analizada y se procede de manera análoga a los casos anteriores.

**Conclusión:** En el caso de restricciones limitantes el cambio que se produzca en algún valor del lado derecho siempre tendrá un efecto sobre la solución óptima, de la siguiente manera:
- Si el aumento o disminución está contenido dentro del intervalo de sensibilidad, no cambiará la base óptima, pero sí los valores de las variables positivas y el valor de la función objetivo.
- Si el aumento o disminución producida hace que el nuevo valor no esté contenido en el intervalo de sensibilidad, cambiará la solución completa.

### PRECIO SOMBRA VS. PRECIO DUAL

Al analizar los cambios en los lados derechos de las restricciones y la interpretación de los resultados que nos brinda la computadora,

---

*Página 124*

dependiendo del software utilizado, aparecen alguno de estos dos importantes conceptos: precio dual y precio sombra.
Es muy importante al momento de analizar la solución óptima, tener en claro la diferencia entre ambos.

**Precio sombra** indica la variación que se produce en el valor de la función objetivo ante un incremento en el lado derecho de una restricción. El precio sombra es el valor de la variable dual correspondiente.
Esto significa que, para un problema de maximización, si el precio sombra es positivo un incremento en el VLD implicará un crecimiento en el valor de la función objetivo y por lo tanto el valor de la función objetivo mejora. Si en cambio el problema es de minimización, como un precio sombra positivo indica un incremento de la función objetivo, entonces nuestro objetivo desmejora.

**Precio dual** representa la mejora o desmejora que se produce en el valor de la función objetivo, ante un incremento en el lado derecho de una restricción, según que el precio dual sea positivo o negativo.
Esto quiere decir que un precio dual positivo nos indica en cuánto mejora el valor de la función objetivo ante un incremento del lado derecho; y aquí mejora expresa que el valor objetivo crece en caso de máximo y decrece en caso de mínimo.
De la misma manera un precio dual negativo representará la desmejora que se produce en el valor de la función objetivo ante un incremento del VLD.

Como resumen de lo anterior podemos decir que en caso de maximización precio sombra y precio dual son iguales, sin embargo, en caso de minimización uno es el opuesto del otro.

### INTRODUCCIÓN DE UNA NUEVA VARIABLE

En numerosas ocasiones, los decisores se plantean la necesidad de incluir en el modelo una variable no considerada en el problema original. Por ejemplo, un nuevo producto o una actividad adicional que no fue contemplada con anterioridad. En estos casos resulta interesante estudiar si es conveniente su introducción analizando de qué manera afectarían a la solución óptima actual. Para efectuar este análisis podemos utilizar a los precios sombra.

Al realizar la interpretación de los elementos de la tabla simplex vimos que las diferencias $c_j - z_j$ correspondientes a las variables de holgura nos indicaban la disminución que se produce en el valor de z si dejamos sin usar una unidad del recurso, y esto se debe a que tendremos que dejar de producir de alguno/s productos.
Asimismo, recordemos que este valor, considerando el signo que nos fija el dual, es el precio sombra y nos indica el valor marginal del recurso al cual se refiere.

Con este razonamiento podremos calcular el “costo de oportunidad” de introducir el nuevo producto y compararlo con la contribución que

---

*Página 125*

aporta a la función objetivo, para determinar si se produce un incremento o una disminución marginal en el valor de z.

Es decir, para los recursos de los cuales tenemos holgura, su costo de oportunidad es cero, pero de aquellos limitantes tendremos que considerar que dejar de utilizar una unidad en la producción actual para derivarlo a la producción de un nuevo producto tiene para nosotros un costo que está dado por el precio sombra. De esta manera podremos calcular cuál es el “costo de introducir” esta nueva variable y luego compararlo con su contribución el objetivo.

Así si $k$ representa a la nueva variable, el cálculo a realizar será:
$$ z_k = \sum_{i=1}^m a_{ik} (y_i) $$
$$ c_k - z_k $$

Si $c_k - z_k$ es positivo, convendrá introducir este nuevo producto o actividad y si es negativo nos indicará la magnitud del cambio que debería realizarse para poder introducirlo.

### ANÁLISIS DE SENSIBILIDAD MEDIANTE UN EJEMPLO

Una empresa fabrica cuatro tipos de alfombras que tienen gran demanda en el mercado.
En el proceso de fabricación, primero se tiñe el hilado, que es la materia prima principal, y luego se la envía a la sección tejido. En la tabla se muestran los kg. de materia prima y las horas en cada sección necesaria para fabricar cada alfombra, la disponibilidad total de estos insumos y la contribución unitaria de cada tipo de alfombra.

| PRODUCTO | Alfombra I | Alfombra II | Alfombra III | Alfombra IV | Disponibilidad |
|---|---|---|---|---|---|
| Materia Prima (Kg/unid) | 3 | 4 | 8 | 6 | 22000 |
| Hrs. Sección Teñido | 8 | 2 | 4 | 2 | 28000 |
| Hrs. Sección Tejidos | 4 | 6 | 2 | 4 | 8000 |
| Contribución (\$/unid) | 40 | 60 | 30 | 10 | |

*Tabla 1*

**Definición de Variables:**
$x_1, x_2, x_3$ y $x_4$ indican las unidades de las alfombras I, II, III y IV a fabricar, respectivamente.

$$ \max Z = 40x_1 + 60x_2 + 30x_3 + 10x_4 $$
**s.a.**
$$ 3x_1 + 4x_2 + 8x_3 + 6x_4 \leq 22000 \quad \text{Materia Prima} $$
$$ 8x_1 + 2x_2 + 4x_3 + 2x_4 \leq 28000 \quad \text{Hrs Sección Teñido} $$
$$ 4x_1 + 6x_2 + 2x_3 + 4x_4 \leq 8000 \quad \text{Hrs Sección Tejidos} $$
$$ x_1, x_2, x_3, x_4 \geq 0 $$

---

*Página 126*

En la página siguiente se muestra el informe de solución del software LINDO y SOLVER correspondiente a este problema. Analice la salida y responda las siguientes preguntas:

a) ¿Cuál es la solución óptima y cuál el valor de la función objetivo?
b) ¿Existe excedente en alguno de los recursos?, ¿en qué cantidad?
c) Si la contribución de la alfombra III aumenta en \$20, ¿cambia la solución óptima?, ¿cómo?, ¿qué sucede con la contribución total?
d) Si la contribución de la alfombra 4 aumenta en \$25, ¿cambia la solución óptima?, ¿cómo?, ¿qué sucede con la contribución total?
e) Suponga que se pueden conseguir 1000 Kg. adicionales de materia prima, pagando un precio adicional de \$5 por Kg. ¿Conviene adquirirlos? ¿Por qué?
f) ¿Cuál es el valor de una hora adicional en la Sección Teñido? Justifique.
g) Suponga que, en la Sección Tejidos, como consecuencia de la rotura de una máquina, disminuyen las horas disponibles en 1000, ¿cómo afecta esto a la solución óptima y al valor de Z?
h) Suponga que un cliente importante le solicita 10 alfombras tipo IV. ¿Cuál será el nuevo valor de la función objetivo? ¿Por qué? ¿De qué tipo será la nueva solución?
i) Calcule el intervalo de sensibilidad para el coeficiente de las variables $x_1$ y $x_2$.
j) Calcule el intervalo de sensibilidad de la primera y segunda restricción.
k) Al fabricante le interesa producir un nuevo modelo de alfombra de colores más brillantes y que se puede vender a \$100. Para su fabricación necesitará 4 kg de Materia Prima, 5 hs. En la Sección Teñido y 5 hs. En la Sección Tejidos. Quiere saber si le conviene producirlo. Si lo cree conveniente, sugiera un precio de venta.

---

*Página 127*

**INFORME DE SOLUCIÓN CON LINDO**

```text
OBJECTIVE FUNCTION VALUE
1)  105000.0

VARIABLE      VALUE          REDUCED COST
X1            0.000000       0.500000
X2            500.000000     0.000000
X3            2500.000000    0.000000
X4            0.000000       35.000000

ROW           SLACK OR SURPLUS  DUAL PRICES
2)            0.000000          1.500000
3)            17000.000000      0.000000
4)            0.000000          9.000000

RANGES IN WHICH THE BASIS IS UNCHANGED:

                           OBJ COEFFICIENT RANGES
VARIABLE      CURRENT          ALLOWABLE        ALLOWABLE
              COEF             INCREASE         DECREASE
X1            40.000000        0.500000         INFINITY
X2            60.000000        30.000000        0.769231
X3            30.000000        90.000000        9.999998
X4            10.000000        35.000000        INFINITY

                           RIGHTHAND SIDE RANGES
ROW           CURRENT          ALLOWABLE        ALLOWABLE
              RHS              INCREASE         DECREASE
2             22000.0000       10000.0000       16666.666016
3             28000.0000       INFINITY         17000.000000
4             8000.0000        25000.0000       2500.000000
```


---

*Página 128*

**INFORME DE SOLUCIÓN CON LINDO**

```text
OBJECTIVE FUNCTION VALUE
1)  105000.0

VARIABLE      VALUE          REDUCED COST
X1            0.000000       0.500000
X2            500.000000     0.000000
X3            2500.000000    0.000000
X4            0.000000       35.000000

ROW           SLACK OR SURPLUS  DUAL PRICES
2)            0.000000          1.500000
3)            17000.000000      0.000000
4)            0.000000          9.000000

RANGES IN WHICH THE BASIS IS UNCHANGED:

                           OBJ COEFFICIENT RANGES
VARIABLE      CURRENT          ALLOWABLE        ALLOWABLE
              COEF             INCREASE         DECREASE
X1            40.000000        0.500000         INFINITY
X2            60.000000        30.000000        0.769231
X3            30.000000        90.000000        9.999998
X4            10.000000        35.000000        INFINITY

                           RIGHTHAND SIDE RANGES
ROW           CURRENT          ALLOWABLE        ALLOWABLE
              RHS              INCREASE         DECREASE
2             22000.0000       10000.0000       16666.666016
3             28000.0000       INFINITY         17000.000000
4             8000.0000        25000.0000       2500.000000
```

- **Disminución que se produce en Z por cada unidad en que se incrementa la variable**: Ver Reduced Cost.
- **Mejora que se produce en Z por cada unidad en que se incrementa el lado derecho de la restricción**: Ver Dual Prices. Tiene validez dentro del intervalo de sensibilidad.
- **Variable no básica**: Si la variación del coeficiente de $x_1$ se produce dentro de este rango, no se producen cambios en los valores de las variables, ni en el valor de Z.
- **Variable básica**: Si la variación del coeficiente de $x_3$ se produce dentro de este rango, no se producen cambios en los valores de las variables, sólo varía el valor de Z.
- **Restricción no limitante**: Si la variación del RHS se produce dentro de este rango, sólo se modifica el valor de la holgura.
- **Restricción limitante**: Si la variación del RHS se produce dentro de este rango, no cambia la base, pero varían los valores de las variables básicas y el valor de Z.

---

*Página 129*

**INFORME DE SOLUCIÓN CON SOLVER**

**Celda objetivo (Máx.)**

| Nombre | Valor original | Valor final |
|---|---|---|
| Objetivo | 0 | 105000 |

**Celdas de variables**

| Nombre | Valor original | Valor final |
|---|---|---|
| Variables Alf. I | 0 | 0 |
| Variables Alf. II | 0 | 500 |
| Variables Alf. III | 0 | 2500 |
| Variables Alf. IV | 0 | 0 |

**Restricciones**

| Nombre | Valor de la celda | Estado | Holgura |
|---|---|---|---|
| Materia Prima (Kg/unid) | 22000 | Vinculante | 0 |
| Hrs. Sección Teñido | 11000 | No vinculante | 17000 |
| Hrs. Sección Tejidos | 8000 | Vinculante | 0 |

**Análisis de Sensibilidad**

| Nombre | Final Valor | Costo Reducido | Coeficiente Objetivo | Aumento Permisible | Reducción Permisible |
|---|---|---|---|---|---|
| Variables Alf. I | 0 | -0,5 | 40 | 0,5 | 1E+30 |
| Variables Alf. II | 500 | 0 | 60 | 30 | 0,76923 |
| Variables Alf. III | 2500 | 0 | 30 | 90 | 10 |
| Variables Alf. IV | 0 | -35 | 10 | 35 | 1E+30 |

| Nombre | Final Valor | Precio Sombra | Restricción Lado derecho | Aumento Permisible | Reducción Permisible |
|---|---|---|---|---|---|
| Materia Prima (Kg/unid) | 22000 | 1,5 | 22000 | 10000 | 16666,667 |
| Hrs. Sección Teñido | 11000 | 0 | 28000 | 1E+30 | 17000 |
| Hrs. Sección Tejidos | 8000 | 9 | 8000 | 25000 | 2500 |

---

*Página 130*

Respuestas a las preguntas del problema de la fábrica de Alfombras:

a) La solución óptima será:
Producir 500 alfombras tipo II y 2500 alfombras tipo III. Con este plan de producción se usará toda la materia prima y todas las horas de la Sección Tejidos, quedando 17000 horas disponibles en la Sección Teñido. La contribución total máxima será de \$ 105000.-

b) Quedan 17000 horas sin utilizar en la Sección Teñido.

c) En primer lugar nos fijamos si el incremento en el coeficiente está dentro del intervalo de sensibilidad y luego si corresponde a una variable básica o no básica, y de acuerdo a ello podremos decir cuáles serán sus efectos. El incremento máximo admitido para el coeficiente de $x_3$ es de 90 y como $x_3$ es una variable básica, podemos decir que la solución óptima no sufrirá cambios, sólo se modificará el valor de Z incrementándose en $20(2500) = \$50000$

d) Como el incremento en el coeficiente de la variable $x_4$ está dentro del intervalo de sensibilidad y además se trata de una variable no básica, podemos decir que no se modificará la solución actual ni el valor de la función objetivo.

e) También en este caso primero nos fijamos si el incremento o disminución está dentro del intervalo de sensibilidad y luego si se trata de una restricción limitante o no. Si es una restricción no limitante, no nos interesará adquirir ninguna cantidad adicional del recurso y si es una restricción limitante debemos comparar el valor marginal del recurso (precio sombra) con el precio adicional que nos piden. Hay que tener en cuenta que el precio sombra es válido en el intervalo de sensibilidad. En nuestro caso si bien se trata de un recurso limitante, el precio adicional solicitado es superior al valor marginal del recurso, por lo tanto concluimos que no nos conviene adquirir más materia prima.

f) El valor de una hora adicional es cero, ya que podemos observar que se trata de un recurso no limitante (hay sobrante). También puede justificarse este valor a través del teorema débil de holgura complementaria que dice: si una restricción es con holgura la variable dual correspondiente será igual a cero (precio sombra). Recordemos que en caso de maximización el precio sombra y el precio dual son iguales.

g) Nuevamente nos fijamos si esta disminución está dentro del intervalo de sensibilidad y luego si la restricción es limitante o no. Como las horas en la Sección Tejidos son limitantes y la disminución está dentro del intervalo de sensibilidad (máximo admitido es 2500), concluimos que no cambiará la base. Es decir que seguiremos produciendo de los mismos tipos de alfombras, pero en diferentes cantidades y el valor de la contribución total disminuirá en:
$$ 1000(9) = 9000. $$

---

*Página 131*

Calculamos los nuevos valores de las variables usando las tasas de sustitución de la variable de holgura correspondiente a la restricción de horas de Sección Tejidos ($S_3$) de la tabla óptima:

$$ x_i = \lambda_{i0} + \Delta b_i \lambda_{ij} \quad (i = 1...m) $$

donde $\Delta b_i$ representa el incremento del valor del lado derecho que en este caso es negativo.

| | | $c_j$ | 40 | 60 | 30 | 10 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|
| $c_j$ | Base | VLD | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $S_1$ | $S_2$ | $S_3$ |
| 30 | $x_3$ | 2500 | 0,05 | 0 | 1 | 0,5 | 0,15 | 0 | -0,10 |
| 0 | $S_2$ | 17000 | 6,5 | 0 | 0 | -1 | -0,5 | 1 | 0 |
| 60 | $x_2$ | 500 | 0,65 | 1 | 0 | 0,5 | -0,05 | 0 | 0,20 |
| | $Z_j$ | 105000 | 40,5 | 60 | 30 | 45 | 1,5 | 0 | 9 |
| | $c_j - z_j$ | | -0,5 | 0 | 0 | -35 | -1,5 | 0 | -9 |

*Tabla 2*

La nueva solución será:
- $x_3 = 2500 - 1000 (-0,10) = 2600$
- $S_2 = 17000 - 1000 (0) = 17000$
- $x_2 = 500 - 1000(0,20) = 300$
- $Z_{nuevo} = 105000 + (-1000)9 = \$96000$

h) Como se trata de un cliente importante y queremos cumplir, vamos a tener que resignar beneficios, es decir que la contribución total disminuirá en:
$35(10) = 350$, esto es, coste reducido por la cantidad de alfombras que vamos a producir. Obviamente la contribución va a disminuir porque para poder producir de la alfombra IV deberemos dejar de producir de las otras para, así liberar los recursos necesarios (ver tasa de sustitución).
Para el cálculo de la nueva solución utilizamos las fórmulas vistas en la interpretación económica:

$$ x_i = \lambda_{i0} - \theta \lambda_{ij} \quad (i = 1...m) $$
$$ x_j = \theta $$
$$ x_k = 0 \quad (k \neq 1, 2, ...m, j) $$

La nueva solución será:
- $x_3 = 2500 - 0,5(10) = 2495$
- $S_2 = 17000 + 1 (10) = 17010$
- $x_2 = 500 - 0,5(10) = 495$
- $x_1 = 0$

---

*Página 132*

- $x_4 = 10$
- $S_1 = 0$
- $S_3 = 0$
- $Z = 105000 - (35)10 = \$104650$

Se trata de una solución factible no básica.
Para calcular los intervalos de sensibilidad, tanto de los coeficientes de la función objetivo como de los valores del lado derecho, necesitamos la tabla óptima de simplex:

| | | $c_j$ | 40 | 60 | 30 | 10 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|
| $c_j$ | Base | VLD | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $S_1$ | $S_2$ | $S_3$ |
| 30 | $x_3$ | 2500 | 0,05 | 0 | 1 | 0,5 | 0,15 | 0 | -0,10 |
| 0 | $S_2$ | 17000 | 6,5 | 0 | 0 | -1 | -0,5 | 1 | 0 |
| 60 | $x_2$ | 500 | 0,65 | 1 | 0 | 0,5 | -0,05 | 0 | 0,20 |
| | $Z_j$ | 105000 | 40,5 | 60 | 30 | 45 | 1,5 | 0 | 9 |
| | $c_j - z_j$ | | -0,5 | 0 | 0 | -35 | -1,5 | 0 | -9 |

*Tabla 3*

i) Intervalo de sensibilidad para los coeficientes de las variables:
Como la variable $x_1$ es no básica, el intervalo de sensibilidad de su coeficiente se determina como:
$$ [-\infty , c_j - z_j] \quad \text{o sea} \quad [-\infty , 0,5] $$

Como la variable $x_2$ es básica, el intervalo de sensibilidad para su coeficiente se calcula a partir de:
$$ (c_j - z_j)' = (c_j - z_j) - \lambda_{kj} \Delta c_k $$

Debiendo mantenerse todos los $(c_j - z_j)' \leq 0$ o sea:
$$ (c_j - z_j) - \lambda_{2j} \Delta c_2 \leq 0 $$

Entonces:
$$ -0,5 - 0,65\Delta c_2 \leq 0 $$
$$ -35 - 0,5\Delta c_2 \leq 0 $$
$$ -1,5 - (-0,05)\Delta c_2 \leq 0 $$
$$ -9 - 0,20\Delta c_2 \leq 0 $$

Despejando en cada una de las restricciones anteriores obtenemos que:
- $\Delta c_2 \geq -0,7692$
- $\Delta c_2 \geq -70$
- $\Delta c_2 \leq 30$
- $\Delta c_2 \geq -45$

---

*Página 133*

De dónde, el coeficiente $c_2$ puede disminuir hasta en 0,769 e incrementarse hasta en 30.

j) Intervalo de sensibilidad para el valor del lado derecho de la primera restricción:

$$ \begin{bmatrix} \lambda_{10} \\ \lambda_{20} \\ \lambda_{30} \end{bmatrix} + \Delta b_i \begin{bmatrix} \lambda_{1j} \\ \lambda_{2j} \\ \lambda_{3j} \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$

Reemplazando por la información de la tabla tendremos el siguiente sistema de inecuaciones:

$$ \begin{bmatrix} 2500 \\ 17000 \\ 500 \end{bmatrix} + \Delta b_1 \begin{bmatrix} 0,15 \\ -0,5 \\ -0,05 \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$

$$ 2500 + \Delta b_1 (0,15) \geq 0 $$
$$ 17000 - \Delta b_1 (0,5) \geq 0 $$
$$ 500 - \Delta b_1 (0,05) \geq 0 $$

Despejando en las restricciones se obtiene que $b_1$ puede disminuir hasta en 16666,67 e incrementarse hasta en 10000, sin que cambie la base actual.
El intervalo de sensibilidad para el lado derecho de la segunda restricción se determina considerando la holgura de la segunda restricción. Así el $b_2$ puede disminuir hasta en 17000 e incrementarse infinitamente, sin que la base actual cambie.

Como el empresario quiere producir un nuevo modelo de alfombra, pero cuenta con los mismos recursos, debemos analizar los precios sombra. Ellos nos indican el valor marginal del recurso, es decir el valor que para la empresa tiene cada unidad de recurso dado que para poder liberar una unidad deberá dejar de fabricar de las otras alfombras.

| Alfombra V | Costo de oportunidad | |
|---|---|---|
| Materia Prima (Kg/unid) | 4 | 4 x 1,5 = 60 |
| Hrs. Sección Teñido | 5 | 0 |
| Hrs. Sección Tejidos | 5 | 5 x 9 = 45 |
| **Diferencia** | | |
| **Contribución (\$/unid)** | 100 | \$105 | **(\$5)** |

*Tabla 4*

---

*Página 134*

Podemos observar que el costo de oportunidad de producir una alfombra V es mayor que su contribución a las utilidades, por lo que podríamos aconsejarle al empresario que, si le interesa producirla, debería realizar las modificaciones necesarias que le permitan incrementar su contribución en \$5.

### EJEMPLO DE CÁLCULO DE INTERVALOS DE SENSIBILIDAD DE LOS VLD PARA RESTRICCIONES DE IGUALDAD Y DE MAYOR O IGUAL

Supongamos el siguiente problema de PL:
$$ \max Z = 50 x_1 + 10 x_2 $$
**s.a.**
$$ 20 x_1 + 10 x_2 = 40 $$
$$ 10 x_1 + 10 x_2 \leq 60 $$
$$ 20 x_1 + 10 x_2 \geq 50 $$
$$ x_1, x_2 \geq 0 $$

La tabla óptima de simplex es:

| | | $c_j$ | 50 | 10 | 0 | -M | -M | 0 |
|---|---|---|---|---|---|---|---|---|
| $C_B$ | Base | VLD | $x_1$ | $x_2$ | $S_2$ | $A_1$ | $A_3$ | $S_3$ |
| 50 | $x_1$ | 1 | 1 | 0 | 0 | 2/30 | -1/30 | 1/30 |
| 0 | $S_2$ | 30 | 0 | 0 | 1 | -1/3 | -1/3 | 1/3 |
| 10 | $x_2$ | 2 | 0 | 1 | 0 | -1/30 | 2/30 | -2/30 |
| | $Z_j$ | 70 | 50 | 10 | 0 | 3 | -1 | 1 |
| | $c_j - z_j$ | | 0 | 0 | 0 | -M | -M | -1 |

*Tabla 5*

**a. Intervalo de sensibilidad para $b_1$**
En este caso por tratarse de una restricción de = se deben usar las tasas de sustitución de la variable artificial $A_1$, planteamos el sistema de restricciones:

$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} + \Delta b_1 \begin{bmatrix} 2/30 \\ -1/3 \\ -1/30 \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$

Planteamos cada ecuación y despejamos $\Delta b_1$:

---

*Página 135*

$$ 1 + \Delta b_1 \left(\frac{2}{30}\right) \geq 0 $$
$$ 30 + \Delta b_1 \left(-\frac{1}{3}\right) \geq 0 $$
$$ 2 + \Delta b_1 \left(-\frac{1}{30}\right) \geq 0 $$

Despejando nos queda que $\Delta b_1 \geq -15$ y $\Delta b_1 \leq 60$, es decir que $b_1$ puede disminuir hasta en 15 e incrementarse hasta en 60 o lo que es lo mismo el valor de $b_1$ puede estar entre $[25, 100]$.

**b. Intervalo de sensibilidad para $b_3$**
En este caso por tratarse de una restricción de $\geq$ tenemos dos opciones:

1. Usar las tasas de sustitución de la variable artificial $A_3$ y hacerlo de la misma manera que en el caso anterior

$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} + \Delta b_3 \begin{bmatrix} -1/30 \\ -1/3 \\ 2/30 \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$

Planteamos cada ecuación y despejamos $\Delta b_3$:

$$ 1 + \Delta b_3 \left(-\frac{1}{30}\right) \geq 0 $$
$$ 30 + \Delta b_3 \left(-\frac{1}{3}\right) \geq 0 $$
$$ 2 + \Delta b_3 \left(\frac{2}{30}\right) \geq 0 $$

2. Usar las tasas de sustitución de $S_3$ y plantear las restricciones con ($-\Delta b_3$). Utilizando las tasas de sustitución de $S_3$ nos queda:

$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} - \Delta b_3 \begin{bmatrix} 1/30 \\ 1/3 \\ -2/30 \end{bmatrix} \geq \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$

Planteamos cada ecuación y despejamos $\Delta b_3$:

---

*Página 136*

$$ 1 - \Delta b_3 \left(\frac{1}{30}\right) \geq 0 $$
$$ 30 - \Delta b_3 \left(\frac{1}{3}\right) \geq 0 $$
$$ 2 - \Delta b_3 \left(-\frac{2}{30}\right) \geq 0 $$

En ambos casos, despejando nos queda que $\Delta b_3 \geq -30$ y $\Delta b_3 \leq 30$, es decir que $b_3$ puede disminuir hasta en 30 e incrementarse hasta en 30 o lo que es lo mismo el valor de $b_3$ puede estar entre $[20, 80]$.

**c. Ejemplo de utilización de los intervalos calculados**

- **Primera restricción (=)**
En este caso se utilizan las tasas de sustitución de la variable artificial $A_1$ y el cálculo se realiza de la misma manera que para restricciones de $\leq$, es decir sumando $\Delta b_1$ cuando se trata de un incremento y restando $\Delta b_1$ cuando se trata de una disminución.

1. Incremento de 10 en el VLD ($\Delta b_1 = 10$)
$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} + 10 \begin{bmatrix} 2/30 \\ -1/3 \\ -1/30 \end{bmatrix} = \begin{bmatrix} 5/3 \\ 80/3 \\ 5/3 \end{bmatrix} $$

2. Disminución de 10 en el VLD ($\Delta b_1 = -10$)
$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} - 10 \begin{bmatrix} 2/30 \\ -1/3 \\ -1/30 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 100/3 \\ 7/3 \end{bmatrix} $$

- **Tercera restricción ($\geq$)**

1. Incremento de 10, es decir $\Delta b_3 = 10$. En este caso tenemos dos alternativas
a. Usar las tasas de sustitución de la variable artificial $A_3$
$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} + 10 \begin{bmatrix} -1/30 \\ -1/3 \\ 2/30 \end{bmatrix} = \begin{bmatrix} 1+10(-1/30) \\ 30+10(-1/3) \\ 2+10(2/30) \end{bmatrix} = \begin{bmatrix} 2/3 \\ 80/3 \\ 8/3 \end{bmatrix} $$

---

*Página 137*

b. Usar las tasas de sustitución de la variable de excedente $S_3$, en este caso cuando se trata de un incremento se lo debe restar, por lo que quedaría
$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} - 10 \begin{bmatrix} 1/30 \\ 1/3 \\ -2/30 \end{bmatrix} = \begin{bmatrix} 1-10(1/30) \\ 30-10(1/3) \\ 2-10(-2/30) \end{bmatrix} = \begin{bmatrix} 2/3 \\ 80/3 \\ 8/3 \end{bmatrix} $$

2. Disminución de 10, es decir $\Delta b_3 = -10$, también tenemos dos formas de hacerlo
a. Usar las tasas de sustitución de la variable artificial $A_3$ considerando una disminución como $-\Delta b_3$
$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} - 10 \begin{bmatrix} -1/30 \\ -1/3 \\ 2/30 \end{bmatrix} = \begin{bmatrix} 1-10(-1/30) \\ 30-10(-1/3) \\ 2-10(2/30) \end{bmatrix} = \begin{bmatrix} 4/3 \\ 100/3 \\ 4/3 \end{bmatrix} $$

b. Usar las tasas de sustitución de la variable de excedente $S_3$, en este caso como se trata de una disminución se lo debe sumar ya que $-(-\Delta b_3) = \Delta b_3$
$$ \begin{bmatrix} 1 \\ 30 \\ 2 \end{bmatrix} + 10 \begin{bmatrix} 1/30 \\ 1/3 \\ -2/30 \end{bmatrix} = \begin{bmatrix} 1+10(1/30) \\ 30+10(1/3) \\ 2+10(-2/30) \end{bmatrix} = \begin{bmatrix} 4/3 \\ 100/3 \\ 4/3 \end{bmatrix} $$

---

*Página 138*

## ACTIVIDADES DE AUTOEXAMEN

### ACTIVIDAD 1

**RESPONDA LAS SIGUIENTES PREGUNTAS**

1.-Sea $c_1 x_1 + c_2 x_2 + \ldots + c_k x_k$ la función objetivo de un modelo de PL (maximización o minimización), y $b_1 y_1 + b_2 y_2 + \ldots + b_L y_L$ la función objetivo del problema dual:
a) ¿Cuántas restricciones hay en el problema primal?
b) ¿Cuántas restricciones hay en el problema dual?
c) Si $(u_1, u_2, \ldots, u_k)$ es una solución factible del primal y $(v_1, v_2, \ldots, v_L)$ es una solución factible del dual,
¿Qué puede decir en relación a los dos valores objetivos?

2.- Si el coeficiente $c_i$ precede a una variable básica, ¿en cuánto se modifica el valor del funcional, si se modifica el valor de $c_i$ de dentro de los límites del intervalo de optimidad?

3.- En caso de un problema de mínimo, ¿cómo deberá modificarse el coeficiente $c_j$ de una variable no básica, para que la solución deje de ser óptima?

4.- ¿Cómo se calcula el intervalo de variación de $b_i$ correspondiente a una restricción no limitante del tipo $\geq$? ¿Qué sucede en este caso con el valor de la función objetivo y con los valores de las variables?

5.- ¿Qué ocurre con la solución óptima y con el valor de Z, cuando cambia el $b_i$ de una restricción limitante, dentro de los límites dados por el intervalo de sensibilidad?

### ACTIVIDAD 2

**EXPLIQUE SI LAS SIGUIENTES AFIRMACIONES SON VERDADERAS O FALSAS:**

A. "Al realizar el análisis de sensibilidad, una restricción del tipo $\leq$ con holgura positiva, tendrá siempre un aumento admisible infinito en el lado derecho"
B. “Cuando en el óptimo de un programa lineal, un insumo es escaso, la variable dual que se relaciona con la restricción correspondiente a dicho insumo es positiva”

---

*Página 139*

### ACTIVIDAD 3

Explique:
a) ¿Qué representa el costo reducido (reduced cost) que aparece en los informes de computadora sobre la solución de un PL?
b) ¿Cuál es la utilidad de esta información?
c) ¿En qué parte de la tabla simplex se encuentra?

### ACTIVIDAD 4

En base al problema de la SuperMovil SA y su tabla óptima de simplex:
A) Encuentre los intervalos de sensibilidad para cada uno de los coeficientes de la función objetivo y para cada uno de los valores del lado derecho.
B) Resuelva el problema con algún software específico y responda:
a) ¿Para qué valores de contribución de un teléfono FX120 la base actual es óptima?
b) Si el trabajador 2 estuviera dispuesto a trabajar solamente 30 horas a la semana, ¿qué efectos tendrá sobre la solución óptima y sobre el valor de Z? Encuentre la nueva solución óptima.
c) Si el trabajador 1 estuviera dispuesto a trabajar horas extras por un precio adicional de \$2, ¿conviene contratarlo? De ser conveniente, ¿hasta cuántas horas se podrían contratar a ese precio?
d) A RM le ofrecen una partida de 20 chips adicionales con un descuento del 50%, le conviene comprarla, ¿por qué?
e) Plantear el problema dual
f) Dar la solución del problema dual.

### ACTIVIDAD 5

En la empresa Amarras SA Juan es gerente de producción y está tratando de decidir cuantos ganchos para trailer debe hacer para usar un metal de desperdicio. Tiene tres tipos de metal y puede hacer cualquiera de tres tipos de ganchos. En la tabla siguiente se proporcionan los datos necesarios:

| Metal | Gancho 1 | Gancho 2 | Gancho 3 | Disponible |
|---|---|---|---|---|
| Hierro acanalado | 4 | 5 | 6 | 950 |
| Hierro plano | 6 | 3 | 5 | 800 |
| Hierro redondo | 4 | 8 | 6 | 1150 |

La contribución a las utilidades es de \$13 por cada gancho tipo 1, \$16 por gancho 2 y \$14 por gancho tipo 3.
Ya hay un pedido comprometido de 40 ganchos tipo 3.

---

*Página 140*

El modelo lineal para este problema es:
**max** $13 G_1 + 16 G_2 + 14 G_3$
**sa**
$$ 4 G_1 + 5 G_2 + 6 G_3 \leq 950 \quad \text{Hierro acanalado} $$
$$ 6 G_1 + 3 G_2 + 5 G_3 \leq 800 \quad \text{Hierro plano} $$
$$ 4 G_1 + 8 G_2 + 6 G_3 \leq 1150 \quad \text{Hierro redondo} $$
$$ G_3 \geq 40 \quad \text{Producción mínima} $$

Usando la salida del software LINDO o SOLVER, responda:
a) Especifique cuál es la solución óptima y cuál el beneficio máximo.
b) Juan recibió una oferta de hierro redondo a \$1.- adicional por unidad. ¿Deberá comprarlo?
c) ¿Hasta qué cantidad puede comprar a ese precio?
d) ¿En cuánto podría incrementarse la utilidad total por unidad adicional de hierro plano?
e) Si la utilidad del gancho 2 se incrementa en \$5.- por unidad ¿cuál será la nueva solución y cuál el valor de la utilidad total (si es que existe alguna variación)?
f) ¿Qué significa (con respecto al problema) el valor de la variable dual correspondiente a la última restricción?

```text
OBJECTIVE FUNCTION VALUE
1)  2667.500

VARIABLE      VALUE          REDUCED COST
G1            57.500000      0.000000
G2            85.000000      0.000000
G3            40.000000      0.000000

ROW           SLACK OR SURPLUS  DUAL PRICES
H ACANAL      55.000000         0.000000
H PLANO       0.000000          1.111111
H REDON       0.000000          1.583333
PRO MIN       0.000000         -1.055556

RANGES IN WHICH THE BASIS IS UNCHANGED:

                           OBJ COEFFICIENT RANGES
VARIABLE      CURRENT          ALLOWABLE        ALLOWABLE
              COEF             INCREASE         DECREASE
G1            13.000000        19.000000        1.727273
G2            16.000000        10.000000        2.375000
G3            14.000000        1.055556         INFINITY

                           RIGHTHAND SIDE RANGES
ROW           CURRENT          ALLOWABLE        ALLOWABLE
              RHS              INCREASE         DECREASE
H ACANAL      950.000000       INFINITY         55.000000
H PLANO       800.000000       165.000000       258.750000
H REDON       1150.000000      110.000000       510.000000
PRO MIN       40.000000        41.250000        40.000000
```

---

*Página 141*

**Celdas de variables**

| Nombre | Final Valor | Coste Reducido | Coeficiente Objetivo | Aumentar Permisible | Reducir Permisible |
|---|---|---|---|---|---|
| Variables G1 | 57,5 | 0 | 13 | 19 | 1,7273 |
| Variables G2 | 85 | 0 | 16 | 10 | 2,375 |
| Variables G3 | 40 | 0 | 14 | 1,0556 | 1E+30 |

**Restricciones**

| Nombre | Final Valor | Precio Sombra | Restricción Lado derecho | Aumentar Permisible | Reducir Permisible |
|---|---|---|---|---|---|
| H.Acanaldo | 895 | 0 | 950 | 1E+30 | 55 |
| H. Plano | 800 | 1,1111 | 800 | 165 | 258,75 |
| H. Redondo | 1150 | 1,5833 | 1150 | 110 | 510 |
| Prod. Mínima | 40 | -1,0556 | 40 | 41,25 | 40 |

### ACTIVIDAD 6

La siguiente tabla corresponde a un PL de maximización canónico:

| | | $c_j$ | 40 | 60 | 50 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| $C_B$ | Base | VLD | $x_1$ | $x_2$ | $x_3$ | $S_1$ | $S_2$ | $S_3$ |
| | | 600 | 1/2 | 0 | 1 | 0 | 0 | 1/2 |
| | | 200 | 9/4 | 1 | 0 | 1/2 | 0 | -1/4 |
| | | 200 | -5/4 | 0 | 0 | -1/2 | 1 | 1/4 |
| | $Z_j$ | | | | | | | |
| | $c_j - z_j$ | | | | | | | |

a) Complete la tabla, ¿es esta la solución óptima? ¿Por qué?
b) Si es la solución óptima, entonces dé la solución del problema dual.
c) Si se incrementa la disponibilidad del recurso 3 en 100 unidades, ¿cómo cambia la solución óptima?, ¿cuál es el nuevo valor de z? ¿Cuáles son los nuevos valores de las variables?
d) ¿Qué tipo de solución es la encontrada en c)? (clasifíquela).
e) ¿Cuál es el intervalo de sensibilidad del coeficiente de $x_3$?
f) Calcule los intervalos de sensibilidad para los lados derechos.

### ACTIVIDAD 7

**Caso: Fábrica de bolsos y carteras “Sureñas”**
Rodrigo es un pequeño empresario que se dedica a la fabricación de carteras y bolsos femeninos.
En este momento está analizando el lanzamiento de dos nuevos modelos de bolsos. En su confección utiliza cuero ecológico, herrajes, cierres, hilo de seda reforzado y una tela especial con diseños originales.

El Modelo 1 requiere 3 herrajes, 50 cm de tela, 2 cierres, 15 mts. de hilo de seda reforzado, 20 cm de cuero ecológico y 5 horas de trabajo y se vende a \$1500.

---

*Página 142*

El Modelo 2 requiere 5 herrajes, 60 cm de tela, 1 cierre, 10 mts. de hilo de seda reforzado, 25 cm de cuero ecológico y 8 horas de trabajo y se vende a \$2500.

A los cierres y al hilo de seda los puede conseguir en la cantidad que necesite sin ningún tipo de limitaciones, asimismo, el proveedor de cueros le ha informado que no tiene inconvenientes en proveerle la cantidad que requiera.
Pero no ocurre lo mismo con respecto a la tela estampada, los herrajes y las horas de mano de obra. Para iniciar la producción cuenta con 1300 herrajes, 1400 horas de mano de obra y 85 mts. de tela y puede comprar más tela a un precio de \$120 el mts.

Ha analizado el mercado y estima que puede vender sin ningún problema todos los bolsos de ambos modelos que fabrique. Actualmente tiene comprometidos 24 bolsos del modelo 1.

1. Formule un modelo para este problema.
a. Plantee el objetivo del problema
b. Describa las variables de decisión
c. Plantee un programa lineal que optimice el objetivo
d. Agregue variables de holgura y descríbalas
2. Complete la tabla simplex
a. Indique si es la solución óptima
b. Identifique cuáles son las variables básicas
c. Identifique cuáles son las variables no básicas
d. Identifique cuáles son las restricciones limitantes
e. Identifique cuáles son las restricciones no limitantes

| | | $c_j$ | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|
| $C_j$ | Básicas | VLD | $X_1$ | $X_2$ | $X_3$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
| | | 24 | 1 | 0 | 0 | 0 | 0 | 0 | -1 |
| | | 428 | 0 | 0 | 0 | 0 | 1 | -0.625 | -0.125 |
| | | 23 | 0 | 0 | 1 | -1 | 0 | 0.075 | -0.125 |
| | | 160 | 0 | 1 | 0 | 0 | 0 | 0.125 | 0.625 |
| | $Z_j$ | | | | | | | | |
| | $c_j - z_j$ | | | | | | | | |

3. Resuelva el problema usando un software, con el informe de solución y la tabla simplex responda a Rodrigo:
a) ¿Cuál es el plan de producción óptimo?
b) ¿Cuántos metros de tela se utilizan en la producción? ¿A cuánto asciende el gasto adicional en telas?
c) El proveedor de las telas le informa que desde el próximo mes no podrá entregarle la misma tela, pero que puede reemplazarse por una importada, aunque de mayor calidad, por lo que el precio se verá incrementado en un 90%. A Rodrigo le gustaría saber si sigue con el mismo plan de producción y en su caso en cuánto se vería afectada su contribución total.
d) Rodrigo quiere saber si le convendría incrementar las horas de mano de obra, para lo que podría analizar las siguientes alternativas:
    - A. Contratar personal eventual pagándole a cada trabajador \$32.000 por 160 horas de trabajo mensuales.
    - B. Pagar horas extras al personal efectivo a razón de \$250 la hora extra.
    - C. Combinar las alternativas 1 y 2 de la forma que más convenga.
    En caso de convenirle incrementar las horas de mano de obra, ¿qué alternativa le aconsejaría al empresario?
4. Formule el problema Dual.
5. Explique el significado del precio dual de la cuarta restricción.
6. El empresario quiere saber si le convendría fabricar un nuevo modelo que tiene: 2 herrajes, 1 cierre, 10 mts. de hilo de seda reforzado, 55 cm de tela, 15 cm de cuero ecológico 6 horas de trabajo y se vendería a \$1700. Si lo cree conveniente, sugiera un precio de venta.
7. El proveedor de herrajes le ofreció a Rodrigo una partida de 500 herrajes con un descuento del 50%, ¿le conviene comprarla?
8. Finalmente, Rodrigo decidió contratar 3 trabajadores eventuales (por 160 hs de trabajo mensuales cada uno) y nos consulta sobre el nuevo plan de producción y a cuánto ascenderá el incremento de la contribución a las utilidades.
