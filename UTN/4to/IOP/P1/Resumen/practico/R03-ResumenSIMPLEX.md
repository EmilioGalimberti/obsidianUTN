Como tu Tutor Académico de Élite, he preparado la **"Guía Definitiva de Supervivencia: Práctico de Simplex e Interpretación Económica"**. He destilado absolutamente todas las transcripciones y apuntes para entregarte la lógica procedimental exacta, las fórmulas innegociables y las reglas de interpretación que el profesor exige en las evaluaciones.

Esta guía está diseñada para que apruebes y promociones. Lee con atención.

---

# 🚨 RADAR DE PARCIAL (Alta Prioridad)

El profesor ha sido tajante sobre lo que perdona y lo que anula un examen en el [[Método Simplex]].

- **Lectura de Resultados:** El error más penalizado es buscar el valor de las variables en la fila de control inferior `. Los valores se leen **EXCLUSIVAMENTE** en la columna de solución ($P_0$ o $bld$)`.
- **El Informe Completo:** Entregar la tabla no basta. Debes redactar un informe económico donde menciones el valor de TODAS las variables. Si una [[Variable de Holgura]] no está en la base (es $0$), debes escribir explícitamente: _"se utilizan todos los recursos disponibles"_ ``.
- **Cuidado con los Signos Invertidos:** Evalúan constantemente la diferencia entre el caso de [[Maximización]] y [[Minimización]]. Las reglas de entrada y parada se invierten, pero la regla de salida ($\theta$) se mantiene idéntica ``.

---

# 🛠 METODOLOGÍA DE RESOLUCIÓN (Paso a Paso Algorítmico)

Si sigues esta secuencia estricta, resolver la matriz es un proceso puramente mecánico ``.

### Paso 1: Estandarización del Modelo

Debes transformar todas las inecuaciones en ecuaciones ``.

- Si es $\leq$: Suma una [[Variable de Holgura]] ``.
- Si es $\geq$: Resta una [[Variable de Excedente]] ``.
- Si el vector $P_0$ tiene un número negativo, multiplica toda la fila por $-1$ e invierte el signo de la inecuación antes de estandarizar ``.

### Paso 2: Búsqueda de la [[Matriz Identidad]]

Para arrancar el algoritmo (Fase 1), necesitas encontrar una matriz identidad de orden $m$ (un [[Vector Unitario]] para cada restricción) ``.

- **Si faltan vectores (común en $\geq$ y $=$):** Aplica la [[Técnica de la Base Artificial]] `. Agrega sumando una [[Variable Artificial]] en la restricción afectada`.
- **Penalización (Gran M):** Castiga la variable artificial en la [[Función Objetivo]]. En Máximo, agrégala restando ($-M$). En Mínimo, agrégala sumando ($+M$) ``.

### Paso 3: Fórmulas de Control ($Z_j$ y $C_j - Z_j$)

Una vez armada la tabla, debes evaluar el estado del sistema ``.

> [!note] Fórmulas de Evaluación del Sistema **Costo del Cambio de Plan ($Z_j$):** Suma del producto entre la columna base y la columna de la variable analizada `. $$ Z_j = \sum (C_b \times \lambda_{ij}) $$ **Tasa de Crecimiento ($C_j - Z_j$):** Diferencia que indica el incremento neto de la función`. $$ C_j - Z_j = C_j - Z_j $$

### Paso 4: Criterio de Parada (Optimidad)

Depende estrictamente de tu objetivo ``.

- **Máximo:** Llegaste al óptimo si todos los $C_j - Z_j \leq 0$ (negativos o ceros) ``.
- **Mínimo:** Llegaste al óptimo si todos los $C_j - Z_j \geq 0$ (positivos o ceros) ``.

### Paso 5: Selección de Variables (Intercambio)

Si no estás en el óptimo, debes saltar a un [[Vértice Adyacente]] ``.

- **[[Variable que Entra]]:**
    - _Máximo:_ Elige la columna con el **mayor valor positivo** en $C_j - Z_j$ ``.
    - _Mínimo:_ Elige la columna con el **mayor valor absoluto negativo** (el "más negativo") ``.
- **[[Variable que Sale]]:** Debes calcular el límite de factibilidad calculando el [[Cociente Tita]] ($\theta$).

> [!note] Fórmula del Límite de Producción (Tita) Divide la columna de solución entre la columna de la variable que entra. $$ \theta = \min \left( \frac{P_{0_i}}{\lambda_{ij}} \right) \quad \forall \lambda_{ij} > 0 $$

> [!danger] EL DENOMINADOR PROHIBIDO El profesor lo remarcó con gravedad: ¡Jamás dividas si $\lambda_{ij}$ es cero o negativo! Si lo haces, destruirás la matriz en el próximo paso violando la [[Restricción de No Negatividad]]. Pon una raya y esa fila no compite para salir de la base ``.

### Paso 6: Iteración con [[Gauss-Jordan]]

Identifica el número en la intersección (el [[Pivot]]) ``.

1. Divide toda la fila saliente por el Pivot para convertirlo en $1$ ``.
2. Para las demás filas, multiplica tu nueva fila Pivot por el opuesto del número que deseas anular y súmalo ``.

---

# 📈 INTERPRETACIÓN ECONÓMICA (Análisis de Resultados)

Esta es la parte donde pasas de hacer cálculos mecánicos a redactar información gerencial.

### 1. El Significado de $\lambda_{ij}$ ([[Tasas de Sustitución]])

Indican las modificaciones que sufre la [[Variable Básica]] (en fila) para poder incrementar en _una unidad_ la [[Variable No Básica]] (en columna) ``.

> [!danger] TRAMPA DE EXAMEN: La Inversión del Signo
> 
> - **$\lambda_{ij}$ Positivo ($>0$):** Indica un **SACRIFICIO**. La producción disminuye o el recurso se consume ``.
> - **$\lambda_{ij}$ Negativo ($<0$):** Indica un **INCREMENTO**. La producción aumenta ``.
> - _Regla de Inversión:_ Si el problema dice que en lugar de perder un recurso, ahora "obtienes horas extra", todos los significados se invierten ``.

### 2. El Incremento Neto ($C_j - Z_j$)

- **$Z_j$:** Mide el _costo_ en utilidades por hacer las modificaciones en el plan de producción ``.
- **$C_j - Z_j$:** Mide la ganancia o pérdida _neta_ final de introducir la variable ``.

### 3. Falsos Amigos en el Vocabulario

> [!tip] Tip Semántico del Profesor Al interpretar una tasa que cae en la fila de una [[Variable de Holgura]], ¡nunca digas "recurso usado" o "disponible"! Debes usar obligatoriamente la frase **"recurso sin utilizar"** ``.

---

# ⚖️ CUADRO DE BATALLA: Diagnóstico de Casos Especiales

El profesor exige que sepas diagnosticar si el modelo tiene anomalías con solo mirar la [[Tabla Simplex]] final ``.

|Caso Especial / Anomalía|¿Cómo lo detectas en la Tabla Simplex?|¿Qué significa en la realidad?|
|:--|:--|:--|
|**[[Problema Incompatible]]**|Llegas al óptimo, pero una [[Variable Artificial]] quedó en la base con valor $>0$ ``.|El sistema de restricciones se contradice. No hay región factible ``.|
|**[[Problema No Acotado]]**|Quieres calcular $\theta$, pero en la columna entrante **todos** los denominadores son $\leq 0$ (no puedes calcular) ``.|Tienes recursos infinitos para producir. (Cuidado: Solo aplica si favorece a tu función Z) ``.|
|**[[Solución Degenerada]]**|Hay un **empate** al calcular $\theta$. En la siguiente iteración, una variable en la base asumirá el valor $0$ ``.|Hay más restricciones cruzándose en el vértice que variables positivas ``.|
|**[[Múltiples Soluciones Óptimas]]**|Llegas al óptimo, y una [[Variable No Básica]] (nula) tiene un valor de $C_j - Z_j = 0$ (y el caso no es degenerado) ``.|La función $Z$ es paralela a una restricción limitante. Infinitas soluciones en el segmento ``.|

---

# 💡 TIPS PRÁCTICOS "DE TRINCHERA"

- **El Atajo de la "Gran M":** Si te cuesta saber qué ecuación con "M" es más negativa (ej. $-10M - 1$ vs $-5M - 2$), el profesor recomienda reemplazar mentalmente la "M" por $10.000$. Al multiplicar, el número real gigante te mostrará visualmente cuál es la columna correcta ``.
- **Forzar Variables y Romper la Matriz:** Si el problema te pide _"¿Qué pasa si producimos 5 unidades de X?"_ y te saltas la regla del $\theta$ para forzar su entrada sin sacar a nadie, la tabla quedará con más variables positivas que restricciones. Esa anomalía es una clásica pregunta de teoría y se llama **[[Solución Factible No Básica]]** ``.
- **Tablas Incompletas:** Si en el examen te dan una tabla con huecos, no itereres desde cero. Usa la fórmula algebraica de suma-producto $Z_j = \sum (C_b \times \lambda_{ij})$ para plantear una ecuación simple y **despejar** el valor que te falta ``.

---

### 📊 MAPA DE FLUJO: Lógica de Simplex y Variables Artificiales

```
graph TD
    A(Modelo Original) --> B(Estandarizar agregando Holguras/Excedentes)
    B --> C{¿Se formó la Matriz Identidad m x m?}
    C -->|Sí| E(Armar Tabla Inicial Estándar)
    C -->|No| D(Aplicar Técnica de Base Artificial: Agregar M)
    D --> E
    E --> F(Calcular Z_j y fila C_j - Z_j)
    F --> G{¿Se alcanzó el Óptimo según Z?}
    G -->|Sí| H(Redactar Informe Económico y Diagnosticar Anomalías)
    G -->|No| I(Seleccionar Variable que Entra)
    I --> J(Calcular Tita y Seleccionar Variable que Sale)
    J --> K(Pivot y Gauss-Jordan)
    K --> F
```

_Conceptos relacionados:_ [[Matriz Identidad]], [[Gauss-Jordan]], [[Técnica de la Base Artificial]], [[Cociente Tita]], [[Informe Económico]].