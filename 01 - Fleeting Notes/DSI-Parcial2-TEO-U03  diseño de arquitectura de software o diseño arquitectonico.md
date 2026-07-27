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
# Unidad 3 → diseño de arquitectura de software o diseño arquitectonico (clase 3)

[DSI 3K3 - Diseño Arquitectónico 2024.pdf](DSI_3K3_-_Diseo_Arquitectnico_2024.pdf)

- que es la arquitectura
    
    Es el conjunto de decisiones significativas que tomamos respecto de como resolver de los rnf  escenciales para la arquitcutra, teniendo en cuenta las retricciones del negocio
    
    ![image.png](image%2046.png)
    
- arquitectura de software
    
    Es la estructura y relación de componentes del sistema, orientada a su tecnología de aplicación. Define
    lineamientos que todos los equipos deben seguir, especificando:
    • Estructura: cómo se organizan los componentes.
    • Comunicación: cómo interactúan los componentes.
    • Requerimientos no funcionales: direcciona atributos como seguridad, desempeño, disponibilidad, etc.
    • Abstracción: provee una visión simplificada del sistema.
    
    ---
    
    - mas detallado
        
        Claro, aquí tienes un resumen de los conceptos clave del texto sobre arquitectura de software:
        
        ### Resumen del Concepto de Arquitectura de Software
        
        La **arquitectura de software** es el diseño estratégico y la estructura fundamental de un sistema informático. Funciona como un esqueleto o plano que define cómo se organizan, comunican e interactúan los distintos componentes de software para satisfacer tanto los requisitos funcionales (lo que el sistema hace) como, y muy especialmente, los **requisitos no funcionales** (cómo lo hace: rendimiento, seguridad, escalabilidad, etc.).
        
        Es la base sobre la que se construye todo el software, y por ello, las decisiones arquitectónicas son las más importantes y difíciles de cambiar una vez implementadas.
        
        Según el texto, las características fundamentales de la arquitectura son:
        
        1. **Define la Estructura:** Se encarga de dividir la aplicación en un conjunto de componentes (módulos, objetos, etc.) y asignarles responsabilidades claras. Un objetivo clave es **minimizar las dependencias** entre ellos (lograr un bajo acoplamiento) para que el sistema sea más fácil de mantener, probar y modificar sin que los cambios se propaguen inesperadamente.
        2. **Especifica la Comunicación de los Componentes:** Establece los protocolos y mecanismos mediante los cuales los componentes se comunicarán entre sí para intercambiar datos e información de control. A menudo, esto se logra utilizando **patrones arquitectónicos** (ej. cliente-servidor, publish-subscribe), que son soluciones probadas y reutilizables para problemas comunes de comunicación.
        3. **Aborda los Requisitos No Funcionales:** Mientras que la funcionalidad se describe en los casos de uso, la arquitectura crea la plataforma que garantiza que dicha funcionalidad se entregue cumpliendo con los requisitos de calidad, como el rendimiento, la distribución física, la seguridad o la capacidad de respuesta.
        4. **Es una Abstracción:** La arquitectura simplifica la complejidad de un sistema al ocultar los detalles internos de los componentes y centrarse en sus propiedades visibles y sus interacciones. Esto permite que diferentes personas (desarrolladores, jefes de proyecto, clientes) entiendan el sistema desde diferentes niveles de detalle, facilitando la comunicación y el trabajo en equipo.

![image.png](image%2047.png)

---

![image.png](image%2048.png)

- ROL del ARQUITECTO
    
    Arquitecto:
    
    - ▪ Revisa y negocia los requerimientos
        
        ![image.png](image%2049.png)
        
    - ▪ Documentar la Arquitectura
        
        ![image.png](image%2050.png)
        
    - ▪ Comunica la arquitectura, asegurándose que los involucrados comprendan.
        
        ![image.png](image%2051.png)
        
    
    ▪ Direcciona requerimientos no funcionales a la arquitectura
    ▪ Configura la arquitectura de hardware
    ▪ Se asegura que la arquitectura es respetada
    ▪ Trabaja con el Administrador del Proyecto, ayudando en la planificación, la estimación la distribución de tareas y la calendarización del proyecto
    

---

## PROCESO

- contexto de la arquitectura (como que yo inserto en un proceso de desarrollo de software esto del diseño arquitectonico )
    
    ![image.png](image%2052.png)
    
    de la izquierda toma como decisciones del disño de arquitectura la arquitctura del hardware, porque los recursos no son ilimitados y son cosas que afectan a nuestra arquitectura
    
    puede exigir modificaciones por ejemplo una empresa sin servidores no puede exigir software web
    
    ---
    
    una vez que el proceso de diseño arquitectonico genera esta versiond e la arquitectura de software entonces ya entramos a las estapas finales del proceso que serian el diseño detallado, codificacion,etc
    
    ![image.png](image%2053.png)
    

### PROCESO DE DISEÑO DE LA ARQUITECTURA DE SOFTWARE

- que es el diseño arquitectonico?
    
    Es la asignación de modelos de requerimientos esenciales a una tecnología específica.
    
    Es el plan del Diseño
    
    ---
    
    el diseño arquitectonico se refiere al proceso que toma el modelo de analisis + los rnf escencilaes para la arquitectura 
    
    def 2:
    
    **El proceso de diseño inicial para identificar estos subsistemas y establecer un marco de trabajo para control y comunicación de los subsistemas se llama Diseño Arquitectónico**4
    
    ![image.png](image%2054.png)
    
    ![image.png](image%2055.png)
    
    ![image.png](image%2056.png)
    
- descripcion del proceso de diseño arquitectonico
    
    <aside>
    💡
    
    este es el proceso para diseñar la arquitectura del software
    
    - NO ES LO MISMO QUE EL WORKFLOW DE DISEÑO
        - este era el proceso general  que abarca todas las cosas que hay que diseñar inclusive la arquitectura
        - la vistas arquitectonicas son un artefacto del worklfo de diseño
    - esto estaria dentro del workflow de diseño
    </aside>
    
    Para guiar al arquitecto hacia la definición de la arquitectura de la aplicación es útil seguir un proceso definido.
    ● La siguiente figura muestra un proceso de arquitectura iterativo en tres pasos que puede ser usado para guiar las actividades durante el diseño
    
    ![image.png](image%2057.png)
    
    este proceso tienen 3 actividades
    
    - 1actividad: determinar los requerimientos arcitectonicos
        - recordadon que estamos dentro del workflo de diseño ya tenmos como entrada los req funcionales y no funcionales
        - solo los no funcionales que no habia tenido en cuenta antes, van a ser de entrada para esta actividad: que es donde los analizamos y determinamos si son o no significativos para la arquitectura
        
        ---
        
        Antes de que una solución arquitectónica pueda ser diseñada, es necesario tener una idea bastante buena de los requerimientos arquitectónicos para la aplicación. Los requerimientos arquitectónicos a veces también suelen llamarse requerimientos significativos para la arquitectura, los cuales son esencialmente la calidad y los requerimientos no funcionales para la aplicación.
        
        - 1.1 Identificar requerimientos significativos.
            
            Las principales fuentes de los requerimientos arquitectónicos son el documento de
            requerimientos funcionales y otros documentos que capturan varias necesidades de las partes interesadas. La salida de este paso es un documento que determina los requerimientos arquitectónicos para la aplicación.
            
            ![image.png](image%2058.png)
            
        - 1.2 Priorización de requerimientos arquitectónicos
            
            ![image.png](image%2059.png)
            
        - ELECCIÓN DEL MODELO ARQUITECTÓNICO Y LOS REQUERIMIENTOS NO FUNCIONALE (como afecta el tema de los rnf a la arquitectura)
            
            Claro, aquí tienes un resumen de los puntos clave del texto sobre el modelado de la arquitectura.
            
            - Resumen sobre el Modelado de la Arquitectura
                
                El **modelado de la arquitectura** es el proceso donde se traducen los requerimientos de un sistema a una solución tecnológica específica y concreta. No se trata de encontrar una solución "perfecta", sino la **óptima** para un conjunto de circunstancias, considerando por primera vez aspectos prácticos como volúmenes de datos, distribución geográfica de los usuarios, la ubicación del procesamiento y la tecnología a utilizar (hardware, sistema operativo, lenguajes, etc.).
                
                Una de las ideas más importantes es que **la arquitectura debe ser documentada**, ya que estas decisiones fundamentales son difíciles de conocer a futuro y complican enormemente la evolución o mantenimiento del sistema si no están registradas.
                
            
            ### Elección del Modelo y Requisitos No Funcionales
            
            El punto central del texto es que la elección de un patrón o estilo arquitectónico está directamente impulsada por los **requisitos no funcionales** (también llamados atributos de calidad) que sean más críticos para el producto. El arquitecto debe priorizar y encontrar un equilibrio, ya que estos requisitos a menudo entran en conflicto.
            
            Los principales requisitos y su impacto en la arquitectura son:
            
            1. **Desempeño (Performance):** Si es crítico (tiempos de respuesta rápidos, alto volumen de transacciones), sugiere una arquitectura con **componentes de granularidad gruesa**. Esto significa tener menos subsistemas, pero más grandes y complejos internamente, para reducir la comunicación entre ellos, que es una de las principales causas de lentitud.
            2. **Seguridad:** Si es un requisito prioritario, se recomienda una **arquitectura en capas**, donde los datos y recursos más críticos se protegen en las capas más internas, con múltiples niveles de validación (autenticación, autorización, encriptación) para poder acceder a ellos.
            3. Protección: Si es un requerimiento crítico, sugiere que la arquitectura
            debe diseñarse para incluir operaciones relacionadas con la protección se
            localicen en un solo subsistema o en un número reducido de subsistemas.
            Esto reduce costos y problemas de validación
            4. **Disponibilidad:** Si el sistema debe estar siempre funcionando, la arquitectura debe incluir **componentes redundantes** (replicados). De esta forma, si un componente falla, una de sus réplicas toma su lugar sin detener el sistema.
            5. **Mantenibilidad:** Si lo más importante es la facilidad para corregir errores y realizar cambios, se debe optar por una arquitectura con **componentes de granularidad fina**. Es decir, componentes pequeños, simples, que hacen una sola cosa (alta cohesión) y que están débilmente conectados con otros (bajo acoplamiento).
            
            ### Conflictos Arquitectónicos
            
            ![image.png](image%2060.png)
            
            El texto concluye destacando que es imposible optimizar todos los atributos a la vez. El trabajo del arquitecto es gestionar estos conflictos:
            
            - **Performance vs. Mantenibilidad:** Usar componentes de granularidad gruesa mejora el rendimiento, pero dificulta enormemente el mantenimiento.
            - **Disponibilidad vs. Performance/Seguridad:** La redundancia mejora la disponibilidad, pero tener copias del sistema consume más recursos (afectando el rendimiento) y crea más puntos que deben ser asegurados.
            - **Seguridad vs. Performance:** Añadir más capas de validación y seguridad inevitablemente hace que el sistema sea más lento.
        
    - 2da actividad diseño arquitectonico
        
        ![image.png](image%2061.png)
        
        Implica la definición de la estructura y las responsabilidades de los componentes que constituirán la arquitectura. 
        
        Elegimos qué patrones arquitectónicos (framework) usaremos para armar el esqueleto del producto, son patrones de alto nivel (Nivel de capas o componentes). Los patrones esta actividad tiene adentro  se aplican (significa que hay que construir los componentes que implementa estos patrones). Luego, distribuimos los componentes, los creamos y aplicamos las soluciones arquitectónicas elegidas. De acá sale la documentación de la arquitectura y las vistas de arquitectura.
        
        La etapa del diseño en sí tiene dos pasos, que son iterativos. El primero involucra elegir una estrategia general para la arquitectura basado en patrones arquitectónicos.
        
        - actividad: eligir framework de arquitectura
            
            ![image.png](image%2062.png)
            
            La elección del framework de arquitectura se conforma con un conjunto de Patrones Arquitectonicos, esto es porque:
            
            - La mayoría de las aplicaciones responden a un número pequeño de arquitecturas probadas y bien comprendidas
            - Utilizar soluciones conocidas, minimiza los riesgos.
            - No hay una fórmula mágica para diseñar un framework de arquitectura. Un pre-requisito es conocer los patrones arquitectónicos para abordar ciertos atributos de calidad.
            - Un pre-requisito: conocer los estilos arquitectónicos principales para abordar ciertos atributos de calidad.
                
                ![image.png](image%2063.png)
                
        
        ---
        
        El segundo incluye especificar los componentes individuales que componen la aplicación, mostrando cómo encajan en el marco general y asignarles responsabilidades. 
        
        - actividad: distribuir componentes
            - Ya se ha seleccionado el framework arquitectónico, basado en uno o más patrones arquitectónicos.
            - ▪ Seguidamente se deben definir los componentes principales que comprenderán el diseño.
            - ▪ El framework define comunicación general para los componentes, además, debe identificarse lo siguiente:
                - ▪ Componentes principales de la aplicación y como se
                insertan en el framework.
                - ▪ Servicios o interfaces que cada componente soporta.
                - ▪ Responsabilidades del Componente, definiendo que será invocado para hacer cuando reciba un pedido.
                - ▪ Dependencias entre componentes.
                - ▪ Particiones en la arquitectura que son candidatas para distribución entre servidores de la red
            - ▪ Minimizar las dependencias entre componentes.
                - ▪ Recordar: si lo cambias debes re-testearlo
            - ▪ Diseñar componentes que encapsulen un conjunto de responsabilidades altamente cohesivas.
                - ▪ Esto limita los tipos de cambios y reduce esfuerzo de mantenimiento y testing.
            - Aislar dependencias entre el middleware y cualquier COT de infraestructura tecnológica.
                - ▪ Es más difícil de construir, pero introduce penalidades de performance.
            - ▪ Utilizar la descomposición para estructurar componentes jerárquicamente.
            - ▪ Minimizar las llamadas entre componentes
            
            ![image.png](image%2064.png)
            
            Una vez que se ha seleccionado el framework de arquitectura, basado en uno o más patrones arquitectónicos, la siguiente tarea es definir los componentes principales que comprenderá el diseño.
            
            El framework define la comunicación general para los componentes, debe identificarse lo siguiente:
            
            ![image.png](image%2065.png)
            
            - Identificar los principales componentes de la aplicación y cómo se insertan en el framework.
            - Identificar la interfaz o los servicios que soporta cada componente.
            - Identificar las responsabilidades del componente, definiendo qué será invocado para hacer cuando reciba una solicitud.
            - Identificación de dependencias entre componentes.
            - Identificar particiones en la arquitectura que son candidatas para la distribución a través de servidores en una red.
            
            ![image.png](image%2066.png)
            
        
        ---
        
        La salida es un conjunto de vistas arquitectónicas que capturan el diseño de la arquitectura y un documento de diseño que explica el diseño, las razones clave de algunas de las principales decisiones de diseño, e identifica los riesgos involucrados.
        
        El resultadoo nos da como salida los artefactos principales que son las vistas de arquitectura y documento de arquitectura
        
        ---
        
        CLASE 5 y 6
        
        [[DSI-Parcial2-TEO-U03 Documentacion]]
        
        [[DSI-Parcial2-TEO-U03-Vistas Arquitectonicas]]
        
    - 3era act validacion
        
        ![image.png](image%2067.png)
        
        ▪ Ayuda a incrementar la confianza del equipo de diseño en que la arquitectura cumpla con su propósito.
        ▪ Debe realizarse con las restricciones de tiempo y presupuesto del proyecto.
        ▪ El truco es ser tan riguroso y eficiente como sea posible. 
        ▪ Es un desafío validar la arquitectura ya que finalmente es un diseño y no puede ejecutarse ni probarse para ver su cumple los requerimientos.
        ▪ su propósito es identificar posibles defectos y debilidades de forma temprana.
        ▪ Existen dos técnicas principales que tienen un uso probado. Ambas ayudan a identificar fallas y debilidades, áreas de riesgo potencial para las posteriores actividades de construcción.
        
        - ▪ 1) Probar Manualmente la Arquitectura utilizando escenarios.
            
            Los escenarios están relacionados con aspectos arquitectónicos tales como atributos de calidad, y ellos ayudan a destacar consecuencias de las decisiones arquitectónicas que están encapsuladas en el diseño. 
            
            - Los escenarios son artefactos simples.
            - Implican  la definición de estímulos que tendrán impacto en la arquitectura.
                - Se define un **estímulo** (un evento específico, como el fallo de un servidor o un ataque) relacionado con un atributo de calidad (disponibilidad, seguridad, etc.)
            - Se trabaja la respuesta de la arquitectura a esos estímulos.
                - Si la respuesta es indeseable o revela una debilidad, se ha encontrado un defecto en el diseño que debe ser corregido.
            - Destacan las implicancias de la arquitectura en las decisiones de diseño.
            
            ▪Los escenarios son una técnica útil para validar la arquitectura, sin embargo, algunos escenarios no son tan simples.
            ▪ Ejemplo: “Hay que procesar 500 órdenes en 5 minutos”
            ▪ La pregunta es simple: ¿Se podrá?
            ▪ La única forma de contestar esta pregunta con algún grado de confianza es construir un prototipo
             ![[Pasted image 20260727185746.png]]
	            ![[Pasted image 20260727185803.png]]
         
        - ▪ 2) Construir  prototipos que crea un arquetipo de la aplicación deseada.
            
            ▪Los prototipos son versiones mínimas, restringidas de la aplicación, creadas específicamente para probar algún aspecto riesgoso o pobremente comprendido del diseño.
            
            ▪Los prototipos son utilizados comúnmente para dos propósitos.
            
            ▪ Prueba de Conceptos:¿Puede la arquitectura como fue diseñada ser construida de manera tal que satisfaga los requerimientos?
            ▪ Prueba de Tecnología: ¿La tecnología elegida (middleware, aplicaciones integradas, librerías, etc.) para implementar la arquitectura se comporta como es esperado?
            
            ▪En ambos casos proveen una evidencia que de otra forma no se puede validar.
            
            1. **Construcción de Prototipos:**
                - Se utiliza cuando los escenarios no son suficientes para validar aspectos de **alto riesgo** o mal entendidos del diseño.
                - Un prototipo es una **versión mínima, reducida y desechable** de una parte de la aplicación. Se crean con dos fines principales:
                    - **Prueba de Concepto:** Confirmar que la arquitectura se puede construir tal como se diseñó y que es factible.
                    - **Prueba de Tecnología:** Verificar que la tecnología seleccionada (una librería, una API, una base de datos) se comporta como se espera bajo las condiciones requeridas (por ejemplo, si puede manejar un cierto volumen de datos).
                - **Advertencia clave:** Los prototipos son una herramienta para reducir el riesgo, no son parte del producto final. Deben desarrollarse rápidamente y **ser descartados** una vez que han cumplido su propósito.
        
        - las salidas de la 2da actividad entran a la 3era actividad
        - analizar o controlar para determinar adecuacion, (la propuesta arquitectonica que me entro de la 2da actividad, que tanto comple con los requerimientos que se tomaron de base, si no cumple vuelve para atras
        
    
    Estas fases son iterativas, con el objetivo de asegurar que la arquitectura diseñada sea robusta y cumpla con las expectativas del sistema final
    
- Modelo arquitectónico → Salida del proceso de diseño arquitectonico
    
    La salida del proceso de diseño arquitectónico consiste en un modelo arquitectónico que describe la forma en que se organiza el sistema como un conjunto de componentes en comunicación.
    
    ▪ El modelo arquitectónico mapea los requerimientos funcionales delanálisis a una arquitectura tecnológica.
    ▪ Debe tratar con los requerimientos no funcionales.
    ▪ No existe la solución “perfecta”, el modelado  arquitectónico debe
    escoger la solución  óptima para el conjunto de circunstancias existentes
    
    - Debe considerar información sobre:
        
        ▪ Volúmenes de Datos.
        ▪ Funcionalidad más demandada en el negocio.
        ▪ Distribución geográfica.
        ▪ Distribución del Procesamiento de datos.
        ▪ Dónde se guardarán los datos.
        ▪ Cuáles procesos se ejecutarán en qué procesadores y que tanta comunicación se requerirá entre ellos
        
    
    ![image.png](image%2068.png)
    
    - concepto de subsistema
        
        ![image.png](image%2069.png)
        
    
    ![image.png](image%2070.png)
    

## Producto

- TIPOS DE SISTEMAS
    
    ![image.png](image%2071.png)
    
- SISTEMAS DISTRIBUIDOS
    
    ▪ Virtualmente todos los sistemas grandes basados en computadoras son ahora sistemas distribuidos.
    
    ▪ El procesamiento de información está distribuido en varios procesadores.
    
    Un sistema distribuido es una colección de computadoras independientes que cooperan para brindar al usuario la apariencia de un sistema único y coherente. A diferencia de los sistemas centralizados, el procesamiento de información se distribuye entre varias máquinas.
    
    - Caracteristicas
        
        ![image.png](image%2072.png)
        
        1. Compartición de recursos: Permite usar hardware y software entre varias computadoras. Esto permite aprovechar recursos que no disponemos físicamente y sí están en otro lugar, lo cual aporta a la capacidad de procesamiento.
        2. Apertura: Basados en estándares para interoperabilidad.
        3. Concurrencia: Procesos simultáneos en distintas máquinas.
        4. Tolerancia a fallas: Funciona degradado ante errores; solo falla completamente si la red lo hace.
        5. Escalabilidad: Capacidad de crecer en tamaño, distribución y manejabilidad.
        
    - Desventajas
        1. Complejidad: Difíciles de diseñar, probar y mantener.
        2. Seguridad: Más puntos vulnerables.
        3. Manejabilidad: Difícil administrar sistemas heterogéneos.
        4. Impredecibilidad: Rendimiento variable por red y carga.
        
    - ATAQUES DE LOS QUE DEBEN DEFENDERSE LOS SISTEMAS DISTRIBUIDOS
        
        ![image.png](image%2073.png)
        
        Amenazas
        
        1. Intercepción: Espionaje de datos.
        2. Interrupción: Saturación de servicios.
        3. Modificación: Alteración de datos o servicios.
        4. Fabricación: Creación de información falsa para conseguir ciertos privilegios.
        
    - FALACIAS DE LOS SISTEMAS DISTRIBUIDOS
        1. La red está siempre disponible
            
            ![image.png](image%2074.png)
            
        2. Latencia cero: Siempre hay retrasos en la comunicación.
            
            ![image.png](image%2075.png)
            
        3. Ancho de banda infinito
        4. La red es segura: Las redes son vulnerables a ataques y requieren medidas de protección.
        5. La topología no cambia: Las redes pueden ser dinámicas (por ejemplo, en la nube o móviles).
        6. Un único administrador: Muchos sistemas no tienen un control centralizado.
        7. Costo de transporte cero: Transferir datos tiene costos y afecta el rendimiento.
        8. La red es homogénea: Los nodos suelen ser heterogéneos en capacidades y recursos.
- Arquitectura monolitica → esto es un estilo o un tipo de sistema eso no entiendo, yo lo pongo aca porque me parece lo contario a un sistema distribuido
    
    Aplicaciones autosuficientes que contengan toda la funcionalidad necesaria para
    realizar la tarea para la cual fueron diseñadas, sin contar con dependencias
    externas que la complementen.
    La capacidad más notable que tiene es la INDEPENDENCIA
    
    ![image.png](image%2076.png)
    
    - En un servicio monolítico, la mayor parte del código del lado del servidor está en un programa que se comunica con una o más bases de datos
    - Dentro de un servidor monolítico, el código aún podría dividirse en componentes y separarse en módulos individuales.
    - Las únicas API definidas suelen ser:
        - A) Entre la interfaz de usuario y el servidor (en cualquier protocolo REST/HTTP )
        - B) Entre el servidor y las bases de datos (en cualquier lenguaje de consulta)
        - C) Entre el servidor y sus dependencias externas
        
        ![image.png](image%2077.png)
        
        ![image.png](image%2078.png)
        
        - pro y contras
            
            ![image.png](image%2079.png)
            
## Patrones y Estilos Arquitectonicos

sobre esto hace foco la 3era clase, recordar que es una actividad del proceso de diseño arquitectonico

---

![image.png](image%2080.png)

- patrones
    
    ![image.png](image%2081.png)
    
    Los patrones arquitectonicos son patrones de alto nivel que afectan a nivel de capas/nivel de susbistemas/ de grandes bloques y como se comunican esos bloques o como se organizan
    
    Los patrones de diseño; apuntan a la programacion pero son independientes del lenguaje de programacion
    
    y los patrones de diseño que son especificos para un lenguaje, esos se llaman idiomas
    
- Framework arquitectónico
    
    Es el conjunto de patrones arquitectónicos utilizados para estructurar una aplicación. No se
    opone a la idea de tener un estilo arquitectónico predominante, pero agrupa varios patrones que una aplicación puede emplear, como Layered, N-Tier o Publish & Subscribe.
    
- patrones Arquitectonicos vs Estilos arquitectonicos
    - La distinción no es tajante y existen ejemplos donde es difícil distinguirlos. A veces se los ve como sinónimos.
    - Los patrones están en una escala menor que los estilos. Múltiples patrones pueden aparecer en un mismo diseño.
    - En contraste, un sistema usualmente tiene un único estilo arquitectónico dominante
    
    ![image.png](image%2082.png)
    
- patron arquitectonico
    
    ![image.png](image%2083.png)
    
- estilo arquitectonico
    
    ![image.png](image%2084.png)
    
- platonicos vs Embebidos (teoria vs la realidad)
    - Platónicos: idealizados, se los ve en los libros y rara vez de igual forma en el código.
    - Embebidos: se los ve en sistemas reales y a menudo violan las restricciones estrictas de los platónicos. La violación generalmente implica una gran compensación
    
    nostros desde la teoria estudiamos los ideales, nos da como deberia ser, pero bueno en la realidad hay implementaciones que no pueden ser tan ideales
    
    entonces tenemos patrones embembidos donde se le hacen adecuaciones para implementarlos para cumplir los req funcionales y cumplir las retricciones que tengo en el contexto
    

clase 3 y 4

[Patrones Arquitectonicos](https://app.notion.com/p/Patrones-Arquitectonicos-22a93f1051dc808ea716f16621bddbf8?pvs=21)

---




---
# References
## Father
## child