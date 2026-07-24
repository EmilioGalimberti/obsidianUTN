## 4. CONCEPTOS BÁSICOS

A continuación enunciaremos algunos conceptos necesarios para continuar con el desarrollo de este capítulo.

**Combinación Lineal convexa de vectores**

Es una combinación lineal convexa de $r$ vectores $V_1, V_2, \ldots, V_r$ es otro vector $V$, tal que:

$$ V = \alpha_1 V_1 + \alpha_2 V_2 + \ldots + \alpha_r V_r $$

---

*Página 62*

Con la condición de que los $\alpha_i \geq 0$ y $\sum_{i=1}^r \alpha_i = 1$, para $i= 1, 2, \ldots, r$

Por ejemplo para el caso de dos dimensiones, si realizamos una combinación lineal convexa de dos vectores obtendremos como resultado un punto (vector) que pertenece al segmento de recta que los une. Gráficamente:

> 📊 [Gráfico 8 - Combinación convexa entre los vectores $V_1$ y $V_2$]

**Conjunto Convexo:** un conjunto de puntos S es un conjunto convexo, si el segmento rectilíneo que une cualquier par de puntos de S, se encuentra completamente en S.

Observe que de las figuras que se muestran a continuación, las dos primeras son conjuntos convexos en tanto que la tercera no lo es.

Para cualquier conjunto convexo S, un punto P es un punto extremo si para cada segmento rectilíneo que se encuentra completamente en S y que pasa por P, P es un extremo del segmento rectilíneo.

Para un problema de PL, en forma estándar, con $m$ ecuaciones de restricción y $n$ variables incluidas las de holgura o excedente, enunciamos los siguientes conceptos respecto al conjunto de soluciones del problema:

- **Solución factible o posible de un PL (SF):** es un conjunto de valores de las variables $x_j$ que verifican el sistema de restricciones incluidas las de no negatividad.

- **Solución Factible Básica (SFB):** es toda solución factible que tiene como máximo $m$ variables positivas; o lo que es lo mismo, tiene al menos $n-m$ valores de las variables nulos. El número máximo de soluciones básicas se calcula de la siguiente manera:

$$ C_m^n = \frac{n!}{m!(n-m)!} $$

---

*Página 63*

- **Solución Factible Básica No Degenerada:** tiene exactamente $m$ variables positivas, o exactamente $n-m$ variables nulas.
- **Solución Factible Básica Degenerada:** tiene menos de $m$ variables positivas, o más de $n-m$ variables nulas.
- **Solución Óptima:** es toda solución que le da a la función Z el máximo (o mínimo) valor.

Podemos resumir estos conceptos en el siguiente diagrama:

> 📊 [Gráfico 9 - Diagrama de clasificación de las Soluciones Factibles]
> **SOLUCIÓN FACTIBLE O POSIBLE** (Todas las $x_j \geq 0$)
> - SOLUCIÓN FACTIBLE NO BÁSICA (Más de $m$ variables $x_i > 0$)
> - SOLUCIÓN FACTIBLE BÁSICA (No Más de $m$ variables $x_i > 0$)
>     - NO DEGENERADA (Exactamente $m$ variables $x_i > 0$)
>     - DEGENERADA (Menos de $m$ variables $x_i > 0$)

## 5. CONSIDERACIONES RESPECTO AL CONJUNTO DE SOLUCIONES

A partir del gráfico del problema de la fábrica de cerámico analicemos, en una tabla, algunos puntos del conjunto de soluciones del problema. Para cada uno de ellos determinemos si las variables (decisión y holgura) son positivas o nulas:

| | A | B | C | D | E |
|---|---|---|---|---|---|
| $x_1$ | $>0$ | $>0$ | $=0$ | $>0$ | $>0$ |
| $x_2$ | $>0$ | $>0$ | $>0$ | $>0$ | $>0$ |
| $S_1$ | $=0$ | $=0$ | $>0$ | $>0$ | $>0$ |
| $S_2$ | $=0$ | $>0$ | $=0$ | $>0$ | $>0$ |
| $S_3$ | $>0$ | $=0$ | $>0$ | $=0$ | $>0$ |

Observe que en los puntos que corresponden a los vértices A, B y C la solución es posible básica (tienen a lo sumo $m=3$ variables positivas). En D y E las soluciones son posibles no básicas (más de $m$ variables positivas).

Considerando lo analizado hasta el momento, podemos hacer las siguientes observaciones:
- Para cumplir con las restricciones de no negatividad de las variables, gráficamente se trabaja siempre en el 1º cuadrante.

---

*Página 64*

- El poliedro de soluciones es un conjunto convexo.
- Los puntos que resulta necesario considerar para buscar el óptimo, son los que se encuentran sobre la frontera de la región factible.
- En particular podemos observar que si el PL tiene solución, ésta se encontrará en, al menos, uno de los vértices.
- Se puede obtener la solución en cada vértice resolviendo en forma simultánea las ecuaciones lineales que lo determinan.
- Las soluciones factibles en los vértices son soluciones factibles básicas.
- Todos los puntos del poliedro de soluciones verifican las restricciones, es decir que el problema tiene infinitas soluciones factibles.
- En todo punto situado sobre una recta no hay sobrante de ese insumo.
- En las ecuaciones determinantes del óptimo (restricciones limitantes), no hay sobrantes de insumos, por lo tanto, las variables de holgura son nulas.
- En las ecuaciones no determinantes del óptimo (restricciones no limitantes) siempre hay sobrantes de insumos, o sea, las variables de holgura son positivas.
- Si el funcional verifica su máximo valor en un único vértice del poliedro, significa que el problema tiene una única solución óptima.
- Si $Z$ fuera paralela a una restricción limitante, el problema tendría infinitas soluciones óptimas.
- Si el óptimo se verifica en un vértice donde se cruzan 3 o más rectas de restricción, la solución óptima es degenerada.

## 6. TEOREMAS DE COMBINACIONES LINEALES CONVEXAS DE SOLUCIONES FACTIBLES

Enunciaremos una serie de teoremas relacionados con las soluciones factibles de los problemas lineales, los que resultarán de utilidad en desarrollos posteriores.

### TEOREMA 1

Este teorema se enuncia como: *“Toda combinación lineal convexa de soluciones factibles de un programa lineal, es otra solución factible de dicho programa”*.

Para demostrarlo partimos de un PL estándar matricial:

---

*Página 65*

Maximizar $CX$
$$ AX = B $$
$$ X \geq 0 $$

Sean $X_1, X_2, \ldots, X_r$ vectores soluciones del PL, por lo tanto se verificará:

$$ AX_1 = B $$
$$ AX_2 = B $$
$$ \vdots \quad (1) $$
$$ AX_r = B $$

Si multiplicamos miembro a miembro las ecuaciones del sistema (1) por escalares $\alpha_1, \alpha_2, \ldots, \alpha_r$ respectivamente, con la condición que, $\alpha_i \geq 0$ y $\sum_{i=1}^r \alpha_i = 1$, tendremos:

$$ \alpha_1 AX_1 = \alpha_1 B $$
$$ \alpha_2 AX_2 = \alpha_2 B $$
$$ \vdots \quad (2) $$
$$ \alpha_r AX_r = \alpha_r B $$

Sumando miembro a miembro:

$$ \sum_{i=1}^r \alpha_i AX_i = \sum_{i=1}^r \alpha_i B $$

Podemos extraer factor común premultiplicando el primer miembro por A y el segundo por B, entonces queda:

$$ A \sum_{i=1}^r \alpha_i X_i = B \sum_{i=1}^r \alpha_i $$

Siendo, $\sum_{i=1}^r \alpha_i = 1$

el vector resultante de la combinación convexa,

$$ \sum_{i=1}^r \alpha_i X_i = X_k $$

será también una solución factible del PL, es decir:

---

*Página 66*

$$ AX_k = B $$

En consecuencia queda demostrado el teorema.

**Corolario del teorema 1:** *“el conjunto de todas las soluciones factibles de un PL, si no es vacío, es un conjunto convexo. Es decir que, si no es vacío, está formado por un único elemento o por una infinidad”*.

### TEOREMA 2

*“Si existe más de una solución factible que le den el mismo valor a la función objetivo, cualquier combinación lineal convexa de las mismas, dará al funcional igual valor”*.

La demostración de este teorema es similar al anterior.
Partimos de un PL en forma estándar matricial:

Maximizar $CX$
$$ AX = B $$
$$ X \geq 0 $$

Sean $X_1, X_2, \ldots, X_r$ vectores soluciones del PL que dan a la función objetivo igual valor, por lo tanto se verificará:

$$ CX_1 = Z_0 $$
$$ CX_2 = Z_0 $$
$$ \vdots \quad (3) $$
$$ CX_r = Z_0 $$

Si multiplicamos miembro a miembro las ecuaciones del sistema (3) por escalares $\alpha_1, \alpha_2, \ldots, \alpha_r$ respectivamente, con la condición que, $\alpha_i \geq 0$ y $\sum_{i=1}^r \alpha_i = 1$ para $i= 1, 2, \ldots, r$, tendremos:

$$ \alpha_1 CX_1 = \alpha_1 Z_0 $$
$$ \alpha_2 CX_2 = \alpha_2 Z_0 \quad (4) $$
$$ \vdots $$
$$ \alpha_r CX_r = \alpha_r Z_0 $$

Si ahora sumamos miembro a miembro, obtendremos:

$$ \sum_{i=1}^r \alpha_i CX_i = \sum_{i=1}^r \alpha_i Z_0 $$

de donde,

$$ C \sum_{i=1}^r \alpha_i X_i = Z_0 \sum_{i=1}^r \alpha_i $$

Como,
$$ \sum_{i=1}^r \alpha_i = 1 $$

tendremos que el vector resultante de la combinación convexa

---

*Página 67*

$$ \sum_{i=1}^r \alpha_i X_i = X_k $$

es también una solución factible del PL que otorga a la función de decisión el mismo valor $Z_0$, es decir:

$$ CX_k = Z_0 $$

En consecuencia, de acuerdo a los teoremas 1 y 2, podemos afirmar que cualquier combinación convexa de soluciones factibles óptimas es también una solución factible óptima.

Por lo cual, respecto al conjunto de soluciones factibles óptimas decimos que es un conjunto convexo, que, si no es vacío, está formado por un elemento o por una infinidad.

### TEOREMA 3

*“Si un PL es resoluble – es decir que posee óptimo -, existirá siempre por lo menos una solución factible básica que también sea óptima”* [^3].
