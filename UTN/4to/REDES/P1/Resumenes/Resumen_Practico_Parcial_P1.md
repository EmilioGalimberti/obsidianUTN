---
tags: [redes, resumen, parcial, IPv4, subnetting, topología, UTN]
aliases: [Resumen Parcial P1, Cheat Sheet Redes]
date: 2026-05-31
---

# 📚 RESUMEN PRÁCTICO — PARCIAL REDES P1

> **Objetivo:** Tener TODO lo necesario para resolver los ejercicios del parcial en un solo lugar.
> Basado en las clases C01 a C07.

---

# 1️⃣ CONCEPTOS FUNDAMENTALES DE REDES

## Dispositivos Clave

| Dispositivo                   | Qué hace                                                                    | Capa OSI |
| ----------------------------- | --------------------------------------------------------------------------- | -------- |
| **Host**                      | Cualquier equipo que consume una IP (PC, celular, impresora, cámara)        | —        |
| **Switch (No Administrable)** | Conecta equipos en la misma LAN. Plug-and-play, no configurable             | Capa 2   |
| **Switch Administrable**      | Permite VLANs (norma 802.1Q), puertos trunk y access                        | Capa 2/3 |
| **Router**                    | Une/separa redes. Enruta paquetes entre redes usando tablas de enrutamiento | Capa 3   |
| **Access Point (AP)**         | Convierte señal de cable a WiFi. Conecta dispositivos inalámbricos a la LAN | Capa 1/2 |

## Regla de Oro: Contar Redes en una Topología

> [!tip] TIP DE PARCIAL
> **Por cada interfaz (puerto) conectada que sale de un Router → se cuenta UNA red diferente.**
> - La conexión entre dos routers = **UNA sola red** (no dos).
> - Switches en cascada sin router intermedio = **misma red**.
>   ![[{F76200E8-FC07-427C-A26A-21C337AA41BF}.png]]

### Tipos de redes
| Tipo    | Qué es                                                           |
| ------- | ---------------------------------------------------------------- |
| **LAN** | Red de Área Local — alcance ≤ 100m (hosts conectados a switches) |
| **WAN** | Conexión entre routers (enlace serial punto a punto)             |

---

## Segmentación de Redes: ¿Por qué dividir?

| Motivo                           | Descripción                                     |
| -------------------------------- | ----------------------------------------------- |
| **Seguridad (ACLs)**             | Controlar qué redes pueden comunicarse entre sí |
| **Reducir Dominio de Broadcast** | Menos "tráfico basura", más eficiencia          |

---

## VLANs (Virtual LAN) — IEEE 802.1Q

Las VLANs dividen **lógicamente** un switch para crear múltiples redes independientes usando el mismo hardware.

| Tipo de conexión    | Entre quiénes                                      | Qué lleva                        |
| ------------------- | -------------------------------------------------- | -------------------------------- |
| **Trunk (Troncal)** | Dos equipos "inteligentes" (Router ↔ Switch Admin) | Todas las VLANs **con etiqueta** |
| **Access (Acceso)** | Equipo inteligente → dispositivo final             | **Una sola VLAN**, sin etiqueta  |

> [!important] Clave
> Un switch No Administrable conectado a un puerto Access hereda automáticamente esa VLAN. Todo lo enchufado ahí pertenece a esa VLAN sin configuración.

---

# 2️⃣ DIRECCIONAMIENTO IPv4

## Estructura de una IP

```
32 bits = 4 octetos separados por puntos
Ej: 192.168.1.10 → 11000000.10101000.00000001.00001010
                        R.         R.       R.C
[ PARTE DE RED ] [ PARTE DE HOST ]
```

| Tipo de dirección | Capa   | Tamaño  | Asignación           |
| ----------------- | ------ | ------- | -------------------- |
| **IP** (lógica)   | Capa 3 | 32 bits | Por software/admin   |
| **MAC** (física)  | Capa 2 | 48 bits | De fábrica en la NIC |

---

## Tabla Maestra de Clases IPv4

```
┌───────┬──────────────┬────────────┬───────────────┬──────────┬────────────┐
│ Clase │ Rango 1° oct │ Estructura │ Máscara       │ Redes    │ Hosts/Red  │
├───────┼──────────────┼────────────┼───────────────┼──────────┼────────────┤
│   A   │    1 – 126   │  R.H.H.H   │ /8  255.0.0.0 │  126     │16.777.214  │
│   B   │  128 – 191   │  R.R.H.H   │ /16 255.255.0 │16.384    │  65.534    │
│   C   │  192 – 223   │  R.R.R.H   │ /24 255.255   │2.097.152 │   254      │
│   D   │  224 – 239   │  Multicast │       —       │  —       │    —       │
│   E   │  240 – 255   │  Reservada │       —       │  —       │    —       │
├───────┼──────────────┼────────────┼───────────────┼──────────┼────────────┤
│ Loop  │     127      │  Loopback  │       —       │ 2^n      │    2^h-2   │
│                                                                 Se restan 2:     │                                                                 dirección │
│                                                                 de red +  │
│                                                                 broadcast.│  
│
└───────┴──────────────┴────────────┴───────────────┴──────────┴────────────┘
```

### Identificación rápida de clase → **MIRAR EL PRIMER OCTETO**

(SOLO CON LA IP)

| Primer bit(s) | Clase         | Rango decimal |
| ------------- | ------------- | ------------- |
| `0xxxxxxx`    | A             | 1–126         |
| `10xxxxxx`    | B             | 128–191       |
| `110xxxxx`    | C             | 192–223       |
| `1110xxxx`    | D (multicast) | 224–239       |
| `1111xxxx`    | E (reservada) | 240–255       |

---

## Rangos de ==IPs Privadas== (RFC 1918)

| Clase | Rango Privado                     | Máscara | cuantas son? |
| ----- | --------------------------------- | ------- | ------------ |
| A     | `10.0.0.0` — `10.255.255.255`     | /8      | 1            |
| B     | `172.16.0.0` — `172.31.255.255`   | /16     |              |
| C     | `192.168.0.0` — `192.168.255.255` | /24     |              |

> Las IPs privadas **NO son enrutables en Internet**. Se necesita **NAT** para salir.

---
## ==Direcciones Especiales== (NO Asignables)

| Dirección                      | Por qué NO es asignable          |
| ------------------------------ | -------------------------------- |
| Parte de host = todo `0`       | Es la **dirección de red**       |
| Parte de host = todo `1` (255) | Es la **dirección de broadcast** |
| `127.x.x.x`                    | Rango **loopback** reservado     |
| `224.x.x.x` a `239.x.x.x`      | **Clase D** (Multicast)          |
| `240.x.x.x` a `255.x.x.x`      | **Clase E** (Reservada)          |
| Octeto > 255                   | IP **inválida**                  |
| `255.255.255.255`              | **Broadcast universal**          |

---




## Cómo Resolver: Dada una IP → Encontrar Red, Broadcast, Rango Válido

### Metodología (sin subnetting — clases naturales)

```
1. Identificar la clase → mirar 1er octeto
2. Determinar estructura → R.H.H.H / R.R.H.H / R.R.R.H
3. Dir. de Red       → parte de host = 0
4. Primera IP válida → Dir. de Red + 1 (en último octeto)
5. Broadcast         → parte de host = 255
6. Última IP válida  → Broadcast - 1
7. Máscara           → según clase
```

### Ejemplo rápido: `180.10.9.5`

```
1° octeto = 180 → Clase B → R.R.H.H
Red:           180.10.0.0
Primera válida: 180.10.0.1
Broadcast:     180.10.255.255
Última válida: 180.10.255.254
Máscara:       255.255.0.0
```

---

## Cómo Resolver: ¿Es asignable una IP?

```
1. ¿Algún octeto > 255? → INVÁLIDA
2. ¿Primer octeto = 127? → LOOPBACK (no asignable)
3. ¿Primer octeto ≥ 224? → Clase D/E (no asignable)
4. Identificar clase y estructura
5. ¿Parte de host = todo 0? → Es dirección de RED (no asignable)
6. ¿Parte de host = todo 255? → Es BROADCAST (no asignable)
7. Si nada de lo anterior → ✅ ES ASIGNABLE
```

> [!warning] Trampa común
> `30.255.0.0` → Clase A → parte de host = `255.0.0` → NO es todo `255.255.255` → **SÍ es asignable**.
> `120.0.0.255` → Clase A → parte de host = `0.0.255` → NO es `0.0.0` ni `255.255.255` → **SÍ es asignable**.

---

## Cálculo de Broadcast (método binario completo)  ==esta no entendi???==

$$\text{Broadcast} = \text{IP} \;\text{OR}\; \text{NOT(Máscara)}$$

**Atajo para máscaras "redondas":** Rellenar los octetos de host con 255.

---

# 3️⃣ ==SUBNETTING== — CÁLCULO DE SUBREDES

## Fórmulas Clave (MEMORIZAR)

```
┌─────────────────────────────────────────────────────────────────┐
│  FÓRMULAS DE SUBNETTING                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Bits a pedir prestados:    2ⁿ ≥ N_subredes                    │
│                                                                 │
│  Cantidad de subredes:      S = 2ⁿ                              │
│                                                                 │
│  Hosts válidos por subred:  H = 2ʰ - 2                          │
│     donde h = bits_host_originales - n
     este tmb se puede hacer 32-/24=h                             │
│                                                                 │
│  Total de hosts:    T = S × H = 2ⁿ × (2ʰ - 2)                  │
│                                                                 │
│  Incremento (bloque):       I = 2ʰ
   este tiene sus complicaciones, si el octeto esta cortado                            Si I > 256:  Incremento en octeto = I / 256
    o con la mascara (256-valor_máscara_octeto_interesante)
    (256-240)=16 I=16
   puede ser hasta mas facil hacerlo en binario                   │
│                                                                 │
│  Dir subred #k:    k × I   (k empieza en 0)                    │
│     (en el octeto que cambia)                                   │
│                                                                 │
│                                                                 │
│                                                                 │
│  Broadcast subred #k:    (k+1) × I - 1                          │
│                                                                 │
│  Primer host válido:     Dir_Subred + 1                         │
│  Último host válido:     Dir_Broadcast - 1                      │
│                                                                 │
│  Dir de Subred (AND):    IP AND Máscara (bit a bit)             │
│     (encontrar a qué subred pertenece una IP dada) 

    AND son todos 0 menos  1 AND 1 = 1             │
│                                                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Proceso Mental de Subnetting (Checklist del Parcial)

```
□  1. Identificar la clase por el primer octeto
□  2. Anotar máscara natural (/8, /16 o /24)
□  3. Calcular subredes necesarias (pisos×oficinas, edificios×aulas, etc.)
□  4. Resolver 2ⁿ ≥ subredes_necesarias → obtener n (mínimo entero)
□  5. Nueva máscara = máscara_natural + n bits → notación CIDR
□  6. Convertir nueva máscara a decimal (octeto afectado)
□  7. Calcular: Subredes = 2ⁿ
□  8. Calcular: h = bits_host_original - n
□  9. Calcular: Hosts/subred = 2ʰ - 2
□ 10. Calcular: Incremento = 2ʰ (si > 256, dividir por 256)
□ 11. Listar subredes incrementando según el octeto afectado
□ 12. Encontrar la subred pedida: Base + k × Incremento (k desde 0)
□ 13. Broadcast = Dir_subred + Incremento - 1
□ 14. Rango válido: [Dir_subred + 1] a [Broadcast - 1]
```

---

## ¿Cómo saber si hay subnetting?

> Si la **máscara aplicada ≠ máscara natural de la clase** → **SÍ hay subredes**.
> Bits prestados = máscara aplicada - máscara natural.
>
> Ejemplo: IP `135.58.9.23/24` → Clase B → máscara natural /16 → aplicada /24 → **hay subredes** (8 bits prestados)

---

## Ejemplo Resuelto Rápido — Clase C

**Enunciado:** Red `192.168.10.0/24`, necesito 10 subredes.

```
1. Clase C → /24 → 8 bits de host
2. 2ⁿ ≥ 10 → n=4 (2⁴=16 ✅)
3. Nueva máscara: /24 + 4 = /28 → 255.255.255.240
4. h = 8 - 4 = 4 bits de host
5. Hosts/subred = 2⁴ - 2 = 14
6. Incremento = 2⁴ = 16

Subred 0: 192.168.10.0    → rango .1 a .14   → broadcast .15
Subred 1: 192.168.10.16   → rango .17 a .30  → broadcast .31
Subred 9: 192.168.10.144  → rango .145 a .158 → broadcast .159
```

---

## Ejemplo Resuelto Rápido — Clase B

**Enunciado:** Red `172.18.0.0/16`, necesito 80 subredes.

```
1. Clase B → /16 → 16 bits de host
2. 2ⁿ ≥ 80 → n=7 (2⁷=128 ✅)
3. Nueva máscara: /16 + 7 = /23 → 255.255.254.0
4. h = 16 - 7 = 9 bits de host
5. Hosts/subred = 2⁹ - 2 = 510
6. Incremento = 2⁹ = 512 → 512/256 = 2 (en 3er octeto)

Subred 0:  172.18.0.0   → rango .0.1 a .1.254   → broadcast .1.255
Subred 1:  172.18.2.0   → rango .2.1 a .3.254   → broadcast .3.255
Subred 47: 172.18.94.0  → rango .94.1 a .95.254 → broadcast .95.255
```

---

## ==Encontrar la Subred de una IP dada (Operación AND)

**Método:** IP AND Máscara (bit a bit) = Dirección de Subred

**Ejemplo:** `100.18.15.45 /21`

```
Máscara /21 = 255.255.248.0

Octeto por octeto:
  100 AND 255 = 100
   18 AND 255 =  18
   15 AND 248 =  ?   ← calcular en binario
   45 AND   0 =   0

15  → 00001111
248 → 11111000
AND → 00001000 = 8

Subred = 100.18.8.0
Broadcast = 100.18.15.255
```

---

# 4️⃣ DISEÑO DE TOPOLOGÍA CON SUBREDES

## Metodología Completa

```
PASO 1: Relevamiento → Identificar TODAS las redes (LAN + WAN)
PASO 2: Proyección   → Aplicar % de crecimiento a futuro
PASO 3: Red mayor    → Determinar la subred que más hosts necesita
PASO 4: Calcular h   → 2^h - 2 ≥ hosts_max_con_crecimiento
PASO 5: Calcular n   → n = bits_clase - h
PASO 6: Verificar    → 2^n ≥ cantidad_subredes_necesarias
PASO 7: Máscara      → Construir la máscara de subred
PASO 8: Tabla        → Listar todas las subredes con sus rangos
PASO 9: Asignar      → Asignar subredes a cada segmento
PASO 10: IPs Routers → Gateway = primera IP usable de cada subred (.1)
```

### Reglas importantes

> [!danger] NUNCA OLVIDAR
> - **Los enlaces WAN (serial entre routers) TAMBIÉN son subredes** — cuentan al hacer el relevamiento.
> - **Switches en cascada sin router = misma subred** — no generan subredes nuevas.

### Regla de asignación de IPs a routers

| Interfaz                          | IP asignada              |
| --------------------------------- | ------------------------ |
| Ethernet (gateway LAN)            | Primera IP usable (`.1`) |
| Serial (extremo A del enlace WAN) | Primera IP usable (`.1`) |
| Serial (extremo B del enlace WAN) | Segunda IP usable (`.2`) |

---

# 5️⃣ CONCEPTOS COMPLEMENTARIOS

## Gateway (Puerta de Enlace)

- Es la **IP del router** que conecta la red local con otras redes.
- Si el destino está en **la misma red** → envío directo (no usa gateway).
- Si el destino está en **otra red** → se envía al gateway.
- Generalmente se usa la primera IP usable de la subred (`.1` o `.254`).

## NAT (Network Address Translation)

- Traduce IPs privadas ↔ IPs públicas para acceder a Internet.
- **PAT** (Port Address Translation): múltiples IPs privadas comparten una IP pública usando puertos diferentes.
- Necesario porque las IPs privadas no son enrutables en Internet.

## DHCP (Dynamic Host Configuration Protocol)

- Asigna automáticamente: IP, máscara, gateway y DNS.
- Proceso: **DORA** → Discover → Offer → Request → Acknowledge.
- Ideal para redes grandes donde la configuración manual es inviable.

## ACL (Listas de Control de Acceso)

- Reglas en el router que controlan qué redes pueden comunicarse entre sí.
- Ejemplo: "Prohibir que VLAN 20 (alumnos) acceda a los servidores".

## APIPA

- `169.254.0.0/16` → IP auto-asignada cuando no hay servidor DHCP.
- No tiene gateway → no puede salir a Internet.
- Indicador de problemas de red.

---

# 6️⃣ ==COMANDOS DE RED (Referencia Rápida)

## Linux

| Acción                      | Comando moderno (`ip`)         | Comando viejo (`ifconfig`)                         |
| --------------------------- | ------------------------------ | -------------------------------------------------- |
| Ver interfaces UP           |                                | `ifconfig`                                         |
| Ver TODAS las interfaces    |                                | `ifconfig -a`                                      |
| Habilitar interfaz          |                                | `ifconfig eth0 up`                                 |
| Asignar IP                  |                                | `ifconfig eth0 192.168.1.10 netmask 255.255.255.0` |
| Ver tabla de rutas          |                                | `route`                                            |
| Ver tabla ARP               |                                | `arp -n`                                           |
| Prueba conectividad         |                                | `ping -c 4 IP`                                     |
| Config permanente           | `nano /etc/network/interfaces` | —                                                  |
| Levantar con config archivo | `ifup eth0`                    | —                                                  |
| Config gateway              |                                | `route add default gw IP`                          |


### Archivo de configuración permanente: `/etc/network/interfaces`

```
iface eth0 inet static
   address 192.168.1.10
   netmask 255.255.255.0
```

## Windows

| Acción | Comando |
|---|---|
| Ver config IP | `ipconfig` |
| Ver config completa | `ipconfig /all` |
| Prueba conectividad | `ping IP` |
| Configurar IP (CMD) | `netsh interface ip set address "Ethernet" static IP MASK GW` |

## Mensajes de Ping

| Mensaje | Significado |
|---|---|
| `64 bytes from ...` | ✅ El host responde, hay conectividad |
| `Destination Host Unreachable` | ❌ La red existe pero el host no responde |
| `Network is unreachable` | ❌ No hay ruta hacia esa red |

---


# 8️⃣ ERRORES FRECUENTES A EVITAR

| Error                                         | Corrección                                                                                                                                    |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Asumir que las subredes empiezan desde 1      | Las subredes se numeran desde **0**                                                                                                           |
| No restar 2 al calcular hosts                 | Siempre restar 2 (dir. de red + broadcast)                                                                                                    |
| Confundir el octeto afectado en Clase B       | Los bits prestados van al **3er octeto**                                                                                                      |
| Identificar la clase por la máscara           | La clase se determina por el **primer octeto de la IP**                                                                                       |
| Asumir subredes sin verificar                 | Si máscara aplicada ≠ máscara natural → hay subredes                                                                                          |
| Asignar el Gateway a una PC                   | El **Gateway** es la IP del Router en tu red local. Sin Gateway configurado, el host tiene red local pero **no sale a otras redes/Internet**. |
| Olvidar contar los enlaces WAN como subredes  | Cada enlace serial punto a punto = 1 subred                                                                                                   |
| Confundir "todo 255" con broadcast en Clase A | En Clase A broadcast = `x.255.255.255`, no solo `.255`                                                                                        |
| No considerar proyección de crecimiento       | Multiplicar hosts × factor indicado y redondear hacia arriba                                                                                  |

---

# 9️⃣ TIPS RÁPIDOS PARA EL PARCIAL

> [!tip] Número Mágico
> **256 - valor del octeto de la máscara = Incremento**
> Ejemplo: máscara `255.255.240.0` → `256 - 240 = 16` → las subredes saltan de 16 en 16 en el 3er octeto.

> [!tip] ¿Cuándo usar AND?
> Cuando te dan **una IP con máscara** y te preguntan **a qué subred pertenece**, usá **IP AND Máscara** en el octeto que no es ni todo 1 ni todo 0 en la máscara.

> [!tip] Verificar rápido
> - La dirección de red siempre es **múltiplo del incremento**.
> - El broadcast siempre es **1 menos que la siguiente dirección de red**.

> [!tip] Protocolo de ping
> `ping` usa **ICMP** (Internet Control Message Protocol) — capa 3.

> [!tip] MTU estándar Ethernet
> **1500 bytes**

> [!tip] Configuración IP en Linux con `ifconfig` o `ip addr add`
> Es **temporal** — se pierde al reiniciar. Para que persista → editar `/etc/network/interfaces`.

---

*Resumen basado en clases C01–C07, Redes de Datos — UTN*
