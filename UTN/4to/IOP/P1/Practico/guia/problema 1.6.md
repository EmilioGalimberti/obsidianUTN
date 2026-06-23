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

> [!note] Restricciones de Igualdad Estricta En un [[Modelo de Transporte]] equilibrado, las inecuaciones se transforman en ecuaciones. Las plantas envían exactamente todo lo que producen (incluida la planta ficticia) y las ciudades reciben exactamente todo lo que demandan, formulándose todas las restricciones con el signo de igualdad ($=$).
