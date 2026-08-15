---
subject: DSI
year: "3"
exam: PARCIAL2
unit: 2,3
type: TEO
zk_type: fleeting
status: done
date: 2026-07-23
tags:
---
---
# Unidad 2/3: Requerimientos no Funcionales Atributos de Calidad del Software , (clase 2 → catanno)

Esto es mas un repaso para saber identificar mas mejor RNF

<aside>
💡

esta creo que tambien fue virtual, no me acuerdo la verdad creo que la tengo grabada fijarse

[DSI 3K3  - RNF  Atributos de Calidad del Software 2023.pdf](DSI_3K3__-_RNF__Atributos_de_Calidad_del_Software_2023.pdf)

</aside>

esta es la de 2021:

https://www.youtube.com/watch?v=Ue-jhSgi3IE

- recordatorio de requerimeinots
    
    Requerimiento funcional se centran en el que → y no teniamos que tener en cuenta en el como (en cuanto tecnologia)
    
    Requerimientos no funcionales el como → nos referimos a la parte tecnologica de implementacion
    
    ![[Pasted image 20260803160648.png]]
    



- Familia de normas ISO/IEC 25000
    
    nos proporciona una guia para identificar los requerimientos y se basan en la calidad del producto
    
    ![[Pasted image 20260803160735.png]]
    
    hay varias y nostros nos basamos en la del calidad del producto: discribe el modelo de calidad para el producto software
    
    ![[Pasted image 20260803160743.png]]
    

![[Pasted image 20260803160753.png]]

- adecuacion funcilan no va en diseño (ya la vimos antes en asi)
    
    Adecuación funcional: el grado con el cual un producto o un sistema provee funciones que cumplen con necesidades establecidas e implícitas cuando son utilizadas bajo condiciones específicas.
    o Completitud funcional: el grado con el cual un conjunto de funciones cubre todas las tareas especificadas y los objetivos de los usuarios.
    o Corrección funcional: el grado con el cual un producto o sistema provee los resultados correctos con el grado de precisión necesaria.
    o Pertinencia funcional: el grado con el cual las funciones facilitan la realización de tareas y funciones específicas.
    
- Eficiencia de Desempeño
    
    desempeño relativo a la cantidad de recursos utilizados bajo determinadas
    condiciones establecidas. (Recursos: productos de software, configuraciones de hardware y software del sistema y otros materiales).
    
    o Comportamiento temporal: el grado con el cual la respuesta, los tiempos de procesamiento, tasas de rendimiento de un producto o sistema cuando ejecuta sus funciones cumple con los requerimientos.
    
    ![[Pasted image 20260803160810.png]]
    
    o Utilización de recursos: el grado con el cual las cantidades y los tipos de recursos utilizados por un producto o sistema cuando ejecuta sus funciones cumplen con los requerimientos
    
    ![[Pasted image 20260803160817.png]]
    
    o Capacidad: el grado con el cual los límites máximos de los parámetros de un producto o sistema cumplen con los requerimientos. Los parámetros pueden ser ítems almacenados, usuarios concurrentes, ancho de banda, rendimiento de las transacciones y tamaño de base de datos
    
    ![[Pasted image 20260803160823.png]]
    
- Compatibilidad
    
    el grado con el que un producto, sistema o componente puede intercambiar información con otros productos, sistemas o componentes, ejecutando sus funciones requeridas mientras comparte el mismo hardware o entorno operativo.
    
    o Coexistencia: el grado con el cual un producto puede ejecutar sus funciones requeridas mientras comparte el entorno y los recursos con otros productos sin impactar en detrimento de los otros productos.
    
    ![[Pasted image 20260803160838.png]]
    
    o Inter-operatividad: el grado con el cual dos o más productos, sistemas o componentes puedenintercambiar información y utilizar esa información intercambiada.
    
    ![[Pasted image 20260803160850.png]]
    
    ![[Pasted image 20260803160901.png]]
    
- Usabilidad
    
    el grado con el cual un producto o sistema puede ser utilizado por usuarios específicos para cumplir con sus objetivos con efectividad, eficiencia y satisfacción en un contexto de uso específico.
    
    o Reconocimiento de corrección: el grado con el cual los usuarios pueden reconocer que un producto o sistema es apropiado para sus necesidades. La habilidad de reconocimiento depende de la impresión inicial y de la documentación asociada al producto o sistema.
    
    o Aprendizaje: el grado con el cual un producto o sistema puede ser utilizado por usuarios específicos para cumplir objetivos de aprendizaje establecidos para ejecutar el producto o sistema con efectividad, eficiencia, libre de riesgos y satisfacción en un contexto determinado de uso.
    
    o Operabilidad: el grado con el cual un producto o sistema posee atributos que lo hacen fácil de operar y controlar.
    
    o Protección frente a errores del usuario: el grado con el cual un producto o sistema protege los usuarios de cometer errores.
    
    o Estética: el grado con el cual una interface de usuario permite una interacción placentera y satisfactoria a los usuarios.
    
    o Accesibilidad: el grado con el cual un producto o sistema puede ser utilizado por personas en el sentido amplio de características y capacidades para lograr un objetivo establecido en determinado contexto de uso.
    
- Confiabilidad
    
    el grado con el cual un producto, sistema o componente ejecuta funciones específicas bajo
    determinadas condiciones por un período de tiempo determinado.
    
    o Madurez: el grado con el cual un sistema, producto o componente cumple las necesidades de confiabilidad durante la operación normal.
    
    o Disponibilidad: el grado con el cual un sistema, producto o componente está operativo y accesible cuando es requerido su uso. Externamente, la disponibilidad puede definirse como el porcentaje de tiempo durante el cual el producto, sistema o componente está en condiciones de ser utilizado. También se define como una combinación de madurez (que gobierna la frecuencia de las fallas), la tolerancia a fallas y la capacidad de recuperación (que gobiernan el tiempo que el sistema no está en condiciones de ser utilizado luego de cada falla).
    o Tolerancia a fallas: grado en el que un sistema, producto o componente opera según lo previsto a pesar de fallas en el software o el hardware.
    
    o Capacidad de recuperación: el grado en el cual en un evento de interrupción o falla, un producto o sistema puede restaurar la información afectada y reestablecer el estado deseado del sistema.
    
    ![[Pasted image 20260803160942.png]]
    
- Seguridad
    
    Seguridad: el grado con el cual un producto o sistema protege información y datos de personas o sistemas que tienen el grado de acceso a datos apropiado a sus tipos y niveles de autorización. La seguridad aplica tanto a datos guardados como a datos transmitidos.
    
    o Confidencialidad: el grado con el que un producto o sistema asegura que los datos son accesibles sólo a aquellos autorizados a acceder.
    
    ![[Pasted image 20260803161029.png]]
    
    o Integridad: el grado con el que un producto, sistema o componente previene el acceso no autorizado o modificaciones a un programa de computadoras o datos.
    o No repudio: el grado con el que acciones o eventos pueden ser probados que existieron de manera que esas acciones o eventos no puedan ser luego repudiados.
    o Autenticidad: el grado con el cuál pueda establecerse y demostrarse la identidad de una persona o un recurso.
    o Responsabilidad: el grado con el cuál una acción de una entidad puede trazarse unívocamente hacia esa entidad.
    
- Mantenibilidad
    
    el grado de eficiencia y eficacia con el que un producto o sistema puede modificarse por
    necesidades evolutivas, correctivas o perfectivas. Incluye la instalación de actualizaciones y nuevas versiones. Es la actividad inherente de facilitar las actividades de mantenimiento.
    
    o Modularidad: el grado con el cual un sistema o programa de computadoras está compuesto por componentes discretos de manera que el cambio en uno de sus componentes tiene impacto mínimo en el resto.
    o Reusabilidad: el grado con el cual un activo puede ser utilizado en más de un sistema o en la construcción de otros activos. Activo refiere a cualquier software o hardware caracterizado por sus atributos y su relación con otros activos. Por ejemplo, un componente de código es un activo, el cual puede ser reusado en diferentes módulos o aplicaciones.
    o Capacidad de ser Analizado: el grado de eficiencia o eficacia con el que es posible evaluar el impacto de un producto o sistema que requiere ser modificado en una o varias de sus partes o diagnosticar un producto a cerca de sus fallas y deficiencias o identificar las partes que necesitan ser modificadas
    
    o Capacidad de ser modificado: el grado en el que un producto o sistema puede ser eficiente y eficazmente modificado sin introducir defectos o degradar la calidad actual del producto.
    o Capacidad de ser probado: el grado de eficacia y eficiencia con que los criterios de prueba pueden establecerse para un sistema, producto o componente y las pruebas pueden ejecutarse para establecer si los criterios se cumplen.
    
- Portabilidad
    
    el grado de eficacia y eficiencia con el que un sistema, producto o componente puede ser
    transferido de un hardware, software u otro entorno operativo o de uso a otro
    
    o Adaptabilidad: el grado con el cual un producto o sistema puede ser efectiva y eficientemente adaptado para otros hardware, software o entornos operacionales o usos diferentes o evolucionados. La escalabilidad de las capacidades internas de un software o hardware (por ejemplo, en un motor de base de datos, sus campos, tablas, volumen de transacciones, etc.) establece su adaptabilidad. Si por ejemplo una base de datos fue definida para una cantidad de usuarios, su adaptabilidad está dada por el grado
    en el que se puede hacer crecer esta cantidad de usuarios.
    
    o Facilidad de instalación: el grado de efectividad y eficiencia con el que un producto o sistema puede ser instalado o desinstalado exitosamente en determinado entorno.
    
    o Capacidad de ser reemplazado: el grado con el cual un producto puede reemplazar otro producto de software específico con el mismo propósito y en el mismo entorno.
    

![[Pasted image 20260803161045.png]]

![[Pasted image 20260803161052.png]]

![[Pasted image 20260803161058.png]]

Al tener más de un RNF crítico, comienzan los conflictos:

1. Si quiero tener buen desempeño, tengo componentes de granularidad alta que afectan la
mantenibilidad
2. Si introduzco datos redundantes, mejora la disponibilidad, pero hago más compleja la seguridad
3. La localización de aspectos de seguridad relacionados significa más comunicación, es decir, peor desempeño.




---
# References
## Father
## child
[[Requerimientos No Funcionales]]