![[P1-U00-P04-Configuracion IPv4 en WIN-LINUX_v2.pdf]]

# 🌐 Configuración de Dirección IPv4 en Windows y Linux

> **Materia:** Redes de Datos · UTN  
> **Práctica:** P04 · Unidad 0  
> **Escenario:** Laboratorio de sistemas — red `192.168.1.0/24`

---

## 📋 Cuadro Resumen General

### 🐧 Comandos Linux

| Comando                                |                                   | Descripción                                 |
| -------------------------------------- | --------------------------------- | ------------------------------------------- |
| `ifconfig`                             | ip a show o ip link               | Muestra interfaces de red en estado **UP**  |
| `ifconfig eth0 up`                     | `ip link set eth0 up`             | Levanta (activa) la interfaz `eth0`         |
| `ifconfig eth0 down`                   |                                   | Baja (desactiva) la interfaz `eth0`         |
| `ifconfig eth0 <IP> netmask <máscara>` | `ip addr add IP/prefijo dev eth0` | Asigna dirección IP y máscara a la interfaz |
| `ping <IP>`                            |                                   | Prueba de conectividad (usa protocolo ICMP) |
| `setxkbmap es`                         |                                   | Cambia el teclado al layout español         |
| ifconfig                               | ip -s link show eth0              | para ver los packetes                       |

### 🪟 Comandos Windows

| Comando | Descripción |
|---|---|
| `ipconfig` | Muestra la configuración IP de las interfaces |
| `ipconfig /all` | Muestra **toda** la configuración detallada de todas las placas de red |
| `ping <IP>` | Prueba de conectividad (usa protocolo ICMP) |

### 📖 Definiciones Clave

| Término                          | Definición                                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------- |
| **Interfaz loopback**            | Interfaz virtual `127.0.0.1` para pruebas locales, no sale al cable                           |
| **Interfaz lógica**              | Interfaz virtual creada por software (alias, VLANs, etc.)                                     |
| **Interfaz física**              | NIC real con cable — en Linux: `eth0`, `ens33`, etc.                                          |
| **MAC Address**                  | Dirección física única del adaptador de red (48 bits, hexadecimal)                            |
| **MTU**                          | *Maximum Transmission Unit* — tamaño máximo de un paquete en bytes                            |
| **RX packets**                   | Paquetes *recibidos* por la interfaz (*Received*)                                             |
| **TX packets**                   | Paquetes *transmitidos* por la interfaz (*Transmitted*)                                       |
| **Bcast**                        | Dirección de broadcast de la red (se envía a todos los hosts)                                 |
| **Gateway / Puerta de enlace**   | IP del router que conecta la red local con otras redes                                        |
| **APIPA**                        | *Automatic Private IP Addressing* — rango `169.254.0.0/16`, se auto-asigna cuando no hay DHCP |
| **ICMP**                         | *Internet Control Message Protocol* — protocolo usado por `ping`                              |
| **Dominio**                      | Red centralizada con servidor de autenticación (Active Directory)                             |
| **Grupo de Trabajo (Workgroup)** | Red peer-to-peer sin servidor central de autenticación                                        |
| **DHCP**                         | Protocolo que asigna IPs automáticamente                                                      |
| **DNS**                          | Sistema de resolución de nombres a IPs                                                        |
| **WINS**                         | Resolución de nombres NetBIOS en redes Windows                                                |

---

## 🐧 Práctica sobre Linux

### Pregunta 1 — Usuario con mayores privilegios

> **¿Cómo se llama el usuario con mayor privilegios que puede configurar las direcciones IP en los sistemas operativos Linux?**

**Respuesta:** El usuario con mayores privilegios en Linux es **`root`**.

- Es el **superusuario** del sistema, equivalente al Administrador en Windows.
- Para ejecutar comandos de configuración de red como `ifconfig` se necesita ser root o usar `sudo` (Super User DO).
- Ejemplo de uso: `sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0`

---

### Pregunta 2 — Consultar configuración existente

> **Consultar la configuración actual de la placa de red.**

**Comando:**
```bash
ifconfig
```

**Explicación:**
- `ifconfig` (*Interface Configurator*) muestra las interfaces de red que están en estado **UP** (activas administrativamente).
- Muestra: nombre de interfaz, dirección IP, máscara, broadcast, MAC, MTU, estadísticas de paquetes.

> [!NOTE]
> `ifconfig` **solo** muestra interfaces UP. Para ver interfaces DOWN también, se usa `ip link`.

**Levantar una interfaz que está DOWN:**
```bash
ifconfig eth0 up
```

**Bajar una interfaz activa:**
```bash
ifconfig eth0 down
```

**Ver estado de todas las interfaces (UP y DOWN):**
```bash
ip link
```

**Identificación de interfaz física Ethernet en Linux:**

En Linux, una interfaz física Ethernet se identifica típicamente como:
- `eth0`, `eth1`, `eth2`... (nomenclatura clásica)
- `ens33`, `enp2s0`, `eno1`... (nomenclatura moderna *predictable names*)

La interfaz de **loopback** se identifica como `lo` (siempre tiene la IP `127.0.0.1`).

---

### Pregunta 3 — ==Identificar la dirección MAC

> **¿Cómo se identifica en Linux el valor de la dirección MAC?**

**Respuesta:** En la salida de `ifconfig` o ip a show , la dirección MAC se muestra en el campo:

```
ether XX:XX:XX:XX:XX:XX
```

O en versiones anteriores:

```
HWaddr XX:XX:XX:XX:XX:XX
```

**Características de la MAC:**
- Es una dirección de **48 bits** representada en **6 grupos hexadecimales** separados por `:` o `-`
- Los primeros 3 grupos identifican al fabricante (**OUI** — Organizationally Unique Identifier)
- Los últimos 3 grupos son el número de serie único del adaptador
- Ejemplo: `00:0C:29:A1:B2:C3` → `00:0C:29` es VMware

---

### Pregunta 4 — ==RX packets y TX packets

> **¿Qué significan RX packets y TX packets?**

con el ifconfig o ip -s link show eth0

| Campo          | Significado                                                                            |
| -------------- | -------------------------------------------------------------------------------------- |
| **RX packets** | *Received packets* — cantidad de paquetes **recibidos** por la interfaz                |
| **TX packets** | *Transmitted packets* — cantidad de paquetes **enviados/transmitidos** por la interfaz |

También aparecen estadísticas de errores:
- `errors` — paquetes con errores
- `dropped` — paquetes descartados
- `overruns` — desbordamientos de buffer

---

### Pregunta 5 — ==MTU

> **¿Qué significa MTU y el valor que acompaña al mismo?**

**MTU = *Maximum Transmission Unit*** (Unidad Máxima de Transmisión)

- Es el **tamaño máximo en bytes** que puede tener un paquete (frame) transmitido por esa interfaz sin necesidad de fragmentarse.
- El valor estándar para Ethernet es **1500 bytes**.
- Si un paquete supera el MTU, se **fragmenta** en paquetes más pequeños.
- La interfaz loopback (`lo`) suele tener MTU de **65536 bytes**.

**Ejemplo en salida de ifconfig:**
```
mtu 1500
```

---

### Pregunta 6 — Configurar la dirección IP

#### a) Configurar IP desde el shell

**Comando:**
```bash
ifconfig eth0 192.168.1.XX netmask 255.255.255.0
```

> Reemplazar `XX` por el número de PC del laboratorio.

**Ejemplo concreto (PC número 10):**
```bash
ifconfig eth0 192.168.1.10 netmask 255.255.255.0
```

**Verificar que quedó configurado:**
```bash
ifconfig eth0
```
o
```bash
ifconfig
```

> [!IMPORTANT]
> Esta configuración es **temporal** (volátil). Se pierde al reiniciar el sistema. Para hacerla permanente hay que editar archivos de configuración de red (`/etc/network/interfaces` en Debian/Ubuntu o usar NetworkManager).


Tambien hicimos con las alternativas en la clase 3


---

### b)==¿Qué significa Bcast? ¿Cómo se obtiene la dirección de broadcast?==

**Bcast = Broadcast address** (Dirección de difusión)

- Es la dirección que se usa para enviar un mensaje a **todos los hosts** de la red simultáneamente.
- **Cálculo:** Se obtiene aplicando OR entre la dirección IP y el complemento de la máscara.

**Ejemplo con la red `192.168.1.0/24`:**

```
IP:      192.168.1.10   →  11000000.10101000.00000001.00001010
Máscara: 255.255.255.0  →  11111111.11111111.11111111.00000000
NOT(M):  0.0.0.255      →  00000000.00000000.00000000.11111111

Broadcast = IP OR NOT(Máscara)
          = 192.168.1.255
```

→ **Broadcast = `192.168.1.255`** (todos los hosts del último octeto)

#### calculo paso a paso
Para entender este cálculo, hay que ver a las direcciones IP no como números decimales separados por puntos, sino como una cadena de 32 bits (unos y ceros).

El objetivo final de esta operación matemática es **mantener intacta la parte de la red** de la IP, y **convertir toda la parte de los hosts en unos ($1$)**.

Aquí tienes el desglose lógico paso a paso de lo que ocurre en tu ejemplo:

#### El "atajo" humano

En la práctica, si estás lidiando con máscaras "redondas" (como la `/24` de tu ejemplo, que termina exactamente en un punto decimal), no hace falta hacer la matemática binaria.

Como la máscara es `255.255.255.0`, sabes que los primeros tres números de la IP (`192.168.1`) están bloqueados para la red. El último número es el que varía para los hosts. Como el Broadcast siempre es la última dirección posible de la subred, simplemente rellenas ese último espacio con el valor máximo permitido en un octeto: **255**.

**1.Convertir a binario:**IP y Máscara.

Primero, las computadoras traducen los cuatro octetos decimales a binario.

- **IP ($192.168.1.10$):** `11000000.10101000.00000001.00001010`
    
- **Máscara ($255.255.255.0$):** `11111111.11111111.11111111.00000000`
    

_Nota: En la máscara, los $1$ representan la "Red" y los $0$ representan los "Hosts"._

**2.Calcular el NOT de la Máscara:**El complemento lógico.

La operación lógica **NOT** simplemente invierte todos los bits. Los $1$ se vuelven $0$, y los $0$ se vuelven $1$. Al aplicarlo a la máscara, "apagamos" la parte de la red y "encendemos" la parte de los hosts.

- **Máscara original:** `11111111.11111111.11111111.00000000`
    
- **NOT(Máscara):** `00000000.00000000.00000000.11111111` _(Esto en decimal equivale a 0.0.0.255, también conocido como "Wildcard")._
    

**3.Aplicar la operación OR:**IP + NOT(Máscara).

La operación **OR** compara los bits uno a uno y sigue una regla sencilla: **si hay al menos un $1$, el resultado es $1$. Solo da $0$ si ambos son $0$.**

Al enfrentar la IP original con la máscara invertida usando OR:

- Los primeros tres octetos de la IP se enfrentan contra puros ceros. El OR devuelve los bits originales de la IP sin cambios.
    
- El último octeto de la IP se enfrenta contra puros unos. El OR fuerza a que todos esos bits se conviertan en unos.
    

Plaintext

```
      11000000.10101000.00000001.00001010  (Dirección IP)
    | 00000000.00000000.00000000.11111111  (NOT Máscara)
    -------------------------------------
      11000000.10101000.00000001.11111111  (Resultado Broadcast)
    ```
  

  
    Finalmente, el sistema toma la cadena binaria resultante y la convierte bloque por bloque a nuestro sistema decimal:
    *   `11000000` = $192$
    *   `10101000` = $168$
    *   `00000001` = $1$
    *   `11111111` = $255$
    
    **Resultado final:** $192.168.1.255$
  

```

### Pregunta 7 — Comando moderno: `ip address show`

> **Un comando más moderno que reemplaza a ifconfig es `ip address show`**

```bash
ip address show
# También se puede abreviar:
ip addr show
ip addr
ip a
```

**Ventajas sobre `ifconfig`:**
- Es parte del paquete `iproute2` (más moderno y mantenido activamente)
- Muestra interfaces UP y DOWN
- Soporta IPv6 de forma nativa
- Sintaxis más consistente y poderosa
- `ifconfig` está **deprecado** en muchas distribuciones modernas

**Comparativa:**

| | `ifconfig` | `ip address show` |
|---|---|---|
| Mantenimiento | Deprecado | Activo |
| Interfaces DOWN | No muestra | Sí muestra |
| IPv6 | Limitado | Completo |
| Paquete | `net-tools` | `iproute2` |

---

### Pregunta 8 — Prueba de conectividad con ping

```bash
ping 192.168.1.XX
```

> **¿Qué protocolo utiliza este comando para realizar las pruebas y cuáles son sus siglas?**

**Respuesta:** El comando `ping` utiliza el protocolo **ICMP**

- **ICMP** = ***Internet Control Message Protocol*** (Protocolo de Mensajes de Control de Internet)
- Es un protocolo de **capa 3** (Red) del modelo OSI, definido en el RFC 792.
- `ping` envía mensajes **ICMP Echo Request** y espera **ICMP Echo Reply**.
- Si recibe respuesta → hay conectividad.
- Si hay **timeout** → no hay conectividad (puede estar bloqueado por firewall también).

**Información que devuelve ping:**
- `bytes` — tamaño del paquete enviado
- `time` — tiempo de ida y vuelta (RTT — Round Trip Time) en milisegundos
- `TTL` — *Time To Live*, saltos de router que quedan

---

### ==Gateway (Puerta de Enlace) — Teoría

> **Debido a que los equipos deben comunicarse con otros en redes lógicas distintas, se necesita configurar el Gateway.**

#### a) ¿Qué es el Gateway y para qué sirve?

**Gateway (Puerta de Enlace):**
- Es la **dirección IP del router** que conecta nuestra red local con otras redes (incluyendo Internet).
- Cuando un host quiere comunicarse con una IP que **no pertenece a su red local**, envía el paquete al Gateway.
- El Gateway (router) se encarga de **enrutar** el paquete hacia la red de destino.

**¿Cuándo se usa?**
- Si destino está en **la misma red** → el host envía directo (no usa Gateway)
- Si destino está en **otra red** → el host envía al Gateway, que reenvía

**Ejemplo:**
```
Mi IP:      192.168.1.10  /24
Gateway:    192.168.1.1
Destino A:  192.168.1.20  → misma red → envío directo
Destino B:  10.0.0.5      → otra red  → envío al Gateway 192.168.1.1
```

**Configurar Gateway en Linux:**
```bash
route add default gw 192.168.1.1
# O con iproute2:
ip route add default via 192.168.1.1
```

#### b) Identificación del Gateway en la topología

En una topología con router conectando dos redes:
- El punto que debe configurarse como **Gateway** es la **interfaz del router** conectada a la red local de los equipos.
- Por cada red conectada al router, hay **una interfaz** que actúa como Gateway para esa red.
- Si hay 2 redes, se necesitan configurar **2 interfaces** del router (una por red).![[{3F1AB97B-3174-4EBE-9385-2A8DE8FE77BB}.png]]

> [!TIP]
> La IP del Gateway generalmente es la primera o última dirección útil de la red. Por convención se suele usar `.1` o `.254`.
> Ej: para `192.168.1.0/24` → Gateway típico: `192.168.1.1`

---

## 🪟 Práctica sobre Microsoft Windows

### Pregunta 1 — Usuario con privilegios

> **¿Quién puede configurar las direcciones IP en un sistema operativo Microsoft Windows?**

**Respuesta:** El usuario **Administrador** (o un usuario con privilegios de administrador).

- En Windows, la configuración de red requiere permisos de administrador.
- Un usuario estándar puede ver la configuración pero **no puede modificarla**.
- En empresas, suele ser el administrador de sistemas o el departamento de IT.

---

### Pregunta 2 — Consultar configuración existente

> **Consultar la configuración actual de la placa de red.**

**Pasos:**
1. Botón Inicio → **Ejecutar** (o `Win + R`)
2. Escribir `cmd` → Aceptar
3. En la consola ejecutar:

```cmd
ipconfig
```

**Sobre APIPA:**

> **APIPA** = *Automatic Private Internet Protocol Addressing* (Direccionamiento Privado Automático del Protocolo de Internet)

- Si Windows no puede obtener una IP de un servidor DHCP, **se auto-asigna una IP** del rango:
  - **`169.254.0.0` a `169.254.255.255`** (máscara `/16` = `255.255.0.0`)
- Permite comunicación **solo con otros equipos en el mismo segmento** que también tengan APIPA.
- **No tiene Gateway** → no puede salir a Internet ni a otras redes.
- Es un indicador de que el servidor DHCP no está disponible o hay un problema de red.
- Definido en el **RFC 3927**.

---

### Pregunta 3 — Configurar la dirección IP en Windows

> **Configurar la IP desde el entorno visual (GUI).**

**Pasos detallados:**

1. **Panel de Control** → **Centro de redes y recursos compartidos**
2. Clic en **"Cambiar configuración del adaptador"**
3. Clic derecho sobre **"Conexión de área local"** → **Propiedades**
4. Seleccionar **"Protocolo de Internet versión 4 (TCP/IPv4)"**
5. Clic en **Propiedades**
6. Seleccionar **"Usar la siguiente dirección IP"**
7. Ingresar:
   - **Dirección IP:** `192.168.1.1XX` *(XX = últimos 2 números del número de PC)*
   - **Máscara de subred:** `255.255.255.0`
   - **Puerta de enlace:** *(no se completa en esta práctica)*
   - **DNS:** *(no se completa en esta práctica)*
8. **Aceptar** → **Cerrar**

> [!NOTE]
> En la pestaña **Opciones Avanzadas** se pueden agregar múltiples IPs, Gateways, servidores DNS y WINS para la misma interfaz.

**¿Qué es WINS?**
- **WINS** = *Windows Internet Name Service*
- Es el equivalente de DNS pero para nombres NetBIOS (nombres de equipos en redes Windows antiguas).

---

### Pregunta 4 — Dominio vs. Grupo de Trabajo

> **Incorporar el equipo a un Grupo de Trabajo o Dominio.**

**Pasos:**
1. Panel de Control → **Sistema** (o clic derecho en "Mi PC" → Propiedades)
2. Clic en **"Cambiar configuración"**
3. Clic en **"Cambiar..."**
4. Cambiar el nombre del equipo: `PC<apellido>` (ej: `PCSantos`)
5. Dejar el Grupo de Trabajo como `WORKGROUP`

#### a) ¿Qué es un dominio? ¿Diferencia entre Dominio y Grupo de Trabajo?

| Característica | **Dominio** | **Grupo de Trabajo** |
|---|---|---|
| **Servidor central** | Sí (Active Directory / DC) | No (peer-to-peer) |
| **Autenticación** | Centralizada en el servidor | Local en cada equipo |
| **Administración** | Centralizada (GPO, políticas) | Descentralizada |
| **Escala** | Redes grandes (empresas) | Redes pequeñas (hogares) |
| **Cuentas de usuario** | Se crean una vez, se usan en todos los equipos | Deben crearse en cada equipo |
| **Requiere servidor** | Sí (Windows Server con AD DS) | No |
| **Seguridad** | Alta (políticas centralizadas) | Baja (cada equipo gestiona lo suyo) |

**Dominio:** Conjunto de equipos y usuarios administrados **centralmente** por un servidor llamado **Controlador de Dominio** (DC — *Domain Controller*). Usa **Active Directory (AD)**.

**Grupo de Trabajo:** Red **peer-to-peer** donde cada equipo gestiona sus propios usuarios y recursos. No hay autoridad central.

#### b) ¿Cualquier usuario puede incorporarse a un Dominio?

**No.** Para unir un equipo a un Dominio se requiere:
- Credenciales de una **cuenta con privilegios de administrador del dominio** (o con permiso explícito para unir equipos).
- El equipo debe poder **alcanzar al Controlador de Dominio** (conectividad de red y DNS funcionando correctamente).
- Un usuario estándar del dominio **no puede** por defecto unir equipos a él.

#### c) Verificar que la IP quedó configurada

**Comando:**
```cmd
ipconfig
```

Muestra un resumen de la configuración IP de cada interfaz.

#### d) Listar toda la configuración de las placas de red

**Comando:**
```cmd
ipconfig /all
```

**Diferencia con `ipconfig`:**
- `/all` muestra **información detallada** de cada adaptador:
  - Nombre del adaptador
  - Descripción (modelo)
  - Dirección MAC (`Physical Address`)
  - DHCP habilitado o no
  - IP, máscara, gateway, DNS
  - Fechas de concesión DHCP

---

### Pregunta 5 — Prueba de conectividad

```cmd
ping 192.168.1.XX
```

*(donde XX es el número de PC de un compañero)*

- Si responde → hay comunicación de capa 3 (red) entre los equipos.
- Si hay timeout → revisar: ¿IPs en la misma red? ¿Firewall bloqueando ICMP? ¿Cable conectado?

---

## 🔁 Comparativa Final: Linux vs. Windows

| Acción              | Linux                           | Windows                              |
| ------------------- | ------------------------------- | ------------------------------------ |
| Ver IPs activas     | `ifconfig` / `ip a`             | `ipconfig`                           |
| Ver toda la config  | `ifconfig -a` / `ip a`          | `ipconfig /all`                      |
| Configurar IP       | `ifconfig eth0 IP netmask MASK` | GUI: Propiedades TCP/IPv4            |
| Configurar Gateway  | `route add default gw IP`       | GUI: Puerta de enlace predeterminada |
| Activar interfaz    | `ifconfig eth0 up`              | GUI: Habilitar adaptador             |
| Desactivar interfaz | `ifconfig eth0 down`            | GUI: Deshabilitar adaptador          |
| Prueba conectividad | `ping IP`                       | `ping IP`                            |
| Usuario requerido   | `root` / `sudo`                 | Administrador                        |
| Config. permanente  | Archivos de configuración       | Registro / GUI                       |

---

## 📝 Notas de estudio

> [!TIP]
> Para el examen, recordar:
> - **ICMP** = protocolo de `ping`
> - **APIPA** = `169.254.x.x` → sin DHCP
> - **MTU Ethernet** = 1500 bytes estándar
> - **Gateway** = router de salida, solo necesario para comunicarse con otras redes
> - `ifconfig` está deprecado → usar `ip address show` en sistemas modernos
> - La config de IP en Linux con `ifconfig` es **temporal** (no sobrevive reboot)

---

*Control de Cambios: v1.0 Abril 2017 (Ing. Gibellini) · v1.1 Feb 2022 · v1.2 Abril 2026 (Ing. Ciceri)*
