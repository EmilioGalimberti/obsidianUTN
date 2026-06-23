# CAPÍTULO 3 - PROGRAMACIÓN LINEAL

---

*Página 50*

## 1. INTRODUCCIÓN

Debido a que la esencia de la PL puede transmitirse mejor a través de un modelo concreto, comenzamos el análisis de este tema mediante un ejemplo.

Una fábrica de cerámicos quiere determinar el plan de producción óptimo de sus dos productos:
- Cerámicos Esmaltados
- Cerámicos Rústicos

El proceso de producción de los cerámicos requiere diferentes combinaciones de horas de mano de obra, horas de secado y de cocción. Para la fabricación de un $m^2$ de cerámico esmaltado son necesarias 5 horas de mano de obra, 4 horas de secado y 6 horas de cocción. Por cada $m^2$ de cerámico rústico se requieren 5 horas de mano de obra, 8 horas de secado y 4 horas de cocción.

La contribución a las utilidades por cada $m^2$ de cerámico son:
- \$8 para el cerámico esmaltado
- \$6 para el cerámico rústico

Teniendo en cuenta que la fábrica dispone de 300 horas de mano de obra, 400 horas para secado y 320 horas para cocción por mes, formule un modelo que le permita a la fábrica determinar el plan de producción que maximice la contribución a las utilidades.

| | Cerámico Esmaltado | Cerámico Rústico | Disponibilidad hrs. mensuales |
|---|---|---|---|
| **Horas de Mano de Obra / $m^2$** | 5 | 5 | 300 |
| **Horas de Secado / $m^2$** | 4 | 8 | 400 |
| **Horas de Cocción / $m^2$** | 6 | 4 | 320 |
| **Contribución a las utilidades / $m^2$** | 8 | 6 | |

*Tabla 1*

Vamos a suponer además, que la empresa no tiene limitaciones respecto a la demanda, es decir, puede vender todo lo que produce.

---

*Página 51*

Al proceso de representar este problema mediante un modelo matemático, se denomina modelización o planteamiento del modelo lineal.

### ALGUNAS CONSIDERACIONES AL MOMENTO DE MODELIZAR

En primer lugar, analizaremos las características del problema:

- La empresa tiene como objetivo la maximización de las utilidades provenientes de la fabricación de los cerámicos rústicos y esmaltados.
- La contribución máxima a las utilidades que puede lograrse está sujeta a la disponibilidad de los insumos.
- Tanto las utilidades como el uso de los insumos son proporcionales a la cantidad que se fabrique de los productos.
- No es posible fabricar cantidades negativas de los productos.

Las características observadas en este problema son comunes a un tipo importante de situaciones que pueden ser representadas a través de un modelo matemático, conocido como **Programación Lineal (PL)**.

De acuerdo a las consideraciones anteriores, desarrollaremos un modelo matemático que represente el problema enunciado. Para modelizar un problema debemos identificar el objetivo, definir a las variables y enunciar las restricciones en forma verbal. Para nuestro ejemplo serán:

**Objetivo:** maximizar la contribución total a las utilidades.

> **Nota:** Observe que las variables están definidas con unidad de medida y para un periodo de análisis.

**Variables de decisión:**
- $x_1$ : $m^2$ de cerámicos esmaltados a fabricar mensualmente.
- $x_2$ : $m^2$ de cerámicos rústicos a fabricar mensualmente.

**Restricciones:**
- La cantidad de horas de mano de obra a utilizar mensualmente no debe superar las 300.
- La cantidad de horas de secado a utilizar mensualmente no debe superar las 400.
- La cantidad de horas de cocción a utilizar mensualmente no debe superar las 320.

Es conveniente, al momento de modelizar, controlar siempre las unidades de medida.

Cuando estemos seguros de haber identificado a todas las restricciones del problema, podremos representarlo a través de un modelo matemático.

---

*Página 52*

### MODELO MATEMÁTICO

$$ \max Z = 8x_1 + 6x_2 $$
$$\left[\frac{\$}{m^2}\right][m^2]$$

**Sujeto a:**
$$ 5x_1 + 5x_2 \leq 300 \quad \text{(Hrs. M O)} $$
$$\left[\frac{\text{hsMO}}{m^2}\right][m^2] \quad [\text{hsMO}]$$

$$ 4x_1 + 8x_2 \leq 400 \quad \text{(Hrs. Secado)} $$
$$ 6x_1 + 4x_2 \leq 320 \quad \text{(Hrs. Cocción)} $$

$$ x_1, x_2 \geq 0 $$

Finalmente el modelo es:

$$ \max Z = 8x_1 + 6x_2 $$
$$ \text{s.a.} \begin{cases} 
5x_1 + 5x_2 \leq 300 & \text{(Hs de M O)} \\ 
4x_1 + 8x_2 \leq 400 & \text{(Hs de Secado)} \\ 
6x_1 + 4x_2 \leq 320 & \text{(Hs de Cocción)} \\ 
x_1, x_2 \geq 0 
\end{cases} $$

Observe que en el primer miembro de las restricciones está representado el uso del recurso y en el segundo miembro (lado derecho) se encuentra la disponibilidad del mismo. Asimismo, la última restricción: $x_1, x_2 \geq 0$ expresa que las variables del problema sólo pueden asumir valores reales no negativos.

Analizando las restricciones del problema, observamos que se admite la posibilidad de utilizar una menor cantidad de recursos que los disponibles. Esta situación puede representarse matemáticamente a través de variables que representen los insumos no utilizados, conocidas con el nombre de variables de holgura o excedente.

Estas variables aparecen en el objetivo con coeficiente nulo, dado que no aportan nada a las utilidades.

$$ \max Z = 8x_1 + 6x_2 + 0S_1 + 0S_2 + 0S_3 $$
$$ \text{s.a.} \begin{cases} 
5x_1 + 5x_2 + S_1 = 300 & \text{(Hs de Mano de Obra)} \\ 
4x_1 + 8x_2 + S_2 = 400 & \text{(Hs de Secado)} \\ 
6x_1 + 4x_2 + S_3 = 320 & \text{(Hs de Cocción)} \\ 
x_1, x_2, S_1, S_2, S_3 \geq 0 
\end{cases} $$

Siendo:
- $S_1$ = cantidad de sobrante de horas de mano de obra.
- $S_2$ = cantidad de sobrante de horas de secado.
- $S_3$ = cantidad de sobrante de horas de cocción.

---

*Página 53*

## 2. MODELO MATEMÁTICO GENERAL DE LA PROGRAMACIÓN LINEAL

La Programación Lineal es un modelo de Programación Matemática [^1] en el cual, la función a optimizar (maximizar o minimizar) es lineal y cuyas variables (no negativas) están sujetas a un conjunto de restricciones también lineales, expresadas como desigualdades del tipo $\geq$, $\leq$ o igualdades.

El modelo puede ser expresado de diferentes maneras:

### FORMA EXPLÍCITA

Maximizar $Z = c_1 x_1 + c_2 x_2 + c_3 x_3 + \ldots + c_n x_n$

Sujetas las $x_j$ a:
$$ a_{11} x_1 + a_{12} x_2 + a_{13} x_3 + \ldots + a_{1n} x_n \leq b_1 $$
$$ a_{21} x_1 + a_{22} x_2 + a_{23} x_3 + \ldots + a_{2n} x_n \leq b_2 $$
$$ \vdots $$
$$ a_{m1} x_1 + a_{m2} x_2 + a_{m3} x_3 + \ldots + a_{mn} x_n \leq b_m $$

$$ \forall x_j \geq 0 \quad (j = 1, 2, \ldots, n) $$

Dónde:
- $x_j$ son las variables de decisión del modelo.
- $c_j$ son parámetros que preceden a las variables en la función objetivo (FO) y generalmente representan beneficios, ingresos o costos unitarios, los que pueden ser monetarios o no.
- $a_{ij} \, (i=1, 2, \ldots, m)$ son parámetros que representan coeficientes técnicos en las restricciones.
- $b_i$ son los términos independientes de las restricciones. Estos parámetros generalmente representan disponibilidades de insumos o requerimientos necesarios.

Es conveniente aclarar que el modelo puede presentar algunas variantes y aún así será un modelo de PL, ellas son:
- El objetivo puede ser minimizar.
- Algunas o todas las restricciones pueden ser del tipo mayor o igual que ($\geq$) o de igualdad ($=$).

### FORMA MATRICIAL

Maximizar $Z = CX$

[^1]: En el anexo 1 se caracteriza un modelo de Programación Matemática.

---

*Página 54*

$$ AX \leq B $$
$$ X \geq 0 $$

donde:
- $C$ = es un vector fila de orden $1 \times n$
- $X$ = es un vector columna de orden $n \times 1$
- $A$ = matriz de orden $m \times n$
- $B$ = es un vector columna de orden $m \times 1$

$$ X = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} \quad C = [c_1, c_2, \ldots, c_n] \quad A = \begin{bmatrix} a_{11} & a_{12} & \ldots & a_{1n} \\ a_{21} & a_{22} & \ldots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \ldots & a_{mn} \end{bmatrix} \quad B = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix} $$

### FORMA VECTORIAL

$$ \text{Máx } \sum_{j=1}^n c_j x_j $$
$$ \text{s.a.} \sum_{j=1}^n P_j x_j \leq P_0 $$
$$ x_j \geq 0, \quad \forall j $$

Donde:
$$ P_j = \begin{bmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{mj} \end{bmatrix} \quad P_0 = B = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix} $$

### FORMA ESTÁNDAR (matricial)

Un PL en forma estándar tiene todas las restricciones de igualdades (independientemente de que la FO sea de máximo o mínimo), es decir:

| Maximizar CX | Minimizar CX |
|---|---|
| $AX = B$ | $AX = B$ |
| $X \geq 0$ | $X \geq 0$ |

### FORMA CANÓNICA (matricial)

Un PL en forma canónica es aquel que:
- en caso de máximo, todas las restricciones son del tipo $\leq$
- en caso de mínimo, todas las restricciones son de $\geq$

| Maximizar CX | Minimizar CX |
|---|---|
| $AX \leq B$ | $AX \geq B$ |
| $X \geq 0$ | $X \geq 0$ |

---

*Página 55*

### FORMA MIXTA (matricial)

Cuando las restricciones son de cualquier tipo, cualquiera sea el sentido de optimidad de la FO, decimos que el PL es mixto.

| Maximizar CX | Minimizar CX |
|---|---|
| $AX [\geq, =, \leq] B$ | $AX [\geq, =, \leq] B$ |
| $X \geq 0$ | $X \geq 0$ |

### SUPUESTOS DEL MODELO

Este modelo tiene implícitos ciertos supuestos, algunos de los cuales son obvios mientras que otros no tanto. De todas maneras es importante tenerlos presente al momento de analizar un problema. Ellos son:

- **Un único objetivo** que está sujeto a restricciones, y a las restricciones de no negatividad de las variables.
- **Aditividad**, lo que implica que las contribuciones de los productos individuales son aditivas.
- **Proporcionalidad**, esto es, que tanto la función objetivo como las restricciones deben ser proporcionales al nivel de las variables.
- **Divisibilidad**, es decir que las variables deben ser divisibles a cualquier nivel fraccionario.
- **Certidumbre**, lo que supone que los parámetros del modelo se conocen con certeza.