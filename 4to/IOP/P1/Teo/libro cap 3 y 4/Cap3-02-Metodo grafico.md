## 3. MÉTODO GRÁFICO PARA RESOLVER PROGRAMAS LINEALES

Nos interesa ahora resolver nuestro problema, es decir poder indicarle al decisor cuántos metros cuadrados de cada cerámico deberá producir mensualmente para maximizar su beneficio.

Resolver un programa lineal significa encontrar un conjunto de valores para las variables de decisión que cumpliendo con todas las restricciones – incluidas las de no negatividad-, optimicen a la función objetivo.

De acuerdo a lo anterior y como el modelo tiene sólo dos variables de decisión ($x_1$ y $x_2$), para solucionar el problema de la fábrica de cerámicos podemos utilizar el método gráfico.

Para identificar la solución óptima, debemos encontrar primero el conjunto de todos los valores de $x_1$ y $x_2$ que son solución del sistema de inecuaciones de restricción, y luego de todos ellos identificar cuál optimiza a la función $Z$. Lo hacemos de la siguiente manera:

---

*Página 56*

1. Encontramos el conjunto de puntos que es solución de la primera restricción. Para hacer esto dibujamos la recta representativa de la igualdad $5x_1 + 5x_2 = 300$ y a continuación verificamos cuál es el semiplano que cumple con la restricción [^2].

Siempre debemos tener en cuenta que las restricciones de no negatividad ubican el gráfico en el primer cuadrante.

> 📊 [Gráfico 1 - Región definida por $5x_1 + 5x_2 \leq 300$]

2. A continuación identificamos el conjunto de puntos que es solución de las dos primeras restricciones, para ello introducimos en el gráfico a la restricción: $4x_1 + 8x_2 \leq 400$, verificamos cuál es el semiplano que es solución de esta restricción y luego identificamos el conjunto de puntos solución de ambas restricciones. Hacemos lo mismo hasta incluir a todas las restricciones.

> 📊 [Gráfico 2 - Región definida por las dos primeras restricciones]
> 📊 [Gráfico 3 - Región factible completa incluyendo la última restricción]

3. Una vez encontrado el conjunto solución o región factible, para identificar la solución óptima, debemos graficar la función $Z$.

[^2]: Esto se logra reemplazando en la inecuación a $x_1$ y $x_2$ por las coordenadas de un punto, como por ejemplo el $(0, 0)$.

---

*Página 57*

Para nuestro problema, $Z = 8x_1 + 6x_2$, siendo la forma explícita de la ecuación de esta recta:

$$ x_2 = \frac{Z}{6} - \frac{8}{6} x_1 $$

Observe que esta ecuación define a una “familia” de rectas paralelas y que a medida que se incrementa el valor de $Z$ (contribución total en este caso), se obtienen rectas paralelas cada vez más alejadas del origen.

Esto nos permite afirmar que, el sentido de optimidad en el desplazamiento de $Z$, será alejándola del origen y como consecuencia, el punto de mayor utilidades será el último punto de contacto entre $Z$ y el polígono de soluciones.

Note que no se habla del punto más alejado del origen, ya que esto involucra el concepto de distancia al origen, el cual no es acertado en este caso.

Para identificar este punto, se debe introducir la recta $Z$ en el gráfico. Luego, la desplazamos en su sentido de optimidad. Es aconsejable darle a $Z$ un valor arbitrario para poder dibujarla.

> 📊 [Gráfico 4 - Función objetivo $Z$ y su desplazamiento en sentido de maximización]

> 📊 [Gráfico 5 - Analice cuál es el sentido de optimidad si el objetivo fuera: $\max Z = 8x_1 - 6x_2$]

Vemos que el punto óptimo se forma con la intersección de las restricciones de horas de mano de obra y de horas de cocción. Para encontrar la solución óptima, se debe resolver el sistema de ecuaciones:

$$ 6x_1 + 4x_2 = 320 $$
$$ 5x_1 + 5x_2 = 300 $$

---

*Página 58*

**Solución Óptima:**
- $x_1 = 40 \, m^2$
- $x_2 = 20 \, m^2$

**Valor de la Función objetivo en el óptimo:**
- $Z = \$ 440$

| | Hrs. Requeridas para $x_1= 40 \, m^2$ y $x_2= 20 \, m^2$ | Horas disponibles | Horas no utilizadas | Tipo de restricción |
|---|---|---|---|---|
| **HMO** | 5(40) + 5(20) = 300 | 300 | 0 | Limitante |
| **Hrs. Secado** | 4(40) + 8(20) = 320 | 400 | 80 | No limitante |
| **Hrs. Cocción** | 6(40) + 4(20) = 320 | 320 | 0 | Limitante |

*Tabla 2*

En la tabla anterior podemos observar que existen 80 horas de secado que no han sido utilizadas ($S_2 = 80$) en tanto que para las horas de mano de obra y de cocción se utilizaron todos los recursos.

En definitiva, la respuesta que podemos darle al responsable de la empresa es que, para obtener la máxima contribución total a las utilidades que será de \$ 440.- debe fabricar 40 unidades del Producto I y 20 unidades del Producto II. Siguiendo este plan de producción utilizará todas las horas de mano de obra y todos los materiales disponibles, quedando sin usar 80 horas máquina.

**Resumen de los pasos en la aplicación del Método gráfico:**
1. Identificar el conjunto de soluciones posibles del problema o región factible.
2. Trazar la recta representativa de la función objetivo.
3. Desplazar la recta en el sentido de optimización hasta identificar el último punto de contacto entre la recta y la región factible. Este punto es la solución óptima y corresponde a un vértice del polígono de soluciones.
4. Encontrar los valores de las variables que optimizan la función objetivo, resolviendo en forma simultánea las ecuaciones de restricción que determinan el punto óptimo.
5. Encontrar los valores de las variables de holgura/excedente, reemplazando los valores de las variables de decisión en cada una de las ecuaciones de restricción.
6. Encontrar el valor de $Z$ reemplazando los valores de las variables en la función objetivo.

---

*Página 59*

En los casos en que el problema tiene más de tres variables de decisión es imposible utilizar el método gráfico. Esto resulta una gran limitación, ya que los problemas reales tienen gran cantidad de variables y restricciones. Afortunadamente, existe un método algebraico para resolver programas lineales que se llama **Método Simplex**, el cual veremos en detalle más adelante.


En los casos en que el problema tiene más de tres variables de decisión es imposible utilizar el método gráfico. Esto resulta una gran limitación, ya que los problemas reales tienen gran cantidad de variables y restricciones. Afortunadamente, existe un método algebraico para resolver programas lineales que se llama **Método Simplex**, el cual veremos en detalle más adelante.

### UN PROBLEMA DE MINIMIZACIÓN

El dueño de una pequeña tienda de mascotas prepara una mezcla especial de comida, para los perros que tiene en guardería durante el fin de semana, combinando dos alimentos, a los que llamaremos I y II.

El veterinario ha sugerido que la grasa contenida en la mezcla no debe superar los 300 gramos y que por lo menos debe tener 40 unidades de vitamina A.

El alimento I contiene 10 grs. de grasa y 4 unidades de vitamina A por cada kg., mientras que el II contiene 20 grs. de grasa y 3 unidades de vitamina A por Kg. También aconsejó incluir en la mezcla por lo menos 3 kg de alimento II.

Además de lo indicado por el veterinario debe tener en cuenta que del alimento I solamente puede conseguir hasta 8 kg. por semana y que, debido a la cantidad promedio de perros en la guardería, necesita por lo menos 12 kg. de mezcla por fin de semana.

El costo del alimento I es de \$5 por kg. y el del alimento II es de \$7 por kg.

Para modelizar este problema debemos identificar el objetivo, definir a las variables y enunciar las restricciones en forma verbal.

**Objetivo:**
minimizar el costo total de la mezcla de alimentos.

**Variables:**
- $x_1$ = Kg. de alimento tipo I a incluir en la mezcla.
- $x_2$ = Kg. de alimento tipo II a incluir en la mezcla.

**Restricciones:**
- El contenido máximo de grasa en la mezcla no debe superar los 300 grs.
- La mezcla debe contener por lo menos 40 unidades de vitamina A.
- Se pueden conseguir hasta 8 kgs. de alimento I por semana.
- La mezcla debe contener por lo menos 3 kgs. del alimento II.
- Se necesitan por lo menos 12 kgs. de mezcla por fin de semana.
- Las variables no pueden asumir valores negativos.

El modelo de PL para este problema es el siguiente:

---

*Página 60*

$$ \min Z = 5x_1 + 7x_2 $$
**s.a.**
$$ 10x_1 + 20x_2 \leq 300 $$
$$ 4x_1 + 3x_2 \geq 40 $$
$$ x_1 \leq 8 $$
$$ x_2 \geq 3 $$
$$ x_1 + x_2 \geq 12 $$
$$ x_1, x_2 \geq 0 $$

Resolvemos gráficamente siguiendo los pasos anteriormente enumerados en el método.

1. Identificamos a la región factible, es decir al conjunto de puntos que es solución de todas las inecuaciones del sistema de restricciones del PL.

> 📊 [Gráfico 6 - Región factible del problema de minimización]

2. Introducimos en el gráfico a la recta representativa de $Z$ y luego la desplazamos en su sentido de optimidad para identificar al punto óptimo.

Como en este caso la función objetivo representa un costo, al disminuir el valor de $Z$ en la ecuación de la recta, la ordenada al origen también disminuye y por lo tanto podemos decir que el sentido de optimidad de $Z$ se encuentra desplazándola hacia el origen.

En el gráfico siguiente, se representa a $Z$ con línea de puntos.

> 📊 [Gráfico 7 - Función $Z$ desplazada hacia el origen para minimizar]

---

*Página 61*

Puede observarse que el punto óptimo se forma por la intersección de las rectas que representan a las restricciones:
$$ x_1 \leq 8 $$
$$ x_1 + x_2 \geq 12 $$

Con ellas planteamos un sistema de dos ecuaciones que nos permitirán determinar los valores de las variables de decisión.

A continuación se encuentran los valores de las variables de holgura/excedente reemplazando a las variables de decisión, por sus respectivos valores, en las restricciones.

La solución completa es:

| VARIABLE | VALOR |
|---|---|
| $x_1$ | 8 |
| $x_2$ | 4 |
| $S_1$ | 140 |
| $S_2$ | 4 |
| $S_3$ | 0 |
| $S_4$ | 1 |
| $S_5$ | 0 |

Esta solución óptima le da a la FO el valor $Z = \$ 68$.-

El informe al dueño de la tienda de mascotas debería contener como mínimo la siguiente información:
- Cantidad de mezcla a preparar por fin de semana: 12 kg.
- Composición: 8 kg. del alimento tipo I y 4 Kg. del alimento tipo II.
- Costo de la mezcla por fin de semana: \$68.-

Especificaciones técnicas:
- Contiene 1 kg. por encima del mínimo requerido del alimento II y exactamente el máximo permitido del alimento I.
- La cantidad de grasa aportada es de 160 grs. y contiene 44 unidades de vitamina A.