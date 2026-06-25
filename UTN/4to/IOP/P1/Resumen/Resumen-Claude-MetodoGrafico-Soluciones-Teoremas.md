# 📘 Resumen Teórico-Práctico: Método Gráfico, Soluciones y Teoremas de PL
> *Generado por Claude — Basado en libro (Cap 3-4), clases teóricas (C04, C06) y ejercicios prácticos*

---

# PARTE I — TEORÍA FUNDAMENTAL

---

## 1. ¿Qué significa resolver un Programa Lineal?

Resolver un PL significa **encontrar un conjunto de valores para las variables de decisión** que:
1. Cumplan **todas** las restricciones (incluidas las de no negatividad)
2. **Optimicen** (maximicen o minimicen) la función objetivo $Z$

---

## 2. Forma Estándar del Modelo

Antes de clasificar soluciones o resolver algebraicamente, el modelo debe transformarse a su **Forma Estándar**: Todo análisis y clasificación de soluciones se hace sobre un modelo donde las desigualdades se transformaron en igualdades agregando [[Variables de Holgura]]
### Regla de estandarización

| Signo original | Acción              | Nombre técnico        | En la F.O.      |
| :------------- | :------------------ | :-------------------- | :-------------- |
| $\leq$         | Se **suma** $+S_i$  | Variable de Holgura   | Coeficiente $0$ |
| $\geq$         | Se **resta** $-S_i$ | Variable de Excedente | Coeficiente $0$ |
| $=$            | Ninguna             | —                     | —               |

> [!danger] Trampa de parcial: el signo de la variable
> Que se *reste* una variable de excedente **NO** significa que la variable sea negativa. La variable siempre cumple $S_i \geq 0$. El signo menos es una **operación algebraica**, no el valor de la variable.

### Ejemplo de estandarización

**Modelo original:**
$$\max Z = 2x_1 + 3x_2$$
$$4x_1 + 2x_2 \leq 20$$
$$2x_1 + 4x_2 \leq 16$$
$$x_1 + x_2 \leq 15$$

**Forma estándar** (se agrega una $S_i$ por cada restricción $\leq$):
$$\max Z = 2x_1 + 3x_2 + 0S_1 + 0S_2 + 0S_3$$
$$4x_1 + 2x_2 + S_1 = 20$$
$$2x_1 + 4x_2 + S_2 = 16$$
$$x_1 + x_2 + S_3 = 15$$

Aquí tenemos:
- $n = 5$ variables totales ($x_1, x_2, S_1, S_2, S_3$)
- $m = 3$ restricciones funcionales (sin contar no negatividad)

---

## 3. Método Gráfico — Algoritmo paso a paso

> Solo aplicable cuando el problema tiene **2 variables de decisión** (máximo 3).

### Los 6 pasos del método

**Paso 1 — Graficar restricciones e identificar la Región Factible**
1. Trabajar siempre en el **1er cuadrante** (por la condición de no negatividad)
2. Para cada restricción, plantearla como **igualdad** y encontrar los puntos donde la recta corta los ejes:
   - Hacer $x_1 = 0$ → obtener $x_2$
   - Hacer $x_2 = 0$ → obtener $x_1$
3. Trazar la recta entre esos dos puntos
4. **Identificar el semiplano válido** usando un punto de prueba

> [!tip] Técnica del Punto de Prueba
> Tomar un punto fácil (generalmente el origen $(0,0)$) y reemplazarlo en la inecuación original:
> - Si la desigualdad **se cumple** → el semiplano correcto es el que **contiene** ese punto
> - Si **no se cumple** → el semiplano correcto es el del **lado contrario**
> 
> ⚠️ **NUNCA asumir** que "$\leq$ va para abajo" o "$\geq$ va para arriba". Depende de la pendiente de la recta.

5. La **intersección de todos los semiplanos** válidos en el 1er cuadrante es la **Región Factible** (o Poliedro de Soluciones)

**Paso 2 — Trazar la recta de la Función Objetivo**
- Asignar un **valor arbitrario** a $Z$ que encaje en la escala del gráfico
- La forma explícita de la recta es:
$$x_2 = \frac{Z}{c_2} - \frac{c_1}{c_2} x_1$$
  donde $-\frac{c_1}{c_2}$ es la **pendiente** de $Z$

**Paso 3 — Desplazar Z en el sentido de optimidad**
- **Maximización:** desplazar paralelamente **alejándose** del origen (la ordenada al origen crece)
- **Minimización:** desplazar paralelamente **acercándose** al origen (la ordenada al origen decrece)
- El **último punto de contacto** entre la recta $Z$ y el poliedro es la **solución óptima**

> [!danger] Trampa mortal de parcial: "El punto más alejado del origen"
> **NUNCA** definir el óptimo como "el punto más alejado del origen". Esto involucra el concepto geométrico de distancia, que es INCORRECTO. La definición correcta es: **el último punto que tienen en común la recta de Z y el poliedro de soluciones** al desplazarla en el sentido de optimidad.

> [!warning] El óptimo depende de la INCLINACIÓN de Z
> Si se dibuja mal la pendiente de la función objetivo, se elige un vértice equivocado. Prestar mucha atención al trazar la recta.

**Paso 4 — Calcular los valores exactos de las variables**
- Identificar las **2 rectas de restricción** que se cruzan en el vértice óptimo
- Plantear el **sistema de 2 ecuaciones** con esas restricciones
- Resolver por **sustitución, igualación o Cramer** (Gauss-Jordan)

> [!danger] Trampa de parcial: cálculo "a ojo"
> **NUNCA** estimar las coordenadas del vértice leyendo la escala del gráfico. Siempre resolver algebraicamente el sistema de ecuaciones.

**Paso 5 — Calcular las variables de holgura/excedente**
- Reemplazar los valores de $x_1, x_2$ en **cada ecuación** de restricción en forma estándar
- Despejar $S_i$ en cada una

**Paso 6 — Calcular el valor de Z**
- Reemplazar los valores de las variables de decisión en la función objetivo

---

### Restricciones Limitantes vs. No Limitantes

| Concepto                     | Significado                                 | Holgura   | Gráficamente                                |
| :--------------------------- | :------------------------------------------ | :-------- | :------------------------------------------ |
| **Restricción Limitante**    | Uso = Disponibilidad. El recurso se agota.  | $S_i = 0$ | El punto óptimo **está sobre** esa recta    |
| **Restricción No Limitante** | Uso < Disponibilidad. Hay recurso sobrante. | $S_i > 0$ | El punto óptimo **NO está sobre** esa recta |

---

## 4. Clasificación de Soluciones ⚠️MEJORAR⚠️

> Toda clasificación se hace sobre el modelo en **Forma Estándar** (con las variables de holgura/excedente incluidas).

### Definiciones formales

Sean $n$ = total de variables (decisión + holgura/excedente) y $m$ = número de restricciones (no se incluye la de no negatividad) funcionales:

| Tipo de Solución                   | Definición                                                                                 | Ubicación gráfica                                                      |
| :--------------------------------- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Solución**                       | Verifica el sistema de ecuaciones (puede tener valores negativos)                          | Cualquier intersección de rectas                                       |
| **Solución Factible (SF)**         | Verifica el sistema de ecuaciones **Y** cumple no negatividad ($x_j \geq 0$ para todo $j$) | Cualquier punto dentro del poliedro o en sus lados                     |
| **Solución Factible Básica (SFB)** | SF con **como máximo $m$** variables positivas (o al menos $n-m$ variables nulas)          | Gráficamente, representan los vértices del [[Poliedro de Soluciones]]. |
| — SFB No Degenerada                | Tiene **exactamente $m$** variables positivas (exactamente $n-m$ nulas)                    | Vértice donde se cruzan exactamente $m$ rectas                         |
| — SFB Degenerada                   | Tiene **menos de $m$** variables positivas (más de $n-m$ nulas)                            | Vértice donde se cruzan **más de $m$** rectas                          |
| **Solución Factible No Básica**    | SF con **más de $m$** variables positivas                                                  | Interior del poliedro o sobre un lado (no en vértice)                  |
| **Solución Básica No Factible**    | Verifica las ecuaciones, tiene $\leq m$ positivas, pero tiene algún valor **negativo**     | Intersección de rectas **fuera** de la región factible                 |
|                                    |                                                                                            |                                                                        |
``` mermaid
graph TD
    A(Solución General) --> B(Solución Factible)
    A --> C(Solución No Factible)
    B --> D(Factible Básica / Vértices)
    B --> E(Factible No Básica / Lados e Interior)
    D --> F(No Degenerada)
    D --> G(Degenerada)
```


### Fórmula del número máximo de soluciones básicas

$$C_m^n = \frac{n!}{m!(n-m)!}$$

- Este número es una **cota superior** tanto para las soluciones básicas como para las soluciones factibles básicas (vértices)
- Las SFB son un **subconjunto** de las soluciones básicas

> **Ejemplo:** Con $n=5$ y $m=3$: $C_3^5 = \frac{5!}{3! \cdot 2!} = 10$ soluciones básicas como máximo

---

### Algoritmo para clasificar un punto (Protocolo de 3 pasos)

> [!important] Este es el protocolo que exige el profesor en los parciales:

```
Paso 1: ESTANDARIZAR → Agregar variables de holgura al modelo
Paso 2: VERIFICAR → Reemplazar los valores en CADA ecuación
         ¿Cumple todas las igualdades?
            NO → NO ES SOLUCIÓN (fin)
            SÍ → Continuar...
Paso 3: CLASIFICAR →
    a) ¿Tiene algún valor negativo?
        SÍ → SOLUCIÓN BÁSICA NO FACTIBLE (si tiene ≤ m positivas)
             o simplemente NO ES FACTIBLE
        NO → Es FACTIBLE. Continuar...
    b) ¿Cuántas variables son > 0?
        Más de m    → FACTIBLE NO BÁSICA
        Exactamente m → FACTIBLE BÁSICA NO DEGENERADA
        Menos de m  → FACTIBLE BÁSICA DEGENERADA
```

> [!danger] Error crítico: Saltarse la Forma Estándar
> Nunca evaluar puntos sobre las inecuaciones originales. Toda evaluación se hace sobre la **Forma Estándar** (con las igualdades).

> [!warning] No descartar un punto solo por tener negativos
> Un valor negativo significa que NO es factible, pero **SÍ puede ser solución** (básica no factible) si cumple algebraicamente el sistema de ecuaciones. Hay que verificar primero si cumple el sistema.

---

## 5. Conjunto Convexo y Combinación Lineal Convexa

### Combinación Lineal Convexa (CLC)

Dados $r$ vectores $V_1, V_2, \ldots, V_r$, una CLC es:
$$V = \alpha_1 V_1 + \alpha_2 V_2 + \ldots + \alpha_r V_r$$

Con las condiciones:
- $\alpha_i \geq 0$ para todo $i$
- $\sum_{i=1}^r \alpha_i = 1$

**Interpretación geométrica:** el resultado es un punto que pertenece al segmento de recta que une los puntos originales. 
Operación matemática fundamental para moverse dentro de la región válida.

### Conjunto Convexo

Un conjunto $S$ es **convexo** si el segmento que une cualquier par de puntos de $S$ está completamente contenido en $S$.

- La Región Factible de un PL **siempre es un conjunto convexo** (esto se demuestra con el Teorema 1)
- No puede ser cóncavo ni tener áreas separadas

Un conjunto de puntos $S$ donde, si tomas cualquier par de puntos dentro de él, el segmento de recta que los une se encuentra completamente dentro de $S$,. El [[Poliedro de Soluciones]] siempre es un conjunto convexo cerrado,.

### Punto Extremo

Un punto $P$ de un conjunto convexo $S$ es un **punto extremo** si, para cada segmento que se encuentra completamente en $S$ y pasa por $P$, $P$ es un extremo del segmento. Los puntos extremos son los **vértices** del poliedro.

---

## 6. Los 3 Teoremas Fundamentales de PL

| Teorema       | Postulado del Profesor                                                                               | Consecuencia Teórica Directa                                                                             |
| :------------ | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Teorema 1** | Toda [[Combinación Lineal Convexa]] de soluciones factibles da otra solución factible.               | Demuestra formalmente que la región factible es un **[[Conjunto Convexo]]**.                             |
| **Teorema 2** | Si dos soluciones factibles le dan el mismo valor a $Z$, su combinación convexa le dará igual valor. | Demuestra la existencia de infinitas soluciones óptimas apoyadas sobre una **[[Recta de Isoutilidad]]**. |
| **Teorema 3** | Si un problema es resoluble, siempre existirá al menos una **SFB** que sea óptima.                   | Es el **[[Teorema Fundamental de la Programación Lineal]]**, base algorítmica del [[Método Simplex]].    |

### Teorema 1: Convexidad del conjunto de soluciones factibles

> *"Toda combinación lineal convexa de soluciones factibles de un PL es otra solución factible de dicho PL."*

**Demostración (esquema):**
- Sean $X_1, X_2, \ldots, X_r$ soluciones factibles → cumplen $AX_i = B$ y $X_i \geq 0$
- Multiplicar cada ecuación por $\alpha_i$ (con $\alpha_i \geq 0$ y $\sum \alpha_i = 1$)
- Sumar miembro a miembro:
$$A\left(\sum_{i=1}^r \alpha_i X_i\right) = B\left(\sum_{i=1}^r \alpha_i\right) = B$$
- Por tanto $X_k = \sum \alpha_i X_i$ también cumple $AX_k = B$ → es solución factible ✓

**Corolario:** El conjunto de todas las soluciones factibles, si no es vacío, es un **conjunto convexo**. Es decir, está formado por un único elemento o por una infinidad.

---

### Teorema 2: Combinación convexa de soluciones con igual Z

> *"Si existe más de una solución factible que le den el mismo valor a Z, cualquier combinación lineal convexa de las mismas dará al funcional igual valor."*

**Demostración (esquema):**
- Sean $X_1, \ldots, X_r$ soluciones factibles con $CX_i = Z_0$ para todo $i$
- Multiplicar por $\alpha_i$ y sumar:
$$C\left(\sum \alpha_i X_i\right) = Z_0 \sum \alpha_i = Z_0$$
- El nuevo vector da el **mismo valor** $Z_0$ a la función objetivo ✓

**Consecuencia:** Esto explica el caso de **infinitas soluciones óptimas** (cuando $Z$ es paralela a una restricción limitante). Al tener dos vértices óptimos, toda CLC entre ellos da otro punto óptimo con el mismo $Z$.

**Corolario de los Teoremas 1 y 2:** El conjunto de soluciones factibles óptimas es un **conjunto convexo**, que si no es vacío, está formado por un elemento o por una infinidad.

---

### Teorema 3: Teorema Fundamental de la Programación Lineal

> *"Si un PL es resoluble (posee óptimo), existirá siempre por lo menos una solución factible básica que también sea óptima."*

**Importancia:** Este es el fundamento sobre el cual George Dantzig construyó el **Algoritmo Simplex**. Garantiza que el óptimo **siempre** estará en al menos un vértice, por lo que no es necesario explorar los infinitos puntos interiores del poliedro.

> [!important] Este teorema NO tiene demostración exigible en el curso, pero su enunciado sí se evalúa.

---

### Tabla resumen: Relación entre conjuntos factibles y óptimos

| Conjunto de Soluciones Factibles | Conjunto de Soluciones Óptimas |
|:--|:--|
| Vacío | Vacío (problema incompatible) |
| Un elemento | Un elemento (ese único punto es el óptimo) |
| Infinitos elementos | Un elemento (óptimo en un único vértice) |
| Infinitos elementos | Vacío (problema no acotado) |
| Infinitos elementos | Infinitos elementos (múltiples óptimos: Z paralela a restricción limitante) |

---

# PARTE II — RESOLUCIÓN PRÁCTICA PASO A PASO

---

## Ejemplo 1: Problema de MAXIMIZACIÓN (Problema 2.10)

### Enunciado
$$\max Z = 2x_1 + 3x_2$$
$$\text{s.a.}$$
$$4x_1 + 2x_2 \leq 20 \quad (R_1)$$
$$2x_1 + 4x_2 \leq 16 \quad (R_2)$$
$$x_1 + x_2 \leq 15 \quad (R_3)$$
$$x_1, x_2 \geq 0$$

### Paso 1: Estandarizar

- $n = 5$ variables ($x_1, x_2, S_1, S_2, S_3$)
- $m = 3$ restricciones

$$4x_1 + 2x_2 + S_1 = 20$$
$$2x_1 + 4x_2 + S_2 = 16$$
$$x_1 + x_2 + S_3 = 15$$

### Paso 2: Graficar restricciones

**R1:** $4x_1 + 2x_2 = 20$
- Si $x_1=0$ → $x_2=10$
- Si $x_2=0$ → $x_1=5$
- Punto de prueba $(0,0)$: $0 \leq 20$ ✓ → semiplano que contiene el origen

**R2:** $2x_1 + 4x_2 = 16$
- Si $x_1=0$ → $x_2=4$
- Si $x_2=0$ → $x_1=8$
- Punto de prueba $(0,0)$: $0 \leq 16$ ✓ → semiplano que contiene el origen

**R3:** $x_1 + x_2 = 15$
- Si $x_1=0$ → $x_2=15$
- Si $x_2=0$ → $x_1=15$
- Punto de prueba $(0,0)$: $0 \leq 15$ ✓ → semiplano que contiene el origen

La intersección de los tres semiplanos en el 1er cuadrante forma el poliedro de soluciones.

### Paso 3: Número máximo de soluciones básicas

$$C_3^5 = \frac{5!}{3! \cdot 2!} = 10$$

De esas 10 intersecciones, solo **4** caen dentro de la región factible (son las SFB = vértices del poliedro).

### Paso 4: Trazar Z y desplazar

Con $Z=12$: $x_2 = 4 - \frac{2}{3}x_1$ → dibujar esta recta

Desplazar paralelamente **alejándose del origen** (maximización).

El último punto de contacto con el poliedro es el **vértice óptimo**.

### Paso 5: Resolver el sistema en el vértice óptimo

Si el óptimo está en la intersección de $R_1$ y $R_2$:
$$4x_1 + 2x_2 = 20$$
$$2x_1 + 4x_2 = 16$$

Multiplicar la segunda por $(-2)$ y sumar:
$$4x_1 + 2x_2 = 20$$
$$-4x_1 - 8x_2 = -32$$
$$\overline{-6x_2 = -12}$$
$$x_2 = 2$$

Reemplazar: $4x_1 + 2(2) = 20$ → $x_1 = 4$

### Paso 6: Calcular holguras

- $S_1 = 20 - 4(4) - 2(2) = 20 - 20 = 0$ → **Restricción limitante**
- $S_2 = 16 - 2(4) - 4(2) = 16 - 16 = 0$ → **Restricción limitante**
- $S_3 = 15 - 4 - 2 = 9$ → **Restricción NO limitante**

### Paso 7: Valor de Z

$$Z = 2(4) + 3(2) = 8 + 6 = 14$$

**Vector solución:** $(x_1=4, \ x_2=2, \ S_1=0, \ S_2=0, \ S_3=9)$, $Z^* = 14$

**Clasificación:** Tiene exactamente $m=3$ variables positivas ($x_1, x_2, S_3$) → **SFB No Degenerada** ✓

---

## Ejemplo 2: Problema de MINIMIZACIÓN (Libro Cap 3)

### Enunciado
$$\min Z = 5x_1 + 7x_2$$
$$\text{s.a.}$$
$$10x_1 + 20x_2 \leq 300 \quad (R_1: \text{grasa})$$
$$4x_1 + 3x_2 \geq 40 \quad (R_2: \text{vitamina A})$$
$$x_1 \leq 8 \quad (R_3: \text{disponibilidad alim. I})$$
$$x_2 \geq 3 \quad (R_4: \text{mínimo alim. II})$$
$$x_1 + x_2 \geq 12 \quad (R_5: \text{necesidad total})$$
$$x_1, x_2 \geq 0$$

### Estandarización (mezcla de $\leq$ y $\geq$)

| Restricción | Tipo | Variable implícita | Ecuación estándar |
|:--|:--|:--|:--|
| $R_1$ | $\leq$ | $+S_1$ (holgura) | $10x_1 + 20x_2 + S_1 = 300$ |
| $R_2$ | $\geq$ | $-S_2$ (excedente) | $4x_1 + 3x_2 - S_2 = 40$ |
| $R_3$ | $\leq$ | $+S_3$ (holgura) | $x_1 + S_3 = 8$ |
| $R_4$ | $\geq$ | $-S_4$ (excedente) | $x_2 - S_4 = 3$ |
| $R_5$ | $\geq$ | $-S_5$ (excedente) | $x_1 + x_2 - S_5 = 12$ |

- $n = 7$ variables, $m = 5$ restricciones

### Sentido de optimidad

En **minimización**, el sentido de optimidad es **hacia el origen** (la ordenada al origen disminuye al disminuir $Z$).

### Resolución

El vértice óptimo se forma en la intersección de:
$$x_1 = 8 \quad \text{y} \quad x_1 + x_2 = 12$$

Resolviendo: $x_1 = 8$, $x_2 = 4$

### Solución completa

| Variable | Valor | Significado |
|:--|:--|:--|
| $x_1$ | 8 | Kg de alimento I |
| $x_2$ | 4 | Kg de alimento II |
| $S_1$ | 140 | Gramos de grasa no utilizados |
| $S_2$ | 4 | Unidades de vitamina A por encima del mínimo |
| $S_3$ | 0 | Restricción limitante (se usa todo el alim. I disponible) |
| $S_4$ | 1 | Kg de alim. II por encima del mínimo |
| $S_5$ | 0 | Restricción limitante (se produce exactamente el mínimo necesario) |
| $Z^*$ | $68 | Costo mínimo de la mezcla |

---

## Ejemplo 3: Clasificación de Soluciones (Ejercicio tipo parcial)

### Modelo dado

$$\max Z = 100x_1 + 120x_2$$
$$10x_1 + 15x_2 \leq 1000 \quad (R_1)$$
$$30x_1 + 20x_2 \leq 1950 \quad (R_2)$$
$$x_1 \leq 65 \quad (R_3)$$
$$x_2 \leq 50 \quad (R_4)$$
$$x_1 \geq 20 \quad (R_5)$$

**Forma estándar:** $n = 7$, $m = 5$

### Clasificación punto por punto

**Punto 1:** $x_1=20, \ x_2=50, \ S_1=50, \ S_2=350, \ S_3=45, \ S_4=0, \ S_5=0$
1. ¿Cumple ecuaciones? → SÍ ✓
2. ¿Algún negativo? → NO ✓
3. Variables positivas: 5 ($x_1, x_2, S_1, S_2, S_3$). Variables nulas: 2 ($S_4, S_5$)
4. Como tiene exactamente $m=5$ positivas → **SFB No Degenerada** ✓

**Punto 2:** $x_1=20, \ x_2=67.5, \ S_1=-212.5, \ S_2=0, \ S_3=45, \ S_4=-17.5, \ S_5=0$
1. ¿Cumple ecuaciones? → SÍ ✓
2. ¿Algún negativo? → SÍ ($S_1$ y $S_4$ son negativos)
3. Tiene $n-m = 2$ ceros → es básica
4. → **Solución Básica No Factible**

**Punto 3:** $x_1=40, \ x_2=18, \ S_1=330, \ S_2=390, \ S_3=25, \ S_4=32, \ S_5=20$
1. ¿Cumple ecuaciones? → SÍ ✓
2. ¿Algún negativo? → NO ✓
3. Variables positivas: **7** (todas). Como $7 > m = 5$ → **Solución Factible No Básica** (punto en el interior del poliedro)

**Punto 4:** $x_1=70, \ x_2=60, \ S_1=100, \ S_2=-1350, \ S_3=-5, \ S_4=-10, \ S_5=90$
1. ¿Cumple ecuaciones? → **NO** ❌ (Ej: $10(70)+15(60)+100 = 1700 \neq 1000$)
2. → **NO ES SOLUCIÓN**

> [!danger] Trampa: No apresurarse a clasificar como "no factible" por ver negativos. Primero verificar si cumple las ecuaciones. Si ni siquiera las cumple, **no es solución** de ningún tipo.

**Punto 5:** $x_1=65, \ x_2=0, \ S_1=350, \ S_2=0, \ S_3=0, \ S_4=50, \ S_5=45$
1. ¿Cumple ecuaciones? → SÍ ✓
2. ¿Algún negativo? → NO ✓
3. Variables positivas: **4** ($x_1, S_1, S_4, S_5$). Variables nulas: **3** ($x_2, S_2, S_3$)
4. Tiene **menos de $m=5$** positivas → **SFB Degenerada**

**Punto 6:** $x_1=26, \ x_2=45, \ S_1=65, \ S_2=270, \ S_3=39, \ S_4=5, \ S_5=6$
1. ¿Cumple ecuaciones? → SÍ ✓
2. ¿Algún negativo? → NO ✓
3. Variables positivas: **7** (todas) → **Solución Factible No Básica**

---

## Ejemplo 4: Aplicación del Teorema 1 (Combinación Lineal Convexa)

### Datos
- **Vector 1:** $(x_1=20, x_2=50, S_1=50, S_2=350, S_3=45, S_4=0, S_5=0)$ con $Z=8000$
- **Vector 2:** $(x_1=40, x_2=18, S_1=330, S_2=390, S_3=25, S_4=32, S_5=20)$ con $Z=6160$
- $\alpha = 0.50$ → entonces $\alpha_1 = 0.50$, $\alpha_2 = 1 - 0.50 = 0.50$

### Cálculo

$$V_{nuevo} = 0.50 \cdot V_1 + 0.50 \cdot V_2$$

| Variable | $0.50 \times V_1$ | $0.50 \times V_2$ | **Resultado** |
|:--|:--|:--|:--|
| $x_1$ | $0.50 \times 20 = 10$ | $0.50 \times 40 = 20$ | **30** |
| $x_2$ | $0.50 \times 50 = 25$ | $0.50 \times 18 = 9$ | **34** |
| $S_1$ | $0.50 \times 50 = 25$ | $0.50 \times 330 = 165$ | **190** |
| $S_2$ | $0.50 \times 350 = 175$ | $0.50 \times 390 = 195$ | **370** |
| $S_3$ | $0.50 \times 45 = 22.5$ | $0.50 \times 25 = 12.5$ | **35** |
| $S_4$ | $0.50 \times 0 = 0$ | $0.50 \times 32 = 16$ | **16** |
| $S_5$ | $0.50 \times 0 = 0$ | $0.50 \times 20 = 10$ | **10** |

**Resultado:** $(30, 34, 190, 370, 35, 16, 10)$ → todas positivas, 7 variables $> 0$ → **SF No Básica** (punto interior del poliedro)

Por el **Teorema 1**, este nuevo punto es **solución factible** del PL. ✓

---

## Ejemplo 5: Aplicación del Teorema 2 (Encontrar solución con mismo Z)

### Objetivo
Encontrar otra solución con $Z = 8000$ usando $\alpha = 0.50$

### Paso clave
Seleccionar **solo los dos vectores** que tengan $Z = 8000$:
- **Vector A:** $(20, 50, 50, 350, 45, 0, 0)$ → $Z = 8000$ ✓
- **Vector B:** $(26, 45, 65, 270, 39, 5, 6)$ → $Z = 8000$ ✓

### Cálculo

| Variable | Resultado |
|:--|:--|
| $x_1$ | $(0.50 \times 20) + (0.50 \times 26) = \mathbf{23}$ |
| $x_2$ | $(0.50 \times 50) + (0.50 \times 45) = \mathbf{47.5}$ |
| $S_1$ | $(0.50 \times 50) + (0.50 \times 65) = \mathbf{57.5}$ |
| $S_2$ | $(0.50 \times 350) + (0.50 \times 270) = \mathbf{310}$ |
| $S_3$ | $(0.50 \times 45) + (0.50 \times 39) = \mathbf{42}$ |
| $S_4$ | $(0.50 \times 0) + (0.50 \times 5) = \mathbf{2.5}$ |
| $S_5$ | $(0.50 \times 0) + (0.50 \times 6) = \mathbf{3}$ |

**Verificación:** $Z = 100(23) + 120(47.5) = 2300 + 5700 = \mathbf{8000}$ ✓

Por el **Teorema 2**, como ambos vectores daban $Z=8000$, la CLC da otra solución con **exactamente el mismo valor de Z**. ✓

> [!tip] Para aplicar el Teorema 2, solo se necesitan **dos puntos** que den el mismo valor a Z. Aunque haya 3 o más, se toman de a dos.

---

# PARTE III — ERRORES FRECUENTES DE PARCIAL (COMPILACIÓN)

---

| #   | Error                                                                         | Corrección                                                                                                          |
| :-- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| 1   | Definir el óptimo como "el punto más alejado del origen"                      | Es el **último punto de contacto** entre Z y el poliedro al desplazarla                                             |
| 2   |                                                                               |                                                                                                                     |
| 3   | Clasificar soluciones sobre el modelo original (inecuaciones)                 | Siempre evaluar sobre la **Forma Estándar** (igualdades con holguras)                                               |
| 4   | Asumir que "$\geq$ va para arriba" al graficar                                | Siempre usar un **punto de prueba** para verificar el semiplano                                                     |
| 5   | Creer que la variable de excedente es negativa                                | La variable siempre es $\geq 0$; el signo menos es una **operación algebraica**                                     |
| 6   | Declarar valores negativos para variables                                     | Viola la no negatividad → **anula el examen**                                                                       |
| 7   | Descartar un punto como "no solución" solo por tener negativos                | Primero verificar si cumple las ecuaciones; puede ser **solución básica no factible**                               |
| 8   | Clasificar un punto sin verificar las ecuaciones                              | Un punto puede **no cumplir** el sistema → no es solución de ningún tipo                                            |
| 9   | Confundir "soluciones factibles infinitas" con "soluciones básicas infinitas" | Las SF pueden ser infinitas, pero las SB siempre son **finitas** ($C_m^n$)                                          |
| 10  | Dibujar mal la pendiente de Z                                                 | El **óptimo depende** de la inclinación de Z; verificar siempre la pendiente                                        |
| 11  | Creer que $C_m^n$ da la cantidad exacta de soluciones factibles               | Da el nº máximo de **soluciones básicas** (cota superior). No todas caen dentro del poliedro                        |
| 12  | Graficar $x_1$ en el eje vertical                                             | **Convención obligatoria de la cátedra:** $x_1$ en el eje horizontal, $x_2$ en el vertical                          |
| 13  | Usar un valor arbitrario de Z inadecuado para la escala                       | Si los ejes van de 10 a 100, no usar $Z=1$. Elegir múltiplos de los coeficientes que caigan dentro de la cuadrícula |

---

# 💡PARTE IV — TIPS PRÁCTICOS "DE TRINCHERA"

---

### Tip 1: Escala inteligente para el valor arbitrario de Z
Al asignar un valor a $Z$ para trazar su pendiente, fijarse en la escala de los ejes. Si tu gráfico va de 10 a 100, **no uses $Z=1$** porque la recta será indibujable. Elegir valores que sean múltiplos de los coeficientes de Z (ej: si $Z = 10x_1 + 10x_2$, probar con $Z=100$).

### Tip 2: Verificación cruzada con el combinatorio
Si la fórmula $C_m^n$ te da 10 soluciones básicas como máximo, y en tu gráfico estás marcando 12 intersecciones, entonces **estás interceptando rectas que no corresponden al modelo**. Usalo como check de sensatez.

### Tip 3: Atajo con restricciones limitantes
Si identificás visualmente que el vértice óptimo se apoya sobre una recta de restricción, ya sabés de antemano que **la holgura de esa restricción es $0$** sin necesidad de calcular. Es un excelente atajo para verificar que tus cálculos posteriores son lógicos.

### Tip 4: ¿Por qué las holguras entran con coeficiente 0 en Z?
Las variables de holgura representan **recursos no utilizados** (capacidad ociosa de horas, máquinas, materia prima). Como esa capacidad ociosa no se vende ni se procesa, **no aporta ganancia ni costo** a la utilidad económica. Por eso entran como $+0S_1 + 0S_2 + \ldots$

### Tip 5: Variables implícitas = Variables de holgura/excedente
Son **exactamente lo mismo**. En el modelo original con inecuaciones, la diferencia entre lo usado y lo disponible está "implícita". Al estandarizar, esa diferencia se hace explícita y toma el nombre técnico de variable de holgura o excedente. Hay **una por cada restricción funcional**.

---

# PARTE V — JUSTIFICACIONES MODELO PARA PARCIAL

---

Estas son plantillas de razonamiento para preguntas tipo *"Justifique su respuesta"*:

### "¿Por qué el Método Simplex solo evalúa vértices y no puntos interiores?"

> Esto se justifica por el **Teorema 3** (Teorema Fundamental de la PL). Este teorema demuestra que, si un problema tiene óptimo, este siempre se encontrará en al menos una Solución Factible Básica (que gráficamente es un vértice). Por lo tanto, el algoritmo Simplex es eficiente porque descarta los infinitos puntos interiores y salta exclusivamente entre el número finito de vértices dado por la fórmula combinatoria $C_m^n$.

### "¿Qué ocurre si la Función Objetivo es paralela a una restricción limitante?"

> Según el **Teorema 2**, si dos soluciones en los extremos de esa restricción le otorgan a $Z$ el mismo valor óptimo, cualquier CLC entre ellas dará otra solución factible con ese mismo $Z$. Como existen infinitos puntos en el segmento que los une (recta de isoutilidad), el problema posee **infinitas soluciones óptimas**.

### "¿Por qué las variables de holgura ingresan a Z con coeficiente cero?"

> Las variables de holgura representan "recursos no utilizados" (capacidad ociosa). Al no venderse ni procesarse, no aportan ninguna ganancia ni costo a la utilidad real económica ($Z$). Por eso se ponderan con coeficiente $0$.

### "Un punto tiene un valor negativo, ¿se descarta directamente?"

> **No necesariamente.** Un valor negativo descarta que sea "Factible" (viola la no negatividad), pero **SÍ puede ser una Solución Básica No Factible** si cumple algebraicamente el sistema de ecuaciones. El protocolo es: primero verificar si cumple las ecuaciones, y recién después clasificar por signos.

### "¿El poliedro de soluciones puede ser cóncavo o tener áreas separadas?"

> **Falso absoluto.** La región factible siempre es un **Conjunto Convexo** cerrado (demostrado por el Teorema 1). Si se toman dos puntos cualesquiera dentro del poliedro, la recta que los une está completamente contenida en él. Si las restricciones no generan una intersección común, el problema simplemente **no tiene solución** (es incompatible).

---

# PARTE VI — CHEAT SHEET DE FÓRMULAS

---

| Concepto | Fórmula |
|:--|:--|
| Pendiente de Z | $-\frac{c_1}{c_2}$ |
| Forma explícita de Z | $x_2 = \frac{Z}{c_2} - \frac{c_1}{c_2} x_1$ |
| Nº máx. de soluciones básicas | $C_m^n = \frac{n!}{m!(n-m)!}$ |
| CLC de 2 vectores | $V_{nuevo} = \alpha_1 V_1 + \alpha_2 V_2$ con $\alpha_1 + \alpha_2 = 1$ y $\alpha_i \geq 0$ |
| Holgura: restricción $\leq$ | $\text{lado izq.} + S_i = \text{lado der.}$ |
| Excedente: restricción $\geq$ | $\text{lado izq.} - S_i = \text{lado der.}$ |
| Convención de ejes | $x_1$ = eje horizontal, $x_2$ = eje vertical |
| Definición de $n$ | Total de variables (decisión + holguras + excedentes) |
| Definición de $m$ | Total de restricciones funcionales (**sin** contar no negatividad) |

---

> *Resumen creado por Claude a partir de: Cap3 (Método Gráfico, Conceptos, Teoremas), Clases C04 y C06, Práctico C05, ejercicios 2.10, 2.31, cuestionarios UV, y resúmenes de NotebookLM (análisis teórico y práctico U02-R02).*
