¡Hola! Como tu Tutor Académico de Élite, he diseñado esta guía procedimental y táctica basada estrictamente en la metodología que la cátedra exige para la parte práctica. En la [[Programación Lineal]], el profesor fue tajante: _"si el planteo está mal, todo lo otro va a estar mal"_.

A continuación, te presento el algoritmo de resolución, las fórmulas y las "trampas" que debes evitar para asegurar tu aprobación.

---

# 🛠 Algoritmo de Modelización: Planteo Paso a Paso

Para formular un [[Modelo Matemático]] a partir de un problema verbal, **nunca debes saltar directamente a escribir ecuaciones**. Debes seguir este flujo de trabajo obligatorio:

```
graph TD
    A[1. Leer y comprender el problema] --> B[2. Traduccion Verbal de Objetivo y Limites]
    B --> C[3. Definicion Estricta de Variables]
    C --> D[4. Formulacion de la Funcion Objetivo]
    D --> E[5. Planteo de Restricciones Estructurales]
    E --> F[6. Cierre: Condicion de No Negatividad]
```


_Conceptos relacionados:_ [[Variables de Decisión]], [[Función Objetivo]], [[Restricciones Estructurales]], [[Condición de No Negatividad]].

### Paso 1: Traducción Verbal

Lee el problema e identifica escribiendo con palabras cuál es la meta del decisor (maximizar ingresos, minimizar costos) y cuáles son las limitaciones físicas, de mercado o de políticas.

### Paso 2: Definición de las [[Variables de Decisión]] ($x_j$)

Son las incógnitas del problema. Toda variable en un examen debe tener una anatomía de tres partes obligatorias:

1. **Unidad de medida:** (Litros, Pesos, Unidades).
2. **Ítem / Acción:** (del producto 1 a fabricar, a invertir en acción A).
3. **Período de tiempo:** (semanalmente, por mes). _Nota: Si es una inversión única de capital, puede no tener período_.

> [!danger] TRAMPA FATAL: El uso de la palabra "Cantidad" Un error que te anulará el planteo es definir la variable como "Cantidad de sillas" o "Cantidad de dinero". El profesor remarcó: _"Cantidad no es una unidad a la cual está medida"_. Usa siempre la métrica exacta (Unidades de sillas a producir, Pesos a invertir).

### Paso 3: Formulación de la [[Función Objetivo]] ($Z$)

Identifica los parámetros económicos (precios, costos, rendimientos) y multiplícalos por tus variables.

> [!note] Fórmula de la Función Objetivo General Para un problema de $n$ variables, la función toma la forma explícita: $$Max Z = c_1 x_1 + c_2 x_2 + \dots + c_n x_n$$ _(Donde $c_j$ son los coeficientes de utilidad o costo)_.

> [!tip] Tip de Parcial: ¿Cuándo Maximizar o Minimizar? Si el problema te da datos de "Precios de Venta" y "Costos", tu objetivo es **Maximizar el Beneficio o Contribución**. Si el problema solo te da "Costos operativos", tu objetivo es **Minimizar Costos**.

### Paso 4: Planteo de las [[Restricciones Estructurales]]

Traduce las limitaciones verbales a inecuaciones matemáticas.

**Diccionario Táctico de Traducción:**

|Frase en el Enunciado del Examen|Símbolo Matemático|Ejemplo de Uso|
|:--|:--|:--|
|_"Como máximo", "No más de", "Hasta", "Dispone de"_|$\le$|Limitación de horas de máquina.|
|_"Como mínimo", "Al menos", "Por lo menos"_|$\ge$|Satisfacer un contrato o demanda.|
|_"Exactamente", "Tiene que ser igual a"_|$=$|Equilibrio de stock o transporte.|

> [!tip] Regla de Estandarización para Resolver Al momento de formular, el profesor exige que dejes el modelo ordenado: _"del lado derecho tienen que estar todo lo que sea constante y del lado izquierdo todo lo que sea variable"_. Por ejemplo, la proporción $x_1 \ge x_2$ debe escribirse en el modelo definitivo como $x_1 - x_2 \ge 0$.

> [!danger] TRAMPA DE EXAMEN: El [[Análisis Dimensional]] Si te asusta ver "Pesos" y "Unidades de Casa" en una misma restricción, recuerda tachar unidades. Al multiplicar un costo ($Pesos/Casa$) por tu variable ($Casas$), las "casas" se simplifican y el resultado te da en "Pesos", coincidiendo perfectamente con tu límite de presupuesto (Lado Derecho).

### Paso 5: [[Condición de No Negatividad]]

Jamás entregues un modelo sin su cierre matemático. Esto asegura que el problema se desarrolle en el primer cuadrante.

> [!note] Fórmula Obligatoria de Cierre $$x_i \ge 0 \quad \forall i$$

> [!danger] ERROR COMÚN: Positividad vs. No Negatividad En los cuestionarios de múltiple choice, es común que aparezca la opción "las variables deben ser positivas". **No la marques.** El profesor advirtió que _"la no negatividad quiere decir mayor o igual a 0, no quiere decir positivo... el 0 no es positivo ni negativo"_. Exigir positividad estricta ($>0$) anularía la posibilidad de decidir no fabricar un producto.

---

# ⚠️ CONSIDERACIONES TÉCNICAS AVANZADAS

Cuando te enfrentes a problemas más complejos, debes aplicar estas tres reglas de ajuste en tus inecuaciones:

1. **Falta de Precio Unitario:** Si el problema exige invertir dinero pero no te da el precio de la acción, no puedes definir la variable como "acciones a comprar". Debes definirla en moneda: _"Pesos invertidos en la acción tipo A"_.
2. **Problemas con [[Mermas]]:** Si un proceso pierde material (Ej: se pierde el $35%$ de agua al destilar), tu coeficiente de salida no es $1$. Debes multiplicar tu variable por lo que _queda_: en este caso, por $0.65$ ($1 - 0.35$) para reflejar el volumen real.
3. **[[Velocidad de Procesamiento]]:** Si la máquina procesa $60~L/hora$, pero tu límite de tiempo está en **Horas**, debes invertir la tasa para mantener la coherencia dimensional. El coeficiente técnico será $1/60$ horas por litro.

---

# 📊 FORMAS Y CLASIFICACIÓN DEL MODELO

Finalmente, es un requisito de examen teórico saber clasificar el modelo resultante según los signos de sus restricciones:

|Clasificación del Modelo|Condición en un Problema de Maximización|Condición en un Problema de Minimización|
|:--|:--|:--|
|**[[Forma Canónica]]**|Todas las restricciones son de $\le$.|Todas las restricciones son de $\ge$.|
|**[[Forma Estándar]]**|Todas las restricciones son de igualdad ($=$).|Todas las restricciones son de igualdad ($=$).|
|**[[Forma Mixta]]**|Contiene sentidos mezclados ($\le, \ge, =$).|Contiene sentidos mezclados ($\le, \ge, =$).|

> [!tip] Metodología: Transformación a Forma Estándar Para convertir restricciones de desigualdad ($\le$) en igualdades ($=$), debes sumar [[Variables de Holgura]] ($S_i$), las cuales representan recursos o disponibilidades no utilizadas y entran a la Función Objetivo con coeficiente nulo ($0$).