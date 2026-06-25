Como tu Tutor Académico de Élite, he aplicado ingeniería inversa a las resoluciones prácticas, correcciones en vivo y advertencias del profesor para destilar exactamente qué evalúa y cómo lo evalúa. No perderemos tiempo en la historia del algoritmo; iremos directo a la mecánica de supervivencia para tu parcial de [[Programación Lineal]].

Aquí tienes la Guía Definitiva de Preparación, estructurada bajo estándares tácticos.

# 🚨 RADAR DE PARCIAL (Alta Prioridad)

El profesor dejó "marcadores de importancia" muy claros durante las clases prácticas. Estos son los temas fijos y los criterios de corrección inflexibles que definirán tu nota:

- **El Ejercicio Trampa: Completar la [[Tabla Simplex]] Incompleta:** El profesor advirtió explícitamente que en los exámenes suelen dar tablas con celdas en blanco (por ejemplo, omitiendo un $\lambda_{ij}$ en el centro). No esperan que iteres desde cero, sino que uses álgebra inversa para encontrar ese valor.
- **Criterio Innegociable: El Informe Económico Completo:** Entregar el vector matemático ($X_1=2, X_2=30$) es insuficiente. El profesor exige que el resultado se redacte detallando todas las variables,.
    
    > [!danger] ERROR LETAL DE REDACCIÓN _"Tomen nota porque es muy importante que no me escriban en una evaluación solo los valores de las variables, que las escriban a todas las variables en forma completa en el informe"_. Debes mencionar también a las [[Variables No Básicas]] (las que valen $0$) indicando obligatoriamente que _"se utilizan todos los recursos disponibles"_.
    
- **Penalización por Exceso de Variables:** Agregar una [[Variable Artificial]] en una restricción que ya tiene un [[Vector Unitario]] natural es considerado un error conceptual grave que demuestra que no sabes analizar la [[Matriz de Coeficientes]].

---

# 🛠 METODOLOGÍA DE RESOLUCIÓN (Paso a Paso)

El profesor exige un algoritmo procedimental estricto. Si dominas esta secuencia, el [[Método Simplex]] se vuelve mecánico.

### Algoritmo de Solución Táctico

1. **Estandarización del Modelo:**
    - Convierte las inecuaciones sumando o restando [[Variables de Holgura]]. (Si es $\leq$, suma; si es $\geq$, resta; si es $=$, no agregues holgura),.
    - Revisa el vector de términos independientes ($P_0$): si hay un negativo, multiplica toda la fila por $-1$ e invierte el signo de la inecuación.
2. **Búsqueda de la [[Matriz Identidad]] Inicial:**
    - Identifica $m$ vectores unitarios (uno para cada fila). Las variables que los posean formarán la base inicial.
    - Si faltan vectores (común en $\geq$ y $=$), inventa [[Variables Artificiales]] y súmalas a la restricción.
3. **Evaluación de Optimidad:**
    - Calcula $Z_j$ y la fila de control $C_j - Z_j$.
    - **Regla de Parada:** En Maximización, el óptimo se alcanza cuando todos los $C_j - Z_j \leq 0$,. En Minimización, cuando todos son $\geq 0$,.
4. **Selección de la [[Variable que Entra]]:**
    - _Máximo:_ Elige el valor positivo mayor en $C_j - Z_j$,.
    - _Mínimo:_ Elige el valor negativo mayor en valor absoluto ("el más negativo"),.
5. **Selección de la [[Variable que Sale]] (Cálculo del Pivot):**
    - Divide la columna solución ($P_0$) por la columna de la variable entrante.
    - Selecciona estrictamente el menor resultado positivo.
6. **Iteración mediante [[Operaciones Elementales de Fila]]:**
    - Aplica [[Gauss-Jordan]]: Divide la fila saliente por el elemento pivot para hacerlo $1$. Multiplica esa nueva fila por el opuesto de los valores que quieres anular en el resto de la columna y súmalos,,.

### Herramientas y Fórmulas Exigidas

> [!note] Fórmula de Despeje Algebraico (Para tablas incompletas) Si falta un valor en la tabla, usa la ecuación del $Z_j$ para despejar la incógnita de las [[Tasas de Sustitución]]: $$ Z_j = \sum (C_{b_i} \times \lambda_{ij}) $$ El profesor indicó que basta con plantear esta ecuación lineal y despejar el valor faltante.

> [!note] Fórmula del Cociente de Salida (Tita) $$ \theta = \min \left( \frac{P_{0_i}}{\lambda_{ij}} \right) \quad \forall \lambda_{ij} > 0 $$

```
graph TD
    A(Inicio: Estandarizar Modelo) --> B{¿Hay Matriz Identidad m x m?}
    B -->|Sí| D(Armar Tabla Inicial)
    B -->|No| C(Agregar Variables Artificiales y penalizar con M)
    C --> D
    D --> E(Calcular Z_j y C_j - Z_j)
    E --> F{¿Se cumple el criterio de óptimo?}
    F -->|Sí| G(FIN: Redactar Informe Económico)
    F -->|No| H(Determinar Variable que Entra)
    H --> I(Calcular Cocientes Tita válidos)
    I --> J(Determinar Variable que Sale - Menor Tita)
    J --> K(Aplicar Gauss-Jordan)
    K --> E
```

_Conceptos Relacionados:_ [[Variables Básicas]], [[Variables No Básicas]], [[Solución Factible Básica]], [[Matriz Identidad]].

---

# ⚠️ ZONA DE PELIGRO (Errores Comunes)

Identifiqué las "trampas de parcial" donde cayeron tus compañeros y que el profesor corrigió enfáticamente.

### Trampa 1: Leer el Resultado en la Fila Equivocada

> [!danger] ZONA DE PELIGRO: ¿Dónde leo las variables? Muchos alumnos buscan el valor final de las variables en la fila inferior de $C_j - Z_j$. ¡Error fatal!. **La regla:** Los valores de las [[Variables Básicas]] y el resultado de la función objetivo ($Z$) se leen **EXCLUSIVAMENTE** en la columna de solución ($P_0$ o $bld$),. Si una variable no está listada en la columna lateral de la base, es una [[Variable No Básica]] y su valor es rigurosamente $0$,.

### Trampa 2: Calcular Denominadores Prohibidos

Al calcular el [[Cociente Tita]] ($\theta$) para ver qué variable sale, los alumnos dividen a ciegas toda la columna.

> **Cómo evitarlo:** El profesor advirtió que calcular un cociente sobre un $\lambda_{ij}$ negativo o igual a $0$ arruina la matriz. Si hay un $0$ o un negativo, pon una raya. Esa fila **no compite** para salir de la base.

### Trampa 3: Vocabulario Económico (El Falso Amigo "Disponible")

Al interpretar una tasa de sustitución ligada a una [[Variable de Holgura]], los alumnos suelen escribir "horas de máquina disponibles" o "usadas".

> **Cómo evitarlo:** El profesor corrigió esto dictaminando que la holgura es estrictamente lo que sobra. Debes usar obligatoriamente la frase **"recurso sin utilizar"**,.

|Variable Analizada|Redacción Exigida si $\lambda_{ij}$ es Positivo (+)|Redacción Exigida si $\lambda_{ij}$ es Negativo (-)|
|:--|:--|:--|
|**[[Variable de Producción]]**|"Se disminuye la producción de..."|"Se incrementa la producción de..."|
|**[[Variable de Holgura]]**|"Se disminuye el recurso **sin utilizar**..."|"Se incrementa el recurso **sin utilizar**..."|

---

# 💡 TIPS PRÁCTICOS "DE TRINCHERA"

Para optimizar tu tiempo y evitar errores operativos, el profesor validó estos atajos:

- **El Atajo Numérico de la "Gran M":** Cuando usas [[Variables Artificiales]] y tienes varias "M" en la fila de $C_j - Z_j$, comparar algebraicamente qué binomio es "el más negativo" puede generar errores.
    
    > [!tip] Truco del Profesor Asigna mentalmente a la $M$ un valor real gigante (ej. $10.000$). Multiplica visualmente los coeficientes por ese número y el resultado numérico te mostrará instantáneamente cuál es la columna más negativa para ingresar a la base.
    
- **El Cuidado con el "Error de Arrastre":** Si tu resultado difiere levemente del cuestionario o del software (ej. te da 34 en lugar de 27.27), no entres en pánico rehaciendo todo. El profesor aclaró que trabajar con 2 o 3 decimales genera "errores de arrastre" debido a números periódicos (como $0.04545...$). Si usas fracciones durante el parcial, evitarás esta desviación,.
- **La Inversión de Signos (Tema de Sensibilidad):** Si el problema plantea "alquilar horas extra" en lugar de perder horas de máquina, la interpretación económica se invierte totalmente por el principio de proporcionalidad. Las tasas positivas pasarán a sumar producción, y las negativas a restarla,,.