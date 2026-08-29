Al analizar la carpeta REDES, se observa que el programa abarca desde la Capa 2 (Acceso al Medio y Enlace) hasta la Capa 3 (Interred, Direccionamiento y Ruteo) y principios de Capa 4/Transporte.

Cada uno de los protocolos y mecanismos presentes en tus apuntes tiene vulnerabilidades inherentes (nacidas porque muchos de estos estándares fueron diseñados originalmente para entornos de confianza sin
autenticación ni cifrado).

A continuación tienes un mapa clasificado por capa y tema, detallando qué vulnerabilidades y técnicas de ataque/defensa puedes aprender y practicar a partir de tus notas:
──────
### 1. Capa de Enlace y Conmutación (L2 / Ethernet / Switches / STP / VLANs)

Basado en: P1-U02 ~  CAPA DE ACCESO EN REDES LOCALES.md, STP.md, VLAN.md.

• MAC Flooding (Desbordamiento de tabla CAM):
  • Concepto en tus notas: Cómo el switch aprende direcciones MAC dinámicas en su tabla CAM para reenviar tramas unicast.
  • Vulnerabilidad: Si se inyectan miles de tramas con direcciones MAC de origen falsas y aleatorias, la tabla CAM del switch se llena.
  • Efecto: El switch entra en modo fail-open (se comporta como un Hub), enviando todo el tráfico en difusión (broadcast flooding), permitiendo capturar tráfico ajeno con un sniffer (Wireshark).
  • Mitigación: Port Security (limitar la cantidad de MACs permitidas por interfaz).
• Ataques al protocolo STP (Rogue Root Bridge):
  • Concepto en tus notas: Elección del Switch Raíz (Root Bridge) mediante intercambio de BPDUs con menor prioridad/Bridge ID.
  • Vulnerabilidad: Un atacante conectado a un puerto de acceso puede inyectar BPDUs falsificadas con la prioridad más baja (Priority = 0).
  • Efecto: El atacante se proclama Root Bridge, forzando a la red a recalcular la topología y redirigir los enlaces lógicos hacia su máquina (Man-in-the-Middle o DoS en Capa 2).
  • Mitigación: BPDU Guard, Root Guard.
• VLAN Hopping (Salto de VLAN):
  • Concepto en tus notas: Etiquetado 802.1Q, enlaces troncales (trunk) y VLAN Nativa.
  • Vulnerabilidad 1 (Switch Spoofing): Si el puerto del switch tiene DTP (Dynamic Trunking Protocol) habilitado por defecto, un atacante puede negociar un enlace troncal y tener visibilidad de todas
  las VLANs.
  • Vulnerabilidad 2 (Double Tagging): Inyectar una trama con doble cabecera 802.1Q donde la etiqueta externa coincide con la VLAN Nativa del enlace troncal. Al desencapsular la primera etiqueta, el
  siguiente switch procesa la etiqueta interna, saltando a otra VLAN aislada.
  • Mitigación: Desactivar DTP (switchport nonegotiate), usar puertos en modo access estricto y cambiar la VLAN nativa a una ID no utilizada.

──────
### 2. Protocolos de Resolución y Asignación (ARP & DHCP)

Basado en: P2-U03-C03 Protocolo ICMP - ARP.md, P2-C01Actividad Análisis ARP - Preguntas Diagnostico.md, P2-U03-C04- DHCP.md.

• ARP Spoofing / ARP Poisoning (Envenenamiento de tabla ARP):
  • Concepto en tus notas: ARP no tiene autenticación; cualquier host acepta ARP Replies o Gratuitous ARP sin haberlos solicitado.
  • Vulnerabilidad: Un atacante responde a una petición ARP diciendo que su dirección MAC corresponde a la IP del Router/Gateway.
  • Efecto: Interceptación de todo el tráfico saliente de la víctima (Man-in-the-Middle - MitM, robo de credenciales en protocolos sin TLS, modificación de paquetes o DoS).
  • Mitigación: Dynamic ARP Inspection (DAI) combinado con DHCP Snooping.
• DHCP Starvation & Rogue DHCP Server:
  • Concepto en tus notas: Proceso DORA (Discover, Offer, Request, Pack/Ack) y asignación de IPs desde un pool.
  • Vulnerabilidad 1 (Starvation): Inundar la red con peticiones DHCP Discover usando MACs falsas para agotar todo el pool de direcciones IP legítimo.
  • Vulnerabilidad 2 (Rogue DHCP): Levantar un servidor DHCP falso en la LAN para responder más rápido que el legítimo, asignando a los clientes un Gateway falso y servidores DNS maliciosos (DNS
  Spoofing).
  • Mitigación: DHCP Snooping (clasificar puertos de switch en confiables/no confiables).

──────
### 3. Redes Inalámbricas (WLAN / 802.11)

Basado en: IEEE 802.11.md, CSMA_CA.md.

• Ataques de Desautenticación (Deauth Flooding):
  • Concepto en tus notas: Tramas de gestión 802.11 (Beacon, Probe, Association, Deauthentication).
  • Vulnerabilidad: En WPA/WPA2 tradicional, las tramas de gestión viajan en texto plano sin firmar.
  • Efecto: Forzar la desconexión de clientes legítimos (Denegación de Servicio Wi-Fi) o forzarlos a reconectarse para capturar el 4-Way Handshake y crackear la clave WPA2 mediante ataque de
  diccionario/fuerza bruta.
  • Mitigación: WPA3 o activación de Protected Management Frames (IEEE 802.11w).
• Evil Twin & Rogue Access Point:
  • Vulnerabilidad: Crear un punto de acceso falso con el mismo SSID (y MAC clonada) que la red legítima pero con mayor potencia de señal para que los clientes se asocien a él.

──────
### 4. Capa de Red (IPv4, IPv6, ICMP, Ruteo y ACLs)

Basado en: P1-U03 CAPA DE INTERRED – DIRECCIONAMIENTO.md, P2-U03-C03 Protocolo ICMP - ARP.md, P2-U02-C02-ipv6.md, ACL.md.

• IP Spoofing & Ataques de Amplificación / Reflexión:
  • Concepto en tus notas: Las cabeceras IPv4 y datagramas UDP no verifican la autenticidad de la IP de origen.
  • Vulnerabilidad: Enviar peticiones a servicios UDP (DNS, NTP, SNMP) falsificando la IP de origen con la IP de la víctima. Las respuestas masivas son reflejadas y amplificadas hacia la víctima (DDoS).
  • Mitigación: Unicast Reverse Path Forwarding (uRPF) y filtrado BCP 38 / RFC 2827.
• Ataques basados en ICMP:
  • ICMP Redirect Attack (Tipo 5): Inyectar mensajes falsos de redirección para que una máquina cambie su tabla de rutas local y mande tráfico a través del atacante.
  • Ping of Death / Ping Flood / Smurf Attack: Saturación de ancho de banda o consumo de ciclos de CPU forzando respuestas masivas.
  • Reconocimiento y Evasión: Uso de mensajes ICMP Type 3 Code 4 (Fragmentation Needed and DF set) para manipular el Path MTU Discovery (PMTUD) o mapear topologías internas y reglas de firewall.
• Vulnerabilidades en IPv6 (NDP vs ARP y Rogue RA):
  • Concepto en tus notas: IPv6 sustituye ARP por NDP (Neighbor Discovery Protocol) y utiliza Router Advertisements (RA) para autoconfiguración SLAAC.
  • Vulnerabilidad: Envío no autenticado de Rogue Router Advertisements, asignando a los hosts una ruta por defecto falsa o saturando con prefijos inexistentes (DoS).
  • Mitigación: RA Guard y SEND (Secure Neighbor Discovery - RFC 3971).
• Fallas de Configuración en ACLs y Firewalls:
  • Concepto en tus notas: ACLs estándar vs extendidas, orden de sentencias de arriba a abajo (first match) y el deny all implícito final.
  • Vulnerabilidad: Reglas mal ordenadas que permiten el paso antes de una restricción, o filtrado stateless que no valida si un paquete TCP entrante pertenece a una conexión previamente establecida
  (ausencia de inspección de estado).

──────
### Resumen de Laboratorios y Herramientas que puedes explorar con esta base

Concepto de tu materia                            | Ataque / Vulnerabilidad a estudiar		| Herramienta de prueba / Lab                      | Mecanismo de Defensa
---------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------
ARP / MAC                                         | ARP Poisoning / CAM Overflow			| arpspoof, bettercap, macof                       | DAI, Port Security
DHCP                                              | DHCP Starvation / Rogue Server			| yersinia, dnsmasq                                | DHCP Snooping
STP / VLAN                                        | Root Bridge Hijack / VLAN Hopping		| yersinia, scapy                                  | BPDU Guard, Private VLANs
802.11 Wi-Fi                                      | Deauth Attack / Handshake Capture		| aircrack-ng, wireshark                           | WPA3, 802.11w (PMF)
ICMP / IP                                         | ICMP Redirect / IP Spoofing			| scapy, hping3                                    | uRPF, Firewall Stateful
