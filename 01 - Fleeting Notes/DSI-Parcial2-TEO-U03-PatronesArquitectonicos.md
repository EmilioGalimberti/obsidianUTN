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
# Patrones Arquitectonicos

https://www.youtube.com/watch?v=q3YQy1lJutw

[10 Diseño Arquitectónico parte 2.pdf](10_Diseo_Arquitectnico_parte_2.pdf)

<aside>
💡

esto mas verlos aplicados capaz asi es mas facil saber cuando son para sistemas distribuidos o no , ose ame ceusta saber por ejemplo porque uno en capas que es para monolitico se puede aplicar y porque tambien se puede aplicar cliente-servidor si es para sistema distribuido o una hexagonal tiene sentido aplicar una hexagonal y una de microservico??? y en esas son las mas tengo dudas

porque capaz la de eda son especificar para solucionar

tendria que ver capaz mas aplicados

- rta
    
    ¡Claro que sí! Tu pregunta es muy perspicaz y aborda una confusión común sobre los patrones arquitectónicos. La clave para entender esto es que los patrones operan en **diferentes niveles de abstracción** y responden a **diferentes tipos de problemas**, por lo que a menudo se complementan en lugar de excluirse mutuamente.
    
    Veamos cómo se pueden aplicar los patrones que mencionas, incluso si sus descripciones iniciales los asocian con sistemas monolíticos o distribuidos:
    
    ### 1. Arquitectura en Capas y Arquitectura Cliente-Servidor: La Combinación para Sistemas Distribuidos
    
    - **Arquitectura en Capas** (también conocida como *Layered Style*) es un **patrón estructural** que se enfoca en la **organización interna del software**. Su propósito es dividir la aplicación en capas horizontales (como Presentación, Lógica de Negocio, Acceso a Datos) para lograr una **alta cohesión y bajo acoplamiento** entre las responsabilidades. La regla fundamental es que cada capa solo puede comunicarse con la capa inmediatamente inferior. Se considera una **vista estática y estructural** del sistema, mostrando cómo se organiza el código y dónde se ubican los componentes. Si bien las aplicaciones que implementan este patrón **"por lo general tienden a ser monolíticas"**, esto se refiere a que la aplicación completa se empaqueta como una sola pieza.
    - **Arquitectura Cliente-Servidor** es un **estilo arquitectónico distribuido**. Su enfoque principal es la **comunicación y la interacción en tiempo de ejecución** entre dos roles fundamentales: un **proveedor (servidor)** que ofrece servicios y un **consumidor (cliente)** que los utiliza. Se desarrollan como **dos aplicaciones diferentes** que pueden usar distintas tecnologías, comunicándose a través de la red o Internet. Es una **vista dinámica** que muestra cómo interactúan los componentes para realizar una tarea. Una de sus ventajas es que los servidores pueden ser duplicados para manejar más carga.
    - **El sentido de combinarlos: Arquitectura N-Tier (o de "N Capas")**
    Aquí es donde la aparente contradicción se resuelve. La **Arquitectura N-Tier** es una **evolución del patrón en capas diseñada específicamente para sistemas distribuidos**. En este modelo, las capas lógicas (presentación, lógica de negocio, datos) que defines con la arquitectura en capas, pueden funcionar en **máquinas o servidores físicos diferentes**.
        - **Ejemplo:** La capa de presentación puede residir en el navegador del cliente (actuando como cliente), la lógica de negocio en uno o más servidores de aplicaciones (actuando como servidor para la capa de presentación, pero como cliente para la capa de datos), y la capa de datos en un servidor de base de datos (actuando solo como servidor).
        - En este caso, la **Arquitectura en Capas** te proporciona la **organización lógica interna** de tu aplicación (separando la UI, la lógica de negocio y el acceso a datos), mientras que la **Arquitectura Cliente-Servidor** (a través de su variante N-Tier) te permite **distribuir físicamente** esas capas en diferentes máquinas para mejorar la escalabilidad, el rendimiento y la especialización de cada componente. La Arquitectura N-Tier resuelve la limitación de la Cliente-Servidor básica, permitiendo que las capas intermedias también actúen como clientes y servidores.
    
    ### 2. Arquitectura Hexagonal y Arquitectura de Microservicios: Diseño Interno en un Entorno Distribuido
    
    - **Arquitectura Hexagonal** (o de Puertos y Adaptadores) es un **patrón arquitectónico** cuyo objetivo principal es **aislar el núcleo de la lógica de negocio de una aplicación de las dependencias externas**. El "hexágono" es una metáfora que ilustra que la aplicación tiene múltiples "lados" o puntos de interacción, protegiendo el **núcleo de la lógica de negocio pura y las entidades del dominio**. Utiliza **Puertos (interfaces)** definidos por el núcleo y **Adaptadores** que implementan esos puertos para conectar el núcleo con el mundo exterior (bases de datos, interfaces de usuario, APIs). La regla clave es que **todas las dependencias (flechas) deben apuntar hacia adentro, hacia el núcleo**.
    - **Arquitectura de Microservicios** es un **estilo arquitectónico distribuido**. Consiste en crear **pequeños componentes de software que solo hacen una tarea, la hacen bien y son totalmente autosuficientes**. Cada microservicio es una **mini-aplicación independiente** con su propio código y a menudo su propia base de datos. Los microservicios se comunican entre sí a través de la red, utilizando **protocolos abiertos y ligeros** como REST o colas de mensajes.
    - **El sentido de combinarlos:** La Arquitectura Hexagonal es un **patrón de diseño de APLICACIÓN, no de DESPLIEGUE**. Esto significa que su aplicación es igualmente válida y **muy beneficiosa tanto para sistemas monolíticos como para sistemas distribuidos (microservicios)**.
        - **En Microservicios, cada microservicio individual** puede (y a menudo se recomienda) ser diseñado **internamente** utilizando la Arquitectura Hexagonal.
        - **¿Por qué tiene sentido?**
            - **Robustez y Autonomía:** Asegura que la lógica de negocio de cada microservicio sea **pura y completamente desacoplada** de la tecnología subyacente (ej. la base de datos específica o el protocolo de comunicación REST/gRPC/mensajería). Si necesitas cambiar la base de datos de un microservicio, solo cambias su adaptador, no su lógica de negocio central.
            - **Testeabilidad:** El núcleo de la lógica de negocio de cada microservicio puede ser **probado en total aislamiento** de sus dependencias externas, lo que hace las pruebas unitarias y de integración mucho más rápidas y sencillas.
            - **Flexibilidad Tecnológica:** Permite que un microservicio específico pueda **adaptarse a nuevas tecnologías o requisitos** con un impacto mínimo, ya que el "cómo" se conecta con el mundo exterior está encapsulado en los adaptadores.
            - **Escalabilidad y Agilidad:** Contribuye a las ventajas de los microservicios, ya que cada servicio es más fácil de mantener, modificar y desplegar independientemente.
        - De hecho, construir un **monolito inicial siguiendo la Arquitectura Hexagonal** es una **práctica recomendada** (el "Monolith-First" de Martin Fowler), porque si en el futuro decides migrar a microservicios, el proceso de "extraer" un dominio de negocio para convertirlo en un microservicio es mucho más sencillo, ya que sus límites están claramente definidos y su núcleo está desacoplado.
    
    ### 3. Arquitectura Dirigida por Eventos (EDA)
    
    - La **Arquitectura Dirigida por Eventos (EDA)** es un **estilo arquitectónico asíncrono y distribuido**. Su objetivo es crear **aplicaciones altamente escalables** donde los componentes se comunican a través de la **producción y consumo de "eventos"** (cambios de estado significativos en el sistema).
    - Utiliza **intermediarios** (como Event Bus o Message Broker) para recibir eventos de los productores y enrutarlos a los consumidores, logrando un **total desacoplamiento** entre ellos. Los productores "disparan y olvidan", y los consumidores reaccionan a los eventos sin saber quién los produjo.
    - **¿Cuándo se aplica?** Es ideal para sistemas donde la **escalabilidad, flexibilidad y resiliencia** son críticas. Es común en sistemas basados en **microservicios**, donde los microservicios pueden comunicarse entre sí publicando y suscribiéndose a eventos en lugar de hacer llamadas directas síncronas. Esto evita los "múltiples puntos de falla" y la latencia de las llamadas síncronas entre microservicios.
    - Aunque es **especializada** y agrega complejidad en el desarrollo y la trazabilidad, su naturaleza asíncrona y distribuida la convierte en una base para sistemas de muy alto rendimiento y concurrencia. El **patrón de Mensajería** es la tecnología fundamental sobre la que se construye EDA, proporcionando las "tuberías" para el transporte asíncrono de los eventos.
    
    En resumen, los patrones arquitectónicos no son "o uno o el otro". Algunos definen cómo se estructura el código *dentro* de una unidad (como Capas o Hexagonal), mientras que otros definen cómo esas unidades se **distribuyen y comunican** a través de una red (como Cliente-Servidor o Microservicios). A menudo, se combinan para crear sistemas complejos que son a la vez **internamente organizados y eficientemente distribuidos**.
    
- rta2
    
    Sí, tu apreciación es muy acertada: **existen casos en los que no se pueden elegir ambos patrones o estilos arquitectónicos al mismo tiempo para la misma solución, ya que sus principios fundamentales son contradictorios**. En estas situaciones, te verás obligado a **elegir una de las opciones**, lo que a menudo implica realizar **compensaciones (trade-offs)** basadas en los requerimientos no funcionales (RNF) del sistema.
    
    A continuación, te presento algunos ejemplos claros donde la elección es mutuamente excluyente, o donde uno de los patrones es una evolución que busca solucionar las desventajas inherentes al otro:
    
    1. **Arquitectura Monolítica vs. Arquitectura de Microservicios**
        - **¿Por qué se excluyen?** Son estilos arquitectónicos fundamentalmente opuestos en su concepción.
            - Una **Arquitectura Monolítica** consiste en una aplicación única y autosuficiente que contiene toda la funcionalidad necesaria, donde sus componentes trabajan juntos, compartiendo los mismos recursos y memoria. Es un concepto de "todo o nada": si la aplicación está operativa, toda la funcionalidad está disponible; si no, toda la funcionalidad está inoperable.
            - Una **Arquitectura de Microservicios**, por el contrario, busca "desmenuzar" una gran aplicación en muchos componentes pequeños, totalmente autosuficientes e independientes, que realizan una única tarea. Cada microservicio puede ser desplegado, desarrollado y escalado de forma independiente.
        - **Implicación:** No puedes tener una aplicación que sea simultáneamente una única unidad compilada y desplegada, y a la vez una colección de múltiples servicios desplegables independientemente para el mismo sistema principal. Si bien se puede *evolucionar* de un monolito a microservicios, en un momento dado, la arquitectura principal de tu aplicación será una u otra.
    2. **Arquitectura Cliente-Servidor (centralizada) vs. Arquitectura Peer-to-Peer (P2P descentralizada)**
        - **¿Por qué se excluyen?** La diferencia más importante radica en su punto medular: la centralización versus la descentralización.
            - La **Arquitectura Cliente-Servidor** tiene un servidor central que provee servicios o recursos a múltiples clientes. El cliente depende completamente de la disponibilidad del servidor. La idea central es la centralización de la información y la separación de responsabilidades.
            - La **Arquitectura Peer-to-Peer (P2P)** es una red de computadoras donde todos los dispositivos actúan como cliente y servidor al mismo tiempo, sin necesidad de un servidor central (aunque puede existir en variantes híbridas). Busca la descentralización.
        - **Implicación:** Para la concepción global de tu red o sistema, elegirás si quieres un modelo centralizado con roles fijos (Cliente-Servidor) o uno descentralizado donde los nodos son iguales y colaboran directamente (P2P), ya que sus filosofías de distribución son opuestas.
    3. **Arquitectura en Capas vs. Arquitectura Hexagonal (respecto a la dirección de las dependencias de la lógica de negocio)**
        - **¿Por qué se excluyen?** Aunque ambas son arquitecturas estructurales que buscan organizar el código, difieren fundamentalmente en la dirección de las dependencias, especialmente en relación con el núcleo de la lógica de negocio.
            - En la **Arquitectura en Capas**, las dependencias fluyen generalmente de arriba hacia abajo (Presentación -> Lógica de Negocio -> Persistencia). Esto significa que la capa de lógica de negocio está acoplada a la tecnología de la capa de persistencia (ej. una base de datos específica).
            - La **Arquitectura Hexagonal (o de Puertos y Adaptadores)** propone que todas las dependencias apunten hacia adentro, hacia el núcleo de la lógica de negocio. El núcleo de la aplicación es independiente de la tecnología externa (como la base de datos o la interfaz de usuario), ya que los adaptadores son los que implementan las interfaces (puertos) definidas por el núcleo.
        - **Implicación:** Si tu objetivo principal es desacoplar completamente la lógica de negocio de la infraestructura (bases de datos, APIs externas, UI), optarás por la Arquitectura Hexagonal, lo cual contradice el acoplamiento inherente de la lógica de negocio con la capa de persistencia en la Arquitectura en Capas. La Arquitectura Hexagonal se presenta como una evolución que resuelve el principal problema de acoplamiento de la arquitectura en capas.
    4. **Coordinador de Proceso (Orquestación) vs. Arquitectura Dirigida por Eventos (Coreografía)**
        - **¿Por qué se excluyen?** Son dos enfoques diferentes para la gestión de flujos de trabajo en sistemas distribuidos.
            - El patrón **Coordinador de Proceso (Orquestación)** centraliza la lógica y secuencia de un flujo de trabajo complejo en un único componente (el Coordinador), que invoca a otros servicios en un orden definido. Actúa como un "director de orquesta".
            - La **Arquitectura Dirigida por Eventos (Coreografía)** no tiene un controlador central. En su lugar, los servicios reaccionan a eventos y emiten nuevos eventos, sin que un componente central les diga qué hacer.
        - **Implicación:** Para un flujo de negocio dado, elegirás una de estas dos estrategias. No puedes tener un controlador centralizado y un comportamiento completamente descentralizado basado en eventos para la misma orquestación. La EDA, al ser asíncrona y distribuida, introduce una complejidad significativa en la gestión de transacciones y errores que el Coordinador de Proceso (síncrono) gestiona de forma diferente.
    
    **Impacto de los Requerimientos No Funcionales (RNF)**
    La elección entre estos estilos y patrones se ve fuertemente influenciada por los **Requerimientos No Funcionales (RNF)** del sistema. En ocasiones, los RNF pueden entrar en conflicto entre sí. Por ejemplo, la búsqueda de un alto rendimiento podría favorecer componentes de grano grueso, mientras que la mantenibilidad podría beneficiarse de componentes de grano fino. Cuando esto ocurre, no hay una solución perfecta, y el arquitecto debe encontrar una "solución mediadora", lo que implica priorizar un RNF sobre otro y aceptar las desventajas de la elección.
    
    En resumen, aunque muchos patrones y estilos pueden combinarse, cuando sus principios rectores son inherentemente contradictorios (como la centralización vs. descentralización o la dirección de las dependencias en el núcleo de negocio), la elección de uno **excluye** la posibilidad de implementar el otro como la estrategia principal para esa preocupación específica.
    
</aside>

ESTO DESPUES PUEDO CONTINUAR

https://g.co/gemini/share/b706abed4d8b

DESPUES AGREGAR DE ACA

https://reactiveprogramming.io/blog/es/estilos-arquitectonicos/monolitico

https://github.com/puncsky/system-design-and-architecture/blob/master/en/145-introduction-to-architecture.md

[FanaticosDelFutbol_Arquitectura Monolítica V 1-12.pdf](FanaticosDelFutbol_Arquitectura_Monoltica_V_1-12.pdf)

Un patrón arquitectónico es una descripción abstracta de buena práctica, que se ensayó y se puso a prueba en diferentes sistemas y entornos. Debe describir cuándo es y no adecuado usarlo, así como sus fortalezas y debilidades

- Diferencia con patrones de diseño
    
    ![image.png](image.png)
    

![image.png](image%201.png)

![Domain Partition ](image%202.png)

Domain Partition 

![image.png](image%203.png)

- Big Ball of Mud
    - También conocida como Spagueti Architecture.
    - • Es el estilo arquitectónico que tiene un producto cuando no se define una arquitectura.
    - • Surge de un equipo que no tiene un plan sobre cómo se va a construir su producto.
    - • Las partes del sistema a menudo están altamente acopladas, el mantenimiento es muy difícil.
    - • Explicar cómo encaja todo a alguien nuevo es casi imposible.

Esta es la unica vista estatica:

- Arquitectura Estratificada o en capas (Layered Style) (estilo) → porque es monolitica y se puede aplicar a sistema distribuido → ejemplo Fanaticos del futbol)?✅
    
    ![Las flechas estan mal](image%204.png)
    
    Las flechas estan mal
    
    ![image.png](image%205.png)
    
    ### Resumen de la Arquitectura en Capas (Layered)
    
    La **arquitectura en capas** es un Estilo arquitectonico que Organiza el sistema en capas con funcionalidad relacionada con cada acapa. 
    
    - Este patron nos da pautas para saber como organizar mis componentes de software en capas
    - las capas son subsitemas y debo tener el criterio de que componentes de software van dentro de cada capa, y debo tener en cuenta el Bajo acomplamiento y la alta cohesion, A niveles de capas,
    - Su propósito principal es lograr un alto nivel de **cohesión** y **bajo acoplamiento**, decidiendo en qué capa se ubica cada componente.
        - Alta cohesion de la capa→ que todos los componentes esten muy relacionados con el concepto que la capa modela, por ejemplo si es la capa de presentacion deben ir todos los componentes de presentacion
        - por ejemplo hasta ahora que solo conocemos las clases de analisis en la capa de presentacion irian las boundary y en la capa de logica de negocio irian el controlador y las de entidad
    
    ### Concepto Clave
    
    La regla fundamental es que cada capa solo puede comunicarse con la capa inmediatamente inferior. Esto significa que una capa consume los servicios de la capa de abajo y provee servicios a la capa de arriba, ocultando la complejidad de las capas inferiores.
    
    - Organiza los componentes de una aplicación en una serie de capas, cada una con una responsabilidad específica.
    - Las capas más comunes son:
        - ➢Capa de presentación: responsable de manejar la entrada y salida del usuario y de mostrar la interfaz de usuario.
        - ➢Capa de Lógica de Negocio:
            - ❑Capa de aplicación: contiene la lógica de negocio de la aplicación, incluidas las reglas y procesos que gobiernan el comportamiento del sistema.
            - ❑Capa de dominio: representa los datos y los conceptos de negocio de la aplicación, y es responsable de gestionar los datos y las reglas de negocio.
        - ➢Capa de acceso a datos: responsable de acceder y manipular datos, generalmente a través de una base de datos.
        - ➢Capa de infraestructura: incluye los sistemas y tecnologías subyacentes que respaldan la aplicación, como el sistema operativo, el sistema de gestión de bases de datos y los protocolos de red
        
        ![image.png](image%206.png)
        
        - Principio: Separacion de intereses (separation of Concers -SoC)
            
            lo vemos aplicado ya que: 
            
            Separación de intereses: La funcionalidad del sistema está organizada en capas separadas y cada una se apoya sólo en los servicios ofrecidos por la capa ubicada de bajo de ella
            
            ![image.png](image%207.png)
            
            ![image.png](image%208.png)
            
            ![image.png](image%209.png)
            
            ![image.png](image%2010.png)
            
            ![image.png](image%2011.png)
            
        
    
    - Ventajas
        - Fácil de desarrollar: fácil de implementar, es muy conocido y una gran mayoría de las aplicaciones la utilizan.
        - Fácil de probar: permite probar por separada cada capa.
        - Fácil de mantener: fácil detectar el origen de un defecto para corregirlo, o identificar donde se debe aplicar un cambio.
        - Seguridad: la separación de capas permite el aislamiento de los servidores en subredes diferentes, lo que hace más difícil realizar ataques.
    - Desventajas
        - Performance: La comunicación por la red o internet es una de las tareas más lentas de un sistema, incluso, más que el mismo procesamiento de los datos, por lo que el hecho de tener que comunicarnos de capa en capa genera un degrado significativo en el performance.
        - Escalabilidad: al ser monolíticas, son difíciles de escalar, aunque es posible replicar la aplicación completa en varios nodos, lo que provoca un escalado monolítico.
        - Complejidad de despliegue: es necesario desplegar los componentes de abajo arriba, lo que crea una dependencia en el despliegue. Un pequeño cambio puede requerir el despliegue completo de la aplicación.
        - Anclado a un Stack tecnológico
        - Tolerancia a los fallos: Si una capa falla, todas las capas superiores comienzan a fallar en cascada.
    
    ### Vista y Atributos de Calidad
    
    - **Vista Estática:** Este patrón representa una **vista estática y estructural** (vista de módulo). Se enfoca en cómo se organiza el código y dónde se ubican los componentes, no en la comunicación dinámica en tiempo de ejecución.
    - **Atributos de Calidad:** Su diseño promueve directamente la **modificabilidad**, **portabilidad** y **reusabilidad**. Como las dependencias están restringidas, una capa puede ser reemplazada por otra equivalente sin afectar a las demás, siempre que su interfaz se mantenga.
    
    ### Realidad vs. Forma Pura
    
    - **Forma Pura (Platónica):** La comunicación es estrictamente con la capa adyacente.
    - **Forma Práctica (Embebida):** En la práctica, es común que esta regla se rompre y una capa "salte" para comunicarse con otras capas más profundas.
        - variantes
            
            Variantes: evitan la restricción de modo que las capas puedan comunicarse con capas de más abajo. Otras variantes usan capas compartidas, donde cada capa puede usar estas capas verticales o compartidas. Este uso tensiona la definición de capas hasta el límite. No obstante, si interpretamos esas capas compartidas como una conveniencia visual para mostrar dependencia sobre un módulo compartido, esta variante tendría más sentido.
            
            ![image.png](image%2012.png)
            
            Notas: El estilo estratificado puede variar considerablemente en su forma platónica de su forma embebida, en la práctica se pueden saltar capas hacia capas inferiores, lo cual provoca negar los atributos de calidad que son su beneficio. Aun así, es beneficiosa dado que las capas agrupan módulos en funcionalidad coherente.
            
    - **Advertencia:** El texto advierte que romper la regla de comunicación estricta **reduce o anula los beneficios de calidad** (como la modificabilidad y el bajo acoplamiento) que el patrón busca ofrecer.
    
    En resumen, es el patrón más común para separar responsabilidades y organizar el código, pero sus beneficios solo se obtienen si se respetan sus restricciones de comunicación.
    
    - Cuando se usa?
        
        ○ Al construirse nuevas facilidades sobre sistemas existentes.
        ○ Cuando el desarrollo se distribuye através de distintos equipos
        de trabajo(cada uno responsable de una capa de funcionalidad).
        ○ Cuando existe un requerimiento de seguridad multinivel
        
    - ejemplos
        
        ![image.png](image%2013.png)
        
    - VARIANTES DE DESPLIEGUE
        
        ![image.png](image%2014.png)
        
    
    ---
    
    meles
    
    ---
    
    ![image.png](image%2015.png)
    
    ![image.png](image%2016.png)
    

---

- Estilo Arquitectónico: Partición de Dominio (vista dinamica o run time)✅
    
    Separan los componentes de nivel superior por flujos de trabajo y/o dominios
    
    - ventajas
        - Modelado más de cerca de cómo funciona el negocio en lugar de hacia detalles de implementación.
        - Se alinea más estrechamente con el monolítico modular y la arquitectura de microservicios.
            - detalle
                
                **este estilo es el puente perfecto entre una arquitectura centralizada y una distribuida (como los microservicios)**.
                
                1. Puedes usar la Partición por Dominio para construir una única aplicación grande (**monolito modular**, que es centralizado) pero muy bien organizada por dentro, como la tienda con sus secciones internas.
                2. Como cada "dominio" (Ropa, Electrónica, etc.) ya es semi-independiente, si en el futuro quieres pasar a **microservicios**, es muchísimo más fácil separar cada dominio en su propio servicio distribuido.
        - El flujo de mensajes coincide con el dominio del problema
        - Fácil de migrar datos y componentes a la arquitectura distribuida
    - Desventaja
        
         • El código de personalización aparece en varios lugares
        
    - Ejemplo
        
        ![image.png](image%2017.png)
        
        La que muestra este estilo seria el de la derecha y el de la izquierda mas un layered
        
    
    En resumen: **Es un estilo arquitectónico para organizar el código según la lógica del negocio, no la lógica técnica, y su gran ventaja es que funciona muy bien para crear sistemas centralizados que son fáciles de evolucionar hacia sistemas distribuidos.**
    
- Arquitectura Hexagonal (estilo, vista dinamica o run time? disbruidos o monoliticos?)✅
    
    ---
    
    ### Arquitectura Hexagonal o de Puertos y Adaptadores
    
    ### ¿Qué es?
    
    La **Arquitectura Hexagonal**, también conocida por su nombre original y más descriptivo, **Arquitectura de Puertos y Adaptadores**, es un estilo arquitectónico cuyo objetivo principal es **aislar el núcleo de la lógica de negocio de una aplicación de las dependencias externas**, como bases de datos, interfaces de usuario, APIs de terceros o pruebas.
    
    La forma de "hexágono" no es literal; es una metáfora visual para ilustrar que la aplicación tiene múltiples "lados" o puntos de interacción, en lugar de la típica estructura en capas (arriba y abajo).
    
    El principio fundamental es: **el núcleo de la aplicación nunca debe depender de la tecnología externa.**
    
    ![image.png](image%2018.png)
    
    ### Componentes Clave
    
    - **El Núcleo (El Hexágono):**
        - Contiene la **lógica de negocio pura** y las entidades del dominio. Es el corazón de la aplicación, donde residen las reglas y los procesos que son únicos para el negocio.
        - Es completamente independiente de la tecnología. No sabe si los datos vienen de una API REST, una base de datos SQL o un archivo de texto.
        - La lógica de negocio crea puertos que se pueden conectar a varios adaptadores de forma intercambiable
    - **Puertos (Ports):**
        - punto de entrada independiente de la tecnología, determina la interfaz que permitirá a los actores externos comunicarse con la Aplicación,  independientemente de quién o qué implementará dicha interfaz. Los puertos también permiten que la Aplicación se comunique con sistemas o servicios externos, como bases de datos, intermediarios de mensajes, otras aplicaciones, etc.
        - Son la clave del desacoplamiento. Un puerto es simplemente una **interfaz** (un contrato) definida por el núcleo.
        - Especifican **qué** se puede hacer, pero no **cómo**. Por ejemplo, un puerto `RepositorioDePedidos` puede definir un método `guardar(pedido)`.
        - **Las interfaces creadas por el código de negocio se denominan puertos,** que se consideran internos tal como los define el negocio.
    - **Adaptadores (Adapters):**
        - Adaptadores iniciará la interacción con la Aplicación a través de un Puerto, utilizando una tecnología específica, por ejemplo, un controlador REST representaría un adaptador
        que permite a un cliente comunicarse con la Aplicación. Pueden existir tantos Adaptadores para un mismo Puerto como sean necesarios sin que esto represente un
        riesgo para los Puertos o la propia Aplicación.
        - Son la "plomería" que conecta el núcleo con el mundo exterior. Son las **implementaciones concretas** de los puertos.
        - Su trabajo es **traducir** la comunicación entre el formato del mundo exterior y el formato del núcleo de la aplicación.
        - **Los adaptadores representan código externo que cierra la brecha entre el puerto y el resto** del código del lado del usuario o del servidor
    - resumen
        
        ![image.png](image%2019.png)
        
    
    ---
    
    - Permite que la entrada de usuarios o sistemas externos llegue en un Puerto a través de un Adaptador, y permite que la salida se envíe desde la Aplicación a través de un Puerto a un Adaptador.
    - Aplicación: representada por un hexágono que recibe comandos o consultas en los Puertos y envía solicitudes a otros actores externos, como bases de datos, también a través de los Puertos
    
    ![image.png](image%2020.png)
    
    - DRIVING SIDE VS. DRIVEN SIDE
        
        Para entender el flujo, se distinguen dos "lados" del hexágono:
        
        - **Lado Conductor (Driving Side / Adaptadores Primarios):**
            - Son los que **inician una acción en la aplicación**. Son los que "conducen" el núcleo.
            - **Ejemplos:** Un controlador de API REST que recibe una petición HTTP, una interfaz de línea de comandos, o una prueba automatizada que llama a un caso de uso.
            - **Flujo:** El adaptador primario (ej. el controlador) utiliza un puerto (interfaz) que es **implementado por el núcleo**.
            - Los actores conductores (o primarios) son los que inician la interacción y siempre están representados en el lado izquierdo. Por ejemplo, un adaptador de conducción podría ser un controlador que es el que toma la entrada (del usuario) y la pasa a la Aplicación a través de un Puerto.
            - Los Adaptadores de conducción utilizarán un Puerto y un Servicio de Aplicación implementará la Interfaz definida por el Puerto, en este caso tanto la interfaz como la implementación del Puerto están dentro del Hexágono.
        - **Lado Conducido (Driven Side / Adaptadores Secundarios):**
            - Son los que **son utilizados por la aplicación** para realizar una acción externa. Son "conducidos" por el núcleo.
            - **Ejemplos:** Un repositorio que se comunica con una base de datos, un cliente que llama a una API de un tercero, un servicio que publica un mensaje en una cola.
            - **Flujo:** El núcleo utiliza un puerto (interfaz) que es **implementado por el adaptador secundario** (ej. el repositorio).
            - Los actores conducidos (o secundarios) son aquellos a los que la Aplicación “impulsa a comportarse”. Por ejemplo, la aplicación llama a un adaptador de base de datos para que obtenga un determinado conjunto de datos de la persistencia
            - Los adaptadores conducidos implementarán el Puerto y un Servicio de Aplicación lo utilizará; en este caso el Puerto está dentro del Hexágono, pero la implementación está en el Adaptador, por lo tanto, fuera del Hexágono.
        
        ![image.png](image%2021.png)
        
        ![image.png](image%2022.png)
        
        ![image.png](image%2023.png)
        
    - FLUJO
        
        ![image.png](image%2024.png)
        
    - Aplicación del principio de Inversión de Dependencias
        
        ![image.png](image%2025.png)
        
        ![image.png](image%2026.png)
        
        Imagina el núcleo como un hexágono en el centro. Las dependencias (las flechas) siempre deben apuntar **hacia adentro**, hacia el núcleo.
        
        Esto se logra aplicando el **Principio de Inversión de Dependencias**: el código de bajo nivel (infraestructura, como una base de datos) depende de las abstracciones (los puertos) definidas por el código de alto nivel (el núcleo).
        
        ●La Arquitectura Hexagonal propone que nuestro dominio sea el núcleo de las capas y que este no se acople a nada externo.
        ●Mediante el principio de Inversión de Dependencias nos acoplamos a contratos (interfaces o puertos) y no a implementaciones concretas
        
        ![image.png](image%2027.png)
        
        ---
        
        ![image.png](image%2028.png)
        
    - Ventajas
        
        ![image.png](image%2029.png)
        
        ![image.png](image%2030.png)
        
        - **Independencia Tecnológica:** El núcleo de la aplicación puede existir y funcionar sin una base de datos o una interfaz de usuario. Puedes cambiar de una base de datos MySQL a una PostgreSQL o MongoDB simplemente cambiando el adaptador, sin tocar una sola línea de la lógica de negocio.
        - **Alta Testeabilidad:** El núcleo, al no tener dependencias externas, puede ser probado con pruebas unitarias de forma rápida y sencilla, sin necesidad de levantar una base de datos o un servidor web.
        - **Mantenibilidad y Evolución:** Es mucho más fácil mantener y hacer evolucionar la aplicación. Las tecnologías externas cambian rápidamente, y esta arquitectura permite adaptarse a esos cambios con un impacto mínimo.
        - **Desarrollo en Paralelo:** Un equipo puede trabajar en el núcleo de la aplicación mientras otros equipos trabajan en diferentes adaptadores (el de la UI, el de la base de datos, etc.).
    - PASOS PARA APLICAR LA ARQUITECTURA HEXAGONAL
        
        ![image.png](image%2031.png)
        
    - cuando utilizar?
        
        ![image.png](image%2032.png)
        
    
    ### Ejemplo Práctico
    
    Imagina una aplicación para gestionar tareas:
    
    - **Núcleo:** Contiene la lógica para `CrearTarea`, `CompletarTarea`, etc. Define dos puertos:
        - `PuertoDeEntradaTareas` (interfaz con el método `crear(datosDeTarea)`).
        - `PuertoDeSalidaTareas` (interfaz con el método `guardar(tarea)`).
    - **Adaptador Primario (Conductor):** Un `ControladorRestTareas` recibe una petición POST. Llama al método `crear()` del `PuertoDeEntradaTareas` (implementado por el núcleo).
    - **Adaptador Secundario (Conducido):** Una clase `RepositorioSqlTareas` implementa la interfaz `PuertoDeSalidaTareas`. Cuando el núcleo necesita guardar la tarea, invoca el método `guardar()`, y este adaptador lo traduce a una sentencia `INSERT` de SQL.
    
    ejemplo 2
    
    ![image.png](image%2033.png)
    
    EJEMPLO
    
    ![image.png](image%2034.png)
    
    Ejemplo
    
    ![image.png](image%2035.png)
    
    ![image.png](image%2036.png)
    
    - es un patron o un estilo?,
        
        Es una excelente pregunta, porque la línea entre "patrón" y "estilo" es a menudo borrosa y tema de debate académico.
        
        En el caso de la **Arquitectura Hexagonal**, se la considera más comúnmente un **patrón arquitectónico**.
        
        Aquí te explico la diferencia y el porqué:
        
        - **Estilo Arquitectónico:** Es una idea o filosofía de alto nivel sobre cómo estructurar un sistema. Describe las restricciones generales y los componentes principales. Piensa en "Cliente-Servidor" o "Arquitectura en Capas" como estilos. Definen una *forma* general de construir.
        - **Patrón Arquitectónico:** Es una **solución concreta y reutilizable** a un problema recurrente dentro de un contexto. Es como una receta o un plano detallado.
        
        La Arquitectura Hexagonal (o de Puertos y Adaptadores) es considerada un **patrón** porque ofrece una solución muy específica y detallada al problema de acoplamiento entre la lógica de negocio y la infraestructura externa. No solo dice "separa las cosas", sino que te dice exactamente *cómo* hacerlo:
        
        1. Define **Puertos** (interfaces) en tu núcleo de negocio.
        2. Crea **Adaptadores** que implementen esos puertos para conectar la tecnología externa.
        3. Aplica el **Principio de Inversión de Dependencias** para que todo apunte hacia el núcleo.
        
        Es una receta muy clara.
        
        **En resumen:** Aunque tiene la visión y los principios de un "estilo", se le llama "patrón" porque ofrece una solución muy específica y reutilizable (Puertos y Adaptadores) para resolver el problema del acoplamiento. La mayoría de los expertos, incluido su creador (Alistair Cockburn), se refieren a él como un patrón.
        
    - es para distribuidos o monoliticos?
        
        La respuesta es: **para ambos**. Y esa es una de sus mayores fortalezas.
        
        La Arquitectura Hexagonal no se preocupa de si tu aplicación se despliega como una sola unidad (monolito) o como múltiples servicios (distribuido). Su único objetivo es **proteger tu lógica de negocio** del mundo exterior.
        
        Veamos cómo aplica en cada caso:
        
        ### 1. En Sistemas Monolíticos
        
        Aplicar la arquitectura hexagonal en un monolito es una práctica excelente para crear lo que se conoce como un **"monolito bien estructurado" o "modular"**.
        
        - **Beneficio:** Evitas el caos del "big ball of mud" (la gran bola de lodo), donde todo está mezclado. Aunque todo el código se ejecuta en un solo proceso, la lógica de negocio (el núcleo) está perfectamente aislada y no sabe nada sobre el framework web que usas, ni sobre la librería específica de la base de datos.
        - **Resultado:** Tienes un monolito mucho más fácil de mantener, probar y evolucionar a largo plazo.
        
        ### 2. En Sistemas Distribuidos (Microservicios)
        
        Es la combinación perfecta. En este escenario, **cada microservicio individual se diseña como un hexágono independiente**.
        
        - **Beneficio:** Asegura que cada microservicio sea robusto y autónomo. El núcleo del microservicio de "Pagos" no se preocupa si es invocado a través de una API REST o por un mensaje de Kafka. Tampoco le importa si guarda sus datos en una base de datos PostgreSQL o DynamoDB.
        - **Resultado:** Cada servicio es tecnológicamente flexible y se puede cambiar o actualizar su infraestructura (base de datos, sistema de mensajería, etc.) sin tocar su lógica de negocio central.
        
        ### El Puente Perfecto entre Monolito y Microservicios
        
        Esta es la razón por la que es tan valorada hoy en día. Si construyes tu monolito inicial siguiendo la arquitectura hexagonal, ya tienes el trabajo de separación de dominios de negocio hecho.
        
        Si en el futuro decides que tu aplicación ha crecido demasiado y quieres migrar a microservicios, el proceso es inmensamente más sencillo. "Extraer" un dominio de negocio para convertirlo en un microservicio es mucho más fácil porque sus límites ya están claramente definidos por los puertos y el núcleo está completamente desacoplado.
        
        **En resumen: la Arquitectura Hexagonal es un patrón de diseño de APLICACIÓN, no de DESPLIEGUE. Funciona excepcionalmente bien en ambos mundos, aportando organización al monolito y robustez e independencia a los microservicios.**
        

- Comparacion de ESTILOS arquitectectonicos (layerd vs hexagonal)✅
    
    ¡Excelente pregunta! Esta es una de las comparaciones más importantes en el diseño de software moderno. Aunque ambas arquitecturas buscan organizar el código, lo hacen con filosofías fundamentalmente diferentes.
    
    Aquí tienes un resumen comparativo entre la Arquitectura Hexagonal y la Arquitectura en Capas.
    
    ### La Diferencia Fundamental: Dirección de las Dependencias
    
    La diferencia clave y más importante entre ambas es la **dirección en que apuntan las dependencias**:
    
    - En la **Arquitectura en Capas**, las dependencias fluyen en una sola dirección, generalmente de arriba hacia abajo. La lógica de negocio (capa de dominio) depende de la capa de acceso a datos. **Tu negocio depende de la base de datos.**
    - En la **Arquitectura Hexagonal**, todas las dependencias apuntan **hacia adentro**, hacia el núcleo de la lógica de negocio. La capa de acceso a datos depende de una abstracción definida por el negocio. **La base de datos depende de tu negocio.**
    
    Este cambio, aunque sutil, tiene implicaciones enormes.
    
    ### Tabla Comparativa
    
    | Característica | Arquitectura en Capas (Layered) | Arquitectura Hexagonal (Ports & Adapters) |
    | --- | --- | --- |
    | **Metáfora Principal** | Una torta de capas. | Un núcleo con puertos y adaptadores (como un enchufe de pared). |
    | **Estructura** | **Horizontal**. Capas apiladas una sobre otra (Presentación, Lógica, Datos). | **Adentro-Afuera**. Un núcleo de negocio aislado del mundo exterior. |
    | **Regla de Dependencia** | **De arriba hacia abajo**. La capa de UI depende de la de Lógica, y la de Lógica depende de la de Datos. | **Hacia adentro**. Todo depende del Núcleo de Negocio. El núcleo no depende de nada externo. |
    | **Acoplamiento** | **Alto**. La lógica de negocio está acoplada a la tecnología de la base de datos y al framework de la UI. | **Bajo**. La lógica de negocio es pura y está completamente desacoplada de cualquier tecnología externa. |
    | **Rol de la Base de Datos** | Es una **capa fundamental** en la base del sistema. Todo se construye sobre ella. | Es un **"detalle" de infraestructura**. Un simple "plugin" o adaptador que se puede cambiar en cualquier momento. |
    | **Testeabilidad** | **Más difícil**. Para probar la lógica de negocio, a menudo necesitas una base de datos real o mocks complejos. | **Muy fácil**. El núcleo se puede probar en total aislamiento, ya que no tiene dependencias externas. Es extremadamente rápido. |
    
    ### Analogía Visual
    
    ![image.png](image%2037.png)
    
    - **Arquitectura en Capas:** Piensa en un edificio. La **cimentación** (base de datos) es lo primero y lo más fundamental. Sobre ella construyes la **estructura** (lógica de negocio) y finalmente la **decoración** (la UI). No puedes cambiar la cimentación sin demoler todo el edificio.
    - **Arquitectura Hexagonal:** Piensa en una **toma de corriente (enchufe) en la pared**.
        - El **Núcleo** es la red eléctrica de la casa.
        - El **Puerto** es la forma del enchufe (la interfaz estándar).
        - El Adaptador es el cargador de tu teléfono.
            
            A la red eléctrica (tu negocio) no le importa si enchufas un cargador de iPhone, de Samsung o una lámpara. Mientras el adaptador cumpla con la interfaz del puerto (el enchufe), todo funciona. Puedes cambiar de teléfono (tecnología) sin llamar a un electricista para que cambie el cableado de tu casa (lógica de negocio).
            
    
    ### ¿Cuándo usar cada una?
    
    - **Usa la Arquitectura en Capas si:**
        - Estás construyendo una aplicación simple o estándar (ej. un CRUD básico).
        - La velocidad de desarrollo inicial es la máxima prioridad y no prevés grandes cambios tecnológicos.
        - Estás trabajando con frameworks que la promueven fuertemente por defecto (como los primeros frameworks MVC).
    - **Usa la Arquitectura Hexagonal si:**
        - Estás construyendo una aplicación compleja y de larga duración.
        - La **mantenibilidad**, la **testeabilidad** y la **independencia tecnológica** son críticas.
        - Anticipas que la tecnología podría cambiar en el futuro (ej. cambiar de base de datos, exponer la lógica a través de una nueva API, etc.).
        - Quieres una base sólida para una posible migración de monolito a microservicios.
    
    En resumen, la Arquitectura Hexagonal es una evolución de la arquitectura en capas que resuelve su principal problema: el acoplamiento de la lógica de negocio con la infraestructura. Requiere un poco más de disciplina al principio, pero ofrece beneficios inmensos a largo plazo en aplicaciones complejas.
    

---

Para arqui distribuidas:

- Sistemas Distribuidos
    
    ![image.png](image%2038.png)
    

Vistas Dinamicas: Runtime

- Arquitecturas Cliente Servidor
    
    ![image.png](image%2039.png)
    
    - Arquitecturas Cliente Servidor - Dos capas✅
        - La aplicación es modelada como un conjunto de servicios que son provistos por servidores y un conjunto de clientes que usan esos servicios
        - Los clientes conocen a los servidores y deben saber cómo buscarlos, pero los
        servidores no necesitan conocer a los clientes.
        - Clientes y Servidores son procesos lógicos.
        - • Los clientes inician la comunicación.
        - • Los servidores no conocen la identidad de los clientes hasta que se han contactado
        
        o Clientes y Servidores: Los clientes son las aplicaciones que hacen solicitudes de servicio, y los servidores son las que proporcionan esos servicios. Los clientes saben cómo encontrar a los servidores, pero los servidores no saben nada de los clientes hasta que los contactan.
        
        es gracias a  Una red que permite a los clientes acceder a esos servicios. Los clientes deben saber que los servidores están disponibles pero no conocen la existencia de otros clientes.
        
        ○ Un modelo de sistema distribuido muestra cómo los datos y el procesamiento se distribuyen a lo largo de varios procesadores.
        
        Esquema:
        
        ![Caso de un servidor conectado con dos clientes. Los clientes pueden iniciarla comunicación peronoel servidor.El servidor no conoce la identidad de los clientes hasta que se conectan](image%2040.png)
        
        Caso de un servidor conectado con dos clientes. Los clientes pueden iniciarla comunicación peronoel servidor.El servidor no conoce la identidad de los clientes hasta que se conectan
        
        estructura lso componentes de sofware clasificandolos en dos tipos
        
        - componente de tipo cliente
            - solo pueden hacer peticiones
        - componente de tipo servidor
            - solo pueden atender
            - OJO: No confundir con responder, si puede responder, no puede hacer peticiones
        
        por ejemplo: componente de software que hace una peticion al la base de datos, la base de datos siempre va a ser un componente de tipo servidor, atiende peticiones
        
        los roles son fijos
        
        este patron es de tipo de vista dinamica, a diferencia del anterior intenta mostrar los vinculos/Relaciones , a diferencia de que el layated solo muestra organizacion
        
        - cuando se utiliza
            
            ![image.png](image%2041.png)
            
            ![image.png](image%2042.png)
            
        - o Ventajas:
            
            ▪ Escalabilidad: Los servidores pueden ser replicados para manejar más usuarios o
            tareas.
            ▪ Centralización: Los datos y servicios pueden ser centralizados y protegidos.
            o Se usa para aplicaciones que necesitan manejar cargas variables o donde se requiere
            protección centralizada de datos.
            
            ![image.png](image%2043.png)
            
            ![image.png](image%2044.png)
            
        - o Desventajas:
            
            ▪ Dependencia del servidor: Si el servidor tiene problemas, todos los clientes afectadospueden sufrir.
            
        
        ---
        
        o Comunicación Sincrónica: Los clientes hacen una petición y esperan una respuesta de los servidores.
        
        ---
        
        ![image.png](image%2045.png)
        
    - Arquitctura Cliente Servidor - Tres Capas✅
        
        ![image.png](image%2046.png)
        
    
    ### Arquitectura Cliente Servido & N-Tier(n capas)✅
    
    ![image.png](image%2047.png)
    
    el problema que tenemos con la cliente servidor basica es que es muy simple y limita que solo los clientes son capas de presentacion y los servidor base de datos que son quienes pueden cumplir esos dos roles
    
    Entonces este tiene la adaptacion que las capas del medio pueden responder y pedir
    
    por ejemplo la capa de base de datos seria toda la de la derecha que es siempre servidor
    
    la capa de logica de negocio es servidor para atender las peteciones de la capa de presentacion pero a su vez es cliente, para hacer peticiones a la base de datos
    
    - • Propiedades clave :
        - Separación de Intereses: capas diferentes y claramente divididos para presentación, negocios y manejo de datos.
            - Cada nivel (tier) tiene responsabilidades definidas,ej: el primer nivel maneja
            la interacción con el usuario, la segunda la lógica de negocio, la tercera maneja la persistencia.
        - • Comunicaciones sincrónicas: la comunicación entre niveles es pedido respuesta sincrónica. Los pedidos emanan en una única dirección del nivel del cliente a los niveles web y de lógica de negocio al nivel EIS Cada nivel espera la respuesta del otro nivel antes de proseguir.
        - • Distribución flexible: no hay restricciones para la distribución multi- capas de la aplicación. Todas las capas pueden correr en la misma máquina o en su propia máquina. En aplicaciones WEB, el cliente usualmente corre en un browser de una PC de escritorio de un. usuario, comunicándose remotamente con Internet con componentes a nivel web.
            - Losniveles (tiers) generalmente están alojados en un hardware específico
            pero un nodo de hardware puede albergar varios niveles(tiers)
    - ventajas
        
        ![image.png](image%2048.png)
        
    - Desventajas
        
        ![image.png](image%2049.png)
        
    
    ![image.png](image%2050.png)
    
    otro ejemplo
    
    ![image.png](image%2051.png)
    
    ### Arquitectura Maestro-esclavo (master-slave)
    
    ### ¿Qué es?
    
    Es un patrón de arquitectura para sistemas distribuidos donde un proceso central, el **Líder (Maestro)**, distribuye y coordina el trabajo entre múltiples procesos subordinados, los **Seguidores (Esclavos)**. Este modelo es especialmente útil para sistemas que necesitan realizar cálculos idénticos o similares de forma repetida sobre diferentes conjuntos de datos.
    
    - Se usan comúnmente en sistemas de tiempo real donde es importante cumplir con los tiempos de procesamiento
    - Se usa cuando es posible predecir el procesamiento distribuido que se requiere y cuando se puede asignar fácilmente el procesamiento a los procesadores esclavos.
    
    ### Roles de los Componentes
    
    1. **Líder (Maestro):**
        - Es el "cerebro" y punto de control central del sistema.
        - **Divide el trabajo:** Parte una tarea compleja en subtareas más pequeñas.
        - **Distribuye las tareas:** Asigna estas subtareas a los diferentes seguidores.
        - **Coordina y monitorea:** Supervisa el estado de los seguidores y gestiona la comunicación.
        - **Agrega los resultados:** Recolecta los resultados parciales de los seguidores y los combina para obtener la solución final.
    2. **Seguidores (Esclavos):**
        - Son los "trabajadores" que ejecutan las tareas.
        - **Reciben y ejecutan:** Aceptan una tarea específica del líder y la procesan.
        - **Devuelven el resultado:** Una vez finalizada la tarea, envían el resultado de vuelta al líder.
        - **Funcionan en paralelo:** Cada seguidor trabaja de forma independiente y, por lo general, no se comunica con otros seguidores.
    
    ### Diagrama Conceptual
    
    Imagina un diagrama simple donde una caja central ("Líder") tiene flechas que salen hacia varias cajas periféricas ("Seguidor 1", "Seguidor 2", "Seguidor 3", ...). Las flechas de ida representan la distribución de tareas y las de vuelta, la recolección de resultados.
    
    ![image.png](image%2052.png)
    
    ### Ventajas y Casos de Uso
    
    Este patrón es ideal para:
    
    - **Computación Paralela:** Es perfecto para problemas que pueden ser divididos en muchas tareas independientes que se ejecutan simultáneamente, acelerando enormemente el procesamiento total.
    - **Sistemas de Tiempo Real:** Como mencionan tus fuentes, es muy común en sistemas que deben cumplir con plazos estrictos (ej. control industrial, robótica), donde se puede asignar un procesador a cada tarea específica (un seguidor para leer sensores, otro para controlar un motor, etc.).
    - **Tolerancia a Fallos:** Si un seguidor falla, el líder puede detectarlo y reasignar su tarea a otro seguidor disponible. Esto hace que el sistema sea más robusto. (Ej: replicación de bases de datos, donde el Líder es la base de datos principal y los Seguidores son las réplicas).
    - **Simplicidad:** Es uno de los modelos más simples para organizar un sistema distribuido cuando el flujo de trabajo es predecible y fácil de dividir.
    
    ### Desventajas y Limitaciones
    
    - **Punto Único de Fallo (Single Point of Failure):** La mayor debilidad es el líder. Si el proceso líder falla, todo el sistema se detiene.
    - **Cuello de Botella en el Rendimiento:** Todo el trabajo y la comunicación pasan a través del líder. Si hay demasiados seguidores o las tareas son muy rápidas, el líder puede sobrecargarse y convertirse en un cuello de botella.
    - **Comunicación Limitada:** El modelo no es adecuado para problemas donde los trabajadores (seguidores) necesitan comunicarse entre sí para resolver la tarea.
    
    - Cuando se utiliza
        
        ![image.png](image%2053.png)
        
    
    ### Ejemplo Práctico (Control de Tráfico)
    
    El ejemplo del sistema de control de tráfico de tus apuntes es perfecto:
    
    - **Seguidores:** Cada sensor en las calles actúa como un seguidor. Su única tarea es medir el flujo de vehículos y enviar esa información.
    - **Líder:** Un ordenador central en una sala de control actúa como el líder. Recibe los datos de todos los sensores, los procesa en conjunto, toma decisiones (ej. cambiar la secuencia de los semáforos) y envía las órdenes a los actuadores de los semáforos.
    
    ![image.png](image%2054.png)
    
    ![image.png](image%2055.png)
    
    ### Peer to Peer (p2p) (estilo)
    
    ### Arquitectura Peer-to-Peer (P2P)
    
    ### ¿Qué es?
    
    La arquitectura Peer-to-Peer (P2P) o "entre pares" describe un **sistema distribuido y descentralizado** donde no existe una jerarquía fija de clientes y servidores. En su lugar, todos los nodos de la red son "pares" (peers) con las mismas capacidades y responsabilidades.
    
    El principio fundamental es que **cada nodo puede actuar como cliente y como servidor al mismo tiempo**: puede solicitar servicios o recursos de otros nodos, y simultáneamente, ofrecer sus propios servicios y recursos al resto de la red.
    
    - El resultado es un conjunto de nodos operando como pares donde cada nodo puede pedir o proveer servicios a cualquier otro nodo
    
    ![image.png](image%2056.png)
    
    ### Ventajas Generales de la Arquitectura P2P
    
    - **Alta Escalabilidad:** La capacidad total del sistema crece a medida que se añaden más nodos. Más nodos significan más recursos disponibles (almacenamiento, ancho de banda, poder de cómputo).
    - **Tolerancia a Fallos y Disponibilidad:** Al no depender de un único servidor central (especialmente en el modelo puro), la red puede seguir funcionando aunque varios nodos se desconecten. Los recursos suelen estar replicados en múltiples pares.
    - **Descentralización:** Evita la dependencia y el control de una autoridad central.
    - **Balanceo de Carga:** La carga de trabajo se distribuye de forma natural entre todos los pares, evitando los cuellos de botella típicos de un servidor central.
    - **Privacidad:** La comunicación directa entre pares y las búsquedas distribuidas pueden ofrecer un mayor nivel de privacidad para los usuarios.
    
    ### Desventajas y Desafíos
    
    - **Complejidad:** Diseñar, desarrollar y mantener aplicaciones P2P es considerablemente más complejo que en un modelo cliente-servidor.
    - **Seguridad y Confianza:** Es difícil verificar la identidad de los otros pares y confiar en ellos. Las redes P2P son un entorno propicio para la distribución de malware y contenido malicioso, ya que no hay una entidad central que valide los recursos.
    - **Control de Contenidos:** Es casi imposible controlar o moderar la información que se comparte en la red, lo que plantea problemas de legalidad y piratería.
    - **Tráfico de Red:** En los modelos puros, la búsqueda de recursos puede generar un tráfico de red excesivo y poco eficiente.
    - ¿Cuándo se recomiendan?
        
        ![image.png](image%2057.png)
        
    
    ### Modelos Arquitectónicos de P2P
    
    ![image.png](image%2058.png)
    
    Las redes P2P no son todas iguales. Se pueden estructurar principalmente de dos maneras:
    
    **1. P2P Puro (Totalmente Descentralizado)**
    
    En este modelo, no hay ningún servidor central. Todos los nodos son completamente iguales. Para encontrar un recurso (como un archivo), un nodo le pregunta a sus vecinos, quienes a su vez le preguntan a sus propios vecinos, y así sucesivamente hasta que se encuentra el recurso.
    
    - **Diagrama:** Imagina una red de nodos interconectados como una telaraña. No hay un punto central; todos los nodos se conectan directamente con varios otros.
        
        ![image.png](image%2059.png)
        
    - **Ventajas:**
        - **Máxima tolerancia a fallos:** La caída de varios nodos no afecta el funcionamiento general de la red. Es extremadamente robusta.
    - **Desventajas:**
        - **Ineficiencia:** Encontrar algo puede generar una enorme cantidad de tráfico de red (una "inundación" de solicitudes), ya que la misma búsqueda se procesa en muchísimos nodos.
        - **Difícil de gestionar.**
    
    **2. P2P Híbrido (Semi-centralizado)**
    
    Este modelo utiliza un nodo especial (a veces llamado "super-par" o "servidor de arranque") que actúa como un directorio o coordinador. Los nodos se conectan a este servidor central para saber qué otros pares están en la red o quién tiene un recurso específico. Una vez que obtienen esa información, la comunicación para la transferencia de datos se realiza directamente de par a par.
    
    - **Diagrama:** Imagina varios nodos periféricos y un nodo central. Todos los nodos periféricos tienen una conexión con el nodo central (para buscar) y también pueden crear conexiones directas entre ellos (para descargar).
        
        ![image.png](image%2060.png)
        
    - **Ventajas:**
        - **Mucho más eficiente:** La búsqueda de recursos es rápida y no satura la red.
    - **Desventajas:**
        - **Punto de fallo:** Si el servidor central falla, la red se vuelve inoperable o, al menos, es imposible que nuevos pares se unan o encuentren recursos.
        - **Menos descentralizado.**
    
    ### Ejemplos Clásicos
    
    - **Napster (Híbrido):** El primer gran fenómeno P2P. Usaba servidores centrales para indexar qué usuario tenía qué canción, pero la descarga era directa entre pares.
    - **BitTorrent (Híbrido):** Utiliza archivos `.torrent` que apuntan a "trackers" (servidores coordinadores) para encontrar a otros pares, pero la transferencia de los trozos de archivo es totalmente P2P.
    - **Gnutella, Kazaa (Puro):** Redes de intercambio de archivos que funcionaban sin servidores centrales.
    - **Criptomonedas (Bitcoin, Ethereum):** Son el ejemplo moderno más claro de un sistema P2P puro. La red de nodos valida transacciones y mantiene una copia del libro contable (la blockchain) sin ninguna autoridad central.
    
    ![image.png](image%2061.png)
    
    hay un ej de esto en la uv, puede servir para estudiar
    
    ventajas,deventajas
    
    (respuestas del power de meles,
    falacias del sistema distribuido
    
    caracteristicas de sistemas distribuidos final oral
    

(el cliente servidor es el que tiene mas cosas y explica mas facil un sistema distribuido)

---

# Motivación de estilos para aplicaciones web/mobile

- Una solicitud del usuario final/cliente para cambiar una característica de la interfaz de usuario por variasrazones como facilidad de uso, adaptabilidad, etc.
- Mover un sistema de una plataforma a otra.
- Actualizaciones del sistema a nuevas versiones.
- Cambios en el diseño de la base de datos
    - nacen de estos req
        
        ![image.png](image%2062.png)
        

## Estilos para el Diseño de Aplicaciones Web

![image.png](image%2063.png)

- Arquitectura MVC(Modelo-Vista-Controlador)
    
    ![image.png](image%2064.png)
    
    ### Arquitectura Modelo-Vista-Controlador (MVC)
    
    ### ¿Qué es?
    
    El Modelo-Vista-Controlador (MVC) es uno de los patrones de arquitectura más influyentes y utilizados, diseñado para organizar el código de una aplicación separando sus responsabilidades en tres componentes lógicos interconectados.
    
    El objetivo principal es la **separación de intereses (separation of concerns)**: separar la lógica de negocio y la gestión de los datos (el **Modelo**) de su representación visual y la interacción con el usuario (la **Vista**). El **Controlador** actúa como el intermediario entre ambos.
    
    ### Los Tres Componentes
    
    - **1. Modelo (Model) →  objeto aplicación**
        - **El Cerebro y los Datos:** Es el corazón de la aplicación. Contiene los datos (el estado) y la lógica de negocio (las reglas sobre cómo manipular esos datos).
        - **Independiente de la UI:** No sabe ni le importa cómo se mostrarán los datos. Su única tarea es gestionar la información correctamente.
        - **Notificador:** Cuando sus datos cambian, el Modelo notifica a todas las Vistas que están "escuchando" para que puedan actualizarse.
        
        <aside>
        💡
        
        - Desacopla el modelo de las vistas estableciendo un modelo de suscripción/ notificación
        
        este a diferencia del pub/sub es que este actualiza las vistas obligadamente, a diferencia del otro que los suscripotr tienen que manifestar el deso de escuchar a un topico
        
        tambi mvc sync y pub/sub async
        
        </aside>
        
    - **2. Vista (View)**
        - **La Interfaz de Usuario (UI):** Es todo lo que el usuario ve y con lo que interactúa (botones, formularios, gráficos, etc.).
        - **Representación del Modelo:** Su única función es solicitar datos del Modelo y presentarlos al usuario de una manera específica. Puede haber múltiples vistas para un mismo modelo (ej. un gráfico de torta y una tabla mostrando los mismos datos de ventas).
        - **No contiene lógica de negocio:** La Vista no toma decisiones, solo muestra información y captura las acciones del usuario.
        - La vista debe asegurarse que su apariencia refleja el estado del modelo
        - • La vista se actualiza a sí misma.
        - Se pueden crear varias vistas de un modelo, para ofrecer diferentes presentaciones.
        - ejemplo modelo y varias vistas
            
            ![image.png](image%2065.png)
            
    - **3. Controlador (Controller)**
        - **El Intermediario:** Actúa como el "pegamento" o el "director de orquesta" entre el Modelo y la Vista.
        - define la forma en que la interfaz reacciona a la entrada del usuario
        - **Recibe la entrada del usuario:** Cuando el usuario realiza una acción en la Vista (como hacer clic en un botón), la Vista informa al Controlador.
        - **Actualiza el Modelo:** El Controlador traduce la acción del usuario en una orden para el Modelo (ej. "guardar este dato" o "borrar este registro").
    
    ![image.png](image%2066.png)
    
    ![image.png](image%2067.png)
    
    ### Flujo de Interacción Típico
    
    El diagrama que proporcionaste ilustra perfectamente el flujo de comunicación:
    
    1. El **usuario** realiza una acción en la **Vista** (ej. llena un formulario y presiona "Guardar").
    2. La **Vista** notifica al **Controlador** sobre la acción del usuario, pasándole los datos necesarios (ej. los datos del formulario).
    3. El **Controlador** recibe la petición y actualiza el **Modelo** (ej. le dice al Modelo que guarde los nuevos datos).
    4. El **Modelo** cambia su estado y **notifica** a todas las Vistas asociadas que ha habido un cambio.
    5. La **Vista**, al recibir la notificación, solicita los datos actualizados del **Modelo** y refresca su pantalla para reflejar el nuevo estado.
    
    ### Ventajas
    
    - **Separación de Intereses:** Permite que la lógica de negocio (Modelo) y la interfaz de usuario (Vista) evolucionen de forma independiente. Un diseñador puede cambiar la UI sin tocar la lógica, y un programador puede mejorar la lógica sin afectar la UI.
    - **Soporte para Múltiples Vistas:** Facilita tener diferentes representaciones de los mismos datos, y todas se actualizan automáticamente cuando los datos cambian.
    - **Desarrollo en Paralelo:** Diferentes equipos pueden trabajar en el Modelo, la Vista y el Controlador al mismo tiempo.
    - **Reutilización y Mantenibilidad:** El código es más organizado, más fácil de mantener y los componentes son más fáciles de reutilizar.
    
    ### Desventajas
    
    - **Complejidad para Proyectos Simples:** Para aplicaciones muy pequeñas y sencillas, implementar MVC puede añadir una capa de complejidad y código innecesaria, resultando excesivo.
    - **Aumento del Código:** Inevitablemente, dividir la aplicación en tres partes puede aumentar la cantidad total de archivos y código a gestionar.
    
    ### Cuando se utiliza?
    
    Se usa cuando existen múltiples formas de ver e interactuar con los datos. También se utiliza al desconocerse los requerimientos futuros para la interacción y presentación
    
    ![image.png](image%2068.png)
    
    ### Relevancia Actual
    
    MVC es la base de innumerables **frameworks de desarrollo web modernos**, como Ruby on Rails, Django (que lo llama MVT - Model-View-Template), Laravel y ASP.NET MVC. Aunque algunos frameworks más nuevos del lado del cliente (como React o Vue) utilizan variaciones (como MVVM - Model-View-ViewModel), la idea fundamental de separar la lógica de los datos de su presentación sigue siendo un pilar en el diseño de software.
    
    - es una vista dinamica?
        
        Excelente pregunta. Es un punto clave para entender bien la diferencia entre los patrones.
        
        El patrón **Modelo-Vista-Controlador (MVC)** es fundamentalmente una **vista dinámica o de comportamiento**.
        
        Aquí está el porqué:
        
        1. **Vista Estática (Estructural):** Se enfoca en **cómo se organiza el código**. Describe los componentes y sus relaciones fijas. El mejor ejemplo es la **Arquitectura en Capas**, que te dice: "El código de la presentación va en esta capa, el de la lógica en esta otra". Es como el plano de una casa, muestra dónde están las habitaciones.
        2. **Vista Dinámica (De Comportamiento):** Se enfoca en **cómo interactúan los componentes en tiempo de ejecución**. Describe el flujo de mensajes y la secuencia de eventos para realizar una tarea.
        
        El poder de MVC no está solo en tener tres componentes, sino en el **flujo de comunicación** que se produce entre ellos cuando el usuario hace algo:
        
        - El usuario interactúa con la **Vista**.
        - La Vista notifica al **Controlador**.
        - El Controlador actualiza el **Modelo**.
        - El Modelo avisa a la **Vista** que ha cambiado.
        - La Vista se refresca.
        
        Toda esa secuencia es un **comportamiento en tiempo de ejecución**. Es la descripción de cómo las partes "conversan" entre sí para funcionar.
        
        **En resumen:** Mientras que una vista estática te muestra el "qué" (qué componentes hay y cómo se agrupan), una vista dinámica como MVC te muestra el "**cómo**" (cómo colaboran esos componentes para responder a un evento).
        
    - es para monolitico o distribuido?
        
        El patrón arquitectónico Modelo-Vista-Controlador (MVC) es fundamentalmente una **vista dinámica o de comportamiento** que se enfoca en cómo interactúan los componentes de un sistema en tiempo de ejecución. Describe el flujo de mensajes y la secuencia de eventos para realizar una tarea.
        
        En este sentido, el patrón MVC es aplicable y se utiliza en **ambos tipos de sistemas**: tanto en **sistemas monolíticos** como en **sistemas distribuidos**.
        
        Aquí se detalla su aplicación:
        
        - **En Sistemas Monolíticos**: El MVC es la base de innumerables *frameworks* de desarrollo web modernos, como Ruby on Rails, Django, Laravel y ASP.NET MVC. Permite que una única aplicación grande (monolito) esté bien organizada internamente, separando claramente la lógica de negocio, la interfaz de usuario y la gestión de datos. Aunque todo el código se empaqueta como una sola pieza, MVC ayuda a mantener la **separación de responsabilidades** y facilita la **modificabilidad y testabilidad** dentro de esa unidad cohesiva.
        - **En Sistemas Distribuidos (como Microservicios)**: Aunque la arquitectura de microservicios define cómo se comunican y se despliegan los servicios de forma independiente, cada microservicio individual o la capa de interfaz de usuario de una aplicación distribuida puede utilizar internamente el patrón MVC para su propia organización. Por ejemplo, el *frontend* de una aplicación basada en microservicios podría estar diseñado con MVC para manejar su propia lógica de presentación y la interacción con el usuario, mientras se comunica con los microservicios *backend* a través de una API Gateway.
        
        En resumen, el patrón MVC se centra en la **organización interna de la aplicación o de un componente específico**, separando su lógica de negocio (Modelo), su representación visual (Vista) y la interacción del usuario (Controlador). No define si el sistema es monolítico o distribuido en sí mismo, sino que es una **herramienta para estructurar el código de una aplicación o módulo**, independientemente de su forma de despliegue.
        

---

- Service Oriented Architecture (SOA) Arquitecturas Orientadas a Servicio
    
    ![image.png](image%2069.png)
    
    ![image.png](image%2070.png)
    
    ![image.png](image%2071.png)
    
    ![image.png](image%2072.png)
    
    ![image.png](image%2073.png)
    
    - Ventajas
        
        ![image.png](image%2074.png)
        
    - Desventajas
        
        ![image.png](image%2075.png)
        

---

- Event-drivenarchitecture(EDA)
    
    ![image.png](image%2076.png)
    
    Claro, aquí tienes un resumen consolidado y estructurado del texto sobre la Arquitectura Dirigida por Eventos (EDA).
    
    ---
    
    ### Resumen de la Arquitectura Dirigida por Eventos (EDA)
    
    ### ¿Qué es?
    
    La **Arquitectura Dirigida por Eventos (EDA)** es un estilo de arquitectura de software **asíncrona y distribuida**, diseñada para construir aplicaciones altamente escalables y desacopladas. En lugar del modelo tradicional de solicitud-respuesta, en EDA los componentes del sistema se comunican a través de la producción y el consumo de **eventos**.
    
    - En una arquitectura EDA se espera que las aplicaciones lancen diversos “eventos” para que otros componentes puedan reaccionar a ellos, procesarlos y posiblemente generar nuevos eventos para que otros componentes continúen con el trabajo.
    
    Un **evento** es un cambio de estado significativo en la aplicación (ejemplo: "PedidoRealizado", "InventarioActualizado", "UsuarioRegistrado").
    
    - Un evento lo podemos definir como un cambio significativo en el estado de la aplicación, ya sea por un dato que cambio o alguna acción concreta en el sistema que merece la pena ser observada para tomar acciones en consecuencia
    
    Un sistema controlado por eventos "reacciona" a los eventos que ocurren en una interfaz de usuario o internamente.
    
    Se basa en procesadores de eventos. El flujo de eventos a través del sistema puede tener lugar de dos maneras diferentes. (Broker o Mediator)
    
    ### Componentes y Flujo de Trabajo
    
    ![image.png](image%2077.png)
    
    1. **Productor de Eventos (Event Producer):** Es el componente que origina un evento cuando ocurre algo en el sistema.
    2. **Intermediario (Event Bus / Message Broker):** Es el núcleo de la arquitectura. Es un sistema (como Apache Kafka, RabbitMQ) que recibe los eventos de los productores y los enruta a través de canales. Su función es desacoplar al productor del consumidor.
    3. **Canal de Eventos (Event Channel):** Son colas o temas (queues/topics) dentro del intermediario donde se publican los eventos de un tipo específico.
    4. **Consumidor de Eventos (Event Consumer / Processing):** Es el componente de negocio que se suscribe a un canal, "escucha" la llegada 
    5. de nuevos eventos y reacciona a ellos ejecutando una lógica específica. Este proceso puede, a su vez, generar nuevos eventos.
    
    El flujo es simple: un productor publica un evento en el intermediario sin saber (ni preocuparse por) quién lo consumirá. Los consumidores, a su vez, procesan los eventos sin saber quién los produjo.
    
    - Bajo topologia broker
        - Bajo la topología de Broker, no existe un control centralizado del procesamiento de eventos.
        - Cada procesador puede transmitir eventos propios para activar otro procesador formando una cadena de eventos.
        - No es necesario administrar las conexiones entre procesadores de eventos específicos o pasos de ejecución.
        
        ![image.png](image%2078.png)
        
    - Bajo topologa mediator
        
        Bajo la topología del Mediator hay algún control central.
        • Los mediadores de eventos controlan qué procesadores se llaman y en qué orden cuando un evento ingresa al sistema.
        
        • Puede haber múltiples mediadores de eventos que trabajen en paralelo o de forma jerárquica.
        
        ![image.png](image%2079.png)
        
    
    ### Características Clave
    
    - **Comunicación Asíncrona:** El productor "dispara y olvida". Envía el evento y continúa con su trabajo sin esperar una respuesta.
    - **Totalmente Desacoplado:** Gracias al intermediario, los componentes no dependen unos de otros, lo que aumenta la resiliencia y la flexibilidad. Si un consumidor falla, los productores y otros consumidores pueden seguir funcionando.
    - **Autonomía de los Componentes:** Cada consumidor es un micro-servicio o componente independiente que gestiona sus propias tareas.
    
    ### Ventajas
    
    - **Alta Escalabilidad:** Es el punto más fuerte. Cada componente consumidor puede ser escalado de forma independiente para manejar altas cargas de trabajo.
    - **Flexibilidad y Agilidad:** Es fácil añadir nueva funcionalidad al sistema simplemente creando un nuevo consumidor que reaccione a un evento existente. Los cambios se pueden aislar sin afectar al resto del sistema.
    - **Resiliencia:** La caída de un componente no detiene todo el sistema. El intermediario puede guardar los eventos hasta que el consumidor vuelva a estar disponible.
    - Despliegue: Debido al bajo acoplamiento entre los componentes, es posible el despliegue sin preocuparse por dependencias o precondiciones, al final, los componentes solamente se suscriben para recibir eventos y reaccionar ante ellos
    - Performance: EDA necesita pasar por una serie de pasos para completar una tarea,
    agregando retrasos en cada paso, desde colocar el Evento por parte del productor,
    esperar a que el consumidor lo tome, y generar nuevos Eventos, sin embargo, la
    naturaleza asíncrona de EDA hace que esta desventaja se supere mediante el
    procesamiento en paralelo.
    - Flexibilidad: EDA permite responder rápidamente a un entorno cambiante, debido a que cada componente procesador de eventos tiene una sola responsabilidad y está completamente desacoplado de los demás, de esta forma, si ocurre un cambio, se puede aislar en un solo componente sin afectar al resto, además, si un nuevo requerimiento es requerido, solo es necesario regresar un nuevo tipo de procesador de eventos que escuche un determinado tipo de evento.
    
    ### Desventajas y Desafíos
    
    - **Complejidad en Desarrollo y Pruebas:** La naturaleza asíncrona hace que el flujo de trabajo sea más difícil de rastrear. Probar el sistema es complejo, ya que no se puede simplemente enviar una petición y esperar un resultado para validarlo.
    - **Gestión de Transacciones:** Este es el mayor desafío. **No existen transacciones distribuidas atómicas en EDA**. Cada consumidor maneja su propia transacción. Si un proceso de negocio requiere varios pasos (eventos) y uno de ellos falla a la mitad, no hay un "rollback" automático para los pasos que ya se completaron. Esto puede llevar a inconsistencias de datos si no se implementan patrones de manejo de errores avanzados (como el patrón Saga o eventos de compensación).
    - **Sin Garantía de Procesamiento:** Si no hay ningún consumidor suscrito a un canal de eventos, los eventos enviados a ese canal simplemente se perderán o quedarán sin procesar.
    
    En conclusión, EDA es un estilo arquitectónico extremadamente poderoso para construir sistemas masivos y resilientes, pero introduce una complejidad significativa en el manejo de errores y transacciones que requiere un diseño cuidadoso y desarrolladores con experiencia en sistemas asíncronos.
    
- Arquitectura Publicar-Suscribir (publish-Suscribe
    
    ![image.png](image%2080.png)
    
    Claro, aquí tienes una explicación sobre la **arquitectura de publicación-suscripción (publish-subscribe)**, a menudo abreviada como **pub/sub**.
    
    - ¿Qué es la Arquitectura Publish-Subscribe?
        
        La arquitectura de publicación-suscripción es un patrón de mensajería en el que los componentes que envían mensajes (editores o "publishers") no están directamente acoplados a los componentes que reciben los mensajes (suscriptores o "subscribers"). En lugar de que un editor envíe mensajes directamente a un suscriptor, los publica en un canal o tema ("topic")
        
        Los suscriptores, a su vez, muestran interés en uno o más de estos temas. El intermediario se encarga de filtrar y distribuir los mensajes de los editores a todos los suscriptores interesados en ese tema específico.
        
        - Componentes independientes publican eventos y otros se suscriben a ellos.
        - Los publicantes ignoran el motivo global por el cual el evento es publicado, los suscriptores ignoran porque o quien publica el evento y dependen sólo del evento no de quien lo publica.
        - •Cada tópico puede tener más de un publicante y los publicantes pueden aparecer y desaparecer dinámicamente, lo que le da flexibilidad sobre configuraciones estáticas.
        - •Los suscriptores pueden suscribirse y des-suscribirse dinámicamente a un tópico.
        - • Aplica a elementos de tiempo de ejecución, es parte de la vista de ejecución (runtime
    - Componentes Clave
        1. **Editores (Publishers):** Son las aplicaciones o servicios que originan los mensajes. No tienen conocimiento de qué suscriptores (si los hay) recibirán sus mensajes. Simplemente envían el mensaje a un tema concreto en el intermediario.
        2. **Suscriptores (Subscribers):** Son las aplicaciones o servicios que consumen los mensajes. Se suscriben a los temas que les interesan y reciben todos los mensajes publicados en dichos temas sin saber qué editor los envió.
        3. **Temas (Topics):** Son los canales a través de los cuales se transmiten los mensajes. Actúan como una categoría o una etiqueta para los mensajes. Los editores publican en temas y los suscriptores se suscriben a ellos.
        4. • Los canales (buses) de eventos varían en las propiedades que soportan
            1. Durables: garantizan que cualquier mensaje que aceptan no se perderá durante una falla. Usualmente la durabilidad se logra escribiendo los eventos en un almacenamiento confiable, al menos temporalmente, lo que trae aparejada cierta latencia.
            2. Entrega en orden: garantizan entrega en orden o priorizada de eventos.
            3. Entrega en lotes: los eventos se acumulan en lotes para evitar cúmulos de eventos similares
        
    - ¿Cómo Funciona?
        
        El flujo de comunicación en un sistema pub/sub es el siguiente:
        
        1. **Publicación:** Un editor crea un mensaje y lo envía a un tema específico en el intermediario.
        2. **Recepción y Filtrado:** El intermediario recibe el mensaje y lo almacena. A continuación, identifica a todos los suscriptores que han mostrado interés en ese tema.
        3. **Distribución:** El intermediario envía una copia del mensaje a cada uno de los suscriptores interesados.
        4. **Consumo:** Los suscriptores reciben el mensaje y lo procesan según su propia lógica de negocio.
        
        ![image.png](image%2081.png)
        
        **Analogía:** Imagina una revista. La editorial (editor) no envía la revista directamente a cada lector (suscriptor). En su lugar, la publica. Los lectores se suscriben a la revista y un distribuidor (intermediario) se asegura de que cada suscriptor reciba su copia. La editorial no necesita saber quiénes son sus lectores, y los lectores no necesitan conocer a la editorial directamente.
        
    - Ventajas de la Arquitectura Pub/Sub
        
        ![image.png](image%2082.png)
        
        - **Desacoplamiento:** Los editores y suscriptores son independientes entre sí. Un editor puede publicar mensajes sin que haya ningún suscriptor escuchando, y un suscriptor puede empezar a escuchar en cualquier momento. Esto aumenta la modularidad y la flexibilidad del sistema.
        - **Escalabilidad:** Es fácil añadir nuevos editores o suscriptores al sistema sin afectar a los componentes existentes. Esto permite que el sistema crezca y se adapte a las nuevas demandas de forma sencilla.
        - **Flexibilidad y Resiliencia:** Si un suscriptor falla, los demás componentes del sistema pueden seguir funcionando sin interrupciones. El intermediario puede incluso guardar los mensajes para que el suscriptor los reciba una vez que se recupere.
        - **Comunicación Asíncrona:** Los editores pueden publicar mensajes y continuar con sus tareas sin esperar una respuesta. Esto mejora la capacidad de respuesta y la eficiencia general del sistema.
        - **Difusión de Eventos:** Facilita la notificación de eventos a múltiples sistemas interesados de manera simultánea y eficiente.
    - Desventajas
        - **Complejidad del Intermediario:** El "message broker" es un componente crítico. Su fallo puede afectar a todo el sistema, por lo que requiere una configuración y un mantenimiento cuidadosos para garantizar la alta disponibilidad y la fiabilidad.
        - **Garantías de Entrega:** Asegurar que un mensaje ha sido entregado y procesado puede ser más complejo que en una comunicación directa. Los sistemas pub/sub suelen ofrecer diferentes niveles de garantía de entrega (al menos una vez, como máximo una vez, exactamente una vez).
        - **Latencia:** La introducción de un intermediario puede añadir una pequeña latencia a la comunicación en comparación con las llamadas directas.
    - Casos de Uso Comunes
        
        ![image.png](image%2083.png)
        
        La arquitectura pub/sub es ideal para una variedad de aplicaciones, entre las que se incluyen:
        
        - **Sistemas de Notificaciones:** Enviar notificaciones push a múltiples usuarios de una aplicación móvil.
        - **Procesamiento de Datos en Tiempo Real:** Distribuir flujos de datos de sensores de IoT a múltiples sistemas de análisis y almacenamiento.
        - **Microservicios:** Permitir la comunicación asíncrona y desacoplada entre diferentes microservicios.
        - **Sistemas de Comercio Electrónico:** Notificar a diferentes sistemas (inventario, facturación, envíos) cuando se realiza un nuevo pedido.
        - **Actualizaciones en Aplicaciones Financieras:** Distribuir actualizaciones de precios de acciones a múltiples clientes en tiempo real.
        
        ### Tecnologías Populares
        
        Algunas de las tecnologías más conocidas que implementan el patrón publish-subscribe son:
        
        - **Apache Kafka:** Una plataforma de streaming de eventos distribuida de alto rendimiento.
        - **RabbitMQ:** Un "message broker" de código abierto muy popular y versátil.
        - **Google Cloud Pub/Sub:** Un servicio de mensajería totalmente gestionado en la nube de Google.
        - **Amazon Simple Notification Service (SNS):** Un servicio de notificaciones y mensajería en la nube de AWS.
        - **Redis Pub/Sub:** Redis, una base de datos en memoria, también ofrece funcionalidades de pub/sub.
    
    ![image.png](image%2084.png)
    
    hay un conjunto de componente de software (suscriptor) que tienen que saber que cierto evento ocurrio, entonces uno se suscribe a a eso deseo de enterarce de cierta cosas, y cuando ese evento sucede tengo un componente de software  (publicante) que cuando sucede ese evento lo informa a un Topico, entonces se dispara la notificacion hacia los suscriptores que era los que estaban suscriptos a ese topico osea deseaban enterearse
    
    ![image.png](image%2085.png)
    
    ![image.png](image%2086.png)
    
    - atributos de calidad
        
        ![image.png](image%2087.png)
        
    
    ![image.png](image%2088.png)
    
    ![image.png](image%2089.png)
    
    ![image.png](image%2090.png)
    
- Arquitectura broker
    
    ![image.png](image%2091.png)
    
    Busca resolver los problemas de compatibilidad de formatos y el ruteo
    
    Convierte el formato que recibe de los remitente a un formato que los Receptor puedan entender
    
    - mucho mas detallado
        
        ---
        
        ### Patrón Arquitectónico de Broker (Agente)
        
        ### ¿Qué es?
        
        El patrón **Broker** es un estilo arquitectónico para sistemas distribuidos diseñado para **integrar componentes que no son compatibles entre sí**, actuando como un intermediario inteligente. Su estructura se describe comúnmente como **Hub-and-Spoke** (Eje y Rayos): el **Broker** es el eje central (hub) y los sistemas que envían y reciben mensajes son los rayos (spokes).
        
        La característica fundamental que lo diferencia de otros patrones de mensajería es que el Broker no solo transporta mensajes, sino que los **entiende, transforma y enruta activamente**.
        
        ### Responsabilidades Clave del Broker
        
        A diferencia de una simple cola de mensajes, el Broker es un componente activo con lógica propia. Sus responsabilidades principales son:
        
        1. **Enrutamiento de Mensajes (Routing):** El Broker contiene la lógica para decidir a qué destino enviar un mensaje. Esta decisión puede estar basada en el contenido del mensaje, el puerto por el que llegó o reglas de negocio predefinidas.
        2. **Transformación de Mensajes (Transformation):** Esta es su función más importante. El Broker puede convertir un mensaje del formato del emisor al formato que el receptor necesita. Por ejemplo, puede transformar un mensaje JSON de una aplicación web a un formato XML o CSV que un sistema antiguo (legacy) pueda entender.
        3. **Validación:** El Broker puede validar los mensajes que recibe en sus puertos de entrada y descartar aquellos que no cumplan con el formato esperado.
        
        ### Diagrama Conceptual (Hub-and-Spoke)
        
        Imagina un componente central, el **Broker**. Varios componentes **Emisores** (Senders) se conectan únicamente al Broker para enviar mensajes. A su vez, varios componentes **Receptores** (Receivers) se conectan únicamente al Broker para recibir mensajes. No existe ninguna línea de comunicación directa entre los emisores y los receptores; todo pasa a través del Broker.
        
        ### Diferencia con Otros Patrones (Messaging y Publish-Subscribe)
        
        Es crucial entender el problema específico que resuelve el Broker:
        
        - **Messaging:** Se enfoca en el **transporte asíncrono y confiable**. El emisor y el receptor deben estar de acuerdo en el formato del mensaje.
        - **Publish-Subscribe:** Se enfoca en la **difusión de eventos** a múltiples suscriptores interesados en un "tema". El intermediario es un despachador simple.
        - **Broker:** Se enfoca en la **integración y transformación**. Su propósito es mediar entre sistemas que **no hablan el mismo idioma** y necesitan un traductor en medio.
        
        ### Ventajas
        
        - **Desacoplamiento y Compatibilidad:** Permite que sistemas heterogéneos (incluso de terceros o legacy) se comuniquen sin necesidad de modificarlos. Cada sistema puede usar su formato de mensaje nativo.
        - **Lógica Centralizada:** Toda la lógica de transformación y enrutamiento se encuentra en un solo lugar (el Broker), lo que facilita su mantenimiento, modificación y comprensión.
        - **Modificabilidad:** Se pueden cambiar las reglas de transformación o añadir nuevos receptores sin afectar a los sistemas emisores existentes.
        
        ![image.png](image%2092.png)
        
        ### Desventajas y Desafíos
        
        - **Cuello de Botella (Bottleneck):** Dado que todo el tráfico y el procesamiento de transformación pasan por el Broker, puede convertirse en un punto de congestión y afectar el rendimiento general, especialmente con grandes volúmenes de mensajes o transformaciones complejas.
        - **Punto Único de Fallo (Single Point of Failure):** Si el Broker falla, se interrumpe toda la comunicación entre los sistemas. Por esta razón, para sistemas críticos, es esencial implementar **replicación y clustering** del Broker para garantizar la alta disponibilidad.
        - **Complejidad:** El Broker en sí mismo puede ser un componente complejo de desarrollar y mantener.
        - Atributos de calidad
            
            ![image.png](image%2093.png)
            
            ![image.png](image%2094.png)
            
        
        ### Ejemplo Práctico
        
        Imagina un hospital moderno.
        
        - **Emisor 1:** Un **sistema de captura de imágenes** (Rayos X, Tomografías) que genera imágenes en formato DICOM.
        - **Emisor 2:** Un **sistema de reconocimiento de voz** que transcribe los dictados de un radiólogo a un formato de texto simple.
        - **Receptor:** El **Sistema de Información Radiológica (RIS)**, que es el sistema central y espera recibir toda la información en un formato estándar HL7.
        
        El **Broker** recibe la imagen DICOM de un emisor y el texto del otro. Su lógica de **transformación** convierte ambos formatos al formato HL7 que el RIS necesita, y su lógica de **enrutamiento** se asegura de que ambos mensajes, ahora compatibles, se envíen al RIS para ser asociados con el paciente correcto.
        
    
    ![image.png](image%2095.png)
    
    ![image.png](image%2096.png)
    
- Patrones arquitectónicos -Patrón Messaging
    
    ---
    
    ### Patrón Arquitectónico de Mensajería (Messaging)
    
    ![image.png](image%2097.png)
    
    ### ¿Qué es?
    
    El patrón de Mensajería es un estilo arquitectónico para sistemas distribuidos que **desacopla los componentes que envían información (emisores) de los que la reciben (receptores)** a través de un canal de comunicación intermedio, conocido como **Cola de Mensajes (Message Queue)**.
    
    La idea central es que, en lugar de una comunicación directa y síncrona, el emisor simplemente deposita un "mensaje" en la cola y continúa con su trabajo sin esperar una respuesta. La cola almacena este mensaje de forma segura hasta que un receptor esté listo para procesarlo.
    
    - El emisor envía un mensaje al receptor y sabe que eventualmente será entregado, aunque la red esté caída o el receptor no esté disponible
    - El patrón tiene inherentemente bajo acoplamiento, esto promueve alta modificabilidad, dado que emisores y receptores no se conectan directamente
    
    ### Componentes y Flujo de Trabajo
    
    1. **Emisor (Sender / Producer):** Es el componente de software que crea y envía el mensaje. No sabe ni necesita saber quién o cuándo se leerá su mensaje.
    2. **Cola de Mensajes (Message Queue):** Es el intermediario. Un software especializado (un *message broker*) que funciona como un "buzón" temporal. Recibe mensajes, los almacena de forma ordenada (generalmente FIFO: el primero que entra es el primero que sale) y garantiza su eventual entrega.
    3. **Receptor (Receiver / Consumer):** Es el componente que se conecta a la cola, retira un mensaje y lo procesa.
    
    El flujo es asíncrono: el emisor "dispara y olvida", confiando en que la cola gestionará la entrega.
    
    ### Diagrama Conceptual
    
    Imagina un diagrama simple: un componente **Emisor** envía un mensaje (una flecha) a una **Cola de Mensajes**. La cola guarda el mensaje. Más tarde, un componente **Receptor** se conecta a la cola y retira ese mensaje para procesarlo.
    
    ![image.png](image%2098.png)
    
    ### Propiedades Clave
    
    - **Comunicación Asíncrona:** Es la característica más fundamental. Permite que el emisor no se bloquee esperando una respuesta, lo que mejora la eficiencia y la capacidad de respuesta del sistema.
    - **Bajo Acoplamiento (Loose Coupling):** Emisores y receptores son completamente independientes. No conocen la ubicación, el estado (si están activos o no) ni la implementación del otro. Solo necesitan conocer la dirección de la cola.
    - **Calidad de Servicio (QoS) Configurable:** La cola se puede configurar para priorizar diferentes aspectos. Por ejemplo:
        - **Entrega Confiable (Reliable):** Garantiza que el mensaje no se pierda, aunque sea un proceso más lento (ej. con confirmaciones y reintentos).
        - **Entrega de Alta Velocidad (No Confiable):** Prioriza la velocidad sobre la garantía de entrega.
    
    ### Ventajas (Atributos de Calidad)
    
    - **Disponibilidad y Tolerancia a Fallos:** El sistema es muy robusto. Si un receptor se cae, los mensajes simplemente se acumulan en la cola hasta que vuelva a estar en línea. Además, la propia cola puede replicarse para evitar que sea un punto único de fallo.
    - **Escalabilidad:** Es muy fácil escalar el sistema. Si hay muchos mensajes, se pueden añadir más receptores para procesar la cola más rápido. Si hay muchos emisores, la cola puede absorber los picos de carga.
    - **Modificabilidad y Flexibilidad:** Se pueden cambiar, actualizar o reemplazar los emisores y receptores de forma independiente sin afectar al resto del sistema, siempre y cuando el formato del mensaje se respete.
    
    ### Desventajas y Consideraciones
    
    - **Dependencia del Formato del Mensaje:** El "contrato" entre el emisor y el receptor es la estructura del mensaje. Un cambio en este formato requiere la actualización de ambos componentes. El uso de formatos auto-descriptivos (como JSON o XML) ayuda a mitigar este problema.
    - **Complejidad del Intermediario:** La cola de mensajes (el *message broker*) es un componente de software complejo que necesita ser instalado, configurado, monitoreado y mantenido.
    - **Rendimiento:** Aunque el sistema en general es eficiente, la comunicación a través de un intermediario siempre introduce una pequeña latencia en comparación con una llamada directa. El intermediario mismo puede convertirse en un cuello de botella si no se gestiona adecuadamente.
    
    ![image.png](image%2099.png)
    
    ### Ejemplo Práctico
    
    El ejemplo de la **notificación de deudas** es perfecto.
    
    - **Emisor:** El sistema de gestión de impuestos detecta una deuda y crea un mensaje: `{"contribuyente_id": 123, "monto": 5000, "tipo": "intimacion"}`. Lo envía a la cola "notificaciones".
    - **Cola de Mensajes:** Almacena este y otros miles de mensajes de notificación.
    - **Receptor:** Un servicio de correo electrónico está escuchando la cola "notificaciones". Toma el mensaje, busca el email del contribuyente 123 y le envía el correo correspondiente. Este servicio no sabe nada del sistema de impuestos, solo sabe cómo procesar mensajes de notificación.
    
    ![image.png](image%20100.png)
    
    ![image.png](image%20101.png)
    
    - Atributos de calidad
        
        ![image.png](image%20102.png)
        
        ![image.png](image%20103.png)
        
- Process coordinator
    
    ---
    
    ### Patrón Arquitectónico Coordinador de Proceso (Orquestación)
    
    ![image.png](image%20104.png)
    
    ### ¿Qué es?
    
    El patrón **Coordinador de Proceso** es un estilo arquitectónico para sistemas distribuidos diseñado para gestionar **procesos de negocio complejos y de múltiples pasos**. La idea central es **encapsular toda la lógica y la secuencia del flujo de trabajo en un único componente central: el Coordinador**.
    
    Este patrón es el ejemplo clásico de un enfoque de **Orquestación**, donde un "director de orquesta" (el Coordinador) le dice a cada "músico" (los servicios) exactamente qué hacer y cuándo hacerlo.
    
    ### Componentes y Flujo de Trabajo
    
    1. **Coordinador de Proceso (Process Coordinator):**
        - **El Orquestador:** Es el cerebro del proceso. Contiene la "receta" completa del flujo de trabajo: qué pasos se deben seguir, en qué orden y con qué lógica condicional.
        - **Inicia y Finaliza:** Recibe la solicitud inicial para comenzar el proceso y es responsable de entregar el resultado final.
        - **Invoca los Servicios:** Llama a los diferentes servidores o servicios en la secuencia correcta, pasando los datos necesarios de un paso al otro.
    2. **Servidores (Servers):**
        - **Los Trabajadores:** Son componentes o servicios independientes y especializados. Cada uno sabe cómo realizar una única tarea de negocio específica (ej. "verificar el riesgo crediticio", "validar una dirección").
        - **Desacoplados y Reutilizables:** Lo más importante es que los servidores son "ignorantes" del proceso de negocio general. No saben quién los llamó ni qué pasará después. Simplemente ejecutan su tarea y devuelven un resultado.
    
    ### Diagrama Conceptual
    
    El esquema de tus fuentes es muy claro. Muestra un flujo centralizado y controlado:
    
    1. Una solicitud llega al **Coordinador**.
    2. El Coordinador llama al **Servidor 1** para el **Paso 1**.
    3. Una vez completado, llama al **Servidor 2** para el **Paso 2**, y así sucesivamente.
    4. Finalmente, el Coordinador consolida los resultados y finaliza el proceso.
    
    ![image.png](image%20105.png)
    
    ### Diferencia Clave: Orquestación vs. Coreografía
    
    - **Coordinador de Proceso (Orquestación):** Un controlador central dicta el flujo. Es como un director de orquesta. Es más fácil de entender y monitorear, pero el director es un punto de fallo.
    - **Arquitectura Dirigida por Eventos (Coreografía):** No hay un controlador central. Cada servicio reacciona a eventos y emite nuevos eventos, sin que nadie les diga qué hacer. Es como un grupo de bailarines que saben cómo reaccionar a la música y a los movimientos de los demás. Es más resiliente pero mucho más difícil de seguir y depurar.
    
    - Atributos de calidad
        
        ![image.png](image%20106.png)
        
    
    ### Ventajas
    
    - **Lógica Centralizada:** El flujo de negocio completo está definido en un solo lugar, lo que lo hace mucho más fácil de entender, monitorear, depurar y modificar.
    - **Bajo Acoplamiento de los Servicios:** Los servidores son simples, reutilizables y no tienen dependencias entre sí, ya que solo conocen al coordinador.
    - **Flexibilidad en la Comunicación:** El coordinador puede comunicarse con los servidores de forma **síncrona** (esperando una respuesta inmediata) o **asíncrona** (enviando una solicitud y esperando una notificación de vuelta), según lo que necesite el proceso.
    
    ![image.png](image%20107.png)
    
    ### Desventajas y Desafíos
    
    - **Punto Único de Fallo y Cuello de Botella:** El coordinador es el componente más crítico. Si falla, todo el proceso se detiene. También puede convertirse en un cuello de botella si debe gestionar demasiados procesos concurrentes. Para mitigar esto, **es esencial replicar el coordinador**.
    - **Manejo de Fallos Complejo:** Este es su mayor desafío. Si un paso falla a mitad de un proceso largo (ej. el paso 3 de 4), ¿qué sucede con los pasos 1 y 2 que ya se completaron y modificaron datos? El coordinador debe implementar una lógica de **transacciones de compensación** para "deshacer" los pasos anteriores y evitar dejar el sistema en un estado inconsistente, lo cual es muy difícil de diseñar correctamente.
    - **Acoplamiento con los Servicios:** Aunque los servidores están desacoplados entre sí, el coordinador está fuertemente acoplado a las interfaces de los servicios que necesita llamar.
    
    ![image.png](image%20108.png)
    
    ### Ejemplo Práctico (Solicitud de Préstamo)
    
    El ejemplo de la solicitud de un préstamo bancario es ideal:
    
    - **Coordinador:** El "Servicio de Gestión de Préstamos".
    - **Paso 1:** El Coordinador recibe la solicitud y llama al **Servidor de Solicitudes** para validarla.
    - **Paso 2:** Si es válida, llama al **Servidor de Evaluación Financiera** para analizar los ingresos del cliente.
    - **Paso 3:** Con esa información, llama al **Servidor de Riesgo Crediticio** para consultar el historial en el buró de crédito.
    - **Paso 4:** Si todo es positivo, llama al **Servidor de Liquidaciones** para aprobar y desembolsar el préstamo.
    
    Cada servidor solo hace su parte, pero el Coordinador se asegura de que todo el proceso se ejecute en el orden y con la lógica correcta.
    
    ![image.png](image%20109.png)
    
    ![image.png](image%20110.png)
    
- estos son variantes del eda?
    
    Es una excelente pregunta y la relación es muy estrecha. Más que una "variante", el patrón de **Mensajería** es la **tecnología fundamental sobre la que se construye la Arquitectura Dirigida por Eventos (EDA)**.
    
    Piensa en la relación de esta manera:
    
    - El **Patrón de Mensajería** es el mecanismo, las "tuberías". Se enfoca en el **CÓMO**: cómo desacoplar dos componentes usando una cola para enviar mensajes de forma asíncrona.
    - La **Arquitectura Dirigida por Eventos (EDA)** es el paradigma, el "plano completo del edificio". Se enfoca en el **QUÉ**: qué significa ese mensaje. En EDA, el mensaje es un "evento", algo que ya ocurrió (ej. "Pedido Creado"). EDA utiliza el mecanismo de mensajería para orquestar el comportamiento de todo un sistema basado en la reacción a esos eventos.
    
    Aquí tienes una tabla para ver la diferencia claramente:
    
    | Característica | Patrón de Mensajería (Messaging) | Arquitectura Dirigida por Eventos (EDA) |
    | --- | --- | --- |
    | **Alcance** | Es un **patrón de comunicación** específico. | Es un **estilo arquitectónico** completo que define el comportamiento de todo el sistema. |
    | **Contenido del Mensaje** | Es un dato o un comando genérico que se envía. | Es un **"Evento"**: una notificación de que algo significativo ocurrió en el pasado. |
    | **Intención** | Desacoplar un emisor de un receptor. | Permitir que múltiples componentes, totalmente independientes, reaccionen a un mismo suceso. |
    | **Ejemplo Simple** | Un servicio A envía un mensaje a una cola para que el servicio B lo procese cuando pueda. | Un evento "UsuarioRegistrado" se publica. Lo escuchan el servicio de "Email de Bienvenida", el de "Análisis de Datos" y el de "Creación de Perfil", y cada uno actúa en paralelo. |
    
    **En resumen: no puedes tener EDA sin un sistema de Mensajería.** La mensajería es la herramienta fundamental que permite que el paradigma de EDA funcione. EDA es una aplicación más sofisticada y de mayor nivel del patrón de mensajería.
    

---

---

[ARQUITECTURA MICROSIERVICIO  (estilo)](https://app.notion.com/p/ARQUITECTURA-MICROSIERVICIO-estilo-22c93f1051dc80808101c76fa728a1d4?pvs=21)

- ejemplo FTGO monolitca capas,  hexagonal y distribuida con micro servicio
    
    ![image.png](image%20111.png)
    
    ![image.png](image%20112.png)
    
    ![image.png](image%20113.png)




---
# References
## Father
## child