# **Preguntas Teóricas \- Investigación Operativa**

## **Primer Parcial**

**Pregunta 1:**  ✅
Dado un problema de minimización, si en una iteración específica de simplex no se elige como variable que entra a la que tienen la diferencia (cj \- zj) \< 0 de mayor valor absoluto, la próxima solución será:

* a) Factible pero No Básica  
* b) Factible No básica y Degenerada  
* c) Factible Básica Degenerada  
* d) Básica pero No Factible  
* e) No Básica y No Factible  
* **f) Ninguna de las demás respuestas es correcta** *(Respuesta marcada)*

**Pregunta 2:**   ✅
Dado un programa lineal de maximización formulado en forma canónica, que tiene 7 variables de decisión y 4 restricciones. ¿Una solución factible básica degenerada cuántas variables nulas debe tener?



**Pregunta 3:**   ✅
Si un Programa Lineal es no factible significa que:

* a) Al menos una variable de decisión se puede hacer tan grande como se desee en la dirección de optimización sin dejar la región factible.  
* b) La función objetivo puede moverse tan lejos como se desee en la dirección de optimización y todavía tocar al menos un punto del conjunto factible.  
* c) Ninguna de las restricciones puede ser satisfecha.  
* **d) Al menos una de las restricciones no puede ser satisfecha.** *(Respuesta marcada)*  
* e) Ninguna de las anteriores

**Pregunta 4:**  
Acabamos de resolver un modelo de minimización de costos (no degenerado) y x1\* \= 0\. La Administración quisiera saber: ¿cuánto deberá modificarse el costo de x1 antes de que comencemos a emplearlo con un valor positivo en la solución óptima? ¿En qué parte del informe de sensibilidad se encuentra la respuesta?

* a. En la disminución permisible de x1.  
* b. En los valores de las variables.  
* **c. En la disminución permisible de c1.** *(Respuesta marcada)*  
* d. En el incremento permisible de c1.  
* e. En el incremento permisible de x1.  
* f. En el precio sombra.

**Pregunta 5:**  
Dado un problema de programación lineal de máximo en forma canónica con 5 restricciones y 4 variables de decisión. Una solución con 4 variables positivas y las restantes nulas, se dice que es una:

* **a. Solución factible básica degenerada** *(Respuesta marcada)*  
* b. Solución factible no básica  
* c. Solución no factible  
* d. Solución factible básica no degenerada  
* e. Solución factible no básica  
* f. Ninguna respuesta es completamente correcta

**Pregunta 6:**  
Dado un problema de programación lineal de mínimo con 5 variables de decisión, 3 restricciones del tipo \<= y 2 restricciones del tipo \>=. ¿Cuántas variables no positivas y cuántas variables no negativas tendrá su Dual?

* **Respuesta (manuscrita):** Variables no positivas del Dual: 2\. Variables no negativas del Dual: 3\.

**Pregunta 7:**  
Si un Programa Lineal es no acotado significa que:

* a) Al menos una variable de decisión se puede hacer tan grande como se desee en la dirección de optimización sin dejar la región factible.  
* **b) La función objetivo puede moverse tan lejos como se desee en la dirección de optimización y todavía tocar al menos un punto del conjunto factible.** *(Respuesta marcada)*  
* c) Ninguna de las restricciones puede ser satisfecha.  
* d) Al menos una de las restricciones no puede ser satisfecha.  
* e) Ninguna de las anteriores

**Pregunta 8:**  
Una relación correcta es:

* a) Las restricciones con precio sombra igual a cero deben ser no limitantes  
* **b) Las restricciones con precio sombra positivo deben ser limitantes** *(Respuesta marcada)*  
* c) Las restricciones con precio sombra igual a cero deben ser limitantes  
* d) Las restricciones con precio sombra positivo deben ser no limitantes

**Pregunta 9:**  
Dado un programa lineal de maximización formulado en forma canónica, que tiene 7 variables de decisión y 4 restricciones, el número máximo de Soluciones Básicas del problema es:

* **Respuesta (manuscrita):** 330

**Pregunta 10:**  
Si el bi (VLD) de una restricción limitante disminuye en Δbi estando este valor dentro de los límites de sensibilidad, ¿en cuánto se modifica el valor de la FO?

* **Respuesta:** Se decrementa en Δbi \* yi

**Pregunta 11:**  
Si x1 y x2 son variables binarias cuyos valores representan si se emprende o no un determinado proyecto, ¿qué condición representa la restricción x2 \- x1 \= 0?

* **Respuesta:** Si se reescribe la restricción, quedaría: X1 \= X2. Por lo que se emprende el proyecto X1 sí solo sí se emprende el proyecto X2.

**Pregunta 12:**  
¿Por qué en PNL no se puede usar un algoritmo como Simplex para explorar los puntos extremos de la solución factible?

* **Respuesta:** Una primera complicación se da cuando el óptimo no se encuentra en un vértice (ya sea porque el conjunto de soluciones no sea un poliedro, o porque la FO sea no lineal). Este hecho tiene consecuencias algorítmicas importantes, ya que es necesario que, para resolver este tipo de problemas, se tengan en cuenta todas las soluciones de la región factible, y no solo aquellas que están en los vértices. No se dispone de un algoritmo que resuelva todos los problemas específicos que se ajustan a este formato. Otro problema se da cuando aparecen óptimos locales y óptimos globales. En general, los algoritmos de PNL no son capaces de distinguir entre un óptimo local y uno global.

**Pregunta 13:**  
¿Cuál/es de las siguientes afirmaciones es verdadera para la solución óptima de un problema de PL?

* a) Todo programa lineal tiene una solución óptima.  
* b) Si un PL es factible entonces debe tener al menos una solución óptima.  
* c) La solución óptima utiliza todos los recursos disponibles.  
* d) La solución óptima se encuentra en por lo menos un vértice.  
* e) Si en la solución óptima incluye alguna variable artificial, el problema es No Factible.

**Pregunta 14:**  
En un Programa Lineal no acotado (indique cuál/es afirmaciones son verdaderas):

* a) Al menos una de las restricciones no puede ser satisfecha.  
* **b) La función objetivo puede moverse tan lejos como se desee en la dirección de optimización y todavía tocar al menos un punto del conjunto factible.** *(Respuesta marcada)*  
* c) En la solución óptima queda una variable artificial con un valor \> 0\.  
* d) La región factible es un poliedro abierto.  
* **e) Al menos una variable de decisión se puede hacer tan grande como se desee sin dejar la región factible.** *(Respuesta marcada)*

**Pregunta 15:**  
Indica si las siguientes afirmaciones son Verdaderas o Falsas:

1. El supuesto de divisibilidad en la PL expresa que el valor de la función objetivo debe ser divisible a cualquier nivel fraccionario. **Respuesta marcada: Falso**  
2. En un problema de minimización, el valor de zj puede interpretarse como el costo de producir una unidad de la variable no básica xj.  
3. Aun cuando los programas no lineales son más difíciles que los programas lineales, es verdad que se puede aplicar en ellos la técnica de búsqueda en los vértices para encontrar una solución óptima. **Respuesta marcada: Falso**  
4. El multiplicador de Lagrange es igual al precio sombra en cuanto a su rango de aplicación, pero difieren la interpretación matemática.

**Pregunta 16:**  
Indica si las siguientes afirmaciones son Verdaderas o Falsas y justifica:

1. En un problema de minimización, si la variable xj ingresa a la base, los nuevos valores de las variables básicas se calculan como: λi \- Θ λij. **Respuesta marcada: Verdadero**  
2. En un Programa Lineal no acotado al menos una de las restricciones no puede ser satisfecha. **Respuesta marcada: Falso**  
3. Si un PL es factible siempre la solución óptima se encuentra en un vértice. **Respuesta marcada: Falso**  
4. Un problema de Programación Lineal es degenerado cuando las tasas de sustitución de la variable que entra a la base son todas \<= 0\.

---

## **Segundo Parcial**

**Pregunta 1:**  
Un pronóstico de ventas realizado con promedios móviles nos indica el valor de nuestra variable de interés para el siguiente periodo.

* **Verdadero** *(Respuesta marcada)*  
* Falso

**Pregunta 2:**  
Los modelos de pronósticos cualitativos incluyen:

* análisis de regresión.  
* líneas de tendencia.  
* **método Delphi.** *(Respuesta marcada)*  
* modelos de series de tiempo.

**Pregunta 3:**  
¿Cuál de las siguientes no es una componente de una serie de tiempo?

* estacionalidad.  
* **variaciones causales.** *(Respuesta marcada)*  
* tendencia.  
* variaciones aleatorias.

**Pregunta 4:**  
Un modelo de pronósticos que tan solo usa datos históricos para la variable que se pronostica se llama:

* **modelo de series de tiempo.** *(Respuesta marcada)*  
* modelo causal.  
* modelo Delphi.  
* modelo variable.

**Pregunta 5:**  
Si una serie muestra una tendencia, los coeficientes de autocorrelación son generalmente pequeños para varios de los primeros retrasos de tiempo y van creciendo gradualmente, a medida que se incrementa el número de retrasos.

* Verdadero  
* **Falso** *(Respuesta marcada)*

**Pregunta 6:**  
En el suavizamiento exponencial, si desea dar un peso significativo a las observaciones más recientes, entonces la constante de suavizamiento debería ser:

* cercana a 0\.  
* **cercana a 1\.** *(Respuesta marcada)*  
* cercana a 0.5.  
* menor que el error.

**Pregunta 7:**  
¿Cuál de los siguientes puede ser negativo?

* MAD  
* MAPE  
* ECM  
* **Error de pronóstico** *(Respuesta marcada)*

**Pregunta 8:**  
Una ecuación de tendencia es una ecuación de regresión en la cual:

* existen múltiples variables independientes.  
* la intersección y la pendiente son iguales.  
* la variable dependiente es el tiempo.  
* **la variable independiente es el tiempo.** *(Respuesta marcada)*

**Pregunta 9:**  
Es conveniente usar el modelo determinista con rupturas cuando:

* a. El costo unitario de almacenamiento es igual a cero.  
* b. El costo del almacenamiento es más del doble que el costo de rupturas.  
* **c. Se puede trabajar con una política de pedidos pendientes.** *(Respuesta marcada)*  
* d. El costo unitario de rupturas es mayor al costo unitario de almacenamiento.  
* e. El costo total de las rupturas es igual a cero.

**Pregunta 10:**  
En programación y Control de Proyectos, el método PERT con referencia a la duración total del proyecto supone que:

* a. Supone que las duraciones de las actividades son estadísticamente independientes.  
* b. La duración de las actividades se presenta dentro de un intervalo cerrado.  
* c. Requiere conocer la varianza de la duración de todas las actividades del proyecto.  
* d. Requiere conocer la desviación estándar de la duración de todas las actividades del proyecto.  
* e. Supone que la duración de las actividades se puede estimar con una distribución Uniforme.  
* f. Supone que la duración de las actividades se puede estimar con una distribución Normal.

**Pregunta 11:**  
Para un problema de transporte que tiene 4 orígenes y 5 destinos y la demanda es mayor que la oferta, la cantidad de variables nulas que tendrá una solución factible básica no degenerada es:

* a. 16 (dieciseis)  
* b. 8 (ocho)  
* c. 9 (nueve)  
* d. 5 (cinco)  
* e. 7 (siete)  
* f. 10 (diez)

**Pregunta 12:**  
Es conveniente usar el modelo determinista sin rupturas cuando:

* **a. El costo unitario de rupturas es mayor al costo unitario de almacenamiento.** *(Respuesta posible indicada)*  
* b. El costo unitario de almacenamiento es igual a cero.  
* c. El costo total de las rupturas es igual a cero.  
* d. Ninguna respuesta es correcta.  
* e. El costo de almacenamiento es mucho menor al costo de rupturas.

**Pregunta 13:**  
En la comparación entre los modelos de transporte con asignación, transbordo y flujo máximo, diga cuál de las siguientes afirmaciones es VERDADERA:

* a. La diferencia entre los problemas: flujo máximo y transbordo, es que en el segundo los arcos no tienen capacidad.  
* b. Las variables de todos los problemas de redes de flujo son enteras.  
* c. La única diferencia entre el problema de transporte y el de asignación es que en el primero la cantidad de orígenes puede ser diferente a la cantidad de destinos.  
* d. En los problemas, transbordo y flujo, lo que entra a cada nodo debe ser igual a lo que sale.  
* e. El valor de la variable xij en la función objetivo del problema de transporte representa el costo de enviar una unidad desde el origen i hacia el destino j.  
* f. Los modelos de transporte y el de asignación se equilibran agregando un origen o un destino ficticio.

**Pregunta 14:**  
Cuáles de las siguientes afirmaciones es verdadera para el lote óptimo del modelo de stock con Reabastecimiento Uniforme:

* a. Ninguna respuesta es completamente correcta.  
* b. El costo total del almacenamiento es menor al costo total de pedir debido a que el tamaño de q\* es mayor que en el modelo CEP.  
* c. El costo total del almacenamiento es mayor al costo total de pedir debido a que el tamaño de q\* es mayor que en el modelo CEP.  
* d. El costo total de pedir es mayor al del modelo CEP.  
* e. El costo total del almacenamiento es menor al del modelo CEP.

**Pregunta 15:**  
¿Cuál de las siguientes afirmaciones es correcta respecto al Modelo con Descuentos por Compras en Cantidad?

* a. El costo unitario de almacenamiento siempre depende del precio del producto.  
* b. Si el lote óptimo está incluido en el intervalo de cantidades más altas, no es necesario que el costo total coincide con el modelo CEP.  
* c. Ninguna de las afirmaciones es completamente correcta.  
* d. La función de costo total coincide con la del Modelo sin ruptura cuando el óptimo se alcanza con el precio más bajo.  
* **e. La función de costo total es igual a la del Modelo sin ruptura excepto en la estructura del costo unitario de almacenamiento.** *(Respuesta marcada)*

**Pregunta 16:**  
En una red con n nodos, el objetivo del algoritmo de Dijkstra es:

* a. Encontrar una red con n-1 ligaduras que conecte a todos los nodos y sea de valor mínimo.  
* b. Encontrar un camino de valor mínimo con n-1 ligaduras que una al nodo origen con el nodo destino.  
* c. Conectar todos los nodos de una red.  
* **d. Encontrar los caminos de valor mínimo entre un nodo marcado como origen y cada uno de los otros vértices de la red.** *(Respuesta marcada)*

**Pregunta 17:**  
En administración de Inventarios, cuál de las siguientes afirmaciones es correcta:

* a. Si la tasa de demanda disminuye la periodicidad de los pedidos disminuye proporcionalmente.  
* **b. Si la tasa de demanda aumenta la periodicidad de los pedidos se mantiene constante.** *(Respuesta marcada en una variante)*  
* c. No se puede saber sin calcularlo.  
* d. La cantidad de días que transcurre entre pedidos es inversamente proporcional a la tasa de demanda.

**Pregunta 18:**  
Dado el siguiente grafo:  
Seleccione la/las opciones correcta/s:

* **a. Hay caminos orientados** *(Respuesta marcada)*  
* **b. Es no conexo** *(Respuesta marcada)*  
* c. Hay bucles  
* d. Hay ciclos

**Pregunta 19:**  
En el modelo con rupturas, si el costo de cada unidad de ruptura se incrementa, el periodo durante el cual existe inventario (t2):

* a. no se puede saber sin calcularlo  
* **b. disminuye** *(Respuesta marcada)*  
* c. aumenta  
* d. no tiene influencia

**Pregunta 20:**  
Para un problema de transporte que tiene 6 orígenes y 4 destinos y la oferta es mayor que la demanda, la cantidad de variables nulas que tendrá una solución factible básica no degenerada es:

* a. 7 (siete)  
* b. 8 (ocho)  
* c. 12 (doce)  
* d. 10 (diez)  
* **e. 20 (veinte)** *(Respuesta marcada)*  
* f. 5 (cinco)

**Pregunta 21:**  
Es conveniente usar el modelo determinista sin rupturas cuando:

* **a. No es posible dejar demanda insatisfecha.** *(Respuesta marcada)*  
* b. Ninguna respuesta es correcta.  
* c. El costo unitario de rupturas es mayor al costo unitario de almacenamiento.  
* d. El costo total de las rupturas es igual a cero.  
* e. El costo unitario de almacenamiento es igual a cero.

**Pregunta 22:**  
En programación y control de proyectos, el método PERT con referencia a la duración total del proyecto supone que:

* a. Los recursos asignados para la realización de las actividades se pueden medir monetariamente  
* **b. Supone que las actividades críticas serán las identificadas usando las duraciones esperadas** *(Respuesta marcada)*  
* c. La duración de las actividades se presenta dentro de un intervalo cerrado  
* d. Dentro del rango de duraciones posibles, el costo de la actividad se incrementa linealmente a medida que la duración disminuye  
* e. Se supone que la duración de las actividades se puede estimar con una distribución uniforme  
* f. Supone que la duración de las actividades se puede estimar con una distribución normal

**Pregunta 23:**  
El modelo de PL de un problema de transbordo equilibrado que tiene 4 nodos de oferta, 4 nodos de demanda, 5 nodos de transbordo y 15 ligaduras, tendrá:

* a. 8 variables  
* b. 15 variables  
* c. 13 variables  
* **d. Ninguna respuesta es completamente correcta** *(Respuesta marcada)*  
* e. 8 restricciones  
* f. 15 restricciones

**Pregunta 24:**  
En una red CPM, el camino crítico:

* **a. Determina la duración mínima de un proyecto** *(Respuesta marcada)*  
* b. Determina la duración máxima de un proyecto  
* c. Determina el tiempo máximo esperado de un proyecto  
* d. Ninguna respuesta es completamente correcta  
* e. Determina la duración mínima esperada de un proyecto

**Pregunta 25:**  
En el modelo con rupturas, si el costo de cada unidad almacenada disminuye, el periodo durante el cual existe inventario (t2):

* a. no tiene influencia  
* b. no se puede saber sin calcularlo  
* c. disminuye  
* **d. aumenta** *(Respuesta marcada)*

**Pregunta 26:**  
Cuáles de las siguientes afirmaciones es verdadera:

* a. La ligadura seleccionada en cada paso del algoritmo de árbol de expansión mínimo cumple con la propiedad de ser la de menor valor que permite disminuir la cantidad de elementos del conjunto de nodos conectados.  
* b. El camino de valor mínimo en una red con n vértices, tendrá n-1 ligaduras que unen el nodo inicio con el nodo fin.  
* **c. Ninguna respuesta es correcta.** *(Respuesta marcada)*  
* d. En los algoritmos para encontrar la ruta de menor valor, la ligadura seleccionada en cada paso debe proporcionar una trayectoria entre el nodo origen y el nodo fin.  
* e. Si al utilizar el algoritmo del árbol de expansión mínima para conectar n nodos se encuentra una red resultante con n-2 ligaduras y otra con n-1 ligaduras pero ambas con el mismo valor mínimo es indiferente seleccionar cualquiera de ellas para identificar al árbol de expansión mínima.

**Pregunta 27:**  
Para un problema de transporte que tiene 5 orígenes y 2 destinos y la demanda es mayor que la oferta, la cantidad de variables positivas que tendrá una solución factible básica no degenerada es:

* **a. 7 (siete)** *(Respuesta marcada)*  
* b. 5 (cinco)  
* c. 15 (quince)  
* d. 8 (ocho)  
* e. 10 (diez)  
* f. 12 (doce)

**Pregunta 28:**  
En la comparación entre los modelos de transporte con asignación, transbordo y flujo máximo, diga cuál de las siguientes afirmaciones es VERDADERA:

* a. La única diferencia entre el problema de transporte y el de asignación es que en el primero la cantidad de orígenes puede ser diferente a la cantidad de destinos.  
* b. Los modelos de transporte y el de asignación se equilibran agregando un origen o un destino ficticio.  
* c. La diferencia entre los problemas: flujo máximo y transbordo, es que en el segundo los arcos no tienen capacidad.  
* **d. En los problemas equilibrados de transporte y de asignación la cantidad de variable se calcula como número de nodos origen por número de nodos destino.** *(Respuesta marcada)*  
* e. Las variables de todos los problemas de redes de flujo son enteras.  
* f. El valor de la variable xij en la función objetivo del problema del transporte representa el costo de enviar una unidad desde el origen i hacia el destino j.  
* **g. En el problema del flujo máximo, al igual que en el de transbordo, se tienen tres tipos de nodos.** *(Respuesta marcada en otra variante)*

**Pregunta 29:**  
En Programación y Control de Proyectos, el método PERT con referencia a las duraciones de las actividades supone que:

* a. Supone que la varianza de la duración de las actividades se calcula como la amplitud en la duración de la actividad divido en seis.  
* b. Supone que la duración de las actividades se puede estimar con una distribución Normal.  
* c. Supone que las duraciones de las actividades son estadísticamente independientes.  
* d. Requiere conocer la varianza de la duración de todas las actividades del proyecto.  
* e. Supone que la duración de las actividades se puede estimar con una distribución Uniforme.  
* **f. La duración de las actividades se puede describir a través de una función unimodal.** *(Respuesta Correcta)*

**Pregunta 30:**  
Indique si es Verdadero o Falso:  
Los pronósticos cualitativos se utilizan bajo el supuesto de que los patrones de comportamiento de la variable analizada son cambiantes.

* **Falso** *(Respuesta marcada)*

**Pregunta 31:**  
En una red con n nodos, el objetivo del algoritmo de árbol de expansión mínima...

* a) Conectar todos los nodos de una red  
* b) Encontrar un camino de valor mínimo entre un nodo marcado como origen y cada uno de los otros vértices de la red  
* c) Encontrar un camino de valor mínimo con n-1 ligaduras que una al nodo origen con el nodo destino  
* **d) Encontrar una red con n-1 ligaduras que conecte a todos los nodos y sea de valor mínimo** *(Respuesta marcada)*  
* e) Ninguna respuesta es correcta.

---

## **Examen Final**

**Pregunta 1:**  
Dado un problema de PL de maximización, explica el significado de la tasa de sustitución λij \= \-2 y de zj \= 50, donde tanto i como j identifican a variables de decisión.

**Pregunta 2:**  
Dada una red, defina:

* Árbol de expansión  
* Árbol de expansión mínima

**Pregunta 3:**  
En una red con n nodos, el objetivo del algoritmo de Dijkstra es:

* a) Encontrar un camino con la mínima cantidad de arcos que conecte a un nodo marcado como origen y cada uno de los otros nodos de la red.  
* b) Encontrar una red con n-1 ligaduras que conecte a todos los nodos y sea de valor mínimo.  
* **c) Encontrar los caminos de valor mínimo entre un nodo marcado como origen y cada uno de los otros nodos de la red.** *(Respuesta marcada)*  
* d) Encontrar un camino de valor mínimo con n-1 ligaduras que una al nodo origen con el nodo destino.  
* e) Conectar todos los nodos de una red con la menor cantidad de arcos.

