---
aliases:
  - DSI - PARCIAL2 - UNIDAD02&03 REQUERIMIENTOS NO FUNCIONALES
subject: DSI
year: "3"
exam: PARCIAL2
unit: 2,3
type: TEO
zk_type: permanent
status: in progress
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

## Adecuación funcional -> No va en diseño

## Eficiencia de Desempeño
La cantidad de recursos utilizados bajo determinadas condiciones establecidas

* Comportamiento Temporal: Tiempos de repuesta cuando se ejecutan sus funciones
	* *La consulta de disponibilidad de la habitación deber llevar no mas de 20 minutos*
* Utilización de recursos: La cantidad de recursos disponibles a la hora de ejecutar sus funciones
	* *El Acceso a la BD en forma concurrente debe soportar al menos 40 puestos de trabajo*
* Capacidad:  Limites máximos de parámetros (almacenamiento, usuarios concurrentes, ancho de banda)
	* *El tamaño máximo de archivo imagen a subir es de 2GB*
## Compatibilidad
el grado con el que un producto, sistema o componente puede intercambiar información con otros productos, sistemas o componentes, ejecutando sus funciones requeridas mientras comparte el mismo hardware o entorno operativo.
## Usabilidad
## Confiabilidad
## Seguridad
## Mantenibilidad
## Portabilidad

![[esquema-iso25010.excalidraw]]

---
# References
## Father
[[DSI-Parcial2-TEO-U02&U03- Req No Fun]]
## child