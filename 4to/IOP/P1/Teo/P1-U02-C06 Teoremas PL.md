Aquí tienes el análisis estructural de la clase teórica. He destilado la transcripción para identificar los **4 pilares fundamentales** sobre los que el profesor construyó su explicación, priorizando el enfoque conceptual y metodológico que exige la materia.

## 2. Fase 2: Repaso del Dominio de Soluciones (9:00 - 15:44)

El primer tema central fue repasar y asentar la jerarquía formal de las soluciones dentro de un modelo matemático. El profesor aclaró que todo análisis de soluciones debe hacerse obligatoriamente sobre un modelo convertido previamente a su [[Forma Estándar]] (agregando las [[Variables de Holgura]]).

- **[[Solución]]:** Cualquier conjunto de valores que simplemente verifique el sistema de ecuaciones (las [[Restricciones Funcionales]]).

![[{09FF7A35-35E7-4CCF-A9B2-48E28FF5502F}.png]]

- **[[Solución Factible]]:** es un conjunto de varlos de las  variables x_j que verifican el sistema de restricciones incluidas las de no negatividad
![[{D946E571-80C3-46C7-9441-ECF72B3DC323}.png|192]]

- **[[Solución Factible Básica]]:** es toda solucion factible que tiene como maximo m variables positivas; o como minimo n-m valores de las variables nulos
	- ![[{D2395769-C226-46DD-A56B-CA87969EFAC9}.png]]
		- Solucion factible Basica No Degenerada: tiene exactamente m variables positivas, o exactamente n-m variables nulas
			- ![[{0F009A70-1619-4C7F-AFCC-D4F982C101F2}.png]]
		- Solucion factible basica degenerada: tiene menos de m variables positivas, o mas de n-m variables nulas
			- ![[{9E94F23C-5032-4B3B-9DE7-B25ED5A1395B}.png]]

![[{1C1549F3-5ABB-4613-A356-C97B2E50CB57}.png]]
Ubicación gráfica:
	Soluciones Factibles Básicas = Vértices del poliedro.
	Soluciones Factibles No Básicas = Lados e interior del poliedro.
	Soluciones Básicas No Factibles = Intersecciones de las rectas que caen fuera de la región válida.

- **[[Solución Óptima]]:** es toda solucion que le da a la funcion Z el valor optimo (maximo o minimo)


> [!note] Fórmula del Número Máximo de Soluciones Básicas Para calcular el límite superior de combinaciones que se pueden formar en el sistema: $$ C = \frac{n!}{m!(n-m)!} $$ Donde $n$ son todas las variables (incluyendo [[Variables de Holgura]]) y $m$ las restricciones funcionales sin contar la de no negatividad.

Las soluciones Fatibles basicas son un subconjuntos de las soluciones basicas, por lo tanto el numero maximo de soluciones basica tmb sirve como cota superior o numero maximo para las soluciones factibles basicas

## 3. Fase 3: Teoría Analítica y Teoremas de PL (15:44 - 34:00)


| Teorema Teórico | Definición del Profesor                                                                                                                                   | Consecuencia / Corolario                                                                                                                                                       |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Teorema 1**   | Toda [[Combinación Lineal Convexa]] de soluciones factibles da como resultado otra solución factible.                                                     | Demuestra que la región factible es un [[Conjunto Convexo]]. El conjunto de soluciones puede ser vacío, unitario o tener infinitos elementos.                                  |
| **Teorema 2**   | Si dos soluciones factibles le otorgan el mismo valor a $Z$, cualquier combinación convexa de ellas dará otra solución con ese exacto mismo valor de $Z$. | Explica el fenómeno de la [[Recta de Isoutilidad]] paralela a una restricción limitante. Genera el caso de infinitas soluciones óptimas.                                       |
| **Teorema 3**   | Si un programa lineal tiene solución óptima, existirá siempre al menos una [[Solución Factible Básica]] (vértice) que sea óptima.                         | Es el **[[Teorema Fundamental de la Programación Lineal]]**. En él se basa el [[Algoritmo Simplex]], ya que justifica buscar el óptimo exclusivamente saltando entre vértices. |

### teorema 1
Teorema 1: Establece que toda combinación lineal convexa de soluciones factibles da por resultado otra solución factible. Este teorema demuestra matemáticamente que el conjunto solución (el poliedro) de cualquier programa lineal es siempre un conjunto convexo.
![[Pasted image 20260624173601.png|576]]

Combinación Lineal Convexa: Es una operación matemática entre vectores que utiliza constantes (escalares, denotados como α). Para que la combinación sea estrictamente "convexa", estos escalares deben cumplir dos condiciones: ser no negativos (mayores o iguales a cero) y su suma debe ser exactamente igual a 1. El resultado es un nuevo vector o punto ubicado en el segmento de recta que une a los dos puntos originales.

Conjunto Convexo: Es un conjunto de puntos con la propiedad geométrica de que, si se toman dos puntos cualesquiera del conjunto y se realiza una combinación lineal convexa entre ellos, el punto resultante también pertenecerá a dicho conjunto

Es decir que si hacemos cl P1 y P2 (SOLUCIONES FACTIBLES) , de esta forma $$ P_0=\alpha_1P_1+\alpha_2P_2$$​​

siendo $$\alpha_i ≥ 0 $$^  $$\sum\alpha_i=1$$

P0, pertenecera a esa recta formada entre P1 y P2, (SERA OTRA SOLUCION FACTIBLE)

CONCECUENCIAS
![[Pasted image 20260624174036.png|588]]

### teorema 2
> **Teorema 2 (y Recta de Isoutilidad / Isocosto)**: Indica que si existen dos o más soluciones factibles que le otorgan el mismo valor a la función objetivo (Z), cualquier combinación lineal convexa de ellas dará exactamente ese mismo valor
![[Pasted image 20260624174124.png]]


### Teniendo cuenta el algoritmo 1 y 2
![[Pasted image 20260624174253.png|575]]

| conjunto de soluciones factibles | conjunto de soluciones optimas                          |
| -------------------------------- | ------------------------------------------------------- |
| vacio                            | vacio                                                   |
| un elemento                      | un elemento (SOL. optima en la inter. de restricciones) |
| infinitos elementos              | 1 elemento (sol opt. en un vertice)                     |
| infinitos elementos              | vacio (problema no acotado)                             |
| infinitos elementos              | infinito elementenos (multiples optimos)                |
Cuando el conjunto de soluciones optimas puede ser infinito?
por ejemplo cuando la recta Z coincide con una restricción limitante

- es decir yo tengo dos soluciones que le dan el valor optimo, entonces por cl convexa obtengo infinitas soluciones
![[Pasted image 20260624174427.png|590]]
Por esto vemos que si no es vacio, o esta formado por un unico vertice o por infinitos
### Teorema 3 (Teorema Fundamental de la PL): (ESTE NO TIENE DEMOSTRACION)
> Teorema 3 (Teorema Fundamental de la Programación Lineal): Postula que si un problema es resoluble y tiene solución óptima, esta siempre se encontrará en al menos una solución factible básica (un vértice). Es el fundamento matemático vital sobre el cual se construyó el Algoritmo Simplex

Traducido al aspecto gráfico, el teorema garantiza que el óptimo jamás estará flotando en el medio del poliedro, sino que siempre se ubicará en al menos uno de sus vértices. Su enorme importancia radica en que es la base teórica fundamental sobre la que se construyó el Método Simplex.

3. El Teorema 3 (El Teorema Fundamental) Hizo un gran énfasis en el Teorema 3, catalogándolo repetidamente como el "teorema fundamental de la programación lineal". Explicó que su importancia radica en que es la base teórica absoluta sobre la cual George Dantzig desarrolló el algoritmo Simplex, ya que garantiza que el óptimo siempre estará en al menos un vértice.
## 4. Fase 4: Cuestionario, Errores y Procedimientos (34:00 - Fin)

Cuestionario: Los alumnos realizan una prueba evaluativa para medir su comprensión,.

### Revisión del Ejercicio 1 (Clasificación de Soluciones):
* Se explica el procedimiento paso a paso para saber si un punto es solución.
	* Primero hay que transformarlo a forma estándar (agg variables de holgura),
	* 2do evaluar si los números (x1;x2;S1;S2;S4;S5) dados cumplen matemáticamente las restricciones, SI LA CUMPLEN ES SOLUCION,
	* 3ero una vez que sabemos que es solucion, la clasificamos: revisar si hay negativos (factibilidad) y contar los ceros (si es básica)-.
> [!tip] Metodología de Resolución Oficial: Clasificación de Soluciones El profesor estableció un protocolo de 3 pasos innegociables para evaluar puntos en un examen:
> 
> 1. **Estandarizar:** Agregar obligatoriamente las [[Variables de Holgura]] para igualar el sistema.
> 2. **Verificar Cumplimiento:** Reemplazar los valores para ver si la igualdad matemática se sostiene.
> 3. **Clasificar:** Revisar si hay variables negativas (define factibilidad) y contar la cantidad de ceros (define si es básica).

![[Pasted image 20260624174710.png|661]]
![[Pasted image 20260624174722.png]]
![[Pasted image 20260624174744.png]]
	esto ta mal
	![[Pasted image 20260624174811.png]]
	z=6500, osea que si esta planteado asi, estaria bien que NO SEA SOLUCION


> [!question] Pregunta de Clase _¿Por qué debemos probar valores si vemos que tienen una variable negativa? ¿No descartamos la solución directamente?_ 
> El profesor aclara que una variable negativa descarta que sea "Factible", pero **SÍ** puede ser una [[Solución Básica No Factible]] si cumple algebraicamente el sistema. No se descarta del análisis general.


> [!danger] Trampa de Examen: Saltarse la Forma Estándar Un error letal evidenciado en el cuestionario es intentar clasificar soluciones evaluando las inecuaciones originales. Las soluciones de PL siempre se definen y evalúan sobre la [[Forma Estándar]] del modelo.


### APLICACION TEOREMA 1 Revisión del Ejercicio 2 (Cálculo algebraico):
profesora enseña cómo aplicar matemáticamente Teoremas 1, resolviendo en una pizarra una combinación lineal convexa utilizando los vectores solución y asignando el valor escalar $\alpha = 0.5$ para encontrar nuevos puntos factibles-,,.![[Pasted image 20260624175018.png]]
paso 1: alpha1* poer el vector 1, y nos da un vector ; alpha2*por el 2do vector y nos da otro vector, esto los sumamos y son la solucion

$$\alpha_1\bar x_1+\alpha_2 \bar x_2 = \bar x_3$$
![[Pasted image 20260624175054.png|402]]
### Revicion ej 3 aplicacion teorema 2
![[Pasted image 20260624175110.png]]
teorema 2: si tengo dos o mas soluciones que le dan el mismo valor a z, toda cl le da otra sol factible que le da a z el mismo valor

selecciones los dos vectores que me dan 8000, y si quiero encontrar otro que me de 8000 hago la CL convexa entre esos 2

$\alpha_1\bar x_1+\alpha_2 \bar x_2 = \bar x_3$

y si verifico z, me da 8000

>[!question] un alumno preguntó si, en el caso de tener tres puntos conocidos que dieran ese mismo valor, debía hacer una combinación lineal sumando los tres vectores.
>Respuesta: Apoyándose en un gráfico en la pizarra, la profesora le aclaró que solo se necesitan tomar dos puntos cualesquiera que estén sobre la recta de isoutilidad. Al hacer una combinación lineal convexa entre dos puntos, el resultado será siempre otro punto válido situado sobre el segmento de recta que los une.



# ----
Aquí tienes el análisis estratégico de la clase virtual. He escaneado la transcripción para detectar exactamente dónde el profesor elevó el tono para marcar temas de examen y he recopilado las dudas de tus compañeros, ya que representan los errores más comunes en los que podrías caer.

# 🚨 RADAR DE PARCIAL: ÉNFASIS Y MARCADORES DE IMPORTANCIA

El profesor fue categórico al señalar ciertos conceptos teóricos como el núcleo fundamental de la materia, los cuales justifican todo el desarrollo práctico posterior.

### 1. El Fundamento del Método Simplex

El profesor hizo un énfasis absoluto al explicar el **Teorema 3** de la [[Programación Lineal]], indicando que es "fundamental" y la base algorítmica de lo que verán el resto del semestre.

> [!note] Teorema Fundamental de la Programación Lineal $$ \text{Si un problema tiene solución óptima, existirá al menos una Solución Factible Básica (vértice) que sea óptima.} $$

- **¿Por qué es clave para el examen?** El profesor explicó que este teorema justifica la existencia del algoritmo que inventó George Dantzig. Gracias a este teorema, el [[Método Simplex]] no necesita explorar todos los puntos interiores infinitos del poliedro, sino que "salta" exclusivamente evaluando las [[Soluciones Factibles Básicas]] (los vértices).

### 2. La Cota Superior de Soluciones

El profesor remarcó con un "esto es muy importante" el límite de soluciones a evaluar.

> [!note] Fórmula Combinatoria de Soluciones Básicas $$ C = \frac{n!}{m!(n-m)!} $$

Explicó que este número combinatorio (donde $n$ son todas las variables y $m$ las restricciones) no solo da el número máximo de [[Soluciones Básicas]], sino que también funciona como una **cota superior** para las [[Soluciones Factibles Básicas]]. Como este número es finito, permite que el software o el humano puedan terminar de calcular el problema.

### 3. Advertencia Crítica y Tarea Obligatoria

> [!danger] PRE-REQUISITO EXCLUYENTE PARA LA PRÓXIMA CLASE El profesor fue tajante: para la próxima clase se evaluará el [[Método Simplex]]. Indicó explícitamente que es **obligatorio ("sí o sí")** ver el video pregrabado del profesor Martín con la teoría del Simplex antes de asistir a la clase sincrónica. En la próxima sesión no explicará la teoría desde cero, sino que irá directo a trabajar un problema con el algoritmo.

---

# 🗣️ PREGUNTAS DE ALUMNOS Y RESPUESTAS DEL PROFESOR

Durante la sesión y el cuestionario práctico, los alumnos manifestaron varias confusiones críticas. Aquí tienes el resumen estructurado de las "trampas" en las que cayeron.

### A. Confusión: Clasificación de Soluciones

> [!question] Pregunta de Alumno _"Profe, ¿puede ser que había una solución que era básica y otra que era factible y básica?"_

**Respuesta del Profesor:** Sí, y la diferencia radica en el cumplimiento de la [[Restricción de No Negatividad]]. El profesor aclaró esta jerarquía:

|Tipo de Solución|Condición de Variables No Nulas|Condición de Signo|Ubicación Gráfica|
|:--|:--|:--|:--|
|**[[Solución Básica No Factible]]**|Tiene un máximo de $m$ valores positivos.|**Posee al menos un valor negativo.**|Intersecciones de rectas fuera de la región válida.|
|**[[Solución Factible Básica]]**|Tiene un máximo de $m$ valores positivos.|**Todos sus valores son $\geq 0$.**|Exclusivamente en los vértices del [[Poliedro de Soluciones]].|

### B. Confusión: Evaluación de Variables Negativas

> [!question] Pregunta de Alumno _"Yo tenía la duda de por qué probar algunas variables negativas que lo dijo recién usted..."_

**Respuesta del Profesor:** Muchos alumnos cometen el error de descartar una solución apenas ven un número negativo sin evaluar el sistema de ecuaciones. El profesor explicó que una variable negativa nos dice que la solución no es factible, pero **sí puede cumplir el sistema de ecuaciones** algebraicamente. Si cumple el sistema, se clasifica como una [[Solución Básica No Factible]].

> [!tip] Metodología de Resolución: Evaluación de Puntos El profesor dictó un protocolo algorítmico estricto de 3 pasos para analizar cualquier punto:

```
graph TD
    A(Paso 1: Reemplazar valores y ver si cumple el sistema de ecuaciones) --> B{¿Cumple?}
    B -->|Sí| C(Paso 2: Revisar signos para determinar Factibilidad)
    B -->|No| D(No es Solución)
    C --> E(Paso 3: Contar variables nulas para determinar si es Básica)
```

_Conceptos relacionados:_ [[Sistema de Ecuaciones]], [[Solución Factible]], [[Solución Básica]].

### C. Confusión: El Error del Cuestionario y la "Forma Estándar"

> [!question] Queja de los Alumnos Varios alumnos indicaron que el cuestionario tenía "todo en rojo" y que no podían clasificar los puntos porque no tenían "experiencia resolviendo sistemas" o esperaban un "ejercicio resuelto".

**Respuesta del Profesor (Trampa Teórica):** El profesor detectó el error raíz: los alumnos estaban intentando evaluar los puntos en el modelo original con inecuaciones ($\leq, \geq$). Recordó tajantemente que **toda evaluación de soluciones se hace sobre la Forma Estándar**.

> [!danger] Error Crítico de Parcial Nunca evalúes puntos en el modelo canónico original. El paso cero obligatorio es agregar las [[Variables de Holgura]] para convertir las desigualdades en igualdades. Solo después de eso puedes probar si los valores de $x$ verifican el sistema.

### D. Confusión: Teorema 2 y la Recta de Isoutilidad

> [!question] Pregunta de Alumno _"Si hubiera puesto otro vector que da 8000, ¿sería una suma de tres vectores? ¿Puedo tomar dos a dos?"_

**Respuesta del Profesor:** El alumno preguntaba cómo aplicar el [[Teorema 2]] (Múltiples óptimos) si tenía tres puntos sobre la misma recta de $Z=8000$. El profesor aclaró que para realizar la [[Combinación Lineal Convexa]] solo se necesitan usar **dos puntos** cualesquiera que estén sobre la [[Recta de Isoutilidad]]. Cualquier combinación de esos dos generará un nuevo punto que también estará apoyado sobre esa recta, dando exactamente el mismo valor a la [[Función Objetivo]].