Problema 1.12
Un constructor va a edificar dos tipos de viviendas prefabricadas: con uno o dos
dormitorios. Dispone de 6 millones de pesos y el costo de una vivienda de 2
dormitorios es de 500 mil pesos mientras que las de un dormitorio cuestan 350 mil
pesos. El número de casas de dos dormitorios deberán ser al menos del 35% del total
fabricado y el de un dormitorio del 25% por lo menos. Para mantener la seguridad
del negocio a realizar, la inversión en viviendas de dos dormitorios no deberá superar
los 4,5 millones, y la inversión en casas de un dormitorio podrá llegar sólo a un límite
máximo del 70% de la inversión total realizada.
Si cada casa de dos dormitorios se vende a 850 mil pesos y cada una de un dormitorio
a 550 mil pesos, ¿Cuántas casas de cada tipo debe construir para obtener el beneficio
máximo?

---
3. Formulación Intermedia: Problema 12 "Constructor de Viviendas" (35:26 - 58:44)

El nivel de dificultad aumenta con un problema de construcción de casas prefabricadas (de 1 y 2 dormitorios), donde se mezclan presupuestos fijos con restricciones proporcionales.

- **Identificación del Objetivo:** Se debate si el objetivo es maximizar producción o ganancias. Se concluye que es maximizar el beneficio (Precio de Venta - Costo).
- **Traducción de Porcentajes a Ecuaciones:** El desafío principal de este problema fue formular restricciones de proporcionalidad (Ej: "Las casas de 1 dormitorio deben ser por lo menos el 25% del total construido").
    - Formulación correcta: x1​≥0.25(x1​+x2​).
- **Estandarización para Resolución:** Para que un software o el [[Método Simplex]] pueda procesar el modelo, las variables deben agruparse a la izquierda y las constantes a la derecha del signo.

[!question] Pregunta de Clase: Confusión de Unidades Un alumno notó que en una misma restricción se multiplicaban "pesos" por "unidades de casas" y preguntó si era correcto. _Respuesta de la profesora:_ Explicó el [[Análisis Dimensional]]. Al multiplicar el costo (Pesos/Unidad) por la variable (Unidades), las "unidades" se simplifican matemáticamente y el resultado queda expresado netamente en "Pesos", siendo coherente con el Límite (Lado Derecho) de la restricción.

---
2. Formulación de [[Restricciones Proporcionales]] y Mixtas

Con el **Problema 12 (Constructor de Viviendas)**, se abordó el desafío de traducir porcentajes y mezclar distintas unidades físicas y monetarias en un mismo modelo.

- **Restricciones de Porcentaje:** Se pedía que las casas de un dormitorio fueran "por lo menos el 25% del total fabricado". La formulación correcta exige sumar ambas variables para representar el total: x1​≥0.25(x1​+x2​).
- **Estandarización:** Para que el modelo pueda resolverse matemáticamente, la profesora indicó que todas las variables deben despejarse hacia el lado izquierdo de la inecuación, dejando solo constantes del lado derecho.

[!question] Pregunta de Clase: Confusión con el Análisis Dimensional Un alumno se confundió al ver que en una restricción se mezclaban "unidades de casas" y "pesos". _Respuesta de la Profesora:_ Explicó que al multiplicar el costo (Pesos/Casa) por la variable (Casas), las unidades de "casa" se simplifican matemáticamente, resultando netamente en "Pesos". Esto hace que el lado izquierdo de la ecuación sea perfectamente coherente con el límite de presupuesto (Lado Derecho).

---
3. Diferencia entre "Positivo" y "No Negativo"

Al momento de plantear el cierre del modelo matemático, recalcó una confusión teórica recurrente:

[!danger] Confusión Frecuente _"Recuerden por favor que no negatividad quiere decir mayor o igual a 0 no quiere decir positivo recuerden la diferencia"_. Exigir que una variable sea positiva excluye el valor cero, lo cual alteraría el conjunto de soluciones factibles en la [[Programación Lineal]].

---


[!question] Pregunta 2: Estructura de las Restricciones Proporcionales **Alumno:** En el problema de construcción de viviendas, un alumno planteó si la restricción de porcentaje (25% del total fabricado) debía escribirse ya despejada con las constantes a la derecha para que fuera correcta. **Respuesta de la Profesora:** Aclaró que, para el momento inicial de _formular_ el modelo y que sea legible por un humano, es perfectamente correcto (y deseable) plantearla lógicamente como x1​≥0.25(x1​+x2​). Sin embargo, confirmó que _para resolverlo_ matemáticamente después, el alumno debe aplicar propiedad distributiva y pasar las variables a la izquierda.


[!question] Pregunta 3: Confusión con el [[Análisis Dimensional]] **Alumno:** _"¿Siempre vamos a estar trabajando con dos tipos de unidades? Por ejemplo dinero y unidades de casa en una misma restricción..."_. Al alumno le generaba ruido visual mezclar "pesos" y "casas" en la misma inecuación. **Respuesta de la Profesora:** Explicó el mecanismo matemático de cancelación de unidades. Cuando se multiplica el coeficiente de costo (medido en Pesos/Unidad de Vivienda) por la variable de decisión (medida en Unidades de Vivienda), la unidad "vivienda" se simplifica. El resultado neto del lado izquierdo queda en Pesos, lo cual es coherente con el límite del [[Lado Derecho]], que también son Pesos.