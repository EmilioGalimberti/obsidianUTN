---
aliases:
  - DSI - PARCIAL2 - UNIDAD02&03 REQUERIMIENTOS NO FUNCIONALES
subject: DSI
year: "3"
exam: PARCIAL2
unit: 2,3
type: TEO
zk_type: permanent
status: done
date: 2026-07-23
tags:
source:
  - "[[DSI-Parcial2-TEO-U02&U03- Req No Fun]]"
---
---
**Recordatorio de que eran los REQUERIMIENTOS:**
* *Requerimiento funcional* se centran en el que → y no teníamos que tener en cuenta en el como (en cuanto tecnología)
* *Requerimientos no funcionales* el como → nos referimos a la parte tecnológica de implementación

# Normas de calidad ISO/IEC 25000
Es una familia de normas cuyo objetivo principal es guiar el desarrollo de los productos de software mediante
* Especificación de requisitos de calidad
* Evaluación de características de calidad

**Nosotros nos basamos en la familia 25010**
Define un modelo de Calidad de producto, el cual determina características de calidad que se deben tener en cuenta al evaluar las propiedades de un producto de software

![[Pasted image 20260803175937.png]]

![[esquema-iso25010.excalidraw]]
## Adecuación funcional -> No va en diseño
Adecuación funcional: el grado con el cual un producto o un sistema provee funciones que cumplen con necesidades establecidas e implícitas cuando son utilizadas bajo condiciones específicas. o Completitud funcional: el grado con el cual un conjunto de funciones cubre todas las tareas especificadas y los objetivos de los usuarios. o Corrección funcional: el grado con el cual un producto o sistema provee los resultados correctos con el grado de precisión necesaria. o Pertinencia funcional: el grado con el cual las funciones facilitan la realización de tareas y funciones específicas.

## Eficiencia de Desempeño
Desempeño relativo a la  cantidad de recursos utilizados bajo determinadas condiciones establecidas

* Comportamiento Temporal: Tiempos de repuesta cuando se ejecutan sus funciones
	* *La consulta de disponibilidad de la habitación deber llevar no mas de 20 minutos*
* Utilización de recursos: La cantidad de recursos disponibles a la hora de ejecutar sus funciones
	* *El Acceso a la BD en forma concurrente debe soportar al menos 40 puestos de trabajo*
* Capacidad:  Limites máximos de parámetros (almacenamiento, usuarios concurrentes, ancho de banda)
	* *El tamaño máximo de archivo imagen a subir es de 2GB*
## Compatibilidad
el grado con el que sistema puede intercambiar información con otros sistemas ejecutando sus funciones requeridas mientras comparte el mismo hardware o entorno operativo.

* Coexistencia: El sistema deberá ser capaz de compartir recursos con otros sistemas sin deteriorar el rendimiento 
	* *El sistema de gestión comercial deberá acceder a la misma BD que el sistema contable*
* Interoperabilidad: La capacidad de dos o mas sistemas, intercambia y utilizar información entre ellos
	* *El sistema tomara los datos de E/S del personal del sistema de registro de asistencias*

## Usabilidad
Capacidad del sistema para ser entendido, aprendido, usado y resultar atractivo para e usuario, cuando se usa bajo determinadas condiciones

* Reconocimiento de corrección: El usuario es capaz de reconocer que el sistema es apropiado para sus necesidades, esto depende de impresión inicial y de la documentación asociada al producto o sistema
* Aprendizaje: entiendo que es que el sistema sea fácil de aprender a usar por usuarios específicos
* Operabilidad: La facilidad de un sistema de ser utilizado
* Protección frente a errores del usuario
* Estética
* Accesibilidad

## Fiabilidad
el grado con el cual un sistema ejecuta funciones específicas bajo determinadas condiciones por un período de tiempo determinado.

* Madurez: El sistema no falla durante una operación normal
* Disponibilidad: el sistema esta disponible cuando es requerido
* Tolerancia a fallas: como el sistema opera a pesar de fallas en software o hardware
* Capacidad de recuperación: El sistema puede restaurar la información afectada y restablecer el estado deseado del sistema
## Seguridad
el grado con el cual un sistema protege información y datos de personas o sistemas que tienen el grado de acceso a datos apropiado a sus tipos y niveles de autorización. La seguridad aplica tanto a datos guardados como a datos transmitidos.

CIA TRAID
* Confidencialidad
* Integridad
* No repudio: logs de eventos dentro del sistema
* Autenticidad
* Responsabilidad _el grado con el cuál una acción de una entidad puede trazarse unívocamente hacia esa entidad_

**IMPORTANT**
Agregaría **Responsabilidad** (o _Accountability_) a la sección de Seguridad. Es distinta al No Repudio: mientras el no repudio prueba que un evento ocurrió, la responsabilidad permite rastrear quién ejecutó cada acción.
## Mantenibilidad
Representa la capacidad de un sistema para ser modificado efectivamente y eficientemente

* Modularidad: cuando un sistema esta compuesto por componentes, de manera que el cambio en uno de ellos tiene impacto mínimo en el resto
* Reusabilidad: el grado con el cual un activo puede ser utilizado en más de un sistema o en la construcción de otros activos. Activo refiere a cualquier software o hardware caracterizado por sus atributos y su relación con otros activos. Por ejemplo, un componente de código es un activo, el cual puede ser reusado en diferentes módulos o aplicaciones.
* Capacidad de ser analizado:  Cuando un sistema es capaz de ser analizado para ser modificado en una o varias partes
* Capacidad de ser modificado: 
* Capacidad de ser probado: si se pueden crear test para un sistema, y pueden ser ejecutadas para establecer si los criterios se cumplen
## Portabilidad
Capacidad del sistema de ser transferido de forma efectiva y eficiente de un entorno hardware, software, etc.

* Adaptabilidad: el grado con el cual un producto o sistema puede ser efectiva y eficientemente adaptado para otros hardware, software o entornos operacionale
* Facilidad de instalación: sistema puede ser instalado o desinstalado exitosamente en determinado entorno.
* Capacidad de ser reemplazado: el grado con el cual un producto puede reemplazar otro producto de software específico con el mismo propósito y en el mismo entorno.



---

# TRADE-OFFS
> **Al tener más de un RNF crítico, comienzan los conflictos:**
> 1. Si quiero tener buen **desempeño**, tengo componentes de granularidad alta que afectan la **mantenibilidad**
> 2. Si introduzco **datos redundantes**, mejora la **disponibilidad**, pero hago más compleja la **seguridad**
> 3. La localización de aspectos de **seguridad** relacionados significa más comunicación, es decir, peor **desempeño**

WARNING

Este punto de los **trade-offs/conflictos entre atributos de calidad** es conceptualmente muy importante para un parcial. Es el tipo de pregunta que suelen hacer para evaluar comprensión profunda (ej: _"¿Qué conflicto puede surgir entre desempeño y mantenibilidad?"_).

# Ejemplo DE RNF
![[Pasted image 20260803180011.png]]
![[Pasted image 20260803180027.png]]
# References
## Father
[[DSI-Parcial2-TEO-U02&U03- Req No Fun]]
## child