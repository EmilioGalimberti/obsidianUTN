# B) Resuelva gráficamente.
![[{B936B44D-7653-4008-9513-6456C104B5F7}.png]]![[{E7D7F83D-56FA-40F6-82EE-BB8676AEE328}.png]]
La profesora pausa la exposición para que los alumnos resuelvan el caso "Fruits SA" en el Aula Virtual (UV). Al regresar, se analizan los fallos.

- **El Error de la Pendiente:** Varios alumnos eligieron un vértice equivocado. La profesora detectó que dibujaron mal la inclinación de la recta Z. _"El óptimo depende de la inclinación de la recta Z... por eso hay que prestar atención al dibujarla"_.
- **Cálculos Posteriores (Salidas):** Se recordó que si el problema pide "litros de concentrado producidos", no basta con el valor de la variable (que era "litros de pulpa ingresada"), sino que hay que aplicar la tasa de transformación (merma).

# pregs uv
## ¿Cuál gráfico corresponde al conjunto solución del problema de _Fruits SA?_
![[Pasted image 20260624182039.png]]
### rta
![[Pasted image 20260624182050.png]]

## Qué valores asumen las variables en la solución óptima? ¿A cuánto asciende su beneficio total? 

x1=
x2=
z*=
### rta

¡Excelente desafío! Como tu Tutor Académico de Élite, he analizado el planteo del caso "Fruits SA" tal como fue discutido y corregido por el profesor durante la clase práctica mediante el uso de software y resolución algebraica.

A continuación, te presento la disección de la modelización y la resolución exacta para que no solo copies los valores, sino que domines el procedimiento algebraico de este modelo de [[Programación Lineal]].

 🎯 MODELIZACIÓN Y RESOLUCIÓN ALGEBRAICA: CASO FRUITS SA

```
graph LR
    A(Análisis de Datos) --> B(Cálculo de Parámetros de Contribución)
    B --> C(Planteo de Restricciones Estructurales)
    C --> D(Resolución del Sistema de Ecuaciones)
    D --> E(Identificación del Vértice Óptimo)
```

#### 1. Definición del Modelo Matemático

Para no cometer errores en la formulación, debemos definir correctamente las [[Variables de Decisión]] con sus unidades exactas:

- $x_1$: Litros de pulpa de arándanos a procesar semanalmente.
- $x_2$: Litros de pulpa de frambuesas a procesar semanalmente.

> [!note] Cálculo Oculto de la Función Objetivo ($Z$) El beneficio por cada litro de pulpa procesada requiere un cálculo previo, ya que hay pérdida de agua durante la destilación. El profesor exige que la [[Función Objetivo]] refleje la ganancia neta ([[Parámetros de Contribución]]):
> 
> - **Arándanos ($c_1$):** Venta $$50 \times 0.65$ (rinde) $- $12$ (costo) = **$$20.50$**
> - **Frambuesas ($c_2$):** Venta $$45 \times 0.75$ (rinde) $- $15$ (costo) = **$$18.75$**

Por lo tanto, buscamos maximizar: $$ \max Z = 20.5 x_1 + 18.75 x_2 $$

#### 2. Sistema de Inecuaciones ([[Restricciones Funcionales]])

1. **Tanque Arándanos (Concentrado):** $0.65x_1 \leq 650$
2. **Tanque Frambuesas (Concentrado):** $0.75x_2 \leq 650$
3. **Horas Máquina Destiladora:** $\frac{1}{60}x_1 + \frac{1}{50}x_2 \leq 30$

> [!danger] Trampa de Parcial: Las Tasas de Producción Muchos alumnos se confunden al armar la restricción de tiempo. Si la máquina procesa $60$ litros por hora, entonces consume $\frac{1}{60}$ de hora por cada litro procesado. Ese es el coeficiente técnico correcto a utilizar en el lado izquierdo de la inecuación.

#### 3. Resolución del [[Vértice Óptimo]]

De acuerdo con el desarrollo en clase, el punto que maximiza $Z$ es la intersección entre la restricción de almacenamiento de arándanos y la capacidad de horas de máquina. Ambas operan como una [[Restricción Limitante]].

> [!tip] Metodología de Resolución (Sistema de Ecuaciones) **Paso 1:** Despejamos la restricción 1 como igualdad: $$0.65 x_1 = 650 \implies x_1 = 1000$$
> 
> **Paso 2:** Reemplazamos $x_1$ en la ecuación de la máquina destiladora: $$ \frac{1000}{60} + \frac{x_2}{50} = 30 $$ $$ 16.6667 + 0.02 x_2 = 30 $$ $$ 0.02 x_2 = 13.3333 \implies x_2 = 666.6666... $$
> 
> **Paso 3:** Reemplazamos los valores óptimos en la [[Función Objetivo]]: $$ Z = 20.5 (1000) + 18.75 (666.666...) = 20500 + 12500 = 33000 $$

---

#### 📋 RESPUESTAS FORMATEADAS PARA EL CUESTIONARIO

A continuación tienes los valores listos para ser copiados y pegados según las estrictas reglas de formato indicadas (solo números, con 3 decimales separados por coma):

**x1 =** 1000,000

**x2 =** 666,667

__Z_ =_* 33000,000





## Cuántos litros de concentrado de arándanos se producen? ¿Cuántos litros de concentrado de frambuesa se producen?   
### rta
**Respuesta 1 Pregunta 4** 650

**Respuesta 2 Pregunta 4** 500

---

> [!tip] Justificación Analítica (Tutor de Élite) Recuerda que las variables $x_1$ y $x_2$ representan los **litros de pulpa** que ingresan a la máquina, no el producto final. Como advirtió la profesora en clase, para calcular el concentrado producido debes aplicarle la tasa de rendimiento (lo que queda después de la evaporación del agua durante la destilación):
> 
> - **Arándanos:** Ingresan $1000$ litros de pulpa. Pierde el $35%$ de agua, por lo tanto rinde el $65%$. Cálculo: $1000 \times 0.65 = 650$ litros de concentrado. (Nota: Esto agota exactamente la capacidad del tanque de 650 lts, confirmando que es una [[Restricción Limitante]]).
> - **Frambuesas:** Ingresan $666.666...$ litros de pulpa. Pierde el $25$ de agua, por lo tanto rinde el $75$. Cálculo: $666.666... \times 0.75 = 500$ litros de concentrado.

## ¿Se están usando todas las horas de la destiladora?
- [ ] No
- [ ] No es posible saberlo con la solución gráfica.
- [ ] Sí
### rta
**Pregunta 5 Respuesta** **Sí**

---

#### 🗣️ CÓMO JUSTIFICAR (El "Por qué" Analítico)

Como tu Tutor Académico de Élite, te explico que no basta con adivinar la respuesta; el profesor evaluará que comprendas la dinámica estructural del [[Método Gráfico]]. La respuesta es afirmativa por dos razones fundamentales (una visual y otra algebraica):

> [!tip] Justificación Gráfica Según lo explicado en clase, cuando el [[Vértice Óptimo]] se encuentra apoyado exactamente sobre la recta trazada para una restricción específica (en este caso, la recta de la máquina destiladora), significa que visualmente hemos alcanzado el límite exacto de esa frontera. Por lo tanto, el recurso se consume en su totalidad.

> [!note] Justificación Algebraica (Teoría Oficial) En la teoría de la [[Programación Lineal]], las ecuaciones que determinan el óptimo al cruzarse se denominan **[[Restricciones Limitantes]]**. En estas restricciones el uso del recurso es exactamente igual a la disponibilidad total ($30$ horas usadas $=$ $30$ horas disponibles). Matemáticamente, esto significa que la **[[Variable de Holgura]]** asociada a la máquina destiladora es exactamente nula ($S_i = 0$).

Para que lo visualices algorítmicamente en tu examen, la lógica de consumo de este recurso sigue este flujo:

```
graph TD
    A(Evaluar Vértice Óptimo) --> B{¿El punto toca la recta de la restricción?}
    B -->|Sí| C(Es una Restricción Limitante)
    C --> D(Consumo Total = Uso Máximo)
    D --> E(Variable de Holgura = 0)
    B -->|No| F(Es una Restricción No Limitante)
    F --> G(Queda Capacidad Ociosa)
    G --> H(Variable de Holgura > 0)
```

_Conceptos relacionados:_ [[Vértice Óptimo]], [[Restricción Limitante]], [[Variable de Holgura]].

Si quisieras hacer la validación numérica en un parcial para estar $100$ seguro, simplemente debes reemplazar la [[Solución Óptima]] que calculamos en la inecuación de las horas de máquina: $$ \frac{1}{60} (1000) + \frac{1}{50} (666.667) \leq 30 $$ $$ 16.666 + 13.333 = 30 $$ $$ 30 = 30 \implies \text{Holgura nula (Se usaron todas las horas)} $$

## ¿Los tanques de almacenamiento están usados en su capacidad máxima? 

- [ ] a.No es posible saber con la solución gráfica
- [ ] b.Solo uno de ellos está usado en su capacidad máxima
- [ ] c.Los dos están usados en su capacidad máxima
- [ ] d.Ninguno de los dos está usado en su capacidad máxima
### rta
**Pregunta 6 Respuesta** **b. Solo uno de ellos está usado en su capacidad máxima**

---
#### 🗣️ CÓMO JUSTIFICAR (El "Por qué" Analítico)

Como tu Tutor Académico de Élite, te explico la mecánica exacta detrás de esta respuesta, vinculándola directamente con los cálculos de concentrado que hicimos en la pregunta anterior y con lo que el profesor remarcó en clase sobre las "variables implícitas".

Para saber si los recursos están agotados, debemos comparar el "Uso Real" contra la "Disponibilidad" evaluando la [[Variable de Holgura]] de cada restricción de almacenamiento:

> [!note] Evaluación Analítica de los Tanques (Capacidad: 650 Lts cada uno)
> 
> **1. Tanque de Arándanos:**
> 
> - **Uso:** Producimos exactamente $650$ litros de concentrado ($1000 \times 0.65$).
> - **Situación:** $650 = 650$. El recurso se consumió en su totalidad.
> - **Concepto Teórico:** Esta es una **[[Restricción Limitante]]**. Su variable de holgura es exactamente $0$.
> 
> **2. Tanque de Frambuesas:**
> 
> - **Uso:** Producimos solo $500$ litros de concentrado ($666.667 \times 0.75$).
> - **Situación:** $500 \leq 650$. Queda capacidad ociosa en el tanque.
> - **Concepto Teórico:** Esta es una **Restricción No Limitante**. Posee una [[Variable de Holgura]] ociosa de $150$ litros.

> [!tip] Tip de Trinchera: El Guiño del Profesor Durante la corrección de este ejercicio en clase, el profesor utilizó justamente esta pregunta como disparador para enseñar el concepto de variables implícitas. Él mencionó literalmente: _"había un tanque que no se usaba completamente, entonces estaba implícita esa capacidad no utilizada... es la variable de holgura"_. Solo el tanque de frambuesas generó esa holgura.

## ¿Crees que existen variables implícitas en el modelo?
a.

No

b.

Imposible saberlo con los datos disponibles

c.

Sí
### rta
**Pregunta 7 Respuesta** **c. Sí**

---

#### 🗣️ CÓMO JUSTIFICAR (El "Por qué" Analítico)

Como tu Tutor Académico de Élite, te confirmo que la respuesta es afirmativa y te explico exactamente cómo el profesor justificó este concepto trampa durante la revisión del cuestionario.

> [!note] Definición del Profesor: Variables Implícitas En un modelo original formulado con inecuaciones, las **[[Variables Implícitas]]** son exactamente las [[Variables de Holgura]] y las [[Variables de Excedente]]. Aunque no se dibujen directamente en los ejes del gráfico, "están implícitas" en la restricción matemática que indica que el uso de un recurso puede ser menor (o el requerimiento mayor) a la disponibilidad total.

Para justificarlo sólidamente en tu examen, debes estructurar el análisis así:

- **La Formulación Original:** Nuestro modelo de _Fruits SA_ tiene dos [[Variables de Decisión]] ($x_1, x_2$) y está sujeto a tres restricciones del tipo "menor o igual" ($\leq$) referidas a la capacidad de los tanques y de la máquina destiladora.
- **La Estandarización:** Para convertir este modelo a su [[Forma Estándar]] y transformarlo en un sistema de ecuaciones resoluble, es algebraicamente obligatorio hacer explícitas estas variables sumando una [[Variable de Holgura]] ($+S_i$) por cada restricción.
- **El Resultado:** Por lo tanto, en este modelo existen **3 variables implícitas** (una por cada restricción). Representan físicamente la capacidad ociosa (vacía) de los dos tanques de enfriamiento y las horas no utilizadas de la destiladora.

> [!tip] Tip de Trinchera (El "Guiño" del Cuestionario) El profesor aclaró expresamente que incluyó esta pregunta no para evaluar un cálculo, sino como un "disparador" teórico. Quería evidenciar que los alumnos suelen olvidar que, en el fondo, un modelo gráfico de dos variables en realidad opera con muchas más variables ocultas ($n=5$ en este caso: $x_1, x_2, S_1, S_2, S_3$), las cuales son fundamentales para calcular el límite combinatorio de soluciones.

## Si respondiste que existen variables implícitas ¿Cuántas son y cómo las definiría?

En el caso de _Fruits SA_, existen exactamente **3 [[Variables Implícitas]]**.

A continuación, te explico detalladamente cómo el profesor exige que las definas y conceptualices para demostrar un dominio absoluto del modelo matemático.

### 🎯 DEFINICIÓN Y CUANTIFICACIÓN DE VARIABLES IMPLÍCITAS

Las [[Variables Implícitas]] en este modelo de [[Programación Lineal]] son las **[[Variables de Holgura]]**. Se denominan "implícitas" porque, aunque no se grafican directamente en los ejes cartesianos (donde solo vemos las [[Variables de Decisión]] $x_1$ y $x_2$), existen algebraicamente y son fundamentales para que el algoritmo pueda operar.

> [!note] Definición Literal del Profesor Una [[Variable de Holgura]] se define como la diferencia exacta entre el lado izquierdo (el uso real del recurso) y el lado derecho (la disponibilidad total) de una [[Restricción]]. Representa físicamente la capacidad ociosa, es decir, la parte del recurso que tenías disponible y no utilizaste.

#### 1. Mapeo Físico y Matemático de las 3 Variables

Como el problema tiene tres [[Restricciones Funcionales]] del tipo menor o igual ($\leq$), al transformar el modelo a su [[Forma Estándar]] es obligatorio sumar una variable por cada limitación.

Así se definen específicamente para el caso _Fruits SA_:

- **$S_1$ (Holgura del Tanque 1):** Representa los litros de capacidad ociosa (espacio vacío) en el tanque de enfriamiento de arándanos.
- **$S_2$ (Holgura del Tanque 2):** Representa los litros de capacidad ociosa (espacio vacío) en el tanque de enfriamiento de frambuesas.
- **$S_3$ (Holgura de la Destiladora):** Representa las horas semanales no utilizadas (tiempo ocioso) de la máquina destiladora.

> [!note] Ecuación de Estandarización (Ejemplo Tanque Arándanos) Para visualizar cómo la variable implícita absorbe la diferencia, la inecuación original $0.65x_1 \leq 650$ se convierte en la siguiente ecuación: $$ 0.65x_1 + S_1 = 650 $$

#### 2. Flujo Lógico de Identificación

```
graph TD
    A(Modelo Original con Inecuaciones) --> B(Lectura de Restricciones)
    B --> C{Tipo de Restricción}
    C -->|Menor o igual| D(Capacidad sobrante)
    D --> E(Se SUMA una Variable de Holgura S)
    E --> F(La variable representa Recurso No Utilizado)
    F --> G(Pasa a ser parte del Modelo en Forma Estandar)
```

_Conceptos relacionados:_ [[Forma Estándar]], [[Restricciones Funcionales]], [[Variables de Holgura]].

#### 3. Dudas de Clase y Criterios de Corrección

Durante la corrección del práctico, un alumno hizo una pregunta clave que el profesor utilizó para asentar este concepto:

> [!question] Pregunta de Clase _Alumno: "Profe, entonces variables implícitas tenemos una, ¿no?"_ _Profesor:_ "En realidad tienes **una por cada restricción**. Las variables implícitas aparecen cuando vos transformas el problema... a su [[Forma Estándar]], o sea le agregas las variables de holgura o excedente que sean necesarias... entonces tenés 3, una por cada restricción."

> [!danger] Trampa Teórica: La Función Objetivo Muchos alumnos se confunden al definir estas variables y creen que alteran el beneficio. El profesor aclaró que, al definir el modelo completo, estas variables ingresan a la [[Función Objetivo]] con un coeficiente de **cero** ($+0S_1 +0S_2 +0S_3$), ya que la capacidad ociosa (como un tanque a medio llenar) no aporta ninguna ganancia económica a la empresa.

> [!tip] Tip de Parcial (Tipificación Inversa) Si en el examen te preguntan por el valor de estas variables y sabes de antemano que una restricción es una **[[Restricción Limitante]]** (como ocurrió con las horas de máquina en este caso), puedes definir matemáticamente y sin calcular que su [[Variable de Holgura]] es exactamente $0$, ya que el recurso se consumió en su totalidad.