https://www.youtube.com/watch?v=fb_VXa-b40A&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=14

la **Interpretación Económica** de la [[Tabla Simplex]]. Esta sesión marca la transición crucial desde la simple iteración matemática hacia el futuro [[Análisis de Sensibilidad]].

A continuación, te presento el resumen detallado de cada tema estructurado bajo las reglas de estudio avanzado.

### 1. 📢 Introducción y Diagnóstico de la Tabla Base (0:00 - 16:44)

El profesor inicia retomando un problema clásico (Fabricaciones Manuel, Productos 1 y 2) para analizar una **segunda tabla iterativa** (no óptima).

- **Lectura de Variables:** Identifica que $X_1$ no se produce porque no está en la base (es una [[Variable No Básica]] y vale $0$). En cambio, lee los valores de las [[Variables Básicas]] en la columna solución: se producen $80.5$ unidades de $X_2$, sobran $175$ horas de mano de obra ($S_1$) y $445$ de materia prima ($S_3$).
- **Agotamiento de Recursos:** La variable $S_2$ (horas máquina) no está en la base.significa que la empresa agotó toda su capacidad de ese recurso.
    
> [!note] Definición Operativa Si una [[Variable de Holgura]] vale cero, significa que ese recurso es una **restricción activa** o limitante. Se ha utilizado toda la capacidad disponible de ese insumo.


> [!note] Definición Operativa del Sistema Si un recurso está agotado, la única forma de producir un nuevo artículo (como $X_1$) es **liberando** ese recurso escaso. Esto implica obligatoriamente alterar el plan de producción y dejar de fabricar unidades de los artículos actuales.

### 2. ⚙️ El Núcleo Teórico: Las Tasas de Sustitución ($\lambda_{ij}$) (16:44 - 23:28)

Este es el concepto más importante de la clase. El profesor plantea la duda: _¿Qué pasa si queremos fabricar una unidad de $X_1$ si ya no nos quedan horas máquina?_

- **El Sacrificio:** Como no hay máquinas libres, para fabricar $X_1$ se debe **dejar de fabricar** algo de $X_2$ para liberar ese recurso.
	- las tasas de sustitución indican la cantidad exacta que debemos modificar de la variable en fila (básica) para poder incrementar en una unidad a la variable en columna (no básica).
- **Interpretación de Signos:**

> [!danger] ZONA DE PELIGRO: El Signo de la Tasa El profesor fue muy claro con la lectura de los elementos de la matriz ($\lambda_{ij}$):
> 
> - **Tasa Positiva ($>0$):** Representa un **SACRIFICIO**. Indica lo que debo dejar de fabricar o restar del sobrante para lograr producir la nueva unidad.
> - **Tasa Negativa ($<0$):** Representa un **INCREMENTO**. Indica la cantidad en la que se suma o incrementa el valor de la variable básica actual.


### 3. 📈 Impacto en $Z$ y Límite de Producción (Cociente $\theta$) (23:28 - 32:47)

El tercer eje conectó el "sacrificio" de recursos con el impacto económico final y el límite máximo que la empresa puede soportar.

- **Cálculo de $C_j - Z_j$:**  Al cambiar el plan de producción para fabricar $X_1$, la empresa pierde dinero por lo que deja de fabricar (ej. $-3.5$), pero gana por la nueva unidad producida ($+4$). El valor inferior de $C_j - Z_j$ refleja el balance o incremento neto en $Z$ (ej. $+0.5$).
- **El Límite Físico:** ¿Cuántas unidades de $X_1$ se pueden fabricar como máximo? El profesor demuestra que está limitado por la [[Restricción de No Negatividad]]. Para calcular este límite máximo (llamado [[Cociente Tita]] o $\theta$), se divide la cantidad disponible de cada recurso básico por su respectiva tasa de sustitución positiva. El menor valor define el tope.



### 4. 🛠️ Aplicación Práctica: Variación de Recursos (32:47 - 49:30)

El último tema adelantó conceptos de sensibilidad aplicando situaciones de la vida real a la tabla, alterando los lados derechos (disponibilidades) sin tener que recalcular toda la matriz.

- **Escenario A (Disminución de Recursos):** _"¿Qué pasa si por la gripe tenemos 120 horas menos de mano de obra?"_.
    - Explicación: Tener 120 horas menos equivale a forzar que la [[Variable de Holgura]] $S_1$ se incremente en $120$ (horas inutilizadas). Se multiplican las tasas de la columna $S_1$ por $120$ para ver el impacto.
- **Escenario B (Aumento de Recursos):** _"¿Qué pasa si alquilamos 60 horas máquina adicionales?"_.
    
    - Explicación: Tener horas _extra_ invierte la lógica.
    - Aquí ocurre un fenómeno crítico que suele confundir en los exámenes.
> [!tip] Tip de Trinchera: La Inversión del Signo El profesor advirtió que al **agregar un recurso extra** (en lugar de perderlo), la interpretación de los signos de la tasa de sustitución se invierte totalmente por el principio de proporcionalidad. $$ \text{Tasa Positiva} \rightarrow \text{Ahora suma (incrementa la producción)} $$ $$ \text{Tasa Negativa} \rightarrow \text{Ahora resta (disminuye la producción)} $$

#### 📊 TABLA DE BATALLA: Interpretación de Signos según el Escenario

|Escenario Operativo|Significado de $\lambda_{ij}$ POSITIVO (+)|Significado de $\lambda_{ij}$ NEGATIVO (-)|
|:--|:--|:--|
|**Iteración normal / Pérdida de recursos**|**SACRIFICIO** (Resta a la variable básica)|**INCREMENTO** (Suma a la variable básica)|
|**Aumento de disponibilidad del recurso**|**INCREMENTO** (Suma a la variable básica)|**SACRIFICIO** (Resta a la variable básica)|

### 5. 📝 Corrección del Cuestionario y Tipología de Soluciones (1:12:31 - 1:20:05)

Tras una dinámica de grupos, el profesor corrige en pantalla dos errores masivos de los alumnos respecto al problema de la "Mochila tipo 3".

- **El Costo de Oportunidad:** Aclaró que si el $C_j - Z_j$ de la mochila 3 era $-70$, significaba que la [[Función Objetivo]] iba a **disminuir** en esa cantidad por cada unidad forzada a producir.
- **Clasificación de la Solución:**
    
> [!question] Duda de Clase: ¿Es solución degenerada? Al forzar la entrada de $100$ mochilas, un alumno dudó sobre cómo clasificar el nuevo punto. El profesor le enseñó a contar: el sistema tenía $3$ restricciones, pero ahora habían quedado $4$ variables estrictamente positivas en la base. Por definición analítica, al tener más variables positivas que restricciones, esta nueva solución abandona los vértices y se clasifica como una **[[Solución Factible No Básica]]** (y descartó que fuera una [[Solución Degenerada]] porque no había variables nulas dentro de la base).
### 6. 🚀 Directivas de Estudio y Logística Moodle (1:20:05 - Final)

- **Advertencia de Examen:** El profesor exigió que, para la próxima clase teórica, es **obligatorio** leer el capítulo de [[Dualidad]] en el libro y ver el video de la profesora Perito. Advirtió que no repetirá la teoría base, sino que pasará directamente a la práctica de "Sensibilidad".

---

### 📊 DIAGRAMA DE FLUJO: Lógica del Impacto Económico (Tasas de Sustitución)

```
graph TD
    A(Quiero incrementar una Variable No Básica en 1 unidad) --> B(Leer su columna en la Tabla Simplex)
    B --> C{¿Cómo es el signo de la Tasa de Sustitución?}
    C -->|Positivo +| D(SACRIFICIO: Restar ese valor a la variable básica de la fila)
    C -->|Negativo -| E(INCREMENTO: Sumar ese valor a la variable básica de la fila)
    C -->|Cero 0| F(No afecta a esa variable básica)
    D --> G(Calcular impacto neto en Función Objetivo Z)
    E --> G
```

_Conceptos relacionados:_ [[Tasas de Sustitución]], [[Tabla Simplex]], [[Variable No Básica]], [[Variable Básica]], [[Función Objetivo]].

# ---- dudas y pregs ---

Como tu Tutor Académico de Élite, he sometido la transcripción de la clase a un escaneo minucioso. He identificado exactamente las advertencias que el profesor lanzó de cara a los próximos temas evaluables, así como las dudas conceptuales críticas que plantearon tus compañeros.

Aquí tienes el reporte de alertas y la resolución de consultas en vivo.

# 🚨 RADAR DE PARCIAL: Énfasis y Advertencias del Profesor

El profesor detuvo su explicación procedimental para hacer advertencias explícitas sobre lo que se exigirá en las próximas evaluaciones y cómo deben estudiar para no fracasar.

### 1. El Pilar del [[Análisis de Sensibilidad]]

El profesor hizo una pausa muy marcada al explicar cómo impacta la variación de un recurso (por ejemplo, tener 120 horas menos de mano de obra y simularlo incrementando la [[Variable de Holgura]]).

> [!tip] Directiva Innegociable _"Esto es importante porque después lo vamos a usar acá en el análisis de sensibilidad en las próximas cuatro semanas... quiero que se entienda bien esto"_. Entender cómo un cambio en el lado derecho ($P_0$) altera el plan de producción sin necesidad de recalcular todo el [[Método Simplex]] es la competencia fundamental que evaluará en la siguiente unidad.

### 2. La Trampa de Ignorar la Bibliografía Oficial

El profesor notó deficiencias teóricas y lanzó una advertencia severa sobre la metodología de estudio:

> [!danger] ZONA DE PELIGRO: Depender solo de los Prácticos _"Chicos, es muy importante que lean el libro. Ustedes no saben la cantidad de preguntas que por ahí me hacían en el trabajo práctico que en realidad estaban en el libro"_. Además, para la próxima clase exigió como **condición fundamental** leer los capítulos de [[Dualidad]] y ver el video asincrónico para poder trabajar directamente sobre la práctica.

---

# 🗣️ PREGUNTAS DE LOS ALUMNOS Y RESPUESTAS DEL PROFESOR

La clase tuvo intervenciones clave, especialmente referidas a la interpretación de signos y a la estructura de la matriz.

### Pregunta 1: La Inversión de Signos ante Recursos Extra

> [!question] Dudas de Concepto en Clase **Alumno:** _"Profe, me escuchas... quería plantear una duda con respecto a lo último que explicó, el cambio de signos... o sea, explicó algo como que cambiaba de signo cuando aumentaba, pero no entendí"_. **Respuesta del Profesor:** El profesor le aclaró el principio de proporcionalidad. Explicó que si te quitan un recurso (ej. una hora de máquina menos), las [[Tasas de Sustitución]] positivas indican un **sacrificio** (lo que dejas de fabricar). Sin embargo, si adquieres un recurso extra (ej. alquilas 60 horas máquina más), la interpretación se invierte totalmente: lo que antes era un coeficiente positivo que te obligaba a restar producción, ahora significa que puedes **sumar o incrementar** la producción de esa variable.

```
graph TD
    A(Variación de Recursos) --> B{¿Qué pasó con la disponibilidad?}
    B -->|Menos recurso| C(Tasa de Sustitución POSITIVA)
    C --> D(SACRIFICIO: Restar de la producción actual)
    B -->|Más recurso extra| E(Tasa de Sustitución POSITIVA)
    E --> F(INCREMENTO: Sumar a la producción actual)
```

_Conceptos relacionados:_ [[Tasas de Sustitución]], [[Análisis de Sensibilidad]].

### Pregunta 2: Discrepancia entre Filas y Restricciones

> [!question] Dudas de la Matriz (Cuestionario) **Alumno:** Al revisar un ejercicio de mochilas, notó una anomalía matricial: _"Yo tengo una duda, ¿por qué tenemos cuatro filas si tenemos tres restricciones...?"_. **Respuesta del Profesor:** El profesor resolvió la confusión rápidamente indicando que esa cuarta fila adicional existía exclusivamente porque el modelo matemático original requirió agregar una **[[Variable Artificial]]**.

### Pregunta 3: Fecha del Parcial y Logística

> [!question] Dudas Administrativas **Alumno:** Consultó sobre la fecha del primer parcial: _"¿El parcial al final se hace en el segundo cuatrimestre?"_. Además, otro alumno preguntó dónde encontrar las grabaciones de las clases. **Respuesta del Profesor:** Confirmó que el parcial fue trasladado a las primeras semanas del segundo cuatrimestre debido a un requerimiento de la coordinación para descomprimir los exámenes de las materias semestrales. Respecto al material, el profesor dedicó varios minutos a reorganizar las pestañas de Moodle en vivo, ya que una actualización del servidor había ocultado los videos y desconfigurado el aula virtual.