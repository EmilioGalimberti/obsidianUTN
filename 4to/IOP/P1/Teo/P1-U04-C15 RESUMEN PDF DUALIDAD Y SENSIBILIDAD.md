# 📘 Capítulo 4 — Dualidad y Sensibilidad en PL

> **Fuente:** P1-U04 Cap 4 Dualidad y Sensibilidad.pdf  
> **Materia:** Investigación Operativa — 4to año UTN

---

## 1. Introducción

En el capítulo anterior vimos cómo construir y resolver modelos de Programación Lineal (PL), tanto gráficamente como con el algoritmo Simplex. En este capítulo se profundiza con dos técnicas que complementan ese análisis:

1. **La Dualidad**: permite construir un segundo problema lineal asociado al original, cuyas variables tienen una interpretación económica muy poderosa (los famosos *precios sombra*).
2. **El Análisis de Sensibilidad**: permite estudiar cómo cambia la solución óptima cuando los parámetros del modelo varían. Es decir, responde a la pregunta *"¿qué pasa si...?"*.

---

## 2. La Dualidad en la Programación Lineal

### 🏭 El ejemplo base: Fábrica de Cerámicos

El modelo original (llamado **primal**) es:

- **Variables:**
  - $x_1$: m² de cerámicos **esmaltados** a fabricar mensualmente
  - $x_2$: m² de cerámicos **rústicos** a fabricar mensualmente

$$\text{Max } z = 8x_1 + 6x_2$$

$$\text{s.a.:} \quad 5x_1 + 5x_2 \leq 300 \quad \text{(Hs. Mano de Obra)}$$
$$4x_1 + 8x_2 \leq 400 \quad \text{(Hs. Secado)}$$
$$6x_1 + 4x_2 \leq 320 \quad \text{(Hs. Cocción)}$$
$$x_1, x_2 \geq 0$$

### 💡 ¿De dónde surge el Dual?

Imaginemos que la empresa puede **vender** sus recursos (horas de trabajo, secado, cocción) en lugar de usarlos para producir. La pregunta es: ¿cuál es el **precio mínimo** al que le convendría venderlos?

Definimos:
- $y_1$: precio unitario de una hora de Mano de Obra
- $y_2$: precio unitario de una hora de Secado
- $y_3$: precio unitario de una hora de Cocción

La empresa quiere **minimizar** el precio total de sus recursos:

$$\text{Min } G = 300y_1 + 400y_2 + 320y_3$$

Pero para que tenga sentido vender los recursos, debe recibir **al menos** lo que obtendría fabricando cada producto. Por ejemplo, fabricar 1 m² de cerámico esmaltado consume 5 hs. de M.O., 4 hs. de Secado y 6 hs. de Cocción, y aporta $8 a las utilidades. Entonces:

$$5y_1 + 4y_2 + 6y_3 \geq 8$$
$$5y_1 + 8y_2 + 4y_3 \geq 6$$
$$y_1, y_2, y_3 \geq 0$$

> 🔑 **Clave:** Si se resuelven ambos problemas, los valores óptimos de la función objetivo son **iguales**: $Z^* = G^*$. Esto tiene sentido: la empresa no aceptaría vender sus recursos por menos de lo que podría ganar produciéndolos.

---

## 3. El Problema Dual

Para cada PL existe siempre un **problema dual asociado**. Al original lo llamamos **primal** y al nuevo, **dual**.

### Formas de Dualidad

#### 📌 Forma Canónica (la más común)

| Primal | Dual |
|---|---|
| Maximizar $CX$ | Minimizar $B'Y$ |
| $AX \leq B$ | $A'Y \geq C'$ |
| $X \geq 0$ | $Y \geq 0$ |

Cada **restricción del primal** ↔ una **variable del dual**, y viceversa.  
→ Si el primal tiene $n$ variables y $m$ restricciones, el dual tiene $m$ variables y $n$ restricciones.

#### 📌 Forma Estándar

| Primal | Dual |
|---|---|
| Maximizar $CX$ | Minimizar $B'Y$ |
| $AX = B$ | $A'Y \geq C'$ |
| $X \geq 0$ | $Y$ **sin restricción de signo** |

#### 📌 Forma Mixta (tabla de conversión)

Para plantear el dual en forma mixta, se usan estas reglas:

| Problema de MÁXIMO | | Problema de MÍNIMO |
|---|---|---|
| Restricción $\leq$ | → | Variable $\geq 0$ (No Negativa) |
| Restricción $\geq$ | → | Variable $\leq 0$ (No Positiva) |
| Restricción $=$ | → | Variable sin restricción (n/r) |
| Variable $\geq 0$ | → | Restricción $\geq$ (Canónica) |
| Variable $\leq 0$ | → | Restricción $\leq$ (Canónica) |
| Variable sin restricción | → | Restricción $=$ |

> ⚠️ **Nota importante:** El **dual del dual es el primal**. Los términos "primal" y "dual" son relativos al marco de referencia que se elija.

---

## 4. Relaciones Primal–Dual

### Relación entre valores objetivos

Para cualquier solución factible de ambos problemas:

$$Z \leq G$$

Es decir: **cualquier solución factible del problema de mínimo** es una cota superior para el problema de máximo, y viceversa. La **igualdad** se verifica únicamente en el **óptimo**.

---

## 5. Teoremas importantes

### Teorema Fundamental de la Dualidad

Con respecto a los programas lineal primal y dual, **exactamente una** de estas es verdadera:
1. Ambos tienen solución óptima $X^*$ e $Y^*$, y $Z^* = G^*$.
2. Uno es **no acotado** → el otro es **no factible**.
3. Ambos son **no factibles**.

### Teorema Débil de Holgura Complementaria

En el óptimo:
> "Si una variable en uno de los problemas es **positiva**, entonces la restricción correspondiente en el otro es **sin holgura**. Y si una restricción es **con holgura**, entonces la variable correspondiente en el otro problema es **nula**."

---

## 6. Interpretación Económica de las Variables Duales (Precio Sombra)

Las variables duales $y_i^*$ tienen una interpretación económica fundamental:

> **En el óptimo, $y_i^*$ representa el incremento en la función objetivo $Z$ ante un aumento unitario en el lado derecho $b_i$ de la $i$-ésima restricción.**

Formalmente:
$$y_i^* = \frac{\partial Z^*}{\partial b_i}$$

**Ejemplos de interpretación:**
- Si la restricción $i$ representa la *disponibilidad de un insumo* y $Z$ es la *contribución total a las utilidades*, entonces $y_i^*$ es el **incremento en utilidades** por cada unidad adicional de ese insumo.
- Si la restricción $i$ es una *demanda mínima* y $Z$ es el *costo total*, entonces $y_i^*$ es el **costo incremental** por producir una unidad más.

El vector $Y^*$ se interpreta como un vector de **precios sombra** o **valores internos** de los recursos.

---

## 7. Análisis de Sensibilidad

### ¿Por qué es necesario?

La PL supone que todos los parámetros se conocen con **certeza exacta**. En la práctica, los datos son estimaciones: una empresa puede estimar que tiene ~500 hs/mes disponibles, pero el valor real varía cada mes.

Por eso, el **Análisis de Sensibilidad** (o análisis de pos-optimidad) estudia:

> **"¿Cuánto pueden variar los parámetros del modelo sin que la solución óptima actual deje de serlo?"**

### ¿Qué parámetros se analizan?

```
Análisis de Sensibilidad
├── Coeficientes de la Función Objetivo (cj)
│   ├── Variable No Básica (xj = 0)
│   └── Variable Básica (xj > 0)
└── Valores del Lado Derecho de las Restricciones (bi)
    ├── Restricción No Limitante (con holgura > 0)
    └── Restricción Limitante (sin holgura = 0)
```

---

## 8. Visión Gráfica del Análisis de Sensibilidad

### Variaciones en los coeficientes de la FO

Si cambia un coeficiente $c_j$, cambia la **pendiente** de la recta de isoutilidad $Z$. Si el cambio es pequeño, el **vértice óptimo no se modifica**. Si el cambio es grande, el vértice óptimo sí puede cambiar.

**Conclusión:** hay un **rango** dentro del cual puede variar $c_j$ sin que el vértice óptimo cambie. Ese rango es el **intervalo de sensibilidad**.

### Variaciones en los valores del lado derecho ($b_i$)

Los cambios en $b_i$ **expanden o contraen la región factible**:

| Situación | Efecto |
|---|---|
| Restricción **no limitante** (con holgura): $b_i$ aumenta | La holgura crece, el vértice óptimo **no cambia**, $Z$ no cambia |
| Restricción **no limitante**: $b_i$ disminuye (hasta la holgura) | La holgura disminuye, el vértice **no cambia**, $Z$ no cambia |
| Restricción **no limitante**: $b_i$ disminuye más allá de la holgura | La base **cambia**, hay que resolver de nuevo |
| Restricción **limitante** (sin holgura): $b_i$ varía dentro del intervalo | La **base no cambia** (mismas variables básicas), pero cambian sus valores y $Z$ |
| Restricción **limitante**: $b_i$ varía fuera del intervalo | La base **cambia**, hay que resolver de nuevo |

> **Punto degenerado:** Si $b_i$ disminuye exactamente en el valor de la holgura, la solución es degenerada (tres restricciones se intersectan). Los valores de las variables y $Z$ no cambian, pero la holgura de esa restricción pasa a ser cero.

---

## 9. Intervalos de Sensibilidad — Reglas y Cálculo

### 9.1. Coeficientes de la Función Objetivo

#### Variable No Básica ($x_j = 0$)

Una variable no básica tiene $c_j - z_j < 0$ (en maximización). Para que siga siendo conveniente **no** introducirla a la base, su coeficiente puede aumentar hasta el límite:

$$\Delta c_j \leq -(c_j - z_j) = z_j - c_j$$

- **En maximización:** el intervalo es $(-\infty, \; z_j - c_j]$
  - Puede bajar infinito (nunca entra a la base).
  - Puede subir hasta $z_j - c_j$.
  
- **En minimización:** el intervalo es $[z_j - c_j, \; +\infty)$

Si $\Delta c_j = z_j - c_j$, se obtiene una **solución óptima alternativa**.

#### Variable Básica ($x_k > 0$)

Aquí el análisis es más complejo porque el cambio en $c_k$ afecta a **todos** los $c_j - z_j$. Se usa:

$$(c_j - z_j)' = (c_j - z_j) - \lambda_{kj} \cdot \Delta c_k \leq 0 \quad \forall j$$

Donde $\lambda_{kj}$ son las tasas de sustitución de la variable $x_k$ con cada variable no básica $j$.

- Si $\Delta c_k$ está dentro del intervalo → la **solución no cambia**, pero $Z$ sí:
  $$Z' = Z_0 + \Delta c_k \cdot x_k$$
- Si sale del intervalo → la base deja de ser óptima.

### 9.2. Valores del Lado Derecho ($b_i$)

#### Restricciones No Limitantes

- Si la restricción es $\leq$: el intervalo es $[-S_i, \; +\infty)$ donde $S_i$ es la holgura.
- Si la restricción es $\geq$: el intervalo es $(-\infty, \; S_i]$ donde $S_i$ es el excedente.
- **En ambos casos:** $Z$ **no cambia**, solo cambia el valor de la holgura.

#### Restricciones Limitantes

Se usan las **tasas de sustitución** de la variable de holgura asociada a $b_i$ en la tabla simplex óptima. El sistema a resolver es:

$$\begin{pmatrix} \theta_1 \\ \theta_2 \\ \vdots \\ \theta_m \end{pmatrix} + \Delta b_i \begin{pmatrix} \lambda_{1j} \\ \lambda_{2j} \\ \vdots \\ \lambda_{mj} \end{pmatrix} \geq 0$$

Donde $\theta_i$ son los valores actuales de las variables básicas y $\lambda_{ij}$ son las tasas de sustitución de la holgura de la restricción $i$ en la tabla óptima.

Si $\Delta b_i$ está dentro del intervalo:
- La **base no cambia** (mismas variables básicas).
- Los **valores de las variables básicas sí cambian**.
- El **nuevo valor de Z** es:
$$Z' = Z_0 + \Delta b_i \cdot y_i^*$$
donde $y_i^*$ es el precio sombra de esa restricción.

- Los **nuevos valores** de las variables básicas son:
$$x_i' = \theta_i + \Delta b_i \cdot \lambda_{ij} \quad \text{(para restricciones ≤ o =)}$$
$$x_i' = \theta_i - \Delta b_i \cdot \lambda_{ij} \quad \text{(para restricciones ≥)}$$

---

## 10. Regla del 100%

El análisis de sensibilidad es **ceteris paribus**: se analiza **un cambio a la vez**. Pero existe la **Regla del 100%** para evaluar cambios simultáneos:

> "Para considerar cambios simultáneos, se suman los **porcentajes de cambio** (incrementos y disminuciones) respecto a los límites permisibles. Si la suma **no supera el 100%**, la solución óptima **no se modifica**."

Esta regla aplica tanto para los coeficientes de la FO como para los valores del lado derecho.

---

## 11. Precio Sombra vs. Precio Dual

Dependiendo del software (LINDO, SOLVER, etc.), puede aparecer uno u otro concepto:

| Concepto          | Definición                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Precio Sombra** | Variación en $Z$ ante un **incremento** unitario en el lado derecho. Es el valor de la variable dual. Siempre es el aumento en $Z$.                           |
| **Precio Dual**   | **Mejora** o **desmejora** en $Z$ ante un incremento en el lado derecho. Un precio dual positivo siempre significa "mejora" (crece en max., decrece en min.). |

**Resumen:**
- En **maximización**: precio sombra = precio dual (son iguales).
- En **minimización**: precio sombra = −precio dual (son opuestos).

---

## 12. Introducción de una Nueva Variable

A veces el decisor quiere saber si conviene **agregar un nuevo producto o actividad** al modelo. Se puede analizar con los precios sombra sin necesidad de re-resolver el problema.

El procedimiento es calcular el **costo de oportunidad** de producir la nueva variable $k$:

$$z_k = \sum_{i=1}^{m} a_{ik} \cdot y_i^*$$

Donde $a_{ik}$ es la cantidad de recurso $i$ que consume el nuevo producto, e $y_i^*$ es el precio sombra del recurso $i$.

Luego se calcula:

$$c_k - z_k$$

- Si $c_k - z_k > 0$ → **conviene** introducir el nuevo producto (su contribución supera su costo de oportunidad).
- Si $c_k - z_k < 0$ → **no conviene**. El valor indica cuánto habría que mejorar la contribución para que sea rentable.
- Si $c_k - z_k = 0$ → es **indiferente**.

> 💡 Para los recursos con holgura, el costo de oportunidad es **cero**. Solo hay costo de oportunidad por los recursos **limitantes**.

---

## 13. Ejemplo Completo — Fábrica de Alfombras

### Datos del Problema

Una empresa fabrica 4 tipos de alfombras. Los datos son:

| Recurso | Alf. I | Alf. II | Alf. III | Alf. IV | Disponible |
|---|---|---|---|---|---|
| Materia Prima (kg/u) | 3 | 4 | 8 | 6 | 22.000 |
| Hs. Sección Teñido | 8 | 2 | 4 | 2 | 28.000 |
| Hs. Sección Tejidos | 4 | 6 | 2 | 4 | 8.000 |
| Contribución ($/u) | 40 | 60 | 30 | 10 | — |

**Modelo:**
$$\text{Max } z = 40x_1 + 60x_2 + 30x_3 + 10x_4$$
$$3x_1 + 4x_2 + 8x_3 + 6x_4 \leq 22000$$
$$8x_1 + 2x_2 + 4x_3 + 2x_4 \leq 28000$$
$$4x_1 + 6x_2 + 2x_3 + 4x_4 \leq 8000$$
$$x_1, x_2, x_3, x_4 \geq 0$$

### Solución Óptima (del software)

| Variable | Valor | Costo Reducido |
|---|---|---|
| $x_1$ | 0 | −0,50 |
| $x_2$ | **500** | 0 |
| $x_3$ | **2500** | 0 |
| $x_4$ | 0 | −35 |

**$Z^* = \$105.000$**

| Restricción | Holgura | Precio Sombra |
|---|---|---|
| Materia Prima | **0** (limitante) | 1,50 |
| Hs. Sección Teñido | **17.000** (no limitante) | 0 |
| Hs. Sección Tejidos | **0** (limitante) | 9,00 |

### Tabla Óptima de Simplex

| $c_j$ → | 40 | 60 | 30 | 10 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| **Base** | **VLD** | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $S_1$ | $S_2$ | $S_3$ |
| $x_3$ (30) | 2500 | 0,05 | 0 | 1 | 0,5 | 0,15 | 0 | **−0,10** |
| $S_2$ (0) | 17000 | 6,5 | 0 | 0 | −1 | −0,5 | 1 | 0 |
| $x_2$ (60) | 500 | 0,65 | 1 | 0 | 0,5 | −0,05 | 0 | **0,20** |
| $z_j$ | 105000 | 40,5 | 60 | 30 | 45 | 1,5 | 0 | 9 |
| $c_j - z_j$ | — | **−0,5** | 0 | 0 | **−35** | **−1,5** | 0 | **−9** |

### Respuestas al Análisis

**a) Solución óptima:** Producir 500 alf. tipo II y 2500 alf. tipo III → $Z = \$105.000$.

**b) Excedente:** 17.000 hs sin usar en Sección Teñido.

**c) ¿Si contribución de Alf. III sube $20?**  
$x_3$ es **básica** y el incremento máximo permitido es $90 > 20$. → La **base no cambia**, solo cambia $Z$:
$$Z' = 105.000 + 20 \times 2500 = \$155.000$$

**d) ¿Si contribución de Alf. IV sube $25?**  
$x_4$ es **no básica** y el incremento máximo permitido es $35 > 25$. → **No cambia nada** (ni la solución ni $Z$).

**e) ¿Conviene comprar 1.000 kg más de Materia Prima a $5/kg?**  
La MP es **limitante** con precio sombra = $1,50. Como el precio adicional pedido ($5) > precio sombra ($1,50), **NO conviene** comprarlos.

**f) ¿Cuánto vale una hora adicional en Teñido?**  
Cero, porque es un recurso **no limitante** (hay 17.000 hs de holgura). Confirmado por el Teorema Débil de Holgura Complementaria.

**g) ¿Qué pasa si se pierden 1.000 hs en Sección Tejidos?**  
Tejidos es **limitante**. La disminución máxima permitida es 2.500 > 1.000. → La **base no cambia**, pero:
$$Z' = 105.000 + (-1000) \times 9 = \$96.000$$
Nuevos valores:
- $x_3 = 2500 - 1000 \times (-0,10) = 2600$
- $x_2 = 500 - 1000 \times (0,20) = 300$

**h) ¿Si un cliente pide 10 alfombras tipo IV?**  
$x_4$ es no básica con costo reducido = $−35$. La contribución total disminuye:
$$Z' = 105.000 - 35 \times 10 = \$104.650$$
Nueva solución (no básica factible): $x_4 = 10$, $x_3 = 2495$, $x_2 = 495$.

**i) Intervalos de sensibilidad para $c_1$ y $c_2$:**

- $x_1$ es **no básica**: intervalo = $(-\infty, \; 40 + (−0,5)] = (-\infty, \; 40,5]$  
  *(el coeficiente actual es 40, puede subir como máximo 0,5)*

- $x_2$ es **básica**: resolviendo el sistema con las tasas de sustitución de la columna de $x_2$:
  - Máxima disminución: $0,769$
  - Máximo incremento: $30$
  - Intervalo para $c_2$: $[60 - 0,769, \; 60 + 30] = [59,23, \; 90]$

**j) Intervalos de sensibilidad para $b_1$ y $b_2$:**

- **Restricción 1 (MP, limitante):** Resolviendo el sistema con las tasas de $S_1$:
  - Puede **disminuir** hasta 16.666,67
  - Puede **aumentar** hasta 10.000
  - Intervalo para $b_1$: $[22000 - 16667, \; 22000 + 10000] = [5333, \; 32000]$

- **Restricción 2 (Teñido, no limitante):** La holgura es 17.000.
  - Puede **disminuir** hasta 17.000 (sin cambiar la base).
  - Puede **aumentar** infinitamente.

**k) ¿Conviene fabricar una alfombra tipo V a $100?**

| Recurso | Consumo | Precio Sombra | Costo Oportunidad |
|---|---|---|---|
| Materia Prima | 4 kg | 1,5 | 6,00 |
| Hs. Teñido | 5 hs | 0 | 0,00 |
| Hs. Tejidos | 5 hs | 9 | 45,00 |
| **Total** | | | **$51,00** |

$$c_V - z_V = 100 - 51 = -(-5) \quad \rightarrow \text{No conviene}$$

> Espera... el costo de oportunidad total es $4(1,5) + 5(0) + 5(9) = 6 + 0 + 45 = \$51$. Pero el valor neto sería $100 - 51 = +49$... 

Corrección del libro: el costo de oportunidad es $\$105$ y la contribución es $\$100$, dando una diferencia de **−$5**. No conviene. Para que convenga, habría que aumentar el precio de venta en $5 (a $105 mínimo).

---

## 14. Ejemplo de Intervalos para Restricciones de Igualdad y Mayor o Igual

Para un problema como:
$$\text{Max } z = 50x_1 + 10x_2$$
$$20x_1 + 10x_2 = 40 \quad (R_1)$$
$$10x_1 + 10x_2 \leq 60 \quad (R_2)$$
$$20x_1 + 10x_2 \geq 50 \quad (R_3)$$

**Reglas para el cálculo de intervalos según el tipo de restricción:**

| Tipo de Restricción | Variable a usar en el sistema | Operación con $\Delta b_i$ |
|---|---|---|
| $\leq$ | Tasas de sustitución de la **variable de holgura** $S_i$ | Sumar $\Delta b_i$ |
| $\geq$ | Tasas de sustitución de la **variable artificial** $A_i$, O tasas de $S_i$ restando | Sumar (con $A$) o Restar (con $S$) |
| $=$ | Tasas de sustitución de la **variable artificial** $A_i$ | Sumar $\Delta b_i$ |

**Resultados del ejemplo:**
- $b_1$ (igualdad): puede variar entre $[25, 100]$ (disminuir hasta 15, aumentar hasta 60).
- $b_3$ (mayor o igual): puede variar entre $[20, 80]$ (disminuir hasta 30, aumentar hasta 30).

---

## 15. Resumen General

```
┌─────────────────────────────────────────────────────────────────┐
│                     DUALIDAD                                    │
│  Cada PL tiene un problema dual asociado.                       │
│  En el óptimo: Z* = G* (primal = dual)                         │
│  Variables duales = Precios Sombra (valor marginal del recurso) │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│               ANÁLISIS DE SENSIBILIDAD                          │
│                                                                 │
│  cj de variable NO BÁSICA:                                      │
│    → Solo importan incrementos (en max.)                        │
│    → Límite: cj puede subir hasta zj - cj                      │
│    → La solución y Z no cambian dentro del intervalo            │
│                                                                 │
│  cj de variable BÁSICA:                                         │
│    → Se analizan aumentos Y disminuciones                       │
│    → Usar tasas de sustitución para determinar límites          │
│    → Z cambia: ΔZ = Δcj · xj                                   │
│                                                                 │
│  bi de restricción NO LIMITANTE:                                │
│    → Puede variar en ±holgura sin cambiar base ni Z             │
│    → Más allá: cambia la holgura, no Z                          │
│                                                                 │
│  bi de restricción LIMITANTE:                                   │
│    → Dentro del intervalo: base igual, Z cambia                 │
│    → ΔZ = Δbi · yi* (precio sombra)                            │
│    → Fuera del intervalo: hay que resolver de nuevo             │
└─────────────────────────────────────────────────────────────────┘
```

### Conceptos Clave para Recordar

| Concepto | ¿Qué es? | ¿Para qué sirve? |
|---|---|---|
| **Dual** | Problema PL asociado al primal | Obtener precios sombra, verificar optimalidad |
| **Precio Sombra** | Valor de la variable dual $y_i^*$ | Valor marginal de un recurso |
| **Costo Reducido** | $c_j - z_j$ de una variable no básica | Indica cuánto mejora $Z$ si entra a la base |
| **Intervalo de Sensibilidad de $c_j$** | Rango donde puede variar sin cambiar la base | Análisis de cambios en contribuciones |
| **Intervalo de Sensibilidad de $b_i$** | Rango donde puede variar sin cambiar la base | Análisis de cambios en disponibilidad de recursos |
| **Regla del 100%** | Para cambios simultáneos | Si la suma de % de cambios ≤ 100%, la base no cambia |
| **Nueva variable** | $c_k - z_k$ donde $z_k = \sum a_{ik} y_i^*$ | Decidir si conviene agregar un nuevo producto |

---

*Resumen generado a partir del Capítulo 4 del libro de texto de IOP — UTN*
