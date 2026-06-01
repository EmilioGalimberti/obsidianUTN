# Unidad 1 – Arquitectura de Redes

CONTENIDOS:

- Introducción
    - Concepto de Red de telecomunicación
    - Clasificación de las redes
- Arquitectura de protocolos TCP/IP
    - Historia
    - Modelo de referencia TCP/IP
    - Función de cada nivel
    - Conjunto de Protocolos
    - Encapsulamiento y desencapsulamiento
- Internet
    - Orígenes
    - Características
    - Servicios básicos
    - Arquitectura de Internet (niveles)
    - Organismos Internacionales de Normalización: ITU, ISO, IEEE,
    Estándares IETF: RFC.

Introduccion - Clase 1 (grabe audio)

[1 - 01 - RED - Unidad 1 - Parte 1_cb0fae546c8dec826dc6d91288929cb7.pdf](1_-_01_-_RED_-_Unidad_1_-_Parte_1_cb0fae546c8dec826dc6d91288929cb7.pdf)

- concepto de red de telecomunicacion
    
    ¿Cuáles son los componentes de una red informática?
    
    Los **componentes esenciales de una red informática** abarcan una combinación de hardware y software necesarios para establecer la comunicación. Estos componentes se pueden desglosar en los siguientes elementos principales:
    
    - **dispositivos finales: Equipos con los que interactúa el usuario o que brindan servicios finales (PCs, servidores, impresoras, celulares).**
    - **Dispositivos de interconexión (o intermedios):** Son los aparatos encargados de unir los dispositivos finales y dirigir el tráfico de datos, destacándose principalmente los **switches**, **routers**, **módems** y **Access Points** (puntos de acceso).
    - **Medios de comunicación:** Constituyen el canal por el cual se transmiten los datos, pudiendo ser medios **guiados** (conexiones físicas a través de cables) o **no guiados** (conexiones inalámbricas a través del aire).
    - **Placa de red:** También conocida como tarjeta de interfaz de red (NIC), es el hardware que permite que un dispositivo se conecte físicamente al medio de comunicación.
    - **Sistema Operativo:** Es el software base indispensable que deben ejecutar los dispositivos (tanto directivos, finales como intermedios) para funcionar de manera compatible en la red.
    - **Protocolo de comunicación:** Representa el conjunto de reglas y estándares lógicos que permiten a los distintos dispositivos "hablar" y entender el mismo idioma para interpretar la información correctamente.
    
    ¿Qué es una red de telecomunicación?
    
    Red de telecomunicación: Una red de telecomunicaciones es un conjunto complejo de medios, tecnologías, protocolos y facilidades diseñadas para facilitar el intercambio de información entre usuarios distantes. Esta estructura posibilita la transferencia de datos desde un emisor hasta un receptor ubicado a larga distancia a través de un medio de comunicación, permitiendo la comunicación efectiva.
    
    a diferencia de:
    
    Red informática: los dispositivos están cercanos entre sí, en una red de telecomunicaciones los dispositivos están separados por grandes distancias, lo que requiere atravesar nodos para establecer la conexión. La raíz "tele" en telecomunicaciones denota la idea de distancia
    
- clasificacion de las redes ✅
    - 1. Según el área de cobertura (Alcance)
        - **PAN (Personal Area Network):**  alcance muy limitado (aprox. 1 metro), utilizadas para conectar una computadora con sus dispositivos periféricos.
        - **LAN (Local Area Network):** Redes de área local privadas que enlazan dispositivos dentro de un área pequeña como un edificio, permitiendo compartir recursos e intercambiar información.
        - **MAN (Metropolitan Area Network):** Redes de área metropolitana que pueden cubrir toda una ciudad (por ejemplo, las redes de televisión por cable).
        - **WAN (Wide Area Network):** Redes de área amplia y de alcance extenso que pueden abarcar países o continentes.
        - **Internet (o GAN - Global Area Networks):** Redes de alcance mundial formadas por nodos interconectados a nivel global.
    - 2.Según la tecnología de transmisión
        - **Redes de difusión (o broadcast):** Utilizan un canal de comunicación compartido, donde los datos son enviados a través de un mismo medio a varios dispositivos.
        - **Redes punto a punto:** Los datos viajan de forma directa desde un punto específico a otro.
            - como un switch, que enlaza directamente a los puestos de trabajo.
    - 3.Según la topología física
        
        ![{21669DE2-D916-400D-969B-5271A55E8373}.png](21669DE2-D916-400D-969B-5271A55E8373.png)
        
    - 4.Según la direccionalidad de los datos
        - **Símplex:** La comunicación ocurre en un único sentido, como en la radiocomunicación.
        - **Semidúplex (Half-dúplex):** Existe comunicación en ambos sentidos, pero no de forma simultánea (ej. mensajería unidireccional o *walkie-talkies*).
        - **Dúplex (Full-dúplex):** Permite la transmisión de información en doble sentido y de manera simultánea, como en las llamadas telefónicas.
    - 5.Según el ancho de banda
        
        Se dividen principalmente en redes de **banda angosta** y redes de **banda ancha**
        
    - 6.Según la movilidad de los dispositivos
        
        Se agrupan en redes **fijas (o alámbricas)** y redes **móviles (o inalámbricas)**