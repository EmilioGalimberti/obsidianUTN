## 3. Arquitectura [[IEEE 802.11]] y Dominios Lógicos
Es el **estándar técnico** y la pila de protocolos. Es el conjunto de normas de red creadas por el Instituto IEEE que definen las reglas lógicas y físicas de _cómo_ debe construirse y operar exactamente esa red inalámbrica


### COMPONENTES – DISPOSITIVOS QUE VAMOS A CONECTAR
1. Estaciones: Dispositivos como PC, notebooks, impresoras, smartphones, Smart TV, etc., que se conectan de manera inalámbrica
2. Medio inalámbrico: Usa radiofrecuencias o infrarrojos como el aire por donde se transmiten las ondas
3. Celda: Área geográfica donde dispositivos se interconectan inalámbricamente, siendo el área de cobertura para mantener conectividad
4. Access Point (AP): Funciona como un bridge, permitiendo la interconexión de dispositivos inalámbricos
5. Sistema de Distribución: Facilita la movilidad entre celdas, conectando varias de ellas a través de cable o aire.
6. Conjunto de Servicios Básicos (BSS): Grupo de estaciones que se comunican, en modos ad hoc o infraestructura, compartiendo un mismo SSID en una red
7. Conjunto de Servicio Extendido (ESS): Unión de varios BSS que permite el roaming, posibilitando la conectividad al desplazarse entre celdas

### Ejemplo Arquitectura de 802.11
![[{4619A1B9-8C5B-45C2-B268-DC543C1CCA7E}.png]]
Nota: Roaming es la capacidad de un dispositivo inalámbrico de
cambiar de área de cobertura, asociándose automáticamente al access point de la nueva área. Los access points se interconectan mediante una red cableada para comunicar dispositivos de diferentes celdas, formando así el Conjunto de Servicios Extendidos.

**[BSS] (Conjunto de Servicios Básicos)**: Es la "celda" o área de cobertura geográfica controlada por un único **[[Access Point]]**. Todos los dispositivos dentro del BSS interactúan bajo la jurisdicción de esa antena.

**[Sistema de Distribución] (DS)**: Es la red troncal (habitualmente cableada por Ethernet) que sirve para interconectar múltiples Access Points entre sí.

**[ESS] (Conjunto de Servicios Extendido)**: Es la suma de varios **[BSS]** interconectados mediante un **[Sistema de Distribución]**, permitiendo abarcar infraestructuras enormes como el campus de una universidad.
![[{3F375644-6022-4EEE-8DB0-0B6C013C33E8}.png]]

---
* Se requiere autenticación y asociación con el AP para establecer conexión

### Modos de Implementación

- **[Modo Ad-hoc]:** Red descentralizada ("peer-to-peer") donde los dispositivos se conectan directamente entre sí sin necesidad de un AP.
	- Envío directo de tramas entre dispositivos
	- Permite formar pequeñas redes inalámbricas entre dispositivos.
	- ![[{E8023E6E-EA6A-4EBF-BF69-960DD7B6C36D}.png]]
- **[Modo Infraestructura]:** Red centralizada donde todos los dispositivos obligatoriamente envían su tráfico a través del [[Access Point]].
	- Conexión del AP a otra red
	- Envío y recepción de tramas por parte del cliente a través del AP.
	- Posibilidad de conectar varios AP formando un "Sistema de Distribución" y una red extendida.![[{D87E9311-9545-46FA-912F-7C6126D1D293}.png]]
	 Nota: Las dos antenas en el Access Point están relacionadas con la tecnología MIMO, que mejora el ancho de banda transmitiendo y recibiendo simultáneamente por varias antenas.



### 4. Servicios del [Sistema de Distribución] (DS)
![[{3F375644-6022-4EEE-8DB0-0B6C013C33E8}.png]]
Para gestionar la movilidad de los usuarios, la norma establece 5 servicios fundamentales:

1. **Asociación:** 
	1. Conexión de una estación a un AP mediante un SSID (nombre de la red inalambrica)
		1. SSID (Service Set Identifier) → nombre de la red formado por 32 caracteres como máximo. Todos los dispositivos dentro de un BSS deben compartir el mismo SSID
	2. Handshake para autenticación.
		1. Paso previo a la asociación, mediante el cual el AP valida la identidad del usuario a través de un intercambio criptográfico o **[Handshake]**
	3. Una estación puede asociarse a un AP a la vez.
	4. Protocolos de autenticación constantes
2. **[Disociación]:** Proceso donde un equipo se desconecta voluntariamente de la red o se apaga, dándose de baja del registro del AP
	1. Salida de un dispositivo de la red.
	2. Puede ser antes de apagarse o por mantenimiento.
	3. Puede ser iniciada por AP o estación
	4. AP apagado provoca disociación automática.
3. **[Reasociación]:** Servicio clave que permite el **[Roaming]**; es decir, permite que un usuario caminando por un edificio se desvincule de un AP con señal débil y se asocie a un nuevo AP con mejor señal de forma transparente, sin perder conectividad
	1. Cambio de asociación de un AP a otro.
	2. Permite roaming y se realiza automáticamente
4. **[Distribución]:** Traslado de los datos a través de la red troncal hasta el AP de destino.
	1. Traslado de datos entre APs
	2. Interconexión de APs mediante tecnología Ethernet.
	3. Datos enviados al AP local y a través del DS al AP remoto.
	4. Trama con 4 direcciones MAC.
5. **[Integración]:**Proceso de conversión de protocolos, traduciendo tramas inalámbricas a tramas Ethernet
	1. Función de puente, conectando tecnologías inalámbricas y Ethernet a nivel de capa 2.



### Como se asocia un cliente inalambrico

1. Para permitir la negociación de estos procesos, se deben configurar los parámetros en el AP y luego en el cliente


2. Autenticacion
Para asociarse, un cliente inalámbrico y un AP deben acordar parámetros específicos.
* SSID → el cliente necesita conocer el nombre de la red para conectarse
* Contraseña → para que el cliente se autentique en el AP
* Modo de red → estándar 802.11 que se esté utilizando
* Modo de seguridad → parámetros de seguridad, WEP, WPA, WPA2 o WPA3
* Configuración de canales → las bandas de frecuencia en uso

![[{C356F989-9AD2-438B-90BC-73160F1CEF12}.png]]

3. El cliente se asocia con un AP o router inalámbrico


(Tipos de tramas manejadas: control, administración y datos.)


Se utilizan tramas de administración para: Implementra los servicios de autenticación, asociación, reasociación, baliza, prueba, etc.
* Descubrir nuevos AP inalámbricos.
* Autenticar con el AP.
* Asociarse al AP.
* Descubrir nuevos AP inalámbricos.
* Autenticar con el AP.
* Asociarse al AP.

### Consideraciones importantes en IEEE 802.11

#### Confiabilidad

* Problema
	* Redes inalámbricas son ruidosas e inseguras
	* Interferencia con otros dispositivos
	* las redes inalámbricas se consideran "no fiables"
* Estrategias para mejorar la fiabilidad:
	* Ajuste de la tasa de transmisión según la calidad de la red.
		* cuando el dispositivo detecta que se pierden datos, (para saber que se perdian dato lo hace atraves de que exigen el envío de acuses de recibo (**[ACK]**) por cada trama exitosa porque utilizan [[CSMA_CA]] )
			* Entonces cuando no llegan los acuses de recibo disminuye la tasa de trasmision
			* y al reves cuando llegan los acuses de recibo aumenta la tasa de trasmision
	* Envío de tramas cortas y fragmentadas. + :
		* mejora la probabilidad de que la trama llegue correctamente
		* Dividir las tramas en fragmentos numerados individualmente. No se puede transmitir el fragmento K+1 hasta que no se haya recibido la confirmación del fragmento k
	* Detección física (si hay una señal o no en el aire) y virtual del canal. (adquirir el canal)
	* Uso de NAV (vector de asignación del canal) para evitar colisiones.
		* - **[NAV] (Vector de Asignación de Red):** Mecanismo de "detección virtual". Temporizador virtual transmitido en las tramas. El dispositivo emisor avisa al resto cuánto tiempo exacto en microsegundos ocupará el canal. Los demás dispositivos leen el **[[NAV]]** y suspenden sus transmisiones durante ese lapso

#### Ahorro de energía
* Problema:
	* La duración de las baterías de los dispositivos móviles es importante
* Estrategias para mejorar
	* Mejorar la vida útil de las baterías de dispositivos
		* que los clientes no tengan que desperdiciar energía cuando no tienen información para enviar o recibir
		* Clientes informan al AP antes de entrar en modo de ahorro de energí
		* AP controla y almacena tramas en el buffer para dispositivos en modo ahorro
	* Uso de tramas baliza para anunciar la presencia del AP y parámetros del sistema.
		* Son difusiones periódicas que realiza el Access Point (cada 100 mseg)
		* Anuncian la presencia del Access Point a los clientes
		* Llevan parámetros del sistema como el identificador del Access Point, tiempo que falta para la siguiente baliza y configuración de seguridad
	* Objetivo: evitar desperdicio de energía cuando los clientes no transmiten o reciben datos.



### Pila de protocolos IEEE 802.11
![[{3FA8FE6C-4E8D-4BB3-B875-6EB2C7EC7D55}.png]]
La profesora recordó que la **[[Capa de Enlace de Datos]]** se divide en dos subcapas y explicó la diferencia fundamental entre ellas en este entorno:
* [Subcapa LLC] **(Control de Enlace Lógico)** es común a todas las tecnologías. Es decir, la lógica de enlace con las capas superiores de red es exactamente la misma ya sea que estemos usando un cable de red clásico o una antena Wi-Fi
* [Subcapa MAC] **(Control de Acceso al Medio)** depende de la parte física, varía en la forma de enviar la señal.


#### Estándares IEEE 802.11 y Frecuencias
Estándares IEEE 802.11
* Transmite en bandas de 2.4 GHz y 5 GHz sin requerir licencia.
* Saturación mayor en 2.4 GHz
* La mayoría de las placas inalámbricas soporta todas las normas
*

Normas y Tecnologias

Se analizaron las bandas ISM (Industrial, Scientific and Medical) donde operan estas tecnologías sin licencia comercial.


| Estándar                                  | Banda de Frecuencia | Velocidad Teórica                                        | Modulación/Tecnología                                                                      |                                                                                 |
| :---------------------------------------- | :------------------ | :------------------------------------------------------- | :----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 802.11a                                   | 5 GHz               | 54 Mbps<br>(real de 20 Mbps).                            | OFDM con 52 sub-portadoras.<br><br>Multiplexación por División de Frecuencias Ortogonales) | Alcance de 20 km con radios especiales.                                         |
| **802.11b**                               | 2.4 GHz             | 11 Mbps                                                  | Espectro Expandido                                                                         | Puede interferir con otros dispositivos en la misma banda.                      |
| **802.11g**<br><br>Evolución del 802.11b, | 2.4 GHz             | 54 Mbps<br><br>(real de 22 Mbps)                         | [OFDM]                                                                                     | Compatible con 802.11a/b/g.<br><br>Copia modelos de modulación OFDM de 802.11a. |
| **802.11n**                               | 2.4 GHz y 5 GHz     | Hasta 600 Mbps<br><br>percibido por el usuario 100 Mbps) | [MIMO] (Múltiples antenas)                                                                 | Compatible con a/b/g.<br><br>Ratificado en 2009.                                |
| **802.11ac**                              | 5 GHz               | Hasta 1.3 Gbps                                           | Utiliza hasta 8 flujos MIMO y modulación de alta densidad 256 QAM.                         | Utiliza hasta 8 flujos MIMO y modulación de alta densidad 256 QAM.              |


### 6. Problemas Físicos de Topología | Protocolo [[CSMA_CA]] en la Subcapa MAC 802.11:

El profesor hizo un fuerte énfasis en dos anomalías físicas de la topología inalámbrica:
1. Rangos de Transmisión Diferentes:
	1. • Estaciones tienen alcances de radio distintos
	2.  Transmisiones pueden no ser recibidas en todas las partes de una celda

2. Terminal Oculta 
	1. - **Problema de la [Terminal Oculta]:**
		1. Una estación no detecta a un competidor potencial debido a la distancia.
		2. Problema de atenuación de la señal
		3. ejemplo: Ocurre cuando dos máquinas (A y C) están demasiado lejos y no se escuchan entre sí. Al creer erróneamente que el canal está libre, transmiten a la vez hacia el nodo central (B), generando una **[Colisión]** destructiva en el receptor.
	   ![[{74AA1080-6A45-4315-88D3-5C92A382BDC8}.png|333]]
	
3. Terminal Expuesta
	- **Problema de la [Terminal Expuesta]:** 
	- Una estación no transmite pensando que el receptor está en zona de interferencia cuando no
	- Subutilización del canal.
	- ejemplo: Falla de optimización donde una estación (B) quiere trasmitir a C, pero escucha que su vecina (A) está transmitiendo (hacia otro lado) y, por precaución, porquee cree que C esta en la misma celda entonces, no transmite. Desperdicia su turno y pierde ancho de banda asumiendo que el canal general está ocupado
		![[{C9091ADE-B19E-429A-ABCC-B0300A36745F}.png|379]]
		 Para que B pueda transmitir, debe esperar a que A termine, va a intentar enviar una trama corta (RTS) a la red y como C si la va a poder escuchar, si llega a estar libre le envía un CTS para que le envíe información. A partir de ahí queda reservado el ancho de banda por el tiempo que B tarda en comunicarse con C.

``` mermaid
graph TD
    A[Dispositivo evalua el medio inalambrico] --> B{¿Detecta transmision de otros?}
    B -- NO SE ESCUCHAN entre si --> C[Transmiten datos al mismo tiempo]
    C --> D[Colision destructiva en el AP central]
    D --> E[Problema de Terminal Oculta]
    B -- SI SE ESCUCHAN --> F[Nodo B escucha a Nodo A transmitir a otro destino]
    F --> G[Nodo B cree falsamente que el medio no esta disponible]
    G --> H[Problema de Terminal Expuesta]
```
### 8. Seguridad Inalámbrica y Autenticación

WiFi Alliance:
* Organización que promueve la tecnología WiFi
* Certifica interoperabilidad en productos WiFi (tecnología 802.11).

Tipos de Autenticación:
1. Autenticación de Sistema Abierto
	* No requiere contraseña, usado en lugares públicos.
	* Permite asociación automática sin proporcionar contraseña.
2. Autenticación de Clave Compartida:
	* Recomendado.
	* Autentica y cifra datos entre cliente y AP.
	* Requiere preacuerdo de clave simétrica entre ambas partes.

#### Evolución de Protocolos:
1. Autenticación de clave compartida (PSK):
	• Significa que es simétrico, o sea, tenemos que preacordar una clave con el AP o con el router.
2. WEP (Wired Equivalent Privacy):
	• Cifrado en estándar original 802.11.
	• Usa RC4 con claves de 64 o 128 bits.
	• No se recomienda por vulnerabilidades.
3. WPA (WiFi Protected Access):
	• Estándar WiFi Alliance.
	• Utiliza servidor RADIUS para autenticación.
	• Implementa Protocolo de Integridad de Clave Temporal (TKIP). cambia las claves dinamicamente
4. WPA2:
	• Ratificado en 2004.
	• Emplea cifrado AES (Advanced Encryption Standard).
5. WPA3:
	• Sucesor de WPA2, anunciado en 2018.
	• Proporciona mejoras en seguridad y cifrado.

#### metodos de autenticacion
Personal
 * Para redes hogareñas o pequeñas oficinas.
 * Dispositivos se autentican con el router mediante clave precompartida (PSK).
 * Autenticación del AP.
Enterprise
* Para empresas, requiere servidor de autenticación RADIUS.
* El AP se comunica con un servidor de autenticación que tiene una base de datos con nombres de usuario y contraseñas para controlar el acceso a la red. Cuando el usuario se quiere autenticar para poder asociarse el AP se comunica con el servidor RADIUS, manda los datos del usuario y si son correctos el servidor le dice al AP que es correcto y recién ahí lo asocia al AP. Se definen los nombres de los empleados con sus respectivas contraseñas y solamente ellos se pueden autenticar, son totalmente privados los accesos. Una vez autenticado el dispositivo, recién ahí se asocia.