# Métricas del TP5 — Cómo se calculan y para qué sirven

## Estructura general: acumuladores

Antes de ver cada métrica, hay que entender el mecanismo base.

El motor **no calcula las estadísticas al final**. Las va acumulando **durante toda la simulación**, evento a evento. Para eso usa variables llamadas **acumuladores** que se definen al inicio y crecen con el tiempo:

```js
let busyQA  = 0   // tiempo total que QA estuvo ocupado
let busyAA  = 0   // tiempo total que AA estuvo ocupado
let busyPA  = 0   // tiempo total que PA estuvo ocupado
let busySec = 0   // tiempo total que la secadora estuvo ocupada
let busyLug = 0   // suma de (tiempo × lugares ocupados)

let sumaPerm   = 0  // suma de permanencias de cada auto que salió
let salidos    = 0  // cantidad de autos que salieron

let sumaEspera = 0  // suma de esperas totales por auto
let countEspera= 0  // cantidad de autos que sumaron espera

let sumaSecado = 0  // suma de tiempos de secado por carrocería
let countSecado= 0  // cantidad de carrocerías secadas

let maxColaQA       = 0
let maxColaAspirado = 0
let maxColaLavado   = 0
let maxColaPA       = 0
```

---

## El método de áreas — cómo funciona `acumular(dt)`

```js
function acumular(dt) {
    if (dt <= 0) return;
    if (QA.ocupado)       busyQA  += dt;
    if (AA.ocupado)       busyAA  += dt;
    if (PA.ocupado)       busyPA  += dt;
    if (secadora.ocupada) busySec += dt;

    let oc = 0;
    if (lugares[0].estado !== 'Libre') oc++;
    if (lugares[1].estado !== 'Libre') oc++;
    busyLug += dt * oc;   // 0, 1 o 2 lugares ocupados
}
```

Se llama **antes de procesar cada evento**, con `dt = ev.time - lastClock` (el intervalo desde el último evento).

La idea es: si QA estuvo ocupado durante ese intervalo `dt`, entonces `busyQA += dt`. Al final, `busyQA` acumula el **área bajo la curva de ocupación** de QA a lo largo de toda la simulación.

### Visualización del método de áreas

```
Ocupación de QA
  1 |████░░░░███████░░░████|
  0 |_____________________|
    0        T/2          T

  busyQA = suma de los tramos en 1
  ocupacion = busyQA / T * 100
```

> [!IMPORTANT]
> `acumular(dt)` usa el **estado PREVIO** al evento que se va a procesar. Primero acumula lo que pasó en el intervalo `[lastClock, ev.time]` con el estado anterior, y recién después procesa el evento que lo cambia.

---

## Las 8 métricas pedidas por el enunciado

---

### 1. Ocupación de QA (%)

**Variable en código:** `ocupacionQA`
```js
ocupacionQA = (busyQA / T) * 100
```

| Campo | Descripción |
|---|---|
| `busyQA` | Tiempo total en minutos que QA estuvo atendiendo a alguien |
| `T` | Tiempo total de simulación (reloj final) |

**¿Qué significa?** Qué porcentaje del tiempo de la jornada QA estuvo ocupado procesando un auto. Si da 80%, QA solo estuvo libre el 20% de la jornada.

**¿Dónde se acumula?**
```js
// En acumular(dt), antes de cada evento:
if (QA.ocupado) busyQA += dt;
```

**¿Para qué sirve?** Detectar si QA es un cuello de botella. Si la ocupación es muy alta (>90%), hay autos acumulándose en la cola de QA.

---

### 2. Ocupación del Aspirado — AA (%)

**Variable en código:** `ocupacionAA`
```js
ocupacionAA = (busyAA / T) * 100
```

Igual al mecanismo de QA pero para el aspirado de alfombras.

**¿Para qué sirve?** Evaluar si el servidor de alfombras es el limitante. Como el aspirado (U(3,5) min) suele terminar antes que el lavado + secado (U(6,12) + RK min), AA generalmente tiene menor ocupación que los lugares de lavado.

---

### 3. Ocupación de los Lugares de Lavado (%)

**Variable en código:** `ocupacionLugares`
```js
ocupacionLugares = (busyLug / (2 * T)) * 100
```

Este es el más especial. `busyLug` **no** es simplemente "¿algún lugar ocupado?", sino que pondera cuántos lugares hay ocupados:

```js
let oc = 0;
if (lugares[0].estado !== 'Libre') oc++;
if (lugares[1].estado !== 'Libre') oc++;
busyLug += dt * oc;   // 0, dt o 2*dt
```

Por eso se divide por `2 * T` al final: la capacidad total del servidor es 2.

**Ejemplo:**
```
Intervalo de 5 min con los 2 lugares ocupados:
  busyLug += 5 * 2 = 10

Intervalo de 3 min con 1 lugar ocupado:
  busyLug += 3 * 1 = 3

Ocupación = 13 / (2 * 8) * 100 = 81.25%
```

> [!NOTE]
> Un lugar está "ocupado" tanto cuando está **Lavando** como cuando está **SecandoCon** o **SecandoSin**. El lugar no se libera hasta que la carrocería esté 100% seca.

**¿Para qué sirve?** Medir qué tan bien se aprovechan los 2 lugares disponibles. Si da 50%, en promedio solo 1 de los 2 lugares estuvo en uso.

---

### 4. Ocupación de la Secadora (%)

**Variable en código:** `ocupacionSecadora`
```js
ocupacionSecadora = (busySec / T) * 100
```

```js
// En acumular(dt):
if (secadora.ocupada) busySec += dt;
```

**¿Para qué sirve?** Evaluar si la única secadora es un cuello de botella. Si está al 100% constantemente, es probable que muchas carrocerías tengan que secarse solas (modo sin secadora), lo que alarga los tiempos de secado.

---

### 5. Tiempo Medio de Secado de la Carrocería (min)

**Variable en código:** `secadoMedio`
```js
secadoMedio = sumaSecado / countSecado
```

**¿Dónde se acumula?** En `evFinSecado()`, cuando la carrocería termina de secarse:
```js
sumaSecado += auto.dryEnd - auto.washEnd;
countSecado++;
```

- `auto.dryEnd` → instante en que terminó el secado (clock en ese momento)
- `auto.washEnd` → instante en que terminó el lavado (cuando empezó a secarse)

Incluye **todo** el tiempo de secado, ya sea:
- Solo con secadora desde el inicio
- Solo sin secadora (si no consiguió la secadora nunca)
- Una parte sin secadora y luego con secadora (si se la reasignaron)

**¿Para qué sirve?** Evaluar el impacto de tener una sola secadora. Si este tiempo es mucho mayor que el tiempo de secado "ideal" (solo con secadora), significa que muchas carrocerías esperan turno para la secadora.

---

### 6. Tiempo Medio de Permanencia en el Sistema (min)

**Variable en código:** `permanenciaMedia`
```js
permanenciaMedia = sumaPerm / salidos
```

**¿Dónde se acumula?** En `evFinPA()`, cuando el auto sale del sistema:
```js
sumaPerm += auto.salida - auto.llegada;
salidos++;
```

- `auto.salida` = `clock` en el momento de salir (fin del PA)
- `auto.llegada` = `clock` en el momento que llegó

Abarca **todo**: tiempo en cola de QA + QA + cola lavado/aspirado + lavado + secado + PA + esperas intermedias.

**¿Para qué sirve?** Medir la experiencia del cliente. Es el tiempo total que el auto pasa en el lavadero, desde que llega hasta que sale limpio.

---

### 7. Tiempo Medio de Espera en Colas (min)

**Variable en código:** `esperaMediaColas`
```js
esperaMediaColas = sumaEspera / countEspera
```

**¿Dónde se acumula?** En `evFinPA()`, sumando las 4 esperas parciales del auto:
```js
sumaEspera += auto.esperaQA + auto.esperaLavado + auto.esperaAspirado + auto.esperaPA;
countEspera++;
```

Cada espera parcial se calcula cuando el auto **empieza a ser atendido**:

```js
iniciarQA(auto):
    auto.esperaQA = clock - auto.llegada
    // espera desde que llegó hasta que QA lo toma

iniciarLavado(auto, idx):
    auto.esperaLavado = clock - auto.qaEnd
    // espera desde que salió de QA hasta que entra al lugar de lavado

iniciarAspirado(auto):
    auto.esperaAspirado = clock - auto.qaEnd
    // espera desde que salió de QA hasta que entra al aspirado

iniciarPA(auto):
    auto.esperaPA = clock - Math.max(auto.dryEnd, auto.aspEnd)
    // espera desde que ambas partes estaban listas hasta que PA lo toma
```

> [!NOTE]
> La diferencia con la permanencia: la permanencia incluye también el tiempo **siendo atendido** (servicio). La espera son solo los tiempos **en cola**, sin ser atendido.

**¿Para qué sirve?** Medir cuánto tiempo pierden los autos esperando (no siendo servidos). Es el indicador más directo de congestión del sistema.

---

### 8. Máxima Cantidad de Autos en Cola de QA

**Variable en código:** `maxColaQA`

```js
// En actualizarMaximos(), después de cada evento:
if (colaQA.length > maxColaQA) maxColaQA = colaQA.length;
```

Es el **máximo histórico** de la longitud de la cola de QA a lo largo de toda la simulación.

**¿Para qué sirve?** Dimensionar el espacio físico necesario para que los autos esperen. Si `maxColaQA = 5`, en algún momento hubo 5 autos esperando para que les quiten las alfombras.

---

## Métricas extras de apoyo (no pedidas pero calculadas)

### Máximas colas de los otros servidores

```js
maxColaAspirado   // máximo de autos esperando el aspirado
maxColaLavado     // máximo de carrocerías esperando un lugar de lavado
maxColaPA         // máximo de autos esperando PA
```

Mismo mecanismo que `maxColaQA`. Sirven para identificar en qué punto del sistema se acumula más la cola.

### Contadores de autos

```js
autosIngresados = idAuto          // total de autos que llegaron al sistema
autosSalidos    = salidos         // total de autos que salieron (terminaron PA)
autosEnSistema  = enSistema.size  // autos que quedaron dentro al cortar la simulación
```

**¿Para qué sirven?**
- `autosIngresados - autosSalidos` = autos que quedaron en el sistema sin terminar
- Si `autosSalidos` es muy bajo en relación a `autosIngresados`, el sistema está sobrecargado

---

## Resumen de la cadena completa para cada métrica

```
OCUPACIONES (QA, AA, PA, Secadora)
  acumular(dt) [antes de c/evento]
       ↓
  busyXX += dt  (si el recurso está ocupado)
       ↓
  Al final: ocupacion = busyXX / T * 100

OCUPACIÓN LUGARES
  acumular(dt) [antes de c/evento]
       ↓
  busyLug += dt * (0, 1 o 2)  (lugares ocupados)
       ↓
  Al final: ocupacionLugares = busyLug / (2*T) * 100

SECADO MEDIO
  evFinSecado() [cuando termina el secado]
       ↓
  sumaSecado += dryEnd - washEnd
  countSecado++
       ↓
  Al final: secadoMedio = sumaSecado / countSecado

PERMANENCIA MEDIA
  evFinPA() [cuando el auto sale]
       ↓
  sumaPerm += salida - llegada
  salidos++
       ↓
  Al final: permanenciaMedia = sumaPerm / salidos

ESPERA MEDIA EN COLAS
  iniciarXX() [cuando el auto empieza a ser atendido]
       ↓
  auto.esperaXX = clock - referencia  (calcula la espera de esa etapa)
  ...al salir: sumaEspera += suma de las 4 esperas parciales
  countEspera++
       ↓
  Al final: esperaMediaColas = sumaEspera / countEspera

MÁXIMAS COLAS
  actualizarMaximos() [después de c/evento]
       ↓
  maxColaXX = max(maxColaXX, cola.length)
       ↓
  Al final: se retorna el máximo acumulado
```
