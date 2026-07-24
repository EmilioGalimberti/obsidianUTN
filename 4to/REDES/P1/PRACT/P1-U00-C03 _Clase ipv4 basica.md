---
tags:
aliases:
  - Clase IPv4 Básica
  - Comandos Red Linux
date: 2026-04-27
practica: P1-U00-P03
---
![[P1-U00-P03-1RVL-Practica Basica IPv4-2025.pdf]]

# 🌐 Configuración de Direccionamiento IPv4 en Linux

> [!info] Objetivo de la práctica
> Configurar los equipos **PC1**, **PC2** y **Servidor** para que tengan conectividad entre sí dentro de la red `192.168.1.0/24`, usando comandos de Linux para configurar, verificar y diagnosticar interfaces de red.

---
## 🗺️ Topología de la Red
![[{52354DFF-767B-4A61-9D5D-EFDC9E0AD81B}.png]]

---
## 🔑 ==Tabla Resumen de Comandos==


|           |                      | ifconfig    | interfaces up               |
| --------- | -------------------- | ----------- | --------------------------- |
| ip a show | estado de interfaces | ifconfig -a | listar todas las interfaces |
|           |                      |             |                             |


### Comandos modernos (`ip` — iproute2) ✅

| Comando                           | Para qué sirve                          |
| --------------------------------- | --------------------------------------- |
| `ip link show eth0`               | Ver estado de una interfaz (UP/DOWN)    |
| `ip link show`                    | Listar **todas** las interfaces         |
| `ip link set eth0 up`             | Habilitar una interfaz                  |
| `ip addr add IP/prefijo dev eth0` | Asignar IP temporalmente                |
| `ip addr show eth0`               | Verificar IP asignada                   |
| `ip route`                        | Ver tabla de rutas                      |
| `ip neigh`                        | Ver tabla ARP                           |
| `ping -c N IP`                    | Probar conectividad (N paquetes)        |
| `arp -n`                          | Ver tabla ARP (IP ↔ MAC)                |
| `route`                           | Ver tabla de rutas (clásico)            |
| `cat /proc/net/arp`               | Ver ARP desde el sistema de archivos    |
| `cat /proc/net/dev`               | Ver estadísticas de interfaces          |
| `reboot`                          | Reiniciar el equipo                     |
| `nano /etc/network/interfaces`    | Editar config permanente de red         |
| `ifup eth0`                       | Activar interfaz con config del archivo |
| `ifdown eth0`                     | Desactivar interfaz                     |
|                                   |                                         |
| su -                              | pasar a root                            |
| apt update && apt install nano -y | installar nano                          |

### Comandos clásicos (`ifconfig` — net-tools) ⚠️ Deprecado

| Comando `ifconfig`              | Equivalente `ip`                  | Para qué sirve                                                                    |
| ------------------------------- | --------------------------------- | --------------------------------------------------------------------------------- |
| `ifconfig eth0`                 | `ip addr show eth0`               | Ver estado e IP de una interfaz<br><br>en el ifconfig es mas facil ver la mascara |
| `ifconfig -a`                   | `ip link show`                    | Ver **todas** las interfaces                                                      |
| `ifconfig eth0 up`              | `ip link set eth0 up`             | Habilitar interfaz                                                                |
| `ifconfig eth0 IP netmask MASK` | `ip addr add IP/prefijo dev eth0` | Asignar IP                                                                        |
| `route`                         | `ip route`                        | Ver tabla de rutas                                                                |
| `arp`                           | `ip neigh`                        | Ver tabla ARP                                                                     |
| ifconfig                        | ip a show                         | sirve para ver interfaces up                                                      |

## 📖 ==Guía de Comandos

> [!note] Sistema operativo
> Todos los comandos son para **Linux** (Debian/Ubuntu/Mint). Se ejecutan en la terminal como usuario con permisos suficientes (o anteponiendo `sudo`).

---

### `ip link show [interfaz]`

**¿Para qué sirve?** Muestra el **estado de una interfaz de red** específica: si está activa (`UP`) o inactiva (`DOWN`), su dirección MAC, MTU, etc.

```bash
ip link show eth0
```

**Salida típica:**
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP ...
    link/ether 08:00:27:ab:cd:ef brd ff:ff:ff:ff:ff:ff
```

| Parte de la salida | Qué significa |
|---|---|
| `eth0` | Nombre de la interfaz |
| `UP` | La interfaz está **habilitada/activa** |
| `DOWN` | La interfaz está **deshabilitada** |
| `mtu 1500` | Tamaño máximo de paquete (Maximum Transmission Unit) |
| `link/ether 08:00:27:...` | Dirección MAC (física) de la interfaz |

---

### `ip link show` *(sin especificar interfaz)*

**¿Para qué sirve?** Lista **todas las interfaces de red** disponibles en el equipo, estén activas o no.

```bash
ip link show
```

**Salida típica:**
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 ...
2: eth0: <BROADCAST,MULTICAST> mtu 1500 ... state DOWN ...
```

| Interfaz | Qué es |
|---|---|
| `lo` | Interfaz de **loopback** (127.0.0.1) — siempre está, es interna |
| `eth0` | Primera **interfaz Ethernet** (cable de red) |
| `eth1`, `eth2`... | Interfaces adicionales |

---

### `ip link set eth0 up`

**¿Para qué sirve?** **Habilita (activa)** una interfaz de red que está en estado `DOWN`.

```bash
ip link set eth0 up
```

> [!tip] No produce salida
> Si el comando se ejecuta correctamente, **no muestra nada**. Para confirmar que funcionó, hay que volver a correr `ip link show eth0` y verificar que diga `UP`.

---

### `ip addr add [IP]/[prefijo] dev [interfaz]`

**¿Para qué sirve?** **Asigna una dirección IP** y su máscara de subred a una interfaz de red.

```bash
ip addr add 192.168.1.10/24 dev eth0
```

| Parte del comando | Qué significa |
|---|---|
| `192.168.1.10` | La dirección IP a asignar |
| `/24` | El **prefijo de red** (equivalente a máscara `255.255.255.0`) |
| `dev eth0` | La interfaz a la que se le asigna la IP |

> [!warning] Configuración temporal
> Esta asignación es **temporal**. Al reiniciar el equipo, se pierde. Para hacerla permanente hay que editar `/etc/network/interfaces`.

---

### `ip addr show` / `ip addr show eth0`

**¿Para qué sirve?** **Verifica** la configuración IP actual de las interfaces. Muestra las IPs asignadas, máscaras y más.

```bash
ip addr show eth0
```

**Salida típica:**
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
    link/ether 08:00:27:ab:cd:ef brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

| Parte de la salida | Qué significa |
|---|---|
| `inet 192.168.1.10/24` | La **IP asignada** con su prefijo |
| `brd 192.168.1.255` | Dirección de **broadcast** de la red |
| `scope global` | La IP es válida para toda la red (no solo local) |

---

### `ping [IP destino]` / `ping -c [N] [IP destino]`

**¿Para qué sirve?** **Prueba la conectividad** entre dos equipos enviando paquetes ICMP (como un "eco"). Si el destino responde, hay comunicación.

```bash
ping 192.168.1.10         # Envía pings continuos (detener con Ctrl+C)
ping -c 4 192.168.1.10    # Envía exactamente 4 paquetes y para
```

**Salida cuando HAY conectividad:**
```
PING 192.168.1.10 (192.168.1.10) 56(84) bytes of data.
64 bytes from 192.168.1.10: icmp_seq=1 ttl=64 time=0.543 ms
64 bytes from 192.168.1.10: icmp_seq=2 ttl=64 time=0.321 ms
```

**Salida cuando NO hay conectividad (host no existe):**
```
From 192.168.1.20 icmp_seq=1 Destination Host Unreachable
```

**Salida cuando la RED no es alcanzable:**
```
connect: Network is unreachable
```

| Mensaje | Qué significa |
|---|---|
| `64 bytes from ...` | ✅ El host existe y **responde** |
| `Destination Host Unreachable` | ❌ La red existe pero el **host no responde** (no tiene esa IP) |
| `Network is unreachable` | ❌ El equipo **no sabe cómo llegar** a esa red (falta ruta) |
| `time=X ms` | Tiempo de ida y vuelta del paquete (latencia) |
| `ttl=64` | Time To Live — saltos máximos que puede dar el paquete |

---

### `arp -n` / `cat /proc/net/arp`

**¿Para qué sirve?** Muestra la **tabla ARP** (Address Resolution Protocol). Esta tabla vincula direcciones IP con direcciones MAC de los equipos con los que el equipo ya se comunicó.

```bash
arp -n
# O también:
cat /proc/net/arp
```

**Salida típica:**
```
Address          HWtype  HWaddress           Flags Mask  Iface
192.168.1.20     ether   08:00:27:11:22:33   C           eth0
192.168.1.100    ether   08:00:27:44:55:66   C           eth0
```

| Columna | Qué significa |
|---|---|
| `Address` | La dirección **IP** del vecino |
| `HWaddress` | La dirección **MAC** correspondiente |
| `Iface` | Por qué interfaz se llega a ese equipo |

---

### `route` / `cat /proc/net/route`

**¿Para qué sirve?** Muestra la **tabla de enrutamiento**: las reglas que tiene el equipo para saber cómo llegar a distintas redes.

```bash
route
```

**Salida típica:**
```
Kernel IP routing table
Destination     Gateway   Genmask         Flags Metric Ref  Use Iface
192.168.1.0     0.0.0.0   255.255.255.0   U     0      0    0   eth0
```

---

### Archivos del sistema `/proc/net/`

Linux expone información de red en archivos de texto dentro de `/proc/net/`. Se pueden leer con `cat`:

| Archivo             | Qué muestra                                                 |
| ------------------- | ----------------------------------------------------------- |
| `/proc/net/arp`     | Tabla ARP (IP ↔ MAC)                                        |
| `/proc/net/dev`     | Estadísticas de cada interfaz (paquetes enviados/recibidos) |
| `/proc/net/netstat` | Estadísticas generales de protocolos de red                 |
| `/proc/net/route`   | Tabla de enrutamiento en formato hexadecimal                |

```bash
cat /proc/net/arp
cat /proc/net/dev
cat /proc/net/netstat
cat /proc/net/route
```

---

### `reboot`

**¿Para qué sirve?** **Reinicia** el equipo. Se usa en la práctica para demostrar que la configuración IP manual se **pierde** al reiniciar.

```bash
reboot
```

---

### `/etc/network/interfaces` — Configuración Permanente

**¿Para qué sirve?** Es el **archivo de configuración de red** de Debian/Ubuntu/Mint. Las interfaces configuradas aquí **persisten tras el reinicio**.

```bash
# Para editar el archivo:
nano /etc/network/interfaces
```

**Contenido a agregar al final del archivo:**
```
iface eth0 inet static
   address 192.168.1.10
   netmask 255.255.255.0
```

| Línea | Qué significa |
|---|---|
| `iface eth0` | Configura la interfaz `eth0` |
| `inet static` | Usa IP **estática** (fija, no DHCP) |
| `address` | La dirección IP a asignar |
| `netmask` | La máscara de subred |

---

### `ifup [interfaz]` / `ifdown [interfaz]`

**¿Para qué sirve?** Levanta (`ifup`) o baja (`ifdown`) una interfaz usando la configuración definida en `/etc/network/interfaces`. Solo funcionan si la interfaz está configurada en ese archivo.

```bash
ifup eth0    # Activa eth0 con la configuración del archivo
ifdown eth0  # Desactiva eth0
```

---

### `ifconfig` — Alternativa clásica (deprecada)

**¿Para qué sirve?** Es el comando tradicional para ver y configurar interfaces de red. Pertenece al paquete `net-tools`, que está **deprecado** (ya no recibe mantenimiento activo). En distros modernas puede no estar instalado.

```bash
ifconfig           # Ver todas las interfaces activas
ifconfig -a        # Ver TODAS las interfaces, incluso las DOWN
ifconfig eth0      # Ver solo eth0
```

**Salida típica de `ifconfig eth0`:**
```
eth0      Link encap:Ethernet  HWaddr 08:00:27:ab:cd:ef
          inet addr:192.168.1.10  Bcast:192.168.1.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1000 errors:0 dropped:0
          TX packets:900  errors:0 dropped:0
```

| Parte de la salida | Qué significa |
|---|---|
| `HWaddr 08:00:27:...` | Dirección **MAC** de la interfaz |
| `inet addr:192.168.1.10` | La **IP** asignada |
| `Mask:255.255.255.0` | La **máscara** de subred |
| `Bcast:192.168.1.255` | Dirección de **broadcast** |
| `UP BROADCAST RUNNING` | La interfaz está **activa** |
| `RX / TX packets` | Paquetes **recibidos / enviados** |

> [!warning] ¿Está instalado?
> En Debian/Ubuntu moderno puede no estar. Instalarlo con: `apt install net-tools`

---

### `ifconfig eth0 up` / `ifconfig eth0 [IP] netmask [máscara]`

**Equivalentes clásicos** a `ip link set` e `ip addr add`:

```bash
ifconfig eth0 up                                      # Habilitar interfaz
ifconfig eth0 192.168.1.10 netmask 255.255.255.0      # Asignar IP
```

---


---

## ✅ Resolución Completa de la Práctica

> [!warning] Antes de empezar
> Todos los comandos se ejecutan en la terminal del equipo indicado. Los equipos están conectados a un switch común en la red `192.168.1.0/24`.

---

### 📍 Paso 1 — ==Verificar si eth0 está habilitada en PC1

**Equipo:** PC1
1)
```bash
ip link show eth0
```



**Salida esperada (interfaz DOWN):**
```
2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN ...
    link/ether 08:00:27:ab:cd:ef brd ff:ff:ff:ff:ff:ff
```

👉 Vemos `state DOWN` → la interfaz existe pero **no está activa**.

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig 
> 
> te dice las interfazes UP
> 
---

o
ip a show eth0

### 📍 Paso 2 — ==Listar todas las interfaces disponibles en PC1==

**Equipo:** PC1

```bash
ip link show
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig -a    # Muestra TODAS las interfaces, incluso las DOWN
> ```

**Salida esperada:**
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 ...
2: eth0: <BROADCAST,MULTICAST> mtu 1500 ... state DOWN ...
```

👉 Vemos que el equipo tiene `lo` (loopback) y `eth0` (la placa de red). `eth0` está DOWN.

---

### 📍 Paso 3 — ==Habilitar la interfaz eth0 en PC1

**Equipo:** PC1

```bash
ip link set eth0 up
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0 up
> ```

**Salida:** Ninguna (si no da error, funcionó).

---

### 📍 Paso 4 — ==Verificar nuevamente el estado de las interfaces en PC1

**Equipo:** PC1

```bash
ip link show
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig -a    # Ahora eth0 debería aparecer sin "DOWN"
> ```

**Salida esperada (ahora UP):**
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 ...
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ... state UP ...
```

👉 Ahora aparece `UP` → la interfaz está activa.

---

### 📍 Paso 5 — Repetir pasos 1 al 4 para PC2 y Servidor

**Equipo: PC2**
```bash
ip link show eth0          # Verificar estado
ip link show               # Listar interfaces
ip link set eth0 up        # Habilitar
ip link show               # Confirmar UP
```

**Equipo: Servidor**
```bash
ip link show eth0
ip link show
ip link set eth0 up
ip link show
```

---

### 📍 Paso 6 — ==Asignar IP a PC1

**Equipo:** PC1  
**IP a asignar:** `192.168.1.10` | **Máscara:** `255.255.255.0` → `/24`

```bash
ip addr add 192.168.1.10/24 dev eth0
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0 192.168.1.10 netmask 255.255.255.0
> ```
> Con `ifconfig` se escribe la máscara completa (`255.255.255.0`) en lugar del prefijo (`/24`).

**Salida:** Ninguna (si no da error, funcionó).

---

### 📍 Paso 7 — ==Verificar la configuración de PC1

**Equipo:** PC1

```bash
ip addr show eth0
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0
> ```
> **Salida equivalente:**
> ```
> eth0   inet addr:192.168.1.10  Bcast:192.168.1.255  Mask:255.255.255.0
> ```

**Salida esperada:**
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
    link/ether 08:00:27:ab:cd:ef brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

👉 Vemos `inet 192.168.1.10/24` → la IP fue asignada correctamente ✅

---

### 📍 Paso 8 — Asignar IP a PC2

**Equipo:** PC2  
**IP a asignar:** `192.168.1.20` | **Máscara:** `/24`

```bash
ip addr add 192.168.1.20/24 dev eth0
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0 192.168.1.20 netmask 255.255.255.0
> ```

---

### 📍 Paso 9 — Verificar la configuración de PC2

**Equipo:** PC2

```bash
ip addr show eth0
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0
> ```

**Salida esperada:**
```
    inet 192.168.1.20/24 brd 192.168.1.255 scope global eth0
```

---

### 📍 Paso 10 — ==Ping de PC2 hacia PC1

**Equipo:** PC2 → destino: `192.168.1.10`

```bash
ping -c 4 192.168.1.10
```

**Salida esperada (hay conectividad):**
```
PING 192.168.1.10 (192.168.1.10) 56(84) bytes of data.
64 bytes from 192.168.1.10: icmp_seq=1 ttl=64 time=0.543 ms
64 bytes from 192.168.1.10: icmp_seq=2 ttl=64 time=0.321 ms
64 bytes from 192.168.1.10: icmp_seq=3 ttl=64 time=0.298 ms
64 bytes from 192.168.1.10: icmp_seq=4 ttl=64 time=0.310 ms

--- 192.168.1.10 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss
```

👉 `0% packet loss` y respuestas de la IP → conectividad exitosa ✅

---

### 📍 Paso 11 — Ping de PC2 hacia el Servidor (todavía sin IP)

**Equipo:** PC2 → destino: `192.168.1.100`

```bash
ping -c 4 192.168.1.100
```

**Salida esperada (el Servidor todavía no tiene IP asignada):**
```
From 192.168.1.20 icmp_seq=1 Destination Host Unreachable
From 192.168.1.20 icmp_seq=2 Destination Host Unreachable
```

👉 `Destination Host Unreachable` → La red existe (`192.168.1.0/24`) pero **ningún equipo tiene esa IP** todavía. Es la respuesta correcta en este punto.

---

### 📍 Paso 12 — Asignar IP al Servidor

**Equipo:** Servidor  
**IP a asignar:** `192.168.1.100` | **Máscara:** `/24`

```bash
ip addr add 192.168.1.100/24 dev eth0
```

---

### 📍 Paso 13 — Verificar la configuración del Servidor

**Equipo:** Servidor

```bash
ip addr show eth0
```

**Salida esperada:**
```
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
```

---

### 📍 Paso 14 — Ping de PC2 hacia el Servidor (ahora con IP)

**Equipo:** PC2 → destino: `192.168.1.100`

```bash
ping -c 4 192.168.1.100
```

**Salida esperada (ahora sí hay conectividad):**
```
64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=0.412 ms
64 bytes from 192.168.1.100: icmp_seq=2 ttl=64 time=0.388 ms
```

👉 El Servidor ya tiene IP y responde ✅

---

### 📍 Paso 15 — Ping desde el Servidor hacia PC1 y PC2

**Equipo:** Servidor → destinos: `192.168.1.10` y `192.168.1.20`

```bash
ping -c 4 192.168.1.10
ping -c 4 192.168.1.20
```

**Salida esperada (ambos responden):**
```
64 bytes from 192.168.1.10: icmp_seq=1 ttl=64 time=0.501 ms
...
64 bytes from 192.168.1.20: icmp_seq=1 ttl=64 time=0.389 ms
```

---

### 📍 Paso 16 — Ping a IP inexistente en la misma red

**Equipo:** Servidor → destino: `192.168.1.30` *(no hay ningún equipo con esa IP)*

```bash
ping -c 4 192.168.1.30
```

**Salida esperada:**
```
From 192.168.1.100 icmp_seq=1 Destination Host Unreachable
```

👉 La red `192.168.1.0/24` es alcanzable, pero no hay ningún equipo en `.30`. Respuesta esperada ✅

---

### 📍 Paso 17 — Ping a IP de otra red

**Equipo:** Servidor → destino: `192.168.2.40` *(red diferente: `192.168.2.0/24`)*

```bash
ping -c 4 192.168.2.40
```

**Salida esperada:**
```
connect: Network is unreachable
```

> [!important] ¿Por qué "Network is unreachable" y no "Host Unreachable"?
> - `Destination Host Unreachable` → El equipo conoce la red pero el host no existe.
> - `Network is unreachable` → El equipo **no tiene ruta** hacia esa red. No sabe ni cómo llegar a `192.168.2.0/24` porque no hay un router configurado que la conecte.

---

### 📍 Paso 18 — ==Inspeccionar la tabla ARP del Servidor

**Equipo:** Servidor

```bash
arp -n
```

**Salida esperada** (después de haber hecho ping a PC1 y PC2):
```
Address          HWtype  HWaddress           Flags Mask  Iface
192.168.1.10     ether   08:00:27:11:22:33   C           eth0
192.168.1.20     ether   08:00:27:44:55:66   C           eth0
```

👉 El Servidor "recuerda" la MAC de los equipos con los que ya se comunicó. Esto es ARP en acción: vincula IP ↔ MAC automáticamente.

---

### 📍 Paso 19 — ==Inspeccionar archivos de red en /proc

**Equipo:** Servidor (o cualquier equipo)

```bash
cat /proc/net/arp       # Tabla ARP
cat /proc/net/dev       # Estadísticas de interfaces
cat /proc/net/netstat   # Estadísticas de protocolos
cat /proc/net/route     # Tabla de rutas (en hex)
```

**Salida de `/proc/net/dev` (ejemplo):**
```
Inter-|   Receive                        |  Transmit
 face |bytes packets errs drop ...       |bytes packets errs ...
    lo:  1024      8    0    0 ...           1024      8    0 ...
  eth0: 84000   1000    0    0 ...          72000    900    0 ...
```

👉 Muestra cuántos bytes y paquetes pasaron por cada interfaz. Útil para diagnóstico.

---

### 📍 Paso 20 — Reiniciar PC1

**Equipo:** PC1

```bash
reboot
```

👉 El equipo se reinicia. La configuración IP asignada con `ip addr add` **se pierde** porque era temporal.

---

### 📍 Pasos 21, 22 y 23 — Verificar que la IP se perdió y volver a habilitar

**Equipo:** PC1 (después del reinicio)

```bash
ip link show eth0     # Paso 21: Verificar — estará DOWN y sin IP
ip link set eth0 up   # Paso 22: Habilitar la interfaz
ip link show          # Paso 23: Confirmar que está UP (pero sin IP)
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig -a          # Paso 21: Ver todas — eth0 estará DOWN y sin inet addr
> ifconfig eth0 up     # Paso 22: Habilitar
> ifconfig -a          # Paso 23: Confirmar UP (pero sin IP asignada)
> ```

👉 Esto demuestra que la configuración manual **no sobrevive al reinicio**.

---

### 📍 Paso 24 — ==Hacer la configuración permanente

**Equipo:** PC1

Editar el archivo `/etc/network/interfaces`:

```bash
nano /etc/network/interfaces
```
o
``` bash
mcedit
```


Agregar al **final del archivo** (respetando la sangría con espacios):

```
iface eth0 inet static
   address 192.168.1.10
   netmask 255.255.255.0
```

Guardar: `Ctrl+O` → `Enter` → `Ctrl+X`

---

### 📍 Paso 25 — ==Levantar la interfaz con la configuración guardada

**Equipo:** PC1

```bash
ifup eth0
```

**Salida esperada:**
```
ifup: interface eth0 already configured
```
*(O bien configura la IP sin output si estaba DOWN)*

NO TE TIRA NADA EL IFUP, pero si no esta bien configurada te tira que no la encuentra


---

### 📍 Paso 26 — ==Verificar que la IP está activa

**Equipo:** PC1

```bash
ip addr show eth0
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0
> ```

**Salida esperada:**
```
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

---

### 📍 Paso 27 — Reiniciar PC1 nuevamente

**Equipo:** PC1

```bash
reboot
```

---

### 📍 Paso 28 — Verificar que la IP persiste tras el reinicio

**Equipo:** PC1 (después del reinicio)

```bash
ip addr show eth0
```

> [!tip] Alternativa con ifconfig
> ```bash
> ifconfig eth0
> # Debe mostrar la inet addr:192.168.1.10 sin haberla configurado manualmente
> ```

**Salida esperada:**
```
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

👉 Ahora la IP **persiste** porque está guardada en `/etc/network/interfaces` ✅

---

## 📊 Resumen Final: IPs asignadas

| Equipo | Interfaz | IP | Máscara | Red |
|---|---|---|---|---|
| PC1 | eth0 | `192.168.1.10` | `255.255.255.0` | `192.168.1.0/24` |
| PC2 | eth0 | `192.168.1.20` | `255.255.255.0` | `192.168.1.0/24` |
| Servidor | eth0 | `192.168.1.100` | `255.255.255.0` | `192.168.1.0/24` |


---
## 🔄 `ip` vs `ifconfig` — ¿Cuál usar?

> [!important] Recomendación
> Preferir siempre `ip` (iproute2). Es el estándar actual. Usar `ifconfig` solo si el enunciado lo pide explícitamente o el sistema es muy viejo.

| Característica | `ifconfig` (net-tools) | `ip` (iproute2) |
|---|---|---|
| **Estado** | ⚠️ Deprecado | ✅ Mantenido activamente |
| **Instalado por defecto** | No en distros modernas | Siempre |
| **Soporte IPv6** | Limitado | Completo |
| **Soporte VLANs / túneles** | No | Sí |
| **Velocidad / eficiencia** | Menor | Mayor |

### Tabla de equivalencias

| `ifconfig` (viejo) | `ip` (nuevo) | Para qué sirve |
|---|---|---|
| `ifconfig` | `ip addr show` | Ver interfaces activas |
| `ifconfig -a` | `ip link show` | Ver **todas** las interfaces |
| `ifconfig eth0 up` | `ip link set eth0 up` | Habilitar interfaz |
| `ifconfig eth0 192.168.1.10 netmask 255.255.255.0` | `ip addr add 192.168.1.10/24 dev eth0` | Asignar IP |
| `route` | `ip route` | Ver tabla de rutas |
| `arp` | `ip neigh` | Ver tabla ARP |

## 🔗 Notas Relacionadas


---

