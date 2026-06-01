# REDES DE DATOS — Actividad de Direccionamiento IP
## Conceptos Generales

> **Materia:** Redes de Datos  
> **Unidad:** 00 — Conceptos Fundamentales  
> **Práctica:** P1-U00-P05 — Análisis Direccionamiento IPv4

---

## 🎯 Objetivos

- Reconocer las diferentes clases de direcciones IP
- Identificar la clase de una dirección según el número de red
- Saber diferenciar entre la dirección de red y la dirección de host
- Definir el intervalo de direcciones por defecto para cada clase
- Determinar cuántos bytes de una dirección IP corresponden a la parte de red y a la parte de host
- Identificar las direcciones de host IP asignables y no asignables

---



#  📌 Resumen de Conceptos Clave

```
┌─────────────────────────────────────────────────────────────────────┐
│               TABLA RESUMEN DE CLASES IPv4 (Classful)               │
├───────┬──────────────┬────────────┬───────────────┬──────┬──────────┤
│ Clase │ Rango 1° oct │ Estructura │ Máscara       │ Redes│ Hosts/Red│
├───────┼──────────────┼────────────┼───────────────┼──────┼──────────┤
│   A   │    1 – 126   │  R.H.H.H   │  255.0.0.0    │  126 │16.777.214│
│   B   │  128 – 191   │  R.R.H.H   │  255.255.0.0  │16.384│  65.534  │
│   C   │  192 – 223   │  R.R.R.H   │255.255.255.0  │2.097K│   254    │
│   D   │  224 – 239   │  Multicast │       —       │  —   │    —     │
│   E   │  240 – 255   │  Reservada │       —       │  —   │    —     │
├───────┼──────────────┼────────────┼───────────────┼──────┼──────────┤
│ Loop  │     127      │  Loopback  │       —       │  —   │    —     │
└───────┴──────────────┴────────────┴───────────────┴──────┴──────────┘
```
 
 Fórmulas importantes

- **Hosts asignables por red** = `2^n − 2`
  - Donde `n` = número de bits de la parte de host
  - Se restan 2: dirección de red (todo ceros) + broadcast (todo unos)

- **Dirección de Red** = Dirección IP con parte de host = `0...0`
- **Broadcast de Red** = Dirección IP con parte de host = `1...1` (= 255 por octeto)
- **Primera dirección válida** = Dirección de Red + 1
- **Última dirección válida** = Dirección de Broadcast − 1



###  **2. Repaso del Sistema Binario

El profesor inició la clase recordando cómo funciona el sistema de numeración posicional de base 2, ya que es la base indispensable para comprender las direcciones IP.

Repasó los valores posicionales de los 8 bits de un byte (1, 2, 4, 8, 16, 32, 64, 128)

![[{BCD028FD-1FC2-42E8-84F7-44CF934E859A}.png]]

ejemplo: (vemos las posiciones donde esta prendido sumamos ese numero)

00110010 → hexa →32+16+2=50

01000011= 64+2+1= 67

11111111=255

---

explicacion de hexa a decimal→

- **El número 120 (Ejemplo principal):** El profesor utilizó este número para mostrar el procedimiento paso a paso basándose en los valores de un byte (128, 64, 32, 16, 8, 4, 2, 1). Lo explicó de la siguiente forma:
    - **128:** Como es mayor que 120, ese bit queda apagado (0).
    - **64:** Como es menor, se enciende el bit (1) y se lo resta: 120 - 64 = 56.
        - 01
    - **32:** Como es menor que 56, se enciende el bit (1) y se lo resta: 56 - 32 = 24.
        - 011
    - **16:** Como es menor que 24, se enciende el bit (1) y se lo resta: 24 - 16 = 8.
        - 0111
    - **8:** Como es igual a 8, se enciende el bit (1) y la resta 8 - 8 da 0.
        - 01111
    - **4, 2 y 1:** Al haber llegado a 0, las posiciones restantes quedan apagadas (0).
    - Finalmente, comprobó el cálculo sumando los valores de los bits encendidos (64 + 32 + 16 + 8 = 120).
        - 01111000



## actvidad 1

### 📋 Resumen de Conceptos — Direccionamiento IP

| Concepto                   | Descripción                                                                               | Detalle clave                                              |
| -------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Dirección IP**           | Identificador único de 32 bits por dispositivo                                            | Notación decimal punteada: 4 octetos (ej: `135.24.56.245`) |
| **Dirección IP (Capa 3)**  | Lógica — modificable por software                                                         | Asignada por administrador. Jerarquía: **Red + Host**      |
| **Dirección MAC (Capa 2)** | Física — grabada en la NIC (48 bits)                                                      | Asignada de fábrica. Direccionamiento **plano**            |
| **Parte de Red**           | Identifica la red                                                                         | Asignada por **InterNIC**. Usada por routers para enrutar  |
| **Parte de Host**          | Identifica el dispositivo dentro de la red                                                | Asignada por el administrador de red                       |
| **Clase A**                | `0xxxxxxx` → <br><br>rango: 00000001 = 1  hasta  01111110 = 126<br><br>0 y 127 reservadas | Estructura `R.H.H.H` → máscara `255.0.0.0`                 |
| **Clase B**                | `10xxxxxx` → <br><br>rango: <br>10000000 = 128  hasta  <br>10111111 = 191<br>             | Estructura `R.R.H.H` → máscara `255.255.0.0`               |
| **Clase C**                | `110xxxxx` → <br><br>rango: 11000000 = 192  hasta  11011111 = 223                         | Estructura `R.R.R.H` → máscara `255.255.255.0`             |
| **Clase D**                | `1110xxxx` → rango `224–239`                                                              | **Multicast** — no asignable a hosts                       |
| **Clase E**                | `1111xxxx` → rango `240–255`                                                              | **Reservada** — no asignable a hosts                       |
| **Loopback**               | Bloque `127.x.x.x`                                                                        | Reservado para pruebas internas del propio dispositivo     |
| **Máscara de subred**      | Indica qué bits son de red y cuáles de host                                               | Bits en `1` = red / Bits en `0` = host                     |

| CLASE | Intervalo del 1er byte                                                                | estructura | mascara por defecto | cant de redes                                                           | cant host                 |
| ----- | ------------------------------------------------------------------------------------- | ---------- | ------------------- | ----------------------------------------------------------------------- | ------------------------- |
| A     | 0xxxxxxx (1er 0 la identifca)<br><br><br><br>rango: 1 a 126<br><br>0 y 127 reservadas | R.H.H.H    | 255.0.0.0           | (7 bits variables)<br>2^7=128<br><br>pero 0 y 127 reservadas<br><br>126 | 2^24-2=16.777.214 hosts** |
| B     | 10xxxxxx<br><br>rango: <br>10000000 = 128  hasta  <br>10111111 = 191<br>              | R.R.H.H    | 255.255.0.0         | 6 +8 bits variable<br><br>2^14=64                                       | 2^16-2=65.534             |
| C     | 110xxxxx<br><br>11000000 = 192  hasta  <br>11011111 = 223                             | R.R.R.H    | 255.255.255.0       | 5+8+8 bits variables<br><br>`2^21 = 2.097.152 redes`                    | `2^8 − 2 = 254 hosts`     |
|       |                                                                                       |            |                     |                                                                         |                           |
### ❓ ==Preguntas de la Actividad 1

#### Pregunta 1: ==¿Cuál es el intervalo binario del primer byte de todas las direcciones IP clase "C" posibles?

**Respuesta:**

Las direcciones Clase C tienen los primeros 3 bits fijos en `110`, y los 5 restantes pueden variar:

```
Mínimo: 110 00000 = 192 (decimal)
Máximo: 110 11111 = 223 (decimal)
```

> El intervalo binario del primer byte de Clase C va de **`11000000`** (192) a **`11011111`** (223).

---

#### Pregunta 2: ==¿Cuál/es byte o bytes representan la parte que corresponde a la red de una dirección IP clase C?

**Respuesta:**

En una dirección Clase C la estructura es `R.R.R.H`:

```
192 . 168 . 1 . 100
 ↑      ↑    ↑    ↑
Red    Red  Red  Host
(1°)   (2°) (3°) (4°)
```

> Los **tres primeros bytes (1°, 2° y 3° octeto)** representan la **parte de red** en Clase C.

---

#### Pregunta 3: ¿Qué byte o bytes representan la parte que corresponde al host de una dirección IP clase "B"?

**Respuesta:**

En una dirección Clase B la estructura es `R.R.H.H`:

```
172 . 16 . 5 . 100
 ↑     ↑    ↑    ↑
Red   Red  Host Host
(1°)  (2°) (3°) (4°)
```

> Los **dos últimos bytes (3° y 4° octeto)** representan la **parte de host** en Clase B.

---

#### Pregunta 4: ==¿Qué característica particular distingue a las direcciones de red de las máscaras de subred?

**Respuesta:**

Aunque ambas parecen similares visualmente, existen diferencias fundamentales:

| Característica      | Dirección de Red              | Máscara de Subred                      |
| ------------------- | ----------------------------- | -------------------------------------- |
| **Propósito**       | Identifica una red específica | Indica qué parte es red y cuál es host |
| **Parte de host**   | Todos los bits en **0**       | Todos los bits en **0**                |
| **Parte de red**    | Contiene el número de red     | Todos los bits en **1**                |
| **Ejemplo Clase B** | `172.16.0.0`                  | `255.255.0.0`                          |

> La característica distintiva es que **la máscara de subred no representa una dirección de red real**: sus bits de red son todos **unos** (255), mientras que la dirección de red tiene el número real asignado a esa red. Además, las máscaras no se asignan a interfaces de dispositivos —son solo una herramienta matemática para separar la parte de red de la parte de host.

---

## actividad  2 

Dada una dirección IP de host, para cualquier clase debemos identificar:

| Concepto                             | Definición                               | Parte de Host                                       |
| ------------------------------------ | ---------------------------------------- | --------------------------------------------------- |
| **Dirección de Red**                 | Identifica la red (no asignable a hosts) | Todos `0`                                           |
| **Primera dirección válida de host** | Primer host asignable                    | Parte de host = `00...001`                          |
| **Broadcast**                        | Envío a todos los hosts de la red        | Todos `1` (= 255)                                   |
| **Máscara de subred**                | Separador red/host                       | Parte de red = todos `1`, parte de host = todos `0` |

Para resolver cada dirección:

1. **Identificar la clase** mirando el primer octeto
2. **Determinar la parte de red** según la clase (R.H.H.H / R.R.H.H / R.R.R.H)
3. **Dirección de red** = parte de red + parte de host en todo `0`
4. **Primera dirección válida** = dirección de red + 1 en el último octeto
5. **Broadcast** = parte de red + parte de host en todo `255`
6. **Máscara** = según clase (255.0.0.0 / 255.255.0.0 / 255.255.255.0)


## actividad 3
Una dirección IP es **NO asignable** si:

| Causa de NO asignabilidad                                           | Ejemplo           |
| ------------------------------------------------------------------- | ----------------- |
| Es una **dirección de red** (parte de host = todo ceros)            | `192.168.1.0`     |
| Es una **dirección de broadcast** (parte de host = todo unos = 255) | `192.168.1.255`   |
| Pertenece al rango de **loopback** (127.x.x.x)                      | `127.0.0.1`       |
| Pertenece a **Clase D** (Multicast, 224–239)                        | `224.0.0.1`       |
| Pertenece a **Clase E** (Reservada, 240–255)                        | `245.1.1.1`       |
| Contiene un octeto con valor **mayor a 255** (inválida)             | `189.34.356.176`  |
| Es la dirección de **broadcast universal**                          | `255.255.255.255` |

> **Regla para detectar broadcast clásico:** Si el/los byte(s) de host valen `255` o `0` según la clase, la dirección no es asignable.

---

### Metodología paso a paso para cada dirección

Para cada dirección:
1. Verificar que los octetos sean válidos (0-255)
2. Identificar la clase por el primer octeto
3. Determinar la parte de host según la clase
4. Verificar si la parte de host es todo `0` (dirección de red) o todo `255` (broadcast)
5. Verificar rangos especiales (127, Clase D, Clase E)
6. Si NO es asignable, proponer una dirección asignable en la misma red


# actividades desarrolladas:
# ✏️ ==ACTIVIDAD Nro. 1 — Tabla de Clases de Direcciones IP (intervalo 1er byte, estructura, mascara por defecto, cantidad de redes y candtidad de hosts)

### 📖 Marco Teórico

#### ¿Qué es una dirección IP?

Una **dirección IP (Internet Protocol)** es un identificador único de **32 bits** que se asigna a cada dispositivo conectado a una red. Se representa en **notación decimal punteada**: cuatro grupos de 8 bits (octetos), separados por puntos.

**Ejemplo:** `135.24.56.245`

```
135       .    24      .    56      .   245
10000111       00011000     00111000    11110101
 Octeto 1       Octeto 2     Octeto 3    Octeto 4
```

#### Dirección Lógica vs. Dirección Física

| Característica | Dirección IP (Capa 3)      | Dirección MAC (Capa 2)       |
| -------------- | -------------------------- | ---------------------------- |
| Tipo           | Lógica (modificable)       | Física (grabada en hardware) |
| Tamaño         | 32 bits                    | 48 bits                      |
| Asignación     | Por software/administrador | De fábrica en la NIC         |
| Uso            | Identificación de red/host | Comunicación en la LAN local |
| Jerarquía      | **Jerárquica**             | **Plana**                    |

> La combinación de ambas (IP + MAC) permite **encaminar paquetes** hacia el destino correcto a través de múltiples redes.

---

#### Estructura de una Dirección IP: Red + Host

Toda dirección IP se divide en **dos partes**:

```
┌──────────────────────┬──────────────────────┐
│    PARTE DE RED      │    PARTE DE HOST     │
│  (identifica la red) │ (identifica el host) │
└──────────────────────┴──────────────────────┘
```

- **Parte de Red:** Asignada por el **InterNIC** (Internet Network Information Center) a organizaciones. Los routers la usan para enrutar paquetes entre redes.
- **Parte de Host:** Asignada por el administrador de red dentro de cada organización. Identifica un dispositivo específico (PC, servidor, impresora, router, etc.).

---

#### Clases de Direcciones IP (Classful)

El sistema **classful** divide el espacio de direcciones IPv4 en 5 clases según el valor del **primer byte (octeto)**. Cada clase tiene un tamaño diferente para la parte de red y la parte de host.

#### Regla de identificación por el primer bit(s):

```
Clase A: El primer bit es 0       → 0xxxxxxx → 1 a 126 (en decimal)
Clase B: Los dos primeros bits son 10  → 10xxxxxx → 128 a 191
Clase C: Los tres primeros bits son 110 → 110xxxxx → 192 a 223
Clase D: Los cuatro primeros bits son 1110 → Multicast (224 a 239)
Clase E: Los cuatro primeros bits son 1111 → Reservada (240 a 255)
```

> ⚠️ **Nota especial:** El bloque `127.x.x.x` está **reservado para loopback** (prueba interna del propio dispositivo). No se puede asignar a hosts de red.

---

#### Máscara de Subred por Defecto

La **máscara de subred** indica qué parte de la dirección IP corresponde a la red y qué parte al host:
- **Bits en 1** (= 255 en decimal) → corresponden a la **parte de red**
- **Bits en 0** (= 0 en decimal) → corresponden a la **parte de host**

---



| CLASE | Intervalo del 1er byte                                                                | estructura | mascara por defecto | cant de redes                                                           | cant host                 |
| ----- | ------------------------------------------------------------------------------------- | ---------- | ------------------- | ----------------------------------------------------------------------- | ------------------------- |
| A     | 0xxxxxxx (1er 0 la identifca)<br><br><br><br>rango: 1 a 126<br><br>0 y 127 reservadas | R.H.H.H    | 255.0.0.0           | (7 bits variables)<br>2^7=128<br><br>pero 0 y 127 reservadas<br><br>126 | 2^24-2=16.777.214 hosts** |
| B     | 10xxxxxx<br><br>128-191                                                               | R.R.H.H    | 255.255.0.0         | 6 +8 bits variable<br><br>2^14=64                                       | 2^16-2=65.534             |
| C     | 110xxxxx<br><br>11000000 = 192  hasta  <br>11011111 = 223                             | R.R.R.H    | 255.255.255.0       | 5+8+8 bits variables<br><br>`2^21 = 2.097.152 redes`                    | `2^8 − 2 = 254 hosts`     |

## Desarrollo paso a paso

### CLASE A

**Primer octeto:** Solo el **bit más significativo** identifica la clase → debe ser `0`.

```
0xxxxxxx → 

rango: 00000001 = 1  hasta  01111110 = 126
```

- **Estructura:** `[Red].[Host].[Host].[Host]` → **1 byte de red, 3 bytes de host**
- **Máscara por defecto:** `255.0.0.0`
- **Cantidad de redes:** El primer octeto va de 1 a 126 → **126 redes**
	- porque los bits que varian son 7 -> 2^7 =128 
	- PERO (Se excluye el 0 —red reservada— y el 127 —loopback—),
	- por lo tanto 126
- **Hosts por red:** Los 3 bytes (24 bits) de host dan `2^24 = 16.777.216` combinaciones.
  - Se restan **2**: la dirección de red (todos ceros en la parte de host) y la de broadcast (todos unos).
  - **Hosts asignables = 2^24 − 2 = 16.777.214 hosts**

### CLASE B

**Primeros dos bits:** deben ser `10`.

```
10xxxxxx → 

rango: 10000000 = 128  hasta  10111111 = 191
```

- **Estructura:** `[Red].[Red].[Host].[Host]` → **2 bytes de red, 2 bytes de host**
- **Máscara por defecto:** `255.255.0.0`
- **Cantidad de redes:** Los bits variables del primer octeto son 6 bits, más los 8 del segundo octeto → `2^14 = 16.384 redes`
- **Hosts por red:** 2 bytes de host → `2^16 − 2 = 65.534 hosts`

### CLASE C

**Primeros tres bits:** deben ser `110`.

```
110xxxxx → 

rango: 11000000 = 192  hasta  11011111 = 223
```

- **Estructura:** `[Red].[Red].[Red].[Host]` → **3 bytes de red, 1 byte de host**
- **Máscara por defecto:** `255.255.255.0`
- **Cantidad de redes:** 5 bits variables en el primer octeto + 8 del segundo + 8 del tercero → `2^21 = 2.097.152 redes`
- **Hosts por red:** 1 byte de host → `2^8 − 2 = 254 hosts`

---

### ✅ Tabla Completada — Actividad 1

| Clase | Intervalo 1er. byte (decimal) |        Parte de Red / Host        | Máscara de subred por defecto | Cantidad de redes | Hosts por red |
| :---: | :---------------------------: | :-------------------------------: | :---------------------------: | :---------------: | :-----------: |
| **A** |            1 – 126            | **R**.\*H\*.\*H\*.\*H\* (1R / 3H) |           255.0.0.0           |        126        |  16.777.214   |
| **B** |           128 – 191           | **R**.**R**.\*H\*.\*H\* (2R / 2H) |          255.255.0.0          |      16.384       |    65.534     |
| **C** |           192 – 223           | **R**.**R**.**R**.\*H\* (3R / 1H) |         255.255.255.0         |     2.097.152     |      254      |

> **Referencia:** R = byte de Red | H = byte de Host

---

## ❓ ==Preguntas de la Actividad 1

### Pregunta 1: ==¿Cuál es el intervalo binario del primer byte de todas las direcciones IP clase "C" posibles?

**Respuesta:**

Las direcciones Clase C tienen los primeros 3 bits fijos en `110`, y los 5 restantes pueden variar:

```
Mínimo: 110 00000 = 192 (decimal)
Máximo: 110 11111 = 223 (decimal)
```

> El intervalo binario del primer byte de Clase C va de **`11000000`** (192) a **`11011111`** (223).

---

### Pregunta 2: ==¿Cuál/es byte o bytes representan la parte que corresponde a la red de una dirección IP clase C?

**Respuesta:**

En una dirección Clase C la estructura es `R.R.R.H`:

```
192 . 168 . 1 . 100
 ↑      ↑    ↑    ↑
Red    Red  Red  Host
(1°)   (2°) (3°) (4°)
```

> Los **tres primeros bytes (1°, 2° y 3° octeto)** representan la **parte de red** en Clase C.

---

### Pregunta 3: ¿Qué byte o bytes representan la parte que corresponde al host de una dirección IP clase "B"?

**Respuesta:**

En una dirección Clase B la estructura es `R.R.H.H`:

```
172 . 16 . 5 . 100
 ↑     ↑    ↑    ↑
Red   Red  Host Host
(1°)  (2°) (3°) (4°)
```

> Los **dos últimos bytes (3° y 4° octeto)** representan la **parte de host** en Clase B.

---

### Pregunta 4: ==¿Qué característica particular distingue a las direcciones de red de las máscaras de subred?

**Respuesta:**

Aunque ambas parecen similares visualmente, existen diferencias fundamentales:

| Característica      | Dirección de Red              | Máscara de Subred                      |
| ------------------- | ----------------------------- | -------------------------------------- |
| **Propósito**       | Identifica una red específica | Indica qué parte es red y cuál es host |
| **Parte de host**   | Todos los bits en **0**       | Todos los bits en **0**                |
| **Parte de red**    | Contiene el número de red     | Todos los bits en **1**                |
| **Ejemplo Clase B** | `172.16.0.0`                  | `255.255.0.0`                          |

> La característica distintiva es que **la máscara de subred no representa una dirección de red real**: sus bits de red son todos **unos** (255), mientras que la dirección de red tiene el número real asignado a esa red. Además, las máscaras no se asignan a interfaces de dispositivos —son solo una herramienta matemática para separar la parte de red de la parte de host.

---

# ✏️ ==ACTIVIDAD Nro. 2 — Identificación de Partes y Direcciones Especiales

### Marco Teórico previo

Dada una dirección IP de host, para cualquier clase debemos identificar:

| Concepto                             | Definición                               | Parte de Host                                       |
| ------------------------------------ | ---------------------------------------- | --------------------------------------------------- |
| **Dirección de Red**                 | Identifica la red (no asignable a hosts) | Todos `0`                                           |
| **Primera dirección válida de host** | Primer host asignable                    | Parte de host = `00...001`                          |
| **Broadcast**                        | Envío a todos los hosts de la red        | Todos `1` (= 255)                                   |
| **Máscara de subred**                | Separador red/host                       | Parte de red = todos `1`, parte de host = todos `0` |

### Metodología paso a paso

Para resolver cada dirección:

1. **Identificar la clase** mirando el primer octeto
2. **Determinar la parte de red** según la clase (R.H.H.H / R.R.H.H / R.R.R.H)
3. **Dirección de red** = parte de red + parte de host en todo `0`
4. **Primera dirección válida** = dirección de red + 1 en el último octeto
5. **Broadcast** = parte de red + parte de host en todo `255`
6. **Máscara** = según clase (255.0.0.0 / 255.255.0.0 / 255.255.255.0)

---

### Resolución: `193.45.5.79`

**Paso 1 — Identificar la clase:**
- Primer octeto = **193** → está entre 192 y 223 → **Clase C**

**Paso 2 — Estructura Clase C:** `R . R . R . H`
```
193 . 45 . 5 . 79
Red   Red  Red  Host
```

**Paso 3 — Dirección de Red:** Se pone `0` en la parte de host:
```
193.45.5.0
```

**Paso 4 — Primera dirección válida:** Dirección de red + 1 en último octeto:
```
193.45.5.1
```

**Paso 5 — Broadcast:** Se pone `255` en la parte de host:
```
193.45.5.255
```

**Paso 6 — Máscara por defecto Clase C:**
```
255.255.255.0
```

---

### Resolución: `126.10.2.25`

**Paso 1 — Identificar la clase:**
- Primer octeto = **126** → está entre 1 y 126 → **Clase A**

**Paso 2 — Estructura Clase A:** `R . H . H . H`
```
126 . 10 . 2 . 25
Red   Host Host Host
```

**Paso 3 — Dirección de Red:**
```
126.0.0.0
```

**Paso 4 — Primera dirección válida:**
```
126.0.0.1
```

**Paso 5 — Broadcast:**
```
126.255.255.255
```

**Paso 6 — Máscara por defecto Clase A:**
```
255.0.0.0
```

---

### Resolución: `128.240.240.240`

**Paso 1 — Identificar la clase:**
- Primer octeto = **128** → está entre 128 y 191 → **Clase B**

**Paso 2 — Estructura Clase B:** `R . R . H . H`
```
128 . 240 . 240 . 240
Red    Red   Host  Host
```

**Paso 3 — Dirección de Red:**
```
128.240.0.0
```

**Paso 4 — Primera dirección válida:**
```
128.240.0.1
```

**Paso 5 — Broadcast:**
```
128.240.255.255
```

**Paso 6 — Máscara por defecto Clase B:**
```
255.255.0.0
```

---

### Resolución: `20.10.5.90`

**Paso 1 — Identificar la clase:**
- Primer octeto = **20** → está entre 1 y 126 → **Clase A**

**Paso 2 — Estructura Clase A:** `R . H . H . H`
```
20 . 10 . 5 . 90
Red  Host Host Host
```

**Paso 3 — Dirección de Red:**
```
20.0.0.0
```

**Paso 4 — Primera dirección válida:**
```
20.0.0.1
```

**Paso 5 — Broadcast:**
```
20.255.255.255
```

**Paso 6 — Máscara por defecto Clase A:**
```
255.0.0.0
```

---

### Resolución: `180.10.9.5`

**Paso 1 — Identificar la clase:**
- Primer octeto = **180** → está entre 128 y 191 → **Clase B**

**Paso 2 — Estructura Clase B:** `R . R . H . H`
```
180 . 10 . 9 . 5
Red   Red  Host Host
```

**Paso 3 — Dirección de Red:**
```
180.10.0.0
```

**Paso 4 — Primera dirección válida:**
```
180.10.0.1
```

**Paso 5 — Broadcast:**
```
180.10.255.255
```

**Paso 6 — Máscara por defecto Clase B:**
```
255.255.0.0
```

---

### ✅ Tabla Completada — Actividad 2

| Dirección IP del host | Clase | Dirección de Red | Primera dirección válida de host | Dirección de broadcast de red | Máscara de subred por defecto |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `193.45.5.79` | C | `193.45.5.0` | `193.45.5.1` | `193.45.5.255` | `255.255.255.0` |
| `126.10.2.25` | A | `126.0.0.0` | `126.0.0.1` | `126.255.255.255` | `255.0.0.0` |
| `128.240.240.240` | B | `128.240.0.0` | `128.240.0.1` | `128.240.255.255` | `255.255.0.0` |
| `20.10.5.90` | A | `20.0.0.0` | `20.0.0.1` | `20.255.255.255` | `255.0.0.0` |
| `180.10.9.5` | B | `180.10.0.0` | `180.10.0.1` | `180.10.255.255` | `255.255.0.0` |

---

# ✏️ ==ACTIVIDAD Nro. 3 — Direcciones Asignables y No Asignables

### Marco Teórico previo

Una dirección IP es **NO asignable** si:

| Causa de NO asignabilidad                                           | Ejemplo           |
| ------------------------------------------------------------------- | ----------------- |
| Es una **dirección de red** (parte de host = todo ceros)            | `192.168.1.0`     |
| Es una **dirección de broadcast** (parte de host = todo unos = 255) | `192.168.1.255`   |
| Pertenece al rango de **loopback** (127.x.x.x)                      | `127.0.0.1`       |
| Pertenece a **Clase D** (Multicast, 224–239)                        | `224.0.0.1`       |
| Pertenece a **Clase E** (Reservada, 240–255)                        | `245.1.1.1`       |
| Contiene un octeto con valor **mayor a 255** (inválida)             | `189.34.356.176`  |
| Es la dirección de **broadcast universal**                          | `255.255.255.255` |

> **Regla para detectar broadcast clásico:** Si el/los byte(s) de host valen `255` o `0` según la clase, la dirección no es asignable.

---

### Metodología paso a paso para cada dirección

Para cada dirección:
1. Verificar que los octetos sean válidos (0-255)
2. Identificar la clase por el primer octeto
3. Determinar la parte de host según la clase
4. Verificar si la parte de host es todo `0` (dirección de red) o todo `255` (broadcast)
5. Verificar rangos especiales (127, Clase D, Clase E)
6. Si NO es asignable, proponer una dirección asignable en la misma red

---

### Resolución: `30.255.0.0`

**Clase:** Primer octeto = 30 → **Clase A** → estructura: `R.H.H.H`
- Parte de Red: `30`
- Parte de Host: `255.0.0`

**Análisis:** La parte de host NO es todo ceros ni todo unos (255.255.255).

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase A en la red `30.0.0.0`

**Nota:** Aunque el segundo octeto sea 255, la parte de host completa es `255.0.0` ≠ `255.255.255` (broadcast), por lo tanto **sí es asignable**.

---

### Resolución: `192.255.255.38`

**Clase:** Primer octeto = 192 → **Clase C** → estructura: `R.R.R.H`
- Parte de Red: `192.255.255`
- Parte de Host: `38`

**Análisis:** La parte de host es `38` ≠ `0` y ≠ `255`.

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase C en la red `192.255.255.0`

---

### Resolución: `196.200.253.0`

**Clase:** Primer octeto = 196 → **Clase C** → estructura: `R.R.R.H`
- Parte de Red: `196.200.253`
- Parte de Host: `0`

**Análisis:** La parte de host es **`0`** → es la **dirección de red** de la subred `196.200.253.0`.

> ❌ **NO ES ASIGNABLE** — Es la dirección de red (parte de host = 0)

**Dirección asignable sugerida:** `196.200.253.1` (primera dirección válida de host)

---

### Resolución: `130.0.0.145`

**Clase:** Primer octeto = 130 → **Clase B** → estructura: `R.R.H.H`
- Parte de Red: `130.0`
- Parte de Host: `0.145`

**Análisis:** La parte de host es `0.145`. Para Clase B, el broadcast sería `255.255` y la dirección de red sería `0.0`. Aquí es `0.145` → ni todo ceros ni todo unos.

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase B en la red `130.0.0.0`

---

### Resolución: `189.34.356.176`

**Clase:** Primer octeto = 189 → **Clase B** → estructura: `R.R.H.H`

**Análisis:** El tercer octeto es **356**, que **excede el valor máximo de 255** para un octeto (un byte solo puede representar valores del 0 al 255).

> ❌ **NO ES ASIGNABLE** — La dirección es **inválida** porque el tercer octeto (356) supera el valor máximo permitido (255)

**Dirección asignable sugerida:** Corregir el octeto inválido → `189.34.100.176` (dirección válida y asignable)

---

### Resolución: `255.255.255.255`

**Clase:** Primer octeto = 255 → **No es Clase A, B ni C** (está en el rango de Clase E, 240–255)

**Análisis:** Además, `255.255.255.255` es la **dirección de broadcast universal** (limited broadcast) — envía a todos los hosts de cualquier red local.

> ❌ **NO ES ASIGNABLE** — Es la dirección de **broadcast universal** (limited broadcast). No pertenece a ninguna red asignable.

**Dirección asignable sugerida:** No aplica directamente (no es de Clase A/B/C). Una alternativa de ejemplo: `192.168.1.1`

---

### Resolución: `127.56.34.0`

**Clase:** Primer octeto = 127 → **Rango reservado para Loopback**

**Análisis:** El bloque `127.0.0.0/8` está completamente reservado para pruebas internas del propio dispositivo (loopback). La dirección más conocida es `127.0.0.1`.

> ❌ **NO ES ASIGNABLE** — Pertenece al rango **loopback** (127.x.x.x), que está reservado y no se puede asignar a interfaces reales.

**Dirección asignable sugerida:** `10.56.34.1` (misma estructura pero en Clase A asignable)

---

### Resolución: `245.156.217.73`

**Clase:** Primer octeto = 245 → está entre 240 y 255 → **Clase E** (reservada para investigación y uso futuro)

**Análisis:** Las direcciones de Clase E no se pueden asignar a dispositivos en redes comerciales/convencionales.

> ❌ **NO ES ASIGNABLE** — Pertenece a **Clase E** (rango 240–255), que es de uso reservado/experimental y no se asigna a hosts.

**Dirección asignable sugerida:** `193.156.217.73` (Clase C, mismos octetos de host)

---

### Resolución: `10.255.255.255`

**Clase:** Primer octeto = 10 → **Clase A** → estructura: `R.H.H.H`
- Parte de Red: `10`
- Parte de Host: `255.255.255`

**Análisis:** La parte de host es `255.255.255` → **todos los bits de host en 1** → es la dirección de **broadcast de la red 10.0.0.0**.

> ❌ **NO ES ASIGNABLE** — Es la dirección de **broadcast** de la red `10.0.0.0` (Clase A)

**Dirección asignable sugerida:** `10.255.255.1` (último host válido de la red 10.0.0.0 con tercer octeto 255)

---

### Resolución: `120.0.0.255`

**Clase:** Primer octeto = 120 → **Clase A** → estructura: `R.H.H.H`
- Parte de Red: `120`
- Parte de Host: `0.0.255`

**Análisis:** La parte de host es `0.0.255`. El broadcast de Clase A requiere que la parte de host sea `255.255.255`. Aquí es `0.0.255`, que **no es ni todo ceros ni todo unos** → es un host válido.

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase A en la red `120.0.0.0`

---

### Resolución: `172.255.254.0`

**Clase:** Primer octeto = 172 → está entre 128 y 191 → **Clase B** → estructura: `R.R.H.H`
- Parte de Red: `172.255`
- Parte de Host: `254.0`

**Análisis:** La parte de host es `254.0`. No es `0.0` (dirección de red) ni `255.255` (broadcast).

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase B en la red `172.255.0.0`

---

### Resolución: `168.1.0.255`

**Clase:** Primer octeto = 168 → está entre 128 y 191 → **Clase B** → estructura: `R.R.H.H`
- Parte de Red: `168.1`
- Parte de Host: `0.255`

**Análisis:** La parte de host es `0.255`. El broadcast Clase B sería `255.255` y la dirección de red sería `0.0`. `0.255` no coincide con ninguno de los dos.

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase B en la red `168.1.0.0`

---

### Resolución: `223.255.255.250`

**Clase:** Primer octeto = 223 → está entre 192 y 223 → **Clase C** → estructura: `R.R.R.H`
- Parte de Red: `223.255.255`
- Parte de Host: `250`

**Análisis:** La parte de host es `250`. No es `0` (dirección de red) ni `255` (broadcast).

> ✅ **ES ASIGNABLE** — Es una dirección de host válida de Clase C en la red `223.255.255.0`

---

## ✅ Tabla Completada — Actividad 3

| Dirección IP | ¿Es asignable? | ¿Por qué sí? o ¿Por qué no? | Dirección asignable (si corresponde) |
|:---:|:---:|---|:---:|
| `30.255.0.0` | ✅ **SÍ** | Clase A. Parte de host (`255.0.0`) no es todo ceros ni todo unos | — |
| `192.255.255.38` | ✅ **SÍ** | Clase C. Parte de host (`38`) no es `0` ni `255` | — |
| `196.200.253.0` | ❌ **NO** | Clase C. Parte de host es `0` → es la **dirección de red** | `196.200.253.1` |
| `130.0.0.145` | ✅ **SÍ** | Clase B. Parte de host (`0.145`) no es `0.0` ni `255.255` | — |
| `189.34.356.176` | ❌ **NO** | El tercer octeto (356) es **inválido** (supera 255) | `189.34.100.176` |
| `255.255.255.255` | ❌ **NO** | Es el **broadcast universal** (limited broadcast). Clase E | — |
| `127.56.34.0` | ❌ **NO** | Primer octeto 127 → rango **loopback** reservado | `10.56.34.1` |
| `245.156.217.73` | ❌ **NO** | Primer octeto 245 → **Clase E** (rango reservado/experimental) | `193.156.217.73` |
| `10.255.255.255` | ❌ **NO** | Clase A. Parte de host (`255.255.255`) = todos unos → **broadcast** | `10.255.255.1` |
| `120.0.0.255` | ✅ **SÍ** | Clase A. Parte de host (`0.0.255`) no es `0.0.0` ni `255.255.255` | — |
| `172.255.254.0` | ✅ **SÍ** | Clase B. Parte de host (`254.0`) no es `0.0` ni `255.255` | — |
| `168.1.0.255` | ✅ **SÍ** | Clase B. Parte de host (`0.255`) no es `0.0` ni `255.255` | — |
| `223.255.255.250` | ✅ **SÍ** | Clase C. Parte de host (`250`) no es `0` ni `255` | — |

---


---

*Práctica elaborada sobre el material: P1-U00-P05 — Análisis Direccionamiento IPv4*  
*Redes de Datos — UTN*