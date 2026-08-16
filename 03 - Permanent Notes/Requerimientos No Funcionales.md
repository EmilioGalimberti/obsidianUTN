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
* *Requerimiento funcional* se centran en el que hace el sistema→ y no teníamos que tener en cuenta en el como (en cuanto tecnología)
* *Requerimientos no funcionales* el como debe comportarse bajo determinadas restricciones → nos referimos a la parte tecnológica de implementación

Los RNF son los verdaderos **conductores o motores de la arquitectura** (_architectural drivers_). Las decisiones estructurales más difíciles de cambiar se toman específicamente para dar respuesta a los RNF críticos:
- Un requerimiento crítico de **Desempeño** sugiere componentes de granularidad gruesa (para reducir la sobrecarga de la comunicación remota).
- Un requerimiento crítico de **Seguridad** sugiere una arquitectura organizada en capas estrictas con altos niveles de validación interna.
- Un requerimiento crítico de **Disponibilidad** sugiere el uso de infraestructura con redundancia física y bases de datos espejo (_shadow_).

# TRADE-OFFS
El arquitecto raramente se enfrenta a un escenario ideal. **Muchos RNF entran en conflicto directo entre sí**, lo que obliga a tomar decisiones de compromiso (_trade-offs_) para buscar soluciones mediadoras

+Desempeño: numero reducido de subsistemas, grano grueso (-disponibilidad, -mantenibilidad)

+Seguridad: estructura en capas, alto nivel de validación (-desempeño, -mantenibilidad)

+Protección: las operaciones de protección se localicen en un solo subsistema o pocos (-disponibilidad, -desempeño)

+Mantenibilidad: debo tener componentes de grano fino que puedan modificarse con facilidad (-desempeño, -disponibilidad)

+Disponibilidad: debe incluir componentes redundantes para poder actualizar los componentes sin detener el sistema (-desempeño, -mantenibilidad)

---
Trade-off

- **Desempeño (Performance) vs. Mantenibilidad:** Si se utilizan **componentes de granularidad alta** (gruesa), el **rendimiento** del sistema puede **mejorar**, ya que se reduce la comunicación entre subsistemas. Sin embargo, esto a su vez **reduce la mantenibilidad**,  haciendo que el sistema sea más difícil de corregir o modificar.
- **Disponibilidad vs. Seguridad:** La **introducción de datos redundantes** puede **mejorar la disponibilidad** del sistema, asegurando que la información esté accesible incluso si un componente falla. No obstante, esta redundancia puede hacer que la **seguridad sea más compleja**, ya que hay más puntos que proteger y asegurar.
- **Seguridad vs. Desempeño (Performance):** La **localización de aspectos relacionados con la seguridad**, como la adición de más capas de validación o protección, generalmente implica **más comunicación** dentro del sistema. Esta comunicación adicional **degrada el desempeño** general, haciendo que el sistema sea más lento.

Estos conflictos demuestran que es imposible optimizar todos los atributos de calidad simultáneamente, y el trabajo del arquitecto es gestionar estas compensaciones.




# 4. Priorización en Ciclos Iterativos
En el Proceso Unificado de Desarrollo (PUD), el arquitecto debe clasificar los RNF significativos para la arquitectura en tres prioridades:

1. **Prioridad Alta:** RNF críticos que condicionan la arquitectura desde la primera iteración. Postergarlos causaría un costoso retrabajo técnico (ej. si el sistema debe operar en dispositivos móviles, la tecnología base debe soportarlo desde el día uno).
2. **Prioridad Media:** Deben ser soportados eventualmente en el ciclo de desarrollo, pero no obligatoriamente en el primer lanzamiento ejecutable.
3. **Prioridad Baja:** Peticiones deseables ("lista de deseos") que no guían activamente las decisiones de diseño arquitectónico.
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

* Coexistencia: Capacidad de compartir recursos de hardware y software con otros programas en el mismo entorno
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

# Ejemplo DE RNF
![[Pasted image 20260803180011.png]]
![[Pasted image 20260803180027.png]]




# Vinculación de los RNF con la Funcionalidad (Casos de Uso)
Un error conceptual común es pensar que los RNF se resuelven de forma abstracta en "el aire". En el software real, **los RNF siempre se implementan y validan a través de la funcionalidad**. Por ello, el arquitecto construye la **[[Vista_Arquitectonica_de_la_funcionalidad]]**, seleccionando el conjunto más pequeño posible de casos de uso representativos que muestren cómo se resuelven los RNF críticos del negocio:

- El RNF de **"Autenticación de usuarios"** se implementa y visualiza en el caso de uso _Iniciar sesión_.
- El RNF de **"Seguimiento en línea mediante GPS"** se materializa en el caso de uso _Visualizar mapa de entregas_.
- El RNF de **"Procesamiento masivo"** (ej. lotes de cobro offline) se implementa en el caso de uso _Procesar comprobantes de cobro offline_.

# Preguntas de parcial
https://app.notion.com/p/Resumen-por-preguntas-25a93f1051dc803aa8e8f246251e2f70
2- Explique que son los requerimientos no funcionales, que dificultades encontramos asociadas a los requerimientos no funcionales a la hora de diseñar software y como impactan en el modelado de la arquitectura. (pregunta de meles xd)

Conflictos entre RNF:Proporcione ejemplos de cómo diferentes RNF pueden entrar en conflicto (3).