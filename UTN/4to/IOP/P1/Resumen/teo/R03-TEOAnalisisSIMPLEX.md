Como tu Tutor Académico de Élite, he analizado exhaustivamente las transcripciones de las clases teóricas proporcionadas. Me he enfocado en destilar la lógica subyacente, el vocabulario técnico innegociable y las sutilezas conceptuales que el profesor evalúa rigurosamente.

A continuación, te presento tu **Mapa de Dominio Conceptual**, diseñado para asegurar la máxima calificación en preguntas teóricas y justificaciones.

---

# 1. 🎯 RADAR CONCEPTUAL (Alta Prioridad)

El profesor construye toda su evaluación sobre una base teórica estricta. Si no dominas la definición exacta de estos conceptos y su función dentro del [[Método Simplex]], perderás puntos críticos.

- **Conceptos Core:**
    
    - **[[Teorema Fundamental de la PL]]:** Es el motor del método. Establece que si un problema tiene solución óptima, esta siempre existirá en al menos un punto extremo o vértice del [[Poliedro de Soluciones]],.
    - **[[Solución Factible Básica]]:** Corresponde algebraicamente a un vértice. Es aquella donde como máximo $m$ variables (igual a la cantidad de restricciones) son positivas, y el resto ($n-m$) son estrictamente nulas,.
    - **[[Tasa de Crecimiento]] ($C_j - Z_j$):** Es el incremento o disminución _neto_ de la función objetivo al introducir una unidad de la variable no básica. Considera el beneficio aportado menos el costo ($Z_j$) de reestructurar la base,.
    - **[[Tasas de Sustitución]] ($\lambda_{ij}$):** Indican el sacrificio o incremento que debe sufrir una variable básica actual para ceder los recursos necesarios y producir exactamente _una unidad_ de una variable no básica,.
- **Palabras Clave Obligatorias (Vocabulario de Examen):**
    
    - Al hablar de [[Variables de Holgura]], el profesor **exige** usar el término **"recurso sin utilizar"**,. Usar "disponible" o "usado" es considerado un error de concepto.
    - Se requiere hablar de **"incremento neto"** para $C_j - Z_j$ y **"costo del cambio de plan"** para $Z_j$,.
    - La matriz inicial válida siempre debe llamarse **[[Matriz Identidad]]** conformada por un **[[Vector Unitario]]** para cada restricción,.

---

# 2. ⚖️ CUADROS DE BATALLA (Comparaciones y Clasificaciones)

El profesor exige que sepas diagnosticar matemáticamente el estado del modelo observando la matriz.

### Clasificación de Puntos y Soluciones

|Tipo de Solución|Condición Algebraica (Siendo $m$ = restricciones)|Ubicación en el Gráfico|
|:--|:--|:--|
|**[[Solución Factible Básica]]**|Exactamente $m$ variables positivas y $n-m$ nulas.|Vértice exacto del poliedro.|
|**[[Solución Degenerada]]**|Menos de $m$ variables positivas (hay ceros dentro de la base),.|Vértice sobredefinido (se cruzan $>2$ rectas).|
|**[[Solución Factible No Básica]]**|Más de $m$ variables positivas.|Punto interior o sobre una arista (no es vértice).|

### El Doble Comportamiento de las [[Tasas de Sustitución]]

> [!danger] ZONA DE PELIGRO: La Inversión del Signo El profesor fue categórico al diferenciar el análisis de la tabla normal respecto al análisis de sensibilidad cuando se _agregan_ recursos extras.

|Valor de $\lambda_{ij}$|Interpretación Normal (Tabla Estándar)|Interpretación Inversa (Si se _agregan_ recursos extras)|
|:--|:--|:--|
|**Positivo ($>0$)**|**Sacrificio:** Disminuye el valor de la variable básica,.|**Incremento:** Aumenta el valor de la variable básica,.|
|**Negativo ($<0$)**|**Incremento:** Aumenta el valor de la variable básica,.|**Sacrificio:** Disminuye el valor de la variable básica,.|

---

# 3. ⚠️ TRAMPAS DE OPCIÓN MÚLTIPLE / V o F

Durante la revisión de los cuestionarios teóricos, el profesor expuso las "trampas" clásicas donde la intuición engaña a la teoría:

> [!question] Falso Amigo 1: ¿Poliedro abierto es igual a Problema No Acotado? **Falso.** Un poliedro abierto _no_ implica necesariamente que sea un [[Problema No Acotado]]. El profesor demostró que la falta de cota depende estrictamente de la dirección de la función $Z$. Un poliedro abierto puede ser no acotado para un problema de maximización, pero poseer un óptimo perfecto y acotado si el problema fuera de minimización,.

> [!question] Falso Amigo 2: El Diagnóstico de las Múltiples Soluciones **Falso.** La regla dice que si en la tabla óptima un $C_j - Z_j = 0$ para una variable no básica, hay múltiples óptimos. ¡Cuidado! El profesor añadió una cláusula obligatoria: **"siempre y cuando la solución no sea degenerada"**,. Si la solución es degenerada, ese cero solo es un reflejo de la anomalía, y el problema tiene un único óptimo degenerado.

> [!question] Falso Amigo 3: El Conjunto de Soluciones Óptimas Vacío En un test de opción múltiple, el profesor evaluó esta abstracción. Si el conjunto de [[Soluciones Óptimas]] es vacío (no hay óptimo), esto ocurre exclusivamente por dos caminos divergentes: o bien el conjunto de [[Soluciones Factibles]] también es vacío (el problema es incompatible), o bien el conjunto de soluciones factibles tiene infinitos elementos y no tiene cota (problema no acotado),,.

---

# 4. 🗣️ CÓMO JUSTIFICAR (El "Por qué")

Si el examen pide "Justifique su respuesta", debes estructurarla utilizando la lógica causal estricta dictada por el profesor.

- **¿Por qué utilizamos [[Variables Artificiales]] y las castigamos con "M"?**
    - **Justificación:** Porque para arrancar el [[Método Simplex]] (Fase 1) es matemáticamente obligatorio poseer una [[Matriz Identidad]]. Si las restricciones originales no aportan los vectores unitarios (ej. por ser inecuaciones de $\geq$ o igualdades), se debe aplicar la [[Técnica de la Base Artificial]] para inventarlos. Como estas variables no pertenecen al modelo real, se las penaliza con un coeficiente gigantesco ($-M$ en máximo, $+M$ en mínimo) para forzar al algoritmo iterativo a expulsarlas de la base rápidamente y recuperar la factibilidad real,,.
- **¿Por qué un empate en el [[Cociente Tita]] ($\theta$) genera una [[Solución Degenerada]]?**
    - **Justificación:** El cociente $\theta$ dictamina qué variable agota primero su disponibilidad y debe anularse (salir de la base). Si hay un empate, significa que _dos_ variables agotan sus recursos simultáneamente,. Al sacar una de la base, la otra permanecerá en la base pero asumirá el valor $0$, rompiendo la regla de $m$ variables estrictamente positivas, dejando al vértice algebraicamente sobredefinido (más restricciones cruzándose que el mínimo necesario),.
- **¿Por qué JAMÁS se debe calcular el cociente de salida sobre denominadores $\leq 0$?**
    - **Justificación:** Matemáticamente, la división por cero no está definida. Dividir sobre una [[Tasa de Sustitución]] negativa significaría que, en la próxima iteración, esa variable de la base asumiría un valor negativo. Esto violaría el dogma más básico del modelo matemático: la [[Restricción de No Negatividad]], posicionando al algoritmo en un punto fuera del poliedro de soluciones,,.

> [!note] Cota Numérica de Vértices Para justificar que el Simplex finalizará en un número finito de pasos, el profesor exige apoyarse en la fórmula combinatoria que limita las soluciones básicas posibles: $$ C_m^n = \frac{n!}{m!(n-m)!} $$ Donde $n$ son todas las variables del sistema estandarizado y $m$ son las restricciones,.

### 📊 DIAGRAMA CONCEPTUAL: El Árbol de Diagnóstico de Casos Especiales

Para justificar diagnósticos visuales o matriciales, memoriza esta taxonomía de validación que el profesor usa en sus correcciones:

```
mindmap
  root((Diagnostico Simplex))
    Optimo Alcanzado
      Artificial Positiva en Base
        ::icon(fa fa-ban)
        PROBLEMA INCOMPATIBLE
      Cj_Zj Cero en No Basica
        Solucion Normal
          MULTIPLES SOLUCIONES
        Solucion con Ceros
          UNICO OPTIMO DEGENERADO
    Iterando
      Empate en Cociente Tita
        PROXIMA SOLUCION DEGENERADA
      Denominadores Tita Negativos o Cero
        ::icon(fa fa-infinity)
        PROBLEMA NO ACOTADO
```

_Conceptos relacionados:_ [[Problema Incompatible]], [[Problema No Acotado]], [[Solución Degenerada]], [[Múltiples Soluciones Óptimas]], [[Cociente Tita]].