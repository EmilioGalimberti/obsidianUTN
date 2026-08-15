---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit: "3"
type: TEO
zk_type: fleeting
status: done
date: 2026-07-27
source:
tags:
---
---
# ARQUITECTURA MICROSIERVICIO  (estilo)

[11 Arquitectura de Microservicios.pdf](11_Arquitectura_de_Microservicios.pdf)

# ¿Qué es?

La **Arquitectura de Microservicios** es un estilo arquitectónico que estructura una aplicación se crea con componentes **pequeños, autónomos y débilmente acoplados,** donde cada módulo
actúa como una aplicación o servicio independiente. . En lugar de construir una única y masiva aplicación monolítica, el sistema se descompone en componentes independientes que colaboran entre sí.

La idea central es que cada servicio:

- Está construido en torno a una **capacidad de negocio** específica (ej. "Gestión de Pagos", "Inventario", "Notificaciones").
- Realiza **una sola tarea y la hace bien** (alta cohesión).
    - 'Micro' proviene del hecho de que cada servicio debe enfocarse en hacer solo 1 tarea.
        - Tamaño de un microservicio
            
            La definición dada de microservicios no dice nada sobre el tamaño de un
            microservicio.
            • El término “microservicio” sugiere que se refiere especialmente a servicios
            pequeños.
            • En la práctica, los microservicios pueden variar enormemente en tamaño.
            • Algunos microservicios mantienen ocupado a todo un equipo, mientras que
            otros comprenden sólo unos pocos cientos de líneas de código.
            • Aunque el tamaño de los microservicios figura como parte del nombre, no es
            adecuado para ser parte de la definición
            
- Puede ser **desarrollado, desplegado y escalado de forma independiente**.
- Cada servicio puede funcionar solo, pero interactuar con otro módulo cuando sea necesario.
- La arquitectura de microservicios es una SOA. Los servicios se conectan a través de interfaces proporcionadas por SOA.

# Principios Fundamentales

1. **Independencia y Autonomía:** Cada microservicio es una mini-aplicación en sí misma. Tiene su propio código, su propio ciclo de vida y, a menudo, su propia base de datos.
    1. Cada servicio en una aplicación de microservicio controla una función única con sus datos. Cada servicio en una aplicación basada en microservicios tiene una base de datos separada.
    2. Aunque esto puede causar datos redundantes, asegura un acoplamiento bajo.
2. **Flexibilidad Tecnológica:** No hay un "molde único". Un servicio puede estar escrito en Java y usar una base de datos SQL, mientras que otro puede estar en Python y usar una base de datos NoSQL. Se elige la mejor herramienta para cada trabajo.
3. **Comunicación a través de APIs:** Los servicios se comunican entre sí a través de la red, utilizando protocolos bien definidos y ligeros, como APIs REST, gRPC o mensajería asíncrona (colas de mensajes).
    - comunicacion entre microservicios
        
        Se conectan entre sí a través de una interfaz de programación de aplicaciones (API), es decir, un conjunto de reglas estrictamente controladas que ambos pueden manejar.
        
        ![image.png](image.png)
        
    
    Un componente común en esta arquitectura es el **API Gateway**, que actúa como una única puerta de entrada para todas las peticiones externas, enrutándolas al microservicio correspondiente y manejando tareas como la autenticación y el balanceo de carga.
    
    ![image.png](image%201.png)
    
4. **Descentralización:** Se evita la centralización tanto en la tecnología como en la gestión de datos. Los equipos son dueños de sus servicios de principio a fin.

## Que caracteriza la arquitectura de microservicios

![image.png](image%202.png)

- Composición vía servicios
    - ⮚Los servicios se despliegan independientemente.
    ⮚Interfaces explícitas para evitar romper el encapsulamiento.
    ⮚Las API remotas de grano grueso
- Organización en torno a capacidades de negocios.
- Productos no proyectos
    - ⮚Capacidades de negocio.
    ⮚El producto puede utilizarse para asistir e incrementar las capacidades del negocio
    ⮚El equipo es dueño de un producto durante todo su ciclo de vida, incluyendo la operación
- Terminales inteligentes y tuberías bobas.
    - ⮚Microservicios lo más desacoplados y cohesivos posible.
    ⮚Peticiones-respuestas HTTP con recursos API y mensajería liviana.
    ⮚Utilizar un bus ligero de mensajes.
    ⮚Cambiar el patrón de comunicaciones
- Administración descentralizada.
    - ⮚Utilización de patrones, prácticas open source y código y librerías compartidas.
    ⮚Evolución de los contratos de los servicios en forma independiente: Patrón Tolerant Reader y Consumer driven contracts.
    ⮚Ética de: “el que lo construye, lo ejecuta
- Gestión de datos descentralizada.
    - ⮚Persistencia políglota.
    ⮚No coordinación de transacciones entre servicios
    ⮚Operaciones compensatorias.
        
        ![image.png](image%203.png)
        
- Automatización de la infraestructura
    - ⮚Pruebas automatizadas
    ⮚Despliegue automatizado e inversión en herramientas.
    ⮚Automatización de la infraestructura
        
        ![image.png](image%204.png)
        
- Diseño para fallas.
    - ⮚Indisponibilidad del proveedor
    ⮚Rastros para predicción de inconvenientes.
    ⮚Detectar fallas y restaurar automáticamente.
    ⮚Monitorización en tiempo real de la aplicación

## Estructura: Monolitica vs. Microservicios

Para entender los microservicios, es útil compararlos con su opuesto, la arquitectura monolítica.

- **Arquitectura Monolítica:** Es una única unidad grande y acoplada. Todos los componentes (UI, lógica de negocio, acceso a datos) están empaquetados y desplegados juntos. Si una pequeña parte falla, toda la aplicación puede caerse. Para escalar, debes replicar toda la aplicación.
- **Arquitectura de Microservicios:** La aplicación se divide en servicios independientes. Si el servicio de "Recomendaciones" falla, los servicios de "Pagos" y "Login" pueden seguir funcionando. Para escalar, solo replicas los servicios que tienen alta demanda.
    
    ![image.png](image%205.png)
    

![image.png](image%206.png)

![image.png](image%207.png)

![image.png](image%208.png)

## Implementacion

| Monolíticas | Microservicios |
| --- | --- |
| Fáciles de desarrollar desde
cero, pero si el tamaño de la
aplicación supera cierto punto,
se vuelven más complejas y
difíciles de implementar. |  Los microservicios crean un
sistema distribuido complejo,
pero aún es fácil implementar
cada servicio por separado. |
|  Sigue una implementación
centralizada, que es más fácil de
implementar. Sin embargo,
tiene el costo de la complejidad
y la dificultad para realizar
cambios.  |  Utiliza un enfoque descentralizado
hacia la implementación. A pesar de la
complejidad de la implementación en
su conjunto, la implementación de un
solo módulo no presenta problemas |

## Despliegue

- Las aplicaciones en arquitectura monolítica son fáciles de implementar, pero a medida que crece el tamaño, se vuelve difícil desplegar la aplicación. Además, incluso los cambios más pequeños requieren desplegar la aplicación completa.
- • Las aplicaciones de gran tamaño también se vuelven más lentas de desplegar. Por lo tanto, las aplicaciones monolíticas no pueden adaptarse a las secuencias de prácticas continuas.
- • Desplegar una aplicación en microservicios es fácil. Cada módulo puede desplegarse de forma independiente sin compilar toda la aplicación. Facilita la aplicación de
prácticas continuas (CI/CD/CD)

### Escalabilidad

- Las aplicaciones monolíticas se pueden escalar, pero es difícil escalar aplicaciones grandes. La escalabilidad en un solo componente requiere escalar toda la aplicación.
- Las aplicaciones de microservicios tienen servicios independientes, que podemos escalar individualmente. No es necesario escalar toda la aplicación.
- La escalabilidad es la clave para incorporar servicios adicionales y agilidad en una aplicación.
- Resulta fácil incluir prácticas de DevOps y servicios web como AWS en aplicaciones de microservicios

## Mantenimiento y administracion

- Así como una función facilita el mantenimiento de un programa, los módulos más pequeños facilitan el mantenimiento de una aplicación completa.
- En el caso de aplicaciones monolíticas, se vuelve difícil de
mantener y administrar si el tamaño de la aplicación es
extremadamente grande.
- Las aplicaciones monolíticas están centralizadas y es fácil
comunicar los problemas entre los desarrolladores. Aunque, el
mantenimiento no es fácil.
- Los microservicios crean una aplicación descentralizada que
aumenta la complejidad, pero es más fácil de mantener.
- La comunicación entre módulos puede convertirse en un
problema en un sistema distribuido, pero los microservicios
son mucho más fáciles de mantener y depurar

## Orientación a Negocio

- Las empresas modernas están más alineadas con
la idea de los microservicios.
- Dado que los microservicios se basan en SOA,
que está diseñado específicamente para un
sistema empresarial.
- Los sistemas monolíticos todavía se utilizan en
gran medida o forman parte de los modelos de
negocio existentes.
- La elección de la arquitectura depende del modelo
comercial, pero las aplicaciones de microservicios
están más orientadas a los negocios

![image.png](image%209.png)

## Ventajas

![image.png](image%2010.png)

- **Escalabilidad Granular:** Es su mayor ventaja. Puedes escalar solo los servicios que lo necesitan (ej. más instancias del servicio de "Pagos" durante el Black Friday) en lugar de escalar toda la aplicación, lo que es mucho más eficiente en costos.
    - Más sencillo escalar el desarrollo.
        - Es posible liberar versiones más frecuentemente
- **Agilidad y Desarrollo Independiente:** Equipos pequeños y autónomos pueden desarrollar, probar y desplegar sus servicios de forma independiente y rápida, sin tener que coordinarse con toda la organización.
    - Cada servicio es relativamente pequeño y fácil de entender para el desarrollado
- **Aislamiento de Fallos (Resiliencia):** Un error en un microservicio no tiene por qué afectar al resto del sistema, lo que aumenta la disponibilidad general de la aplicación.
- **Flexibilidad Tecnológica:** Permite innovar y adoptar nuevas tecnologías para nuevos servicios sin tener que reescribir toda la aplicación.
    - Elimina los compromisos de largo plazo con una tecnología determinada.

## Desventajas y Desafíos Significativos

Adoptar microservicios implica gestionar un sistema distribuido, lo cual es inherentemente complejo.

- **Complejidad Operacional:** Hay muchas más "piezas móviles" que desplegar, monitorear, y gestionar. Requiere una cultura DevOps madura y herramientas de automatización robustas.
- **Transacciones Distribuidas:** Garantizar la consistencia de los datos a través de múltiples servicios es extremadamente difícil. No se puede hacer una transacción de base de datos que abarque varios servicios, por lo que se deben usar patrones complejos como **Saga**.
- **Comunicación por Red:** La comunicación entre servicios a través de la red es más lenta y menos confiable que las llamadas internas en un monolito. Esto introduce latencia y nuevos puntos de fallo.
- **Trazabilidad y Monitoreo:** Seguir una solicitud de un usuario a través de varios servicios para depurar un error es muy complicado. Se necesitan herramientas de **logging centralizado** y **trazado distribuido**.

![image.png](image%2011.png)

![image.png](image%2012.png)

## ¿Cuándo Usar Microservicios?

![image.png](image%2013.png)

![image.png](image%2014.png)

## Cuando NO utilizar microservicios

▪ Evite la creación de un monolítico distribuido: garantice la
descomposición adecuada de los servicios adhiriéndose a principios de
desacoplamiento, como la aplicación de contexto limitado y capacidades
de negocio. Crear un monolítico distribuido es perjudicial, ya que
amplifica la complejidad arquitectónica sin aprovechar los beneficios de
los microservicios.

▪ Implemente microservicios con DevOps o servicios en la nube: los
microservicios adoptan enfoques distribuidos y nativos de la nube, y sus
beneficios solo pueden lograrse plenamente si se adhieren a los
principios nativos de la nube. Esto implica implementar:

1. Pipelines de integración continua/despliegue continuo (CI/CD) con
automatizaciones de DevOps.
2. Herramientas efectivas de despliegue y monitoreo.
3. Servicios en la nube administrados para respaldar su
infraestructura.
4. Tecnologías y herramientas clave como contenedores, Docker y
Kubernetes.
5. Adopción de comunicaciones asíncronas mediante servicios de
mensajería y servicios de streaming de eventos.

▪ Tamaños de equipo restringidos, equipos compactos: si el tamaño de
su equipo carece de la capacidad para gestionar cargas de trabajo de
microservicios de manera eficiente, inevitablemente se producirán
retrasos en la entrega.

• Desafíos para equipos pequeños: para equipos más pequeños,
justificar una arquitectura de microservicios puede ser un desafío,
ya que es posible que el equipo deba dedicar esfuerzos
significativos para manejar la implementación y administración de
los microservicios.

• Inaplicabilidad para nuevos productos: cuando se trata de un
producto nuevo que requiere cambios sustanciales durante el
desarrollo y las iteraciones, iniciar con microservicios puede no ser
el enfoque más adecuado. Los microservicios tienden a ser más
costosos al rediseñar los dominios de negocio, incluso si la
escalabilidad se convierte en un requisito crítico para el éxito.

• Inconvenientes de rediseñar dominios de negocio: los
microservicios pueden ser costosos, especialmente cuando se
rediseñan dominios de negocio, incluso en escenarios donde el
éxito conduce a la necesidad de una arquitectura altamente
escalable.

• Evitar el anti patrón de base de datos compartida: es esencial
desalentar la adopción del anti patrón de base de datos
compartida. Este patrón socava los principios de los microservicios
y puede introducir complejidades que obstaculizan la eficacia de la
arquitectura

---

## Patrones para Microservicios: estan divididos en tres capas

Dentro de microservicio tiene sus propios patrones

![image.png](image%2015.png)

(para el parcial vemos estos pero hay mas)

- De infraestructura
    - Single Service Per Host
        
        Contexto
        ▧Ha aplicado el patrón de arquitectura de microservicio y ha diseñado su sistema como un conjunto de servicios. Cada servicio se despliega como un conjunto de instancias de servicio para lograr rendimiento y disponibilidad
        
        Problema
        ¿Cómo se empaquetan y despliegan los servicios?
        
        - MOTIVACION
            
            ▧Los servicios se escriben utilizando una variedad de lenguajes, marcos y versiones de marcos.
            ▧Cada servicio consta de múltiples instancias de servicio para rendimiento y disponibilidad.
            ▧Escalar e implementar el servicio de forma independiente.
            ▧Aislar las instancias de servicio unas de otras
            ▧Crear e implementar rápidamente un servicio.
            ▧Poder limitar los recursos (CPU y memoria) consumidos por un servicio.
            ▧Monitorear el comportamiento de cada instancia de servicio.
            ▧Que la implementación sea confiable
            ▧Implementar la aplicación de la manera más rentable posible
            
        
        Solución
        • Despliegue cada instancia de servicio única en su propio host.
        
        - ventajas
            
            ▧Las instancias de servicios están aisladas unas de otras.
            ▧No hay posibilidad de que entren en conflicto requisitos de recursos o versiones de dependencia.
            ▧Una instancia de servicio solo puede consumir como máximo los recursos de un único host
            ▧Es sencillo monitorear, administrar y volver a implementar cada instancia de servicio.
            
        - desventajas
            
            ▧Utilización de recursos potencialmente menos eficiente en comparación con servicios múltiples por host
            porque hay más hosts
            
        
        ![image.png](image%2016.png)
        
        - PATRÓN SINGLE SERVICE PER HOST SERVICE INSTANCE PER VIRTUAL MACHINE
            
            Solución
            ▧Empaquete el servicio como una imagen de máquina virtual y despliegue cada instancia de servicio como una máquina virtual separada.
            
            Beneficios
            ▧Es sencillo escalar el servicio aumentando el número de instancias.
            ▧La VM encapsula los detalles de la tecnología utilizada para crear el servicio.
            ▧Cada instancia de servicio está aislada.
            ▧Una VM impone límites a la CPU y la memoria consumidas por una instancia de servicio
            ▧Las soluciones IaaS como AWS proporcionan una infraestructura madura y rica en funciones para implementar y administrar máquinas virtuales. Por ejemplo,
            
            ⮚ Balanceador de carga elástico
            ⮚ Grupos de escalado automático
            
            Desventajas
            ▧Construir una imagen de máquina virtual es lento y requiere mucho tiempo
            
        - PATRÓN SINGLE SERVICE PER HOST SERVICE INSTANCE PER VIRTUAL CONTAINER
            
            Solución
            ▧Empaquete el servicio como una imagen de contenedor (Docker) y despliegue cada instancia de servicio como un contenedor.
            
            Beneficios
            ▧Es sencillo ampliar y reducir un servicio cambiando la cantidad de instancias de contenedor.
            ▧El contenedor encapsula los detalles de la tecnología utilizada para crear el servicio.
            ▧Cada instancia de servicio está aislada.
            ▧Un contenedor impone límites a la CPU y la memoria consumidas por una instancia de servicio.
            ▧Los contenedores son extremadamente rápidos de construir e iniciar. Los contenedores Docker se inician mucho más rápido que una VM, ya que solo se inicia el proceso de la aplicación en lugar de un sistema operativo completo.
            
            Desventajas
            ▧La infraestructura para implementar contenedores no es tan rica como la infraestructura para desplegar máquinas virtuales.
            
    - Multiple Service Per Host
        - contexto
            
            ▧Ha aplicado el patrón de arquitectura de
            microservicio y ha diseñado su sistema como un
            conjunto de servicios. Cada servicio se implementa
            como un conjunto de instancias de servicio para
            lograr rendimiento y disponibilidad.
            
        
        Problema
        ¿Cómo se empaquetan y despliegan los servicios?
        
        - Motivacion
            
            ▧Los servicios se escriben utilizando una variedad de lenguajes, marcos y versiones de marcos.
            ▧Cada servicio consta de múltiples instancias de servicio para rendimiento y disponibilidad.
            ▧Escalar e implementar el servicio de forma independiente.
            ▧Aislar las instancias de servicio unas de otras
            ▧Crear e implementar rápidamente un servicio.
            ▧Poder limitar los recursos (CPU y memoria) consumidos por un servicio.
            ▧Monitorear el comportamiento de cada instancia de servicio.
            ▧Que la implementación sea confiable
            ▧Implementar la aplicación de la manera más rentable posible.
            
        
        Solución
        • Ejecute múltiples instancias de diferentes servicios en un host (máquina
        física o virtual)
        
        - Existen varias formas de implementar una instancia de servicio en un host
        compartido, entre las que se incluyen:
            -  Implemente cada instancia de servicio como un proceso JVM. Por ejemplo,
            instancias de Tomcat o Jettypor instancia de servicio.
            -  Implemente varias instancias de servicio en la misma JVM. Por ejemplo, como
            aplicaciones web o paquetes OSGI.
        
        ![image.png](image%2017.png)
        
        ![image.png](image%2018.png)
        
        - Ventajas
            
            ▧Utilización de recursos más eficiente que el patrón una instancia de servicio por host.
            ▧Es aún más eficiente si un proceso o grupo de procesos ejecuta múltiples instancias de servicio, por ejemplo, múltiples aplicaciones web que comparten el mismo servidor Apache Tomcat y JVM.
            ▧La implementación de un servicio es relativamente rápida
            
        - Desventajas
            
            ▧Riesgo de requisitos de recursos contradictorios.
            ▧Riesgo de versiones de dependencia conflictivas.
            ▧Difícil limitar los recursos consumidos por una instancia de servicio.
            ▧Si se implementan varias instancias de servicios en el mismo proceso, entonces es difícil monitorear el consumo de recursos de cada instancia de servicio.
            ▧Es imposible aislar cada instancia.
            
- Aplicacion de infraestructura
    - Patron Api Gateway
        
        Problema
        ¿Cómo acceden los clientes de una aplicación basada en microservicios a los servicios individuales?
        
        Desafios:
        
        ▧La granularidad de los microservicios suele ser diferente de la que necesita un cliente.
        ▧Diferentes clientes necesitan datos diferentes.
        ▧El rendimiento de la red es diferente para diferentes tipos de clientes.
        ▧La partición en servicios puede cambiar con el tiempo y debe ocultarse a los clientes.
        ▧Los servicios pueden utilizar un conjunto diverso de protocolos, algunos de los cuales pueden no ser compatibles con la web
        
        Solución
        
        - Implementar una API Gateway que sea el punto de entrada único para todos los clientes.
        - La API Gateway maneja las solicitudes de dos maneras:
            - Algunas solicitudes simplemente se envían/enrutan al servicio apropiado.
            - Otras solicitudes las distribuye a múltiples servicios.
        - Puede exponer una API diferente para cada cliente.
        - • También podría implementar seguridad, por ej. verificar que el cliente está
        autorizado a realizar la solicitud.
        - • API Gateway es responsable del enrutamiento de solicitudes, la composición y la traducción de protocolos. Proporciona a cada uno de los clientes de la aplicación una API personalizada.
            - La API Gateway cumple la función crucial de ocultar la
            ubicación y los detalles de implementación de los servicios vinculados a los endpoints de la API Gateway
        - • API Gateway también puede enmascarar fallas en los servicios backendal devolver datos almacenados en caché o predeterminados.
        - API Gateway de microservicios se abstiene de albergar lógica de negocios, orquestación o mediación, defendiendo el principio sagrado de un "contexto limitado“ (Bounded context (DDD))
        - Ventajas
            
            ▧Aísla a los clientes de cómo se divide la aplicación en microservicios.
            ▧Aísla a los clientes del problema de determinar las ubicaciones de las instancias de servicio.
            ▧Proporciona la API óptima para cada cliente.
            ▧Reduce el número de solicitudes/ida y vuelta.
            ▧Menos solicitudes también significan menos gastos generales y mejoran la experiencia del usuario.
            ▧Una API Gateway es esencial para las aplicaciones móviles.
            ▧Simplifica el cliente al mover la lógica para llamar a múltiples servicios desde el cliente a la API Gateway.
            ▧Se traduce desde un protocolo API público "estándar" compatible con la web a cualquier protocolo que se utilice internamente
            
        - Desventajas
            
            ▧Mayor complejidad: la API Gateway es otra parte que debe desarrollarse, implementarse y gestionarse.
            ▧Mayor tiempo de respuesta: debido al salto de red adicional a través de la API Gateway.
            
        - PORQUE DEBERIA USARLO?
            
            ![image.png](image%2019.png)
            
        
        ![image.png](image%2020.png)
        
        ![image.png](image%2021.png)
        
        ![image.png](image%2022.png)
        
        ![image.png](image%2023.png)
        
    - Patron Backend for Frontends
        
        Es una variación del patrón Api Gateway: Define una API Gateway
        separada para cada clase de cliente.
        
        ![image.png](image%2024.png)
        
- De aplicacion
    - Patrón: Descomposición por Subdominios
        - Descomposición por capacidad de negocio
        - Descomposición por subdominio, basado en los subdominios de DDD
        - Subdominio: parte de un dominio, basado en una descomposición conceptual particular del dominio
        
        ![image.png](image%2025.png)
        
        Fanaticos del futbol
        
        ![image.png](image%2026.png)
        
        - Contexto Acotado (Bounded Context): Definición operacional donde un modelo particular es aplicable y está bien definido. (Comúnmente un subsistema)
        
        ![image.png](image%2027.png)
        
        ### GUÍA PARA TRABAJAR CON DDD
        
        ![image.png](image%2028.png)
        
        ![image.png](image%2029.png)
        
    - Patron: Base de datos por servicio
        
        Contexto
        Necesidad de persistencia de los microservicios
        
        Problema
        ¿Cómo manejar la base de datos para microservicios?
        
        Solución
        • Cada microservicio debe manejar sus datos en forma privada y sólo acceder a ellos a través de su API.
        • La base de datos del servicio es parte efectiva de la implementación del servicio. No puede accederse directamente por otros servicios.
        
        ![image.png](image%2030.png)
        
        - ejemplo de flujo de trabajo
            
            ![image.png](image%2031.png)
            
        
        ![image.png](image%2032.png)
        
        ![image.png](image%2033.png)
        
        - ventajas
            
            ▧Bajo acoplamiento.
            ▧Utilizar la base de datos más conveniente.
            
        - desventjas
            
            ▧Implementación compleja.
            ▧Complejidad de manejar Bases de datos SQL y NoSQL
            
        - recomendaciones
            
            ▧Composición de API
            ▧Segregación de responsabilidad con una o más vistas
            
        
        ![image.png](image%2034.png)
        
        - MANTENER ACID
            
            ![image.png](image%2035.png)
            
- MELES TRABAJO CON EL EJ FTGO → NOSE CUAL ES
    
    ![image.png](image%2036.png)
    
    ![image.png](image%2037.png)
    
    ![image.png](image%2038.png)
    
    ![image.png](image%2039.png)
    
    ![image.png](image%2040.png)
    

---

- Concepto REST (REPRESENTATIONAL STATE TRANSFER)
    
    ¿Qué es?: REST es un conjunto de restricciones arquitectónicas que crean un estilo arquitectónico utilizado para sistemas distribuidos.
    
    Es una estructura de servicio que permite comunicación fácil y rápida entre cliente y servidor
    
    Fue desarrollado como alternativa a SOAP y  web services basados en WSDL.
    
    Casi todas las aplicaciones tienen un API REST que nos permite interactuar con ellas por medio de servicios.
    
    REST ignora los detalles de implementación del componente y la sintaxis del protocolo para enfocarse en los roles de los componentes, las restricciones sobre su implementación con otros componentes y la representación de los datos.
    
    ![image.png](image%2041.png)
    
    ![image.png](image%2042.png)
    
    ![image.png](image%2043.png)
    
    ![image.png](image%2044.png)
    
    - Ventajas
        
        ![image.png](image%2045.png)
        
    - Desventajas
        
        ![image.png](image%2046.png)
        
- ¿QUÉ ES UNA API?
    - API: interfaz de programación de aplicaciones, es la parte de una aplicación que se
    comunica con otras aplicaciones en todos los ámbitos. Para ser más técnico, una API es
    un protocolo específico y un grupo de métodos que define cómo dos aplicaciones
    diferentes pueden compartir y modificar los datos de entre sí
    - • Son importantes y bastante necesarias en una infraestructura digital moderna porque
    proporcionan la base para una comunicación eficiente y estandarizada entre dos
    aplicaciones construidas y que funcionan de manera diferente.
    - • Una API normalmente se encuentra entre los componentes principales de un software y
    el público. Los desarrolladores externos a menudo pueden acceder a partes específicas
    del backend de una aplicación sin tener que aprender y comprender cómo funciona
    toda la aplicación. Esto es lo que hace que una API sea una interfaz de programador.
    - • Las API son las que permiten las integraciones de software, o entidades de software
    separadas, para que funcionen entre sí y compartan información.
    - • Algunos ejemplos:
    ⮚ Pagar desde una página de e-commerce con MODO.
    ⮚ Un sitio web de viajes que utiliza la API de una aerolínea para ver los horarios de
    los vuelos y los precios de los billetes.
    ⮚ Sitios que utilizan las API de Facebook o Google para permitir el inicio de sesión.
    - • Hasta ahora definimos un tipo de API específico, al que llamamos API web.
    Estas API facilitan la comunicación entre servidores web. Los ejemplos que
    detallamos anteriormente también son ejemplos de API abiertos, lo que
    básicamente significa que están disponibles para que cualquiera los use.
    - • Cuando hablamos de API internas, por ejemplo, hablamos de interfaces que
    se utilizan para la comunicación dentro de una aplicación, con acceso
    restringido. Por lo general, las organizaciones utilizarán este tipo de API y
    otorgarán acceso a desarrolladores y empleados autorizados
    
- APIS REST
    
    ![image.png](image%2047.png)
    
- API VS MICROSERVICIOS
    
    Los microservicios son estilos de arquitectura de software que dividen las funciones específicas de la aplicación en "servicios" o componentes más pequeños. Cuando los desarrolladores crean una aplicación de esta manera, dirán quesigue una arquitectura de microservicio.
    
    Para evitar confusiones, usaremos el término "servicios" cuando describamos los componentes y usaremos "microservicios" cuando hablemos de toda la arquitectura del sistema.
    
    Una API es la parte de la web abb que le permite comunicarse con otras aplicaciones. Una API de software define un conjunto de solicitudes aceptables para otras API junto con las respuestas a dichas solicitudes.
    
    Un microservicio es un enfoque que normalmente define cómo los desarrolladores crean una aplicación. Divide todas las funciones de la aplicación en programas modulares independientes. Como tales, facilitan tanto el proceso de desarrollo como el mantenimiento.
    
    Si bien son bastante diferentes, las API y los microservicios se usan frecuentemente juntos; porque los servicios dentro de la arquitectura de microservicios generalmente usarán API para comunicarse entre sí. Así como las aplicaciones usan una API pública para integrarse con diferentes aplicaciones, un componente (o servicio) dentro de un microservicio usa una API privada para acceder a un componente diferente dentro del mismo microservicio.
    
    En dicho microservicio, cada servicio tiene su propia API que determina las solicitudes que puede recibir junto con las respuestas. Estas API normalmente seguirán los principios REST.
    
    Los microservicios utilizan las API de manera diferente. Algunos pueden asignar varias API a un solo servicio o utilizar una API para acceder a varios servicios. No todas las aplicaciones siguen un emparejamiento uno a uno de API y servicio.
    
    Las API prácticamente tendrán usos más allá de los microservicios. Las API web permitirán el intercambio de datos entre diferentes sistemas, lo cual es necesario para que muchas aplicaciones web funcionen de manera eficiente. Además, las API también se pueden utilizar para fines internos sin necesidad de implementar un sistema de microservicio
    
- ¿QUÉ SON LAS API RESTFUL?
    
    Una API REST (también llamada API"RESTful") es un tipo específico de API que sigue estas pautas:
    
    - Cliente: una persona o programa que utiliza la API. El cliente realiza solicitudes a la API para recuperar alguna información o cambiar algo.
    - • Recurso: cualquier dato que la API puede proporcionar al cliente. Cada recurso tiene un nombre único, llamado identificador de recurso.
    - • Servidor: lo utiliza la aplicación que recibe las solicitudes del cliente y contiene los recursos que el cliente desea

![image.png](image%2048.png)




---
# References
## Father
## child