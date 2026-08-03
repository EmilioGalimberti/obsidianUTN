---
aliases:
  - DSI -PARCIAL 2 - UNIDAD02- Workflo DISEnio
subject: DSI
year: "3"
exam: PARCIAL2
unit: "2"
type: TEO
zk_type: permanent
status: done
date: 2026-08-03
tags:
source:
  - "[[DSI-Parcial2-TEO-U02- Workflow de Diseño]]"
  - https://www.youtube.com/watch?v=Rng8xmqeFek
---
---


# Propósito y Definición
El diseño es un proceso iterativo que transforma un modelo conceptual o lógico (salida del análisis) en un modelo físico teniendo en cuenta las restricciones del negocio (tecnología implementación, calidad)

El  diseño de software crea una representacion o modelo del software que propociona detalles sobre:
* La arquitectura del software
* Estructura de datos
* Interfaces
* Componentes


**objetivo**: achicar el puente que existe entre el modelo de análisis y la etapa de codificación o implementación

**propósito**:
* Comprender en profundidad los aspectos relacionados con los [[Requerimientos No Funcionales]]  y restricciones tecnológicas
* Producir una entrada apropiada y un punto de partida para el workflow  de implementación (preparar el "plano" para el código)
	* *CUAL ES EL PLANO?*
	* *1. - Respuesta: El "plano" de implementación es el **Modelo de Diseño** en su conjunto (principalmente los _Diagramas de Clases de Diseño_, _Diagramas de Secuencia de Diseño_, la especificación de _Subsistemas/Componentes_ y el documento de _Descripción de la Arquitectura de Software_).**
* Descomponer el trabajo de implementación en parte mas manejables, permitiendo a diferentes equipos de desarrollo trabajar en paralelo
	* *Cuales SON ESTAS PARTES?*
	* *1. - **Respuesta:** Son los **Subsistemas, Paquetes o Componentes de Software**. Al dividir la arquitectura en subsistemas independientes con interfaces bien definidas, diferentes equipos de desarrollo pueden programar en paralelo.*
* Identificar las [[interfaces]] entre los [[subsistemas]]
* - Crear una abstracción de la solución de diseño sin estar restringidos a una tecnología.
	* *COMO SERIA ESTO?*
	* *1. - **Respuesta:** Significa diseñar usando **patrones de diseño y conceptos arquitectónicos lógicos** (por ejemplo: división en capas, patrones como MVC, Repository, DTO, etc.) antes de atarse a la sintaxis o particularidad de un lenguaje/framework específico (ej. definir el diseño independientemente de si se implementará en Java/Spring, C#/.NET o Node.js).*

**Rol de diseño en PUD**
* Fase de elaboración: contribuye a una arquitectura estable y robusta
* Fase de construcción: Crea un plano para la implementación
* ![[Pasted image 20260728141157.png|562]]

**Trabajadores involucrados** (*Esto ya no se toma*)
para profundizar: https://www.youtube.com/watch?v=d69ycx_f-Wo

**Diagramas de UML 2.0 en el diseño**
![[Pasted image 20260728141627.png|509]]
- **Diagramas de Estructura (Estáticos):** Diagrama de Clases de Diseño, Diagrama de Componentes, Diagrama de Despliegue, Diagrama de Estructura Compuesta.
- **Diagramas de Comportamiento / Interacción (Dinámicos):** Diagrama de Secuencia de Diseño, Diagrama de Comunicación, Diagrama de Estados.
# Entradas y salida del diseño
![[Pasted image 20260728141412.png|497]]
En el contexto del PUD, el diseño comienza una vez finalizado el análisis. 
El análisis solo se ocupó de los requerimientos funcionales; ahora el diseño 
transforma ese modelo lógico en un modelo físico.
## Entradas
- **Modelo de Análisis** (Realización de Casos de Uso de Análisis, Diagrama de Clases de Análisis).
- **Especificación de Requisitos del Software** (principalmente [[Requerimientos No Funcionales]] y Restricciones Tecnológicas).
- **Descripción de la Arquitectura de Referencia / Entorno de Implementación**.

## Salidas
### Modelo de diseño
* Es un modelo físico porque es un plano de la implementación
* No es genérico sino que es especifico para determinadas condiciones de implementación
* Busca preservar la estructura definida en el análisis tanto como sea posible
* **Descripción de la Arquitectura:**
	* El artefacto rector que destila las decisiones más críticas del sistema. Es la visión que garantiza que todos los equipos trabajen bajo una misma dirección técnica.

### Modelo de despliegue
Enfocado en la distribución del software sobre los nodos de hardware necesarios para que funcione.

# Análisis VS Diseño *preg de parcial*
mientras que el análisis se enfoca en el _qué_ debe hacer el sistema (requerimientos funcionales, *modela la solución en términos lógicos*), el diseño define el **cómo** el sistema logrará hacer eso, dando respuesta arquitectónica y estructural a los [[Requerimientos No Funcionales]], **modela la solución en términos físicos**

| Analisis                                                                                         | Diseño                                                       |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| Modelo Conceptual, porque es una abstraccion del sistema y permite aspectos de la implementacion | Modelo físico, porque es un plano de la implementación       |
| Genérico respecto al diseño (aplicable a varios diseños)                                         | No generico, especifico para una implementacion              |
| Menos formal                                                                                     | Mas formal                                                   |
| Dinámico (No muy centrado en la secuencia)<br>*QUE es que no este centrado en la secuecnia?*     | Dinamico, muy centrado en la secuencia??                     |
| Bosquejo del diseño del sistema, incluyendo su arquitectura                                      | Manifiesto deldiseño del sistema, incluyendo su arquitectura |
El modelo de diseño es mas detallado que el modelo de análisis y comienza a tener mas cosas en cuenta (restricciones de implementación, rnf, estructura, tecnología)

**Porque se mantienen por separado?**
El análisis se mantiene por separado para poder ser implementado en distintas tecnologías, es decir que para un mismo modelo de análisis puedo plantear distintos diseños que me resuelvan el problema de maneras diferentes

Por lo tanto el el modelo físico producto del diseño es para algo en particular (por ejemplo una infraestructura)

****`*QUE es que no este centrado en la secuencia? / Dinamico, muy centrado en la secuencia??*`****
*1. - **Respuesta:** En Análisis, la vista dinámica (Realizaciones de Casos de Uso) es **conceptual**: muestra la interacción lógica entre actor, pantallas conceptuales, controladores de negocio y entidades sin entrar en detalles de métodos concretos. En Diseño, se vuelve **centrado en la secuencia exacta de llamadas**: especifica firmas de métodos reales, parámetros, llamadas síncronas/asíncronas, objetos de persistencia y manejo de mensajes entre clases de software.*
****
# Que aspectos deben diseñarse *preg de parcial*

![[Pasted image 20260728181558.png|533]]
## Diseño arquitectónico (este es el principal)
[[Diseño Arquitectónico]]
## Diseño de Datos
Transformar los requerimientos en las estructura de datos necesarias para hacer persistente al software
El diseño de datos crea modelo de datos o información en un nivel de abstracción elevado (punto de vista del usuario)
* Refinamiento progresivo hacia representación especificas de la implementación (base de datos)
* Arquitectura de datos -> Influye en la arquitectura de software
## Diseño de procesos
Se encarga de transformar los elementos estructurales(*QUE SON LOS ELEMENTOS ESTRUCTURALES??*) en una descripción procedimental y lógica de los componentes de software. En este paso, se toma el trabajo inicial del análisis (las Realizaciones de Casos de Uso de Análisis) y se lo profundiza de forma considerable para crear las Realizaciones de Casos de Uso de Diseño. A diferencia de la etapa anterior, aquí los procesos se diseñan incorporando todos los mecanismos tecnológicos reales: se modela cómo funcionará la concurrencia, las transacciones automáticas, los protocolos de seguridad, la autenticación y la recuperación ante fallos de hardware o red

****`*QUE SON LOS ELEMENTOS ESTRUCTURALES??*`** (en Diseño de Procesos)**
*1. - **Respuesta:** Son las **clases de análisis, clases de dominio, fronteras y controles** identificados en la estructura estática del Análisis. En el diseño de procesos, estos elementos lógicos se traducen y convierten en clases de software con métodos, atributos concretos e interfaces.*
## Diseño de Experiencia de usuario
Es la disciplina orientada específicamente a pensar, evaluar e implementar la interacción humana con el sistema computacional
## Diseño formas de entrada/salida
Describe de forma minuciosa los mecanismos mediante los cuales se va a ingresar la información al software y de qué manera este presentará sus salidas o resultados

**Tipos de sistemas según forma de entrada:**

* **En lote (batch):** la información se procesa en bloques (ej: censos de población)

* **En línea:** procesamiento interactivo en tiempo real (ej: inscripciones)

* **En tiempo real:** afectan al ambiente con restricciones de tiempo estrictas

→ Dependiendo del tipo de sistema se diseña la forma de entrada
## Diseño de los procedimientos manuales
Se enfoca en detallar cómo la nueva herramienta de software se va a acoplar e integrar a los procesos del Sistema de Negocio de la empresa. Aquí se especifican todos aquellos procedimientos y tareas de respaldo que no pueden ser automatizados, garantizando que los usuarios sepan exactamente qué pasos manuales deben realizar antes o después de utilizar el software para que el flujo de trabajo general de la compañía no se interrumpa

# Guía para evaluar un buen diseño
Principios del proceso de diseño del software
- El diseño deberá implementar todos los requisitos explícitos del modelo de análisis, y deberán ajustarse a todos los requisitos implícitos que desea el cliente;
- El diseño deberá ser una guía legible y comprensible para aquellos que generan código y para aquellos que comprueban y consecuentemente, dan soporte al software
- El diseño deberá proporcionar una imagen completa del software, enfrentándose a los dominios de comportamiento, funcionales y de datos desde una perspectiva de implementación

---
# References
## Father
[[DSI-Parcial2-TEO-U02- Workflow de Diseño]]
## child



	    
    