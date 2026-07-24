
==TODAS ESTAS HACER DE VUELTA , ESTAN RESUELTAS CON NOTEBBOK LM PERO HACERLAS SOLO EN EL CUADERNO==

# Comandos
![[{394C3E9C-0544-4962-B924-B75CBB81ECC1}.png]]
## ¿Cuál es el comando que me permite observar la dirección MAC de la placa de red de un host? (ESCRIBILO TODO JUNTO, SIN ESPACIOS)
linux: ifconfig
windows:  ipconfig/all 





## Con la configuración mostrada ¿Podría conectarse a otras redes?
![[{A907E552-CEC1-49B0-B02F-F614AD8D2A13}.png]]
### rta
- **Alcance Local:** La interfaz `eth0` tiene asignada la dirección IP `192.168.10.10` con una máscara de subred `255.255.255.0` (un prefijo /24). Esto le permite comunicarse perfectamente con cualquier otro dispositivo que se encuentre en esa misma subred local (es decir, direcciones desde la `192.168.10.1` hasta la `192.168.10.254`).
    
- **El dato faltante (Puerta de enlace):** Para que un equipo pueda enviar tráfico a _otras redes_ (por ejemplo, a Internet o a una VLAN distinta), necesita tener configurada una **puerta de enlace predeterminada** (Default Gateway), que es básicamente la dirección IP del router que conecta su red con el exterior.
    
- **Limitación del comando:** La imagen muestra la salida del comando `ifconfig`. Este comando detalla el estado de las interfaces de red, su IP y su máscara, pero **no muestra la tabla de enrutamiento ni el gateway**.


## ![[{ECD18025-F94D-4DCC-B437-E232FE81B207}.png]]
1) Indique el comando ejecutado.
	1) ifconfig
2) ¿Se encuentra habilitada la placa de red eth17?
	1) NO
3) Con la con�guración mostrada ¿Podría conectarse a otras redes?
	1) La imagen confirma que el equipo puede comunicarse dentro de su propia red local, ya que la interfaz `eth0` tiene asignada la dirección IP `192.168.10.10` con la máscara de subred `255.255.255.0`. 
	2) Sin embargo, para enviar paquetes a _otras_ redes (como por ejemplo, salir a Internet), el dispositivo requiere una **puerta de enlace predeterminada (Gateway)**. 
	3) El comando `ifconfig` no revela información de enrutamiento, por lo que no podemos ver si esa puerta de enlace está configurada. Sería necesario ejecutar comandos como `route -n`
# Calculos
## Indique cuántas direcciones IP válidas se disponen en la red 148.250.64.0/23 
- [ ] 1024 2
- [ ] 56
- [ ] 510
- [ ] 255
- [ ] 512
- [ ] 1022
- [ ] 254
#### rta
32-23=  9 bits en host disponbiles

2^9-2=510

## El ISP le asigna a una empresa la IP 190.45.96.0/22 ello implica que se dispone de (==cant de host validos==): 
- [ ] 1024 direcciones de host válidas
- [ ] 510 direcciones de hosts válidas
- [ ] 2048 direcciones de hosts válidas
- [ ] 4094 direcciones de hosts válidas
- [ ] 2046 direcciones de hosts válidas
- [ ] 1022 direcciones de hosts válidas
### rta
1022 direcciones de hosts válidas

Resolucion:
1. ==**Bits disponibles para hosts:**== Las direcciones IPv4 están formadas por un total de 32 bits. El prefijo `/22` indica que los primeros 22 bits están fijos para identificar la red. Por lo tanto, el efecto directo es que quedan **10 bits restantes** destinados exclusivamente a la porción de host ==(32−22=10)==
2. **Cálculo total:** Con 10 bits disponibles, la cantidad de combinaciones matemáticas posibles es de 2^{10}, lo que da un total de 1024 direcciones
3. ==**Descuento de direcciones reservadas:** Para obtener el número de direcciones "válidas" (es decir, las que se pueden asignar a dispositivos o interfaces reales), la regla exige utilizar la fórmula 2^n−2. Esto causa que al total de 1024 se le deban restar ineludiblemente 2 direcciones, dando como resultado final **1022**
4. **Causalidad de la resta:** ¿Por qué se restan exactamente dos direcciones? Se debe a que la primera combinación (cuando todos los bits de la porción de host valen `0`) es una dirección reservada que identifica a la propia **dirección de red**. Paralelamente, la última combinación posible (cuando todos los bits de host se encienden en `1`) queda reservada para la **dirección de broadcast** o difusión. Ninguna de estas dos puede asignarse a un equipo.

## Su ISP le ha asignado un espacio completo de clase C públicas. Usted deberá armar 3 subredes que puedan soportar 60 hosts cada una. ¿Cuales, de las siguientes, son ==direcciones de red== que satisfacen tal requisito? Seleccione una o más de una:
- [ ] 195.16.2.65 
- [ ] 192.16.2.127 
- [ ] 193.16.2.64 
- [ ] 193.16.2.128 
- [ ] 193.16.2.0 
- [ ] 255.255.255.192

### rta
Las respuestas correctas que satisfacen el requisito como **direcciones de red** son:

- **193.16.2.0**
- **193.16.2.64**
- **193.16.2.128**

Para comprender el **porqué** de este resultado, analicemos el proceso de cálculo de subredes basándonos en la relación de causa y efecto de los requisitos planteados:

**1. La causa (El requisito de hosts):** El ISP asignó un espacio de **Clase C**, el cual por defecto dispone de 8 bits para la porción de host. El administrador necesita armar subredes que soporten al menos 60 hosts cada una. Para resolver esto, debemos calcular cuántos bits de host necesitamos conservar utilizando la fórmula $2^n - 2$. Si conservamos 6 bits para host, obtenemos $2^6 - 2 = 62$ direcciones válidas. Esto cumple perfectamente con el requisito de soportar 60 puestos de trabajo.

**2. El efecto en la subred (Los bits prestados):** Como la Clase C tenía 8 bits de host originarios y decidimos conservar 6, el efecto directo es que debemos pedir prestados los **2 bits** restantes para crear las subredes ($8 - 6 = 2$). Al pedir 2 bits prestados, la cantidad de subredes posibles es $2^2 = 4$ subredes. Esto también satisface el requisito de armar al menos 3 subredes.

**3. ==El cálculo de las direcciones de red:** Al pedir 2 bits prestados en el cuarto octeto, el valor de salto o incremento entre subredes es de 64 (ya que el bit menos significativo prestado tiene el valor posicional de 64). Por lo tanto, las 4 direcciones de subred resultantes son:

- Subred 0: **X.Y.Z.0** (ej. 193.16.2.0)
- Subred 1: **X.Y.Z.64** (ej. 193.16.2.64)
- Subred 2: **X.Y.Z.128** (ej. 193.16.2.128)
- Subred 3: **X.Y.Z.192** (ej. 193.16.2.192)

**Por qué las demás opciones son incorrectas:**

- **195.16.2.65:** No es una dirección de red, sino que es la **primera IP válida** asignable a un host dentro de la subred 1 (cuyo rango va de .65 a .126).
- **192.16.2.127:** Tampoco es una dirección de red; al tener los 6 bits de host encendidos en binario, representa la **dirección de broadcast** de la subred 1.
- **255.255.255.192:** Esto no es una dirección de red, sino que es la **máscara de subred** que resulta de pedir los 2 bits prestados. Se utiliza como parámetro de configuración conjunto, pero no identifica a la red en sí.

## Dada la dirección IP: 17.34.65.24 /12 Indicar:
1) Clase de red a la que pertenece el host.
2) Tipo de dirección
3) Dirección de Red/subred a la que pertenece el host
4) Cantidad de Host Utiles por red/subred.
5) Direccion de broadcast de la red/subred a la que pertenece el host
### RTA NOTBEOOK
**1) Clase de red a la que pertenece el host:** **Clase A**. La clase de una dirección IPv4 se determina observando su primer byte; como el valor **17** se encuentra en el rango de 1 a 127, pertenece directamente a esta clase.

o ![[{A13DDB1E-0F16-45DA-BFF5-3ADBADF9346E}.png]]

**2) Tipo de dirección:** Es una **dirección IPv4 Pública** y una **dirección de host válida**. No es una dirección privada porque no se encuentra dentro del rango reservado por la RFC 1918 para la Clase A (el cual está estrictamente delimitado de 10.0.0.0 a 10.255.255.255). Además, al no tener la porción de host con todos sus bits en 0 ni en 1, es una IP que puede ser asignada perfectamente a la interfaz de un dispositivo.


**3) Dirección de Red/subred a la que pertenece el host:** **17.32.0.0**. Para hallar este valor, el dispositivo realiza la operación de **AND Booleano** entre la IP y su máscara. El prefijo `/12` nos indica que la máscara es **255.240.0.0**. Al analizar el segundo octeto (donde ocurre el corte):

![[{02D85896-2A3D-40EB-879C-4CB5C8C986FD} 1.png]]

- El número 34 en binario es `00100010`.
- El número 240 de la máscara es `11110000`.
- Al aplicar el AND lógico, el resultado es `00100000`, que en decimal equivale a **32**. Los bytes de host restantes se apagan a cero.

**4) Cantidad de Host Útiles por red/subred:** **1.048.574 hosts útiles**. Al tener una máscara `/12` (12 bits para red/subred), nos quedan **20 bits** libres para la porción de host (32 - 12 = 20). Aplicando la fórmula arquitectónica de $2^n - 2$:

- $2^{20} = 1.048.576$ combinaciones totales.
- Se le restan 2 (la dirección de la subred y la dirección de broadcast), resultando en 1.048.574 direcciones IP asignables a dispositivos.

**5) Dirección de broadcast de la red/subred:** **17.47.255.255**. La dirección de broadcast se obtiene encendiendo (poniendo en `1` binario) todos los bits correspondientes a la porción de host. En este caso, como los 4 bits prestados de la máscara en el segundo octeto generan saltos de a 16 ($256 - 240 = 16$), sabemos que la siguiente subred comenzará en la 17.48.0.0. Por ende, el límite superior o broadcast de nuestra subred actual es exactamente la dirección anterior a ese salto: **17.47.255.255**.


## dada
![[{C0370CA7-8188-45B3-A592-0B59D0568C94}.png]]



## Cuál de las siguientes es la dirección de broadcast de la subred 190.10.24.0/23:
- [ ] 190.10.31.255
- [ ] 190.10.27.255
- [ ] 190.10.25.254
- [ ] 190.10.25.255
- [ ] 190.10.24.255

### rta
1ero identificar la clase
```190 a binario

128 64 32
1    0   

empieza con 1 0 -> clase B
```
2do la clase B tiene R.R.H.H -> por defecto /16

en este caso es 23  -> 23-16=7 se pidieron prestados

3ero pasamos el 3er octeto a binario para ver como quedaria si ponemos todo en 1 la parte de host
```190.10.24.0
24 -> 128 64 32 16 8 4 2   1
        0  0  0  1 1 0  0  0
```
entonces poniendo todo en 1 la parte de red quedari 25 de la siguiente forma:
```
      128 64 32 16 8 4  2 |  1
        0  0  0  1 1 0  0 | 1
         Red              | host  
         
         25

```

nos quedaria la direccion de brodcast asi: 190.10.25.255 / 23
## Indique cuáles de las siguientes son direcciones de broadcast (seleccione dos):
- [ ] 100.50.51.254/22
- [ ]  100.50.43.255/22
- [ ]  100.50.53.255/22
- [ ] 200.80.48.95/28
- [ ] 200.80.48.93/28
### rta
1ero con las 100
determinaos la clase
``` 
100 a binario
128 64 32
  0       
 -> empieza con 0 es clase A
```

2do
prefijo de la clase A por defecto /8  -> 22-8=14 bits se pidieron prestados

R.SR.000000 | 00

3ero trabajomos con el 3er octeo
```
53 a binario
128 64 32 16 8  4 | 2 1
        1  1 0  1 | 0 1
        
vemos que uno del host lo tiene apagaod por lo tanto esta no va a ser de brodcast

```

```
43 a binario

128 64 32 16 8  4 | 2 1
  0  0  1  0  1 0 | 1 1

la parte de host prendido
```
ademas la direccion es  100.50.43.255 /22  -> ES DE BRODCAST

el mismo procedimiento para el otro y da 200.80.48.95 /28 -> ES DE BRODCAST
## La empresa Fármacos SA lo ha contratado para definir el esquema de direccionamiento de su infraestructura. Para ello cuenta con la siguiente topologia configurada para conectar su red privada a internet. Elija la configuración correcta:
![[{985195DA-2063-4695-8F63-72AA0EE265A0}.png]]
- [ ] Red/Subred 200.21.10.0 255.255.255.0
- [ ] Red/Subred 192.10.25.0 255.255.255.128
- [ ] Red/subred 192.168.10.0 255.255.255.182
- [ ] Red/Subred 172.16.17.0 255.255.255.224
### rta
La opción seleccionada en la imagen (`Red/Subred 172.16.17.0 255.255.255.224`) es la correcta. Para fundamentarlo con el rigor necesario en el diseño de arquitecturas de red, podemos desglosar el problema evaluando los dominios de broadcast, la validación de rangos privados (RFC 1918) y el análisis de las máscaras de subred de cada opción.

**1. Identificación de dominios de broadcast (Subredes necesarias)**

Como se indica con los números escritos a mano en la topología, cada interfaz de un router delimita un dominio de broadcast distinto. En total, hay 5 subredes que deben ser direccionadas para que exista conectividad total:

- **Red 1:** LAN izquierda (Switch + 2 PCs).
    
- **Red 2:** Enlace WAN entre el router izquierdo y el central.
    
- **Red 3:** Enlace WAN entre el router derecho y el central.
    
- **Red 4:** Conexión directa del router central a la laptop.
    
- **Red 5:** LAN derecha (Switch + 3 PCs).
    

Se requieren como mínimo **5 subredes**. La red con más hosts es la LAN derecha (Red 5), que necesita al menos 4 direcciones IP útiles (3 PCs + 1 interfaz _gateway_ del router).

**2. Análisis de las opciones descartadas**

- **`200.21.10.0 255.255.255.0`**: La dirección 200.x.x.x pertenece al espacio de direccionamiento **público**, lo cual contradice el requerimiento del enunciado de diseñar el esquema para la "red privada" de la empresa.
    
- **`192.10.25.0 255.255.255.128`**: Nuevamente, 192.10.x.x es una IP pública (el rango privado es 192.168.x.x). Además, la máscara `.128` (equivalente a /25) solo divide el bloque en 2 subredes, lo cual es insuficiente para las 5 necesarias en esta infraestructura.
    
- **`192.168.10.0 255.255.255.182`**: Aunque el rango es privado, la máscara de subred `.182` es matemáticamente **inválida**. En sistema binario, 182 se representa como `10110110`. Las reglas de redes dictan que una máscara válida debe estar formada por una secuencia contigua de unos ("1") seguida exclusivamente de ceros ("0").
    

**3. Por qué la última opción es la correcta**

- **`172.16.17.0 255.255.255.224`**:
    
    - Utiliza el bloque `172.16.x.x`, que está reservado para **redes privadas** según el estándar RFC 1918.
        
    - La máscara `255.255.255.224` equivale a un prefijo de red **/27** (los primeros 3 bits del último octeto están destinados a red: `11100000`).
        
    - Al tomar 3 bits para subnetting a partir de un bloque tradicional /24, se obtienen $2^3 =$ **8 subredes** de igual tamaño. Esto cubre perfectamente las 5 subredes de la topología.
        
    - Los 5 bits restantes quedan para la porción de host, permitiendo $2^5 - 2 =$ **30 hosts útiles** por subred, lo que satisface con holgura los requisitos de la LAN más grande.

## ==Un administrador de red ha subneteado la red 172.16.0.0 usando la mascara de subred 255.255.255.224. Accidentalmente ha duplicado la dirección IP 172.16.2.121 en 2 equipos de la misma subred. De acuerdo a los datos proporcionados, ¿cuál es la IP que podría asignarse en reemplazo de la duplicada? Seleccione una:==
- [ ] 172.16.2.128 
- [ ] 172.16.1.64 
- [ ] 172.16.2.96 
- [ ] 172.16.2.100 
- [ ] 172.16.2.64 
- [ ] 172.16.1.80 
- [ ] 172.16.2.127
### rta
La respuesta correcta es:

- [x] **172.16.2.100**

Para comprender el **porqué** de este resultado, debemos aplicar las reglas matemáticas de cálculo de subredes para identificar a qué segmento pertenece la IP original y qué rango de direcciones útiles tenemos disponibles para reemplazarla:

- **Paso 1: Identificar el salto de red.** La máscara de subred asignada es `255.255.255.224`. Al analizar el valor del cuarto octeto (`224`), podemos deducir que la red se ha dividido en bloques con un salto de **32 direcciones** cada uno (resultado de la constante 256 - 224 = 32). Esto significa que las subredes irán saltando de 32 en 32 en el cuarto octeto: .0, .32, .64, .96, .128, etc.
- **Paso 2: Encontrar la Subred actual.** Sabiendo que la IP duplicada es `172.16.2.121`, buscamos en qué bloque de 32 encaja el valor de su cuarto octeto (`121`). Como 121 es mayor que 96 pero menor que 128, deducimos ineludiblemente que esta máquina pertenece a la subred **`172.16.2.96`**.
- **Paso 3: Calcular el rango de IPs válidas.**
    - **Dirección de red:** `172.16.2.96` (Reservada, no se asigna).
    - **Primera IP válida:** Se suma 1 a la red, siendo `172.16.2.97`.
    - **Broadcast de la subred:** Es una dirección antes de que comience la subred siguiente (.128), es decir, `172.16.2.127` (Reservada para difusión, no se asigna).
    - **Última IP válida:** Se resta 1 al broadcast, siendo `172.16.2.126`.

En conclusión, para que la nueva IP pertenezca a la misma subred, **debe estar comprendida obligatoriamente en el rango del .97 al .126**. La única opción que cumple matemáticamente este requisito es **`172.16.2.100`**.

**Por qué las demás opciones son incorrectas:**

- **172.16.2.96:** Es la **dirección de subred** que representa a todo el grupo, por lo que es una dirección reservada que jamás puede configurarse en un host.
- **172.16.2.127:** Es la dirección de **Broadcast (difusión)** de esta subred específica, utilizada por el switch para mandar mensajes a todos los equipos, por lo que es inválida para un host individual.
- **172.16.2.128 y 172.16.2.64:** Son identificadores lógicos correspondientes a las direcciones de red de la subred siguiente y de la subred anterior, respectivamente.
- **172.16.1.64 y 172.16.1.80:** Poseen un error estructural evidente en su tercer octeto (`.1` en lugar de `.2`). Estas direcciones pertenecen lógicamente a otra área de la organización. Como dictan los apuntes, si le asignas una IP de una subred distinta, la máquina quedará aislada y no tendrá conectividad local con los demás equipos de su propia área.


## ej de a que subred pertenece una ip
### Dada la dirección IP: 17.34.65.24/12 Indicar:
Clase : A
ip publica? sim
#### Dirección de Red/subred a la que pertenece el host:
1ero es clase A por lo tanto -> R.H.H.H
```pasamos la direccion entera a binario
17->

34->

65->

24->

```
## ej de cuantas direcciones ip se pierden
### Una empresa decide implementar un esquema de direccionamiento IP utilizando subredes. El administrador decide utilizar la IP 160.4.0.0/23. Ello implica:

1ero determinar la clase
```
160 a binario -> 128 64
                   1  0
                   
                   empieza con 1 0 es clase B

```
2do cuantos bits se pidieron prestados si  es R.R.H.H -> el prefijo por defeto es /16

por lo tanto 23-16= 7 bits se pidieron prestoado


por lo tanto 2^7= 128

3er paso, y si por cada subred perdemos dos direcciones -> una la de la subred y otra la de brdocuast

tenemos que 128 x 2 = 256

Se pierden 256 direcciones IP del total del espacio de direccionamiento
# RESUMEN
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

## 4️⃣ DISEÑO DE TOPOLOGÍA CON SUBREDES

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


## 6️⃣ ==COMANDOS DE RED (Referencia Rápida)

## Linux

| Acción                      | que hace                                                                                                                                                                                           | Comando viejo (`ifconfig`)                         |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Ver interfaces UP           |                                                                                                                                                                                                    | `ifconfig`                                         |
| Ver TODAS las interfaces    |                                                                                                                                                                                                    | `ifconfig -a`                                      |
| Habilitar interfaz          |                                                                                                                                                                                                    | `ifconfig eth0 up`                                 |
| Asignar IP                  |                                                                                                                                                                                                    | `ifconfig eth0 192.168.1.10 netmask 255.255.255.0` |
| Ver tabla de rutas          | **¿Para qué sirve?** Muestra la **tabla de enrutamiento**: las reglas que tiene el equipo para saber cómo llegar a distintas redes.                                                                | `route`                                            |
| Ver tabla ARP               | Tabla ARP (IP ↔ MAC)                                                                                                                                                                               | `arp -n`                                           |
| Prueba conectividad         |                                                                                                                                                                                                    | `ping -c 4 IP`                                     |
| Config permanente           | **¿Para qué sirve?** Es el **archivo de configuración de red** de Debian/Ubuntu/Mint. Las interfaces configuradas aquí **persisten tras el reinicio**.                                             | `nano /etc/network/interfaces`                     |
| Levantar con config archivo | **¿Para qué sirve?** Levanta (`ifup`) o baja (`ifdown`) una interfaz usando la configuración definida en `/etc/network/interfaces`. Solo funcionan si la interfaz está configurada en ese archivo. | `ifup eth0`                                        |
| Config gateway              |                                                                                                                                                                                                    | `route add default gw IP`                          |


### Archivo de configuración permanente: `/etc/network/interfaces`

```
iface eth0 inet static
   address 192.168.1.10
   netmask 255.255.255.0
```

## Mensajes de Ping

| Mensaje | Significado |
|---|---|
| `64 bytes from ...` | ✅ El host responde, hay conectividad |
| `Destination Host Unreachable` | ❌ La red existe pero el host no responde |
| `Network is unreachable` | ❌ No hay ruta hacia esa red |

---


## 8️⃣ ERRORES FRECUENTES A EVITAR

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

## 9️⃣ TIPS RÁPIDOS PARA EL PARCIAL

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


# dsp acomodar
![[{DB13990F-7867-474B-B882-D71CD86BD7B8}.png]]![[{21001BF2-96A5-41C1-B645-DDEDF8D86FBB}.png]]