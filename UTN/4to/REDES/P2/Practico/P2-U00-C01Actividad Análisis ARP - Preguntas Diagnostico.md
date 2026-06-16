# Redes de Datos — Actividad de Análisis de ARP
## Preguntas Diagnóstico

> **Cátedra:** Redes de Datos  
> **Archivo original:** `P2-U00-C01Actividad Análisis ARP - Preguntas Diagnostico.pdf`  
> **Autor del enunciado:** Ing. Ciceri, Leonardo — Versión 1.0 (Junio 2025)

---

## Teoría previa: ¿Qué es ARP?

### Address Resolution Protocol (ARP) — RFC 826

**ARP** (Address Resolution Protocol) es un protocolo de la capa de enlace de datos (Capa 2 / Capa 3 frontera) que permite **traducir direcciones IP (Capa 3) a direcciones MAC (Capa 2)**.

### ¿Por qué existe ARP?

En una red Ethernet, los frames se entregan usando **direcciones MAC** (físicas). Sin embargo, las aplicaciones y protocolos superiores (como IP) usan **direcciones lógicas (IP)**. ARP actúa como el "traductor" entre ambos mundos.

```
┌──────────────────────────────────────────────────┐
│  Capa 3 (Red)    → Dirección IP   → 192.168.1.10 │
│                         ↕  ARP                    │
│  Capa 2 (Enlace) → Dirección MAC → AA:BB:CC:DD:EE:FF │
└──────────────────────────────────────────────────┘
```

### Funcionamiento de ARP paso a paso

1. **PC_A quiere enviar un paquete a PC_B** (misma red).
2. PC_A revisa su **tabla ARP** (caché local). Si no hay entrada para la IP de PC_B:
3. PC_A envía un **ARP Request** (broadcast):
   - Destino MAC: `FF:FF:FF:FF:FF:FF` (broadcast Ethernet)
   - Mensaje: *"¿Quién tiene la IP X.X.X.X? Díganle a Y.Y.Y.Y"*
4. **Todos los dispositivos en la misma red** reciben el broadcast.
5. Solo el dispositivo con esa IP responde con un **ARP Reply** (unicast):
   - Mensaje: *"Yo tengo esa IP, mi MAC es AA:BB:CC:DD:EE:FF"*
6. PC_A guarda la relación `IP → MAC` en su **tabla ARP** (caché).
7. El frame se envía directamente al MAC de PC_B.

### Tabla ARP (ARP Cache)

La tabla ARP es una **memoria temporal** que guarda las asociaciones `IP ↔ MAC` aprendidas recientemente.

| Campo | Descripción |
|-------|-------------|
| **IP Address** | Dirección lógica del dispositivo |
| **MAC Address** | Dirección física (hardware) del dispositivo |
| **Type** | `dynamic` (aprendido por ARP) o `static` (configurado manualmente) |
| **TTL / Age** | Tiempo de vida de la entrada (generalmente ~20 minutos) |

### Comando para ver la tabla ARP

```bash
# Windows
arp -a

# Linux / Mac
arp -n
# o también:
ip neigh show
```

### ARP y el router (Gateway)

> ⚠️ **Regla fundamental:** ARP solo funciona dentro de la **misma subred/segmento de red**.

Cuando una PC quiere comunicarse con un equipo en **otra red** (diferente subred):
- La PC **no envía ARP por la IP destino** remota.
- En cambio, envía ARP por la IP del **Gateway (router)**.
- El router reenvía el paquete hacia la red destino.

```
PC Cliente 1                 Router (Gateway)              Servidor (otra red)
192.168.1.10   ──ARP──►   192.168.1.1  /  10.0.0.1   ──────►   10.0.0.50
               "¿MAC del               
                gateway?"              
```

---

## Topología asumida

```
         RED LAN: 192.168.1.0/24
┌─────────────────────────────────────┐
│                                     │
│  [PC Cliente 1]   [PC Cliente 3]   │
│  192.168.1.10     192.168.1.30     │
│                                     │
│          [Router/Gateway]           │
│          192.168.1.1 (LAN)          │
│          10.0.0.1    (WAN)          │
└────────────────┬────────────────────┘
                 │
         RED WAN: 10.0.0.0/24
                 │
           [Servidor]
           10.0.0.50
```

> *Nota: La topología exacta puede variar según el archivo de simulación (.pkt de Packet Tracer), pero las respuestas aplican a cualquier topología con clientes en una LAN y un servidor en otra subred.*

---

## Respuestas a las Preguntas

---

### Pregunta 1

**Al prender la PC Cliente 1: ¿Qué comando utilizó para ver la tabla ARP del equipo y qué registros puede ver en la máquina? ¿Por qué?**

#### Comando utilizado

```bash
arp -a
```

En Cisco Packet Tracer, dentro de la terminal de la PC:
```
C:\> arp -a
```

#### Respuesta: ¿Qué registros se ven?

**Al encender la PC por primera vez (sin haber hecho ninguna comunicación), la tabla ARP estará vacía.**

```
C:\> arp -a
No ARP Entries Found.
```

#### ¿Por qué está vacía?

La tabla ARP es una **caché dinámica** que se construye **a medida que la PC se comunica** con otros dispositivos. El proceso es el siguiente:

1. Al prender la PC, no ha enviado ni recibido ningún paquete todavía.
2. No ha necesitado resolver ninguna dirección IP a MAC.
3. Por lo tanto, **ninguna entrada ha sido aprendida** aún.
4. La tabla ARP comienza vacía y se va llenando progresivamente cuando la PC genera tráfico.

> **Excepción posible:** Si el sistema operativo realiza automáticamente una comunicación al arrancar (como consultar al servidor DHCP, hacer un ping al gateway, etc.), podría aparecer alguna entrada. En simuladores como Packet Tracer, por defecto la tabla estará vacía hasta que el usuario genere tráfico manualmente.

**Conclusión:** La tabla ARP vacía al inicio es el comportamiento esperado y correcto, ya que no hay comunicaciones previas que hayan generado resoluciones ARP.

---

### Pregunta 2

**Al hacer ping desde la PC Cliente 1 hacia la PC Cliente 3, ¿Qué registro nota en la tabla ARP?**

#### Paso a paso del proceso

**Suponiendo:** PC Cliente 1 = `192.168.1.10`, PC Cliente 3 = `192.168.1.30` (misma subred LAN).

```
C:\> ping 192.168.1.30
```

**¿Qué sucede internamente?**

```
Paso 1: PC Cliente 1 verifica que 192.168.1.30 está en su misma red
        → Máscara /24: 192.168.1.X → misma subred ✓

Paso 2: Consulta su tabla ARP → No encuentra la MAC de 192.168.1.30

Paso 3: Envía ARP Request (broadcast):
        Origen IP:  192.168.1.10
        Origen MAC: AA:AA:AA:AA:AA:AA
        Destino IP: 192.168.1.30
        Destino MAC: FF:FF:FF:FF:FF:FF  ← broadcast

Paso 4: PC Cliente 3 responde con ARP Reply (unicast):
        Origen IP:  192.168.1.30
        Origen MAC: BB:BB:BB:BB:BB:BB
        Destino MAC: AA:AA:AA:AA:AA:AA

Paso 5: PC Cliente 1 guarda en su tabla ARP:
        192.168.1.30 → BB:BB:BB:BB:BB:BB

Paso 6: PC Cliente 1 envía los paquetes ICMP (ping) directamente a BB:BB:BB:BB:BB:BB
```

#### Registro en la tabla ARP después del ping

```
C:\> arp -a

Internet Address    Physical Address    Type
192.168.1.30        BB-BB-BB-BB-BB-BB   dynamic
```

#### ¿Por qué solo aparece la MAC de PC Cliente 3 y no otras?

- La comunicación fue **directa entre dos equipos de la misma LAN**.
- No fue necesario pasar por el router/gateway.
- **Solo se aprende la MAC del dispositivo con quien se comunica directamente**.
- ARP solo registra los dispositivos que responden a sus requests.

> **Dato extra:** PC Cliente 3 también aprende la MAC de PC Cliente 1 al recibir el ARP Request, ya que el request contiene la IP y MAC del solicitante. Así que en PC Cliente 3 también quedará una entrada para 192.168.1.10.

---

### Pregunta 3

**Al hacer ping desde la PC Cliente 1 hacia el equipo Servidor, ¿Qué registro nota en la tabla ARP?**

#### Paso a paso del proceso

**Suponiendo:** PC Cliente 1 = `192.168.1.10/24`, Servidor = `10.0.0.50/24` (diferente subred), Gateway = `192.168.1.1`.

```
C:\> ping 10.0.0.50
```

**¿Qué sucede internamente?**

```
Paso 1: PC Cliente 1 verifica que 10.0.0.50 NO está en su misma red
        → Máscara /24: 192.168.1.X ≠ 10.0.0.X → red diferente ✗

Paso 2: PC Cliente 1 sabe que debe enviar el paquete al GATEWAY (192.168.1.1)

Paso 3: Consulta su tabla ARP → No encuentra la MAC de 192.168.1.1 (gateway)

Paso 4: Envía ARP Request (broadcast) por la MAC del GATEWAY:
        "¿Quién tiene 192.168.1.1? Díganle a 192.168.1.10"

Paso 5: El Router responde con ARP Reply con su MAC:
        192.168.1.1 → CC:CC:CC:CC:CC:CC

Paso 6: PC Cliente 1 guarda en su tabla ARP:
        192.168.1.1 → CC:CC:CC:CC:CC:CC  ← MAC del GATEWAY (NO del servidor)

Paso 7: PC Cliente 1 envía el paquete IP encapsulado en un frame Ethernet:
        IP destino:   10.0.0.50          ← IP del servidor
        MAC destino:  CC:CC:CC:CC:CC:CC  ← MAC del GATEWAY

Paso 8: El Router recibe el frame, lo desencapsula,
        ve el IP destino 10.0.0.50 y lo reenvía hacia la red 10.0.0.0/24
```

#### Registro en la tabla ARP después del ping al Servidor

```
C:\> arp -a

Internet Address    Physical Address    Type
192.168.1.1         CC-CC-CC-CC-CC-CC   dynamic   ← MAC del GATEWAY (router)
```

> ⚠️ **Punto clave:** La tabla ARP de PC Cliente 1 **NO registra la MAC del Servidor** (10.0.0.50).  
> Registra únicamente la MAC del **router/gateway** (192.168.1.1), porque ese es el dispositivo de Capa 2 con quien se comunica directamente.

#### ¿Por qué se registra la MAC del gateway y no la del servidor?

| Concepto | Explicación |
|----------|-------------|
| **ARP es de Capa 2** | Solo funciona dentro del mismo segmento de red (broadcast domain) |
| **IP destino vs MAC destino** | El paquete IP lleva la IP del servidor, pero el frame Ethernet lleva la MAC del gateway |
| **El router hace de intermediario** | Recibe el frame, lo desencapsula, y reenvía el paquete IP hacia la red del servidor |
| **Cada salto resuelve su propio ARP** | El router hará su propio ARP Request en la red 10.0.0.0/24 para encontrar al servidor |

---

### Pregunta 4

**Si la PC Cliente 1 se comunica con todos los equipos de la topología. ¿Registra las MAC de todos ellos? ¿Por qué?**

#### Respuesta: NO, no registra las MAC de todos los equipos.

#### ¿Qué MACs SÍ registra?

| Equipo | IP | ¿Registra su MAC? | Motivo |
|--------|----|--------------------|--------|
| PC Cliente 3 | 192.168.1.30 | ✅ **SÍ** | Misma subred → ARP directo |
| Router (Gateway) | 192.168.1.1 | ✅ **SÍ** | Necesita la MAC del gateway para salir de la red |
| Servidor | 10.0.0.50 | ❌ **NO** | Distinta subred → ARP solo llega al gateway |
| Otros dispositivos misma LAN | 192.168.1.X | ✅ **SÍ** | Misma subred → ARP directo |
| Dispositivos en redes remotas | X.X.X.X | ❌ **NO** | No accesibles por ARP directo |

#### Explicación detallada

**Regla fundamental de ARP:**

> ARP opera exclusivamente dentro del **mismo dominio de broadcast** (misma subred). Los routers **no reenvían broadcasts ARP** hacia otras redes.

**Caso 1: Comunicación con equipos en la MISMA LAN**
```
PC Cliente 1 ──ARP broadcast──► [toda la LAN 192.168.1.0/24]
              ◄─ARP reply──────  PC Cliente 3
Resultado: Aprende MAC de PC Cliente 3 ✅
```

**Caso 2: Comunicación con equipos en OTRA red (Servidor)**
```
PC Cliente 1 ──ARP broadcast──► [toda la LAN 192.168.1.0/24]
              ◄─ARP reply──────  Router (gateway)
Resultado: Aprende MAC del Router ✅  (NO la del Servidor ❌)

El router reenvía el paquete, pero PC Cliente 1
nunca "ve" la MAC del servidor.
```

#### Diagrama visual del comportamiento ARP

```
                   LAN: 192.168.1.0/24
    ┌──────────────────────────────────────────┐
    │                                          │
    │  [PC C1]────────────────────[PC C3]     │
    │  .10    ←─ ARP directo ──►  .30         │
    │    │                                     │
    │  [Router/GW 192.168.1.1]                │
    │    ↑                                     │
    │  ARP Request de C1                       │
    └────┼─────────────────────────────────────┘
         │
         │ (el router NO reenvía el ARP broadcast)
         │
    ┌────┼─────────────────────────────────────┐
    │    │    WAN: 10.0.0.0/24                  │
    │  [Router/GW 10.0.0.1]                   │
    │    └───ARP propio──►[Servidor 10.0.0.50] │
    └──────────────────────────────────────────┘

Tabla ARP de PC Cliente 1 al final:
  192.168.1.30 → MAC de PC C3     ✅
  192.168.1.1  → MAC del Gateway  ✅
  10.0.0.50    → ??? (no registra) ❌
```

#### ¿Por qué los routers no reenvían broadcasts ARP?

1. **Diseño deliberado:** Si los routers reenviaran broadcasts, una sola red con miles de dispositivos inundaría con ARP Requests toda Internet.
2. **Escalabilidad:** Dividir la red en subredes y segmentar los dominios de broadcast es esencial para el funcionamiento de Internet a escala.
3. **Principio de capas:** ARP es un protocolo de Capa 2/3; los routers operan en Capa 3 y terminan los dominios de broadcast de Capa 2.

---

## Resumen de lo visto

### Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| **ARP** | Protocolo que resuelve IPs a MACs dentro de una misma red |
| **ARP Request** | Mensaje broadcast: *"¿Quién tiene esta IP?"* |
| **ARP Reply** | Respuesta unicast: *"Yo la tengo, mi MAC es..."* |
| **Tabla ARP** | Caché local que almacena relaciones IP↔MAC aprendidas |
| **Dominio de broadcast** | Segmento de red donde los broadcasts llegan a todos |
| **Gateway** | Router que conecta la LAN con otras redes; su MAC se aprende por ARP |
| **Entrada dinámica** | Entrada ARP aprendida automáticamente (expira con el tiempo) |
| **Entrada estática** | Entrada ARP configurada manualmente (no expira) |

### Comportamiento de la tabla ARP según el destino

```
Destino en la MISMA red → ARP directo → Se aprende MAC del destino
Destino en OTRA red     → ARP al GW   → Se aprende MAC del Gateway (NO del destino)
```

---

## Resumen de Fórmulas y Comandos

### Comandos ARP

| Comando | Sistema | Función |
|---------|---------|---------|
| `arp -a` | Windows / Linux | Muestra la tabla ARP completa |
| `arp -n` | Linux | Muestra la tabla ARP sin resolver hostnames |
| `arp -d *` | Windows | Borra todas las entradas ARP dinámicas |
| `arp -d <IP>` | Windows/Linux | Borra una entrada ARP específica |
| `arp -s <IP> <MAC>` | Windows/Linux | Agrega una entrada ARP estática |
| `ip neigh show` | Linux moderno | Muestra la tabla ARP (equivalente moderno) |

### Lógica de decisión ARP

$$
\text{Si } (IP_{destino} \text{ AND } Mascara) = (IP_{origen} \text{ AND } Mascara)
$$
$$
\Rightarrow \text{ARP directo al destino (aprende MAC del destino)}
$$
$$
\text{Si } (IP_{destino} \text{ AND } Mascara) \neq (IP_{origen} \text{ AND } Mascara)
$$
$$
\Rightarrow \text{ARP al Gateway (aprende MAC del gateway)}
$$

### Ejemplo numérico de verificación de subred

```
PC Cliente 1:  192.168.1.10  /24  →  Red: 192.168.1.0
PC Cliente 3:  192.168.1.30  /24  →  Red: 192.168.1.0
Servidor:      10.0.0.50     /24  →  Red: 10.0.0.0

PC C1 → PC C3:   192.168.1.0 == 192.168.1.0  → MISMA RED  → ARP directo ✅
PC C1 → Servidor: 192.168.1.0 ≠ 10.0.0.0    → RED REMOTA → ARP al GW  ✅
```

### Estructura de un frame ARP

| Campo | Tamaño | Descripción |
|-------|--------|-------------|
| Hardware Type | 2 bytes | Tipo de red (1 = Ethernet) |
| Protocol Type | 2 bytes | Protocolo (0x0800 = IPv4) |
| Hardware Size | 1 byte | Longitud de MAC (6 bytes) |
| Protocol Size | 1 byte | Longitud de IP (4 bytes) |
| Opcode | 2 bytes | 1 = Request, 2 = Reply |
| Sender MAC | 6 bytes | MAC del emisor |
| Sender IP | 4 bytes | IP del emisor |
| Target MAC | 6 bytes | MAC del destino (00:00... en request) |
| Target IP | 4 bytes | IP del destino |

### Ciclo de vida de una entrada ARP

```
Nueva comunicación
       │
       ▼
[Tabla ARP vacía?] ──SÍ──► ARP Request (broadcast)
       │                          │
       NO                         ▼
       │                   ARP Reply (unicast)
       ▼                          │
[Usar MAC en caché]               ▼
                         [Guardar IP→MAC en tabla]
                                  │
                                  ▼
                         [Usar entry hasta que expire]
                                  │
                                  ▼
                         [Entrada expira (≈20 min)]
                                  │
                                  ▼
                         [Eliminar de la caché → volver a inicio]
```

---

*Documento generado como complemento de estudio para la actividad de análisis ARP — Redes de Datos, UTN.*
