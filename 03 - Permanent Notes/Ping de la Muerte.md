---
aliases:
subject:
  - REDES
  - cybersecurity
year:
exam:
unit:
type: TEO
zk_type: permanent
status: in-progress
date: 2026-08-28
source:
tags:
---
---
## 📌 Diferencia Conceptual Rápida

│ [!IMPORTANT] La Diferencia Clave
│
│ • Ping de la Muerte: Es un exploit de software basado en un paquete malformado. No necesita volumen: una sola computadora enviando un único paquete inválido podía congelar o reiniciar el sistema
│ operativo víctima debido a un desbordamiento de búfer (buffer overflow).
│ • DDoS: Es un ataque de agotamiento de recursos por volumen masivo. No explota fallas en el código del sistema operativo, sino que satura el ancho de banda, la memoria o la tabla de conexiones
utilizando
│ miles de dispositivos distribuidos (Botnets/Zombies).
──────
## 📊 Tabla Comparativa
Parámetro             | 💀 Ping de la Muerte (Ping of Death)                                                 | 🌐 DDoS (Distributed Denial of Service)
-----------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------
Capa del Modelo OSI   | Capa 3 (Red) — Protocolos IPv4 / ICMP.                                               | Capa 3, 4 y 7 (Red, Transporte y Aplicación).
Origen del Ataque     | Un único equipo atacante.                                                            | Miles o millones de equipos (Botnet / Zombies).
Mecanismo de Acción   | Paquete ICMP fragmentado que supera el tamaño máximo legal de IPv4 (65.535  bytes).  | Envío masivo de tráfico o solicitudes legítimas/falsas que saturan la capacidad del
					 |                                                                                      | servidor.
Efecto en la Víctima  | Colapso del SO: Kernel panic, pantalla azul (BSOD) o reinicio instantáneo.           | Degradación / Caída del Servicio: El servidor se vuelve inaccesible por falta de ancho de
					 |                                                                                      | banda, CPU o sockets.
Naturaleza del Ataque | Vulnerabilidad de implementación en la pila TCP/IP (Buffer Overflow).                | Saturación volumétrica o agotamiento de estado de conexiones.
Estado Actual         | Obsoleto / Mitigado: Todos los sistemas operativos modernos descartan paquetes       | Altamente vigente y sofisticado: Uno de los vectores de ataque más comunes y peligrosos hoy
					 | malformados desde fines de los 90.                                                   | en día.
──────
## 1. 💀 Anatomía del Ping de la Muerte (Ping of Death)
### ¿Cómo funcionaba?

1. La especificación del protocolo IPv4 establece que el tamaño máximo teórico de un datagrama IP (incluyendo cabecera) es de 65.535  bytes (2¹⁶ - 1).
2. Como las redes Ethernet tienen una MTU máxima de 1500 bytes, cualquier datagrama grande debe fragmentarse.
3. El atacante creaba un paquete ICMP Echo Request y lo dividía en fragmentos manipulando el campo Fragment Offset. Al sumar el desplazamiento del último fragmento más su tamaño, el total superaba los 65.
535  bytes (por ejemplo, 65.538  bytes).
4. Al recibir todos los fragmentos, la pila TCP/IP del sistema operativo intentaba reensamblarlos en un búfer de memoria de tamaño fijo (65.535  bytes).
5. Resultado: Al sobrepasar el búfer, se producía un desbordamiento de memoria (Buffer Overflow) que corrompía la memoria del kernel, colgando la máquina de inmediato.

graph LR
	Attacker[Atacante: 1 sola PC] -->|Fragmento 1| R[Red]
	Attacker -->|Fragmento 2| R
	Attacker -->|Fragmento N: Offset ilegal| R
	R --> Victima[Víctima: Reensambla > 65.535 bytes]
	Victima --> Crash["💥 Buffer Overflow / Crash del Sistema"]
──────
## 2. 🌐 Anatomía de un Ataque DDoS

### ¿Cómo funciona?

6. Un atacante compromete previamente miles de dispositivos conectados a Internet (PCs, routers hogareños, cámaras IP, dispositivos IoT) infectándolos con malware para convertirlos en Zombies / Bots.
7. Esta red de equipos secuestrados forma una Botnet, controlada remotamente mediante un servidor de Comando y Control (C&C).
8. A la orden del atacante, todos los zombies envían peticiones simultáneas hacia la víctima.

graph TD
	Attacker["👤 Atacante (C&C)"] -->|Orden de disparo| Z1["🧟 Zombie 1"]
	Attacker -->|Orden de disparo| Z2["🧟 Zombie 2"]
	Attacker -->|Orden de disparo| Z3["🧟 Zombie N..."]
	
	Z1 -->|Peticiones masivas| Target["🎯 Servidor Víctima"]
	Z2 -->|Peticiones masivas| Target
	Z3 -->|Peticiones masivas| Target
	
	Target --> Drop["🚫 Saturación de Sockets / CPU / Enlace<br/><b>Servicio Inaccesible para Usuarios Legítimos</b>"]

### Tipos comunes de DDoS según la Capa OSI:
flowchart TD
	DDoS[Tipos de Ataques DDoS] --> L3[Capa 3: Volumétricos]
	DDoS --> L4[Capa 4: Agotamiento de Estado]
	DDoS --> L7[Capa 7: Capa de Aplicación]

	L3 --> ICMP_Flood["ICMP Flood / UDP Amplification<br/><i>(Saturan el ancho de banda del enlace)</i>"]
	L4 --> SYN_Flood["TCP SYN Flood<br/><i>(Saturan la tabla de conexiones/sockets del servidor)</i>"]
	L7 --> HTTP_Flood["HTTP GET/POST Flood / Slowloris<br/><i>(Saturan los hilos/CPU del servidor web)</i>"]

• Capa 3 / Volumétricos (ICMP/UDP Flood): Inundan el enlace de Internet con tantos Gigabits por segundo que el canal físico se satura y los paquetes legítimos se descartan por desborde.
• Capa 4 / Agotamiento de Estado (TCP SYN Flood): Envían paquetes SYN de inicio de conexión TCP pero nunca responden con el ACK final. El servidor deja la conexión semiabierta en memoria esperando el
saludo, llenando su tabla de sockets y rechazando conexiones reales.
• Capa 7 / Aplicación (HTTP Flood): Envían miles de solicitudes complejas (ej. consultas pesadas a bases de datos o descargas de archivos) para llevar el uso de CPU y memoria RAM del servidor al 100%.
──────
## 🎯 Síntesis para Examen / Estudio

• Ping de la Muerte: Se basaba en romper el código del receptor mediante un paquete ICMP ilegalmente grande (>65.535  bytes). Bastaba un solo atacante.
• DDoS: Se basa en agotar la capacidad física/lógica del receptor (ancho de banda, memoria o hilos de procesamiento) mediante una marea coordinada de tráfico proveniente de múltiples orígenes (botnets).








# PING DE LA MUERTE MODENOS
¡Sí, totalmente! Aunque el Ping of Death original de los años 90 (el del límite de los 65.535  bytes) está superado, el mismo principio técnico sigue apareciendo con frecuencia en sistemas operativos
modernos:

│ [!NOTE] El Principio del Ataque
│ Ocurre cuando un atacante envía un único paquete de red especialmente manipulado (crafted packet) que aprovecha una falla de programación en el controlador de red del sistema operativo (tcpip.sys en
│ Windows o en el subsistema de red del Kernel Linux). Al procesarlo a nivel de Kernel (Ring 0), el sistema colapsa con pantalla azul (BSOD) o permite Ejecución Remota de Código (RCE) sin autenticación.

A continuación, los casos modernos más famosos y peligrosos que son los verdaderos "Ping de la Muerte del siglo XXI":
──────
### 1. Bad Neighbor (CVE-2020-16898) — El Ping de la Muerte de IPv6

Bautizado por la comunidad de ciberseguridad literalmente como el «Nuevo Ping de la Muerte»:

• ¿Cómo funcionaba? Explotaba el protocolo ICMPv6. El atacante enviaba un paquete de anuncio de router (Router Advertisement) con una opción de servidor DNS (RDNSS - Opción 25) que contenía una longitud
inválida en sus campos de cabecera.
• El fallo: El controlador de red de Windows (tcpip.sys) no validaba correctamente el tamaño de la opción en memoria al parsear el paquete ICMPv6.
• Impacto: Con enviar un solo paquete ICMPv6 a una máquina con Windows 10 / Server, la computadora tiraba instantáneamente una Pantalla Azul (BSOD) o permitía tomar control total del equipo de forma
remota, sin requerir contraseñas ni interacción del usuario.

graph LR
Attacker["👤 Atacante"] -->|1 solo paquete ICMPv6 malformado| Target["💻 Windows 10/Server (tcpip.sys)"]
Target -->|Falla de lectura en memoria kernel| BSOD["💥 Pantalla Azul Instantánea (BSOD) / RCE"]
──────
### 2. IPv6 Windows Packet Flaw (CVE-2024-38063) — Agosto 2024

Una de las vulnerabilidades más críticas y recientes de la historia de Windows:

• ¿Cómo funcionaba? Afectaba al manejo de fragmentación en IPv6.
• El fallo: Una vulnerabilidad de tipo Integer Underflow (subdesbordamiento de enteros) al procesar paquetes IPv6 fragmentados que llegaban desordenados o con extensiones de cabecera anómalas.
• Impacto: Permite a atacantes no autenticados ejecutar código arbitrario con privilegios del sistema o congelar cualquier máquina Windows conectada a la red local o a Internet que tenga IPv6 habilitado
por defecto.
──────
### 3. FragmentSmack (CVE-2018-5391) y SegmentSmack (CVE-2018-5390) en Linux

Estos ataques afectaron a servidores Linux y demostraron cómo saturar una máquina sin necesidad de una Botnet:

• ¿Cómo funcionaba? El atacante enviaba pequeños fragmentos IP o segmentos TCP con desplazamientos (offsets) completamente aleatorios y diseñados de forma maliciosa.
• El fallo: El algoritmo del kernel Linux para reensamblar y ordenar los fragmentos en memoria tenía una complejidad temporal de O(n²).
• Impacto: Con apenas unos pocos Kilobits por segundo de tráfico (el equivalente a una conexión lentísima enviada desde una sola PC), el kernel de Linux gastaba el 100% de la CPU intentando ordenar la
lista de fragmentos, dejando servidores gigantescos completamente paralizados.
──────
### 4. Ripple20 y Urgent/11 — Ataques a Dispositivos IoT

Muchos dispositivos modernos (cámaras de seguridad, impresoras, switches, dispositivos médicos o PLCs industriales) no usan Windows ni Linux completos, sino pilas TCP/IP embebidas como Treck o VxWorks.

• El problema: Se descubrieron más de 19 vulnerabilidades críticas donde el envío de paquetes ICMP / IP malformados a impresoras o equipos industriales provocaba el reinicio inmediato o la toma de control
del hardware.
──────
## 🔍 ¿Por qué siguen ocurriendo estos fallos en la actualidad?

flowchart TD
A["Pilas de Red Complejas<br/>(IPv6, Cabeceras de Extensión, Opciones)"] --> B["Procesamiento en Espacio de Kernel (Ring 0)"]
B --> C["Cualquier error de memoria (Punteros / Búfers) provoca Kernel Panic o BSOD"]

1. Mayor complejidad en IPv6: A diferencia de IPv4 que tenía cabeceras fijas simples, IPv6 incluye Cabeceras de Extensión, opciones variables (Hop-by-Hop, Routing, RDNSS) y mecanismos complejos de
autoconfiguración (SLAAC) que abren más margen para errores de programación.
2. Espacio de Kernel (Ring 0): Los controladores de red (tcpip.sys, drivers de placa) corren en el nivel más bajo y privilegiado del hardware. Si una aplicación normal como un navegador falla, se cierra
el programa; pero si falla el controlador de red al leer un paquete, se cae todo el sistema operativo.

### 📌 Resumen para recordar

• El Ping de la Muerte clásico atacaba el reensamblado de datagramas IPv4 >65.535  bytes.
• Las vulnerabilidades modernas equivalentes (Bad Neighbor, CVE-2024-38063, etc.) atacan el parseo de opciones ICMPv6, cabeceras de extensión o fragmentación TCP/IP en el kernel, logrando el mismo efecto
destructivo con un solo paquete.


# LABS
, totalmente. En el ámbito académico y de ciberseguridad defensiva, la forma estándar de estudiar estas vulnerabilidades es mediante laboratorios aislados y controlados. Esto permite entender el
comportamiento a bajo nivel de los protocolos (Capa 2, 3 y 4) sin poner en riesgo redes reales ni infringir normativas.

A continuación tienes las mejores alternativas y plataformas para estudiarlas de forma segura y legal:
──────
### 1. SEED Labs (Universidad de Syracuse) — La opción académica por excelencia
Es un proyecto educativo de código abierto desarrollado específicamente para cursos universitarios de redes y seguridad informática:

• ¿Qué incluye? Guías paso a paso y entornos preconfigurados en Docker / Máquinas Virtuales.
• Laboratorios clave:
• TCP/IP Attack Lab: Permite estudiar ataques de ARP Poisoning / Spoofing, ICMP Redirect, TCP SYN Flood y TCP RST Hijacking.
• Packet Sniffing and Spoofing Lab: Enseña cómo construir y manipular paquetes crudos usando Python y Scapy.
• Firewall and NAT Lab: Configuración de reglas en Linux (iptables / nftables) para mitigar estos ataques.
• Sitio oficial: SEED Labs - Syracuse University https://seedsecuritylabs.org/
──────
### 2. Laboratorio Local Aislado (VirtualBox / VMware)
Puedes montar tu propio banco de pruebas en tu computadora utilizando virtualización:

graph LR
subgraph Host_Fisico ["Tu Computadora"]
	subgraph Red_Aislada ["Red Interna / Host-Only (Sin salida a Internet)"]
		VM1["🐧 Kali Linux / Ubuntu<br/><i>(Generador con Scapy/Wireshark)</i>"]
		VM2["🎯 Máquina de Prueba (Víctima)<br/><i>(Versión de SO de estudio)</i>"]
		
		VM1 <-->|Tráfico de red aislado| VM2
	end
end

#### Reglas de oro para el laboratorio local:

1. Adaptador en modo Host-Only o Red Interna (Internal Network): Nunca uses modo Bridge (Puente) para pruebas de vulnerabilidades; de este modo, los paquetes solo existen entre las máquinas virtuales y no
salen a tu router ni a la red de tu casa.
2. Uso de Snapshots (Instantáneas): Saca una instantánea de la máquina de prueba antes de cualquier prueba para restaurarla en segundos si el sistema operativo se congela o sufre un kernel panic.
──────
### 3. Estudio con Scapy y Análisis en Wireshark

Para entender cómo se construyen estas anomalías de protocolo a nivel de bits, la herramienta más utilizada en docencia e investigación es Scapy (biblioteca de Python para manipulación de paquetes):

• Permite definir campos específicos de la cabecera IP, ICMP o TCP de forma manual (por ejemplo, alterar el Fragment Offset, manipular las opciones de cabecera o modificar el Checksum).
• Flujo de estudio:
1. Construyes el paquete en Python/Scapy dentro de la VM emisora.
2. Capturas el tráfico con Wireshark en la interfaz virtual.
3. Inspeccionas cómo se visualizan los campos malformados en la captura .pcap y cómo responde la pila TCP/IP receptora.

──────
### 4. Análisis Pasivo de Muestras PCAP (PCAP Forensics)

Si prefieres no montar máquinas vulnerables, la forma más segura y rápida de aprender es analizar archivos de captura de paquetes (.pcap) de ataques ya documentados:

• Repositorios como el Wireshark Sample Captures Wiki o análisis de incidentes de seguridad contienen capturas de tráfico reales con ataques como FragmentSmack, SYN Floods, ARP Spoofing o Bad Neighbor.
• Te permite abrir el archivo directamente en Wireshark, ver el desglose hexadecimal, analizar los árboles de cabecera y entender exactamente qué campo violaba la especificación RFC sin necesidad de
ejecutar ningún código.
──────
### 5. Plataformas Online de Aprendizaje (CTFs y Labs)

Si buscas entornos listos para usar en la nube:

• TryHackMe: Salas como Intro to Networking, Wireshark 101, Network Security y módulos de Blue Team (Detección de intrusiones con Snort/Zeek).
• Hack The Box (Academy): Módulos enfocados en análisis de tráfico de red y seguridad en capas OSI.