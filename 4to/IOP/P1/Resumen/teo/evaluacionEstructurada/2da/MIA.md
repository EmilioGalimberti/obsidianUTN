
# 1)
![[Pasted image 20260607222746.png]]
![[{CB82E746-42A2-4178-B7FF-12C343CE263E}.png]]
## RTA
Como tu Tutor Académico de Élite, he analizado la `[[Tabla Simplex]]` óptima que presentas para resolver el cálculo analítico de los `[[Intervalos de Sensibilidad]]` correspondientes a los parámetros $C_3$ y $b_3$.

A continuación, te desgloso paso a paso la justificación matemática utilizando la teoría oficial de la cátedra, garantizando el cumplimiento de la regla de truncamiento a tres decimales exigida.

# RTA

## 1. Variación en $C_3$ ([[Coeficientes de la Función Objetivo]])

El parámetro $C_3$ corresponde al coeficiente de la variable $x_3$. Al inspeccionar la columna "Base" en tu tabla, vemos que $x_3$ es una **`[[Variable Básica]]`**.

> [!tip] Metodología para Coeficientes Básicos Si cambia el coeficiente de una variable que está en la base, este cambio impacta a toda la fila de evaluación $C_j - Z_j$. Debemos garantizar la `[[Condición de Optimidad]]` exigiendo que ninguna diferencia marginal de las variables no básicas se vuelva positiva.

> [!note] Fórmula del Intervalo de Optimidad Para un incremento $\Delta c_k$, se debe cumplir para toda variable no básica $j$: $$ (C_j - Z_j) - \Delta c_k \cdot \lambda_{kj} \le 0 $$ _(Donde $\lambda_{kj}$ son las `[[Tasas de Sustitución]]` ubicadas en la fila de la variable analizada)_.

Aplicamos la inecuación para las variables no básicas ($x_2, S_2, S_3$), leyendo la fila de $x_3$ ($\lambda_{3j}$):

- **Para $x_2$:** $-7,377 - \Delta c_3 \cdot (0,632) \le 0 \Rightarrow -7,377 \le 0,632 \cdot \Delta c_3 \Rightarrow \Delta c_3 \ge -\frac{7,377}{0,632} \Rightarrow \Delta c_3 \ge -11,672...$
- **Para $S_2$:** $-0,458 - \Delta c_3 \cdot (0,053) \le 0 \Rightarrow -0,458 \le 0,053 \cdot \Delta c_3 \Rightarrow \Delta c_3 \ge -\frac{0,458}{0,053} \Rightarrow \Delta c_3 \ge -8,641...$
- **Para $S_3$:** $-0,324 - \Delta c_3 \cdot (-0,021) \le 0 \Rightarrow -0,324 + 0,021 \cdot \Delta c_3 \le 0 \Rightarrow 0,021 \cdot \Delta c_3 \le 0,324 \Rightarrow \Delta c_3 \le \frac{0,324}{0,021} \Rightarrow \Delta c_3 \le 15,428...$

Intersectando los resultados y aplicando la regla del límite más restrictivo, la variación neta permitida es: **$-8,641 \le \Delta c_3 \le 15,428$**

## 2. Variación en $b_3$ ([[Valor del Lado Derecho]])

El parámetro $b_3$ es el recurso de la tercera restricción. Su variable de holgura asociada es $S_3$. Al mirar la base, notamos que $S_3$ asume el valor $0$ (es una **`[[Variable No Básica]]`**), lo que nos confirma que estamos evaluando una **`[[Restricción Limitante]]`**.

> [!tip] Metodología para Lados Derechos Limitantes Altera los valores de las variables en la base. Debemos asegurar la `[[Condición de Factibilidad]]` (que ninguna variable básica asuma un valor negativo).

> [!note] Fórmula de Factibilidad Para una variación $\Delta b_k$, se debe cumplir para toda variable en la base $i$: $$ VLD_i + \Delta b_k \cdot \lambda_{i,S_k} \ge 0 $$ _(Donde $\lambda_{i,S_k}$ son los elementos de la columna de la holgura asociada al recurso)_.

Aplicamos la inecuación leyendo la columna de $S_3$ para las variables básicas actuales ($S_1, x_3, x_1$):

- **Fila $S_1$:** $285,965 + \Delta b_3 \cdot (-0,561) \ge 0 \Rightarrow 285,965 \ge 0,561 \cdot \Delta b_3 \Rightarrow \Delta b_3 \le \frac{285,965}{0,561} \Rightarrow \Delta b_3 \le 509,741...$
- **Fila $x_3$:** $29,474 + \Delta b_3 \cdot (-0,021) \ge 0 \Rightarrow 29,474 \ge 0,021 \cdot \Delta b_3 \Rightarrow \Delta b_3 \le \frac{29,474}{0,021} \Rightarrow \Delta b_3 \le 1403,523...$
- **Fila $x_1$:** $38,596 + \Delta b_3 \cdot (0,044) \ge 0 \Rightarrow 0,044 \cdot \Delta b_3 \ge -38,596 \Rightarrow \Delta b_3 \ge -\frac{38,596}{0,044} \Rightarrow \Delta b_3 \ge -877,181...$

Intersectando los resultados y tomando los límites más estrictos, la variación permitida es: **$-877,181 \le \Delta b_3 \le 509,741$**

> [!danger] Atención de Parcial: Cuidado con la Desigualdad y el Límite Observa que en la Fila $x_1$ tenemos un valor positivo $(0,044)$, por lo que la inecuación nos marca el tope de "caída" (límite inferior o $\ge$), y en las otras filas nos marcan el tope de "subida" (límite superior o $\le$). Se elige siempre la cota más restrictiva.

---

### Diagrama de Post-Optimidad

```
graph TD
    A[Analisis de Intervalos de Sensibilidad] --> B{Que parametro se modifica?}

    B -->|Coeficiente Objetivo C3| C[Afecta la fila de evaluacion Cj-Zj]
    C --> D[Evaluar a traves de la fila x3]
    D --> E[Garantizar Condicion de Optimidad]
    E --> F[-8.641 <= Delta C3 <= 15.428]

    B -->|Lado Derecho b3| G[Afecta el vector solucion VLD]
    G --> H[Evaluar a traves de la columna S3]
    H --> I[Garantizar Condicion de Factibilidad]
    I --> J[-877.181 <= Delta b3 <= 509.741]
```

_Conceptos Relacionados:_ `[[Condición de Optimidad]]`, `[[Condición de Factibilidad]]`, `[[Tasas de Sustitución]]`.

---

### Tabla de Resultados (Truncados a 3 decimales)

Conforme a la instrucción imperativa del sistema, he extraído directamente el valor absoluto de crecimiento y decrecimiento truncando (cortando, sin redondear hacia arriba) a tres decimales.

| Parámetro | Incremento | Disminución |
| :-------- | :--------- | :---------- |
| **C3**    | 15,428     | 8,641       |
| **b3**    | 509,741    | 877,181     |
# 2)
![[Pasted image 20260607222954.png]]
3
2
# 3)
![[Pasted image 20260607223054.png]]
Si decide producir 12 kilos de premezcla 3, el nuevo valor de S1 es:
104,05

Si decide producir 7 kilos de premezcla 3, el nuevo valor de X1 es:
14,225
# RTA 1
Como tu Tutor Académico de Élite, he analizado la **[[Tabla Simplex]]** óptima proporcionada para resolver tu consulta aplicando los teoremas de actualización de variables dictados por la cátedra.

Para determinar el nuevo valor de una variable en la base cuando forzamos la producción de un producto que no es óptimo, aplicamos el concepto de las **[[Tasas de Sustitución]]**. A continuación, te desgloso el cálculo paso a paso.



## 1. Identificación de los Parámetros en la Tabla

Primero extraemos los datos exactos del reporte matricial para las variables involucradas:

- **Variable a forzar ($X_3$):** Corresponde a la premezcla 3. Al no estar en la columna "Base" ($P_0$), sabemos que es una **[[Variable No Básica]]** y su valor actual es $0$. El decisor desea forzar una producción de $\theta = 12$ kilos.
- **Variable a analizar ($S_1$):** Es una **[[Variable Básica]]** (holgura de horas de mano de obra), y su valor actual en la columna solución ($VLD$ o $P_0$) es $\lambda_{S_1} = 148,75$.
- **[[Tasa de Sustitución]] ($\lambda_{S_1, X_3}$):** Es el valor ubicado en la intersección de la fila de la variable básica ($S_1$) y la columna de la variable que ingresa ($X_3$ o $P_3$). En tu tabla, este valor es **$3,725$**.

## 2. Interpretación Económica del Signo

El profesor hace mucho énfasis en interpretar correctamente los signos de esta matriz para no cometer errores lógicos en los parciales:

> [!danger] Trampa de Signos en el Simplex A diferencia del ejercicio anterior donde la tasa era negativa (lo que implicaba un aumento), aquí la tasa de sustitución es **positiva** ($3,725$). Un valor positivo representa un **sacrificio** real. Es decir, por cada kilo de premezcla 3 ($X_3$) que decidas fabricar, el sobrante de horas de mano de obra ($S_1$) va a **disminuir** en $3,725$ horas.

## 3. Cálculo Matemático del Nuevo Valor

Para conocer el impacto exacto, aplicamos la ecuación de actualización de variables derivada del Teorema Fundamental del Método Simplex.

> [!note] Fórmula de Actualización de Variables Básicas $$ X_i^{nuevo} = \lambda_i - \theta \cdot \lambda_{ij} $$ _(Donde $\lambda_i$ es el Valor del Lado Derecho actual, $\theta$ es la cantidad a producir de la nueva variable, y $\lambda_{ij}$ es la tasa de sustitución)_.

Reemplazando algebraicamente con los datos de tu problema:

1. Planteamos la ecuación: $S_1^{nuevo} = 148,75 - 12 \cdot (3,725)$
2. Resolvemos el producto (el sacrificio total): $12 \cdot 3,725 = 44,7$
3. Efectuamos la resta: $148,75 - 44,7$
4. Resultado final: **$104,05$**

### Conclusión a tu Pregunta

**Respuesta:** 104,05

---

## 4. Diagrama Lógico de Decisión

```
graph TD
    A[Decisión Gerencial: Forzar Producción de X3 en 12 kilos] --> B[Identificar Tasa de Sustitución en fila S1]
    B --> C[Tasa en columna P3 = 3,725]
    C --> D{¿Qué significa el signo positivo?}
    D -->|Sacrificio / Reducción| E[Se resta de la cantidad actual de S1]
    E --> F
    F --> G[Nuevo valor de S1: 104,05 horas sobrantes]
```

_Conceptos relacionados:_ [[Tasas de Sustitución]], [[Variable Básica]], [[Variable No Básica]], [[Valor del Lado Derecho]], [[Tabla Simplex]].
# RTA 2
Como tu Tutor Académico de Élite, he aplicado nuevamente los teoremas de actualización del **[[Método Simplex]]** utilizando los datos de la **[[Tabla Simplex]]** óptima que me proporcionaste anteriormente.

Para resolver este nuevo escenario donde decides fabricar 7 kilos en lugar de 4, volvemos a utilizar el concepto de las **[[Tasas de Sustitución]]**.



## 1. Identificación de Parámetros

Extraemos los valores exactos de la matriz para nuestro cálculo:

- **Variable a forzar ($X_3$):** Premezcla 3. Al tener un valor de cero en la tabla óptima, es una **[[Variable No Básica]]**. La nueva cantidad a forzar es $\theta = 7$.
- **Variable a analizar ($X_1$):** Premezcla 1. Es una **[[Variable Básica]]** cuyo valor actual en el **[[Valor del Lado Derecho]]** ($P_0$ o VLD) es $\lambda_1 = 11,25$.
- **[[Tasa de Sustitución]] ($\lambda_{1,3}$):** Se ubica en la intersección de la fila de $X_1$ y la columna de $X_3$ (indicada como $P_3$ en tu tabla). El valor exacto es **$-0,425$**.

## 2. Interpretación Económica y Signo

> [!tip] Recordatorio: Tasa de Sustitución Negativa Como vimos previamente, una tasa de sustitución con signo negativo ($-0,425$) invierte su significado tradicional. En lugar de representar un "sacrificio" de recursos, indica que la variable básica actual se verá **favorecida e incrementará** su valor por cada unidad nueva que introduzcamos.

## 3. Cálculo Matemático del Nuevo Valor

Aplicamos la fórmula general de actualización de variables:

> [!note] Fórmula de Actualización $$ X_i^{nuevo} = \lambda_i - \theta \cdot \lambda_{ij} $$

Reemplazamos con nuestros datos:

1. **Ecuación:** $X_1^{nuevo} = 11,25 - 7 \cdot (-0,425)$
2. **Producto (Impacto total):** $7 \cdot (-0,425) = -2,975$
3. **Aplicación de signos:** $X_1^{nuevo} = 11,25 - (-2,975) \Rightarrow 11,25 + 2,975$
4. **Resultado:** **$14,225$**

### Conclusión

**Respuesta:** Si decide producir 7 kilos de premezcla 3, el nuevo valor de $X_1$ es **$14,225$**.

---

## 4. Diagrama Lógico de Decisión

```
graph TD
    A[Decision Gerencial: Producir 7 kilos de X3] --> B[Identificar VLD y Tasa de Sustitucion]
    B --> C[VLD de X1 = 11.25]
    B --> D[Tasa en columna P3 = -0.425]

    D --> E{Que indica el signo negativo?}
    E -->|Incremento Productivo| F[En lugar de restar, el impacto se suma al VLD]

    C -.-> G[Calculo: 11.25 + 2.975]
    F -.-> G

    G --> H[Nuevo valor de X1: 14.225 kilos]
```

_Conceptos relacionados:_ [[Tasas de Sustitución]], [[Variable Básica]], [[Variable No Básica]], [[Valor del Lado Derecho]], [[Método Simplex]].

# 4)
![[Pasted image 20260607223350.png]]
A)

guardada

![](https://uv.frc.utn.edu.ar/theme/image.php/boost/core/1780687009/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se modifica un coeficiente de la función objetivo, cualquiera sea la variable a la cual pertenece.

Pregunta 5 Seleccione una:

a.

Cambia la inclinación de la función objetivo

b.

Cambia la ordenada al origen de la función objetivo

c.

Se produce una nueva solución óptima

d.

Se obtiene un nuevo valor para la función objetivo

e.

Todas las alternativas son correctas

# RTA
 Resolución: Variación de los [[Coeficientes de la Función Objetivo]]

La respuesta correcta a tu pregunta de examen es la **a. Cambia la inclinación de la función objetivo**.

A continuación, te desgloso la fundamentación teórica y gráfica de por qué esta es la única afirmación universalmente correcta, basándome en los principios del [[Análisis de Sensibilidad]].

## 1. Fundamento Geométrico del Cambio

Si se incrementa o disminuye algún coeficiente de la [[Función Objetivo]] ($c_j$), el efecto directo y universal es que cambiará la pendiente o inclinación de la recta que la representa en el plano cartesiano.

> [!note] Ecuación Explícita de la Recta de Isoutilidad El profesor y la bibliografía demuestran esto despejando una de las variables principales (por ejemplo, $x_2$): $$ x_2 = \frac{Z}{c_2} - \frac{c_1}{c_2} x_1 $$ A partir de esta ecuación, se observa claramente que cualquier cambio en los coeficientes $c_j$ ($c_1$ o $c_2$) modificará obligatoriamente la pendiente de la recta (su inclinación).

## 2. Refutación de las Opciones Incorrectas

El enunciado incluye una frase clave: _"cualquiera sea la variable a la cual pertenece"_. Esta es la condición que invalida las opciones C y D.

|Opción Descartada|Análisis Teórico|
|:--|:--|
|**c. Se produce una nueva [[Solución Óptima]]**|**Falso.** Modificar la inclinación no altera obligatoriamente el vértice óptimo. Dependiendo de la magnitud del cambio, la nueva pendiente puede seguir contenida entre las restricciones limitantes, por lo que el vértice actual seguirá siendo óptimo.|
|**d. Se obtiene un nuevo valor para la [[Función Objetivo]]**|**Falso.** Esto no siempre ocurre y depende del tipo de variable. Si el coeficiente modificado pertenece a una [[Variable No Básica]] y el incremento no supera el límite del [[Intervalo de Sensibilidad]], **no se produce ningún cambio en la solución óptima ni en el valor de Z**. El valor de Z solo cambia ineludiblemente si se modifica el coeficiente de una [[Variable Básica]].|
|**b. Cambia la ordenada al origen de la función objetivo**|**Falso.** Como se observa en la fórmula de isoutilidad, si se modifica $c_1$, la ordenada al origen ($\frac{Z}{c_2}$) se mantiene inalterada, pero la inclinación de la recta ($- \frac{c_1}{c_2}$) sí cambia ineludiblemente.|

> [!danger] Trampa de Parcial: Generalización del Valor Z Es un error muy común creer que cualquier cambio en los costos o ganancias ($c_j$) repercute automáticamente en el número final de $Z$. Como advierte la teoría de post-optimidad, si el artículo que sufre la variación de mercado es un producto que actualmente **no fabricas** (una [[Variable No Básica]]), y esa variación no lo vuelve lo suficientemente rentable como para entrar a la base, el sistema ignora el cambio y tu ganancia total se mantiene intacta.

## 3. Diagrama de Impacto Paramétrico

```
graph TD
    A[Modificacion de un Coeficiente Cj] --> B[Efecto Geometrico Universal]
    B --> C[Cambia la pendiente o inclinacion de la recta Z]

    A --> D{A que variable pertenece el coeficiente?}
    D -->|Variable No Basica| E{Supera el Intervalo?}
    E -->|No| F[Z no se modifica]
    E -->|Si| G[Cambia la Base y cambia Z]

    D -->|Variable Basica| H{Supera el Intervalo?}
    H -->|No| I[La Base se mantiene pero Z cambia]
    H -->|Si| J[Cambia la Base y cambia Z]

    C -.-> K[La unica opcion siempre correcta es el cambio de inclinacion]
```

_Conceptos relacionados:_ [[Coeficientes de la Función Objetivo]], [[Análisis de Sensibilidad]], [[Variable Básica]], [[Variable No Básica]], [[Intervalo de Sensibilidad]], [[Función Objetivo]].
# 5)
![[Pasted image 20260607223537.png]]
Para una solución óptima no degenerada de un modelo de Max, si el coeficiente de la función objetivo de la variable no básica x1 aumenta en (exactamente) el incremento permisible

Pregunta 6 Seleccione una:

a.

La solución óptima previa permanece óptima

b.

Ninguna de las alternativas es correcta

c.

Habrá una nueva solución óptima con un valor óptimo mayor de x1

d.

Podría cambiar el valor de la función objetivo

e.

Cambia el valor de la función objetivo pero no la solución óptima
# RTA
La respuesta correcta a tu pregunta de examen es la **a. La solución óptima previa permanece óptima**.

A continuación, te desgloso la fundamentación teórica basándome en los principios del [[Análisis de Sensibilidad]] para una [[Variable No Básica]].

 esolución: Variación Exacta en el Límite Permisible de una [[Variable No Básica]]

## 1. Fundamento Teórico del Intervalo

De acuerdo a la teoría de post-optimidad de la cátedra, el [[Intervalo de Sensibilidad]] para una [[Variable No Básica]] define los posibles valores de su coeficiente ($c_j$) para los cuales esa variable sigue siendo no básica.

En un problema de [[Maximización]], la **[[Condición de Optimidad]]** exige que todas las diferencias marginales en la fila de evaluación sean menores o iguales a cero ($(C_j - Z_j) \le 0$).

Si el coeficiente de la variable no básica $x_1$ aumenta **exactamente** en su incremento permisible, su valor de $(C_1 - Z_1)$ crecerá desde un número negativo hasta llegar a ser **exactamente cero**.

> [!note] Cumplimiento de Optimidad Como el valor cero sigue satisfaciendo matemáticamente la regla de ser "menor o igual a cero", la matriz actual no se rompe. Por lo tanto, la base actual y la **[[Solución Óptima]]** previa permanecen inalteradas y válidas.

## 2. Refutación de las Opciones Incorrectas

|Opción|Análisis Teórico|
|:--|:--|
|**d. Podría cambiar el valor de la función objetivo** **e. Cambia el valor de la función objetivo...**|**Falso.** Al tratarse de una [[Variable No Básica]], su valor actual en el plan de producción es cero ($x_1 = 0$). Si le aumentas el coeficiente de ganancia a un producto que actualmente no fabricas, el valor total de tu [[Función Objetivo]] ($Z$) no sufre ninguna alteración matemática.|
|**c. Habrá una nueva solución óptima con un valor óptimo mayor de $x_1$**|**Técnicamente engañoso.** Al llegar exactamente al límite permisible ($(C_1 - Z_1) = 0$), se habilita matemáticamente la posibilidad de ingresar la variable a la base sin empeorar el valor de $Z$, creando un escenario de **[[Múltiples Soluciones Óptimas]]** (o solución alternativa). Sin embargo, la redacción "habrá una nueva" sugiere que la matriz cambiará automáticamente. En [[Programación Lineal]], el modelo rígido se queda en el vértice actual (la solución previa permanece óptima) a menos que el decisor fuerce manualmente una nueva iteración para pivotar hacia el vértice alternativo.|

> [!danger] Trampa de Parcial: El Límite Exacto Es un error común pensar que al tocar el límite exacto del intervalo de sensibilidad, la tabla se desestabiliza. La bibliografía es clara: la solución actual no sufre cambios si el incremento es **menor o igual** al límite superior. La palabra "igual" garantiza que en el límite exacto, la solución previa está a salvo.

## 3. Diagrama de Decisión del Límite Permisible

```
graph TD
    A[Aumento del Coeficiente C1 de Variable No Basica] --> B{¿Cual es la magnitud del aumento?}

    B -->|Supera el Incremento Permisible| C[El C1-Z1 se vuelve positivo > 0]
    C --> D[La solucion previa deja de ser optima y x1 debe entrar a la base]

    B -->|Es Exactamente Igual al Incremento Permisible| E[El C1-Z1 se vuelve exactamente 0]
    E --> F[Se sigue cumpliendo la Condicion de Optimidad Cj-Zj <= 0]
    F --> G[La Solucion Previa Permanece Optima]
    G -.-> H[Se origina la posibilidad de Multiples Soluciones Optimas si el decisor lo desea]
```

_Conceptos relacionados:_ [[Variable No Básica]], [[Condición de Optimidad]], [[Intervalo de Sensibilidad]], [[Múltiples Soluciones Óptimas]].
# 6)
![[Pasted image 20260607223625.png]]
Dada la solución óptima de un modelo de maximización de beneficios (no degenerado) y x1*= 0.El decisor quisiera saber: _“cuánto habrá que aumentar el beneficio de x1 para que convenga incluirla con un valor positivo en la solución óptima”_

¿En qué parte del informe que nos devuelven los software se encuentra la respuesta?

Pregunta 7 Seleccione una:

Ninguna de las otras respuestas es correcta

En los valores de las variables

En los cambios permisibles del VLD de la primera restricción

En el costo reducido

En el incremento permisible de x1

# RTA
Como tu Tutor Académico de Élite, he analizado tu consulta basándome en la teoría de post-optimidad y en la lectura de los reportes de software (como **[[LINDO]]** o **[[SOLVER]]**) enseñados por tu cátedra.

La respuesta correcta a tu pregunta de examen es: **En el costo reducido**. _(Nota: Numéricamente, el "incremento permisible" de una variable no básica coincide exactamente con su costo reducido, pero el concepto económico directo que responde a esta premisa es el costo reducido)._

A continuación, te desgloso detalladamente la justificación teórica y económica de esta respuesta para que asegures el concepto.

 Análisis de Post-Optimidad: Inclusión de Nuevos Productos

## 1. El Escenario del Problema

El enunciado plantea que estamos ante un modelo de **[[Maximización]]** y que la variable $x_1^* = 0$. Esto significa que $x_1$ es una **[[Variable No Básica]]**.

En términos económicos, la empresa decidió **no fabricar el producto $x_1$** porque no es rentable. Su contribución a las utilidades (el beneficio que aporta) es menor que el valor de los **[[Recursos Limitantes]]** que consume para fabricarse.

## 2. El Significado del [[Costo Reducido]]

En los reportes de software, el **[[Costo Reducido]]** (Reduced Cost) para una variable no básica representa el valor absoluto de la diferencia marginal $C_j - Z_j$ de la **[[Tabla Simplex]]** óptima.

> [!note] Definición Teórica El **[[Costo Reducido]]** indica exactamente la "penalización" o disminución que sufriría la **[[Función Objetivo]]** ($Z$) por cada unidad que se fuerce a producir de una variable que actualmente no es óptima.

Por lo tanto, respondiendo a la pregunta del decisor, el **[[Costo Reducido]]** nos dice de manera directa **la cantidad exacta en la que debe aumentar el beneficio (precio o utilidad) del producto para que deje de dar pérdidas** y se vuelva conveniente incluirlo en el plan de producción óptimo (es decir, para que ingrese a la base).

> [!danger] Trampa de Parcial: Costo Reducido vs. Incremento Permisible En la tabla de los reportes (como vimos en las salidas de LINDO de tu bibliografía), para una **[[Variable No Básica]]**, el valor numérico del **[[Costo Reducido]]** es _matemáticamente idéntico_ al valor del **[[Incremento Permisible]]** en la sección de rangos de los coeficientes objetivos. Sin embargo, la teoría clásica de Investigación Operativa reserva el término **[[Costo Reducido]]** o "Costo de Oportunidad" para responder a la pregunta de _"cuánto me falta para que sea rentable"_. Si en el examen ambas opciones están presentes y debes elegir la más representativa del análisis económico directo en la tabla de variables, es el Costo Reducido.

> [!tip] Tip de Interpretación del Profesor Recuerda lo que el profesor explicó en clase con el caso de los "acondicionadores de lujo": _"¿Qué consecuencias tendría si decide producir acondicionadores de lujo? La utilidad disminuye en 24... eso sale del costo reducido"_. Si el costo reducido es 24, significa que el producto debe aumentar su precio/beneficio en exactamente 24$ para que convenga empezar a fabricarlo.

## 3. Diagrama Lógico de Decisión

graph TD
    A[Variable No Basica x1 = 0] --> B{¿Por que no se fabrica?}
    B --> C[El beneficio que aporta es menor al valor de los recursos que consume]

    C --> D[Lectura del Software]
    D --> E(Columna: Costo Reducido)

    E --> F[Indica la penalizacion por forzar su produccion]
    F --> G[Es exactamente lo que le falta al Beneficio de x1 para empatar y ser rentable]

    G --> H[Respuesta al Decisor: Debe aumentar su beneficio en la magnitud del Costo Reducido]


_Conceptos relacionados:_ [[Variable No Básica]], [[Costo Reducido]], [[Función Objetivo]], [[Maximización]], [[Análisis de Sensibilidad]].
# 7)
![[Pasted image 20260607223706.png]]

Una relación correcta es:

Pregunta 8 Seleccione una:

a.

Si una restricción es limitante entonces el precio sombra debe ser positivo

b.

Si una restricción es no limitante entonces el precio sombra deber igual a cero

c.

Si una restricción es limitante entonces el precio sombra deber igual a cero

d.

Si una restricción es no limitante entonces el precio sombra debe ser positivo
# RTA
La respuesta correcta a tu pregunta de examen es la **b. Si una restricción es no limitante entonces el precio sombra debe ser igual a cero**.

A continuación, te explico el fundamento teórico basándome en los principios de la dualidad enseñados en tu cátedra.

### 1. El Fundamento: [[Teorema Débil de Holgura Complementaria]]

La relación exacta entre el uso de los recursos en un modelo y su valor económico marginal se explica mediante el **[[Teorema Débil de Holgura Complementaria]]**. Este teorema establece una relación matemática estricta y excluyente entre las variables del **[[Problema Primal]]** y las del **[[Problema Dual]]**.

> [!note] Enunciado Teórico del Teorema Si una restricción en uno de los problemas es con holgura (es decir, la variable de holgura es positiva), entonces la variable principal correspondiente en el otro problema debe ser obligatoriamente nula (cero).

> [!note] Ecuación Lógica de Holgura Complementaria $$ S_i \times Y_i = 0 $$ _(Donde $S_i$ es la holgura del primal e $Y_i$ es la variable dual o precio sombra. Si uno de los factores es mayor a cero, el otro debe ser rigurosamente cero)._

### 2. Análisis de una [[Restricción No Limitante]]

Una **[[Restricción No Limitante]]** es aquella que no determina el vértice óptimo, lo que significa que el recurso disponible no se agotó por completo.

- Al existir un recurso sobrante, su **[[Variable de Holgura]]** ($S_i$) asume un valor estrictamente positivo ($> 0$) en la solución óptima.
- Aplicando el teorema mencionado, como la holgura es positiva, su respectiva **[[Variable Dual]]** debe ser forzosamente nula ($0$).
- Dado que el valor numérico de la variable dual representa el **[[Precio Sombra]]** (o valor marginal del recurso), este también será cero.

> [!tip] Interpretación Económica Económicamente tiene todo el sentido lógico: si a tu empresa le sobra capacidad de un insumo (restricción no limitante), el costo de oportunidad de ese recurso es cero. No estarías dispuesto a pagar ni un centavo extra por conseguir una unidad adicional de algo que ya te está sobrando.

### 3. Refutación de las otras opciones

> [!danger] Trampa de Parcial: Restricciones Limitantes y Precios Positivos Es un error muy común y una trampa frecuente en evaluaciones marcar la opción _a. (Si una restricción es limitante entonces el precio sombra debe ser positivo)_. Si bien esto ocurre en la mayoría de los casos de estudio, matemáticamente es falso generalizar el "debe ser". Cuando te encuentras ante una **[[Solución Factible Básica Degenerada]]**, un recurso puede agotarse (su holgura es $= 0$) y su variable dual (precio sombra) también puede valer cero simultáneamente. Por lo tanto, un precio sombra no _siempre_ está obligado a ser positivo ante una restricción limitante.

### Resumen Comparativo

|Naturaleza de la Restricción|Uso del Recurso en la Realidad|**[[Variable de Holgura]]** ($S_i$)|Impacto en la **[[Variable Dual]]** o **[[Precio Sombra]]** ($Y_i$)|
|:--|:--|:--|:--|
|**[[Restricción No Limitante]]**|Hay recurso Sobrante|$S_i > 0$|**Debe ser estrictamente $Y_i = 0$**|
|**[[Restricción Limitante]]**|El recurso está Agotado|$S_i = 0$|Generalmente $Y_i > 0$, pero existe la posibilidad de que sea $0$ (Degeneración)|

### Esquema Lógico de Comprobación

```
graph TD
    A[Analisis de la Restriccion en el Optimo] --> B{¿Se agoto el recurso?}

    B -->|No| C[Es una Restriccion No Limitante]
    C --> D[La Variable de Holgura es Positiva > 0]
    D --> E[Por Teorema de Holgura Complementaria]
    E --> F[La Variable Dual asume valor 0]
    F --> G[El Precio Sombra es IGUAL A CERO]

    B -->|Si| H[Es una Restriccion Limitante]
    H --> I[La Variable de Holgura es 0]
    I --> J[El Precio Sombra puede ser Positivo o Cero]
```

_Conceptos relacionados:_ [[Restricción Limitante]], [[Restricción No Limitante]], [[Precio Sombra]], [[Teorema Débil de Holgura Complementaria]], [[Variable de Holgura]].
# 8)
![[Pasted image 20260607223812.png]]
Dado un problema de minimización, el valor de una variable dual (yi) representa:

Pregunta 9 Seleccione una:

a.

La mejora que se produce en el valor de la función Z ante un incremento en el bi.

b.

Ninguna respuesta es correcta

c.

El incremento que se produce en el valor de la función Z ante una disminución en el bi.

d.

El incremento que se produce en el valor de la función Z ante un incremento en el bi.

e.

La desmejora que se produce en el valor de la función Z ante una disminución en el bi.

# RTA
Como tu Tutor Académico de Élite, he analizado tu consulta basándome en la teoría oficial de la cátedra y en el énfasis que hizo el profesor durante las clases sobre la interpretación de los reportes de post-optimidad.

La respuesta correcta a tu pregunta de examen es la **d. El incremento que se produce en el valor de la función Z ante un incremento en el bi**.

A continuación, te desgloso el fundamento teórico para que no caigas en las trampas semánticas comunes de este tema.

 Análisis Teórico: Significado de la [[Variable Dual]]

## 1. El [[Significado Matemático]] Rígido

La cátedra hace una distinción muy estricta entre lo que representa matemáticamente la variable y su interpretación económica de mejora o desmejora.

Por definición teórica, la **[[Variable Dual]]** ($y_i$), también conocida en las salidas de software como **[[Precio Sombra]]**, tiene un significado matemático inalterable, independientemente de si el problema es de maximización o de minimización.

> [!note] Definición Teórica de la Variable Dual En el óptimo, la variable dual ($y_i$) representa la cantidad exacta en la que se **incrementa** la [[Función Objetivo]] ($Z$) ante un **incremento** unitario en el valor del [[Lado Derecho]] ($b_i$) de su restricción asociada.

El profesor fue muy enfático en clase respecto a esto: _"el significado matemático es el que me indica... que la variable dual representa la cantidad que incrementa la función zeta ante un incremento unitario en el valor del lado derecho... siempre recuerden que indica incremento"_.

## 2. Refutación de la Trampa de "Mejora / Desmejora"

El error más común en los exámenes es confundir la definición de la **[[Variable Dual]]** (o [[Precio Sombra]]) con la definición del **[[Precio Dual]]**.

> [!danger] Trampa de Parcial: Precio Sombra vs. Precio Dual
> 
> - La **[[Variable Dual]]** o **[[Precio Sombra]]** te habla de **incrementos matemáticos** directos. Si es positivo, $Z$ se incrementa. En un [[Problema de Minimización]], si $Z$ se incrementa, económicamente tu objetivo "desmejora" (porque te cuesta más caro).
> - El **[[Precio Dual]]**, en cambio, sí se define usando las palabras **mejora o desmejora**. El precio dual indica explícitamente la _mejora_ que se produce en la función objetivo al aumentar un recurso. En un problema de minimización, el Precio Dual es el opuesto (negativo) del Precio Sombra.

Por lo tanto:

- La opción **A** (La mejora que se produce...) es incorrecta porque en minimización un incremento en $Z$ es una desmejora, no una mejora. Además, definirlo en términos de "mejora" corresponde al concepto de [[Precio Dual]], no al de la variable dual pura.
- La opción **E** (La desmejora... ante una _disminución_ en el bi) también es incorrecta por invertir la dirección del cambio del recurso (la definición evalúa un _incremento_ en el $b_i$).

## 3. Esquema Lógico de Interpretación

```
graph TD
    A[Variable Dual yi / Precio Sombra] --> B[Significado Matematico Estricto]
    B --> C[Evalua un INCREMENTO en el Lado Derecho bi]
    C --> D[Provoca un INCREMENTO en la Funcion Objetivo Z]

    D --> E{Es Problema de Minimizacion?}
    E -->|Si| F[Ese incremento en Z significa que el objetivo desmejora]
    E -->|No Maximizacion| G[Ese incremento en Z significa que el objetivo mejora]

    F -.-> H[Pero la definicion de la variable yi sigue siendo puramente: Incremento de Z por Incremento de bi]
```

_Conceptos relacionados:_ [[Problema de Minimización]], [[Variable Dual]], [[Precio Sombra]], [[Precio Dual]], [[Lado Derecho]], [[Función Objetivo]].
# 9)
![[Pasted image 20260607223849.png]]
“Cuando se modifica el lado derecho de una restricción, cambia su pendiente.”

Pregunta 10 Seleccione una:

Verdadero

Falso

# RTA
La respuesta correcta a tu pregunta de examen es **Falso**.

A continuación, te explico la fundamentación teórica y matemática de por qué esta afirmación es incorrecta, basándome en los principios gráficos del análisis de post-optimidad dictados por la cátedra.

### 1. Fundamento Geométrico del [[Lado Derecho]]

Cuando se modifica el valor del **[[Lado Derecho]]** ($b_i$) de una **[[Restricción]]**, el efecto gráfico no es un cambio de inclinación, sino un **desplazamiento paralelo** de la recta representativa.

La teoría establece estrictamente que el cambio en un $b_i$ tiene como único efecto geométrico **expandir o contraer la [[Región Factible]]** (o poliedro de soluciones).

> [!note] Ecuación Explícita de la Restricción Si tomamos una inecuación genérica $a_1x_1 + a_2x_2 \le b_i$ y despejamos $x_2$ para graficarla como recta, obteneuos: $$ x_2 = \frac{b_i}{a_2} - \frac{a_1}{a_2}x_1 $$ Como se puede observar, el parámetro $b_i$ solo divide al término independiente (modificando la ordenada al origen), pero **no afecta en absoluto a la pendiente** ($- \frac{a_1}{a_2}$), la cual depende exclusivamente de los coeficientes tecnológicos.

### 2. Contraste Paramétrico: ¿Qué cambia la pendiente?

> [!danger] Trampa Conceptual Es un error frecuente confundir los efectos visuales de los parámetros. **Lo único que cambia la pendiente** o inclinación de una recta en un modelo de Programación Lineal es la modificación de los coeficientes que acompañan a las variables.
> 
> - Si cambia un **Coeficiente de la Función Objetivo ($c_j$)**, cambia la pendiente de la recta $Z$.
> - Si cambia un **Coeficiente Tecnológico ($a_{ij}$)**, cambia la pendiente de la restricción.

### Esquema Visual de Impacto

```
graph TD
    A[Modificacion de Parámetros] --> B{¿Qué parámetro se modificó?}

    B -->|Lado Derecho bi| C[Afecta la ordenada al origen]
    C --> D[Desplazamiento Paralelo de la Recta]
    D --> E[Expande o Contrae la Región Factible]

    B -->|Coeficientes cj o aij| F[Afecta el factor multiplicador de la variable]
    F --> G[Cambia la Pendiente o Inclinación]
```

_Conceptos relacionados:_ [[Lado Derecho]], [[Restricción]], [[Región Factible]], [[Análisis de Sensibilidad]].
# 10)
![[Pasted image 20260607223923.png]]
“El precio sombra es la tasa de cambio de la función objetivo a medida que aumenta el VLD”

Pregunta 11 Seleccione una:

Verdadero

Falso

# RTA
La respuesta correcta a tu pregunta de examen es **Verdadero**.

A continuación, te desgloso la fundamentación teórica y analítica de esta afirmación basándome en los textos y clases de tu cátedra.

### Fundamento Teórico: El Significado del [[Precio Sombra]]

El enunciado es estrictamente correcto porque define con precisión el **[[Significado Matemático]]** de la **[[Variable Dual]]** (que en los reportes de software asume el nombre de **[[Precio Sombra]]**).

> [!note] Definición Matemática Exacta En el óptimo, el [[Precio Sombra]] o variable dual ($y_i$) representa la variación o cantidad exacta en la que se incrementa el valor de la **[[Función Objetivo]]** ($Z$) ante un incremento unitario en el **[[Valor del Lado Derecho]]** ($VLD$ o $b_i$) de su restricción asociada.
> 
> Matemáticamente, esta "tasa de cambio" equivale a la derivada parcial de la función respecto al recurso: $$ \frac{\partial Z^*}{\partial b_i} = y_i^* $$

### Interpretación Económica Práctica

Como el profesor explicó en clase, esta tasa de cambio es clave para el **[[Análisis de Sensibilidad]]**. Te indica cuál es la "valoración interna" que tiene un recurso para la empresa:

- Si el [[Precio Sombra]] es positivo, significa que por cada unidad adicional que consigas de ese $VLD$, tu [[Función Objetivo]] va a crecer exactamente en esa proporción.
- Esta tasa de cambio se mantiene constante y válida siempre y cuando la modificación del recurso no exceda los límites impuestos por su respectivo **[[Intervalo de Sensibilidad]]**.

```
graph TD
    A[Aumento en el VLD bi] --> B[Genera un impacto en el sistema]
    B --> C[Cambio marginal en la Funcion Objetivo Z]
    C -.-> D[Esta tasa de cambio exacta esta medida por el Precio Sombra]
```

_Conceptos relacionados:_ [[Precio Sombra]], [[Variable Dual]], [[Función Objetivo]], [[Valor del Lado Derecho]], [[Análisis de Sensibilidad]].