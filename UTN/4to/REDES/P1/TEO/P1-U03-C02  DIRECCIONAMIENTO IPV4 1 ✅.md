# P01-U03-C02- DIRECCIONAMIENTO IPV4 1

https://www.youtube.com/watch?v=0N9mUbvsSM4&list=PLYZrqm_pzRumO_6c3u7yeHbNF9j6bkbM8&index=6

TODO ESTO NI NOS DIERON, esto lo saque lite del resumen de chamia dsp ver si del resumen Unido final y RESUMEN FINAL RIN podemos sacar algo

La capa de interred, equivalente a la capa de red en el modelo OSI, facilita la comunicación de datos entre máquinas en una red, permitiendo la interconexión incluso entre segmentos de red diferentes. A diferencia de la capa de enlace, que se limita a dispositivos en el mismo segmento, la capa de interred posibilita la comunicación a nivel global, como cuando una máquina se conecta con un servidor en cualquier parte del mundo

Esta capa opera sobre una red de conmutación de paquetes, donde la información se divide en paquetes que son enrutados por routers. La conmutación de paquetes implica que cada paquete se dirige de manera independiente, sin una ruta preestablecida, pudiendo llegar desordenados al destino. La capa de interred es fundamental para Internet, ya que sin ella la conectividad global sería imposible

La capa de interred no establece conexiones extremo a extremo y permite la entrada de paquetes a la red, transportándolos de manera independiente hasta su destino. Sus funciones principales incluyen el direccionamiento, donde se asignan direcciones IP para lograr conectividad, el encaminamiento de paquetes realizado por routers, el control de congestión para evitar saturación y la gestión de calidad de servicio para mantener conexiones estables, como en la transmisión de contenido multimedia.

Esta capa se ejecuta en dispositivos como routers, hosts (PCs) y servidores, pero no en switches, ya que estos solo comprenden las capas 1 y 2. Aunque ocasionalmente se le asigna una dirección IP al switch para administración remota, este no cumple la función de router, y su dirección nunca actuará como Gateway.

> Encaminamiento:
Se refiere al proceso en el que un router, al recibir paquetes, desencapsula la información para obtener la dirección IP de destino. Luego, consulta una tabla de encaminamiento para determinar la interfaz por la cual enviar el paquete. El control de congestión es esencial para evitar la pérdida de paquetes y el colapso de la red, ya que la retransmisión constante puede provocar problemas mayores.
> 

> No se establece conexiones extremo a extremo?
Esto es, cuando un dispositivo tiene datos para transmitir simplemente los lanza a la red, es decir que, no establece una conexión extremo a extremo.
Cada vez que una PC quiere transmitir datos simplemente se inyectan datos o
paquetes a la red, van ingresando a la red de manera independiente.
> 

[1 - 02 - RED - Unidad 3 - Direcciones IPv4 - Parte 1.pdf](1_-_02_-_RED_-_Unidad_3_-_Direcciones_IPv4_-_Parte_1.pdf)

ip- Clase 2  salto aca

### DIRECCIONAMIENTO IPV4 ✅

Internet Protocol es un protocolo, perteneciente a la capa de Internet del TCP/IP y a la capa de Red del modelo OSI, que asigna direcciones a dispositivos para permitir la comunicación. La IPv4 es una de las dos versiones actuales del protocolo IP, siendo esencial para las redes de difusión, ya que las direcciones IP facilitan que los mensajes lleguen de una PC a otra específica.

> “fundamental distinguir entre la identidad física y la ubicación lógica de un 
dispositivo. “
Mientras que la dirección MAC (Capa 2) identifica al hardware de forma única e inalterable, la **dirección IP** actúa como un identificador lógico en la Capa 3, permitiendo la organización jerárquica necesaria para la comunicación global. Sin este sistema lógico, el enrutamiento de paquetes en redes complejas sería  técnicamente inviable.
> 

### IPv4 ✅

Se denomina IPv4 por pertenecer a la capa de Interred y es esencial para la conectividad global de Internet.

- Funcionamiento / eficiencia y robustez
    
    El protocolo IP opera recibiendo segmentos de la capa de transporte, los cuales encapsula en paquetes añadiéndoles sus respectivas cabeceras. Una vez formados, estos paquetes —que en ocasiones deben dividirse en trozos más pequeños— se encaminan de manera independiente hacia su destino. Aunque este proceso de encaminamiento individualizado puede resultar lento, le otorga a la red una gran robustez, ya que permite encontrar rutas alternativas en caso de que ocurran fallos. Para tomar estas decisiones de enrutamiento, el protocolo evalúa la dirección IP de destino, apoyándose en la máscara de red y en las tablas de encaminamiento.
    
- caracteristicas y razones para la no entrega
    
    Una de las características fundamentales del protocolo IP es que no está orientado a la conexión y opera bajo el principio de "mejor esfuerzo", es decir, no garantiza que los paquetes lleguen a su destino. Las razones más comunes para esta falta de entrega incluyen la pérdida de paquetes por la caída de enlaces físicos o problemas de congestión en la red, lo cual ocurre cuando la memoria de los routers se llena y se ven obligados a descartar el tráfico entrante. Para compensar esta falta de fiabilidad inherente a IP, se utiliza el protocolo TCP, el cual se encarga de asegurar una entrega fiable de los datos y de gestionar la retransmisión de cualquier segmento que se haya perdido en el camino.
    
- roles en dispositivos de red
    - En routers, las tablas de encaminamiento contienen direcciones de red o subred.
    - En switches, las tablas almacenan direcciones MAC de los hosts.

---

- Características de una dirección IPv4
    - Identificación y Comunicación:
        - Identifican dispositivos en una red y permiten la comunicación.
        - Sin configurar la IP, un dispositivo carece de conectividad fuera de la red local.
    - Jerarquía y Ubicación Física:
        - Son jerárquicas y permiten determinar la ubicación física de un dispositivo.
        - Esto permite localizar geográficamente el dispositivo, de manera similar a cómo un número de teléfono tiene un código de área
    - Especificaciones:
        - Formadas por 32 bits.
        - Son direcciones lógicas y no físicas, pudiendo cambiar dinámicamente.
    - Notación y Conversión:
        - Notación decimal con cuatro bytes separados por puntos.
        - Se convierten a binario para manipular rangos, pero se configuran en formato decimal
        
        ![imagen.png](imagen.png)
        
        <aside>
        💡
        
        recordar de como pasar  a binario
        
        </aside>
        
- Estructura de una direccion ipv4 (red-host)
    
    La dirección IP se divide en dos partes, la primera que hace referencia a la red a la cual está conectado un dispositivo (por esto se dice que es jerárquica), y la parte de Host, que hace referencia al dispositivo mismo, su identificador.
    
    ![imagen.png](imagen%201.png)
    

#### ==Clases de direcciones IPv4✅

Según cuántos bytes tome cada parte, podemos tener diferentes clases de direcciones:

- ==Clases
    
    ![imagen.png](imagen%202.png)
    
    ![imagen.png](imagen%203.png)
    
- ==Como determinal la clase de una direccion ipv4 ✅
    
    La determinación de la clase de una dirección IPv4 se basa en el valor del primer byte. El valor más pequeño en binario que se puede utilizar para la red de la clase A es 00000001, que en decimal es 1. Por lo tanto, la dirección
    inicial es 1.0.0.0, esto es porque La dirección de red 0 está reservada, no se puede asignar a una máquina o red específica
    
    ![{BABD9E9C-50E2-4C3E-B959-DE22E6F99C74}.png](BABD9E9C-50E2-4C3E-B959-DE22E6F99C74.png)
    
- ==Cantidad de redes y de hosts ✅
    
    La cantidad de redes y hosts en las clases A, B y C se determina por la cantidad de bits libres para direcciones.
    Se utiliza la fórmula $2^n$, donde "n" es el número de bits libres. 
    
    - La resta de 2 en la fórmula se debe a que se reservan dos direcciones: una para la dirección de red y otra para la dirección de broadcast. Esto se debe al manejo de componentes en una red y al envío de mensajes en broadcast, que se refiere a transmitir un mensaje a todos los dispositivos de una red local, y un router divide dominios de broadcast.
    
    ![{50AE472A-40E2-4742-9983-1E5700F2A083}.png](50AE472A-40E2-4742-9983-1E5700F2A083.png)
    
    ![es -2 por la dos reservadas](DD05CE86-508A-42C5-A03D-5F419EA6BFA0.png)
    
    es -2 por la dos reservadas
    

![imagen.png](imagen%204.png)

- ejemplo para poner en practica las clases de direcciones IPv4
    
    ![{7715B852-622A-447B-B454-1579610BBF8D}.png](7715B852-622A-447B-B454-1579610BBF8D.png)
    
    1. clase A
    2. clase B
    3. clase c

#### ==Máscara de red/subred✅

La Máscara de red tiene como función identificar la parte de red de una dirección IPv4. La máscara es una dirección especial reservada, que acompaña a la dirección IP, que tiene 1 consecutivos en la parte de Red y 0 consecutivos en la parte de  Host. Otra forma de expresar la máscara es mediante la utilización de un prefijo, que representa la cantidad de bits encendidos para formar la máscara de red

![mascara por defecto](73088CA8-5FD9-4216-90E5-4A86A6B02C2F.png)

mascara por defecto

<aside>
💡

QUE ES   identificar la parte de red de una dirección IPv4???

</aside>

Ejemplo:

![{A1CDD0A7-5CDA-4885-8F5A-02356A0EB63E}.png](A1CDD0A7-5CDA-4885-8F5A-02356A0EB63E.png)

#### ==Direcciones de red✅

entonces como vimos la mascara de red sirve para identificar la red a cual pertenece una direccion ip

Por ejemplo, si tenemos la dirección IPv4 172.10.2.3

se puede deducir que se trata de una red de clase B→ R.R.H.H

como podemos averiguar a al red que pertenece? aca hacemos uso de la macara

![solo verificar 1 and 1 =1](6F22FA34-ECB0-4789-B0FC-92D6780E2DF7.png)

solo verificar 1 and 1 =1

> **==DIRECCION ==RESERVADA==
Dirección de Red:** Identifica a la red en sí misma. Se reconoce porque todos los bits de la porción de host están apagados (en 0)
> 
- Direcciones reservadas o especiales
    
    porque haciamos -2 antes?
    
    una es por la direccion de red y la otra es por
    
    > 
    > 
    > 
    >  **180.23.255.255 Dirección de Broadcast (Difusión):** Se utiliza para enviar un paquete a todos los dispositivos de la red al mismo tiempo. Se caracteriza por tener todos los bits de la porción de host encendidos (en 1).
    > 
    > - *Nota:* Por existir la Dirección de Red y la Dirección de Broadcast, la fórmula para calcular las IP válidas siempre es restar dos direcciones al total posible (ej. 2n−2)
    
    ![{786D4F9E-3E14-4CE5-9413-8841B2612D29}.png](786D4F9E-3E14-4CE5-9413-8841B2612D29.png)
    
- ==RANGO DE DIRECCIONES IP VÁLIDAS (NO SON RESERVADAS)==
    
    Los rangos de direcciones IP asignables a dispositivos se determinan según la clase de red. En la interfaz del router, se establece la primera o última dirección IP válida.
    
    1. Por ejemplo, en una red de clase C con la dirección R.R.R.H, al examinar el último byte "H"(el 0 en el ejemplo) y expresarlo en binario, la dirección de red tiene los 8 bits apagados para la primera combinación binaria y todos los bits encendidos para la broadcast, resultando en 254 direcciones IP válidas (2^8 - 2).
        
        ![{08BBA457-48F7-42A0-820A-E29D27427B4E}.png](08BBA457-48F7-42A0-820A-E29D27427B4E.png)
        
        1. En una red de clase B con la dirección R.R.H.H:
            1. Dirección de red: 150.30.0.0 (Bytes host = 0)
            2. Rango de IP válidas: desde 150.30.0.1 hasta 150.30.255.254
                1. 2^16-2
            3. Broadcast de red: 150.30.255.255 (Bytes host = 1)
        2. En una red de clase A con la dirección R.H.H.H:
            1. Dirección de red: 14.0.0.0
            2. Rango de IP válidas: desde 14.0.0.1 hasta 14.255.255.254 (Empieza en impar y termina siempre en par)
                1. 2^24-2
            3. Broadcast de red: 14.255.255.255
- ==Direcciones privadas RFC 1918==
    
    RFC→ reques for 
    
    > ***Direcciones Privadas (RFC 1918):** Se crearon para evitar el agotamiento global de las direcciones IPv4. Se utilizan libremente dentro del ámbito privado de un hogar o empresa. Pueden repetirse en distintas organizaciones en el mundo, pero jamás pueden estar duplicadas dentro de una misma red local, y **no son visibles desde Internet***
    > 
    - vs direcciones publicas
        
        > **Direcciones Públicas:** Son direcciones únicas e irrepetibles a nivel global (como un número de teléfono único). Son obligatorias para poder navegar y tener conectividad directa en Internet
        > 
    
    Características:
    
    - uso privado
    - No visbiles desde internet
    - Necesidad de traduccion de direcciones
    
    > ***Traducción de Direcciones:** Es el proceso que ejecuta un router para sustituir la IP privada local de un dispositivo por una IP pública, permitiendo así que la información logre salir a Internet y volver*
    > 
    
    ![{55E357CB-72AF-4EFC-8977-F072A0A68617}.png](55E357CB-72AF-4EFC-8977-F072A0A68617.png)
    
    <aside>
    💡
    
    CUANTAS DIRECCIONES de red clase a PRIVADAS EXISTEN?
    
    es una sola, solamente es la 10
    
    clase b, son 16
    
    clase c son 256, por el 3er byte es de REd
    
    </aside>
    
- **Parámetros de Conectividad** Para que una computadora tenga conectividad completa
    1. **Dirección IP:** Identificador dentro de la red local.
    2. **Máscara de red:** Para entender el límite de su propia red.
        1. HASTA ACA PODRIA HACER UNA LAN
    3. **Puerta de enlace (Gateway):** Es la dirección IP del router. Obligatoria para que el equipo pueda salir de su red local y comunicarse con redes externas o con Internet.
    4. **Servidor DNS (Domain Name System):** Sistema o aplicación encargada de traducir nombres de dominio comprensibles para humanos (ej. google.com) en las direcciones IP numéricas que necesitan las máquinas para poder enviar los paquetes a través de Internet
- ej de practica
    
    ![{F12BE9F6-4635-4C3C-BB5F-84327925AA37}.png](F12BE9F6-4635-4C3C-BB5F-84327925AA37.png)
    
    <aside>
    💡
    
    **El cálculo de la última dirección IP válida (Error muy común):** El profesor hizo un gran énfasis al corregir un ejercicio, advirtiendo sobre un error frecuente que cometen los alumnos al calcular el rango de direcciones IP. Recalcó tener mucho cuidado al determinar la última IP válida de una red, señalando que es un error "muy común" poner simplemente un `254` al final y dejar los octetos anteriores en `0` (por ejemplo, `126.0.0.254` en una red de Clase A), cuando lo correcto es que todos los bits de la porción de host previos estén encendidos (por ejemplo, `126.255.255.254`)
    
    </aside>