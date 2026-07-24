# Análisis del Código — TP5 Simulación del Lavadero (Grupo 25)

## Descripción General del Sistema

El TP simula un **lavadero de autos** usando **simulación por vector de estado / próximo evento (next-event)**. El reloj no avanza en pasos fijos, sino que **salta de evento en evento**.

Cada auto al entrar al sistema se "parte" en dos flujos paralelos:
- **Carrocería** → QA → Lavado → Secado (RK4) → PA
- **Alfombras** → QA → Aspirado → PA

Solo cuando **ambos** flujos terminan, el auto puede hacer PA (Poner Alfombras) y salir.

---

## Arquitectura de Archivos

```
src/
├── main.jsx               → Punto de entrada React
├── App.jsx                → Orquestador principal (UI + lógica de simulación)
├── utils/
│   └── format.js          → Utilidades de formateo numérico
├── sim/
│   ├── rng.js             → Generador de números aleatorios
│   ├── rungeKutta.js      → Método de Runge-Kutta 4 para el secado
│   └── engine.js          → Motor de simulación (toda la lógica)
└── components/
    ├── ParametersForm.jsx  → Formulario de parámetros
    ├── StatisticsPanel.jsx → Panel de estadísticas finales
    ├── StateVectorTable.jsx→ Tabla del vector de estado
    └── RungeKuttaTables.jsx→ Tablas de RK por auto
```

---

## Flujo de Llamadas (Call Flow)

```mermaid
flowchart TD
    A["Usuario presiona ▶ Simular"] --> B["App.jsx: onSimular()"]
    B --> C["normalizar(params)"]
    C --> D["simular(params) — engine.js"]

    D --> D1["crearRng(semilla) — rng.js"]
    D --> D2["Inicialización del estado\n(autos, colas, recursos)"]
    D2 --> D3["exponencial(rng, media)\nPrograma primera llegada"]
    D3 --> D4["construirFila(INIT)\nFila n=0 del vector"]

    D4 --> LOOP["🔁 Bucle principal\nwhile(true)"]

    LOOP --> E["proximoEvento()\nEncuentra el mínimo entre\ntodos los tiempos futuros"]
    E --> F{Evento}

    F -->|LLEGADA| G["evLlegada()"]
    F -->|FIN_QA| H["evFinQA()"]
    F -->|FIN_AA| I["evFinAA()"]
    F -->|FIN_LAVADO| J["evFinLavado(idx)"]
    F -->|FIN_SECADO| K["evFinSecado(idx)"]
    F -->|FIN_PA| L["evFinPA()"]

    G --> G1["elegirTipo() — rng.js"]
    G --> G2["exponencial() → próxima llegada"]
    G --> G3["iniciarQA() o colaQA.push"]

    H --> H1["iniciarAspirado() o colaAspirado.push"]
    H --> H2["iniciarLavado() o colaLavado.push"]
    H --> H3["Libera QA / atiende cola QA"]

    I --> I1["matsReady = true"]
    I --> I2["intentarPA()"]

    J --> J1["resolverSecado() — rungeKutta.js\nModo 'con' o 'sin' secadora"]
    J --> J2["guardarTabla()"]

    K --> K1["bodyReady = true"]
    K --> K2["Libera lugar de lavado"]
    K --> K3["Reasigna secadora (FIFO)\nreasignarSecadora()"]
    K --> K4["iniciarLavado() desde cola"]
    K --> K5["intentarPA()"]

    L --> L1["Suma estadísticas permanencia"]
    L --> L2["Retira auto del sistema"]
    L --> L3["Atiende cola PA"]

    LOOP --> M["acumular(dt)\nAcumula tiempos de ocupación"]
    LOOP --> N["actualizarMaximos()\nActualiza colas máximas"]
    LOOP --> O["construirFila()\nGuarda fila en ventana [j, j+i)"]

    O --> LOOP

    LOOP -->|"ev.time > tiempoX\no iter >= maxIteraciones"| P["Cierre"]
    P --> Q["Estadísticas finales\n(ocupaciones, permanencia, esperas)"]
    Q --> R["Retorna: filas, stats,\ntablasRK, ultimaFila, info"]
    R --> S["App.jsx muestra:\n- StatisticsPanel\n- StateVectorTable\n- RungeKuttaTables"]
```

---

## Desglose por Archivo y Función

---

### `rng.js` — Generador de Números Aleatorios

#### `truncar2(x)`
- **Trunca** (no redondea) un número `[0,1)` a **2 decimales**: `0.9797 → 0.97`.
- Se usa internamente para que el número mostrado en el vector de estado sea exactamente el que se usó para calcular el evento.

#### `crearRng(semilla)`
- **Crea y devuelve un generador** de números pseudoaleatorios.
- Si recibe semilla → usa el algoritmo **Mulberry32** (resultados reproducibles).
- Si no → usa `Math.random()` (distinto en cada corrida).
- Retorna una función `rng()` que cada vez que se llama entrega el próximo número truncado a 2 decimales.

#### `exponencial(rng, media)`
- Genera un tiempo con distribución **Exponencial Negativa**.
- Fórmula: `T = -media * ln(1 - rnd)`
- Retorna `{ rnd, valor }` (el número crudo Y el tiempo calculado).

#### `uniforme(rng, a, b)`
- Genera un tiempo con distribución **Uniforme U(a,b)**.
- Fórmula: `T = a + rnd * (b - a)`
- Retorna `{ rnd, valor }`.

#### `elegirTipo(rng, prob, kCoef)`
- Determina el **tipo de auto** (Pequeño / Mediano / Pick-up) con un único número aleatorio usando probabilidades acumuladas.
- Retorna `{ rnd, tipo, k }` donde `k` es el coeficiente de secado del auto.

---

### `rungeKutta.js` — Método de Runge-Kutta 4 para el Secado

Las ecuaciones diferenciales del secado son:

$$\frac{dH}{dt} = \begin{cases} -5t^2 + 2H - 200 & \text{con secadora} \\ -k \cdot H & \text{sin secadora} \end{cases}$$

> [!NOTE]
> La ecuación **con secadora** tiene el término `+2H` que la hace inestable con paso `h=1`. Por eso se usa un paso fino de `h=0.1 min` para estabilizarla.

#### `pasoRK4(f, t, H, h)`
- Ejecuta **un paso del método de Runge-Kutta de 4to orden**.
- Calcula las 4 pendientes:
  - `k1 = f(t, H)`
  - `k2 = f(t + h/2, H + h/2 * k1)`
  - `k3 = f(t + h/2, H + h/2 * k2)`
  - `k4 = f(t + h, H + h * k3)`
- Nuevo valor: `Hnext = H + (h/6)(k1 + 2k2 + 2k3 + k4)`
- Retorna `{ k1, k2, k3, k4, Hnext }`.

#### `resolverSecado({ Hinicial, tInicial, modo, k })`
- **Integra el secado completo** paso a paso (cada 0.1 min) hasta que `H ≤ UMBRAL_SECO (0.05%)`.
- Selecciona la ecuación correcta según `modo`: `'con'` → `fCon`, `'sin'` → `fSin(k)`.
- Retorna `{ pasos, minutos, Hfinal }`:
  - `pasos`: array con cada paso RK4 (para la tabla visual).
  - `minutos`: tiempo total hasta secar.

#### `humedadEnPaso(pasos, tLocal)`
- Lee la humedad de una tabla RK en un tiempo local dado (sin interpolar).
- Se usa para saber cuánta humedad le queda a una carrocería que se secaba **sola** en el momento en que **consigue la secadora**.

---

### `engine.js` — Motor de Simulación

Este es el núcleo del TP. Toda la lógica de simulación vive aquí.

#### `simular(params)` — Función principal exportada

Recibe todos los parámetros y retorna el resultado completo. Internamente define el estado del sistema y todas las funciones helper.

**Estado del sistema:**
| Variable | Descripción |
|---|---|
| `clock` | Reloj actual de la simulación |
| `autos` (Map) | Todos los autos actualmente en el sistema |
| `enSistema` (Set) | IDs de autos presentes |
| `QA`, `AA`, `PA` | Recursos de capacidad 1 |
| `secadora` | La única secadora |
| `lugares[0..1]` | Los 2 lugares de lavado |
| `colaQA`, `colaAspirado`, `colaLavado`, `colaPA` | Colas FIFO |
| `S.proxLlegada`, `S.finQA`, etc. | Tiempos futuros de eventos |

---

#### Helpers de inicio de operación

##### `iniciarQA(auto)`
- Marca QA como ocupado, registra la espera del auto y programa `S.finQA = clock + 2 min` (fijo).

##### `iniciarAspirado(auto)`
- Marca AA como ocupado, genera tiempo **U(aspMin, aspMax)** via `uniforme()`, programa `S.finAA`.
- Guarda el rnd usado en `rndLog.aspirado`.

##### `iniciarLavado(auto, idx)`
- Ocupa el lugar `idx`, genera tiempo **U(lavMin, lavMax)**, programa `lugares[idx].finLavado`.
- Guarda el rnd en `rndLog.lavado`.

##### `iniciarPA(auto)`
- Marca PA como ocupado, calcula la espera desde `max(dryEnd, aspEnd)`, programa `S.finPA = clock + 3 min` (fijo).

##### `intentarPA(auto)`
- **Coordina el punto de sincronización**: verifica si `bodyReady AND matsReady`.
- Si sí, marca `paIniciado = true` e inicia PA o encola el auto.
- Si no, no hace nada (el otro flujo se encargará cuando termine).

---

#### Helpers del secado

##### `guardarTabla(auto, modoInicial, pasos, minutos)`
- Almacena la tabla RK del secado en `tablasRK[]` (máximo 500 para no agotar memoria).
- Retorna referencia a la tabla guardada (para poder modificarla si cambia la secadora).

##### `reasignarSecadora(idx)`
- Se llama cuando la secadora queda libre y hay una carrocería secándose **sola**.
- Flujo:
  1. Calcula cuánto tiempo lleva secándose sola.
  2. Lee la humedad restante `Hr` de la tabla sin secadora en ese instante (`humedadEnPaso`).
  3. Trunca la tabla sin secadora al tiempo realmente transcurrido.
  4. Lanza `resolverSecado` en modo `'con'` desde `H0 = Hr`.
  5. Actualiza el `finSecado` del lugar y la tabla mostrada (concatena fases).

##### `humedadActual(l)`
- Calcula la humedad **interpolada** de una carrocería que se está secando ahora mismo.
- Ubica la fase vigente (puede haber cambiado de `sin` a `con`), calcula el tiempo local dentro de esa fase e interpola entre pasos.
- Permite que la columna "H" del vector de estado muestre valores intermedios (no salta de 100% a 0%).

---

#### Procesadores de eventos

##### `evLlegada()`
- Crea el auto con su tipo y `k` (`elegirTipo`).
- Programa la **próxima llegada** con tiempo exponencial.
- Envía el auto a QA o a la cola.

##### `evFinQA()`
- El auto termina de quitarse las alfombras.
- **Bifurcación**: alfombras → aspirado (o cola), carrocería → lavado (o cola).
- Libera QA y atiende la cola si hay autos esperando.

##### `evFinAA()`
- Termina el aspirado de alfombras.
- Marca `matsReady = true`.
- Llama a `intentarPA(auto)` → si la carrocería ya está seca, inicia PA.
- Libera AA y atiende la cola.

##### `evFinLavado(idx)`
- La carrocería termina de lavarse.
- Si la secadora está libre → modo `'con'`, toma la secadora.
- Si no → modo `'sin'`, se seca sola con `dH/dt = -kH`.
- Llama a `resolverSecado()` y guarda la tabla RK.

##### `evFinSecado(idx)`
- La carrocería terminó de secarse.
- Marca `bodyReady = true`.
- **Libera el lugar de lavado** (recién ahora, no antes).
- Si tenía la secadora → la libera y busca la carrocería que más tiempo lleva secándose sola (FIFO por `dryingStart`) → `reasignarSecadora`.
- Inicia un lavado pendiente en el lugar liberado.
- Llama a `intentarPA(auto)`.

##### `evFinPA()`
- El auto sale del sistema.
- Acumula estadísticas: permanencia total, tiempo de espera total.
- Libera PA y atiende la cola.

---

#### Funciones del bucle principal

##### `proximoEvento()`
- Busca el **mínimo tiempo** entre todos los eventos futuros.
- Desempata por prioridad: `FIN_PA < FIN_SECADO < FIN_LAVADO < FIN_AA < FIN_QA < LLEGADA`.
- Retorna `{ time, type, slot }`.

##### `acumular(dt)`
- Acumula el área bajo la curva de ocupación de cada recurso durante el intervalo `dt`.
- Permite calcular las **ocupaciones promedio** al final.

##### `actualizarMaximos()`
- Actualiza los máximos históricos de cada cola.

##### `construirFila(ev, conObjetos)`
- Toma un **snapshot** del estado completo del sistema en el instante actual.
- Incluye: reloj, evento, tiempos futuros, estados de recursos, longitudes de colas, acumuladores.
- Opcionalmente incluye el inspector de objetos (autos en el sistema).

##### `snapshotObjetos()`
- Para cada auto en el sistema, llama a `ubicacionAuto(id)` y `humedadActual()`.
- Retorna una lista con el estado detallado de cada auto.

##### `ubicacionAuto(id)`
- Determina **dónde está** cada parte del auto (carrocería y alfombras).
- Consulta los recursos, las colas y las flags `bodyReady`/`matsReady`.

---

### `App.jsx` — Orquestador React

| Función | Rol |
|---|---|
| `normalizar(params)` | Convierte strings vacíos a 0, limita `maxIteraciones` a 100000 |
| `onSimular()` | Llama a `simular()` y actualiza el estado de React |

Renderiza 4 componentes principales con los resultados.

---

### `utils/format.js` — Utilidades de Formato

| Función | Descripción |
|---|---|
| `num(v, dec=2)` | Formatea número con `dec` decimales; `Infinity` → `"—"` |
| `rndFmt(v)` | Formatea número aleatorio a 2 decimales |

---

## Flujo Completo de un Auto (desde que llega hasta que sale)

```
t=0  Auto llega → evLlegada()
       → tipo + k asignados (elegirTipo)
       → va a QA (o espera en colaQA)

t=2  Fin QA → evFinQA()
       → alfombras → colaAspirado / iniciarAspirado (AA)
       → carrocería → colaLavado / iniciarLavado (lugar i)

t=2+U(3,5)  Fin Aspirado → evFinAA()
       → matsReady = true
       → intentarPA() [¿bodyReady? → PA o espera]

t=2+U(6,12)  Fin Lavado → evFinLavado(i)
       → resolverSecado (RK4, modo 'con' o 'sin')
       → finSecado programado

t=2+U(6,12)+RK  Fin Secado → evFinSecado(i)
       → bodyReady = true
       → Libera lugar + reasigna secadora si corresponde
       → intentarPA() [¿matsReady? → PA o espera]

t=...+3  Fin PA → evFinPA()
       → Auto sale del sistema
       → Suma permanencia y esperas
```

---

## Estadísticas Calculadas

| Estadística | Fórmula |
|---|---|
| Ocupación QA | `busyQA / T * 100` |
| Ocupación AA | `busyAA / T * 100` |
| Ocupación Lugares | `busyLug / (2*T) * 100` |
| Ocupación Secadora | `busySec / T * 100` |
| Tiempo medio de secado | `sumaSecado / countSecado` |
| Permanencia media | `sumaPerm / salidos` |
| Espera media en colas | `sumaEspera / countEspera` |
| Máx. cola QA | `maxColaQA` |

> [!TIP]
> Los acumuladores se actualizan en `acumular(dt)` ANTES de procesar cada evento, usando el **estado previo** del sistema durante el intervalo `[lastClock, ev.time]`.

---

## El auto nunca se divide en dos objetos

Cuando el auto termina el QA y se "separa" en carrocería y alfombras, **no se crean dos objetos nuevos**. Es el **mismo objeto `auto`** referenciado simultáneamente por dos recursos distintos.

```js
function evFinQA() {
    const auto = QA.auto;  // UN solo objeto auto

    // El MISMO auto va a dos recursos distintos
    iniciarAspirado(auto);   // → AA.auto = auto   (alfombras)
    iniciarLavado(auto, 0);  // → lugares[0].auto = auto   (carrocería)
}
```

En un momento dado, esto es lo que hay en memoria:

```
AA.auto          → apunta al objeto auto #3  (procesando alfombras)
lugares[0].auto  → apunta al objeto auto #3  (lavando carrocería)
```

El mismo objeto `auto` aparece en dos lugares a la vez. El sistema lo coordina con dos flags booleanas:

```js
auto.matsReady = false   // ¿terminó el aspirado?
auto.bodyReady = false   // ¿terminó el secado?
```

`intentarPA()` es el punto de reunificación — el que llega **último** encuentra ambas flags en `true` y dispara el PA:

```js
function intentarPA(auto) {
    if (auto.bodyReady && auto.matsReady && !auto.paIniciado) {
        auto.paIniciado = true;
        if (!PA.ocupado) iniciarPA(auto);
        else colaPA.push(auto.id);
    }
    // Si solo uno está listo → no hace nada, el otro lo llamará después
}
```

---

## El falso paralelismo — cómo funciona realmente

JavaScript es **single-threaded**. No hay hilos reales. El "paralelismo" entre el flujo de la carrocería y el de las alfombras es una ilusión del motor de eventos.

### Qué hace evFinQA() en realidad

No "ejecuta" el aspirado ni el lavado. Solo **escribe dos números** (tiempos futuros) en variables y termina:

```js
function iniciarAspirado(auto) {
    S.finAA = clock + U(3,5);       // ← escribe un número, nada más
}

function iniciarLavado(auto, idx) {
    lugares[idx].finLavado = clock + U(6,12);  // ← escribe otro número
}
```

### Cómo queda la lista de eventos después

Antes de `evFinQA()` (clock = 10):
```
S.finAA              = Infinity
lugares[0].finLavado = Infinity
S.proxLlegada        = 22.0
```

Después de `evFinQA()`:
```
S.finAA              = 14.2   ← aspirado programado
lugares[0].finLavado = 18.5   ← lavado programado
S.proxLlegada        = 22.0
```

El paralelismo son **dos números flotando en memoria**. Nada más.

### El bucle los procesa de a uno, en orden

```
proximoEvento() → mínimo(14.2, 18.5, 22.0) = 14.2
  → clock = 14.2 → evFinAA()
    matsReady = true, intentarPA() → bodyReady=false ❌ → no hace nada

proximoEvento() → mínimo(18.5, 22.0) = 18.5
  → clock = 18.5 → evFinLavado()
    lanza RK4, programa finSecado = 20.8

proximoEvento() → mínimo(20.8, 22.0) = 20.8
  → clock = 20.8 → evFinSecado()
    bodyReady = true, intentarPA() → matsReady=true ✅ → PA!
```

> [!NOTE]
> `intentarPA()` no bloquea ni espera. Si solo un flujo terminó, simplemente se va. El otro lo llamará cuando le toque. El segundo en llegar siempre encuentra al primero ya marcado.

---

## Los servidores del sistema

En simulación, un **servidor** es un recurso que procesa entidades. El programa tiene 5 servidores (6 si se cuentan los 2 lugares de lavado por separado):

| Servidor | Variable en código | Capacidad | Cola | Tiempo futuro |
|---|---|---|---|---|
| Quitar Alfombras | `QA` | 1 | `colaQA` | `S.finQA` |
| Aspirado | `AA` | 1 | `colaAspirado` | `S.finAA` |
| Lavado (lugar 1) | `lugares[0]` | 1 | `colaLavado` | `lugares[0].finLavado` |
| Lavado (lugar 2) | `lugares[1]` | 1 | (misma) | `lugares[1].finLavado` |
| Secadora | `secadora` | 1 | (ninguna*) | `lugares[i].finSecado` |
| Poner Alfombras | `PA` | 1 | `colaPA` | `S.finPA` |

`*` La secadora no tiene cola propia. Cuando se libera, `evFinSecado()` busca activamente quién lleva más tiempo secándose solo (FIFO por `dryingStart`).

### Cómo está definido cada servidor en el código

```js
// QA, AA y PA — los más simples
const QA = { ocupado: false, auto: null };
const AA = { ocupado: false, auto: null };
const PA = { ocupado: false, auto: null };

// Secadora — sabe qué LUGAR la está usando, no el auto directamente
const secadora = { ocupada: false, lugar: null };

// Lugares de lavado — más ricos, tienen dos fases (lavar + secar)
const lugares = [
    { estado: 'Libre', auto: null, finLavado: INF, finSecado: INF, secado: null },
    { estado: 'Libre', auto: null, finLavado: INF, finSecado: INF, secado: null },
];

// Colas FIFO (solo guardan IDs)
const colaQA        = [];
const colaAspirado  = [];
const colaLavado    = [];
const colaPA        = [];

// Tiempos futuros de eventos globales
const S = { proxLlegada: INF, finQA: INF, finAA: INF, finPA: INF };
```

### Atributos de cada objeto servidor

**QA / AA / PA:**
| Atributo | Qué guarda |
|---|---|
| `ocupado` | `true` / `false` |
| `auto` | referencia al objeto auto siendo atendido (o `null`) |

**`lugares[i]`:**
| Atributo | Qué guarda |
|---|---|
| `estado` | `'Libre'` / `'Lavando'` / `'SecandoCon'` / `'SecandoSin'` |
| `auto` | referencia al auto en ese lugar |
| `finLavado` | tiempo futuro de fin de lavado |
| `finSecado` | tiempo futuro de fin de secado |
| `secado` | objeto con fases RK4 (tablas de Runge-Kutta) |

**`secadora`:**
| Atributo | Qué guarda |
|---|---|
| `ocupada` | `true` / `false` |
| `lugar` | índice `0` o `1` del lugar que la tiene (`null` si libre) |

> [!NOTE]
> La secadora no tiene referencia directa al auto. Para saber qué auto la usa: `lugares[secadora.lugar].auto`.

### Qué guarda el objeto auto vs. qué guarda el servidor

```
SERVIDOR         →  guarda el tiempo FUTURO
──────────────────────────────────────────────────────
S.finAA               cuándo termina el aspirado
S.finQA               cuándo termina el QA
S.finPA               cuándo termina el PA
S.proxLlegada         cuándo llega el próximo auto
lugares[i].finLavado  cuándo termina el lavado del lugar i
lugares[i].finSecado  cuándo termina el secado del lugar i

AUTO             →  guarda la HISTORIA y FLAGS
──────────────────────────────────────────────────────
auto.llegada          cuándo llegó al sistema
auto.qaEnd            cuándo terminó el QA
auto.washEnd          cuándo terminó el lavado
auto.dryEnd           cuándo terminó el secado
auto.aspEnd           cuándo terminaron las alfombras
auto.bodyReady        flag "carrocería seca y lista"
auto.matsReady        flag "alfombras aspiradas y listas"
auto.esperaQA         tiempo de espera en cola QA
auto.esperaLavado     tiempo de espera en cola Lavado
auto.esperaAspirado   tiempo de espera en cola Aspirado
auto.esperaPA         tiempo de espera en cola PA
```

`proximoEvento()` mira **solo los servidores** (S + lugares), nunca mira adentro del auto. El auto es un "pasajero" — el servidor sabe cuándo va a terminar con él; el auto solo sabe qué le pasó hasta ahora.
