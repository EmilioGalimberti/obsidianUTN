## 2. Fase 2: Construcción del Gráfico y Restricciones (5:00 - 16:00)
[[✅PROBLEMA 2.10 GRAFICO]]

A)
Se detalla el paso a paso para delimitar el área de trabajo válida.

- **Restricción de No Negatividad:** Circunscribe el gráfico exclusivamente al primer cuadrante, ya que las [[Variables de Decisión]] deben ser $\geq 0$.
- **Trazado de Inecuaciones:** Se grafica cada [[Restricción]] asumiéndola temporalmente como una igualdad para encontrar las intersecciones con los ejes (anulando $x_1$ y luego $x_2$).
![[{F773EC83-2B75-4876-AD1B-BAC136BF4367}.png|131]]
![[{CF106BC1-02C3-4FC6-9487-0EB23F54BEFA}.png]]
![[{A3CE7E52-93D0-4FEE-90D0-FF9FFAD0AF77}.png|355]]

- **Identificación de Semiplanos:** Se utiliza un "punto de prueba" (frecuentemente el origen $(0,0)$ o un punto como $(2,2)$) para verificar hacia qué lado de la recta se cumple la inecuación original.
![[{1FC13917-F35F-410E-B4C1-489823CD5276}.png]]

lo mismo con el resto de las restricciones ....

- **Intersección:** La superposición de todos los semiplanos válidos genera la [[Región Factible]] o [[Poliedro de Soluciones]].
- ![[{85194BD9-B641-4436-AFBD-B2A57BB7FC41}.png]]
![[{A429859E-EFF9-4C0A-BE1D-DBE56D0DCE2A}.png]]
---


> [!question] Pregunta Frecuente en Clase _¿El poliedro de soluciones factibles puede ser un conjunto cóncavo o tener áreas separadas?_ Falso. El profesor aclaró que la región común de soluciones siempre debe ser un [[Polígono Convexo]]. Si tomas dos puntos cualesquiera dentro del área, la línea que los une debe estar completamente dentro de ese polígono.

## 3. Fase 3: Análisis de Soluciones y Teorema Combinatorio (16:00 - 24:00)
B y c)

El segundo bloque se centró en la teoría detrás de los puntos de intersección del gráfico y cómo predecir su cantidad máxima sin necesidad de graficar.

> [!note] Fórmula del Número Máximo de Soluciones Básicas $$ C = \frac{n!}{m!(n-m)!} $$ _(Donde $n$ es el número total de variables, incluyendo las de holgura, y $m$ es el número de restricciones no se incluye la de no negativadad)_.


|Tipo de Solución|Ubicación Gráfica|Característica Principal|
|:--|:--|:--|
|**[[Soluciones Básicas]]**|Todas las intersecciones de rectas (incluyendo ejes).|No todas respetan la no negatividad. En el ejemplo: 10 soluciones.|
|**[[Soluciones Posibles Básicas]]**|Exclusivamente en los vértices del [[Poliedro de Soluciones]].|Verifican todas las restricciones simultáneamente. En el ejemplo: Solo 4 soluciones.|

en nuestro ejemplo n=5 y m=3
$$C = \frac{5!}{2!(5-2)!}=10$$ en la calculadora x! es el factorial

SOLUCIONES BASICAS: (10)
![[{C7D56DCC-18FA-4EDC-BC29-575F3A7166F3}.png]]

SOLUCIONES POSIBLES BASICAS (4) -> SUBCONJUNTO DE SOLUCIONES BASICAS
![[{11AC18B2-5039-490E-84AC-7C4A5E5A47DC}.png]]

---
### ANALISIS DE SOLUCIONES
![[{51C6D5E7-326A-43CF-AE43-54573A10AF6A}.png]]

## 4. Fase 4: Optimización y Resolución Algebraica (24:00 - 40:00)
G)
Una vez graficadas las restricciones, el profesor explicó cómo encontrar el punto óptimo. La clave es asignarle a la [[Función Objetivo]] ($Z$) un valor arbitrario (ej: $Z=12$ o $Z=0$) para poder trazar su pendiente en el plano.
![[{06330AED-B83B-4352-BA2E-45A1B4797DA3}.png]]
![[{E28E9558-7348-47DB-93B2-AB47FC3AD20B}.png|258]]

- **Desplazamiento:** Al ser un caso de [[Maximización]], la recta se desplaza paralelamente **alejándose del origen** hasta tocar el último vértice del polígono de soluciones.
	- **En [[Minimización]]:** La recta se desplaza en sentido contrario, **acercándose hacia la izquierda/origen**, buscando el punto de contacto de menor valor.

![[{7BD96D93-C8B2-41D1-AF97-048577817E39}.png]]

- **Cálculo Exacto:** Una vez identificado visualmente el vértice óptimo, se debe resolver el sistema de ecuaciones de las dos rectas que se cruzan en ese punto mediante métodos algebraicos (Igualación, Sustitución o Cramer).
![[{B394858B-DEC0-4B6D-A8C8-957D9ADC8758}.png]]
![[{64E83311-1B98-4DEE-9A7D-7CFCBB416596}.png]]
> [!danger] Trampa de Parcial: El cálculo "a ojo" El profesor fue tajante: NUNCA se deben estimar los valores de las variables "a ojo" mirando la escala del gráfico. Una vez identificado el vértice óptimo visualmente, debes usar el [[Método de Igualación]] o el [[Método de Sustitución]] con el sistema de ecuaciones de las dos rectas que se cruzan para hallar el valor algebraico exacto.


El último tema crucial fue cómo introducir las variables adicionales para convertir el modelo gráfico (inecuaciones) en un modelo estandarizado (ecuaciones), que es la base para el futuro [[Método Simplex]].

- En inecuaciones $\leq$: Se suma una [[Variable de Holgura]] ($+S_i$) para igualar el recurso consumido con el disponible.
- En inecuaciones $\geq$: Se resta una [[Variable de Excedente]] ($-S_i$) para quitar el exceso sobre el requisito mínimo.

> [!danger] Error Crítico de Examen: Confusión de Signos Las variables NUNCA pueden ser negativas. Una violación a la [[Restricción de No Negatividad]] anula directamente el examen. El profesor aclaró que la [[Variable de Excedente]] en sí misma siempre es $\geq 0$. El signo "menos" en la ecuación es meramente una _operación algebraica_ del modelo para restar esa cantidad positiva.

### solucion

Y POR ultimo para hallar el vector solucion nos falta encontrar el valor de las variables de holgura

para encontrarlo remplazamos x1,x2 en las ecucaiones
![[{BAF2977A-7BF2-4D0C-B5EA-D083D4303A44}.png]]

![[{67B40F9E-92EB-44B2-9F3C-9DB97A6C8A0B}.png]]
## 5. Fase 5: Revisión de Cuestionario y Minimización (40:00 - 53:00)
![[{97B4AA82-72C3-4986-9ED5-4361DE8BDFC2}.png]]
Se repasa un ejercicio de parcial/cuestionario enfocado en [[Minimización]], destacando los errores comunes de los alumnos.

![[{39EB821F-EEF7-459C-B4D2-884CFB1646A7}.png]]
RTA: F
- **Lectura de Semiplanos:** Se alerta sobre el error de asumir que una restricción $\geq$ siempre "va para arriba". Depende de la pendiente, y siempre debe comprobarse con un punto de prueba.


> [!question] Pregunta de Clase _¿El poliedro de soluciones factibles puede ser un conjunto cóncavo con áreas separadas?_ 
> 
> Falso. El profesor aclara que siempre debe ser un [[Polígono Convexo]]. Si tomas dos puntos cualesquiera dentro del área, la línea que los une debe estar completamente dentro del polígono. Si hay áreas "separadas", el problema no tiene solución.


cual es el numer maximo de soluciones basicas que puede tener este problema?
rta: 10

identifique el vertice optimo:![[{FD718F9B-91A6-4F89-96EF-6530AB78C268}.png|347]]
rta G

- **Peculiaridades de Minimizar:** La [[Función Objetivo]] se desplaza hacia la izquierda (hacia el origen) buscando el primer punto de contacto con el poliedro.

El valor de la funcio objetivo en el punto optimo?
rta: 109

valor de las variables?
rta [x1=10 ; x2=3 ; s1=0 ;s2=96 ;s3=0 ]


cuales eran restricciones limitantes en el punto optimo?
rta: la 1 y la 3![[{9A34DFF9-93B5-4B93-AC60-3D0BEABA2D22}.png]]


> [!danger] ZONA DE PELIGRO ABSOLUTA: Variables Negativas Durante la corrección del cuestionario, el profesor advierte sobre un error que **anula directamente el examen**: declarar valores negativos para las variables (sean de decisión o de holgura). Violar la condición de no negatividad es un error conceptual crítico.

## 6. Fase 6: Software y Aclaraciones Estructurales (53:00 - Fin)

- **Demostración Tecnológica:** El profesor muestra la interfaz de [[PHP Simplex]] para verificar gráficamente los resultados y observar la tabla de iteraciones de vértices.
- **Signos de Variables Auxiliares:** Cierre magistral sobre la estandarización de inecuaciones:
    - En $\leq$: Se SUMA una [[Variable de Holgura]] para llegar a la igualdad.
    - En $\geq$: Se RESTA una [[Variable de Excedente]] para bajar hasta el requerimiento mínimo.
    - **Importante:** En todos los casos, la variable matemática en sí misma siempre es exigida como $\geq 0$ por definición, el signo menos es una operación algebraica del modelo, no un valor negativo de la variable.



---


# ----
Aquí tienes el análisis estratégico de la clase práctica. He rastreado las advertencias directas del profesor sobre los criterios de corrección de exámenes y he sistematizado las dudas conceptuales que plantearon tus compañeros, ya que representan los "puntos de dolor" más comunes al estudiar este tema.

# 🚨 ANÁLISIS ESTRATÉGICO: ÉNFASIS DEL PROFESOR Y DUDAS DE CLASE

## 1. Marcadores de Importancia y Criterios de Examen

El profesor hizo un fuerte énfasis en advertir sobre errores críticos que cometen los alumnos durante las evaluaciones prácticas del [[Método Gráfico]]. Debes prestar especial atención a estos tres puntos:

> [!danger] TRAMPA MORTAL DE EXAMEN: Variables Negativas El profesor advirtió explícitamente que asignar valores negativos a las variables (sean de decisión o auxiliares) es un **error grave que "anula el examen directamente"**. Violar la [[Restricción de No Negatividad]] demuestra una incomprensión total del modelo matemático.

> [!danger] TRAMPA DE PARCIAL: Cálculo de Vértices "A Ojo" Cuando se le preguntó a la clase cómo despejaban los valores de los vértices, el profesor recalcó que **NUNCA** deben determinarse leyendo visualmente las coordenadas en el gráfico ("a ojo"). Una escala imprecisa te llevará a resultados incorrectos; siempre debes usar un [[Sistema de Ecuaciones]] mediante igualación, sustitución o Cramer.

> [!tip] CONSEJO LOGÍSTICO: El Uso del Papel vs. Software Aunque existen herramientas informáticas como el [[PHP Simplex]] (que el profesor demostró al final de la clase), insistió en que los primeros ejercicios deben resolverse obligatoriamente **a mano y en papel**. Esta es la única manera de tomar verdadera dimensión de las particularidades del trazado y encontrar los valores correctamente.

---

## 2. Preguntas Relevantes de los Alumnos y Respuestas del Profesor

Durante la clase, los alumnos plantearon dudas fundamentales que el profesor aprovechó para asentar conceptos teóricos clave:

### A. Duda sobre el Teorema Combinatorio

> [!question] Pregunta del Alumno: _Al calcular el número máximo de [[Soluciones Básicas]] con la fórmula combinatoria $C = \frac{n!}{m!(n-m)!}$, ¿el valor $n$ se refiere solo a las dos variables principales ($x_1, x_2$)?_

**Respuesta del Profesor:** NO. El valor $n$ debe incluir tanto las [[Variables de Decisión]] como las variables auxiliares implícitas. En el problema analizado, $n=5$ porque se suman las dos variables principales más tres [[Variables de Holgura]] (una por cada restricción).

### B. Duda sobre el Trazado de Semiplanos

> [!question] Pregunta del Alumno: _Un alumno confesó haber marcado mal la [[Región Factible]] porque asumió que, al ser una restricción de "mayor o igual" ($\geq$), los valores válidos debían ir "para arriba" en el gráfico._

**Respuesta del Profesor:** El profesor corrigió este sesgo visual. Aclaró que la inclinación de la recta puede ser engañosa y **no se debe asumir la dirección del semiplano solo por el símbolo**. La metodología obligatoria es tomar un "punto de prueba" (como el $(0,0)$ o el $(3,3)$), reemplazarlo en la inecuación original y verificar si la afirmación es verdadera o falsa.

### C. Duda sobre la Continuidad de la Región Factible

> [!question] Pregunta del Profesor a la Clase / Duda de validación: _¿El [[Poliedro de Soluciones]] puede ser un conjunto cóncavo o tener "dos áreas distintas, soluciones separadas"?_

**Respuesta del Profesor:** Totalmente **Falso**. Es mecánicamente imposible tener áreas separadas porque la región debe verificar TODAS las restricciones simultáneamente. Además, siempre debe formarse un [[Polígono Convexo]]: esto significa que si tomas cualquier par de puntos dentro del polígono, la recta que los une quedará completamente dentro de la figura. Si no hay una única área de intersección común, el problema simplemente **no tiene solución**.

### D. Duda Crítica sobre Variables de Holgura (El Signo vs. El Valor)

> [!question] Pregunta del Alumno: _¿Cómo es posible que una variable se reste en la ecuación si usted acaba de decir que NUNCA pueden ser negativas? ¿No deberían ponerse como positivas?_

**Respuesta del Profesor (Concepto Clave):** El profesor se detuvo a escribir las ecuaciones en pantalla para diferenciar el "valor matemático" del "signo algebraico" de la operación:

1. La variable en sí misma **siempre cumple** que $S_i \geq 0$ (es cero o positiva).
2. Lo que cambia es **la operación algebraica** mediante la cual se inserta en la restricción para lograr la igualdad.

Para que no queden dudas, el profesor armó esta estructura lógica:

|Tipo de Inecuación|Situación del Recurso|Acción para Estandarizar|Signo de la Operación|Valor de la Variable ($S_i$)|
|:--|:--|:--|:--|:--|
|**Menor o igual ($\leq$)**|El lado izquierdo es menor al derecho.|Hay que **SUMARLE** una cantidad para igualarlo.|**$+S_i$**|$\geq 0$|
|**Mayor o igual ($\geq$)**|El lado izquierdo supera el requerimiento.|Hay que **RESTARLE** el exceso para igualarlo al mínimo.|**$-S_i$**|$\geq 0$|

> [!note] Representación en Función Objetivo Independientemente de si se suman o se restan en las restricciones, estas variables se agregan a la [[Función Objetivo]] con un coeficiente de **cero** ($+ 0S_1 + 0S_2...$).