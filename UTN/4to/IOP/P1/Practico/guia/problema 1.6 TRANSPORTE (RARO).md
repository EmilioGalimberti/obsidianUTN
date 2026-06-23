# Enunciado
Una empresa energética dispone de tres plantas de generación para satisfacer la demanda eléctrica de cuatro ciudades. Las ==plantas 1, 2 y 3 pueden satisfacer 35, 50 y 75 millones de kw==. respectivamente. El ==valor máximo de consumo ocurre a las 2pm y es de 45, 40, 80 y 30 millones de kw==. en las ciudades 1, 2, 3 y 4 respectivamente. El costo de enviar 1 kw depende de la distancia que deba recorrer la energía. La siguiente tabla muestra los costos de envío unitario desde cada planta a cada ciudad.

![[{CE131A54-0A9F-4106-AF16-768795155089}.png]]

a) Formule el problema como un modelo de PL.
b) Describa correctamente las variables y objetivos del problema.

---
objetivo: Minimizar el costo total de transporte de la energia

variables de decicion:
* - $x_{ij}$: "Cantidad de kilowatts a enviar desde la planta $i$ a la ciudad $j$" (donde $i = 1,2,3$ y $j = 1,2,3,4$).

restricciones
* producción máxima de planta1
* producción máxima de planta2
* producción máxima de planta3
* demanda maxima de ciudad1
* demanda maxima de ciudad2
* demanda maxima de ciudad3

---

==PROBLEMA DESIQUILIBRADO==
![[{1E126FCF-D097-4E15-8AD5-8C22179B99CE}.png]]
Este es el punto técnico más importante de la primera mitad de la clase. Al sumar la capacidad de las plantas ($160$ millones de kW) y compararla con el consumo total requerido ($195$ millones de kW), se observa que la demanda supera a la producción.

![[{FD7ED707-7F03-4A1B-9B25-535E75EE4064}.png|534]]
- **[[Planta Ficticia]]:** Para que el [[Modelo de Transporte]] pueda resolverse, debe estar estrictamente equilibrado. Se debe agregar una planta inventada (origen ficticio) que "produzca" los 35 millones de kilowatts faltantes.
- **Interpretación de Variables Ficticias:** Las variables asociadas a esta planta ficticia representan en realidad la **demanda insatisfecha** (los kilowatts que la ciudad no va a recibir).
- **Penalización en el Objetivo:** Como estas unidades en realidad no se envían, su costo de transporte en la [[Función Objetivo]] es exactamente $0$.

==funcion objetivo==
Min Z = 18X_11+16X_12+20X_13+19X_14+19X_21+22X_22+25X_23+17X_24+24X_31+19X_32+30X_33+15_34+0X_41+0X_42+0X_43+0X_44

==Restricciones==
X_11+X_12+X_13+X_14=35
X_21+X_22+X_23+X_24=50
X_31+X_32+X_33+X_34=75
X_41+X_42+X_43+X_44=35 (origen ficticio)
(Restricciones que indican que cada origen debe enviar los kw de energia que posee)

> [!note] Restricciones de Igualdad Estricta En un [[Modelo de Transporte]] equilibrado, las inecuaciones se transforman en ecuaciones. Las plantas envían exactamente todo lo que producen (incluida la planta ficticia) y las ciudades reciben exactamente todo lo que demandan, formulándose todas las restricciones con el signo de igualdad ($=$).

X_11+X_21+X_31+X_41=45
X_12+X_22+X_32+X_42=40
X_13+X_23+X_33+X_43=80
X_14+X_24+X_34+X_44=30
(Restricciones que indican que cada destion o ciudad debe recibir los KW de energia que requiere)


---
porque en el ej 6 las retricciones solo son X y no estan acompañadas por un coeficiente?
¡Hola! Excelente observación. Como tu Tutor Académico de Élite, me alegra ver que estás prestando atención a la estructura matemática de las ecuaciones.

La razón por la cual en el Problema 6 ("Energy S.A.") las [[Variables de Decisión]] ($X$) parecen estar "solas" sin un coeficiente numérico multiplicándolas, es porque en realidad **su coeficiente es exactamente $1$**.

El porqué de esto radica en la naturaleza del [[Modelo de Transporte]] y en el principio de [[Análisis Dimensional]] que la profesora explicó en clase. A continuación, te detallo la justificación técnica.

---

### 1. La Coherencia del [[Análisis Dimensional]]

A diferencia de los problemas de manufactura (donde produces unidades físicas pero consumes "horas" o "gramos"), en un [[Modelo de Transporte]] puro, lo que transita por la red es exactamente lo mismo que te limita.

La profesora lo justificó con esta lógica:

- **La Variable ($X_{ij}$):** Indica la _"cantidad de kilowatts a enviar"_.
- **El [[Lado Derecho]] de la restricción:** Indica los _"kilowatts disponibles en la planta"_ o los _"kilowatts demandados por la ciudad"_.

Como la unidad de medida de la variable (Kilowatts) es **idéntica** a la unidad de medida del límite (Kilowatts), no necesitas ningún parámetro de conversión. Al sumar $x_{11} + x_{12} + x_{13} + x_{14}$, ya estás sumando netamente "Kilowatts enviados", lo cual se compara directamente con los 35 millones de Kilowatts que produce la planta.

> [!note] Regla Estructural del Modelo de Transporte En la formulación de orígenes y destinos de un [[Modelo de Transporte]], los coeficientes tecnológicos de las variables en las restricciones físicas **siempre son $1$**. La ecuación es una sumatoria directa de flujo: $$1x_{11} + 1x_{12} + 1x_{13} + 1x_{14} = 35$$

### 2. Lo que NO debe ir en las Restricciones

Un error común al ver la tabla de datos del Problema 6 es querer usar los números del centro de la tabla (18, 16, 12, etc.) como coeficientes para las $X$.

> [!danger] Trampa de Parcial (Costos vs. Capacidades) La profesora advirtió explícitamente: _"los numeritos que nosotros tenemos acá en esta tabla... son los costos unitarios del envío"_. Esos costos se miden en **Pesos por Kilowatt**. Si los pusieras en las restricciones, estarías transformando el lado izquierdo en "Pesos", lo cual sería incompatible con el límite de la planta que está en "Kilowatts". **Los costos van EXCLUSIVAMENTE en la [[Función Objetivo]].**

---

### Análisis Comparativo: Transporte vs. Producción

Para que la diferencia estructural te quede grabada para el parcial, compara el Problema 6 con el Problema 14 (el de los envases) que vieron en la misma clase:

|Tipo de Modelo|Problema Analizado|Unidad de la [[Variable de Decisión]]|Unidad del [[Lado Derecho]]|¿Requiere Coeficiente de Conversión?|
|:--|:--|:--|:--|:--|
|**[[Modelo de Transporte]]**|Ejercicio 6 (Energy SA)|Kilowatts enviados|Kilowatts disponibles|**NO (Coeficiente $= 1$)**. La suma es directa.|
|**[[Modelo de Producción]]**|Ejercicio 14 (Envases)|Unidades a envasar|Horas de máquina|**SÍ (Ej: $1/60$ horas/unidad)**. Se requiere para igualar unidades.|

---

### Flujo Dimensional en el Modelo de Transporte

El siguiente diagrama ilustra cómo fluyen las unidades en las restricciones del Ejercicio 6 sin necesidad de alterarse con parámetros:

```
graph LR
    A[Variable X11] -->|Medida en: Kilowatts| C(Suma Directa)
    B[Variable X12] -->|Medida en: Kilowatts| C
    C --> D[Total Enviado por la Planta 1]
    D -.->|Coincide exactamente en unidad física con| E[Lado Derecho: 35 Millones de Kilowatts]

    style C fill:#f9f,stroke:#333,stroke-width:2px
```

_Conceptos relacionados:_ [[Análisis Dimensional]], [[Modelo de Transporte]], [[Lado Derecho]], [[Variables de Decisión]].

> [!tip] Tip de Formulación Siempre que dudes si una variable lleva coeficiente en la restricción o si va "sola" (con coeficiente $1$), pregúntate: _"¿La unidad en la que definí mi variable es exactamente la misma unidad en la que está expresado el límite máximo?"_. Si la respuesta es sí, las variables solo se suman.