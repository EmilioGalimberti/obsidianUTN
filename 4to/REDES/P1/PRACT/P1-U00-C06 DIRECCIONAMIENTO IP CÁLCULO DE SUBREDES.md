# P1-U00-C06 · DIRECCIONAMIENTO IP — CÁLCULO DE SUBREDES

> **Materia:** Redes de Datos  
> **Unidad:** 00 — Fundamentos de Redes  
> **Práctica:** P06 — Diseño de Direccionamiento IPv4 / Subredes  
> **Fuente:** P1-U00-P06-Diseño de Direccionamiento_IPv4_Subredes.pdf


![[P1-U00-C06.m4a]]

---

## 📋 OBJETIVOS DE LA PRÁCTICA

- Establecer un esquema de direccionamiento IP utilizando subredes.
- Realizar el cálculo de subredes en función de la cantidad de subredes necesarias o según la cantidad de hosts por subred.
- Determinar las direcciones de subred y de broadcast de una subred determinada.
- Descubrir las ventajas y desventajas de la implementación de subredes.
- Comprender el proceso de cálculo de subredes Clase C y Clase B.

![[P1-U00-P06-Diseño de Direccionamiento_IPv4_Subredes.pdf]]

---

# Resumen
## 📌 Errores Frecuentes a Evitar

| Error                                    | Corrección                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------- |
| Asumir que las subredes empiezan desde 1 | Las subredes se numeran desde **0**. Usar la fórmula: Dir = Base + **k** × Incremento |
| No restar 2 al calcular hosts            | Siempre restar 1 por dirección de red y 1 por broadcast                               |
| Confundir el octeto afectado en Clase B  | Los bits prestados van al **tercer octeto** (el primer octeto de host)                |
| Identificar la clase por la máscara      | La clase se determina por el **primer octeto de la IP**, no por la máscara            |
| Asumir subredes sin verificar            | Si máscara aplicada ≠ máscara natural → hay subredes                                  |
| Olvidar el gateway al configurar un host | Sin gateway, no hay comunicación fuera de la subred                                   |

## 🔢 FÓRMULAS FUNDAMENTALES


```
┌─────────────────────────────────────────────────────────────────┐
│  FÓRMULAS CLAVE DE SUBNETTING                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Bits a pedir prestados:    2ⁿ > N_subredes                     │
│                                                                 │
│  Cantidad de subredes:      S = 2ⁿ                              │
│                                                                 │
│  Hosts válidos por subred:      H = 2ʰ - 2                      │
│     donde h = bits_host_originales - n                          │
│                                                                 │
│es -2 por que no es valido para host direct de red y de brodcast │
│                                                                 │
│  Total de hosts:    T = S × H = 2ⁿ × (2ʰ - 2)                   │
│                                                                 │
│  Incremento de bloque:      I = 2ʰ                              │
│  (cada cuanto van saltando las subredes)                        │
│                                                                 │
│  Dirección subred Nro k:    k × I   (k empieza en 0)            │
│  (octeto que cambia)                                            │
│  (si e le incremento I>256   I/256=                             │
│  -> y este sera el nuevo incremento)                            │             │                                                                 │
│  Broadcast subred Nro k:    (k+1) × I - 1                       │
│                                                                 │
│  Primer host válido:        Dir_Subred + 1                      │
│  Último host válido:        Dir_Broadcast - 1                   │
│                                                                 │
│  Dirección de Subred (AND): IP AND Máscara (bit a bit)          │
│   (encnotrar la subred de una ip dada)                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

atento a que en nuestra clase comenzamos como la primera subred como la 0, 
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

## 🔑 Conceptos Clave

| Concepto                   | Definición                                                        |
| -------------------------- | ----------------------------------------------------------------- |
| **Dirección IP**           | Identificador de 32 bits en formato decimal punteado              |
| **Clase A**                | Primer octeto 1–126, máscara natural /8                           |
| **Clase B**                | Primer octeto 128–191, máscara natural /16                        |
| **Clase C**                | Primer octeto 192–223, máscara natural /24                        |
| **Subnetting**             | División de una red en subredes más pequeñas                      |
| **Bits prestados (n)**     | Bits tomados del campo HOST para crear subredes                   |
| **Dirección de red**       | Primera IP del bloque: todos bits host = 0                        |
| **Dirección de broadcast** | Última IP del bloque: todos bits host = 1                         |
| **Hosts válidos**          | Direcciones entre la de red y la de broadcast                     |
| **Máscara AND**            | Operación bit a bit IP AND Máscara = Dir. Subred                  |
| **NAT**                    | Traducción de IPs privadas ↔ IPs públicas para acceder a Internet |
| **DHCP**                   | Asignación automática de parámetros de red a hosts                |
|                            |                                                                   |


## 📐 Proceso Mental de Subnetting (Checklist)

```
□ 1. Identificar la clase por el primer octeto
□ 2. Anotar la máscara natural de esa clase (/8, /16 o /24)
□ 3. Calcular subredes necesarias (pisos×oficinas, edificios×aulas, etc.)
□ 4. Resolver 2ⁿ ≥ subredes_necesarias → obtener n
□ 5. Nueva máscara = máscara_natural + n bits
□ 6. Convertir nueva máscara a decimal (octeto afectado)
□ 7. Calcular: Subredes = 2ⁿ
□ 8. Calcular: h = bits_host_original - n
□ 9. Calcular: Hosts/subred = 2ʰ - 2
□ 10. Calcular: Incremento = 2ʰ
□ 11. Listar subredes incrementando según el octeto afectado
□ 12. Encontrar la subred pedida: Base + k × Incremento  (k empieza en 0)
□ 13. Calcular broadcast: Dir_subred + Incremento - 1
□ 14. Rango válido: [Dir_subred + 1] a [Broadcast - 1]
```
# 📚 MARCO TEÓRICO COMPLETO

## 1. ¿Qué es una dirección IP?

Una **dirección IP (Internet Protocol)** es un identificador numérico de 32 bits (IPv4) asignado a cada interfaz de red de un dispositivo. Se representa en **notación decimal punteada** (dot-decimal notation), dividida en 4 grupos de 8 bits llamados **octetos**:

```
Binario:  11000000 . 10101000 . 00001010 . 00000001
Decimal:     192   .   168   .    10   .     1
```

Los 32 bits se dividen en dos partes:

| Parte | Descripción |
|-------|-------------|
| **Parte de RED** | Identifica la red a la que pertenece el host |
| **Parte de HOST** | Identifica el dispositivo dentro de esa red |

---

## 2. Clases de Direcciones IPv4

Las direcciones IPv4 originalmente se organizaron en **clases** según el valor del primer octeto:

| Clase | Primer Octeto | Primer Bit(s) | Máscara Natural | Rango de IPs | Hosts por Red |
|-------|--------------|----------------|-----------------|--------------|---------------|
| **A** | 1 – 126      | `0xxxxxxx`     | /8 → 255.0.0.0 | 1.0.0.0 — 126.255.255.255 | 16.777.214 |
| **B** | 128 – 191    | `10xxxxxx`     | /16 → 255.255.0.0 | 128.0.0.0 — 191.255.255.255 | 65.534 |
| **C** | 192 – 223    | `110xxxxx`     | /24 → 255.255.255.0 | 192.0.0.0 — 223.255.255.255 | 254 |
| **D** | 224 – 239    | `1110xxxx`     | — (Multicast) | 224.0.0.0 — 239.255.255.255 | — |
| **E** | 240 – 255    | `1111xxxx`     | — (Investigación) | 240.0.0.0 — 255.255.255.255 | — |

> **¿Cómo identificar la clase de una IP?**  
> Observar el **primer octeto** en decimal y ubicarlo en la tabla anterior.  
> Ejemplo: `172.18.0.0` → primer octeto = 172 → **Clase B**  
> Ejemplo: `192.168.10.0` → primer octeto = 192 → **Clase C**  
> Ejemplo: `100.18.15.45` → primer octeto = 100 → **Clase A**

---

## 3. ==Máscara de Subred (Subnet Mask)

La **máscara de subred** es un número de 32 bits que indica qué parte de la dirección IP corresponde a la **red** y qué parte corresponde al **host**.

- **Bits en 1 (unos)** → identifican la parte de RED.
- **Bits en 0 (ceros)** → identifican la parte de HOST.

Los bits de red siempre van **primero** (a la izquierda) y son contiguos.

### Notación CIDR (Classless Inter-Domain Routing)

La **notación CIDR** (barra oblicua `/n`) indica la cantidad de bits de red. Es equivalente a la máscara decimal:

| CIDR | Máscara Decimal | Octeto afectado en binario                  |
| ---- | --------------- | ------------------------------------------- |
| /8   | 255.0.0.0       | `11111111`.`00000000`.`00000000`.`00000000` |
| /16  | 255.255.0.0     | `11111111`.`11111111`.`00000000`.`00000000` |
| /24  | 255.255.255.0   | `11111111`.`11111111`.`11111111`.`00000000` |
| /25  | 255.255.255.128 | `11111111`.`11111111`.`11111111`.`10000000` |
| /26  | 255.255.255.192 | `11111111`.`11111111`.`11111111`.`11000000` |
| /27  | 255.255.255.224 | `11111111`.`11111111`.`11111111`.`11100000` |
| /28  | 255.255.255.240 | `11111111`.`11111111`.`11111111`.`11110000` |
| /29  | 255.255.255.248 | `11111111`.`11111111`.`11111111`.`11111000` |
| /30  | 255.255.255.252 | `11111111`.`11111111`.`11111111`.`11111100` |
| /23  | 255.255.254.0   | `11111111`.`11111111`.`11111110`.`00000000` |
| /22  | 255.255.252.0   | `11111111`.`11111111`.`11111100`.`00000000` |
| /21  | 255.255.248.0   | `11111111`.`11111111`.`11111000`.`00000000` |

---

## 4. ==¿Por qué implementar Subredes?

**Subnetting** = proceso de dividir una red grande en redes más pequeñas denominadas **subredes**.

### Ventajas

| Ventaja                                | Descripción                                                       |
| -------------------------------------- | ----------------------------------------------------------------- |
| **Organización lógica**                | Agrupa dispositivos por ubicación física o función                |
| **Reducción del tráfico de broadcast** | Cada subred tiene su propio dominio de broadcast                  |
| **Mayor seguridad**                    | Se puede aplicar control de acceso entre subredes                 |
| **Optimización de IPs**                | Se asignan IPs de forma eficiente según la cantidad real de hosts |
| **Facilita la administración**         | Problemas aislados dentro de cada subred                          |

### Desventajas

| Desventaja                   | Descripción                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| **Desperdicio de IPs**       | Las direcciones de red y broadcast no son asignables a hosts |
| **Mayor complejidad**        | Requiere planificación y configuración adicional             |
| **Se necesita enrutamiento** | Los routers deben comunicar las subredes entre sí            |

---

## 5. ==Proceso de Cálculo de Subredes (Algoritmo General)

El cálculo de subredes sigue un proceso sistemático de **5 pasos**:

### PASO 1 — Identificar los datos del problema

- Dirección IP de la red.
- Cantidad de subredes necesarias (N_subredes).
- Cantidad de hosts por subred necesarios (N_hosts).

### PASO 2 — Determinar la cantidad de bits a pedir prestados

Los bits se "piden prestados" de la **parte de host** para crear subredes:

**Si se conoce la cantidad de subredes necesarias:**

$$2^n \geq N_{subredes}$$

Buscar el mínimo `n` (número entero) que satisfaga la inecuación.

**Si se conoce la cantidad de hosts por subred:**

$$2^h - 2 \geq N_{hosts}$$

Buscar el mínimo `h`, luego `n = bits\_originales\_host - h`.

### PASO 3 — Calcular la nueva máscara de subred

```
Nueva máscara CIDR = Máscara original CIDR + n bits prestados
```

Para convertir a decimal, en el octeto afectado se colocan los bits de subred a la izquierda:

```
Máscara Clase C + 4 bits = /28
Octeto 4 en binario: 1111|0000 = 240
Nueva máscara: 255.255.255.240
```

### PASO 4 — Calcular la cantidad de subredes y hosts

```
Subredes disponibles     = 2^n
Hosts válidos por subred = 2^h - 2  (se restan dirección de red y broadcast)
Total hosts direccionables = Subredes × Hosts_por_subred
```

> **¿Por qué se restan 2?**  
> - La **primera dirección** de cada subred es la **dirección de red** (identifica la subred, no asignable a hosts).  
> - La **última dirección** es la **dirección de broadcast** (envío a todos los hosts de la subred, no asignable a hosts).

### ==PASO 5 — Calcular las direcciones de cada subred

Se calcula el **incremento de bloque** (block size):

```
Incremento = 2^h = (total de IPs por subred, incluyendo red y broadcast)
```

Las subredes se listan incrementando la dirección según el octeto afectado:

```
Subred 0 → Dirección_base + 0 × Incremento
Subred 1 → Dirección_base + 1 × Incremento
Subred n → Dirección_base + n × Incremento
```

Para cada subred:
- **Dirección de red** = inicio del bloque.
- **Primer host válido** = dirección de red + 1.
- **Último host válido** = dirección de broadcast - 1.
- **Dirección de broadcast** = siguiente dirección de red - 1.

---

## 6. Tabla de Referencia Rápida — Clase C (/24)

| Bits Prestados (n) | CIDR | Máscara | Subredes (2ⁿ) | Hosts/subred (2⁽⁸⁻ⁿ⁾−2) | Incremento |
|:-----------------:|------|---------|:---:|:---:|:---:|
| 1 | /25 | 255.255.255.128 | 2  | 126 | 128 |
| 2 | /26 | 255.255.255.192 | 4  | 62  | 64  |
| 3 | /27 | 255.255.255.224 | 8  | 30  | 32  |
| **4** | **/28** | **255.255.255.240** | **16** | **14** | **16** |
| 5 | /29 | 255.255.255.248 | 32 | 6   | 8   |
| 6 | /30 | 255.255.255.252 | 64 | 2   | 4   |

---

## 7. Tabla de Referencia Rápida — Clase B (/16)

| Bits Prestados (n) | CIDR | Máscara 3er Octeto | Subredes (2ⁿ) | Hosts/subred (2⁽¹⁶⁻ⁿ⁾−2) | Incremento 3er Octeto |
|:-----------------:|------|---------------------|:---:|:---:|:---:|
| 1 | /17 | 128 | 2      | 32.766   | 128 |
| 2 | /18 | 192 | 4      | 16.382   | 64  |
| 3 | /19 | 224 | 8      | 8.190    | 32  |
| 4 | /20 | 240 | 16     | 4.094    | 16  |
| 5 | /21 | 248 | 32     | 2.046    | 8   |
| 6 | /22 | 252 | 64     | 1.022    | 4   |
| **7** | **/23** | **254** | **128** | **510** | **2** |
| 8 | /24 | 255 | 256    | 254      | 1   |
| 9 | /25 | 255 (más octeto 4) | 512 | 126 | — |

---





---

# 📋 ==CASO DE ESTUDIO 1 — SUBREDES CLASE C

## Enunciado

> La empresa **XX** está ubicada en un edificio de **5 pisos**. En cada uno de los pisos se ubican **2 oficinas** con **12 puestos de trabajo** cada una. Se desea implementar un esquema de direccionamiento privado de **Clase C**, utilizando subredes, considerando que **cada oficina pertenecerá a una subred** en particular.
>
> **Dirección IP a utilizar:** `192.168.10.0/24`

## Análisis Previo

Antes de calcular, identificamos los datos del problema:

| Dato                                          | Valor                            |
| --------------------------------------------- | -------------------------------- |
| Pisos                                         | 5                                |
| Oficinas por piso                             | 2                                |
| **Total de oficinas (= subredes necesarias)** | **5 × 2 = 10 subredes**          |
| Puestos por oficina (= hosts por subred)      | 12 hosts                         |
| Dirección base                                | 192.168.10.0                     |
| Clase                                         | C (192 está en el rango 192–223) |
| Máscara natural                               | /24 → 255.255.255.0              |
| Bits de host disponibles                      | 8 bits (el cuarto octeto)        |

---

## a) Dirección IP a Utilizar

$$\boxed{192.168.10.0 \;\;/24}$$

Es una dirección **privada** de **Clase C** (rango privado: 192.168.0.0 – 192.168.255.255, definido por RFC 1918).

La máscara original `/24` indica que los primeros 24 bits identifican la red y los últimos 8 bits están disponibles para hosts.

```
192.168.10.0 en binario:
11000000 . 10101000 . 00001010 . 00000000
|----------RED (24 bits)----------|HOST(8)|
```

---

## b) Cantidad de Bits a Pedir Prestados

**Necesitamos al menos 10 subredes.**

Aplicamos la fórmula: `2ⁿ ≥ N_subredes`

| n (bits prestados) | 2ⁿ | ¿Suficiente para 10? |
|:------------------:|:--:|:--------------------:|
| 1 | 2  | ❌ No |
| 2 | 4  | ❌ No |
| 3 | 8  | ❌ No |
| **4** | **16** | **✅ Sí** |

Con **n = 3** obtenemos 8 subredes, que es **menor que 10** (insuficiente).  
Con **n = 4** obtenemos 16 subredes, que es **mayor o igual que 10** ✅.

$$\boxed{n = 4 \text{ bits prestados}}$$

Esto deja: `8 - 4 = 4 bits` para hosts en cada subred.

```
Cuarto octeto antes del préstamo:
[  0   0   0   0  |  0   0   0   0  ]
 bits de HOST (8 bits)

Cuarto octeto después del préstamo de 4 bits:
[  1   1   1   1  |  0   0   0   0  ]
 ←SUBRED(4 bits)→  ←HOST(4 bits)→
```

---

## c) Máscara de Subred en Decimal

Partimos de la máscara original `/24` y le sumamos los 4 bits prestados:

```
/24 + 4 bits = /28
```

El cuarto octeto de la máscara queda: `11110000₂ = 240₁₀`

| Octeto | Binario    | Decimal |
|--------|------------|---------|
| 1°     | 11111111   | 255     |
| 2°     | 11111111   | 255     |
| 3°     | 11111111   | 255     |
| 4°     | **11110000** | **240** |

$$\boxed{\text{Máscara de subred: } 255.255.255.240 \;\;(/28)}$$

---

## d) Cantidad Máxima de Subredes Disponibles

$$\text{Subredes} = 2^n = 2^4 = \boxed{16 \text{ subredes}}$$

> **Nota histórica:** En redes antiguas se excluían la subred "todo ceros" y "todo unos" usando la fórmula `2^n - 2`. Hoy, según el RFC 1812 (y en redes modernas como Cisco IOS actual), **se utilizan las 16 subredes** incluyendo esas dos. En esta práctica trabajamos con las **16 subredes disponibles**.

---

## e) Cantidad de Hosts Válidos por Subred

Con **h = 4 bits de host** restantes:

$$H = 2^h - 2 = 2^4 - 2 = 16 - 2 = \boxed{14 \text{ hosts válidos por subred}}$$

- Se restan 2 porque:
  - La **primera dirección** es la dirección de red (no asignable).
  - La **última dirección** es la dirección de broadcast (no asignable).

> ✅ ¿Son suficientes 14 hosts para 12 puestos de trabajo por oficina? **Sí**: 14 ≥ 12.

---

## f) Cantidad Total de Hosts Direccionables

$$T = \text{Subredes} \times \text{Hosts\_por\_subred} = 16 \times 14 = \boxed{224 \text{ hosts totales}}$$

---

## g) Dirección de la Subred Número 9

**Incremento de bloque:**

$$I = 2^h = 2^4 = 16$$

Cada subred abarca 16 direcciones IP consecutivas. La lista completa de subredes:

>[!danger] OJO ACA NOSTROS EMPEZAMOS DESDE LA CERO, NO DESDE 1, ESO TE PUEDE DEFASAR 

| # Subred |  Dirección de Red  | Primer Host | Último Host | Broadcast | Rango Completo  |
| :------: | :----------------: | :---------: | :---------: | :-------: | :-------------: |
|    0     |  192.168.10.**0**  |     .1      |     .14     |    .15    |    .0 — .15     |
|    1     | 192.168.10.**16**  |     .17     |     .30     |    .31    |    .16 — .31    |
|    2     | 192.168.10.**32**  |     .33     |     .46     |    .47    |    .32 — .47    |
|    3     | 192.168.10.**48**  |     .49     |     .62     |    .63    |    .48 — .63    |
|    4     | 192.168.10.**64**  |     .65     |     .78     |    .79    |    .64 — .79    |
|    5     | 192.168.10.**80**  |     .81     |     .94     |    .95    |    .80 — .95    |
|    6     | 192.168.10.**96**  |     .97     |    .110     |   .111    |   .96 — .111    |
|    7     | 192.168.10.**112** |    .113     |    .126     |   .127    |   .112 — .127   |
|    8     | 192.168.10.**128** |    .129     |    .142     |   .143    |   .128 — .143   |
|  **9**   | **192.168.10.144** |  **.145**   |  **.158**   | **.159**  | **.144 — .159** |
|    10    | 192.168.10.**160** |    .161     |    .174     |   .175    |   .160 — .175   |
|    11    | 192.168.10.**176** |    .177     |    .190     |   .191    |   .176 — .191   |
|    12    | 192.168.10.**192** |    .193     |    .206     |   .207    |   .192 — .207   |
|    13    | 192.168.10.**208** |    .209     |    .222     |   .223    |   .208 — .223   |
|    14    | 192.168.10.**224** |    .225     |    .238     |   .239    |   .224 — .239   |
|    15    | 192.168.10.**240** |    .241     |    .254     |   .255    |   .240 — .255   |

**Cálculo de la subred 9 (contando desde 0):**

$$\text{octeto que cambia} = 9 \times 16 = 192.168.10.0 + 144$$

$$\boxed{\text{Dirección de la subred 9: } 192.168.10.144}$$

**Verificación en binario:**

```
192.168.10.144  →  11000000.10101000.00001010. 1001 | 0000
                                                ↑RED  ↑HOST
                   Los 4 bits de subred = 1001₂ = 9₁₀ (subred número 9 contando desde 0) ✓
```

---

## h) Dirección de Broadcast de la Subred Número 9

La dirección de broadcast es la **última dirección del bloque** de la subred 9.

$$\text{Broadcast subred 9} = 192.168.10.144 + 16 - 1 = 192.168.10.159$$

O equivalente: es la dirección donde **todos los bits de host están en 1**:

```
192.168.10.144 en binario:    11000000.10101000.00001010. 1001 | 0000
Broadcast (host bits = 1):    11000000.10101000.00001010. 1001 | 1111
Broadcast en decimal:         192.168.10.159
```

$$\boxed{\text{Broadcast subred 9: } 192.168.10.159}$$

---

## i) Rango de Direcciones IP Válidas de la Subred Número 9

```
Dirección de red:      192.168.10.144  ← NO asignable (identifica la subred)
Primer host válido:    192.168.10.145  ← PRIMER HOST ASIGNABLE
   .
   .  (12 hosts del puesto de trabajo se ubican aquí)
   .
Último host válido:    192.168.10.158  ← ÚLTIMO HOST ASIGNABLE
Dirección broadcast:   192.168.10.159  ← NO asignable (envío a todos)
```

$$\boxed{\text{Rango válido subred 9: } 192.168.10.145 \;\text{ A}\; 192.168.10.158 \;\;(14 \text{ hosts})}$$

---

## j) Método de Acceso a Internet

La dirección `192.168.10.0/24` es una **dirección privada** (RFC 1918). Las direcciones privadas **no son enrutables en Internet** directamente.

**Solución: NAT (Network Address Translation)**

Para que los equipos de la empresa accedan a Internet se necesita un **router** que implemente **NAT** (Network Address Translation). El router:

1. Recibe los paquetes de los hosts con IPs privadas (192.168.10.x).
2. **Traduce** la IP privada a la IP pública asignada por el ISP.
3. Reenvía el paquete a Internet.
4. Cuando llega la respuesta, realiza la traducción inversa.

```
                     NAT
 [Hosts Privados]  ───────→  [Router con IP pública]  ───→  INTERNET
 192.168.10.x/28      traduce IP privada → IP pública
```

**Variante más común: PAT (Port Address Translation)** o **NAT Overload**, donde múltiples IPs privadas comparten una única IP pública usando diferentes puertos de origen.

---

## k) Diseño de Red con Switches y Routers

**Topología propuesta:**

```
                         INTERNET
                             │
                         [ ISP ]
                             │ (IP Pública)
                    ┌────────┴────────┐
                    │  ROUTER CENTRAL │  ← 1 Router con NAT/PAT
                    └────────┬────────┘     Interfaz interna: 192.168.10.x/28
                             │
              ┌──────────────┼──────────────┐
              │              │              │
         [SWITCH P1]    [SWITCH P2]   [SWITCH P3]  ... hasta [SWITCH P5]
         (1 por piso)   (1 por piso)
              │
         ┌────┴────┐
    [SWITCH OF.A] [SWITCH OF.B]   ← 2 switches por piso (uno por oficina)
         │               │
    [12 PCs]         [12 PCs]    ← Subred diferente por oficina
```

**Cantidad de dispositivos:**

| Dispositivo             | Cantidad | Justificación                                                                  |
| ----------------------- | :------: | ------------------------------------------------------------------------------ |
| **Routers**             |  **1**   | Un router central con NAT hacia Internet y enrutamiento interno entre subredes |
| **Switches de piso**    |  **5**   | Uno por piso (distribución)                                                    |
| **Switches de oficina** |  **10**  | Dos por piso (uno por oficina)                                                 |
| **Total Switches**      |  **15**  | —                                                                              |

> Cada switch de oficina pertenece a una subred diferente (10 oficinas = 10 subredes de las 16 disponibles).

---

# 📋 CASO DE ESTUDIO 2 — SUBREDES CLASE B

## Enunciado

> La empresa **YY** está ubicada en un campus de **4 edificios**. En cada uno de los edificios se ubican **20 aulas** con **50 puestos de trabajo** cada una. Se desea implementar un esquema de direccionamiento privado de **Clase B**, utilizando subredes, considerando que **cada aula pertenecerá a una subred** en particular.
>
> **Dirección IP a utilizar:** `172.18.0.0/16`

## Análisis Previo

| Dato                                       | Valor                              |
| ------------------------------------------ | ---------------------------------- |
| Edificios                                  | 4                                  |
| Aulas por edificio                         | 20                                 |
| **Total de aulas (= subredes necesarias)** | **4 × 20 = 80 subredes**           |
| Puestos por aula (= hosts por subred)      | 50 hosts                           |
| Dirección base                             | 172.18.0.0                         |
| Clase                                      | B (172 está en el rango 128–191)   |
| Máscara natural                            | /16 → 255.255.0.0                  |
| Bits de host disponibles                   | 16 bits (tercero y cuarto octetos) |

---

## a) Dirección IP a Utilizar

$$\boxed{172.18.0.0 \;\;/16}$$

Es una dirección **privada** de **Clase B** (rango privado: 172.16.0.0 – 172.31.255.255, definido por RFC 1918).

```
172.18.0.0 en binario:
10101100 . 00010010 . 00000000 . 00000000
|──────RED (16 bits)──────|──HOST (16 bits)──|
```

---

## b) Cantidad de Bits a Pedir Prestados

**Necesitamos al menos 80 subredes.**

Aplicamos la fórmula: `2ⁿ ≥ N_subredes`

| n (bits prestados) | 2ⁿ | ¿Suficiente para 80? |
|:------------------:|:--:|:--------------------:|
| 4 | 16  | ❌ No |
| 5 | 32  | ❌ No |
| 6 | 64  | ❌ No |
| **7** | **128** | **✅ Sí** |

$$\boxed{n = 7 \text{ bits prestados}}$$

Bits de host restantes: `16 - 7 = 9 bits`

Los 16 bits de host de la Clase B se reparten así:

```
Antes del préstamo:
[  3° octeto (8 bits)  ] [  4° octeto (8 bits)  ]
[  HOST bits 8–15      ] [  HOST bits 0–7        ]

Después del préstamo de 7 bits (del 3° octeto):
[ 1  1  1  1  1  1  1  | 0 ] [  0  0  0  0  0  0  0  0 ]
  ←SUBRED (7 bits)→     ↑     ←────── HOST (8 bits) ──────→
                     HOST(1 bit)
                   3° octeto             4° octeto
```

El tercer octeto queda: `11111110₂ = 254₁₀`  
El cuarto octeto: `00000000₂ = 0₁₀`

---

## c) Máscara de Subred en Decimal

```
/16 (original) + 7 bits prestados = /23
```

| Octeto | Binario    | Decimal |
|--------|------------|---------|
| 1°     | 11111111   | 255     |
| 2°     | 11111111   | 255     |
| 3°     | **11111110** | **254** |
| 4°     | 00000000   | 0       |

$$\boxed{\text{Máscara de subred: } 255.255.254.0 \;\;(/23)}$$

---

## d) Cantidad Máxima de Subredes Disponibles

$$\text{Subredes} = 2^n = 2^7 = \boxed{128 \text{ subredes}}$$

(Se necesitaban 80, y se dispone de 128: ✅ suficientes con margen para crecimiento futuro.)


>[!question ] PODRIAMOS ARMAR LAS 128 SUBREDES?
>SI, no perdemos subredes, lo que perdemos son ips en las subredes

---

## e) Cantidad de Hosts Válidos por Subred

Con **h = 9 bits de host** (1 bit en el 3° octeto + 8 bits en el 4° octeto):

$$H = 2^h - 2 = 2^9 - 2 = 512 - 2 = \boxed{510 \text{ hosts válidos por subred}}$$

> ✅ ¿Son suficientes 510 hosts para 50 puestos de trabajo por aula? **Sí**: 510 ≥ 50. Hay amplio margen.

---

## f) Cantidad Total de Hosts Direccionables

$$T = \text{Subredes} \times H = 128 \times 510 = \boxed{65.280 \text{ hosts totales}}$$

---

## g) Dirección de la Subred Número 47

**Incremento de bloque:**

$$I = 2^h = 2^9 = 512 \text{ direcciones por subred}$$

Como cada subred tiene 512 IPs y el 4° octeto solo puede contener 256 direcciones (0–255), **cada subred ocupa 2 valores consecutivos del tercer octeto**:

```
Incremento en el 3° octeto = 512 / 256 = 2
```

Fórmula para la subred número k (contando desde k=0):

$$\text{3° octeto} = k \times 2$$

| # Subred | Dirección de Red |     Broadcast      |
| :------: | :--------------: | :----------------: |
|    0     |  172.18.**0**.0  |  172.18.**1**.255  |
|    1     |  172.18.**2**.0  |  172.18.**3**.255  |
|    2     |  172.18.**4**.0  |  172.18.**5**.255  |
|    …     |        …         |         …          |
|    46    | 172.18.**92**.0  | 172.18.**93**.255  |
|  **47**  | **172.18.94.0**  | **172.18.95.255**  |
|    48    | 172.18.**96**.0  | 172.18.**97**.255  |
|    …     |        …         |         …          |
|   127    | 172.18.**254**.0 | 172.18.**255**.255 |

**Cálculo de la subred 47 (contando desde 0):**

$$\text{3° octeto} = 47 \times 2 = 94$$

$$\boxed{\text{Dirección de la subred 47: } 172.18.94.0}$$

**Verificación en binario:**

```
172.18.94.0:
10101100.00010010. 0101111 | 0 .00000000
                   ↑ 7 bits SUBRED = 0101111₂ = 94/2 = 47₁₀ (índice base 0) ✓
                             ↑ 1 bit HOST del 3° octeto
```
---
Otra forma es resolverlo como en clases que hacemos esto
```
1ero) planteamos en binario

172.18.0000000 | 0 . 000000000
       Red     |host

2) con los de de red armamos el 47

   64 32 16 8 4 2 1
47:0  1  0  1 1 1 1

3) ahora ponendolo en la direccion original

172.18.01011110.00000000

4)y lo pasamos a decimal al octeto que cambio

128 64 32 16 8 4 2 1
0    1  0  1 1 1 1 0

pasandolo a decimi 64+16+8+4+2=94

5)Nos quedaria: 172.18.94.0



```


---

## h) Dirección de Broadcast de la Subred Número 47

La subred 47 abarca desde `172.18.94.0` hasta `172.18.95.255`.

La dirección de broadcast tiene **todos los bits de host en 1**:

```
172.18.94.0 en binario del 3° y 4° octeto:
  [3° octeto]  [4° octeto]
   0101111 | 0   00000000    ← Inicio subred 47
                               94.0 
   0101111 | 1   11111111    ← Broadcast (bits host = todos 1)
                               95.255
```

$$\boxed{\text{Broadcast subred 47: } 172.18.95.255}$$

---

## i) Rango de Direcciones IP Válidas de la Subred Número 47

```
Dirección de red:      172.18.94.0    ← NO asignable
Primer host válido:    172.18.94.1    ← PRIMER HOST ASIGNABLE
   .
   .  (hasta 510 hosts pueden ubicarse aquí)
   .
Último host válido:    172.18.95.254  ← ÚLTIMO HOST ASIGNABLE
Dirección broadcast:   172.18.95.255  ← NO asignable
```

$$\boxed{\text{Rango válido subred 47: } 172.18.94.1 \;\text{—}\; 172.18.95.254 \;\;(510 \text{ hosts})}$$

---

## j) Configuración de un Puesto de Trabajo en la Subred 47

Para que un equipo tenga **conectividad dentro y fuera de la empresa**, se deben configurar los siguientes parámetros:

| Parámetro                  | Valor                                       | Explicación                                                           |
| -------------------------- | ------------------------------------------- | --------------------------------------------------------------------- |
| **Dirección IP**           | 172.18.94.10                                | Cualquier dirección del rango válido (.94.1 — .95.254)                |
| **Máscara de subred**      | 255.255.254.0                               | Máscara calculada en el punto c)                                      |
| **Gateway predeterminado** | 172.18.94.1                                 | IP de la interfaz del router en esta subred (primer host, convención) |
| **DNS preferido**          | 172.18.x.x (servidor DNS interno) o 8.8.8.8 | Servidor de nombres de dominio                                        |
| **DNS alternativo**        | 8.8.4.4                                     | DNS alternativo de Google                                             |

**Ejemplo de configuración en Windows (CMD):**
```cmd
netsh interface ip set address "Ethernet" static 172.18.94.10 255.255.254.0 172.18.94.1
netsh interface ip set dns "Ethernet" static 8.8.8.8
```

**Ejemplo de configuración en Linux:**
```bash
ip addr add 172.18.94.10/23 dev eth0
ip route add default via 172.18.94.1
```

> **¿Por qué necesita gateway?** El gateway permite que el host envíe paquetes a redes distintas a la suya (como otras subredes de la empresa o Internet). Sin gateway, la comunicación queda restringida a los hosts dentro de la misma subred.

---

## k) Propuesta de Configuración con Solo 2 Administradores de Red

**Problema:** La empresa YY tiene 80 aulas con 50 PCs cada una = **4.000 puestos de trabajo**. Configurar manualmente cada PC (dirección IP, máscara, gateway, DNS) sería **inviable** para 2 administradores.

**Solución propuesta: DHCP (Dynamic Host Configuration Protocol)**

### ¿Qué es DHCP?

DHCP es un protocolo de red que permite a un servidor **asignar automáticamente** los parámetros de red a cada host que se conecta:
- Dirección IP.
- Máscara de subred.
- Gateway predeterminado.
- Servidores DNS.

### Implementación propuesta

```
┌──────────────────────────────────────────────────────────────────┐
│                   SERVIDOR DHCP CENTRAL                          │
│              (puede ser un router o servidor dedicado)           │
│                                                                  │
│  Pool subred 0:  172.18.0.2  —  172.18.1.254  (máscara /23)    │
│  Pool subred 1:  172.18.2.2  —  172.18.3.254  (máscara /23)    │
│  ...                                                             │
│  Pool subred 47: 172.18.94.2 — 172.18.95.254  (máscara /23)    │
│  ...                                                             │
│  Pool subred 79: 172.18.158.2 — 172.18.159.254 (máscara /23)   │
└──────────────────────────────────────────────────────────────────┘
```

### Ventajas de DHCP para 2 administradores

| Ventaja | Descripción |
|---------|-------------|
| **Configuración centralizada** | Se configura el servidor una sola vez |
| **Sin intervención manual** | Los PCs obtienen su IP automáticamente al encenderse |
| **Evita conflictos de IP** | El servidor lleva registro de las IPs asignadas (leases) |
| **Fácil gestión de cambios** | Cambiar gateway o DNS se hace en el servidor, no en cada PC |
| **Escalable** | Agregar nuevos equipos no requiere trabajo adicional de los admins |

**Fundamento:** Con DHCP, los 2 administradores solo necesitan configurar el servidor DHCP con los pools de direcciones de cada subred. Cada PC, al iniciar, solicita automáticamente su configuración de red al servidor mediante el proceso **DORA** (Discover → Offer → Request → Acknowledge).

---

# 🧠 PARA PENSAR

## Ejercicio 1 — Máscara 255.255.255.224

### Enunciado
> Dada la máscara de subred `255.255.255.224` determine:
> a) ¿A qué clase pertenece?
> b) ¿Cómo puede asegurarlo?
> c) ¿Cuántos bits se pidieron prestados?



> [!caution] a) ¿A qué clase pertenece? → **NO SE PUEDE DETERMINAR**
> La clase de una dirección IP se obtiene del **primer octeto de la IP**, no de la máscara.
> Con solo la máscara `255.255.255.224` es **imposible** saber la clase,

**Ejemplos de /27 en distintas clases:**

| IP de ejemplo       | Primer octeto | Clase | Máscara         |
| ------------------- | :-----------: | :---: | --------------- |
| **10**.0.0.32/27    |      10       | **A** | 255.255.255.224 |
| **172.16**.0.32/27  |      172      | **B** | 255.255.255.224 |
| **192.168.1**.32/27 |      192      | **C** | 255.255.255.224 |

Las tres tienen la **misma máscara** pero pertenecen a clases diferentes.

> [!caution] b) ¿Cómo puede asegurarlo? → **NO ES POSIBLE sin la dirección IP**
> Para asegurar la clase se necesita ver el **primer octeto de la IP**:
> - 1–126 → Clase A
> - 128–191 → Clase B
> - 192–223 → Clase C
>
> Solo con la máscara, esta información no existe.

> **c) Bits prestados: DEPENDE de la clase base**

Sin la dirección IP no se puede saber cuál es la máscara natural, por lo tanto tampoco cuántos bits se prestaron:



---

## Ejercicio 2 — IP 135.58.9.23/24

### Enunciado
> Dada la siguiente dirección IP: `135.58.9.23 / 24` determine:
> a) ¿A qué clase pertenece?
> b) ¿Se implementan subredes (SI/NO) y por qué?

### Resolución Paso a Paso

**Paso 1: Identificar la clase por el primer octeto**

Primer octeto = **135**

| Rango     | Clase                 |
| --------- | --------------------- |
| 1 – 126   | A                     |
| 128 – 191 | **B ← 135 está aquí** |
| 192 – 223 | C                     |

> **==a) Clase: B** (primer octeto 135 ∈ [128–191])

**Paso 2: Determinar la máscara natural de Clase B**

La máscara natural de Clase B es `/16` → `255.255.0.0`

**Paso 3: Comparar la máscara aplicada con la natural**

| Máscara | CIDR | Decimal |
|---------|------|---------|
| Natural (Clase B) | /16 | 255.255.0.0 |
| Aplicada en la IP | /24 | 255.255.255.0 |

La máscara aplicada `/24` es **diferente** de la máscara natural `/16`.

> ==**b) SÍ, se implementan subredes.**

**Justificación:**

La máscara natural de Clase B es /16. Al utilizarse una máscara /24, se están **pidiendo prestados** `24 - 16 = 8 bits` del campo host para crear subredes. Esto implica una división en subredes de la red de Clase B original.

```
Binario de la máscara /24:
11111111 . 11111111 . 11111111 . 00000000
|──── RED natural B (16 bits) ──── | SUBRED (8 bits) | HOST (8 bits) |
```

**Análisis adicional:**

| Parámetro | Valor |
|-----------|-------|
| Dirección IP | 135.58.9.23 |
| Máscara | 255.255.255.0 (/24) |
| Clase base | B (máscara natural /16) |
| Bits prestados | 24 - 16 = **8 bits** |
| Subredes posibles | 2⁸ = 256 |
| Hosts por subred | 2⁸ - 2 = 254 |
| Dirección de red | 135.58.9.0 |
| Broadcast | 135.58.9.255 |
| Rango de hosts | 135.58.9.1 — 135.58.9.254 |

---

## Ejercicio 3 — IP 100.18.15.45/21

### Enunciado
> Dada la siguiente dirección IP: `100.18.15.45 / 21` determine:
> a) ¿A qué clase pertenece?
> b) ¿Qué máscara de subred se debe configurar en el puesto de trabajo?
> c) ¿A qué subred pertenece esa dirección IP?
> d) ¿Cuál sería la dirección de broadcast si se desea que un paquete llegue a todas las PC de esa subred?

### Resolución Paso a Paso

**Paso 1: Identificar la clase**

Primer octeto = **100**

| Rango | Clase |
|-------|-------|
| **1 – 126** | **A ← 100 está aquí** |
| 128 – 191 | B |
| 192 – 223 | C |

> ==**a) Clase: A** (primer octeto 100 ∈ [1–126])

Máscara natural de Clase A: `/8` → `255.0.0.0`

---

**Paso 2: Calcular la máscara de subred**

La máscara aplicada es `/21`.

Convirtiendo /21 a decimal:

```
/21 = 21 bits en 1, seguidos de 11 bits en 0

porque se pidieron prestados 13 bits, y para las mascara todos los bits de red= 1 y todos los bits de host=0



  8 bits  +   8 bits  +  5 bits + 3 bits  +  8 bits
11111111  . 11111111  . 11111000 . 00000000
  255     .   255     .   248   .     0
```

Tercer octeto: `11111000₂ = 255₁₀ - 7₁₀ = 248₁₀`  
(128+64+32+16+8 = 248)

> ==**b) Máscara de subred a configurar: `255.255.248.0` (/21)**

---

**Paso 3: Determinar a qué subred pertenece**

Para encontrar la dirección de subred, se aplica la operación **AND bit a bit** entre la IP y la máscara:

```
IP:      100 .  18  .  15  .  45
Máscara: 255 . 255  . 248  .   0

Cálculo octeto por octeto:

  1° octeto: 100 AND 255 = 100  (255 en binario = todo 1s → no cambia)
  2° octeto:  18 AND 255 =  18  (255 en binario = todo 1s → no cambia)
  3° octeto:  15 AND 248 = ?    ← este es el importante
  4° octeto:  45 AND   0 =   0  (0 en binario = todo 0s → siempre da 0)
```

**Cálculo detallado del 3° octeto:**

```
 1) 15  en binario: 
    128 64 32 16 8 4 2 1  ->8+4+2+1=15
      0  0  0  0 1 1 1 1  
      
      
 2)248  en binario: 
	 128 64 32 16 8 4 2 1 -> 128+64+32+16+8=254
       1  1  1  1 1 0 0 0
                  
─────────  AND (bit a bit) -> 1 and 1= 1 , el resto siempre cero
0  0  0  0 1 1 1 1
1  1  1  1 1 0 0 0 

=
0  0  0  0 1 0 0 0

                  128 64 32 16 8 4 2 1
  Resultado:      0    0  0  0 1 0 0 0  =  8
```

o ASI:

| Bit         |           15            |               248               |    15 AND 248    |
| ----------- | :---------------------: | :-----------------------------: | :--------------: |
| 2⁷=128      |            0            |                1                |        0         |
| 2⁶=64       |            0            |                1                |        0         |
| 2⁵=32       |            0            |                1                |        0         |
| 2⁴=16       |            0            |                1                |        0         |
| 2³=8        |            1            |                1                |      **1**       |
| 2²=4        |            1            |                0                |        0         |
| 2¹=2        |            1            |                0                |        0         |
| 2⁰=1        |            1            |                0                |        0         |
| **EN hexa** | *8+4+2+1*<br><br>**15** | *128+64+32+16+8*<br><br>**248** | *8*<br><br>**8** |

**Dirección de subred:**
```
100 . 18 . 8 . 0
```

> *==*c) La dirección 100.18.15.45/21 pertenece a la subred: `100.18.8.0`**

**Verificación por incremento:**

- Máscara /21 → bits de host = 32 - 21 = **11 bits** -> son los que quedan de host
- Bloque = 2¹¹ = **2048 IPs**
- Incremento en 3° octeto = 2^3= 8 (los 3 bits de host que están en el tercer octeto) o podrias haber hecho 2048/256=8 

Subredes consecutivas en el tercer octeto (con incremento 8):

| # Subred | 3° octeto |                     Rango de IPs                      |
| :------: | :-------: | :---------------------------------------------------: |
|   ...    |    ...    |                          ...                          |
|    k     |     0     |           100.18.**0**.0 — 100.18.**7**.255           |
|   k+1    |     8     | 100.18.**8**.0 — 100.18.**15**.255 ← aquí está .15.45 |
|   k+2    |    16     |          100.18.**16**.0 — 100.18.**23**.255          |
|   ...    |    ...    |                          ...                          |

¿Está 100.18.15.45 en la subred 100.18.8.0?  
→ 100.18.8.0 a 100.18.15.255: el tercer octeto 15 ∈ [8, 15] ✅  
→ .15.45: sí está en ese rango ✅

---

==**¿A qué número de subred corresponde? ==

Cuando los bits prestados abarcan más de un octeto (como en Clase A con /21), el número de subred se obtiene leyendo **todos los bits prestados juntos como un número binario**.

**Estructura de la dirección /21 sobre Clase A:**

```
[  1° octeto  ] [  2° octeto  ] [      3° octeto       ] [  4° octeto  ]
[   RED (8)   ] [ SUBRED (8)  ] [ SUBRED(5) | HOST (3)  ] [  HOST (8)  ]
[    100      ] [     18      ] [    8      |     0      ] [    0      ]
```

Los **13 bits prestados** se extraen de la dirección de subred (100.18.**8**.0):

| Octeto | Valor decimal |    Binario     | Tipo de bits                      |
| ------ | :-----------: | :------------: | --------------------------------- |
| 2°     |      18       |   `00010010`   | 8 bits de SUBRED                  |
| 3°     |       8       | `00001`\|`000` | 5 bits de SUBRED + 3 bits de host |

Los 13 bits de subred (concatenados):

```
  [ 2° octeto ] [ primeros 5 bits del 3° octeto ]
    0 0 0 1 0 0 1 0   0 0 0 0 1 
    ↑               ↑ ↑       ↑
    bit 12          bit 5  bit 0

Valor = 2¹² + ... = ?
```

Calculando bit a bit:

| Posición |  12  |  11  |  10  |      9      |  8  |  7  |     6      |  5  |  4  |  3  |  2  |  1  |     0     |
| :------: | :--: | :--: | :--: | :---------: | :-: | :-: | :--------: | :-: | :-: | :-: | :-: | :-: | :-------: |
|   Bit    |  0   |  0   |  0   |    **1**    |  0  |  0  |   **1**    |  0  |  0  |  0  |  0  |  0  |   **1**   |
|  Valor   | 4096 | 2048 | 1024 | 2^9=**512** | 256 | 128 | 2^6=**64** | 32  |  8  | 18  |  8  |  2  | 2^0=**1** |

$$\text{N° Subred} = 512 + 64 + 1 = \boxed{577}$$

**Fórmula rápida** (cuando el incremento está en el 3° octeto):

$$\text{N° Subred} = (\text{Octeto 2 en decimal} \times 2^{\text{bits\_sub\_oct3 }}) + \left(\frac{\text{Octeto 3 de la subred}}{\text{Incremento}}\right)$$

$$= (18 \times 2^5) + \left(\frac{8}{8}\right) = (18 \times 32) + 1 = 576 + 1 = \boxed{577}$$

> **Regla general para calcular el número de subred:**  
> Tomá la dirección de subred, extraé solo los bits prestados (ignorando la parte de red y de host), y convertí ese número binario a decimal.

---

**Paso 4: Calcular la dirección de broadcast**

La dirección de broadcast tiene **todos los bits de host en 1**:

```
Bits de host: 11 bits (3 bits en el 3° octeto + 8 bits en el 4° octeto)

Dirección de subred:  100.18. 00001000 . 00000000
                                        ↑ bits host = 0  (inicio subred)

Broadcast:            100.18. 00001111 . 11111111
                               (3 bits  (8 bits de
                              host = 111) host = todos 1)

3° octeto broadcast: 00001111₂ = 15
4° octeto broadcast: 11111111₂ = 255
```

$$\boxed{\text{Broadcast: } 100.18.15.255}$$

**Verificación matemática:**

```
Dir. subred:   100.18.8.0
Tamaño bloque: 2048 IPs
Broadcast = Dir_subred + 2048 - 1 = 100.18.8.0 + 2047

100.18.8.0 + 2047:
  El 4° octeto puede tomar 256 valores (0-255), así que:
  2047 = 7×256 + 255
  3° octeto: 8 + 7 = 15
  4° octeto: 255
  Broadcast: 100.18.15.255 ✓
```

**Resumen del ejercicio:**

```
IP analizada:          100.18.15.45 /21
Clase:                 A (primer octeto 100, rango 1-126)
Máscara natural Cl.A:  /8  → 255.0.0.0
Máscara aplicada:      /21 → 255.255.248.0
Bits prestados:        21 - 8 = 13 bits para subredes
Dirección de subred:   100.18.8.0
Primer host válido:    100.18.8.1
Último host válido:    100.18.15.254
Broadcast:             100.18.15.255
Hosts por subred:      2¹¹ - 2 = 2046 hosts
```

---


# ----

# 📋 Resumen de los Ejercicios Resueltos

### Caso 1 — Clase C (192.168.10.0/24)

| Item | Valor |
|------|-------|
| Dirección base | 192.168.10.0 |
| Subredes necesarias | 10 (5 pisos × 2 oficinas) |
| Bits prestados | 4 |
| Nueva máscara | 255.255.255.240 (/28) |
| Subredes disponibles | 16 |
| Hosts por subred | 14 |
| Total hosts | 224 |
| Subred 9 | 192.168.10.144 |
| Broadcast subred 9 | 192.168.10.159 |
| Rango válido subred 9 | 192.168.10.145 — 192.168.10.158 |
| Acceso a Internet | NAT (IP privada) |

### Caso 2 — Clase B (172.18.0.0/16)

| Item | Valor |
|------|-------|
| Dirección base | 172.18.0.0 |
| Subredes necesarias | 80 (4 edificios × 20 aulas) |
| Bits prestados | 7 |
| Nueva máscara | 255.255.254.0 (/23) |
| Subredes disponibles | 128 |
| Hosts por subred | 510 |
| Total hosts | 65.280 |
| Subred 47 | 172.18.94.0 |
| Broadcast subred 47 | 172.18.95.255 |
| Rango válido subred 47 | 172.18.94.1 — 172.18.95.254 |
| Config. puesto de trabajo | IP + Máscara + Gateway + DNS |
| Propuesta para 2 admins | DHCP |

### Para Pensar

| Ejercicio | Dato | Resultado |
|-----------|------|-----------|
| 1a | Máscara 255.255.255.224 | ❌ NO DETERMINABLE — se necesita la IP (primer octeto) |
| 1b | ¿Cómo asegurarlo? | ❌ IMPOSIBLE sin la IP — la clase no se obtiene de la máscara |
| 1c | Bits prestados | Depende de la clase: Cl.A→19 bits / Cl.B→11 bits / Cl.C→3 bits |
| 2a | 135.58.9.23/24 | Clase B (135 ∈ [128-191]) |
| 2b | ¿Hay subredes? | SÍ: máscara aplicada /24 ≠ máscara natural /16 (8 bits prestados) |
| 3a | 100.18.15.45/21 | Clase A (100 ∈ [1-126]) |
| 3b | Máscara | 255.255.248.0 (/21) |
| 3c | Subred a la que pertenece | 100.18.8.0 (AND: 15 AND 248 = 8) |
| 3d | Broadcast de esa subred | 100.18.15.255 |

---

## 🌐 Rangos de Direcciones IP Privadas (RFC 1918)

| Clase | Rango Privado                 | Máscara Natural |
| ----- | ----------------------------- | --------------- |
| A     | 10.0.0.0 — 10.255.255.255     | /8              |
| B     | 172.16.0.0 — 172.31.255.255   | /16             |
| C     | 192.168.0.0 — 192.168.255.255 | /24             |

> Las IPs privadas **no son enrutables en Internet**. Se necesita NAT para conectarse al exterior.

---
