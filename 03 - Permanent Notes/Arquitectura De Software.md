---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit: "3"
type: TEO
zk_type: permanent
status: in-progress
date: 2026-08-04
source:
  - "[[DSI-Parcial2-TEO-U03  diseño de arquitectura de software o diseño arquitectonico]]"
tags:
---
---

# Arquitectura de Software
Es el conjunto de decisiones significativas que se toma para satisfacer los requerimientos del sistema, esencialmente los [[Requerimientos No Funcionales]] o atributos de calidad, teniendo el cuenta el contexto y las restricciones de negocio

Es un conjunto de decisiones significativas porque es sobre donde se construirá todo el software, por ello las decisiones arquitectónicas son las mas importantes y difícil de cambiar una vez implementadas

## Características fundamentales de la arquitectura:
* Define la estructura: Como se organizan los componentes
	* divide la aplicación en un conjunto de componentes (módulos, objetos, etc.) y asignarles responsabilidades claras
	* Su objetivo principal es **Minimizar las dependencias** (lograr un [[Bajo Acoplamiento]]) haciendo al sistema fácil de mantener, probar y modificar
* Especifica la Comunicaciones de los componentes: como interactúan los componentes 
	* protocolos y mecanismo mediante los cuales los componentes se comunicaran entre si.
	* Esto se logra  utilizando [[Patrones Arquitectónicos]] (cliente-servidore, publish-suscribe)
	* *Que son los componentes?*
* Aborda los requisitos no funcionales: garantiza que la funcionalidad se entregue cumpliendo con los requisitos de calidad, com el rendimiento, seguridad, capacidad.
* Es una abstracción: provee una  vision simplificada del sistema
	* La arquitectura simplifica y oculta detalles internos para centrarse en las propiedades visibles y sus interacciones. Esto permite que diferentes personas entienda el sistema desde diferentes niveles de detalle, facilitando la comunicación y trabajo en equipo

## El dominio de la Arquitectura
![[Pasted image 20260804175256.png]]

## Rol del arquitecto
* **Revisar y negociar los requerimientos**
	* El arquitecto actúa como un "gran negociador". Su función es encontrar un equilibrio viable entre lo que el software necesita para satisfacer los atributos de calidad y lo que la organización realmente puede proveer en términos de hardware, infraestructura, tiempo y presupuesto
	* los famosos trade-off
* **Direccionar [[Requerimientos No Funcionales]] (RNF) a la arquitectura:**
	* Se encarga de traducir los requerimientos de calidad (como seguridad, desempeño, usabilidad y disponibilidad) en decisiones arquitectónicas que darán forma al sistema
* **Documentar la arquitectura**
	* Genera y mantiene actualizado el **Documento de Arquitectura de Software** y la **Descripción de la Arquitectura**, registrando de manera justificada las decisiones tecnológicas fundamentales para que sirvan de base ante futuros cambios o mantenimiento.
	* [[Documentación De La Arquitectura]]
* **Comunicar la arquitectura**
	* Es responsable de asegurar que todos los involucrados (usuarios finales, desarrolladores, administradores de sistemas, jefes de desarrollo, etc.) comprendan la estructura global y los lineamientos del "esqueleto" del software.
* **Asegurar que la arquitectura se respete**
	* Actúa como un supervisor técnico, garantizando que el diseño detallado y la posterior codificación sigan fielmente los lineamientos arquitectónicos establecidos.
* **Configurar la arquitectura de hardware:**
	* Define la topología y distribución del software sobre los componentes físicos del entorno
* **Colaborar con la administración del proyecto:**
	* Trabaja de la mano con el Administrador del Proyecto ayudando en la planificación general, las estimaciones de tiempos, la distribución de tareas y la calendarización del proyecto.

---
# References
## Father
## child