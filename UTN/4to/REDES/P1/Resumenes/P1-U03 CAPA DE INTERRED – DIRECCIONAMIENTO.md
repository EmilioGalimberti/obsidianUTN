# TEMAS
* Direccionamiento IPv4  ❌
* Protocolo IPv4
	* Caracteristicas de una Direccion IPv4 ✅
	* Estructura de una direccion IPv4✅
	* Clases de direcciones IPv4 ✅
		* Como determinar la clase de una direccion IPv4? ✅
		* Cantidad de Redes y cantidad de host ✅
	* Mascara de Red/Subred ✅
	* Direcciones de RED 
		* Direcciones Especiales o Reservadas ❌
		* Rango de dirccion IP validas (NO RESERVADAS) ✅
		* Direcciones privadas RFC ✅
	* Sistema binario ❌
	* Subredes
		* Caracteristicas ❌
		* Calculo de las subredes ✅
		* Mascara de Subred ✅
		* Concluciones sobre subredes ✅
		* Obtener la subred a partir de una IP ✅
		* Conculsiones de ejercicios ❌
	* Direccionamiento IPv4-VLANS
		* Concepto Vlan ✅
		* Implementacion de las VLANS✅
			* Protocolo IEE 802.1q
		* Tipos de vlans✅
			* Estaticas✅
			* Dinamicas✅
	* Agotamiento de direcciones IPv4
		* Causas ❌
		* asigancion de direcciones IPv4 por clases ❌
		* Soluciones de agotamiento
			* Direccionamiento privado ❌
			* Traducciones de direcciones de red privadas (NAT) ❌
			* CIDR ❌
				* SUMARIZACIÓN O RESUMEN DE RUTAS✅
			* VLSM (Máscaras de subred de longitud variable) ❌
			* -
		* Administracion de direcciones IP ❌



# RESUMEN POR PREGUNTAS
## DIRECCIONAMIENTO IPV4❌
Internet Protocol es un protocolo, perteneciente a la capa de Internet del TCP/IP y a la capa de Red del modelo OSI, que asigna direcciones a dispositivos para permitir la comunicación. La IPv4 es una de las dos versiones actuales del protocolo IP, siendo esencial para las redes de difusión, ya que las direcciones IP facilitan que los mensajes lleguen de una PC a otra específica.
## ipv4
Se denomina IPv4 por pertenecer a la capa de Interred y es esencial para la conectividad global de Internet.
* Funcionamiento:
	* • Recibe segmentos de la capa de transporte y los encapsula en paquetes con cabeceras.
	* • Cada paquete se encamina de manera independiente, dividido en trozos más pequeños.
*  Eficiencia y Robustez:
	* • Encaminar paquetes es lento pero robusto, permitiendo rutas alternativas en caso de fallos.
	* • Utiliza máscara de red y tablas de encaminamiento, considerando la dirección IP de destino.
*  Roles en Dispositivos de Red:
	* • En routers, las tablas de encaminamiento contienen direcciones de red o subred.
	* • En switches, las tablas almacenan direcciones MAC de los hosts.
*  Características de IP:
	* • No es orientado a conexión y no garantiza la entrega de paquetes al destino.
	* • TCP asegura la entrega fiable de datos y gestiona la retransmisión de segmentos perdidos.
*  Razones para la No Entrega:
	* • Pérdida de paquetes por caída de red o enlaces.
	* • Congestión de la red, donde la memoria de los routers se llena y descarta paquetes.

### ==1 Cuál de las siguientes características corresponde al protoclo IPv4: ⚠️==
- [ ] Encapsula una trama de datos 
- [ ] Pertenece a la capa de enlace de datos 
- [ ] Orientado a la conexión 
- [ ] Construye segmentos
- [ ] No fiable 
- [ ] Garantiza que los datos se entreguen en el destino
#### rta
No fiable

justif:
La respuesta correcta es: **No fiable**.

Para comprender el **porqué** de esta respuesta y mantener el análisis arquitectónico de causa y efecto, debemos observar cómo el modelo TCP/IP distribuye las responsabilidades entre sus capas:

- **La Causa (La división de tareas):** En la arquitectura de redes, el protocolo IPv4 opera en el **Nivel de Interred (Capa 3)**. Su objetivo central es identificar a los dispositivos mediante direcciones IP y buscar el mejor camino (encaminamiento) para que los paquetes viajen de forma independiente a través de diferentes redes hacia su destino.
- **El Efecto (La falta de fiabilidad):** Como consecuencia de este diseño, IPv4 se enfoca exclusivamente en tratar de enrutar el paquete haciendo su "máximo esfuerzo", pero **no es un protocolo fiable** por sí mismo. No establece conexiones previas, no verifica la integridad de los datos útiles y no tiene mecanismos nativos para reenviar paquetes perdidos, delegando toda esa responsabilidad a las capas superiores.

**Por qué las demás opciones son incorrectas:**

- **Garantiza que los datos se entreguen en el destino** y **Orientado a la conexión:** Estas dos características son falsas para IPv4 porque corresponden exclusivamente al protocolo **TCP** (Nivel de Transporte). Es la capa de transporte la que establece una conexión lógica de extremo a extremo y quien asume la carga de "garantizar una transmisión fiable", asegurándose de que los datos lleguen a destino sin errores, ordenados, y solicitando retransmisiones si algo falla.
- **Construye segmentos:** Existe un error en la unidad de datos (PDU). La acción de tomar los datos de la aplicación y dividirlos para construir "segmentos" es una función de la **Capa de Transporte (Capa 4)**. El protocolo IPv4 toma esos segmentos y construye **paquetes** (o datagramas).
- **Encapsula una trama de datos:** Esto plantea la lógica inversa de encapsulamiento. IPv4 nunca encapsula tramas; de hecho, ocurre lo contrario. La Capa de Enlace de Datos (Capa 2) es la que recibe el paquete IPv4 armado y lo encapsula dentro de una **trama** (agregando las direcciones MAC origen y destino) para inyectarlo en el medio físico local.
- **Pertenece a la capa de enlace de datos:** Falso por ubicación en la arquitectura. Como mencionamos, la capa de enlace de datos corresponde a la Capa 2 (donde operan tecnologías como Ethernet o Wi-Fi), mientras que IPv4 opera un nivel más arriba, en la **Capa de Interred o de Red (Capa 3)**.
### ==2 Cuál de las siguientes características corresponde al protocolo IPv4:== ⚠️
- [ ] Es fiable
- [ ] Encapsula una trama en un paquete
- [ ] Pertenece a la capa Host a Red
- [ ] Encapsula un segmento en una trama
- [x] Es no orientado a conexión
- [ ] Garantiza que los datos se entreguen ordenados en el destino
- [ ] Un paquete puede quedar dando vueltas eternamente en la red
#### rta
Es no orientado a conexión


### ==3 Cuál de las siguientes características corresponde al protocolo IPv4:== ⚠️
- [ ] Utiliza números de secuencia
- [x] Encamina cada paquete de manera independiente
- [ ] Utiliza direcciones de 48 bits
- [ ] Retransmite el paquete que no llegó correctamente
- [ ] Reordena los paquetes en el destino
#### rta
IP es el responsable de dirigir cada paquete desde el origen hasta el destino a través de la
red, independientemente de los demás paquetes.
Cada paquete IP puede tomar una ruta distinta, dependiendo de la congestión, estado de
los routers, etc.

¿y TCP?
TCP no realiza encaminamiento. TCP opera en la capa de transporte, y sus funciones
clave son:
Control de �ujo
Control de errores (retransmite lo perdido)
Ordenación de paquetes: si llegan desordenados, los reordena en el destino antes de
entregar a la aplicación.
### == 4 ¿Qué característica distingue a una dirección IP de una dirección MAC?==
 - [ ] a IP no se puede cambiar.
 - [ ] La MAC es jerárquica.
 - [x] La IP es lógica y con�gurable.
 - [ ] La MAC pertenece a la capa de red
#### rta
La IP es lógica y con�gurable.
### caracteristicas
* Identificación y Comunicación:
	* • Identifican dispositivos en una red y permiten la comunicación.
	* • Sin configurar la IP, un dispositivo carece de conectividad fuera de la red local.
* • Jerarquía y Ubicación Física:
	* • Son jerárquicas y permiten determinar la ubicación física de un dispositivo.
* • Especificaciones:
	* • Formadas por 32 bits.
	* • Son direcciones lógicas y no físicas, pudiendo cambiar dinámicamente.
* • Notación y Conversión:
	* • Notación decimal con cuatro bytes separados por puntos.
	* • Se convierten a binario para manipular rangos, pero se configuran en formato decima
##  Clases de direcciones IPv4
Según cuántos bytes tome cada parte, podemos tener diferentes clases de direcciones:

| Clase | Bit de inicion binario | direccion inicial | direccion final | mascara por defecto | uso especifico                                            | estructura |
| ----- | ---------------------- | ----------------- | --------------- | ------------------- | --------------------------------------------------------- | ---------- |
| A     | 0                      | 1.0.0.0           | 127.255.255.255 | 255.0.0.0 (/8       | **Asignación Comercial**<br>muchísimos hosts.             | R.H.H.H    |
| B     | 10                     | 128.0.0.0         | 191.255.255.255 | 255.255.0.0 (/16)   | tamaño medio                                              | R.R.H.H    |
| C     | 110                    | 192.0.0.0         | 223.255.255.255 | 255.255.255.0 (/24) | muchas redes pequeñas (como PYMES) que tienen pocos hosts | R.R.R.H    |
| D     | 1110                   | 224.0.0.0         | 239.255.255.255 | _No aplica_         | ==Multidifusión (Multicast)==                             |            |
| E     | `1111`                 | 240.0.0.0         | 254.255.255.255 | _No aplica_         | **Uso Experimental:**                                     |            |

### == 5 ¿Qué tipo de dirección IP es la que permite que se conecten la mayor cantidad de hosts?==
- [ ] Clase C
- [x] Clase A
- [ ] Clase B
#### rta
Clase A
### ==6¿Cuál es el uso de las redes clase D?==
- [ ] Crear redes
- [ ] Subnetting
- [x] Multicast
- [ ] Broadcast
- [ ] Unicast
#### rta
Multicast

Las direcciones Clase D en IPv4 van desde 224.0.0.0 hasta 239.255.255.255.
¿Para qué se usan?
Para Multicast, que es una forma de enviar datos a un grupo especí�co de
dispositivos, no a todos (como en broadcast) ni a uno solo (como en unicast).
### Como determinar la clase de una direccion IPv4?

#### ==7Si una dirección IP empieza con el byte 200, pertenece a la clase:==
- [ ] A
- [ ] B
- [x] C
##### rta
Clase C

justif
200 la clase c es entre 192 a 223

o en binario

128 64 32 16 8 4 2 1
1       1    0

110 es clase C


#### ==8Una dirección IP que comienza con los bits 1110, ¿Qué clase de dirección es?==
- [ ] Todas
- [ ] Clase C
- [ ] Clase B
- [ ] Clase A
- [x] Clase D
##### rta
Clase D
#### ==9¿Cómo se determina la clase de una dirección IPv4? Seleccione una:
- [ ] Ninguna de las opciones
- [x] Por el valor del primer byte
- [ ] Por la cantidad de host
- [ ] Por la máscara
- [ ] Por la cantidad de redes
##### rta
Por el valor del primer byte

#### ==10Si una dirección IP comienza con 191, ¿Qué clase de dirección es?==
- [ ] A
- [x] B
- [ ] C
##### rta
B

justif por el rango de 128 a 191

o

191 a binario

128 64 32 
1      0

y si `0` es clase  A , `1 0` es clase B
### Cantidad de Redes y cantidad de host
cantidad de redes : 2^n -> n son la cantidad de bits en RED

cantidad de host es: 2^h-2 ->h la cantidad de bits disponibles 
(cantidad de direcciones validas seria)

La resta de 2 en la fórmula se debe a que se reservan dos direcciones: una para la dirección de red y otra para la dirección de broadcast.



## Mascara de Red/Subred
La Máscara de red tiene como función identificar la parte de red de una dirección IPv4


### ==11¿Cual es la función de la máscara en una dirección IPv4? Seleccione una:
- [ ] Determinar la puerta de enlace
- [ ] Ninguna de las opciones
- [x] Determinar la porción de red
- [ ] Determinar la clase
- [ ] Determinar la cantidad de host de esa red
#### rta
Determinar la porción de red


### 12¿Qué característica particular distingue a las direcciones de red de las máscaras de subred?

**La Función (Identificación vs. Delimitación):**
- La **dirección de red** es un identificador  cuya función es **representar a la red en sí misma** y agrupar a todos los dispositivos que pertenecen a ella,.
- En contraposición, la **máscara de subred** su función exclusiva es actuar como una plantilla matemática para **determinar qué porción de una dirección IPv4 corresponde a la red y qué porción corresponde al host**,,.
**2. La Estructura Binaria (El formato estricto):**
- en la **máscara de subred**, debe estar conformada por **bits encendidos (en "1" (representando la red/subred), seguidos por **bits apagados (en "0") (representando los hosts),. 
- Por su parte, la **dirección de red** puede tener cualquier combinación de unos y ceros en su "parte de red" (dependiendo de la red lógica asignada), pero su rasgo definitorio es que tiene **absolutamente todos los bits apagados (en "0") en la "parte de host"**.

**3. La Regla de Asignación (Reserva vs. Parámetro inseparable):**

- La **dirección de red** es estrictamente una **dirección reservada**; debido a su naturaleza general, jamás se le puede asignar ni configurar a la tarjeta de red de una PC, a un servidor, o a la interfaz de un router.
- Por el contrario, la **máscara de subred** es un **parámetro de configuración obligatorio** e inseparable que debe ingresarse en conjunto con cualquier dirección IP de host válida, ya que sin la máscara, el dispositivo es incapaz de interpretar su propio esquema de red
### ==13¿Cómo hace el router para extraer solo el NetID de la dirección IP?==
- [ ] Determina la clase y obtiene la NetID
- [ ] Determina la clase y obtiene la HostID
- [ ] Obtiene la máscara de la dirección IP
- [x] Determina la clase, aplica la máscara adecuada y realiza la operación AND
- [ ] Aplica la máscara y realiza la operación AND
#### rta
Determina la clase, aplica la máscara adecuada y realiza la operación AND
## Direcciones de RED
Por ejemplo, si tenemos la dirección IPv4 172.10.2.3, rápidamente se puede deducir que se trata de una red de clase B, por lo que la dirección de red a la que pertenece es 172.10.0.0, siendo su dirección de broadcast 172.10.255.255. Para poder resolver esto, podemos emplear el AND booleano:

| AND                                  |
| ------------------------------------ |
| siempre 0 a menos que<br>1 AND 1 = 1 |
![[{BA01ED98-EC0A-4C57-B9D7-9C44A1FD6411}.png]]
### Direcciones Especiales o Reservadas
| Dirección IP / Rango            | Significado                                               | Descripción                                                                                                                                                              |
| :------------------------------ | :-------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0.0.0.0**                     | Este host (dirección local).                              | Todos los 32 bits son 0.                                                                                                                                                 |
| **0.0.0.24**                    | Un host de la red.                                        | Dirección utilizada para representar un host específico dentro de una red.                                                                                               |
| **255.255.255.255**             | Difusión en esta red local.                               | Todos los 32 bits son 1. Se utiliza para enviar mensajes a todos los dispositivos en la red local (broadcast).                                                           |
| **180.23.0.0 - 180.23.255.255** | Dirección de red clase B y difusión en la red 180.23.0.0. | Representa una red específica de clase B y su dirección de difusión.                                                                                                     |
| **127.x.x.x**                   | Dirección de loopback - localhost.                        | Reservada para pruebas y diagnósticos; utilizada para dirigir el tráfico de red de vuelta al mismo dispositivo. La "x" puede ser cualquier valor en el rango de 0 a 255. |
#### ==14Cuáles de las siguientes afirmaciones son correctas en relación a la dirección IPv4 0.0.0.0 (seleccione dos):==
- [x] Identifica al propio dispositivo cuando no tiene asignada una dirección IPv4
- [ ] Se utiliza cuando se desea enviar un paquete a todos los dispositivos de una LAN
- [x] Sólo puede aparecer en la dirección IP origen de un paquete IPv4
- [ ] Esa dirección nunca puede aparecer en la cabecera de un paquete IPv4
- [ ] Identifica todos los dispositivos de la LAN
##### rta
- [ ] Identifica al propio dispositivo cuando no tiene asignada una dirección IPv4
- [ ] - [ ] Sólo puede aparecer en la dirección IP origen de un paquete IPv4

0.0.0.0 es una dirección no enrutable que se utiliza para identi�car al host local cuando
aún no tiene una dirección IP asignada.
Sólo puede usarse como dirección de origen (mensaje DHCPDISCOVER desde 0.0.0.0
hacia 255.255.255.255) nunca como destino, ya que no identi�ca a ningún host
especí�co.
#### 15La dirección IPv4 0.0.0.0:
- [ ] Representa una puerta de enlace de la LAN
- [ ] Está prohibido su uso
- [ ] Puede aparecer en la dirección de una trama
- [x] Se utiliza en la dirección origen del paquete DHCPdiscover
- [ ] Representa todos los host de una LAN
##### rta
- [ ] Se utiliza en la dirección origen del paquete DHCPdiscover

Cuando una PC recién se prende y no tiene IP, quiere pedirle una al servidor DHCP. Pero
como todavía no sabe su propia dirección, usa la 0.0.0.0 como IP de origen.
El mensaje que manda se llama DHCP Discover, y sale con:
Origen: 0.0.0.0
Destino: 255.255.255.255 (para que lo escuchen todos)
#### ==16La dirección IPv4 127.1.1.1:==
- [ ] Es una dirección privada
- [ ] Es la puerta de enlace de una LAN
- [ ] Es una dirección multicast
- [ ] El administrador la configura en un host en producción
- [x] Permite verifcar la correcta instalación de la pila de protocolos TCP/IP
##### rta
Permite verifcar la correcta instalación de la pila de protocolos TCP/IP
La dirección 127.1.1.1 pertenece al rango 127.0.0.0/8, que está reservado para loopback o
localhost.
Este tipo de dirección no sale a la red, sino que se utiliza para probar la con�guración
interna del protocolo TCP/IP en el propio equipo.
La más común es 127.0.0.1, pero cualquier IP dentro del rango 127.x.x.x cumple la misma
función
#### ==17Un router recibe por una de sus interfaces un paquete cuya dirección destino es 255.255.255.255==
- [ ] Se lo envía al servidor de la LAN
- [ ] Se lo envía a todas las PCs de la LAN
- [x] Lo procesa
- [ ] Lo retransmite por todas sus interfaces, menos por la que ingresó.
- [ ] Lo encapsula en una trama.
##### rta 
La respuesta correcta es:

- [x] **Lo procesa**

Para comprender el **porqué** de esta acción basándonos en las explicaciones de la cátedra, analicemos qué representa esta dirección y cómo reacciona estructuralmente un router:

- **El tipo de dirección:** La dirección IP `255.255.255.255` es una dirección reservada que significa estrictamente **"difusión en esta red local"** (broadcast).
- **El comportamiento del router (El Procesamiento):** Como la interfaz del router pertenece y forma parte de ese mismo segmento de red o LAN, recibe el paquete de difusión al igual que el resto de los dispositivos conectados y obligatoriamente **lo procesa**. Procesarlo significa que el router lo desencapsula para evaluar si el paquete va dirigido a algún servicio que él mismo esté brindando. Un ejemplo clásico que menciona el profesor es cuando una PC recién encendida solicita una dirección IP; si el router funciona como servidor DHCP, procesará ese paquete de difusión para asignarle una IP.

**Por qué las demás opciones son incorrectas (incluyendo la nueva que agregaste):**

- **Lo descarta:** Esta fue una duda real planteada en la clase teórica. El router no descarta el paquete ciegamente ni de inmediato. Primero debe **procesarlo** (desencapsularlo) para averiguar si es una petición dirigida a sus propios servicios (como DHCP). El descarte definitivo solo ocurre como último recurso si, tras procesarlo, el router concluye que el mensaje no le incumbe.
- **Lo retransmite por todas sus interfaces, menos por la que ingresó:** Esta es la principal trampa arquitectónica. Los routers son dispositivos diseñados específicamente para **dividir y separar los dominios de broadcast**. Un router jamás retransmitirá un paquete de difusión hacia el otro lado de su interfaz, ya que si los routers hicieran esto a nivel global sería sumamente fácil causar tormentas de broadcast y tirar abajo toda la Internet. (La acción de retransmitir a ciegas por todos los puertos menos por el de ingreso pertenece a un dispositivo de Capa 1, como un Hub).
- **Se lo envía a todas las PCs de la LAN:** El router no es responsable de distribuir el paquete en la red local. Al ser un mensaje de difusión, el medio físico de la LAN ya se encargó de que la señal llegara a todas las máquinas de la celda.
- **Se lo envía al servidor de la LAN:** Arquitectónicamente falso. El router no tiene la función de redirigir a ciegas los mensajes de difusión local hacia servidores específicos; solo evalúa si el mensaje le sirve a él mismo.
- **Lo encapsula en una trama:** El proceso que realiza el router al recibir los bits desde el cable para poder leer que la IP de destino es 255.255.255.255 es exactamente el inverso: el **desencapsulamiento**. Solo encapsula cuando necesita enviar información hacia afuera.
### Rango de dirccion IP validas (NO RESERVADAS)
![[{FCC42A6B-322A-41A3-836D-D5326294773E}.png]]


En las siguientes hay temas de subredes pero me parece que van mejor aca por lso calculos de direct validas y se ven las reservadas tmb
#### ==18Dada la siguiente dirección de subred 189.45.8.0/25 determine cual de los siguientes es un rango de direcciones válidas:==
- [ ] 189.45.8.1-189.45.8.254
- [ ] 189.45.8.1-189.45.11.254
- [ ] 189.45.8.1-189.45.8.126
- [ ] 189.45.8.0-189.45.8.255
##### rta
189.45.8.1-189.45.8.126

justi:
1ero determinar que clase es 

189 a binario
```
	128   64  32 16 8 4 2 1
	  1    0
	   
1 0 -> CLASE B
```

clase b -> R.R.H.H el prefijo por defecto es /16 -> se pidieron prestados 25-16  ->9 bits

por lo que nos queda
R.R.R. 0 | 0000000   -> 189.48.9.0 RED

0 | 0000001  -> 1era direct valida  189.45.8.1

cantidad de host 2^7-2=126 direcciones validas

0 | 1111110 -> ultima direct valida 189.48.9.126

0 | 1111111 -> 189.48.9.127 BRODCAST



#### ==19Indique cuál es el rango de direcciones IPv4 válidas de la subred 170.62.32.0/22==
- [ ] 170.62.32.1 170.62.47.254
- [ ] 170.62.32.1 170.62.255.255
- [ ] 170.62.32.1 170.62.39.254
- [ ] 170.62.32.1 170.62.35.254
- [ ] 170.62.33.1 170.62.35.254
- [ ] 170.62.32.1 170.62.33.254
##### rta
170.62.32.1 170.62.35.254

1ero determinar la clase
```170 a binario

128 64 32
1    0


empieza con 10-> clase b
```

clase b -> R.R.H.H -> prefijo por defecto /16 -> se pidieron prestado 22-16=6 bits
* mas facil es hacer 32-22= 10 bits de host disponibles

para confirmar: R.R. 111111 | 00 . 00000000

170.62.32.0 -> direccion de red

001000 | 00 . 00000001 -> 1era ip valida 170.62.32.1

001000 | 11 . 11111110 -> ultima ip valida  170.62.35.254

001000 | 11 . 11111111 -> 170.62.35.255 BRODCAST




#### ==20Se necesita configurar 3 hosts con direcciones IPs que puedan ser enrutadas a través de INTERNET. ¿Cuales de las siguientes direcciones cumplen con lo solicitado? seleccione mas de una==
- [ ] 192.168.23.252
- [ ] 181.0.0.1
- [ ] 198.234.255.95
- [ ] 172.16.223.125
- [ ] 172.64.12.0
- [ ] 10.172.13.65
##### rta
- [ ] 181.0.0.1
- [ ] - [ ] 198.234.255.95
- [ ] - [ ] 172.64.12.0
- [ ] Comentarios
Direcciones IP públicas (enrutables por Internet)
### ==21¿Qué partes de la dirección IP utilizan los routers para enviar los paquetes a una subred? ⚠️
- [ ] La dirección IP completa
- [ ] Solo el NetID
- [ ] El hostID
- [x] El NetID más la subred
- [ ] La dirección lógica
#### rta
- [ ] El NetID más la subred

### ==22Determine cuál de las siguientes direcciones IP son públicas:==
- [x] 172.14.60.8
- [ ] 192.168.255.16
- [x] 11.10.10.16
- [ ] 10.28.5.10
- [ ] 172.28.56.90
- [x] 190.168.21.56
#### rta
- [ ] 172.14.60.8
- [ ] - [ ] 11.10.10.16
- [ ] - [ ] 190.168.21.56
### ==23Indique las direcciones enrutables en internet (públicas):==
- [ ] 172.45.100.5/16
- [ ] 127.0.0.3/8
- [ ] 11.45.3.10/8
- [ ] 201.34.13.5/24
- [ ] 200.25.30.0/24
- [ ] 192.168.1.15/24
- [ ] 191.45.45.255/24
#### rta
- [ ] 172.45.100.5/16
- [ ] 11.45.3.10/8
- [ ] 201.34.13.5/24
      
justificacion de alguinas
**200.25.30.0/24:** La "trampa" aquí radica en la porción de host. Aunque `200.x.x.x` es un rango público, al tener un prefijo `/24` sabemos que los últimos 8 bits representan al host. Al estar esos 8 bits completamente apagados en "0" (`.0`), esta es la **Dirección de Red**. Como analizamos anteriormente, las direcciones de red son reservadas y jamás se pueden asignar a un host para enrutar su tráfico
**191.45.45.255/24:** Esta es la trampa inversa a la anterior. En esta subred `/24`, el último byte (`255`) indica que los 8 bits de la porción de host están encendidos en "1". Estructuralmente, esto forma la **Dirección de Broadcast** (difusión) del segmento. Al igual que la dirección de red, es una dirección reservada para enviar mensajes a todos los equipos locales y no es enrutable como IP de origen o destino único en Internet.
### Direcciones privadas RFC

| Clase | Rango                     | Máscara | Cantidad de redes |     |
| ----- | ------------------------- | ------- | ----------------- | --- |
| A     | 10.0.0.0                  | /8      | 1                 |     |
| B     | 172.16.0.0– 172.31        | /16     | 16                |     |
| C     | 192.168.0.0 – 192.168.255 | /24     | 256               |     |
- **No son visibles desde Internet.**
- Necesitan **NAT** (traducción de direcciones) para acceder a Internet.
- Pueden repetirse en distintas organizaciones, pero **jamás duplicarse** dentro de una misma red.
#### ==24Determine cuáles de las siguientes direcciones IPv4 se podría utilizar para que una computadora tenga conectividad en internet (seleccione tres opciones)
- [x] 11.10.10.10 
- [ ] 10.10.12.14 
- [x] 194.168.10.6 
- [x] 172.32.60.90 
- [ ] 192.168.32.48 
- [ ] 172.26.56.0 
- [ ] 172.29.0.90
##### rta
Las respuestas correctas son:

- **11.10.10.10**
- **194.168.10.6**
- **172.32.60.90**

justif:
- **El Requisito (La Causa):** Para que una computadora tenga conectividad directa en Internet (es decir, que sea visible y enrutable a nivel global sin necesidad de traducción), requiere obligatoriamente tener configurada una **dirección IPv4 Pública**.
- **La Restricción (Las Direcciones Privadas):** Como efecto del agotamiento de las direcciones IPv4, la IETF estableció en la RFC 1918 rangos de direcciones "privadas". La regla estructural estricta dicta que estas direcciones **sólo pueden utilizarse dentro de una empresa u organización y no pueden ser visibles desde Internet**.

**Análisis de las opciones correctas (IPs Públicas):**

1. **11.10.10.10:** Es una dirección válida de **Clase A**. Su rango privado reservado abarca únicamente desde la 10.0.0.0 hasta la 10.255.255.255. Al empezar con el byte `11`, es una dirección de asignación pública.
2. **194.168.10.6:** Es una dirección válida de **Clase C**. El bloque privado reservado para la Clase C abarca exclusivamente desde la 192.168.0.0 hasta la 192.168.255.255. Como empieza con `194`, es una IP pública que navega por Internet.
3. **172.32.60.90:** Es una dirección válida de **Clase B**. Aquí suele haber confusión, pero el rango privado estricto de la Clase B va **solamente desde 172.16.0.0 hasta 172.31.255.255**. Como el segundo byte es `32` (fuera del límite del 31), se trata de una dirección IPv4 pública.

**Por qué las demás opciones son incorrectas (IPs Privadas):**

- **10.10.12.14:** Pertenece al rango privado de Clase A (10.x.x.x).
- **192.168.32.48:** Pertenece al rango privado de Clase C (192.168.x.x).
- **172.26.56.0** y **172.29.0.90:** Ambas pertenecen al rango privado de Clase B, ya que sus segundos bytes (`26` y `29`) caen dentro del bloque reservado de 16 a 31. Además, la primera (`.0`) probablemente actuaría como dirección de red dependiendo de su máscara, lo cual la hace inasignable a un host. Ninguna de estas puede rutearse directamente en Internet.
#### ==25¿Cuál es el rango de direcciones privadas definidas en el RFC 1918? Seleccione una o más de una:==
- [ ] 172.16.0.0 hasta 172.16.255.255
- [ ] 127.0.0.0. hasta 127.255.255.255
- [ ] 0.0.0.0 hasta 255.255.255
- [x] 172.16.0.0 hasta 172.31.255.255
- [x] 192.168.0.0 hasta 192.168.255.255
- [x] 10.0.0.0 hasta 10.255.255.255
- [ ] 224.0.0.0 hasta 239.255.255.255
##### rta
10.0.0.0 hasta 10.255.255.255 -> Clase A
172.16.0.0 hasta 172.31.255.255 -> Clase B
192.168.0.0 hasta 192.168.255.255 -> Clase C



#### ==26Cuál de las siguientes afirmaciones es correcta sobre el direccionamiento IPv4==
- [ ] Se definieron 10 redes clase A para direccionamiento privado
- [ ] Se definieron 16 redes clase B para direccionamiento público
- [ ] Se definio una única dirección de red clase A para direccionamiento público
- [ ] Se definieron 255 redes clase B para direccionamiento privado
- [x] Se definieron 256 redes clase C para direccionamiento privado
##### rta
se definieron 256 redes clase C para direccionamiento privado

En IPv4, las direcciones privadas están definidas por rangos reservados que no se enrutan
en Internet. 

Para la clase C, el rango reservado para uso privado es:
192.168.0.0 a 192.168.255.255 → lo que equivale a 256 redes clase C

Para la clase A es una direct privada la 10
Para la clase B son 16 direct privadas




#### ==27Determine cuales de las siguientes direcciones IPv4 son privadas (seleccione 3):==
- [x] 172.28.10.9
- [ ] 172.33.60.95
- [x] 192.168.150.78
- [ ] 194.168.50.18
- [x] 10.20.10.18
- [ ] 14.40.60.5
##### rta
172.28.10.9
192.168.150.78
10.20.10.18

#### 28Cuál de las siguientes direcciones IP es una dirección privada? (invetnada por ia)
- [x] 192.168.1.1
- [ ] 8.8.8.8
- [ ] 172.32.0.1
- [ ] 1.1.1.1
##### rta
- [ ] 192.168.1.1

## Sistema binario
## Subredes (Subnetting)
Los routers dividen los dominios de broadcast. Inicialmente, toda la red funciona como un solo
dominio broadcast, 
Entonces: consiste en dividir una gran red *(o un gran dominio de broadcast),* en grupos  más pequeños  (*en áreas lógicas más pequeñas y jerárquicas.*)

### Caracteristicas ❌
1. Jerarquicas
    1. Introducen un nivel adicional de jerarquía en las direcciones IP, más allá de las partes Host y Red.
2. Las Asigna el Administrador de Red:
    1. Creadas por el administrador de red a partir de la dirección de red proporcionada por el proveedor.
    2. Conocido como plan o esquema de direccionamiento IP.
3. Visibilidad Interna:
    1. Solo son visibles dentro de la organización; desde fuera, solo se ve la red completa.
4. Modificación de Máscaras de Subred:
    1. Se ajustan las máscaras de subred para definir y delimitar las subredes.

Ventajas:

1. Control del Tráfico entre Áreas de la Empresa:
    1. Permite dividir el direccionamiento según áreas de la empresa para controlar el tráfico y mejorar la seguridad.
    2. Evita la necesidad de más routers, lo que sería más costoso.
2. Reducción de Dominios de Broadcast:
    1. Evita un único dominio de broadcast grande para toda la red.
    2. Se crean varios dominios más pequeños, uno por cada subred.
3. Facilita Implementación de Seguridad:
    1. Posibilita la configuración de listas de control de accesos (ACL) para cada subred, mejorando la seguridad

### Calculo de subredes
Se "piden bits prestados" de la porción de host para agregarlos a la porción de subred:
- Más subredes → menos hosts por subred.
- Siempre deben quedar **mínimo 2 bits para host** (para tener al menos 2 IPs válidas).


$$\text{Cantidad de subredes} = 2^n \quad (n = \text{bits prestados})$$

$$\text{Hosts válidos por subred} = 2^h - 2 \quad (h = \text{bits que quedan para host})$$

$$\text{Bits prestados} = \text{Máscara aplicada} - \text{Máscara natural de la clase}$$


Ejemplo de Clase C - utilizando el último byte.
![{1B1F98B6-1B85-423B-9A37-931C08410AFE}.png|338](1B1F98B6-1B85-423B-9A37-931C08410AFE.png)
![[Pasted image 20260528215645.png|365]]
En el ejemplo de una red de Clase C, al utilizar el último byte, se puede asignar hasta 6 bits para subredes. Para no comprometer la parte de host, siempre deben quedar al menos 2 bits. Se pueden pedir prestados hasta 6 bits en una red de Clase C, garantizando un mínimo de 2 host. 

No puede haber una subred con solo 1 bit para la parte de host, ya que se reservan para el broadcast y la dirección de subred, dejando sin posibilidad de hosts. Si se utilizan 6 bits prestados, quedan 2 hosts, lo que se utiliza comúnmente en redes punto a punto para la interconexión de routers

el prefijo va cambiando por cuantos se prestan por ejemplo: el por defecto de un clase c es /24 + la cant de bits tomados prestado de host. El maximo sera /30

#### ==29Por ejemplo: Dada la red 195.34.20.0/24 (Clase C). Se deciden crear 12 subredes.==
**Red Base:** `195.34.20.0/24` (tienes 8 bits para hosts).
**Subredes requeridas:** 12.
¿Cuántos bits hay que pedir? 4 (2^4=16 subredes)
**Bits de host restantes (h):** 8 totales - 4 prestados = 4 bits.
¿Cuántas direcciones IP válidas se dispondrá en cada una de las subredes? 14 (2^4 – 2 = 14)
¿Cuántas direcciones IP se pierden en total? 16 subredes×2 perdidas por subred=32 IPs perdidas.

¿Cuántas direcciones IP válidas se dispondrá en total en la organización? 16 subredes×14 vaˊlidas por subred=224 IPs uˊtiles en total.

#### --
#### ==30Teniendo la estructura N.N.H.H y necesito crear subredes, minimizando la cantidad de subredes. ¿De donde se piden prestados los bits? Seleccione una:
- [ ] Del segundo octeto y de derecha a izquierda
- [ ] Del segundo octeto y de izquierda a derecha
- [x] Del tercer octeto y de izquierda a derecha
- [ ] Del tercer octeto y de derecha a izquierda
- [ ] Del último octeto de izquierda a derecha
- [ ] Del último octeto de derecha a izquierda
##### rta
Del tercer octeto y de izquierda a derecha

#### ==31La cantidad máxima de bits que se pueden pedir prestados para crear subredes en una dirección IP clase A es:
- [x] 22
- [ ] 14
- [ ] 6
##### rta
22

justif
R.H.H.H  -> 8+8+8=24 y le restas 2 por que tenes que dejar 2 bits para asignar host

####  ==32La cantidad máxima de bits que se pueden pedir prestados para crear sub-redes en una dirección IP clase B es:==
- [ ] 16 bits
- [ ] 7 bits
- [ ] 13 bits
- [x] 14 bits
- [ ] 5 bits
- [ ] 6 bits
##### rta
14

justif
R.R.H.H  -> 8+8=16 y le restas 2 por que tenes que dejar 2 bits para asignar host

#### ==33El ISP le asigna a una empresa la IP 190.45.96.0/22 ello implica que se dispone de:
- [ ] 1024 direcciones de host válidas
- [ ] 510 direcciones de hosts válidas
- [ ] 2048 direcciones de hosts válidas
- [ ] 4094 direcciones de hosts válidas
- [ ] 2046 direcciones de hosts válidas
- [ ] 1022 direcciones de hosts válidas
###### rta
1022 direcciones de hosts válidas

Resolucion:
1. **Bits disponibles para hosts:** Las direcciones IPv4 están formadas por un total de 32 bits. El prefijo `/22` indica que los primeros 22 bits están fijos para identificar la red. Por lo tanto, el efecto directo es que quedan **10 bits restantes** destinados exclusivamente a la porción de host (32−22=10)
2. **Cálculo total:** Con 10 bits disponibles, la cantidad de combinaciones matemáticas posibles es de 2^{10}, lo que da un total de 1024 direcciones
3. **Descuento de direcciones reservadas:** Para obtener el número de direcciones "válidas" (es decir, las que se pueden asignar a dispositivos o interfaces reales), la regla exige utilizar la fórmula 2^n−2. Esto causa que al total de 1024 se le deban restar ineludiblemente 2 direcciones, dando como resultado final **1022**
4. **Causalidad de la resta:** ¿Por qué se restan exactamente dos direcciones? Se debe a que la primera combinación (cuando todos los bits de la porción de host valen `0`) es una dirección reservada que identifica a la propia **dirección de red**. Paralelamente, la última combinación posible (cuando todos los bits de host se encienden en `1`) queda reservada para la **dirección de broadcast** o difusión. Ninguna de estas dos puede asignarse a un equipo.

#### ==34Una empresa decide implementar un esquema de direccionamiento IP utilizando subredes. El administrador decide utilizar la IP 160.4.0.0/23. Ello implica:==
- [ ] Se pierden 64 direcciones IP del total del espacio de direccionamiento
- [ ] Se pierden 128 direcciones IP del total del espacio de direccionamiento
- [ ] Se pierden 256 direcciones IP del total del espacio de direccionamiento
- [ ] Se pierden 510 direcciones IP del total del espacio de direccionamiento
- [ ] Se pierden 512 direcciones IP del total del espacio de direccionamiento
- [ ] Se ganan 510 direcciones IP del total del espacio de direccionamiento
- [ ] Se ganan 256 direcciones IP del total del espacio de direccionamiento
##### rta

La respuesta correcta es:

- [ ] **Se pierden 256 direcciones IP del total del espacio de direccionamiento**

Para comprender el **porqué** de este resultado basándonos en la arquitectura de redes y mantener nuestro análisis de causa y efecto, analicemos matemáticamente cómo impacta la creación de subredes:

- **1. La causa (Identificación de la red base y la máscara):** La dirección asignada empieza con el byte **160**. Como este valor cae en el rango de 128 a 191, deducimos inmediatamente que es una dirección de **Clase B**. Las redes de Clase B utilizan por defecto una máscara `/16`.
- **2. El efecto en los bits (El préstamo):** El administrador decide aplicar una máscara `/23`. El efecto directo de alargar la máscara originaria de `/16` a `/23` es que el administrador le está pidiendo prestados exactamente **7 bits** a la porción de host para poder crear las subredes ($23 - 16 = 7$).
- **3. El cálculo de subredes:** Al utilizar estos 7 bits prestados, la cantidad de celdas o subredes que se van a generar es de $2^7$, lo que nos da un total de **128 subredes**.
- **4. El efecto final (La pérdida de IP):** La regla estructural ineludible del direccionamiento dicta que **por cada subred creada, siempre se pierden 2 direcciones IP útiles**: la primera (porque identifica la dirección de subred en sí) y la última (porque es la dirección reservada para el broadcast).

Por lo tanto, para saber el total de direcciones IP que se desaprovechan o pierden del espacio general, debemos multiplicar la cantidad de subredes creadas por las 2 IP que se pierden en cada una: **$128 \text{ subredes} \times 2 = 256 \text{ direcciones IP perdidas}$**.

**Por qué las demás opciones son incorrectas:**

- **Nunca se "ganan" direcciones IP:** Al implementar un esquema de subredes, el efecto es dividir los dominios de broadcast para un mejor rendimiento y seguridad, pero el costo arquitectónico ineludible es que **siempre se pierden direcciones IP** (nunca se ganan) debido a la reserva obligatoria de red y broadcast en cada nueva partición.
- Los valores de **64, 128, 510 o 512** son resultados matemáticos incorrectos para este escenario específico, ya que no reflejan la multiplicación de las 128 subredes por las 2 IP que se consumen en cada una de ellas.




#### ==35Cuáles de las siguientes direcciones IP podrá utilizar un administrador de red, si desea implementar un esquema de direccionamiento IP con 20 subredes, maximizando la cantidad de hosts por subred (seleccione dos)==
- [ ] 100.0.0.0/14 
- [ ] 98.0.0.0/15 
- [ ] 189.85.0.0/23 
- [ ] 140.56.0.0/22 
- [ ] 190.60.0.0/21 
- [ ] 199.60.5.0/29
##### rta
Las respuestas correctas son:

- [x] **190.60.0.0/21**
- [x] **199.60.5.0/29**

Para comprender el **porqué** de este resultado basándonos en la arquitectura de redes, desglosemos los requisitos planteados mediante la relación de causa y efecto:

- **1. La causa (El requisito de las 20 subredes):** El administrador necesita implementar un esquema que soporte exactamente 20 subredes. Para saber cuántos bits de la porción de host se deben pedir prestados ineludiblemente, utilizamos la regla de potencias base 2 ($2^n$):
    - Si pide 4 bits: $2^4 = 16$ subredes (No alcanza).
    - Si pide 5 bits: $2^5 = 32$ subredes (Alcanza y cumple el requisito).
- **2. El factor limitante (Maximizar hosts):** El enunciado exige **"maximizando la cantidad de hosts por subred"**. El efecto directo de esta condición es que el administrador **debe pedir prestados exactamente 5 bits y ni uno más**. Si pidiera 6 o 7 bits, tendría más subredes (64 o 128), pero le quedarían menos bits libres para direccionar los hosts, incumpliendo la regla de maximizarlos.

Sabiendo que estructuralmente la nueva máscara debe tener **exactamente 5 bits más** que la máscara por defecto de la red, analizamos las opciones:

- **190.60.0.0/21:** El primer byte es 190, lo que indica que es una dirección comercial de **Clase B**. Su máscara por defecto originaria es `/16`. Al aplicar una máscara `/21`, el administrador pidió exactamente **5 bits prestados** ($21 - 16 = 5$). Esto satisface los requisitos, generando 32 subredes y maximizando el espacio restante (11 bits) para los hosts.
- **199.60.5.0/29:** El primer byte es 199, perteneciente a la **Clase C**. Su máscara por defecto originaria es `/24`. Al aplicar la máscara `/29`, el administrador también pidió exactamente **5 bits prestados** ($29 - 24 = 5$). Nuevamente, se generan 32 subredes y se reserva el resto (3 bits) para maximizar la capacidad de hosts de esa celda.

**Por qué las demás opciones son incorrectas:**

- `100.0.0.0/14` y `98.0.0.0/15`: Ambas son de Clase A (máscara por defecto `/8`). Al tener `/14` y `/15`, significa que pidieron 6 y 7 bits prestados respectivamente. Esto crea 64 y 128 subredes, reduciendo innecesariamente el espacio para hosts.
- `140.56.0.0/22` y `189.85.0.0/23`: Ambas son de Clase B (máscara por defecto `/16`). Al tener `/22` y `/23`, pidieron 6 y 7 bits prestados. Nuevamente, superan el requisito mínimo de 5 bits, por lo que no maximizan la porción de host.

### ==36¿Cuántas subredes pueden crearse si se solicitan 5 bits al HostID?==
- [ ] 16 
- [ ] 18 
- [ ] 8 
- [ ] 14 
- [x] 32
#### rta
2^5=32
###  Mascara de subred 
![{BD421C40-B52C-42CB-A238-5BCA9E2B43B9}.png|382](BD421C40-B52C-42CB-A238-5BCA9E2B43B9.png)
- **Todos los dispositivos** de la organización comparten la **misma máscara de subred**.
- La máscara permite identificar a qué subred pertenece un dispositivo.
- Sin conocer la máscara, es **imposible** definir si una IP es de red, broadcast o host válido.

Entonces para saber cuántos bits se pidieron prestados, necesito saber la máscara de subred y la clase de red. Si solamente conocemos uno (o la máscara, o la clase de red), no podemos saber cuántos bits se pidieron prestados para la subred

Por ejemplo si pedimos dos bits:

![{AC5B060E-BBBD-4EF9-BE60-3F42030B0ACD}.png](AC5B060E-BBBD-4EF9-BE60-3F42030B0ACD.png)
- Análisis de cómo se altera la máscara de red por defecto (de /24 → clase C) al sumarle los bits prestados (ej. pasando a /26).
    - porque 26-24=2 → que es la cantidad de bits prestado,
### Operación AND (Encontrar la Subred de una IP)

$$\text{Dirección de Subred} = \text{IP} \; \text{AND} \; \text{Máscara}$$

- Se compara bit a bit: `1 AND 1 = 1`, `0 AND X = 0`.
- En la porción de red/subred (donde la máscara tiene 1s), se copian los bits de la IP.
- En la porción de host (donde la máscara tiene 0s), todos los bits quedan en 0.
###  Conclusiones sobre subredes
• Todas las máquinas de un área deben pertenecer a la misma subred.
• Las máquinas en una subred comparten la misma máscara de subred y el mismo GW.
• Configurar el GW es esencial para la conectividad fuera de la LAN.
### OBTENER LA SUBRED A PARTIR DE UNA IP
IGUAL QUE PARA LAS REDES

Para obtener la subred a partir de una dirección IP, se sigue un proceso en tres pasos: escribir la dirección IP y la máscara en formato booleano, considerando la clase y los bits prestados en el prefijo, y realizar una operación AND booleana. Este método es similar al utilizado para redes, pero la máscara tiene más bits activados. 

Al analizar una dirección IP, como por ejemplo 200.4.6.80:

1. ==Para determinar si es una dirección de host válida, se necesita la máscara. En subredes, la dirección IP y la máscara son inseparables.
2. Para identificar si es una dirección de subred, se examina el último byte después de aplicar la máscara.
Ejemplos:
    1. ==Con una máscara /26, el último byte con dos bits prestados sería 0 1 | 0 1 0 0 0 0, siendo una dirección de host válida.==
    2. Con una máscara ==/28==, el último byte con cuatro bits prestados sería 0 1 0 1 | 0 0 0 0, indicando una ==dirección de subred debido a que todos los bits del host son 0==. Si todos fueran ==1, también sería una dirección de subred o de broadcast==

#### ==37 Si se realiza un AND booleano entre una dirección IPv4 de una PC y una máscara de subred, se obtiene como resultado:
- [ ] La dirección del gateway y por defecto de la PC
- [ ] La máscara de subred
- [ ] La máscara de red
- [ ] La dirección MAC de la PC
- [ ] La clase a la cual pertenece la dirección IP
- [x] La dirección de la subred a la cual pertenece la PC
##### rta
La dirección de la subred a la cual pertenece la PC

### CHEQUEAR:
- Todas las máquinas de un área deben pertenecer a la **misma subred**.
- Comparten la **misma máscara** y el **mismo Gateway**.
- Sin Gateway configurado → solo hay conectividad local.
- El **router no necesita Gateway** (su función nativa ya es enrutar).
- La primera IP válida del rango suele asignarse al **Gateway** (convención).
- Una IP de la subred que se asigne al Gateway **resta 1 host** disponible.
## Direccionamiento IPv4-VLANS
### Concepto Vlan
Las VLANs (Virtual Local Area Network) permiten crear redes lógicas separadas sobre una misma red física.

* beneficio
	* Son adaptables a cambios en la organización.
* req tecnico
	* Requieren especificar la cantidad de VLANs, sus nombres y asignación de dispositivos.


#### ==38Cuáles de las siguientes características corresponden a la VLANs (seleccione tres opciones)==
- [ ] Se implementan mediante hubs configurables
- [x] Se implementan mediante configuración en los switches
- [ ] Todas las VLANs deben pertenecer a la misma subred
- [ ] Los empleados pertenecientes a una VLAN deben estar conectados a un mismo switch
- [x] Facilitan la implementación de seguridad en la empresa
- [x] Agrupan empleados lógicamente independientemente de cuál sea su ubicación física 
- [ ] se implementan mediante el protocolo IEEE 802.1d
##### rta
* beneficio
	* Facilitan la implementación de seguridad en la empres
	* Agrupan empleados lógicamente independientemente de cuál sea su ubicación física

* req tecincco
	* Se implementan mediante configuración en los switches

#### ==39 Cuáles de las siguientes características corresponden a la VLANs (seleccione tres opciones)==
- [ ] Se agrega una etiqueta en el paquete IPv6 en los enlaces troncales
- [x] Si se definen 5 VLANs, se con�gurarán 5 subredes diferentes
- [x] Cada VLAN es un dominio de broadcast
- [ ] Los switches se coneectan entre sí, a través de enlaces de acceso
- [ ] Se implementan en las NIC de las computadoras
- [x] Se implementan mediante el protocolop 802.1q
- [ ] Los usuarios pertenecientes a una VLAN deben estar conectados al mismo switch
##### rta
* beneficio:
	* Cada VLAN es un dominio de broadcast
* requerimientos tecnicos:
	* Si se definen 5 VLANs, se configurarán 5 subredes diferentes
	* Se implementan mediante el protocolop 802.1q
### Implementacion de las VLANS
![[Pasted image 20260530184042.png|338]]
* Enlaces de acceso: donde se conectan los dispositivos finales (PC, servidores, impresoras).
* Enlaces troncales: enlaces de conexión entre switches o dispositivos de interconexión (router, hub)
#### ==40 Indique cuántos dominios de broadcast existen en la figura. ==
![[{A258FBF9-BDB5-44F4-89C9-4E1EB21783BD}.png]]
##### rta
Hay 3 dominios de broadcast en la imagen porque hay 3 VLANs distintas, y cada VLAN es
un dominio de broadcast separado, incluso si comparten el mismo switch físico. Los
paquetes broadcast enviados por una PC en la VLAN 10 no llegan a las PC de la VLAN 20
ni a las de la VLAN 30.
####  Protocolo IEE 802.1q
![[{603578FB-A4B8-42FE-AEBA-1AB8A4F05F55}.png]]
>[!question] COMO distinguen el switch entre tramas pertenecientes a diferntes VLANS en los enlaces troncales?
>
>cuando la red tiene múltiples switches interconectados, sus uniones se denominan **[Enlace Troncal]**. Por estos enlaces viaja el tráfico mezclado de todas las áreas
>
>Para que los switches puedan distinguir las tramas de diferentes VLANs, se desarrolló el protocolo [[IEEE 802.1q]].
>
>Una PC envía una trama común, el switch identifica a qué VLAN pertenece el puerto por el que ingresó la trama, le agrega la etiqueta de esa VLAN. Viaja la trama modificada por los enlaces troncales. Cuando llega al switch al que se encuentra conectada la PC destino, elimina la etiqueta y entrega la trama común. Las PC no entienden el protocolo IEEE 802.1q.
##### 41¿Qué protocolo permite implementar VLANs en switches administrables?  (inventada por IA)
- [ ] IEEE 802.11
- [ ] IEEE 802.3
- [x] IEEE 802.1Q
- [ ] IEEE 802.15
###### rta
IEEE 802.1Q

Este protocolo marca las tramas Ethernet con un “tag” que dice a qué VLAN pertenece.
Así, el switch sabe a cuál VLAN debe mandar cada trama

##### 42Bits usados en ID de VLAN (IEEE 802.1Q): (inventada por ia)
- [ ] 12
- [ ] 8
- [ ] 16
- [ ] 10
###### rta
12
##### 43 Máximo de VLANs en 802.1Q: (inventada por IA)
- [x] 4096
- [ ] 255
- [ ] 1024
- [ ] 65535
###### rta
4096
### Tipos de vlans

#### ==44 En la creación de VLAN estática: Seleccione una:==
- [ ] A medida que las estaciones de trabajo se conectan a los puertos del Switch, éste les va a asignando una de las VLAN que tiene disponible
- [x] Un administrador debe crear la VLAN en el switch y luego agregar los puertos a ella
- [ ] De acuerdo al protocolo del tráfico que envía el host, es la VLAN a la que va a pertenecer el puerto del switch
- [ ] El Switch Raiz le indica a los otros a qué VLAN pertenecen
- [ ] De acuerdo al tipo de host (PC, teléfono IP, TV, tablet, etc) será la VLAN a la que pertenezcan
##### rta
Un administrador debe crear la VLAN en el switch y luego agregar los puertos a ella

justif:
Son **basadas en el puerto**. El administrador configura manualmente en el **[Switch]** qué bocas físicas pertenecen a qué red (ej. del puerto 1 al 8 son VLAN 10). 

Cuando se conecta un dispositivo, automáticamente asume su pertenencia a la VLAN a la que se asignó el puerto


Son las más utilizadas por ser sencillas, pero son rígidas: si un usuario cambia su PC de boca sin avisar, pierde conectividad al quedar en una **[Subred]** incorrecta.
#### ==45 Una empresa posee un switch al cual están conectadas 20 computadoras. El administrador saca el cable del puerto 4 del switch y lo coloca en el puerto 18. A continuación, recibe la queja del empleado, informando que no tiene conectividad. ¿Cuál de las siguientes opciones podría ser la causa del problema?==
- [ ] El administrador configuró VLANS dinámicas
- [ ] La computadora debería haber actualizado su dirección MAC
- [ ] La computadora debería haber actualizado el navegador
- [ ] La computadora debería implementar el protocolo 802.1d
- [x] El switch tiene implementado VLANs basadas en el puerto
- [ ] Las velocidades del puerto del switch y de la NIC son diferentes
##### rta
El switch tiene implementado VLANs basadas en el puerto
#### VLAN DINAMICA
Son automáticas y flexibles. 

La asignación de VLANs se realiza a través de un servidor VMPS (VLAN Management Policy Server) que
permite al administrador de red asignar puertos de manera automática basándose en la dirección MAC del dispositivo
o el nombre de usuario utilizado para acceder. 

Cuando un dispositivo se conecta, se consulta la base de datos de miembros de la VLAN para determinar su asignación.

En este enfoque, los puertos no están vinculados a una VLAN específica; Esto brinda flexibilidad, permitiendo
que los dispositivos se muevan entre switches y aun así permanezcan en la misma VLAN.

Esta técnica se utiliza comúnmente en empresas grandes y ofrece la capacidad de crear VLANs basadas en
el usuario o en la dirección MAC del dispositivo

#### 46 VLAN dinámica se distingue por: (inventada por IA)
- [ ] No requiere configuración
- [x] Servidor VMPS
- [ ] Es más lenta
- [ ] Es para WiFi
##### rta
- [ ] Servidor VMPS
## Agotamiento de direcciones IPv4
### Causas ❌
* El crecimiento exponencial de Internet, (causa principal)
- Gran cantidad de “dispositivos” que requieren una dirección IP
- las conexiones de banda ancha "siempre activas" y la proliferación masiva de dispositivos por usuario.
- **El Error Estructural ([Classful]):** El diseño original asignaba direcciones en bloques enteros de clase (A, B o C). Este método no utiliza eficazmente las direcciones disponibles y ha llevado a la necesidad de IPv6 para abordar la creciente demanda de direcciones IP.
> [!danger] El Derroche del Modelo Classful El profesor recalcó por qué este modelo falló matemáticamente: si una empresa necesitaba 500 direcciones, una red de Clase C (254 IPs) no era suficiente. Como solución, se le entregaba una Clase B entera (2^16−2=65.534 IPs). Esto generaba un **derroche irrecuperable** de más de 65.000 direcciones públicas por empresa

### Soluciones de agotamiento
#### Direccionamiento privado
#### Traducion de direcciones de red privadas (NAT) ❌
* lo gestiona el rute

##### que hace nat? (inventada por IA)
- [ ] Traduce IP privada a pública
- [ ] Asigna MAC
- [ ] Cifra datos
- [ ] Evita colisiones
###### rta
- [ ] Traduce IP privada a pública

#### CIDR ❌
Es una metodología que elimina el concepto de clases de direcciones IP y asignar redes enteras  y se enfoca en asignar direcciones en función de la cantidad de hosts necesarios y la ubicación geográfica.

Sus objetivos son:
* Distribuir direcciones IPv4 públicas no asignadas geográficamente
	* CIDR agrupa las IP por continentes. Esto permite que los routers lean menos bits (ej. los primeros 8 bits) para saber que el paquete va a Sudamérica, agilizando drásticamente el procesamiento
* Mejorar el enrutamiento al reducir el tamaño de las tablas en los routers y acelerar el procesamiento de paquetes
* Asignar direcciones en bloques de tamaño variable, eliminando la asignación por "clase"
* Basarse en la cantidad necesaria de direcciones válidas.
* Permitir la implementación de resumen de rutas ([[Sumarización de Rutas]]]), similar a IPv6
![[Pasted image 20260530190718.png|481]]![[Pasted image 20260530190728.png|490]]
##### 47 CIDR se caracteriza por (inventada por IA)
- [x] Eliminar clases de IP
- [ ] Usar clase C
- [ ] Fijar tamaño de red
- [ ] Funcionar con IPv6
###### rta
- [ ] Eliminar clases de IP

#### Sumarizacion o Resumen de rutas

| Tecnología                         | Modificación de la [Máscara de Subred]          | Efecto en la Tabla del Router                             |
| ---------------------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| **Subnetting**                     | Se desplaza hacia la **derecha** (se alarga).   | Aumenta la cantidad de renglones (rutas específicas).     |
| **Supernetting**<br>(sumarizacion) | Se desplaza hacia la **izquierda** (se acorta). | Reduce los renglones (resume múltiples rutas en una sola) |
El administrador de red configura el router para la Sumarización de rutas, donde una dirección de resumen cubre múltiples direcciones IP al identificar bits coincidentes. Esto simplifica el enrutamiento, por ejemplo, la dirección 201.3.32.0/20 abarca todas las IP con los primeros 20 bits iguales.

> [!note] El Algoritmo de Cálculo (Corte de Bits) El objetivo es encontrar una única **[Dirección IP]** que abarque múltiples redes.
> 1.Se identifican las direcciones a resumir y se ubica el octeto "conflictivo" (el que cambia).
> 2. Se pasan a binario y se comparan bit a bit de izquierda a derecha.
> 3.Se realiza el "corte" exactamente en el punto donde los bits dejan de coincidir.
> 4.Los bits coincidentes se copian tal cual , mientras que todos los bits a la derecha del corte se ponen en cero.
> 	ESTO LO PASAMOS A DECIMAL Y TENEMOS LA IP DE RED
> 5.Para el prefijo Se suman los bits coincidentes totales
> 
> Un router debe publicar ("enseñar") las redes que conoce al siguiente router
> 
> ![[{B834C59C-50E2-448D-9898-683DCA235899}.png]]

##### ==48A un administrador de red le propusieron que configurara sumarización de rutas en el router. ¿Qué benefcios tiene?==
- [ ] Se configuran automáticamente en el router
- [x] Reduce el tamaño de las tablas de encaminamiento
- [ ] No necesita crear rutas estáticas
- [ ] Tiene más opciones el router de elegir rutas

###### rta
Reduce el tamaño de las tablas de encaminamiento
##### ==49 A partir de las siguientes direcciones IP:  200.15.43.0/24, 200.15.50.0/24, 200.15.39.0/24, indique cuál es la superred (resumen de rutas) correcta que debería publicar un ISP:==
- [ ] 200.15.32.0/18
- [ ] 200.15.32.0/20
- [ ] 200.15.48.0/20
- [ ] 200.15.32.0/19
- [ ] 200.15.48.0/19
- [ ] 200.15.38.0/19

###### rta
- [ ] 200.15.32.0/19

1ero identificar el octeto conflictivo; en este caso es el 3ero

pasamos a binario el octeto conflictivo

```
200.15.43.0 
43 a binario -> 128 64 32 16 8 4 2 1
                  0  0  1  0 1 0 1 1

200.15.50.0 
50 a binario -> 128 64 32 16 8 4 2 1
                  0  0  1  1 0 0 1 0

200.15.39.0 

39 a binario -> 128 64 32 16 8 4 2 1
                  0  0  1  0 0 1 1 1
                  
```

 3er paso corte 
 ```
 
                   0  0  1 | 0 1 0 1 1
				   0  0  1 | 1 0 0 1 0
                   0  0  1 | 0 0 1 1 1
                   -------------------
                   0  0  1 | 0 0 0 0 0
                   
                   
 ```

4 paso pasamos el 3er octeto a decimal
```
	128 64 32 16 8 4 2 1
	 0  0  1 | 0 0 0 0 0    => 32
```

5to sumamos los bit coincidentes totales para la nueva mascara
8+8+3= /19

quedandonos  200.15.32.0/19
##### ==50 A partir de las siguientes direcciones IP 200.15.54.0/24, 200.15.55.0/24, 200.15.60.0/24 indique cual es la superred (ruta resumen):
- [ ] 200.15.48.0/20
- [ ] 200.15.32.0/19
- [ ] 200.15.48.0/21
- [ ] 200.15.32.0/18
- [ ] 200.15.48.0/19
- [ ] 200.15.32.0/20

###### rta
- [ ] 200.15.48.0/20

#### VLSM (Mascaras de subre de longitud variable) 
La solución definitiva es **[[VLSM]]** (Máscara de Subred de Longitud Variable)(Variable Length Subnet Masking), es una técnica que permite "crear subredes dentro de subredes" lo que agrega un nivel adicional de jerarquía.  

Usa máscaras largas (mascaras con muchos bits) (ej. `/30`) para direccionar pocos hosts, y máscaras cortas para direccionar muchos host, optimizando al máximo las IPs públicas.

> VLSM se usa con **IPs públicas**. Con IPs privadas no hay restricción de espacio.

#### ==51Para la sigueiten topologia de red, determine las mascaras que podrian usarse para sastifacer los requisitos de direcciones de host en cada subred==
el orden: Enlaces wan, cordoba, rio cuarto, villa maria
![[{079B4267-1F54-4974-B35D-9D9CE9FC586A}.png]]
- [ ] /30 , /25 , /26 , /27
- [ ] /24, /25 , /26 , /27
- [ ] /24 , /25 , /26 , /23
##### rta
1ero vemos que es una clase C  , en binario arranca 110

* la mascara por defecto es /24 
	* para cordoba 2^7-2=126 host  ; 1 bit movemos a la derecha  /25
	* para rio cuarto 2^6-2=62 host ; 2 bit nos movemos a la derecha /26
	* para villa maria 2^5-2=30 host ; 3 bit nos movemos a la derecha /27
	* Enlaces WAN: /30 (permite 2 hosts útiles) 
		* --- ¿Qué es un enlace WAN?
			* Es una conexión punto a punto entre dos routers, por ejemplo: Río Cuarto ↔ Córdoba, Río Cuarto ↔ Villa María En este tipo de enlaces solo hay 2 dispositivos que necesitan dirección IP: cada uno de los dos routers

##### EJEMPLO
![[Pasted image 20260530202034.png|370]]

>[!question] **Pregunta en clase: Limitación Topológica** El profesor interpeló: _"¿Se puede resolver este caso con subredes clásicas?"_. 
>- **Alumno:** Intentó dejar 6 bits para host (permitiendo 62 máquinas, lo que cubre el área de 50). Pero notó que esto solo dejaba 2 bits para red, permitiendo crear apenas 2^2=4 subredes, cuando el ejercicio pide 6.
> - **Respuesta del Profesor:** Validó que **no tiene solución** con el _subnetting_ tradicional. Como la máscara clásica es fija, todas las subredes quedan del mismo tamaño. Esto genera que en el enlace donde solo hay 2 hosts, estemos derrochando 60 IPs públicas, lo cual es inaceptable.
>   Por ende, es obligatorio usar **[[VLSM]]






######  PROCEDIMIENTO DE CALCULO VLSM
>[!tip] **Regla de Oro (Metodología de Cálculo)** El profesor fue tajante con el primer paso del algoritmo: Para que **[[VLSM]]** funcione, **siempre se deben ordenar los requerimientos de mayor a menor** cantidad de **[Host]** antes de empezar a subdividir


1. Primero se determinan los requerimientos de direccionamiento, considerando la cantidad de dispositivos y las IPs necesarias para cada área de la empresa, organizándolos de mayor a menor importancia
	1. ![[{507D17A5-2BFC-4B34-903F-A174C43E2812}.png|229]]
2. Luego, se calcula el espacio total de direccionamiento, en este caso, se utilizan 8 bits para las IPs, lo que da 254 direcciones
3. A continuación, se determina la cantidad de bits para hosts y se asigna el espacio restante a subredes. En este ejemplo (de 50 hosts), quedan 2 bits para subredes, lo que permite crear 2^2=4 subredes con capacidad para 2^6-2=62 hosts cada una
4. Luego, se analiza cada área o departamento con sus requerimientos de hosts y se elige la subred adecuada. Se divide esta subred en subredes más pequeñas según sea necesario.![[{2DD10B2A-0F5F-4591-8756-366BBE94FADD}.png|475]]
>[!note] La máscara /30 es la más grande que podemos tener, ya que la máscara /31 no nos permite direccionar hosts.
>El uso de VLSM permite aprovechar al máximo las direcciones IP públicas y es una técnica que se utiliza junto con CIDR(Classless Inter-Domain Routing) para lograr un direccionamiento eficiente y escalable en redes IPv4 públicas.


![[{D90C3588-BF75-45A6-8154-9C1C58B031B2}.png|521]]
#### ==52 Cuál de las siguientes características corresponde a VSLM (seleccione una o varias):==
- [ ] Permite crear para muchos hosts, mascaras largas
- [x] Permite tomar una subred y volverla a dividir en sub-redes más pequeñas
- [x] Permite crear para pocos hosts, máscaras más largas
- [ ] Exige que todas las áreas o departamentos de la empresa posean la misma mascara de subred
- [ ] Se implementa especialmente en direcciones privadas
##### rta
- [ ] Permite tomar una subred y volverla a dividir en sub-redes más pequeñas
- [ ] Permite crear para pocos hosts, máscaras más largas
## Administracion de direcciones IP
### ==53 Un administrador de red tiene que configurar manualmente 5 puestos de trabajo de una red. Por error omitió poner la puerta de enlace en una de ellos. ¿Se pueden comunicar entre ellas?==
- [x] Si, todas se comunican entre ellas.
- [ ] Si y todas pueden salir a Internet
- [ ] Ninguna de las opciones
- [ ] No, sólo se pueden comunicar las 4 que tienen puerta de enlace
#### rta
Si, todas se comunican entre ellas.

Comentarios
La puerta de enlace (gateway) solo es necesaria cuando una computadora necesita
comunicarse con otras redes (por ejemplo, salir a Internet).
Pero para comunicarse dentro de la misma red local (LAN), no es necesario tener
con�gurada la puerta de enlace

# --- preg o cosas de ver donde agregar dsp 

## ==54 se puede determinar la clase entonces solo con la direccion ip?==
Sí, exactamente. Se puede determinar la clase de una dirección IPv4 observando únicamente el valor de su **primer byte** (es decir, el primer número que aparece antes del primer punto en su notación decimal).

Las fuentes establecen la siguiente regla basándose en el valor de ese primer byte para identificar la clase rápidamente:

- **Clase A:** Si el primer número está entre **1 y 127** (ej. 1.0.0.0 – 127.255.255.255).
- **Clase B:** Si el primer número está entre **128 y 191** (ej. 128.0.0.0 – 191.255.255.255).
- **Clase C:** Si el primer número está entre **192 y 223** (ej. 192.0.0.0 – 223.255.255.255).
- **Clase D:** Si el primer número está entre **224 y 239** (ej. 224.0.0.0 – 239.255.255.255).

Para ilustrarlo con ejemplos:

- Si tienes la dirección IP **45.67.255.8**, como su primer byte es **45** (un valor entre 1 y 127), puedes asegurar inmediatamente que pertenece a la **Clase A**.
- Si tienes la dirección **180.34.23.29**, al empezar con **180**, sabes automáticamente que es de **Clase B**.
- Si la dirección es **201.35.58.10**, al tener un **201** en su primer byte, se determina de inmediato que es una **Clase C**.

Por lo tanto, **no necesitas conocer la máscara de red para saber a qué clase comercial fue asignada**; el diseño original de la arquitectura obliga a que el primer byte de la dirección IP contenga esa información.



## ==55 y pero cuando se necesita la direccion ip y la mascara? para que se necesitaban ambas? ==
Se necesitan ambas de forma conjunta porque funcionan lógicamente como una **pareja inseparable** en la configuración de cualquier dispositivo de red. Una dirección IP por sí sola no brinda la información suficiente para operar, y una máscara por sí sola tampoco sirve para nada.

Para comprender la relación de causa y efecto de por qué se exigen ambas simultáneamente:

- **La necesidad de la Dirección IP:** La dirección IP es un número lógico de 32 bits que **identifica a un dispositivo** para que pueda tener conectividad y comunicarse con otros equipos,,. El diseño de esta dirección es jerárquico, lo que significa que está dividida lógicamente en dos segmentos: una **"parte de red"** (que indica la ubicación física o subred) y una **"parte de host"** (que identifica al dispositivo individual),.
- **La necesidad de la Máscara de Red (El problema):** Como la IP es solo una secuencia continua de números, la computadora no tiene forma de adivinar por sí misma dónde termina la parte de red y dónde empieza la parte de host. La causa que obliga a usar una máscara es que su función exclusiva es **identificar exactamente cuál es la parte de red dentro de esa dirección IPv4**,,.
- **El Efecto de usarlas juntas (La solución):** Al tener configurados ambos parámetros, el dispositivo ejecuta internamente una operación lógica y matemática llamada **AND Booleano**, comparando bit a bit la dirección IP con su respectiva máscara,,. El resultado directo de esta operación le permite a la computadora **descubrir la Dirección de Red exacta a la que pertenece**,,.

En conclusión, la regla estructural dicta que **siempre debe estar presente la máscara de subred** acompañando a la dirección IP,. Sin la configuración conjunta de estos dos parámetros (junto con la puerta de enlace para salir al exterior), el dispositivo simplemente no sabrá en qué red se encuentra parado y no tendrá conectividad,.



este ni idea donde poner o si lo vimos
# ==56 EN TEORÍA NO VA AL PARCIAL! Cual de las siguientes a�rmaciones describen el campo suma de veri�cación del protocolo IPv4 (seleccione dos)==
- [ ] Lo calculan sólo los routers para saber si encaminar o descartar el paquete
- [ ] Se utiliza para garantizar la integridad de todo paquete IPv4
- [ ] Se calcula en el origen, el destino y dos veces en cada router
- [ ] Permite saber si el origen debe retransmitir un paquete dañado
- [ ] Permite detectar errores en la cabecera del paquete IPv4
## rta
Lo calculan sólo los routers para saber si encaminar o descartar el paquete
Se calcula en el origen, el destino y dos veces en cada router
Permite detectar errores en la cabecera del paquete IPv4

Comentarios
En cada router se VERIFICA una vez (veo que esté todo en orden) y se CALCULA una
vez (para actualizar el TTL).
NO SÉ si es lo mismo que decir que se CALCULA dos veces, pero supuestamente, el profe
lo toma como que sí (fuente: Times New Roman).



#  == 57 Cuál de los siguientes campos pertenece a la cabecera de un paquete IPv4 (seleccione 2)==
- [ ] Time to live
- [ ] Límite de salto
- [ ] Longitud de carga útil
- [ ] Longitud de cabecera
## rta
TTL 
longitud de cabecera
# ==58 Los mensajes ICMP se envían utilizando el encabezado IP básico Seleccione una:==

v o f
## rta
La respuesta correcta es: **Verdadero (V)**.

Para comprender el **porqué** basándonos en la arquitectura de redes, analicemos la relación entre estos protocolos:

- **La ubicación en la arquitectura (La Causa):** Según la suite de protocolos TCP/IP, tanto el protocolo **IP** como el protocolo **ICMP** pertenecen y operan conjuntamente en el **Nivel de Interred (Capa 3)**.
- **La Función:** Una de las responsabilidades ineludibles delineadas para esta Capa de Interred es la de **"Implementar mensajes de control"**. ICMP es precisamente el protocolo encargado de generar estos mensajes (por ejemplo, para reportar errores o diagnósticos como los del comando _ping_).
- **El Encapsulamiento (El Efecto):** _(Nota técnica externa a las fuentes provistas: Aunque los apuntes ubican a ICMP en la misma capa que IP, el detalle arquitectónico de que usa el "encabezado IP básico" es teoría general de redes que complementa tu material y puedes verificar en tu bibliografía oficial)._ Debido a que ICMP es un protocolo de control y carece de mecanismos propios de encaminamiento o direccionamiento para viajar entre routers, sus mensajes se encapsulan directamente como "datos" o carga útil dentro de un datagrama IP estándar. Por lo tanto, el paquete resultante utiliza ineludiblemente el **encabezado IP básico** para poder ser ruteado hasta su destino final.
#  ==59 Indique cuál es el tamaño mínimo de la cabecera de un paquete IPv4===
- [ ] 18 bytes 
- [ ] 15 bytes 
- [ ] 20 bytes 
- [ ] 40 bytes 
- [ ] 30 bytes 
- [ ] 60 bytes 
- [ ] 25 bytes 
- [ ] 6 bytes
## rta
**20 bytes**.

justif:
La respuesta correcta es: **20 bytes**.

Para comprender el **porqué** de este tamaño basándonos en el proceso de encapsulamiento de la arquitectura TCP/IP:

- **El Encapsulamiento (La Causa):** Cuando los datos descienden por el modelo de capas en el dispositivo de origen, la Capa de Interred (Capa 3) recibe el segmento de la Capa de Transporte y necesita ineludiblemente agregarle su propia información de control para formar un **paquete** (o datagrama). Esta información es la que le permite al router tomar decisiones de encaminamiento.
- **El Tamaño Estructural (El Efecto):** Esta información de control obligatoria conforma el encabezado IPv4. Como se puede constatar en las capturas de análisis de tráfico (Wireshark) incluidas en la documentación, el campo `Header Length` (Longitud de cabecera) de un paquete IPv4 determina que su tamaño base es de **20 bytes**. Dentro de esos 20 bytes viajan ineludiblemente las direcciones lógicas (IP de origen y destino), el protocolo, la suma de verificación y el desplazamiento de fragmentación, entre otros.

**Por qué las demás opciones son incorrectas:**

- **18 bytes:** Es una medida real y habitual, pero aplica a otra unidad de datos. Corresponde a la cantidad exacta de bytes de control que se le adhieren a una **trama Ethernet clásica** en la Capa de Enlace de Datos (es decir, 6 bytes de la MAC de destino + 6 bytes de la MAC de origen + 2 bytes del campo Tipo + 4 bytes de la secuencia de verificación FCS en la cola). No corresponde al paquete de Capa 3.
- Las demás opciones numéricas (15, 25, 30 o 40 bytes) son falsas para el encabezado mínimo de este protocolo. _(Nota técnica externa a las fuentes provistas: Aunque la cabecera IPv4 puede extenderse teóricamente hasta los 60 bytes si se le agregan campos de "Opciones", el tamaño mínimo indispensable que siempre debe estar presente es de 20 bytes)._

# == 60 ¡EN TEORÍA NO VA AL PARCIAL! El algoritmo para determinar el checksum del IPv4 se calcula:
- [ ] En el origen, en el destino, y una vez en cada salto
- [ ] En el origen, en el destino y dos veces en cada salto
 
## rta
En el origen, en el destino y dos veces en cada salto

omentarios
En el origen, cuando se crea el paquete.
En cada salto (cada router por el que pasa) → porque se modi�ca un campo llamado
TTL, así que hay que recalcular el checksum.
En cada router se VERIFICA una vez (veo que esté todo en orden) y se CALCULA una
vez (para actualizar el TTL).
NO SÉ si es lo mismo que decir que se CALCULA dos veces, pero supuestamente, el profe
lo toma como que sí (fuente: Times New Roman).
En el destino, para veri�car que el paquete llegó bien.

# 61 ¿Cómo hace un router para distinguir un paquete de datos de uno que transporta un reporte ICMP?
- [ ] Se remite a las capas superiores
- [ ] Lee el campo Protocolo del encabezado IP
- [ ] Lo distingue según su valor
- [ ] No es necesario hacer nada
- [ ] Por las entidades de transporte

## rta
- [ ] Lee el campo Protocolo del encabezado IP

Comentarios
Cuando un router recibe un paquete IP, necesita saber qué tipo de contenido lleva ese
paquete:
¿Es un mensaje normal (como de una app)?
¿O es un mensaje especial de error o control, como los de ICMP?
Para eso, mira un campo del encabezado IP llamado “Protocolo”.
Este campo dice con un número:
1 → es ICMP
6 → es TCP
17 → es UDP

# ---- REGLAS FUNAMETALES
Sí, **todo lo que has enumerado es estrictamente cierto**. Tus anotaciones son un resumen perfecto de las reglas de diseño y configuración de direccionamiento IPv4 para redes y subredes.

A continuación, te explico el **porqué** arquitectónico de cada una de estas reglas basándonos en tus apuntes:

- **Todas las máquinas de un área deben pertenecer a la misma subred:**
    
    - **¿Por qué?** Crear subredes permite dividir el esquema de direcciones de una organización en función de sus diferentes áreas o departamentos. Arquitectónicamente, esto agrupa a los equipos separando el tráfico, lo que permite reducir los dominios de broadcast (cada área tiene el suyo propio) y facilita enormemente la implementación de reglas de seguridad (por ejemplo, definir en un firewall qué áreas tienen acceso a Internet o a un servidor específico y cuáles no).
- **Comparten la misma máscara y el mismo Gateway:**
    
    - **¿Por qué?** La **máscara de subred** debe ser obligatoriamente idéntica para todas las máquinas de esa área porque es la "plantilla" que utilizan para entender su propia red, indicándoles qué porción de la IP corresponde a la subred y cuál a los hosts. El **Gateway** (puerta de enlace) debe ser el mismo porque todas las computadoras de esa subred ineludiblemente utilizarán la misma "puerta de salida" (la interfaz del router conectada a su switch) para enviar información hacia el exterior.
- **Sin Gateway configurado → solo hay conectividad local:**
    
    - **¿Por qué?** La PC utiliza el Gateway por defecto como su única vía de escape. Si a la máquina no se le configura este parámetro, no sabrá por dónde enviar los paquetes cuyo destino no pertenezca a su propio segmento. Como efecto directo, la PC quedará aislada y solo podrá comunicarse con los equipos conectados a su misma LAN (conectividad local), siendo incapaz de alcanzar otras subredes de la empresa o Internet.
- **El router no necesita Gateway (su función nativa ya es enrutar):**
    
    - **¿Por qué?** Un dispositivo final (host) necesita un Gateway para que otro equipo más inteligente lo ayude a salir de su red. Pero el router _es_ ese dispositivo inteligente. Opera en la Capa 3 (Interred) y su función estructural principal es **encaminar** los paquetes entre redes diferentes. El router no delega su tráfico a un Gateway por defecto genérico; en su lugar, examina la IP de destino de cada paquete y consulta su propia tabla de encaminamiento para tomar decisiones lógicas sobre por qué interfaz reenviar la información.
- **La primera IP válida del rango suele asignarse al Gateway (convención):**
    
    - **¿Por qué?** A nivel técnico, a la interfaz del router se le podría asignar cualquier dirección IP válida del rango de la subred (por ejemplo, la 66, la 70 o la 74). Sin embargo, se utiliza la primera (o a veces la última) simplemente por una **convención o acuerdo práctico entre administradores de red**. La causa de esto es operativa: si hay que probar la conectividad o reconfigurar la red, es mucho más predecible y fácil hacer _ping_ a la primera IP del rango que tener que adivinar o buscar entre decenas de direcciones intermedias posibles.
- **Una IP de la subred que se asigne al Gateway resta 1 host disponible:**
    
    - **¿Por qué?** La interfaz del router que actúa como Gateway de la subred es, a nivel de direccionamiento, un nodo físico más dentro de esa LAN que necesita ser identificado. De la cantidad de direcciones útiles que obtenemos en una subred mediante el cálculo ($2^n - 2$), se debe "gastar" o asignar forzosamente una IP válida a la interfaz del router. Como consecuencia, si el cálculo de tu subred te da 30 IPs disponibles y le asignas una al router, matemáticamente te quedarán un máximo de 29 direcciones para configurar en las PCs u otros dispositivos finales.