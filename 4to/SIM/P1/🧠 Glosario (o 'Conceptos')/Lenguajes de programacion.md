# lenguaje de proposito general vs especificos de sim

vs

| ==pros proposito general==                            | contra sespecificos de sim                                |
| ----------------------------------------------------- | --------------------------------------------------------- |
| 1. ==No hay restriciones para el formato de salida==  | 1. Poca Diversidad en el formato de salida                |
| 2. Por lo general se ==conoce muy bien el lenguaje==  | 2. Conocomiento del lenguaje                              |
| 3. ==Menor costo del software==                       | 3. Costo del sofware                                      |
| 4. ==Flexibilidad== para adaptarse a cualquier modelo | 4. Limitada flexibilidad para adaptarse a cualquer modelo |
| 5. ==Tiempo de ejecucion reducido==                   | 5. Tiempo de ejecucion incrementado                       |

vs

| contras proposito general                                                                            | ==Pros especificos de sim==                                                                    |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 1.  Es necesario desarrollar las funcionalidades requeridas para construir un modelo                 | 1.==Brindan la mayoria de las funcionalidades== necesarias para constuir un modelo             |
| 2. Es más laboriosa la generación de datos necesarios para la simulación                             | 2. ==Generacion automatica de ciertos datos== necesarios                                       |
| 3. Es más laboriosa la administración y asignación de recursos de la computadora, durante la corrida | 3. ==Recopilacion y despliegue de los datos producidos==                                       |
| 4. Se necesita gestionar la recopilación y despliegue de los datos producidos                        | 4. ==Control de administracion y asignacion de recuros de la computadora, durante la corrida== |
|                                                                                                      | --                                                                                             |
|                                                                                                      | 5.Los modelos son generalmente más fáciles de modificar y mantener.<br>                        |
|                                                                                                      | 6.Los modelos son menos propensos a errores.                                                   |
|                                                                                                      | 7.Tiempo de programación más corto. (puede incidir en el costo total del proyecto).            |
![[{428DD1CE-3012-416B-988C-7F9E8F83DEF9}.png]]

Lenguajes de Propósito General: Como Python o Java. Brindan formato de salida libre, son bien conocidos, sus corridas son más rápidas y no limitan al desarrollador, pero exigen que todo se programe desde cero.
* Ventajas de los lenguajes de propósito general:
	* Formatos libres: No hay restricciones para el formato de salida de los datos, lo que otorga total libertad al desarrollador.
	* Familiaridad: Por lo general, se conoce muy bien el lenguaje gracias a la formación universitaria o profesional previa.
	* Menor costo de software: Representan un menor costo inicial en licencias en comparación con los lenguajes de simulación, aunque esto no siempre se traduce en un menor costo total del proyecto.
	* Gran flexibilidad: Permiten construir diversos modelos sin encasillarse en una rama específica, lo cual suele ocurrir con las herramientas especializadas de simulación.
	* Velocidad: Suelen ofrecer un menor tiempo de ejecución al momento de realizar las corridas.

Lenguajes Específicos de Simulación: Generan los datos estadísticos solos, administran automáticamente la memoria de la computadora y son más rápidos para estructurar y mantener, aunque limitan los formatos visuales y su software es más costoso.
* Ventajas de los lenguajes de simulación:
	* Funcionalidades nativas: Proveen la mayoría de las funcionalidades necesarias para construir el modelo, evitando tener que programar toda la infraestructura estadística y de eventos desde cero.
	* Gestión de datos: Generan automáticamente datos necesarios y facilitan enormemente la recopilación y el despliegue de los resultados producidos.
	* Administración eficiente de memoria: Controlan internamente el almacenamiento y los recursos de la computadora, evitando que el sistema se quede sin memoria o se trabe durante corridas muy largas.
	* Facilidad de modificación: Los modelos son más fáciles de modificar y de mantener. Añadir un nuevo componente a menudo es tan simple como agregar un ícono y asignarle una distribución estadística.
	* Rapidez y fiabilidad: Al estar pre-armados, el tiempo de programación es notablemente más corto y el modelo final es menos propenso a tener errores de programación, lo que puede llegar a compensar el alto valor de su licencia de software.