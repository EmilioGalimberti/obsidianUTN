---
tags:
aliases:
  - Resumen Teórico P1
  - Teoría Redes Parcial
date: 2026-05-31
---

# 📖 RESUMEN TEÓRICO — PARCIAL REDES P1

> Basado en las clases teóricas C01 – C11 (Unidades 1, 2 y 3).

---

# ═══════════════════════════════════════════
# UNIDAD 1 — ARQUITECTURA DE REDES E INTERNET
# ═══════════════════════════════════════════

---

## 1.1 Conceptos Fundamentales

### ¿Qué es una Red de Telecomunicaciones?

Un conjunto de medios, tecnologías, protocolos y facilidades diseñadas para facilitar el intercambio de información entre usuarios **distantes** (la raíz "tele" denota distancia). A diferencia de una **red informática** (dispositivos cercanos), una red de telecomunicaciones requiere atravesar nodos intermedios.

### Componentes Esenciales de una Red

| Componente | Descripción |
|---|---|
| **Dispositivos finales** | Equipos que interactúan con el usuario: PCs, servidores, impresoras, celulares |
| **Dispositivos de interconexión** | Unen dispositivos finales y dirigen el tráfico: switches, routers, módems, APs |
| **Medios de comunicación** | Canal de transmisión: **guiados** (cables) o **no guiados** (inalámbricos) |
| **Placa de red (NIC)** | Hardware que permite la conexión física al medio |
| **Sistema operativo** | Software base para que el dispositivo funcione en la red |
| **Protocolo de comunicación** | Reglas y estándares que permiten a los dispositivos interpretarse mutuamente |

---

## 1.2 Clasificación de las Redes

### Según el Área de Cobertura

| Tipo                                | Alcance               | Ejemplo                          |
| ----------------------------------- | --------------------- | -------------------------------- |
| **PAN** (Personal Area Network)     | ≈ 1 metro             | Bluetooth entre PC y periféricos |
| **LAN** (Local Area Network)        | Dentro de un edificio | Red de oficina                   |
| **MAN** (Metropolitan Area Network) | Una ciudad            | TV por cable                     |
| **WAN** (Wide Area Network)         | Países / continentes  | Conexiones entre sucursales      |
| **Internet / GAN**                  | Global                | La red mundial                   |

### Según la Tecnología de Transmisión

| Tipo | Descripción |
|---|---|
| **Redes de difusión (broadcast)** | Canal compartido; los datos se envían a varios dispositivos |
| **Redes punto a punto** | Los datos viajan directamente de un punto a otro |

### Según la Topología Física

Bus, estrella, anillo, malla, árbol.

### Según la Direccionalidad de los Datos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Símplex** | Comunicación en un único sentido | Radio |
| **Semidúplex (Half-duplex)** | Ambos sentidos, pero no simultáneo | Walkie-talkie |
| **Dúplex (Full-duplex)** | Ambos sentidos simultáneamente | Llamada telefónica |

### Otras Clasificaciones

- **Según el ancho de banda:** banda angosta vs banda ancha.
- **Según la movilidad:** redes fijas (alámbricas) vs redes móviles (inalámbricas).

---

## 1.3 Modelo de Referencia OSI

El **Modelo OSI** (Open Systems Interconnection), creado por ISO en 1980, es un marco conceptual de 7 capas para los protocolos de red. Se usa como referencia para estudiar la arquitectura TCP/IP.

### Principios de las Capas

- Cada capa **provee servicios a la capa superior** y **solicita servicios a la capa inferior**.
- La interfaz de capa es el conjunto de normas de intercomunicación entre capas adyacentes.
- La comunicación entre capas homólogas (misma capa en emisor y receptor) se realiza mediante protocolos de esa capa.
- En la práctica, la información desciende encapsulándose hasta la capa física (emisor), se transmite, y asciende desencapsulándose en el receptor.

> **Regla clave:** Un dispositivo clasificado en una capa superior **asume obligatoriamente las funciones de todas las capas inferiores**. Ejemplo: un Router (Capa 3) también realiza funciones de Capa 2 y Capa 1.

---

## 1.4 Conjunto de Protocolos TCP/IP

Surge de **DARPA** (proyecto militar de EE.UU.) que utilizó la conmutación de paquetes.

### Objetivos

- **Conectividad permanente:** redirige paquetes si cae un nodo (conmutación de paquetes).
- **Independiente del hardware y SO.**
- **Transmisión de todo tipo de información** (texto, video, música, etc.).

### Las 4 Capas del Modelo TCP/IP

```
┌──────────────────────────────────────────────────────┐
│  CAPA 4: APLICACIÓN                                  │
│  Protocolos de alto nivel (HTTP, FTP, SMTP, DNS)     │
│  No incluye sesión ni presentación                   │
├──────────────────────────────────────────────────────┤
│  CAPA 3: TRANSPORTE                                  │
│  Conexión lógica extremo a extremo                   │
│  TCP (confiable, orientado a conexión)               │
│  UDP (sin conexión, no confiable)                    │
│  PDU: Segmento                                       │
├──────────────────────────────────────────────────────┤
│  CAPA 2: INTERRED (Red)                              │
│  Direccionamiento IP, encaminamiento, fragmentación  │
│  Protocolo IP: "mejor esfuerzo", no orientado a cnx  │
│  PDU: Paquete                                        │
├──────────────────────────────────────────────────────┤
│  CAPA 1: HOST A RED (Enlace + Física)                │
│  Encapsulamiento en tramas, control de acceso,       │
│  detección de errores, direcciones MAC               │
│  PDU: Trama → Bits                                   │
└──────────────────────────────────────────────────────┘
```

### Correspondencia OSI ↔ TCP/IP

| OSI | TCP/IP | PDU |
|---|---|---|
| Capa 7, 6, 5 (Aplicación, Presentación, Sesión) | Capa 4: Aplicación | Datos |
| Capa 4 (Transporte) | Capa 3: Transporte | Segmento |
| Capa 3 (Red) | Capa 2: Interred | Paquete |
| Capa 2, 1 (Enlace, Física) | Capa 1: Host a Red | Trama / Bits |

---

## 1.5 Encapsulamiento y Desencapsulamiento

### En el Origen (Encapsulamiento — descendente)

1. **Capa de Aplicación** → genera los datos.
2. **Capa de Transporte** → segmenta y agrega cabecera TCP/UDP → **Segmento**.
3. **Capa de Interred** → agrega cabecera IP → **Paquete**.
4. **Capa Host a Red** → agrega cabecera Ethernet (MAC) + cola CRC → **Trama** → **Bits** al medio.

### En Dispositivos Intermedios (Router)

- Recibe bits (Capa 1).
- Desencapsula la trama (Capa 2), lee la MAC.
- Lee la IP destino del paquete (Capa 3) y consulta su **tabla de encaminamiento**.
- Re-encapsula con nueva trama y envía por la interfaz correspondiente.

### En el Destino (Desencapsulamiento — ascendente)

- Bits → Trama (verifica CRC; si error → descarta sin avisar) → Paquete → Segmento → Datos.

> **Ethernet es de "máximo esfuerzo":** si la trama está corrupta, se descarta SIN avisar. El protocolo TCP de capa superior se encarga de la retransmisión.

---

## 1.6 Internet ✅

### Orígenes

- **ARPA** (1958) → **ARPANET** → **DARPA** → Internet.
- Precursora de Internet, surgida del Departamento de Defensa de EE.UU.

### Características

Pública, anónima, accesible, global, crecimiento ilimitado, descentralizada, interpersonal, útil, instantánea.

### Arquitectura de Niveles (Tiers)✅

| Tier       | Descripción                                                                                                                                        | Ejemplo         |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **Tier 1** | Operadores globales, backbone de Internet. Tendido de fibra en ≥2 continentes. Todas las Tier 1 están interconectadas entre sí. No pagan tránsito. | Verizon, NTT    |
| **Tier 2** | Operadores regionales. Se conectan a Tier 1 para acceso global.<br>Brindan servicios a operadores Tier 3.                                          | British Telecom |
| **Tier 3** | ISPs que dan conexión a usuarios finales (hogares/empresas).                                                                                       | Movistar, Claro |

### Puntos Neutros (IXP)

- **IXP (Internet Exchange Point):** infraestructura física (data center) donde diferentes redes se conectan para intercambiar tráfico directamente. No pertenece a un proveedor específico.

### Tipos de Conexiones entre Operadores ✅

| Tipo | Descripción |
|---|---|
| **Tránsito** | Conecta operadores de diferente jerarquía; el mayor vende acceso |
| **Peering** | Conecta operadores de la misma jerarquía sin costo. Puede ser público (IXP) o privado |

---

## 1.7 Estandarización✅

### Tipos de Estándares

| Tipo         | Descripción                           | Ejemplo              |
| ------------ | ------------------------------------- | -------------------- |
| **De facto** | Surgen sin plan formal                | HTTP, Bluetooth      |
| **De jure**  | Adoptados por organizaciones formales | IEEE 802.3, ISO 9001 |

### Organismos Internacionales

| Organismo | Rol                                                               |
| --------- | ----------------------------------------------------------------- |
| **ITU**   | Regulación de TICs a nivel internacional (ONU)                    |
| **ISO**   | Normas técnicas (ISO 9001, modelo OSI)                            |
| **IEEE**  | Estándares eléctricos/electrónicos (802.3 Ethernet, 802.11 Wi-Fi) |
| **IETF**  | Ingeniería de Internet a corto plazo, crea estándares (RFCs)      |
| **IRTF**  | Investigación a largo plazo para evolución de Internet            |
| **IANA**  | Asigna direcciones IP y números de sistema autónomo               |

### RFC (Request for Comments)

Documento de la IETF que estandariza protocolos y prácticas para Internet. Identificado por un número único, mantenido por IANA.

---

# ═══════════════════════════════════════════
# UNIDAD 2 — CAPA DE ENLACE DE DATOS Y MEDIOS
# ═══════════════════════════════════════════

---

## 2.1 Capa de Enlace de Datos (Capa 2 OSI)

Actúa como **intermediaria** entre el mundo lógico (software) y el mundo físico (hardware). Prepara los datos para transmitirlos sobre un medio físico específico.

### Subcapas

| Subcapa | Función | Interactúa con |
|---|---|---|
| **LLC (IEEE 802.2)** | Recibe paquete de Capa 3, lo encapsula en tramas, identifica protocolo encapsulado (IPv4, IPv6) | Software (capas superiores) |
| **MAC (Control de Acceso al Medio)** | Organiza el acceso al canal, construye la estructura física de la trama. Depende del medio físico | Hardware (capa física) |

### PDU de Capa 2: la Trama

- En Capa 3 → **Paquete**
- En Capa 2 → **Trama**
- En Capa 1 → **Bits**

---

## 2.2 Métodos de Acceso al Medio

Viven en la **subcapa MAC** de la Capa 2. Organizan "quién habla y cuándo" para evitar que las señales choquen.

### Asignación Estática vs Dinámica

| Tipo | Método | Característica |
|---|---|---|
| **Estática** | FDMA, TDMA, CDMA | Se divide el canal matemáticamente. No hay competencia |
| **Dinámica (Contienda)** | CSMA/CD, CSMA/CA, Token Ring | Los dispositivos compiten por el medio |

### CSMA/CD — Ethernet Clásica (LAN Cableada)

- **Carrier Sense Multiple Access with Collision Detection.**
- El dispositivo **escucha** el canal; si está libre, transmite.
- Si dos transmiten simultáneamente → **colisión** → envían **señal de atasco** → esperan un **tiempo aleatorio** → reintentan.
- Después de **16 intentos** sin éxito → error.
- Implementado en la **NIC** y en el **Switch**.
- **No sirve para redes inalámbricas** (no pueden detectar colisiones en el aire).

### CSMA/CA — Redes Inalámbricas (Wi-Fi)

- **Carrier Sense Multiple Access with Collision Avoidance.**
- Como es imposible detectar colisiones en el aire, intenta **prevenirlas** con un intercambio de mensajes de control.

**Flujo:**
1. El emisor escucha el medio. Si está libre:
2. Envía **RTS** (Request to Send) — solicita permiso, incluye MAC origen/destino y duración estimada.
3. El receptor responde:
   - **CTS** (Clear to Send) → autoriza la recepción.
   - **RxBUSY** → receptor ocupado, el emisor espera.
4. Al recibir CTS, el emisor espera un tiempo aleatorio breve y si el medio sigue libre, **transmite DATA**.
5. El receptor envía:
   - **ACK** → datos llegaron bien.
   - **NAK** → datos con errores, se reinicia el proceso.

### Token Ring (IEEE 802.5)

- Método **determinístico** y libre de colisiones.
- Un **token** (testigo) circula por la red en anillo.
- Solo la máquina que posee el token puede transmitir.
- Si no tiene datos, lo pasa a la siguiente estación.
- Si tiene datos, convierte el token en trama (agrega datos y MACs).
- **Lento** comparado con Ethernet, pero **garantiza** que todos puedan transmitir.
- **Topología lógica:** anillo. **Topología física:** estrella (switch actúa como puente).

---

## 2.3 Estándar IEEE 802.3 (Ethernet)

### Evolución de Ethernet

| Fase | Medio | Topología | Modo | Método acceso |
|---|---|---|---|---|
| **Ethernet Clásica** | Coaxial (10Base5, 10Base2) | Bus | — | CSMA/CD |
| **Ethernet sobre UTP** | UTP (10BaseT) + Hub | Estrella | Half-Duplex | CSMA/CD |
| **Ethernet Conmutada** | UTP + Switch | Estrella | **Full-Duplex** | **No requiere CSMA/CD** |

> **El Switch elimina las colisiones**: cada puerto es un dominio de colisión independiente, y el modo Full-Duplex permite enviar y recibir simultáneamente.

### Versiones Modernas

| Tecnología              | Estándar | Velocidad | Características                                        |
| ----------------------- | -------- | --------- | ------------------------------------------------------ |
| **Fast Ethernet**       | 802.3u   | 100 Mbps  | Autonegociación, UTP Cat 5 o fibra                     |
| **Gigabit Ethernet**    | 802.3ab  | 1000 Mbps | Half (Hub) o Full (Switch), fibra multimodo/monomodo   |
| **10 Gigabit Ethernet** | 802.3ae  | 10 Gbps   | **Solo Full-Duplex**, sin hubs. Troncales y servidores |

> **Autonegociación:** los extremos acuerdan automáticamente la velocidad y modo del equipo con menores prestaciones.

---

## 2.4 Estructura de la Trama Ethernet

### Ethernet II

| Campo                        | Tamaño                              |
| ---------------------------- | ----------------------------------- |
| Preámbulo                    | 8 bytes (sincronización de relojes) |
| Dirección MAC Destino        | 6 bytes                             |
| Dirección MAC Origen         | 6 bytes                             |
| Tipo (protocolo encapsulado) | 2 bytes                             |
| Datos                        | 46–1500 bytes                       |
| FCS (CRC — verificación)     | 4 bytes                             |

> **La MAC destino va primero** intencionalmente: si no coincide con la MAC del receptor, se descarta inmediatamente sin leer el resto (optimización).

### Tamaño de la Trama

$$\text{Tama{n}o}_{Mín} = 46_{datos} + 18_{cabecera/cola} = 64 \text{ bytes}$$

$$\text{Tama{n}o}_{Máx} = 1500_{datos} + 18_{cabecera/cola} = 1518 \text{ bytes}$$

> **El relleno (padding) NO es un campo definido en la norma.** Si los datos son < 46 bytes, se rellena para alcanzar el mínimo, pero forma parte del campo "Datos".

---

## 2.5 Direccionamiento Físico: Dirección MAC ✅

- **48 bits** (6 bytes) expresados en **12 dígitos hexadecimales**.
- Grabada de fábrica en la ROM de la NIC.
- **Primeros 24 bits (OUI):** identifican al fabricante (asignado por IEEE).
- **Últimos 24 bits:** asignados por el fabricante al producto.

### Tipos de Direcciones MAC ✅

| Tipo | Descripción | En campo... |
|---|---|---|
| **Unicast** | Identifica un dispositivo único | Origen y Destino |
| **Broadcast** | FF-FF-FF-FF-FF-FF — todos los equipos del segmento | Solo Destino |
| **Multicast** | 01-00-5E-XX-XX-XX — grupo específico de dispositivos | Solo Destino |

> Una MAC de **origen** siempre es tipo **unicast**.

---

## 2.6 Dispositivos de Red

### Tabla Resumen de Dispositivos

| Dispositivo             | Capa OSI   | Impacto en Dom. Colisión         | Impacto en Dom. Broadcast |
| ----------------------- | ---------- | -------------------------------- | ------------------------- |
| **NIC** (Placa de red)  | Capa 1 y 2 | —                                | —                         |
| **Hub** (Concentrador)  | Capa 1     | Lo **extiende** (1 solo dominio) | Lo mantiene               |
| **Bridge** (Puente)     | Capa 2     | Lo **divide** (1 por puerto)     | Lo mantiene               |
| **Switch** (Conmutador) | Capa 2     | Lo **divide** (1 por puerto)     | Lo mantiene               |
| **Router** (Enrutador)  | Capa 3     | Lo divide                        | Lo **divide**             |

### NIC (Tarjeta de Interfaz de Red) ✅

- Opera en Capa 1 y Capa 2 del modelo osi.
- Cada NIC posee una MAC única (en ROM).
- Trabaja autónomamente analizando la MAC destino de las tramas entrantes.
- Detecta errores mediante CRC.
- Tipos: UTP, fibra óptica, inalámbrica (Wi-Fi).

### Hub (Concentrador) ✅

- Dispositivo de **Capa 1**, sin inteligencia.
- "Repetidor multipuerto": recibe señal por un puerto y la reenvía por **todos** los demás.
- Opera en **Half-Duplex** → requiere CSMA/CD.
- **Extiende** el dominio de colisión.

### Bridge (Puente)

- Dispositivo de **Capa 2**, inteligente.
- **Segmenta** la red dividiendo dominios de colisión.
- Maneja tabla de direcciones MAC por segmento.
- **NO divide** dominios de broadcast.
- Puede interconectar diferentes protocolos de enlace (ej. Ethernet ↔ Wi-Fi).

### Switch (Conmutador) ✅

- Dispositivo de **Capa 2**, reemplazó al Hub.
- Opera en **Full-Duplex** → no requiere CSMA/CD.
- Cada puerto = un dominio de colisión independiente.
- **NO divide** dominios de broadcast (a menos que tenga VLANs).

#### Técnicas de Conmutación ✅

| Técnica               | Funcionamiento                                        | Control de errores                               |
| --------------------- | ----------------------------------------------------- | ------------------------------------------------ |
| **Store and Forward** | Almacena trama completa antes de enviar               | Verifica CRC. Seguro pero lento                  |
| **Cut-through**       | Lee solo los primeros 6 bytes (MAC destino) y conmuta | **No** controla errores. <br>Rápido              |
| **Fragment-Free**     | Lee los primeros 64 bytes y conmuta                   | Filtra fragmentos de colisión, pero no CRC total |

#### Lógica de Aprendizaje del Switch (Tabla CAM)✅

1. Al encender, la tabla está **vacía** → actúa como hub (**inundación**).
2. **Aprende** observando la **MAC origen** de cada trama entrante → registra MAC + puerto.
3. **Conmuta** buscando la **MAC destino** en su tabla:
   - Si la conoce → envía solo por ese puerto.
   - Si NO la conoce o es broadcast → **inunda** (todos los puertos excepto el de entrada).
4. Un mismo puerto puede tener **múltiples MACs** (si hay un hub o switch conectado).
5. Las entradas tienen un **temporizador**; si la MAC no envía datos en un tiempo, se borra.

> **Regla de oro:** El switch _aprende_ por la MAC Origen. El switch _conmuta_ por la MAC Destino.

### Router (Enrutador)

- Dispositivo de **Capa 3** (pero procesa Capa 1, 2 y 3).
- Es el **único** dispositivo que divide **dominios de broadcast**.
- Cada interfaz conectada = una red/subred diferente.
- Consulta su **tabla de encaminamiento** para decidir por dónde enviar el paquete.

---

## 2.7 Redundancia, Bucles y STP

### El Problema: Bucles de Capa 2

Si se interconectan switches en malla (redundancia), una trama broadcast o desconocida se inunda infinitamente generando una **tormenta de difusión** que colapsa la red.

### La Solución: STP (Spanning Tree Protocol) — IEEE 802.1D✅

- **Objetivo:** Eliminar bucles lógicos manteniendo la redundancia física.
- Convierte una red física de malla en una **red lógica de árbol**.
- Bloquea puertos redundantes y los activa si falla el enlace principal.

#### Funcionamiento Resumido

1. **Elección del Puente Raíz (Root Bridge):** El switch con menor ID/prioridad es elegido mediante intercambio de tramas **BPDU** (cada 2 segundos).
2. **Selección de Puertos Raíz:** Cada switch determina el puerto con menor costo hacia el Puente Raíz.
3. **Bloqueo de Puertos Redundantes:** Los puertos que generarían bucles se desactivan lógicamente.
4. **Recálculo ante falla:** Si un enlace cae, STP recalcula y desbloquea puertos.

#### Costos STP (Inversamente proporcional a velocidad)

| Velocidad | Costo STP |
|---|---|
| 10 Gbps | 2 |
| 1 Gbps | 4 |
| 100 Mbps | 19 |
| 10 Mbps | 100 |

#### Estados de los Puertos STP

| Estado          | Procesa BPDU      | Aprende MAC | Envía datos |
| --------------- | ----------------- | ----------- | ----------- |
| **Bloqueo**     | Recibe (no envía) | No          | No          |
| **Escucha**     | Sí                | No          | No          |
| **Aprendizaje** | Sí                | **Sí**      | No          |
| **Envío**       | Sí                | Sí          | **Sí**      |
| **Desactivado** | No                | No          | No          |

> **Variantes:** RSTP (802.1w, convergencia más rápida), SPB (802.1aq).

---

## 2.8 Redes LAN Inalámbricas (WLAN) — IEEE 802.11

### Definición

Red de dispositivos conectados mediante **ondas electromagnéticas** (radiofrecuencia), eliminando medios físicos guiados.

| Ventajas                           | Desventajas                                |
| ---------------------------------- | ------------------------------------------ |
| Movilidad                          | Baja seguridad inherente                   |
| Reducción de costos de instalación | Susceptible a interferencias               |
| Fácil escalabilidad                | Canal compartido → ancho de banda reducido |

### Dispositivos

| Dispositivo                 | Descripción                                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Access Point (AP)**       | Capa 2. Actúa como Bridge entre red inalámbrica (802.11) y cableada (802.3). Posee IP para configuración remota |
| **Router Módem WiFi (ISR)** | Equipo hogareño integrado: AP + Switch + Router (NAT) + Servidor DHCP                                           |

### Arquitectura IEEE 802.11

| Componente                       | Descripción                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------- |
| **BSS** (Basic Service Set)      | Celda/área de cobertura de un único AP. Todos comparten el mismo SSID                    |
| **ESS** (Extended Service Set)   | Unión de varios BSS interconectados por un sistema de distribución (DS). Permite roaming |
| **Sistema de Distribución (DS)** | Red troncal (generalmente cableada) que interconecta APs                                 |
| **SSID**                         | Nombre de la red (máx. 32 caracteres)                                                    |

### Modos de Implementación

| Modo | Descripción |
|---|---|
| **Ad-hoc** | Descentralizado (peer-to-peer). Sin AP. Dispositivos se conectan directamente |
| **Infraestructura** | Centralizado. Todo el tráfico pasa obligatoriamente por el AP |

### Servicios del Sistema de Distribución

1. **Asociación:** Conexión de estación a un AP (requiere SSID + autenticación/handshake).
2. **Disociación:** Desconexión voluntaria del AP.
3. **Reasociación:** Cambio de AP (roaming) de forma transparente.
4. **Distribución:** Traslado de datos entre APs por la red troncal.
5. **Integración:** Conversión de tramas 802.11 ↔ Ethernet (función de puente).

### Confiabilidad y Mecanismos

- **Ajuste de tasa de transmisión:** disminuye si no llegan ACKs; aumenta si llegan.
- **Fragmentación:** tramas cortas tienen mayor probabilidad de llegar correctas.
- **NAV (Vector de Asignación de Red):** mecanismo de detección virtual. El emisor anuncia cuánto tiempo ocupará el canal; los demás suspenden transmisiones durante ese lapso.

### Problemas Físicos de Topología

| Problema | Descripción |
|---|---|
| **Terminal Oculta** | Dos estaciones lejanas no se escuchan entre sí → transmiten a la vez → colisión en el receptor central |
| **Terminal Expuesta** | Una estación cree que el canal está ocupado por un vecino que transmite en otra dirección → desperdicia su turno |

### Trama IEEE 802.11

- **4 campos de dirección MAC** (a diferencia de Ethernet que tiene 2):
  - DA (destino final), SA (origen), RA (AP receptor), TA (AP transmisor).
- Cabecera/cola: **34 bytes** (vs 18 de Ethernet).
- Datos: hasta **2312 bytes**.
- Campo **Duración:** usado para NAV (microsegundos).

### Estándares IEEE 802.11

| Estándar     | Banda       | Velocidad Teórica | Tecnología             |
| ------------ | ----------- | ----------------- | ---------------------- |
| **802.11a**  | 5 GHz       | 54 Mbps           | OFDM                   |
| **802.11b**  | 2.4 GHz     | 11 Mbps           | Espectro Expandido     |
| **802.11g**  | 2.4 GHz     | 54 Mbps           | OFDM                   |
| **802.11n**  | 2.4 / 5 GHz | 600 Mbps          | MIMO                   |
| **802.11ac** | 5 GHz       | 1.3 Gbps          | 8 flujos MIMO, 256 QAM |

### Seguridad Inalámbrica

| Protocolo | Características |
|---|---|
| **WEP** | RC4, 64/128 bits. Vulnerable, **no recomendado** |
| **WPA** | TKIP (claves dinámicas), servidor RADIUS |
| **WPA2** | AES (2004). Estándar actual |
| **WPA3** | Sucesor de WPA2 (2018), mejoras en seguridad |

**Métodos de autenticación:**
- **Personal (PSK):** clave precompartida, para hogares/oficinas pequeñas.
- **Enterprise:** requiere servidor RADIUS, para empresas.

### Otras Tecnologías Inalámbricas

| Tecnología | Estándar | Tipo | Alcance |
|---|---|---|---|
| **Bluetooth** | IEEE 802.15 | WPAN | Muy corto (metros) |
| **WiMax** | IEEE 802.16 | WMAN | Hasta 70 km |

---

# ═══════════════════════════════════════════
# UNIDAD 3 — DIRECCIONAMIENTO IPv4 Y SUBREDES
# ═══════════════════════════════════════════

---

## 3.1 Capa de Interred (Capa de Red)

### Funciones Principales

- **Direccionamiento:** asigna direcciones IP para lograr conectividad.
- **Encaminamiento:** routers consultan tablas de enrutamiento para dirigir paquetes.
- **Control de congestión:** evita saturación.
- **Calidad de servicio (QoS):** prioriza paquetes importantes.

### Características del Protocolo IP

- **No orientado a la conexión.**
- **Mejor esfuerzo:** no garantiza la entrega.
- Los paquetes viajan **independientemente** (pueden llegar desordenados).
- TCP compensa la falta de fiabilidad.

### ¿Dónde se ejecuta?

- En **routers**, hosts (PCs) y servidores.
- **NO en switches** (Capa 2). Un switch puede tener IP para administración, pero **nunca será Gateway**.

---

## 3.2 Direccionamiento IPv4

### Estructura

- **32 bits = 4 octetos** separados por puntos.
- Dirección **lógica** (no física), puede cambiar dinámicamente.
- Dividida en: **Parte de Red** | **Parte de Host**.

### Diferencia entre IP y MAC

| Dirección | Capa | Tamaño | Asignación | Naturaleza |
|---|---|---|---|---|
| **IP** | Capa 3 | 32 bits | Por software/admin | Lógica, jerárquica |
| **MAC** | Capa 2 | 48 bits | De fábrica (ROM) | Física, plana |

### Clases de Direcciones IPv4

| Clase        | Primer octeto | Estructura | Máscara por defecto | Redes     | Hosts/Red  |
| ------------ | ------------- | ---------- | ------------------- | --------- | ---------- |
| **A**        | 1 – 126       | R.H.H.H    | /8 (255.0.0.0)      | 126       | 16.777.214 |
| **B**        | 128 – 191     | R.R.H.H    | /16 (255.255.0.0)   | 16.384    | 65.534     |
| **C**        | 192 – 223     | R.R.R.H    | /24 (255.255.255.0) | 2.097.152 | 254        |
| **D**        | 224 – 239     | Multicast  | —                   | —         | —          |
| **E**        | 240 – 255     | Reservada  | —                   | —         | —          |
| **Loopback** | 127           | —          | —                   | —         | —          |

> **Determinación de clase:** siempre se basa en el **primer octeto** de la IP.

### Máscara de Red/Subred

La máscara identifica la parte de red de una dirección IPv4:
- Tiene **1s consecutivos** en la parte de Red y **0s consecutivos** en la parte de Host.
- Se puede expresar en notación decimal (255.255.255.0) o como prefijo (/24).
- Es **inseparable** de la dirección IP.

### Direcciones Especiales (No Asignables)

| Dirección | Motivo |
|---|---|
| Parte de host = todo `0` | **Dirección de Red** |
| Parte de host = todo `1` | **Dirección de Broadcast** |
| 127.x.x.x | Rango loopback |
| 224.x.x.x – 239.x.x.x | Clase D (Multicast) |
| 240.x.x.x – 255.x.x.x | Clase E (Reservada) |

$$\text{Hosts válidos} = 2^n - 2 \quad \text{(se restan Dir. Red + Broadcast)}$$

### Direcciones Privadas (RFC 1918)

| Clase | Rango                     | Máscara | Cantidad de redes |
| ----- | ------------------------- | ------- | ----------------- |
| A     | 10.0.0.0                  | /8      | 1                 |
| B     | 172.16.0.0– 172.31        | /16     | 16                |
| C     | 192.168.0.0 – 192.168.255 | /24     | 256               |

- **No son visibles desde Internet.**
- Necesitan **NAT** (traducción de direcciones) para acceder a Internet.
- Pueden repetirse en distintas organizaciones, pero **jamás duplicarse** dentro de una misma red.

### Direcciones Públicas

- Únicas e irrepetibles a nivel global.
- Obligatorias para tener conectividad directa en Internet.

### Parámetros de Conectividad

Para que un equipo tenga conectividad completa necesita:

1. **Dirección IP** → identificador en la red.
2. **Máscara de red** → para entender el límite de su red (con esto alcanza para una LAN).
3. **Puerta de enlace (Gateway)** → IP del router, obligatoria para salir de la red local.
4. **Servidor DNS** → traduce nombres de dominio a IPs.

---

## 3.3 Subredes (Subnetting)✅

### ¿Por qué dividir en subredes?✅

1. **Reducir dominios de broadcast** → más eficiencia.
2. **Controlar tráfico entre áreas** → segmentación lógica.
3. **Facilitar seguridad** → ACLs por subred.
4. **Optimizar tráfico** → menos "basura" circulando.

> Las subredes son **invisibles** desde fuera de la organización.

### Mecanismo: "Bits Prestados"✅

Se "piden bits prestados" de la porción de host para agregarlos a la porción de subred:
- Más subredes → menos hosts por subred.
- Siempre deben quedar **mínimo 2 bits para host** (para tener al menos 2 IPs válidas).

### Fórmulas✅

$$\text{Cantidad de subredes} = 2^n \quad (n = \text{bits prestados})$$

$$\text{Hosts válidos por subred} = 2^h - 2 \quad (h = \text{bits que quedan para host})$$

$$\text{Bits prestados} = \text{Máscara aplicada} - \text{Máscara natural de la clase}$$

### Máscara de Subred✅

- **Todos los dispositivos** de la organización comparten la **misma máscara de subred**.
- La máscara permite identificar a qué subred pertenece un dispositivo.
- Sin conocer la máscara, es **imposible** definir si una IP es de red, broadcast o host válido.

### Dirección de Subred y Broadcast✅

- **Dirección de Subred:** parte de host = todo 0. Es **reservada** (no asignable).
- **Dirección de Broadcast:** parte de host = todo 1. Es **reservada** (no asignable).
- Por cada subred creada se **pierden** 2 direcciones.

### Operación AND (Encontrar la Subred de una IP)✅

$$\text{Dirección de Subred} = \text{IP} \; \text{AND} \; \text{Máscara}$$

- Se compara bit a bit: `1 AND 1 = 1`, `0 AND X = 0`.
- En la porción de red/subred (donde la máscara tiene 1s), se copian los bits de la IP.
- En la porción de host (donde la máscara tiene 0s), todos los bits quedan en 0.

### Subnetting en Clase B✅

- Máscara por defecto: /16 → 16 bits para host.
- Los bits prestados afectan el **3er y/o 4to octeto**.
- Máximo: 14 bits prestados (quedan 2 para host → enlace punto a punto).

> **Error típico:** Al calcular rangos en Clase B, los alumnos olvidan que deben variar AMBOS octetos de host (3° y 4°), no solo el último.

### Reglas Fundamentales ✅

- Todas las máquinas de un área deben pertenecer a la **misma subred**.
- Comparten la **misma máscara** y el **mismo Gateway**.
- Sin Gateway configurado → solo hay conectividad local.
- El **router no necesita Gateway** (su función nativa ya es enrutar).
- La primera IP válida del rango suele asignarse al **Gateway** (convención).
- Una IP de la subred que se asigne al Gateway **resta 1 host** disponible.

---

## 3.4 VLANs (Virtual LAN) — IEEE 802.1Q

### Problema

Empleados de distintos departamentos mezclados físicamente en el mismo switch → comparten dominio de broadcast → ineficiencia y falta de seguridad.

### Solución: VLANs

Crean **redes lógicas separadas** sobre una misma topología física.

### Características

- Agrupan empleados **lógicamente**, independientemente de su ubicación física.
- Cada VLAN = un **dominio de broadcast** separado.
- Cada VLAN debe tener una **subred diferente**.
- Requieren **Switch Administrable** (no funcionan en switches genéricos).
- Para comunicar VLANs diferentes es **obligatorio un Router** (o Switch Layer 3).

### Tipos de Enlaces

| Tipo | Entre quiénes | Qué transporta |
|---|---|---|
| **Access (Acceso)** | Switch → dispositivo final | Una sola VLAN, sin etiqueta |
| **Trunk (Troncal)** | Switch ↔ Switch o Switch ↔ Router | Todas las VLANs, **con etiqueta 802.1Q** |

### Protocolo IEEE 802.1Q

Inyecta una **etiqueta de 4 bytes** (32 bits) en la trama Ethernet, entre la MAC origen y el campo Tipo/Longitud.

| Campo | Tamaño | Función |
|---|---|---|
| Tipo | 16 bits | Valor constante 0x8100 |
| Prioridad | 3 bits | Priorizar tráfico (ej. VoIP) |
| CFI | 1 bit | Formato canónico (histórico, en desuso) |
| **VLAN ID** | **12 bits** | Identifica la VLAN → hasta **4096 VLANs** (2^12) |

> **Solo los switches** agregan y quitan las etiquetas. Las PCs envían/reciben tramas Ethernet estándar sin etiqueta.

### Tipos de Implementación

| Tipo | Asignación | Ventaja / Desventaja |
|---|---|---|
| **VLAN Estática** | Basada en el **puerto** (manual) | Sencilla, pero rígida. Si el usuario cambia de boca sin avisar → pierde conectividad |
| **VLAN Dinámica** | Basada en **MAC o usuario** (servidor VMPS) | Flexible (ideal para grandes empresas), pero requiere servidor de BD |

---

## 3.5 Agotamiento de IPv4 y Soluciones

### Causas

- Crecimiento exponencial de Internet.
- Asignación **Classful** (se entregaban clases enteras sin importar la necesidad real).
- Ejemplo de derroche: empresa con 500 PCs recibía una Clase B (65.534 IPs) → 65.034 desperdiciadas.

### Soluciones

| Solución | Descripción |
|---|---|
| **Direccionamiento Privado (RFC 1918)** | IPs no enrutables en Internet, uso interno |
| **NAT** | Traducción de IP privada ↔ pública en el router |
| **CIDR** | Asignación sin clases, por cantidad de hosts necesarios |
| **VLSM** | Máscaras de subred de longitud variable |
| **IPv6** | Nuevo protocolo con espacio de direcciones enormemente mayor |

### NAT (Network Address Translation)

- El router traduce la IP privada (origen) por la IP pública al salir a Internet.
- Al volver, traduce la IP pública (destino) por la IP privada.
- Mantiene tablas de traducción.
- **Cuello de botella:** el proceso es computacionalmente lento.
- **No se necesita NAT** para comunicación interna entre redes privadas.

### Administración de IPs Públicas

| Organismo | Función |
|---|---|
| **IANA** | Autoridad mundial, distribuye grandes bloques a los RIR |
| **RIR** (ej. LACNIC) | Registros regionales, distribuyen a los ISP |
| **ISP** | Proveedores que asignan IPs a empresas/usuarios |

---

## 3.6 CIDR (Classless Inter-Domain Routing)

### Concepto

Elimina el concepto de clases y asigna direcciones en bloques de **tamaño variable** basándose en la **cantidad de hosts necesarios**.

### Objetivos

- Distribuir IPs públicas no asignadas **geográficamente** (los routers leen menos bits).
- Reducir el tamaño de las tablas de enrutamiento.
- Asignar bloques de tamaño variable.
- Permitir **sumarización de rutas** (supernetting).

### Ejemplo de CIDR vs Classful

| Necesidad | Classful (antiguo) | CIDR (actual) |
|---|---|---|
| 100 IPs | Clase C (254 IPs) → derroche 154 | /25 → 126 IPs → derroche mínimo |
| 500 IPs | ¡Clase B (65.534 IPs)! → derroche masivo | /23 → 510 IPs (= 2 Clase C consecutivas) |
| 1000 IPs | Clase B → derroche | /22 → 1022 IPs (= 4 Clase C consecutivas) |

---

## 3.7 Sumarización de Rutas (Supernetting)

### Concepto

Proceso inverso al subnetting: la máscara se **acorta** (se desplaza a la izquierda), agrupando múltiples redes bajo una sola dirección de resumen.

| Técnica | Máscara | Efecto en tabla del router |
|---|---|---|
| **Subnetting** | Se alarga (→ derecha) | Aumenta renglones (rutas específicas) |
| **Supernetting** | Se acorta (→ izquierda) | Reduce renglones (resume rutas) |

### Algoritmo de Cálculo

1. Identificar las direcciones a resumir.
2. Ubicar el octeto conflictivo (el que cambia).
3. Pasar a binario y comparar bit a bit de izquierda a derecha.
4. **Cortar** donde los bits dejan de coincidir.
5. Los bits coincidentes → definen la nueva máscara.
6. Los bits a la derecha del corte → se ponen en 0.

### Ejemplo

Redes: `201.3.38.0/24`, `201.3.40.0/24`, `201.3.42.0/24`

```
38 → 0010 0110
40 → 0010 1000
42 → 0010 1010
         ^^^^ coinciden 4 bits del 3er octeto

Bits coincidentes totales: 8+8+4 = 20 → /20
Octeto resultante: 00100000 = 32

Ruta sumarizada: 201.3.32.0 /20
```

> A medida que nos acercamos a la troncal de Internet, **la máscara se va reduciendo** (de /24 a /20 a /17...), lo que permite a los routers centrales procesar paquetes más rápidamente.

---

## 3.8 VLSM (Variable Length Subnet Masking) ✅

### Problema del Subnetting Tradicional

Todas las subredes heredan la **misma máscara** → mismo tamaño → derroche en enlaces con pocos hosts.

### Solución: VLSM

Permite crear **subredes dentro de subredes** con **máscaras de diferente longitud**:
- Máscaras largas (ej. /30) → pocos hosts (enlaces punto a punto).
- Máscaras cortas (ej. /26) → muchos hosts.

> VLSM se usa con **IPs públicas**. Con IPs privadas no hay restricción de espacio.

### Comparativa

| Característica | Subnetting Tradicional | VLSM |
|---|---|---|
| Máscara | Fija (todas iguales) | Variable (cada subred tiene la suya) |
| Capacidad de hosts | Idéntica en todas | Ajustada a la necesidad |
| Derroche | Altísimo | Nulo o mínimo |

### Metodología de Cálculo VLSM

> **Regla de Oro:** Siempre ordenar los requerimientos de **mayor a menor** cantidad de hosts.

1. Determinar requerimientos de hosts por área (ordenar de mayor a menor).
2. Calcular el espacio total disponible.
3. Para el requerimiento mayor: calcular bits de host necesarios → definir máscara → dividir.
4. Asignar bloques a las áreas grandes.
5. Para requerimientos menores: tomar un bloque libre y **subdividirlo** alargando la máscara.
6. Repetir hasta asignar todas las áreas.

### Ejemplo

Red `201.3.6.0/24`, requerimientos: 50, 45, 25, 25, 10, 2 hosts.

```
1. 50 y 45 hosts → necesitan 6 bits (2⁶-2=62) → /26
   Se divide /24 en 4 bloques /26:
   - 201.3.6.0/26   → Área 50 hosts
   - 201.3.6.64/26  → Área 45 hosts
   - 201.3.6.128/26 → disponible para subdividir
   - 201.3.6.192/26 → disponible para subdividir

2. 25 y 25 hosts → necesitan 5 bits (2⁵-2=30) → /27
   Se subdivide el bloque 201.3.6.128/26 en 2 sub-bloques /27:
   - 201.3.6.128/27 → Área 25 hosts
   - 201.3.6.160/27 → Área 25 hosts

3. 10 hosts → necesitan 4 bits (2⁴-2=14) → /28
   Se subdivide el bloque 201.3.6.192/26:
   - 201.3.6.192/28 → Área 10 hosts

4. 2 hosts → necesitan 2 bits (2²-2=2) → /30
   Se subdivide un sub-bloque restante:
   - 201.3.6.208/30 → Enlace punto a punto
```

> La máscara **/30** es la más larga posible (2 hosts). Con /31 no se pueden direccionar hosts.

---

# ═══════════════════════════════════════════
# CONCEPTOS TRANSVERSALES Y TRAMPAS DE PARCIAL
# ═══════════════════════════════════════════

---

## Dominios de Colisión vs Broadcast

| Concepto                 | Qué es                                                        | Quién lo divide               |
| ------------------------ | ------------------------------------------------------------- | ----------------------------- |
| **Dominio de Colisión**  | Segmento físico donde las señales pueden chocar               | Switch (1 por puerto), Router |
| **Dominio de Broadcast** | Área lógica donde los dispositivos reciben difusiones masivas | **Solo el Router**            |

> **Hub** → extiende el dominio de colisión.
> **Switch/Bridge** → divide el de colisión, pero NO el de broadcast.
> **Router** → divide AMBOS.

---

## Trampas de Parcial Frecuentes

| Trampa                                                | Corrección                                                                   |
| ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| Un dispositivo de Capa 3 solo opera en Capa 3         | Opera en Capa 3 **Y todas las inferiores** (2 y 1)                           |
| El relleno (padding) es un campo de la trama Ethernet | **NO está definido como campo.** Es parte de Datos                           |
| Las PCs leen las etiquetas 802.1Q                     | **Solo los switches** las inyectan y retiran                                 |
| Un switch asigna una IP como Gateway                  | Un switch puede tener IP (administración) pero **nunca será Gateway**        |
| Última IP válida Clase A termina en .254              | Clase A R.H.H.H → última válida = x.**255.255.254**                          |
| CSMA/CD funciona en redes inalámbricas                | CSMA/CD es solo para redes **cableadas**; en Wi-Fi se usa CSMA/CA            |
| El switch tiene un solo MAC por puerto                | Un puerto puede tener **múltiples MACs** (si hay hub/switch conectado)       |
| En VLAN estática, cambiar de boca es transparente     | Si cambia de boca → asume otra VLAN → IP incompatible → **sin conectividad** |
| La trama 802.11 tiene 2 direcciones MAC               | Tiene **4**: DA, SA, RA, TA                                                  |
| Subnetting aprovecha mejor las IPs                    | No: por cada subred se pierden 2 IPs (red + broadcast)                       |

---

## Fórmulas Clave (Resumen Final)

| Concepto                   | Fórmula                                         |
| -------------------------- | ----------------------------------------------- |
| Hosts válidos              | $2^h - 2$                                       |
| Cantidad de subredes       | $2^n$                                           |
| Bits prestados             | Máscara aplicada − Máscara natural              |
| Dirección de subred        | IP AND Máscara                                  |
| Incremento/Bloque          | $2^h$                                           |
| Broadcast de subred k      | $(k+1) \times \text{Incremento} - 1$            |
| Número mágico              | $256 - \text{valor máscara octeto interesante}$ |
| Tamaño mín. trama Ethernet | 64 bytes (46 datos + 18 cab/cola)               |
| Tamaño máx. trama Ethernet | 1518 bytes (1500 datos + 18 cab/cola)           |
| VLANs posibles (802.1Q)    | $2^{12} = 4096$                                 |
| Costo STP                  | Inversamente proporcional a velocidad           |

---

*Resumen basado en clases teóricas C01–C11, Redes de Datos — UTN*
