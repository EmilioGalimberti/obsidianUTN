# P1-U00-C07 | PRÁCTICA DE DIRECCIONAMIENTO IP
## Aplicado a una Topología Física

> **Materia:** Redes de Información — UTN FRC  
> **Fuente:** P1-U00-P07 Direccionamiento_IP_Subredes_Diseño 2024  
> **Autor cátedra:** Ing. Gibellini Fabián (v1.1 Abril 2024)

---

## 📋 OBJETIVOS DE LA PRÁCTICA

- Practicar el proceso de creación de subredes.
- Interpretar las necesidades de direccionamiento IP a partir de un escenario dado.
- Confeccionar una solución de direccionamiento IP a partir de un caso práctico de diseño de red.
- Desarrollar la capacidad para el análisis y el diseño de topologías de redes y su correspondiente ubicación en un gráfico.
![[P1-U00-P07 Direccionamiento_IP_Subredes_Diseño 2024.pdf]]
---

## 🗺️ TOPOLOGÍA DEL ESCENARIO

La topología presenta **3 routers** interconectados mediante enlaces seriales (WAN), con redes LAN en cada uno:

```
                    [Academica]
                    45 Hosts
                       |
                     [SW] -- Eth1
                              |
[Router1] ---S0---S1--- [Router2] ---Eth0--- [SW]--- [DOCENTES 60 Hosts]
    |   \                   |
   Eth0  \                 S0
    |     S1                |
  [sw]     \                |
    |       \               |
[Alumnos]    \             S1
212 Hosts     \S0------[Router3]
                      /        \
                   Eth0         Eth1
                    |             |
    [SW]---------[SW]             |
     |        [Sistemas]    [NO DOCENTES]  
    sistemas     30 Hosts     75 Hosts
    150 host                     
```

### Resumen de Redes LAN del Escenario

| Área / Segmento         | Hosts declarados  | Router        | Interfaz  |
| ----------------------- | ----------------- | ------------- | --------- |
| Alumnos                 | 212               | Router1       | Eth0      |
| Docentes                | 60                | Router2       | Eth0      |
| Academica               | 45                | Router2       | Eth1      |
| NO Docentes             | 75                | Router3       | Eth1      |
| Sistemas (grande)       | 150               | Router3       | Eth0      |
| Sistemas (pequeño)      | 30                | Router3       | Eth0 +sw) |
| Enlace R1 ↔ R2 (Serial) | 2 (punto a punto) | R1-S0 / R2-S1 | —         |
| Enlace R1 ↔ R3 (Serial) | 2 (punto a punto) | R1-S1 / R3-S0 | —         |
| Enlace R2 ↔ R3 (Serial) | 2 (punto a punto) | R2-S0 / R3-S1 | —         |

---

## 📚 MARCO TEÓRICO

### 1. Clases de Direcciones IPv4

Las direcciones IP versión 4 tienen 32 bits y se clasifican en clases:

| Clase | Rango del primer octeto | Máscara por defecto | Redes disponibles | Hosts por red |
| ----- | ----------------------- | ------------------: | ----------------- | ------------- |
| A     | 1 – 126                 |     /8  (255.0.0.0) | 126               | 16.777.214    |
| B     | 128 – 191               |   /16 (255.255.0.0) | 16.384            | 65.534        |
| C     | 192 – 223               | /24 (255.255.255.0) | 2.097.152         | 254           |

> **⚠️ El ejercicio exige usar una dirección de Clase B**

### 2. ¿Qué es una Subred?

El **subnetting** consiste en dividir una red mayor (con su máscara de clase) en redes más pequeñas, tomando prestados bits del campo de host para usarlos como bits de subred.

```
Dirección Clase B:    [  Red (16 bits)  ][    Host (16 bits)    ]
Con subnetting:       [  Red (16 bits)  ][ Subred (n) ][ Host (h) ]
```

### 3. Fórmulas Fundamentales

#### 🔢 Número de Subredes

$$N_{subredes} = 2^n$$

Donde **n** = cantidad de bits prestados del campo host para subred.

#### 🖥️ Hosts Utilizables por Subred

$$N_{hosts} = 2^h - 2$$

Donde **h** = bits restantes para host. Se restan 2: dirección de **red** (todo ceros) y **broadcast** (todo unos).

#### 📐 Máscara de Subred

La máscara se forma poniendo **1** en todos los bits de red + subred, y **0** en los de host.

```
Clase B base:  1111 1111 . 1111 1111 . 0000 0000 . 0000 0000  = /16
Con n=4 bits:  1111 1111 . 1111 1111 . 1111 0000 . 0000 0000  = /20
```

#### 📏 Bloque / Salto (Magic Number)

$$Bloque = 2^h$$

Es el tamaño de cada subred. Las subredes avanzan de a este valor.

### 5. ==Los Enlaces WAN también son Subredes

Un enlace serial **punto a punto** entre dos routers es una red como cualquier otra: cada extremo tiene una dirección IP, por lo tanto necesita su propia subred.

```
[Router1]─── S0: 172.16.10.1 ════════ S1: 172.16.10.2 ───[Router2]
                        subred 172.16.10.0/23
                   ↑ es una subred igual que una LAN
```

**¿Por qué necesitan IP?**
- Los routers usan esas IPs para **enrutarse entre sí**.
- Los protocolos de routing (RIP, OSPF) intercambian mensajes entre esas IPs.
- Sin IP en el serial, no hay comunicación entre routers.

**¿Cuántos hosts usa?** Solo **2** (uno por extremo), pero igual consume una subred entera. En este ejercicio con subnetting fijo (`/23`) se desperdician 508 direcciones por enlace WAN. En diseño real se usaría `/30` (VLSM) que da exactamente 2 hosts.

| Tipo de segmento         | ¿Necesita subred? | Hosts mínimos |
|--------------------------|:-----------------:|:-------------:|
| LAN con hosts            | ✅ Sí             | según diseño  |
| Enlace serial WAN (P2P)  | ✅ Sí             | 2             |
| Interfaz loopback        | opcional          | 1             |

> 📌 **Regla de oro:** Toda interfaz de router con IP pertenece a una subred. Los seriales tienen IP → **siempre cuentan como subred al hacer el relevamiento**.

### 6. Proceso de Diseño (Metodología)

```
PASO 1: Relevamiento → Identificar TODAS las redes (LAN + WAN)
PASO 2: Proyección   → Aplicar % de crecimiento a futuro
PASO 3: Red mayor    → Determinar la subred que más hosts necesita
PASO 4: Calcular h   → 2^h - 2 ≥ hosts_max_con_crecimiento
PASO 5: Calcular n   → n = 16 - h  (para clase B)
PASO 6: Verificar    → 2^n ≥ cantidad_subredes_necesarias
PASO 7: Máscara      → Construir la máscara de subred
PASO 8: Tabla        → Listar todas las subredes con sus rangos
PASO 9: Asignar      → Asignar subredes a cada interfaz
```

---

## ✏️ RESOLUCIÓN PASO A PASO

### 📌 PASO 1 — Relevamiento: ==Identificación de todas las subredes

Del diagrama de topología identificamos **todas** las redes lógicas (LAN + enlaces WAN punto a punto):

| N°  | Nombre       | Hosts requeridos | Tipo |
| --- | ------------ | ---------------- | ---- |
| 1   | Alumnos      | 212              | LAN  |
| 2   | Sistemas     | 180              | LAN  |
| 3   | NO Docentes  | 75               | LAN  |
| 4   | Docentes     | 60               | LAN  |
| 5   | Academica    | 45               | LAN  |
| 6   | Enlace R1↔R2 | 2                | WAN  |
| 7   | Enlace R1↔R3 | 2                | WAN  |
| 8   | Enlace R2↔R3 | 2                | WAN  |

> ==**Total mínimo de subredes necesarias = 8**==
![[{5ABF0F08-8E99-49D4-8111-51D96043668C}.png]]
![[{5ABF0F08-8E99-49D4-8111-51D96043668C}.png]]
---
### 📌 PASO 2 — ==Cantidad de subredes

$$N_{subredes} = 2^n = 2^4 = \textbf{16 subredes}$$

¿Tenemos suficientes subredes?
- Subredes mínimas necesarias: 8
- Subredes con 30% de expansión: 8 × 1.30 = 10,4→ **11 subredes mínimas con expansión**
- Subredes disponibles: **16**

> ✅ **16 ≥ 12** → El diseño es válido con margen más que suficiente para crecer.

**Respuestas al cuestionario del TP:**

| Pregunta                                             | Respuesta |
| ---------------------------------------------------- | --------- |
| Número mínimo de subredes necesarias (identificadas) | **8**     |
| Número de subredes para un 30% de expansión          | **11**    |
| numero de subredes disponibles                       | 16        |




---

### Esto es solo para confirmar de que este bien:
#### 📌 PASO 2 — Proyección de Crecimiento al 30%

El enunciado indica considerar un **30% de crecimiento** a futuro. Aplicamos la fórmula:

$$Hosts_{futuro} = Hosts_{actual} \times 1{,}30$$

| N°  | Área            | Hosts actuales | × 1.30 | Hosts proyectados (↑)   |
| --- | --------------- | -------------- | ------ | ----------------------- |
| 1   | Alumnos         | 212            | 275.6  | **276**                 |
| 2   | Sistemas grande | 180            | 234    | 234                     |
| 3   | NO Docentes     | 75             | 97.5   | **98**                  |
| 4   | Docentes        | 60             | 78     | **78**                  |
| 5   | Academica       | 45             | 58.5   | **59**                  |
| 7   | Enlace R1↔R2    | 2              | 2.6    | **2** *(mínimo físico)* |
| 8   | Enlace R1↔R3    | 2              | 2.6    | **2**                   |
| 9   | Enlace R2↔R3    | 2              | 2.6    | **2**                   |


> **Red más grande proyectada: Alumnos con 276 hosts**

---

#### 📌 PASO 3 — Determinación del Espacio de Direccionamiento

**Dirección de Clase B
- Máscara de clase B: `255.255.0.0`
- Bits de host disponibles para subdivisión: **16 bits** (los dos últimos octetos)

####  📌 PASO 4 — Cálculo de Bits de Host (h)

Necesitamos que cada subred pueda alojar **al menos 276 hosts** (el área más grande).

Si pedimos prestado 4 bits para red nos quedaron 12 bits para host
por lo tanto 2^h -2 = 2^12 -2 =4094  >= 276  ✅ Sí alcanza


> **h = 12 bits de host** → cada subred soporta hasta **4094 hosts utilizables**

---



### 📌 ==PASO 3 — Construcción de la Máscara de Subred

**Distribución de bits:**

```
Clase B:  [ 8 bits red ][ 8 bits red ][ 8 bits host ] [ 8 bits host ]
255.255.0.0

pero como pedimos prestado 4 bits para subnetting nos quedaria algo asi
255.255.1111 | 0000 . 00000000

```

**En binario por octeto:**

```
Octeto 1:  11111111  = 255   (bits de red)
Octeto 2:  11111111  = 255   (bits de red)

trabajamos con el octeto 3
Octeto 3: 11110000 

128 64 32 16 8 4 2 1
  1  1  1  1 0 0 0 0   -> en hexa seria 128+64+32+16=240


Octeto 4:  00000000  = 0     (8 bits de host)
```

#### 🎯 Máscara de Subred = `255.255.240.0` = `/16 + 4 = /20`

```
255   .  255  .  240  .   0
11111111.11111111.1111 | 0000.00000000
```



### 📌 ==PASO 4 — Tabla Completa de Subredes

**Bloque (salto entre subredes):**

$$Bloque = 2^h = 2^{12} = 4096$$
h= cantindad de bits de host

ahora como Incremento es mayor a 256, 

para el 3er octeto =  4096/256=16 

la subrdedes van avanzado de 16 en 16


> [!note] ## El método del "Número Mágico" (256 - máscara)
Hacer $256 - 240 = 16$ es simplemente un atajo diseñado para hacerlo rápido mentalmente.
> 
> Este truco funciona porque el valor decimal de la máscara en el octeto interesante (240) es la representación exacta de los bits de red encendidos, dejando fuera los bits de host. Restarle ese valor a 256 siempre expone matemáticamente el tamaño del bloque sin tener que calcular potencias grandes o hacer divisiones largas 
>
En conclusión 
****Tu método ($2^h / 256$)** es la explicación técnica real de cómo las IPs se desbordan de un octeto a otro.
****El método de restar (256 - máscara)** es la herramienta práctica para calcularlo en segundos.


**Red base:** `172.18.0.0 /20`  
**Máscara:** `255.255.240.0`  
**Bloque en octeto 3:** 16 
**Hosts utilizables por subred:** 2^h -2=2^12 -2=4094

**Fórmula para cada subred # i:**
- **Dirección de Red:** `172.18.(i×16).0`
- **Primer host:** `172.18.(i×16).1`
- **Último host:** `172.18.(i×16+15).254`   ← bloque de 16 en 3er octeto: el último valor es i×16+15
- **Broadcast:** `172.18.(i×16+15).255`

#### Tabla completa de subredes (16 en total, índices 0 a 15):

> Con n=4 bits → 2⁴ = **16 subredes** disponibles. Se muestran todas.

| #   | Dir. de Red  | Primer Host  | Último Host    | Broadcast      |
| --- | ------------ | ------------ | -------------- | -------------- |
| 0   | 172.18.0.0   | 172.18.0.1   | 172.18.15.254  | 172.18.15.255  |
| 1   | 172.18.16.0  | 172.18.16.1  | 172.18.31.254  | 172.18.31.255  |
| 2   | 172.18.32.0  | 172.18.32.1  | 172.18.47.254  | 172.18.47.255  |
| 3   | 172.18.48.0  | 172.18.48.1  | 172.18.63.254  | 172.18.63.255  |
| 4   | 172.18.64.0  | 172.18.64.1  | 172.18.79.254  | 172.18.79.255  |
| 5   | 172.18.80.0  | 172.18.80.1  | 172.18.95.254  | 172.18.95.255  |
| 6   | 172.18.96.0  | 172.18.96.1  | 172.18.111.254 | 172.18.111.255 |
| 7   | 172.18.112.0 | 172.18.112.1 | 172.18.127.254 | 172.18.127.255 |
| 8   | 172.18.128.0 | 172.18.128.1 | 172.18.143.254 | 172.18.143.255 |
| 9   | 172.18.144.0 | 172.18.144.1 | 172.18.159.254 | 172.18.159.255 |
| 10  | 172.18.160.0 | 172.18.160.1 | 172.18.175.254 | 172.18.175.255 |
| 11  | 172.18.176.0 | 172.18.176.1 | 172.18.191.254 | 172.18.191.255 |
| 12  | 172.18.192.0 | 172.18.192.1 | 172.18.207.254 | 172.18.207.255 |
| 13  | 172.18.208.0 | 172.18.208.1 | 172.18.223.254 | 172.18.223.255 |
| 14  | 172.18.224.0 | 172.18.224.1 | 172.18.239.254 | 172.18.239.255 |
| 15  | 172.18.240.0 | 172.18.240.1 | 172.18.255.254 | 172.18.255.255 |

> **Total: 16 subredes disponibles** (subredes 0 a 15) — se necesitaban 8, sobran 8 para expansión ✅

---

### 📌 PASO 9 — Asignación de Subredes a cada Interfaz

De acuerdo a la numeración indicada en el diagrama de la topología (números 1 al 8), asignamos las subredes de la siguiente manera:

| Subred # | Área asignada / Enlace             | Hosts proyect. | Dir. de Red  | Broadcast      |
| :------: | ---------------------------------- | :------------: | ------------ | -------------- |
|  **0**   | Academica (R2-Eth1)                |       59       | 172.18.0.0   | 172.18.15.255  |
|  **1**   | Docentes (R2-Eth0)                 |       78       | 172.18.16.0  | 172.18.31.255  |
|    2     | Sistemas SW1+SW2 cascada (R3-Eth0) |      234       | 172.18.32.0  | 172.18.47.255  |
|  **3**   | NO Docentes (R3-Eth1)              |       98       | 172.18.48.0  | 172.18.63.255  |
|  **4**   | Alumnos (R1-Eth0)                  |      276       | 172.18.64.0  | 172.18.79.255  |
|  **5**   | Enlace R1(S0) ↔ R2(S1) (WAN)       |       2        | 172.18.80.0  | 172.18.95.255  |
|  **6**   | Enlace R2(S0) ↔ R3(S1) (WAN)       |       2        | 172.18.96.0  | 172.18.111.255 |
|  **7**   | Enlace R3(S0) ↔ R1(S1) (WAN)       |       2        | 172.18.112.0 | 172.18.127.255 |



---

### 📌 ==PASO 10 — Asignación de IP a Interfaces de Routers

> **Regla de asignación:** 
> - A las interfaces **Ethernet (Eth)** (gateways de las LAN) se les asigna la **primera IP usable** de su subred (`.1`).
> - A las interfaces **Seriales (S)** (enlaces punto a punto) se les asigna la **primera IP usable** (`.1`) a un extremo y la **segunda IP usable** (`.2`) al otro extremo de la subred correspondiente al enlace.

#### 🔴 Router 1

| Interfaz | Subred asignada   | IP de Interfaz | Descripción                 |
| -------- | ----------------- | -------------- | --------------------------- |
| **S0**   | Enlace R1↔R2 (#6) | `172.18.80.1`  | Punto a punto hacia R2 (S1) |
| **S1**   | Enlace R1↔R3 (#8) | 172.18.112.2   | Punto a punto hacia R3 (S0) |
| **Eth0** | Alumnos (#5)      | 172.18.64.1    | Gateway LAN Alumnos         |

#### 🔵 Router 2

| Interfaz | Subred asignada   | IP de Interfaz | Descripción                 |
| -------- | ----------------- | -------------- | --------------------------- |
| **S0**   | Enlace R2↔R3 (#7) | 172.18.96.1    | Punto a punto hacia R3 (S1) |
| **S1**   | Enlace R1↔R2 (#6) | 172.18.80.2    | Punto a punto hacia R1 (S0) |
| **Eth0** | Docentes (#2)     | 172.18.16.1    | Gateway LAN Docentes        |
| **Eth1** | Academica (#1)    | 172.18.0.1     | Gateway LAN Academica       |

#### 🟢 Router 3

| Interfaz | Subred asignada   | IP de Interfaz | Descripción                 |
| -------- | ----------------- | -------------- | --------------------------- |
| **S0**   | Enlace R1↔R3 (#8) | 172.18.112.1   | Punto a punto hacia R1 (S1) |
| **S1**   | Enlace R2↔R3 (#7) | 172.18.96.2    | Punto a punto hacia R2 (S0) |
| **Eth0** | Sistemas (#3)     | 172.18.32.1    | Gateway Sistemas (180H)     |
| **Eth1** | NO Docentes (#4)  | 172.18.48.1    | Gateway NO Docentes         |

---


---

## ✅ RESPUESTAS FINALES AL CUESTIONARIO DEL TP

| Pregunta del TP                             | Respuesta                                             |
| ------------------------------------------- | ----------------------------------------------------- |
| **Dirección de clase B**                    | `172.18.0.0` (privada, RFC 1918)                      |
| **Cantidad de Subredes (total disponible)** | **16 subredes** (2⁴)                                  |
| **Máscara de Subred calculada**             | **255.255.240.0 (/20)**                               |
| **Número mínimo de subredes necesarias**    | **8 subredes** (según diagrama provisto)              |
| **Subredes para expansión**                 | Sobran 8 subredes para expansión (total 16, uso 8)    |
| **Bits de subred (n)**                      | **4 bits**                                            |
| **Bits de host (h)**                        | **12 bits**                                           |
| **Hosts utilizables por subred**            | **4.094 hosts** (2¹² - 2)                             |
| **Bloque / Salto**                          | **16 en el 3er octeto** (4096 direcciones por subred) |

---

## 📖 RESUMEN FINAL PARA EL PARCIAL

### 🔑 Conceptos Clave

| Concepto         | Definición                                                                    |
| ---------------- | ----------------------------------------------------------------------------- |
| **Subred**       | División lógica de una red mayor, creada tomando bits del campo host          |
| **Máscara**      | Indica qué bits son red/subred (1s) y cuáles son host (0s)                    |
| **Broadcast**    | Última IP de una subred (todos los bits de host en 1). No se asigna a hosts   |
| **Dir. de Red**  | Primera IP de una subred (todos los bits de host en 0). No se asigna a hosts  |
| **Rango usable** | Desde (Dir. Red + 1) hasta (Broadcast - 1)                                    |
| **Clase B**      | Rango 128.x–191.x, máscara /16, hasta 65.534 hosts sin subnetting             |
| **Gateway**      | IP del router en cada subred. Generalmente la primera IP usable               |
| **Enlace WAN**   | Conexión serial punto a punto: necesita una subred con mínimo 2 hosts usables |

---

### 📐 Fórmulas para el Parcial

```
┌─────────────────────────────────────────────────────────┐
│  Subredes disponibles  = 2ⁿ                             │
│                                                         │
│  Bits a pedir prestados 2^n > N_subredes                │
│                                                         │
│  Hosts utilizables     = 2ʰ - 2                         │
│   h= los bits que quedaron de host                      │
│                                                         │
│    Total de hosts:    T = S × H = 2ⁿ × (2ʰ - 2)         │
│                                                         │
│     Bloque (salto) (incremento)  = 2ʰ                   │
│                                                         │
│  Dirección subred Nro k:    k × I   (k empieza en 0)    │
│  (octeto que cambia)                                    │
│  (si e le incremento I>256   I/256=                     │
│  -> y este sera el nuevo incremento)                    │                        │                                                         │
│  Broadcast subred Nro k:    (k+1) × I - 1               │
│                                                         │
│  Primer host válido:        Dir_Subred + 1              │
│  Último host válido:        Dir_Broadcast - 1           │
│                                                         │
│  Dirección de Subred (AND): IP AND Máscara (bit a bit)  │
│   (encnotrar la subred de una ip dada)                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

CALCULOS PARA EL INCREMENTO
> [!note] ## El método del "Número Mágico" (256 - máscara)
> 
> ****Tu método ($2^h / 256$)** es la explicación técnica real de cómo las IPs se desbordan de un octeto a otro.
****El método de restar (256 - máscara)** es la herramienta práctica para calcularlo en segundos.
> 
> si teniamos por ejemplo como mascara 255.255.240  -> 
> >  y hacemos $256 - 240 = 16$ es simplemente un atajo diseñado para hacerlo rápido mentalmente.
>   Incremetno I=16
>   
> Este truco funciona porque el valor decimal de la máscara en el octeto interesante (240) es la representación exacta de los bits de red encendidos, dejando fuera los bits de host. Restarle ese valor a 256 siempre expone matemáticamente el tamaño del bloque sin tener que calcular potencias grandes o hacer divisiones largas 




---

### 🏗️ Metodología para el Parcial (Checklist)

- [ ] **Leer el diagrama** → identificar TODAS las LANs + enlaces WAN punto a punto
- [ ] **Aplicar crecimiento** → multiplicar cada segmento por el factor indicado
- [ ] **Encontrar la red más grande** → determina el valor de **h**
- [ ] **Calcular h** → el menor h tal que `2ʰ - 2 ≥ hosts_max`
- [ ] **Calcular n** → `n = bits_clase - h`
- [ ] **Verificar subredes** → `2ⁿ ≥ cantidad_subredes_necesarias (con expansión)`
- [ ] **Construir la máscara** → n unos de subred + h ceros de host
- [ ] **Calcular el bloque** → `2ʰ` (tamaño de cada subred)
- [ ] **Hacer la tabla de subredes** → dirección red, rango hosts, broadcast
- [ ] **Asignar subredes** → LAN más grande = subred más baja (orden de preferencia)
- [ ] **Asignar IPs a routers** → primera IP usable de cada subred = gateway

---

### ⚡ Trucos Rápidos

1. **Los WAN siempre necesitan su propia subred** — aunque solo usen 2 IPs (una por extremo del serial), el enlace entre routers es una red independiente. Contarlos al hacer el relevamiento es obligatorio o el cálculo de subredes queda errado.
2. **Switches en cascada sin router = misma subred** — No importa cuántos switches estén encadenados: si no hay router en el medio, todos los hosts comparten el mismo dominio de broadcast → una sola subred.


---

### 🔢 Tabla de Referencia Rápida: Clase B (/16 base)

| n (bits subred) | Máscara           |  CIDR   | Subredes | h (bits host) | Hosts/subred |
| :-------------: | ----------------- | :-----: | :------: | :-----------: | :----------: |
|        1        | 255.255.128.0     |   /17   |    2     |      15       |    32.766    |
|        2        | 255.255.192.0     |   /18   |    4     |      14       |    16.382    |
|        3        | 255.255.224.0     |   /19   |    8     |      13       |    8.190     |
|        4        | 255.255.240.0     |   /20   |    16    |      12       |    4.094     |
|        5        | 255.255.248.0     |   /21   |    32    |      11       |    2.046     |
|        6        | 255.255.252.0     |   /22   |    64    |      10       |    1.022     |
|      **7**      | **255.255.254.0** | **/23** | **128**  |     **9**     |   **510**    |
|        8        | 255.255.255.0     |   /24   |   256    |       8       |     254      |
|        9        | 255.255.255.128   |   /25   |   512    |       7       |     126      |
|       10        | 255.255.255.192   |   /26   |   1024   |       6       |      62      |
|       11        | 255.255.255.224   |   /27   |   2048   |       5       |      30      |
|       12        | 255.255.255.240   |   /28   |   4096   |       4       |      14      |
|       13        | 255.255.255.248   |   /29   |   8192   |       3       |      6       |
|       14        | 255.255.255.252   |   /30   |  16384   |       2       |      2       |



---

