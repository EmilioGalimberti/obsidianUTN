La **[[Trama Ethernet]]** es la pieza clave que conecta el mundo del software con el mundo físico. Es el "vehículo" o la "caja" que la Capa de Enlace de Datos arma para que la información pueda viajar por los cables.

### 1. Su relación con la Capa de Enlace de Datos (PDU)

Cada capa del Modelo OSI le da un nombre distinto a los datos (a esto se le llama PDU: Unidad de Datos del Protocolo).
- En la Capa 3 (Red) los datos se llaman _Paquetes_.
- **En la Capa 2 (Enlace de Datos) los datos se llaman _Tramas_**. La **Subcapa MAC** es literalmente la obrera encargada de construir esta trama, agregándole un "encabezado" y una "cola" protectora al paquete que viene de arriba (el proceso de **[[Encapsulamiento y Desencapsulamiento]]** o "mamushkas" que mencionó tu profesor).

### 2. Su relación con el Estándar IEEE 802.3

Como vimos recién, **[[IEE 802.3 (Ethernet)]]** son las "reglas del juego". Bueno, este estándar es el que dicta **exactamente qué forma debe tener la Trama Ethernet**. Es el que dice: _"La trama debe empezar con un Preámbulo para sincronizar, luego debe tener las direcciones MAC, y al final un código de error"_.

### 3. Su relación con las Direcciones MAC

Las **[[Dirección MAC|Direcciones MAC]]** no viajan sueltas por el cable; **son campos específicos dentro de la cabecera de la Trama Ethernet**. La trama coloca estratégicamente la _MAC de Destino_ primero para que las placas de red de las otras computadoras puedan leerla rápido y descartar la trama velozmente si no es para ellas.

---
# Estructura de la [[Trama Ethernet]]
la relacion con los temas anteriores es que la Trama es el pdu de [[CAPA DE ENLACE DE DATOS]] y la [[IEE 802.3 (Ethernet)]] nos dice como se debe armar la trama:

El formato de la trama Ethernet, utilizado en la capa 2 para la transmisión de datos entre máquinas, varía entre Ethernet II y IEEE 802.3.

Ethernet II:
- **[Preámbulo]:** Serie inicial de 8 bytes. Su único fin lógico es lograr sincronizar los relojes del equipo emisor y receptor antes de que empiecen a llegar los datos vitales
- 6 bytes de dirección de destino (MAC).
	- (La destino va primero intencionalmente para permitir el descarte veloz si la trama no corresponde a la máquina).
- 6 bytes de dirección de origen (MAC).
- 2 bytes para el campo tipo que indica el protocolo encapsulado
	- Indica explícitamente qué protocolo de red está viajando encapsulado dentro del espacio de carga útil (por ejemplo, marca si el contenido interno es IPv4, IPv6 o ICMP)
- 46 bytes de datos (pueden incluir 4 bytes de relleno).
- 4 bytes de secuencia de verificación de tramas (CRC).
	- **[FCS] (Secuencia de Verificación de Trama):** Algoritmo matemático para descartar tramas que hayan sido dañadas en tránsito. Ethernet _no_ retransmite si hay error, es una tecnología de "máximo esfuerzo".![[{97BF7CD5-1C12-4AEE-8207-8ADC6F458196}.png]]

IEEE 802.3
*  Preambulo de 7 bytes y delimitador de inicio de trama de 1 byte.
* 6 bytes para dirección de destino y 6 para dirección de origen (MAC).
* Campo tipo > 1536. Protocolo que se está usando. Dice que se encapsuló de la capa de arriba.
* Campo longitud <= 1536. Tamaño de la trama, lo que se está enviando de datos en la trama.
* 4 bytes de secuencia de verificación de trama (CRC).*![[{AFCA806D-C616-4CF5-A974-58FE45FA1B17}.png]]

> [!note] **Fórmulas para el Cálculo del Tamaño de la Trama Ethernet** El profesor indica que la carga útil (los datos) oscila entre 46 y 1500 bytes, y a esto se le suma una cabecera y cola fijas de 18 bytes (excluyendo el preámbulo). $$ Tamaño_{Mínimo} = 46_{bytes (Datos)} + 18_{bytes (Cabecera/Cola)} = 64_{bytes} $$ $$ Tamaño_{Máximo} = 1500_{bytes (Datos)} + 18_{bytes (Cabecera/Cola)} = 1518_{bytes} $$

El tamaño mínimo de una trama Ethernet es de 64 bytes, compuesto por 46 bytes de datos más 18 bytes de la cabecera (dirección destino, dirección origen, longitud) y la cola (secuencia de verificación de la trama). Este cálculo excluye el preámbulo, y la trama comienza después de este.

El tamaño máximo permitido es de 1518 bytes, con 1500 bytes como máximo de datos y los restantes 18 bytes de la cabecera y la cola (6 de dirección de destino, 6 de dirección de origen, 2 de longitud y 4 de secuencia de verificación de trama). La disposición de la dirección de destino antes que la de origen facilita la identificación del destinatario y evita la lectura innecesaria de bits de la dirección de origen.