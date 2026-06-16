https://www.youtube.com/watch?v=q7EOjGSJda0&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=3

Problema 1.5
Una persona ha recibido 1 millón de pesos de una herencia y le aconsejan que lo invierta en dos tipos de acciones, A y B. Las acciones de tipo A tienen más riesgo, ==pero producen un beneficio del 30% anual mientras que las de tipo B son más seguras, pero producen sólo el 10% anual. ==
Después de analizarlo decide invertir ==como máximo 600 mil en la compra de acciones A y, por lo menos, 200 mil en la compra de acciones B==. Además, ==decide que la cantidad invertida en A sea, por lo menos, igual a lo invertido en B.== 
¿Cómo deberá invertir el millón de pesos para que el beneficio anual sea máximo suponiendo que los valores tienen certeza y se puede comprar cualquier número de acciones A o B, inclusive fracciones de ellas?

a) Describa el objetivo en forma verbal
b) Defina las variables de decisión del problema.
c) ¿Al describir las variables utilizó alguna unidad de tiempo? Si la respuesta es afirmativa indique cual es en cada variable y cual corresponderá a la función objetivo
d) Formule la función objetivo explicando el valor de cada uno de los coeficientes.
e) Plantee las restricciones en forma literal y en forma de ecuaciones o inecuaciones lineales, explicando c/u de ellas.
f) Plantee el problema como un modelo de programación lineal.
g) Defina las variables de holgura


---
- **Lectura y Comprensión:** La profesora recalca que no se debe saltar a formular el modelo sin antes leer y expresar verbalmente el objetivo y las restricciones.

a) Describa el objetivo en forma verbal
	Maximazar el rendimiento del dinero invertido

b) Defina las variables de decisión del problema.
	A través del **Problema 5 (Inversión en Acciones)**, la profesora demostró qué hacer cuando los datos convencionales no están disponibles. Como el enunciado no proporcionaba el precio unitario de cada acción, no era posible definir las variables como "número de acciones a comprar".
	- **Definición de las [[Variables de Decisión]]:**
	    - _El problema de los datos:_ No se pueden definir las variables como "cantidad de acciones" porque el enunciado no da el precio unitario de cada acción.
    - _Solución:_ 
	    - Se debió definir la variable utilizando una unidad monetaria:
		    - x1="Pesos a invertir en la acción tipo A")
		    - x2="Pesos a invertir en la acción tipo B")
>[!danger] Trampa de Parcial (El uso de la palabra "Cantidad") Un error grave y frecuente es definir las variables como "cantidad de acciones a comprar". Esto es **INCORRECTO** en este caso específico porque el enunciado no nos proporciona el precio unitario de cada acción. Como el beneficio (30% y 10%) se calcula sobre el capital invertido, la variable debe definirse usando una unidad monetaria para mantener la coherencia del [[Análisis Dimensional]]

- **Formas de Definición de Variables:**
    - **[[Definición por Extensión]]:** Detallar cada variable individualmente (Ej: x1​ = pesos invertidos en acción A).
    - **[[Definición por Comprensión]]:** Usar una notación general (Ej: xi​ = pesos a invertir en la acción tipo i, para i=1,2).

c) ¿Al describir las variables utilizó alguna unidad de tiempo? Si la respuesta es afirmativa indique cual es en cada variable y cual corresponderá a la función objetivo

d) Formule la función objetivo explicando el valor de cada uno de los coeficientes.


---
> [!note] Modelo Matemático Formulado: Problema 5 **[[Función Objetivo]]:** (Maximizar el rendimiento total) MaxZ=0.30x1​+0.10x2​ **[[Restricciones]]:** x1​+x2​≤1000 (Capital disponible en miles) x1​≤600 (Máximo a invertir en A) x2​≥200 (Mínimo a invertir en B) x1​−x2​≥0 (Condición: Inversión en A ≥ Inversión en B) x1​,x2​≥0 ([[Condición de No Negatividad]]).

- **Concepto de Resolver:** Se define teóricamente que "resolver" el modelo es encontrar los valores numéricos de las variables que cumplan todas las inecuaciones y optimicen la función.
---

e) Plantee las restricciones en forma literal y en forma de ecuaciones o inecuaciones lineales, explicando c/u de ellas.
	Restriccion 1:
		como máximo 600 mil en la compra de acciones A
	Restriccion 2:
		por lo menos, 200 mil en la compra de acciones B
	Restriccion 3
		la cantidad invertida en A sea, por lo menos, igual a lo invertido en B.==





---
1. La Importancia del Análisis Previo a la Formulación

La profesora enfatizó que no se debe saltar directamente a escribir ecuaciones sin antes realizar un análisis comprensivo del enunciado. Textualmente indicó: _"no subestimen estos pasos de leer y analizar el problema e identificar con palabras qué es lo que tengo es muy importante y en medida que los problemas se hacen más complicados más importantes se vuelven estos pasos"_.

[!tip] Metodología de Resolución Antes de plantear variables matemáticas (x1​,x2​), debes escribir verbalmente cuál es la meta del decisor y cuáles son los límites físicos o económicos que enfrenta.

2. El Error Crítico de Usar la Palabra "Cantidad"

Un punto de gran énfasis, basado en errores detectados en cuestionarios anteriores, es la definición de las [[Variables de Decisión]].

[!danger] Trampa de Parcial (Definición de Variables) La profesora advirtió firmemente que definir una variable como "cantidad del producto" es un error conceptual. Explicó que _"cantidad no es una unidad a la cual esta medida"_. Por ejemplo, en lugar de decir "cantidad de dinero a invertir", se debe ser exacto y definir "pesos a invertir", o en lugar de "cantidad de sillas", usar "unidades de sillas a producir". Esto garantiza la correcta aplicación del [[Análisis Dimensional]].

---
[!question] Pregunta 1: Notación de Variables (Por Extensión vs. Comprensión) **Alumno:** Al ver cómo la profesora definía matemáticamente las variables genéricas, el alumno consultó cómo se llamaba esa forma de anotación en contraposición a listar x1​ y x2​. **Respuesta de la Profesora:** Explicó que definir xi​ como _"pesos a invertir en la acción tipo i (para i=1, 2)"_ se denomina **[[Definición por Comprensión]]**, mientras que listar x1​ y x2​ de forma individual es **[[Definición por Extensión]]**. Recomendó la forma por comprensión cuando existen múltiples variables (ej: 6 u 8 acciones) para ahorrar tiempo y mantener la claridad]
