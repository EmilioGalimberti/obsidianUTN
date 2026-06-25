
# Si el conjunto de soluciones factibles de un PL tiene infinitos elementos, entonces el conjunto de soluciones básicas tendrá  
- [ ]  La cantidad de elementos depende de la cantidad de variables y restricciones del problema
- [ ] Ningún elemento
- [ ] Un elemento
- [ ] Infinitos elementos

## rta
**Respuesta Correcta:** **La cantidad de elementos depende de la cantidad de variables y restricciones del problema**

---

### 🗣️ CÓMO JUSTIFICAR (El "Por qué" Analítico)

Como tu Tutor Académico de Élite, te explico el núcleo teórico detrás de esta pregunta "trampa". El profesor evalúa aquí si comprendes la diferencia geométrica y algebraica entre el área de un poliedro y los puntos donde se cruzan sus líneas.

En la teoría de la [[Programación Lineal]], es completamente normal que las **[[Soluciones Factibles]]** sean infinitas. Si lo visualizas en un gráfico, la región factible (el área verde o sombreada dentro del [[Poliedro de Soluciones]]) está compuesta por infinitos puntos decimales y fraccionarios.

Sin embargo, las **[[Soluciones Básicas]]** no son áreas, sino puntos algebraicos exactos. Se encuentran única y exclusivamente en las intersecciones de las rectas del sistema de ecuaciones. Como el número de rectas en un problema es limitado, el número de intersecciones también tiene un techo matemático finito, el cual se calcula mediante una fórmula combinatoria.

> [!note] Fórmula de la Cota Superior Combinatoria El número máximo de [[Soluciones Básicas]] está dictaminado por el combinatorio de los elementos de la matriz del modelo, y depende estructuralmente de $n$ y $m$: $$ C_m^n = \frac{n!}{m!(n-m)!} $$ Donde:
> 
> - $n$ = Número total de variables (incluye [[Variables de Decisión]] + [[Variables de Holgura]] / Excedentes).
> - $m$ = Número de [[Restricciones Funcionales]] (las ecuaciones del sistema).

### ⚠️ ZONA DE PELIGRO: La Trampa de Examen

> [!danger] Falso Amigo Teórico: El contagio del "Infinito" Muchos alumnos se equivocan al pensar: _"Si lo factible es infinito, entonces sus bases también lo son"_. Esto es un error conceptual crítico. El profesor recalcó explícitamente en clase: _"las soluciones factibles son infinitas... pero las soluciones básicas no son infinitas tienen un número máximo un límite... dado por el combinatorio de n elementos tomados de m en m"_.

Para que estructures mentalmente la jerarquía analítica que el profesor espera ver dominada, sigue este flujo:

```
graph TD
    A(Modelo de Programación Lineal) --> B(Poliedro de Soluciones / Región Factible)
    B --> C(Puntos interiores y lados)
    C -->|Son infinitos puntos| D(Infinitas Soluciones Factibles)
    A --> E(Sistema de Ecuaciones Restrictivas)
    E --> F(Intersecciones de Rectas)
    F -->|Depende de n variables y m restricciones| G(Número Finito de Soluciones Básicas)
```

_Conceptos relacionados:_ [[Soluciones Factibles]], [[Soluciones Básicas]], [[Programación Lineal]].


# Si el conjunto de soluciones factibles de un PL tiene infinitos elementos, entonces el conjunto de soluciones óptimas

- [ ] Tiene un elemento
- [ ] Es vacío
- [ ] La cantidad de elementos depende de la cantidad de variables y restricciones del problema
- [ ] Tiene infinitos elementos

## rta
**Respuestas Correctas (Seleccione estas TRES opciones):**

- **Tiene un elemento**
- **Es vacío**
- **Tiene infinitos elementos**

---

### 🗣️ CÓMO JUSTIFICAR (El "Por qué" Analítico)

Como tu Tutor Académico de Élite, te explico que esta es una clásica pregunta de evaluación teórica donde el profesor evalúa si comprendes los escenarios de optimización basados en los teoremas de PL.

Durante la clase teórica sobre los Teoremas de PL, el profesor explicó explícitamente qué sucede cuando el conjunto de **[[Soluciones Factibles]]** tiene infinitos elementos (lo cual es el caso más común, ya que representa toda el área dentro del [[Poliedro de Soluciones]]). En este escenario, el conjunto de **[[Soluciones Óptimas]]** puede presentar tres situaciones distintas:

> [!note] Los 3 Escenarios de Optimidad (Explicación Literal del Profesor)
> 
> 1. **Tiene un único elemento:** Es el caso estándar. Se da cuando la función objetivo toca un único vértice óptimo al desplazarse.
> 2. **Es vacío:** Ocurre cuando el problema es "no acotado". El poliedro está abierto (infinito hacia un lado) y la función objetivo $Z$ se puede desplazar infinitamente sin encontrar nunca un límite superior o cota. Al no poder cerrarse un valor óptimo finito, el conjunto de soluciones óptimas es vacío.
> 3. **Tiene infinitos elementos:** Ocurre debido al **Teorema 2**. Se da cuando la recta de la función $Z$ es exactamente paralela a una **[[Restricción Limitante]]**. Cualquier punto sobre ese segmento otorga el mismo beneficio óptimo.

### ⚠️ ZONA DE PELIGRO: La Opción "Trampa"

Debes **dejar sin marcar** la opción: _"La cantidad de elementos depende de la cantidad de variables y restricciones del problema"_.

**¿Por qué es trampa?** Porque esa afirmación no aplica a las soluciones óptimas, sino a la fórmula combinatoria $C = \frac{n!}{m!(n-m)!}$. Esa fórmula se usa exclusiva y estrictamente para calcular el límite de las **[[Soluciones Básicas]]** (las intersecciones de las rectas), no para definir cuántos óptimos tiene el sistema.

# Si el conjunto de soluciones óptimas de un PL es vacío, entonces el conjunto de soluciones factibles
- [ ] Es vacío
- [ ] La cantidad de elementos depende de la cantidad de variables y restricciones del problema
- [ ] Tiene un elemento
- [ ] Tiene infinitos elementos
## rta
**Respuestas Correctas (Seleccione estas DOS opciones):**

- **Es vacío**
- **Tiene infinitos elementos**

---

### 🗣️ CÓMO JUSTIFICAR (El "Por qué" Analítico)

Como tu Tutor Académico de Élite, te explico que esta pregunta evalúa tu capacidad para hacer "ingeniería inversa" sobre los postulados teóricos del profesor. En lugar de preguntarte qué pasa si el conjunto factible es infinito (como en la pregunta anterior), aquí te da el resultado final (no hay óptimo) y te pide deducir cómo era el [[Poliedro de Soluciones]] original.

Basándonos en la explicación teórica exacta de la clase, si el conjunto de **[[Soluciones Óptimas]]** es vacío (es decir, no existe un punto óptimo), esto solo puede justificarse matemáticamente por dos escenarios estructurales:

> [!note] Escenario 1: El [[Problema Incompatible]] Si el conjunto de **[[Soluciones Factibles]]** es **vacío** (no existe ningún punto que cumpla todas las restricciones a la vez), es lógicamente imposible encontrar un óptimo. El profesor lo definió literalmente: _"si el conjunto de soluciones factibles es vacío entonces el conjunto de soluciones óptimas también será vacío"_.

> [!note] Escenario 2: El [[Problema No Acotado]] Se da cuando el conjunto de **[[Soluciones Factibles]]** tiene **infinitos elementos** formando un área "abierta" hacia el infinito. En este caso, la [[Función Objetivo]] ($Z$) puede desplazarse infinitamente sin chocar nunca con una cota o límite superior. Al no poder detenerse la recta, el óptimo no se alcanza jamás, por lo que el conjunto de soluciones óptimas es vacío.

Para que domines esta lógica causal bidireccional, aquí tienes el mapa conceptual del razonamiento:

```
graph TD
    A(Conjunto de Soluciones Óptimas es VACÍO) --> B{¿Por qué ocurre esto?}
    B -->|Causa 1: No hay área válida| C(El Conjunto Factible es VACÍO)
    C --> D(Problema Incompatible)
    B -->|Causa 2: El área no tiene límite| E(El Conjunto Factible tiene INFINITOS ELEMENTOS)
    E --> F(Problema No Acotado)
```

_Conceptos relacionados:_ [[Problema Incompatible]], [[Problema No Acotado]], [[Soluciones Factibles]], [[Soluciones Óptimas]].

### ⚠️ ZONA DE PELIGRO: Descarte Analítico de las "Trampas"

Debes dejar sin marcar estrictamente las otras dos opciones por estas razones teóricas:

> [!danger] Trampa Lógica: "Tiene un elemento" ¿Por qué es falso? Porque el profesor demostró que si el conjunto de [[Soluciones Factibles]] está formado por un único elemento (las rectas se cruzan en un solo punto válido), entonces ese único punto es obligatoriamente el óptimo. Su conjunto óptimo tendría un elemento, no sería vacío.

> [!danger] Falso Amigo de Examen: "Depende de la cantidad de variables..." Como vimos en la pregunta anterior, esta afirmación es una trampa recurrente. La fórmula combinatoria $C = \frac{n!}{m!(n-m)!}$ **solo** define la cantidad de [[Soluciones Básicas]] (las intersecciones de las rectas), y jamás se utiliza para dictaminar el tamaño del conjunto factible ni del conjunto óptimo.



---
# ----------

#  Dado el PL
Max  Z = 100X1 + 120X2  
Sa
1) 10X1 +15X2 ≤ 1000  
2) 30X1 +20X2 ≤ 1950  
3) X1 ≤ 65  
4) X2 ≤ 50  
5) X1 ≥ 20  
X1; X2 ≥ 0

Clasifique los conjuntos de valores de las variables que se dan a continuación
 1) X1=20;    X2= 50;   S1= 50;   S2=350;    S3=45;   S4= 0;   S5= 0;     Z = 8000
 2) X1=20;    X2= 67,5;   S1= -212,5;   S2=0;    S3=45;   S4= -17,5;   S5= 0 ,      Z = 10100
 3) X1=40;    X2= 18;   S1= 330;   S2=390;    S3=25;   S4= 32;   S5= 20;      Z = 6160
 4) X1=70;    X2= 60;   S1= 100;   S2=-1350;    S3=-5;   S4= -10;   S5= 90;    Z = 14200
 5) X1=65;    X2= 0;   S1= 350;   S2=0;    S3=0;   S4= 50;   S5= 45;    Z = 6500
 6) X1=26;    X2= 45;   S1= 65;   S2=270;    S3=39;   S4= 5;   S5= 6;     Z = 8000
## rta
Aquí tienes el análisis exhaustivo de cada conjunto de valores. Como tu Tutor Académico de Élite, he aplicado estrictamente la metodología de clasificación que el profesor evaluó y corrigió durante la clase práctica, asegurándome de no caer en las "trampas" típicas de examen.

### 🛠 METODOLOGÍA DE RESOLUCIÓN (Algoritmo del Profesor)

> [!tip] Protocolo Innegociable de Clasificación Para evitar errores letales (como clasificar un punto que ni siquiera pertenece al modelo), el profesor exige seguir este flujo:
> 
> 1. **Transformar a la [[Forma Estándar]]:** Identificar que el modelo tiene $n=7$ variables (2 de decisión + 5 auxiliares) y $m=5$ restricciones.
> 2. **Verificar Igualdad:** Reemplazar TODOS los valores en el [[Sistema de Ecuaciones]]. Si falla en al menos una, se descarta automáticamente.
> 3. **Análisis de Signos:** Verificar si viola la [[Restricción de No Negatividad]].
> 4. **Conteo de Variables Positivas:** Si hay un máximo de $m$ positivas (5 en este caso), es **Básica**. Si hay más de $m$ positivas, es **No Básica**.

```
graph TD
    A(Evaluar Valores en Sistema de Ecuaciones) --> B{¿Cumple las 5 igualdades?}
    B -->|No| C(NO ES SOLUCIÓN)
    B -->|Sí| D{¿Tiene algún valor negativo?}
    D -->|Sí| E(BÁSICA NO FACTIBLE)
    D -->|No| F{¿Cuántos valores son > 0?}
    F -->|> 5 variables| G(FACTIBLE NO BÁSICA)
    F -->|Exactamente 5 variables| H(FACTIBLE BÁSICA NO DEGENERADA)
    F -->|< 5 variables| I(FACTIBLE BÁSICA DEGENERADA)
```

_Conceptos relacionados:_ [[Solución Factible Básica]], [[Forma Estándar]], [[Sistema de Ecuaciones]].

---

### 📋 CLASIFICACIÓN DE RESULTADOS

A continuación, presento el dictamen analítico para cada uno de los incisos:

**Respuesta 1 Pregunta 1** **[[Solución Factible Básica No Degenerada]]** (o simplemente **[[Solución Factible Básica]]**)

> 🗣️ **Cómo Justificar:** Al reemplazar los valores en la [[Forma Estándar]], la igualdad matemática se cumple en las 5 restricciones. Como todos sus valores son $\geq 0$, es "Factible". Al contar las variables, posee exactamente $m=5$ variables positivas ($X_1, X_2, S_1, S_2, S_3$) y exactamente $n-m=2$ variables nulas ($S_4, S_5$). Gráficamente, esto representa un vértice perfecto del [[Poliedro de Soluciones]].

**Respuesta 2 Pregunta 1** **[[Solución Básica No Factible]]**

> 🗣️ **Cómo Justificar:** Cumple algebraicamente el sistema de ecuaciones, pero presenta valores negativos en las variables $S_1$ y $S_4$. Esto viola la [[Restricción de No Negatividad]], lo que la hace "No Factible" (está fuera del primer cuadrante válido). Es "Básica" porque mantiene exactamente $n-m=2$ variables en cero ($S_2, S_5$).

**Respuesta 3 Pregunta 1** **[[Solución Factible No Básica]]**

> 🗣️ **Cómo Justificar:** Verifica todo el sistema y no tiene valores negativos, por lo que pertenece a la región válida. Sin embargo, al observar los datos, **las 7 variables son estrictamente positivas** ($>0$). Como el número de variables positivas (7) supera la cantidad de restricciones $m=5$, se clasifica como "No Básica". Gráficamente, es un punto que está flotando en el interior del poliedro, no en un vértice.

**Respuesta 4 Pregunta 1** **[[No es Solución]]**

> [!danger] ZONA DE PELIGRO ABSOLUTA: El "Falso Amigo" La trampa aquí es ver los valores negativos de las holguras y apresurarse a etiquetarla como "No Factible". ¡Alto ahí! Si reemplazamos los valores de $X_1=70$ y $X_2=60$ en la restricción 1 ($10_70 + 15_60 + S_1 = 1000$), con $S_1=100$, el resultado es $1700 \neq 1000$. Falla el paso 1 del algoritmo. Como no satisface la igualdad matemática, el conjunto simplemente es basura analítica.

**Respuesta 5 Pregunta 1** **[[Solución Factible Básica Degenerada]]**

> 🗣️ **Cómo Justificar:** Cumple el sistema y respeta la positividad. La clave teórica aquí radica en el conteo de variables. Posee $3$ variables iguales a cero ($X_2, S_2, S_3$), lo cual supera el estándar normal de $n-m=2$. Como consecuencia, tiene apenas $4$ variables positivas ($< m$). El profesor definió explícitamente que cuando esto ocurre, la solución es "Degenerada". Gráficamente, se están cruzando más de dos rectas en ese único vértice.

**Respuesta 6 Pregunta 1** **[[Solución Factible No Básica]]**

> 🗣️ **Cómo Justificar:** Al igual que en la Respuesta 3, todos los valores satisfacen el modelo a la perfección y no violan ningún signo. Sin embargo, las 7 variables ($X_1, X_2, S_1, S_2, S_3, S_4, S_5$) son positivas, careciendo de los ceros obligatorios requeridos para anclarse a los ejes o a las fronteras del modelo. Se encuentra en el interior del polígono.

#  Con los vectores solución:
X1=20;    X2= 50;   S1= 50;   S2=350;    S3=45;   S4= 0;   S5= 0;     Z = 8000

X1=40;    X2= 18;   S1= 330;   S2=390;    S3=25;   S4= 32;   S5= 20;      Z = 6160

y un α= 0,50, encuentre otra solución del problema.

X1= Respuesta 1 Pregunta 2 ;     
X2= Respuesta 2 Pregunta 2;    
S1= Respuesta 3 Pregunta 2;    
S2= Respuesta 4 Pregunta 2;     
S3= Respuesta 5 Pregunta 2;    
S4= Respuesta 6 Pregunta 2;    
S5= Respuesta 7 Pregunta 2;
## rta 
Como tu Tutor Académico de Élite, he resuelto este cálculo aplicando estrictamente el procedimiento algorítmico que el profesor desarrolló en la pizarra virtual durante la clase práctica.

Este ejercicio evalúa la aplicación directa del **Teorema 1** de la [[Programación Lineal]], el cual demuestra que el espacio de soluciones es un [[Conjunto Convexo]].

> [!note] Fórmula de [[Combinación Lineal Convexa]] Para obtener un nuevo [[Vector Solución]] factible ($V_{nuevo}$) a partir de dos vectores ($V_1$ y $V_2$), se multiplican por escalares ($\alpha$) que deben sumar exactamente $1$. $$ V_{nuevo} = \alpha_1 V_1 + \alpha_2 V_2 $$ Si el enunciado te otorga $\alpha_1 = 0.50$, por regla estricta $\alpha_2 = 1 - 0.50 = 0.50$.

### 🛠 METODOLOGÍA DE RESOLUCIÓN (Cálculo Vectorial)

Debes multiplicar cada elemento del primer vector por $0.50$ y sumarlo al elemento respectivo del segundo vector multiplicado por $0.50$:

- $X_1 = (0.50 \times 20) + (0.50 \times 40) = 10 + 20 = 30$
- $X_2 = (0.50 \times 50) + (0.50 \times 18) = 25 + 9 = 34$
- $S_1 = (0.50 \times 50) + (0.50 \times 330) = 25 + 165 = 190$
- $S_2 = (0.50 \times 350) + (0.50 \times 390) = 175 + 195 = 370$
- $S_3 = (0.50 \times 45) + (0.50 \times 25) = 22.5 + 12.5 = 35$
- $S_4 = (0.50 \times 0) + (0.50 \times 32) = 0 + 16 = 16$
- $S_5 = (0.50 \times 0) + (0.50 \times 20) = 0 + 10 = 10$

---

### 📋 RESPUESTAS FORMATEADAS PARA EL CUESTIONARIO

Aquí tienes los valores exactos listos para rellenar en tu plataforma:

**X1=** 30

**X2=** 34

**S1=** 190

**S2=** 370

**S3=** 35

**S4=** 16

**S5=** 10

> [!tip] Tip Práctico "De Trinchera" Si observas los valores obtenidos, verás que todas las variables del nuevo vector son positivas ($>0$). Al tener 7 variables estrictamente mayores a cero en un problema que tiene solo 5 restricciones ($m=5$), esta nueva solución se clasifica teóricamente como una **[[Solución Factible No Básica]]** (es un punto que quedó flotando en el interior del poliedro de soluciones, no en los vértices).

# Con un α= 0,50, encuentre otra solución del problema tal que el valor de Z  se igual a  8000
X1=40;    X2= 18;   S1= 330;   S2=390;    S3=25;   S4= 32;   S5= 20;            Z = 6160 

X1=20;    X2= 50;   S1= 50;   S2=350;    S3=45;   S4= 0;   S5= 0;                  Z = 8000  

X1=65;    X2= 0;   S1= 350;   S2=0;    S3=0;   S4= 50;   S5= 45;                    Z = 6500  

X1=26;    X2= 45;   S1= 65;   S2=270;    S3=39;   S4= 5;   S5= 6;                      Z = 8000 

X1=20;    X2= 67,5;   S1= -212,5;   S2=0;    S3=45;   S4= -17,5;   S5= 0 ,       Z = 10100

---
X1= Respuesta 1 Pregunta 3;     
X2= Respuesta 2 Pregunta 3;    
S1= Respuesta 3 Pregunta 3;    
S2= Respuesta 4 Pregunta 3;     
S3= Respuesta 5 Pregunta 3 ;    
S4= Respuesta 6 Pregunta 3;    
S5= Respuesta 7 Pregunta 3;

## rta
Como tu Tutor Académico de Élite, he analizado tu petición y los vectores proporcionados. Este ejercicio evalúa tu capacidad para aplicar analíticamente el **Teorema 2** de la [[Programación Lineal]] mediante el uso de una [[Combinación Lineal Convexa]].

> [!note] Teorema 2: Múltiples Óptimos y Recta de Isoutilidad El profesor dictaminó en la teoría que _"Si existe más de una solución factible que le den el mismo valor a la función objetivo, cualquier combinación lineal convexa de las mismas, dará al funcional igual valor"_. Esto significa que cualquier punto intermedio entre dos soluciones apoyadas sobre la misma recta $Z$ mantendrá intacto el beneficio económico.

### 🛠 METODOLOGÍA DE RESOLUCIÓN (Algoritmo Vectorial)

```
graph TD
    A(1. Filtrar el conjunto de datos) --> B(2. Identificar los dos vectores donde Z = 8000)
    B --> C(3. Asignar los escalares: alfa1 = 0.50 y alfa2 = 0.50)
    C --> D(4. Calcular la suma ponderada variable por variable)
    D --> E(5. Obtener el nuevo Vector Solución)
```

_Conceptos relacionados:_ [[Teorema 2]], [[Combinación Lineal Convexa]], [[Vector Solución]], [[Recta de Isoutilidad]].

**Paso 1: Selección de Vectores** De la lista proporcionada, debemos aislar únicamente los dos vectores que otorgan $Z = 8000$:

- **Vector A:** $X_1=20; X_2=50; S_1=50; S_2=350; S_3=45; S_4=0; S_5=0$
- **Vector B:** $X_1=26; X_2=45; S_1=65; S_2=270; S_3=39; S_4=5; S_5=6$

**Paso 2: Aplicación de la Fórmula**

> [!tip] Tip de Trinchera: El Escalar Complementario Para que una combinación lineal sea "convexa" y caiga dentro de la [[Región Factible]], la suma de los escalares ($\alpha$) debe ser exactamente $1$. Si el enunciado te da $\alpha_1 = 0.50$, el segundo escalar es obligatoriamente $\alpha_2 = 1 - 0.50 = 0.50$.

**Paso 3: Cálculo Analítico** Multiplicamos cada elemento de los vectores elegidos por $0.50$ y los sumamos:

- **$X_1$:** $(0.50 \times 20) + (0.50 \times 26) = 10 + 13 = \mathbf{23}$
- **$X_2$:** $(0.50 \times 50) + (0.50 \times 45) = 25 + 22.5 = \mathbf{47.5}$
- **$S_1$:** $(0.50 \times 50) + (0.50 \times 65) = 25 + 32.5 = \mathbf{57.5}$
- **$S_2$:** $(0.50 \times 350) + (0.50 \times 270) = 175 + 135 = \mathbf{310}$
- **$S_3$:** $(0.50 \times 45) + (0.50 \times 39) = 22.5 + 19.5 = \mathbf{42}$
- **$S_4$:** $(0.50 \times 0) + (0.50 \times 5) = 0 + 2.5 = \mathbf{2.5}$
- **$S_5$:** $(0.50 \times 0) + (0.50 \times 6) = 0 + 3 = \mathbf{3}$

---

### 📋 RESPUESTAS FORMATEADAS PARA EL CUESTIONARIO

Aquí tienes los valores numéricos exactos listos para ser ingresados en la plataforma:

**X1 =** 23

**X2 =** 47.5

**S1 =** 57.5

**S2 =** 310

**S3 =** 42

**S4 =** 2.5

**S5 =** 3

> [!danger] Trampa de Justificación: Clasificación de esta nueva solución Si observas el vector resultante, notarás que las 7 variables son estrictamente positivas ($>0$). Como en este problema el número de restricciones ($m$) es $5$ (lo sabemos porque hay 5 [[Variables de Holgura]]), y este nuevo punto tiene $7$ variables positivas, este nuevo vector es matemáticamente una **[[Solución Factible No Básica]]**. Gráficamente, acabas de encontrar un punto apoyado en el medio de la [[Recta de Isoutilidad]] que une a los dos vértices originales.

