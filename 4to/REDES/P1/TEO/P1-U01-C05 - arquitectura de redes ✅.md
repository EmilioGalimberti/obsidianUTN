# P1-U01-C05 - arquitectura de redes

clase 5 → no hay clase virtual

[1 - 05 - RED - Unidad 1 - Arquitectura de redes.pdf](1_-_05_-_RED_-_Unidad_1_-_Arquitectura_de_redes.pdf)

Modelo OSI vs. Conjunto de Protocolos TCP/IP

- La conexión entre equipos informáticos es posible gracias a los protocolos de comunicaciones.
- Un protocolo de comunicaciones es un conjunto de reglas perfectamente organizadas y convenidas de mutuo acuerdo entre los participantes en una comunicación, cuya misión es permitir el intercambio de información entre los dos dispositivos, detectando los posibles errores que se produzcan.
- El conjunto de protocolos que facilitan la comunicación entre dispositivos se le denomina arquitectura de la red.

- Problemas en la interconexión de redes
    - ¿Que medio de transmisión vamos a utilizar?
    - ¿Qué dispositivo accede a la red?
    - ¿Como identificamos el dispositivo al que hay que enviar la información?
    - ¿Qué tamaño de datos es permitido?
    - ¿Es necesario codificar la información?.
    - ¿Cómo corregir errores?
    - ¿ QoS?
    - Etc. …

- Con el fin de simplificar la complejidad de cualquier red, los diseñadores de red estructuran en diferentes módulos las reglas de interconexión entre equipos informáticos.
- El objetivo es dividir la problemática inicial en subproblemas más sencillos.
- Para cada uno de estos subproblemas se crea un subconjunto de programas y reglas que le den solución, de tal forma, que cada subproblema puede ser tratado y desarrollado de forma independiente del resto de subproblemas.
- A cada uno de los módulos de la interconexión de equipos se le llama nivel o capa.

- Relaciones entre capas adyacentes
    - Cada capa provee servicios a las capas superiores, haciendo transparente el modo en que estos servicios se llevan a cabo.
    - Cada nivel debe ocuparse exclusivamente de su nivel inmediatamente inferior, a quien solicita servicios, y del nivel inmediatamente superior, a quien devuelve resultados (presta servicios).
    - Se llama interfaz de capa al conjunto de normas de intercomunicación entre capas.
    
    ![{CFA01F30-1927-44F8-A78D-25ED45058E2E}.png](CFA01F30-1927-44F8-A78D-25ED45058E2E.png)
    
- Comunicaciones entre capas homologas
    - Entre máquinas diferentes, el proceso de comunicación se produce entre las capas equivalentes (homólogas).
    - Se dice que la capa N de un emisor se comunica con la capa N de un receptor a través de un protocolo de capa N.
    - Realmente, la petición de servicios va descendiendo por la estructura de capas del emisor hasta el nivel más bajo (ENCAPSULADO), que transmite físicamente la señal al receptor. A partir de ese nivel, se inicia el viaje ascendente por las capas del receptor (DESENCAPSULADO) , hasta llegar a la capa que solicitó el servicio en el emisor.
    
    ![{9ABE8243-70B0-4B1D-ACB5-193D780F52E0}.png](9ABE8243-70B0-4B1D-ACB5-193D780F52E0.png)
    
- MODELOS (OSI,TCP/ip)
    
    ![{F4B1354E-7E04-4777-90E7-A2B89308694F}.png](F4B1354E-7E04-4777-90E7-A2B89308694F.png)
    

## Conjunto de protocolo TCP/IP

Surge a partir de DARPA net, un proyecto militar de los Estados Unidos que utilizó la conmutación de paquetes para la transmisión de datos.

Protocolo:

- Estándar que acuerda la interpretación de tramas de bits entre dispositivos.
- Software que interpreta bits de manera consistente y previamente instalado en los dispositivos de comunicación.
- Ejemplo: al receptor únicamente le llegan unos y ceros, entonces por medio de un protocolo se le dice cómo interpretarlos: los primeros 48 bits son de la dirección origen, los segundos 48 bits son de la dirección destino (es el formato de trama)

TCP/IP es una pila de protocolos (muchos) que trabajan de manera conjunta, siendo TCP (Transmission Control Protocol) e IP (Internet Protocol) los más destacados. 

OBJETIVOS:

- Conectividad permanente: Garantiza la continuidad de la comunicación incluso si se cae un nodo, redirigiendo paquetes por caminos alternativos (conmutación de paquetes).
- Independiente del hardware y del sistema operativo: Implementable sin importar el hardware o sistema operativo subyacente.
- Transmisión de todo tipo de información: Permite la transferencia de archivos de texto, videos, música, etc

MODELOS DE REFERENCIA TCP/IP

- TCP/IP, siglas de Transmission Control Protocol/Internet Protocol, permite la comunicación entre dispositivos conectados a Internet en diversas redes.
- Objetivo de interconectar nodos mediante tecnologías variadas, garantizando robustez y capacidad de supervivencia ante la pérdida de hardware en la subred.
- Utiliza conmutación por paquetes para la transmisión de datos

![{46934121-ED31-4AEE-9159-0ABDAC29032B}.png](46934121-ED31-4AEE-9159-0ABDAC29032B.png)

## FUNCIÓN DE CADA NIVEL

### Capa 1: Host a Red

La función principal de esta capa es facilitar la comunicación entre dispositivos en el mismo segmento de red. 

Sus responsabilidades incluyen el encapsulamiento de datos de la capa de red en tramas para transmisión, control de acceso al medio, detección y corrección de errores, asignación de direcciones físicas únicas (MAC), y control de flujo para garantizar una transmisión eficiente.

![{FD87F677-91D6-4141-8E86-2D28FB0DD1ED}.png](FD87F677-91D6-4141-8E86-2D28FB0DD1ED.png)

por ejemplo:

Para poder transferir datos entre dos máquinas necesito tener alguna dirección para
que el switch sepa a qué maquina le envío los datos (o trama, propiamente dicho), en el
caso de que queramos comunicar la maquina A con la C esta dirección seria la MAC, si
quisiera comunicar la maquina A con la E utilizaría el IP lo que me haría trabajar en la
siguiente capa y no en esta debido a que aquí solo se trabaja entre dispositivos del
mismo segmento.

![{A31C6297-5211-4585-95B9-92225489975D}.png](A31C6297-5211-4585-95B9-92225489975D.png)

### Capa 2: Interred

Actuando como el núcleo central, esta capa permite la inyección de paquetes en
cualquier red y su viaje independiente a través de diferentes redes. Se encarga del encaminamiento de paquetes, asignación de direcciones únicas (IP) (DIRECCIONAMIENTO), fragmentación y reensamblado de paquetes, control de congestión y servicios de calidad de servicio (QoS) para priorizar paquetes importantes.

![{C8DA4A82-044A-45D0-889C-FB1475A83B93}.png](C8DA4A82-044A-45D0-889C-FB1475A83B93.png)

### Capa 3: Transporte

esta capa tiene como función conectar dispositivos extremos a extremo. Esta conexión, es una conexión lógica, no física. Dos protocolos de transporte son TCP (confiable y orientado a la conexión) y UDP (sin conexión y no confiable). Sus funciones incluyen segmentación y reensamblado de datos, control de flujo, multiplexación, identificación de aplicaciones mediante números de puerto y verificación de integridad de datos.

![{33F03869-35B9-489D-B9D9-5451CD2B75D7}.png](33F03869-35B9-489D-B9D9-5451CD2B75D7.png)

### Capa 4: Aplicación

Esta capa no incluye sesiones ni presentación y alberga todos los protocolos de alto nivel. Compuesta por aplicaciones o procesos de alto nivel, es responsable de generar, enviar o recibir datos. Las capas de sesión y presentación no se consideraron necesarias en este modelo.

![{B7971BC5-AC16-43B4-8933-EB934C421958}.png](B7971BC5-AC16-43B4-8933-EB934C421958.png)

![{9C21398E-E3D2-42A0-B55F-0B1D03F3AE14}.png](9C21398E-E3D2-42A0-B55F-0B1D03F3AE14.png)

---

- y de la nada aca wireshark
    
    ![{082F7379-0E66-40D2-8699-0EBCD8C1971A}.png](082F7379-0E66-40D2-8699-0EBCD8C1971A.png)
    

CLASE 6 → NO HAY CLASE VIRTUAL