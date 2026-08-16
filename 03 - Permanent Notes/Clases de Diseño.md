---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit:
type: TEO
zk_type: permanent
status: done
date: 2026-08-16
source:
tags:
---
---
Las clases de diseño son clases cuyas especificaciones se han completado hasta tal nivel que se pueden implementar. Es una abstracción de una clase o construcción similar en la implementación del sistema.
* Son especificadas mediante un lenguaje de programación. 
* Se especifican las operaciones, parámetros, atributos, tipos utilizando la sintaxis del lenguaje de programación elegido.
* Se especifican con frecuencia la visibilidad de los atributos y operaciones. (public, protected, private)
* Las relaciones de las clases de diseño con otras clases tienen un significado directo cuando la clase es implementada. Por ej, la generalización se corresponde con la herencia en el lenguaje de programación.
* Los métodos (realizaciones de operaciones) de una clase de diseño, tienen correspondencia directa con el correspondiente método en la implementación de las clases (en el código). 
* En el diseño los métodos suelen especificarse con lenguaje natural o pseudocódigo y esto puede usarse como comentarios en el código.
* Una clase de diseño puede posponer el manejo de algunos requerimientos para las subsiguientes actividades de implementación, indicándolos como requerimientos de implementación de la clase.
* Una clase de diseño aparece como un estereotipo que se corresponde con una construcción en el lenguaje de programación dado. Por ejemplo, una clase de diseño para una aplicación en visual basic podría estereotiparse como un form.
* Una clase de diseño puede realizar (y por tanto, proporcionar) interfaces, si tiene sentido hacerlo en el lenguaje de programación.
* Una clase de diseño puede activarse, implicando que objetos de la clase mantengan su propio hilo de control y se ejecuten concurrentemente con otros objetos activos.
 

Las clases de diseño provienen de dos lados:
* El ámbito del problema vía una mejora de las clases de análisis: a las clases de análisis se le añaden detalles de implementación.
* El ámbito de la solución: es el ámbito de librerías de clases de utilidad y componentes reutilizables (Time, Date, String, colecciones, middleware, frameworks, etc.). 
 
En las clases de diseño hay que especificar: atributos (nombre, tipo, visibilidad y opcionalmente un valor predeterminado), operaciones o métodos (nombre, parámetros con tipo y tipo de retorno). Esto además sirve para generar código que después les servirá a los programadores.

Cuatro características que debe tener una clase de diseño para que se considere bien diseñada:
* Completa y suficiente: proporciona a los clientes lo que se espera de ella y contiene el conjunto esperado de operaciones y nada más.
* Sencilla: ofrece un solo servicio sencillo. A veces se “relaja” un poco por cuestiones de rendimiento.
* Alta cohesión: tiene un pequeño número de responsabilidades que están íntimamente relacionadas. Son fáciles de entender y mantener, y son reutilizables.
* Bajo acoplamiento: debería asociarse con clases si solamente tienen vínculo semántico entre ellas.




---
