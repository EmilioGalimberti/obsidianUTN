¡Hola! Activando protocolo de Síntesis Teórica y Preparación de Exámenes Conceptuales. Como tu Tutor Académico de Élite, he "escaneado" exhaustivamente las transcripciones de las clases teóricas de la unidad 1 y 2, prestando especial atención a las pausas de la profesora, sus anécdotas de evaluación y su manera particular de definir los conceptos frente a lo que dicen los libros tradicionales.

Aquí tienes tu **Mapa de Dominio Conceptual**, destilado y listo para que lo integres como base teórica infalible para tus parciales.

---

# 1. 🎯 RADAR CONCEPTUAL (Alta Prioridad)

En esta sección agrupamos los conceptos _core_ que sustentan toda la materia y el vocabulario obligatorio que los profesores buscan leer (o escuchar) para dar por aprobada una pregunta teórica.

- **Modelo Matemático:** Es una _"representación simplificada de la realidad"_ que utiliza funciones matemáticas para representar un problema.
- **Modelo Formal:** La Programación Lineal (PL) se considera un "modelo formal" porque _atiende a la forma_ en la que se modeliza y no al contenido intrínseco. Se puede usar exactamente la misma estructura matemática para planificar una dieta de cerdos que para cargar bombas en un avión militar.
- **Modelo de Universo Cierto:** Se llama así porque asume la certeza total de los parámetros que lo definen.

**Palabras Clave Obligatorias (Buzzwords de la cátedra):**

- **Parámetros:** (Coeficientes, tasas de transformación, disponibilidades $c_j, a_{ij}, b_i$). Son _datos conocidos con certeza_ que acompañan a las variables.
- **Variables de Decisión:** Las incógnitas puras a determinar ($x_j$).
- **Supuestos / Hipótesis:** Las bases que dan validez al modelo. Si no se cumplen, el modelo no es válido.

---

# 2. ⚖️ CUADROS DE BATALLA (Comparaciones y Clasificaciones)

### Contribución Marginal vs. Ingreso

En un examen teórico-práctico te pueden pedir identificar la meta económica. La profesora fue muy estricta en separar estos conceptos:

- **Ingreso Total:** Es simplemente el Precio de Venta. Se maximiza _solo_ si el problema te da únicamente precios de venta.
- **Contribución Marginal (o Beneficio / Utilidad):** Es el Precio de Venta _menos_ los Costos Variables Directos. Si el problema te da ventas y costos, estás obligado a maximizar la Contribución Marginal.

### Clasificación de Modelos de PL (Por Signos)

Esta es una pregunta segura de evaluación estructurada. El modelo se clasifica observando las inecuaciones.

|Clasificación|Para Maximización|Para Minimización|Concepto Clave de Clase|
|:--|:--|:--|:--|
|**Forma Canónica**|Todas las restricciones $\le$|Todas las restricciones $\ge$|Debe ser puro. _"Con que una restricción ya no sea menor o igual... ya se considera mixta"_.|
|**Forma Estándar**|Todas las restricciones $=$|Todas las restricciones $=$|Condición de equilibrio estricto.|
|**Forma Mixta**|Signos mezclados ($\le, \ge, =$)|Signos mezclados ($\le, \ge, =$)|Es la situación más habitual en problemas reales.|

---

# 3. ⚠️ TRAMPAS DE OPCIÓN MÚLTIPLE / V o F

Aquí están los "falsos amigos" donde los alumnos marcan mecánicamente y reprueban en los cuestionarios de la UV.

- **🚨 Falso Amigo 1: "Las variables deben ser POSITIVAS".**
    - _Por qué es falso:_ La profesora contó que un alumno hizo aplazar a su grupo por esto. La condición es de **No Negatividad** ($\ge 0$). _Justificación teórica de clase:_ "El 0 no es positivo ni negativo". Exigir positividad estricta ($>0$) obliga al modelo a producir siempre y anula la posibilidad de decidir no fabricar un producto.
- **🚨 Falso Amigo 2: "El objetivo es maximizar la producción".**
    - _Por qué es falso:_ En problemas económicos, no es lo mismo maximizar la suma física de productos que maximizar su rentabilidad. Cada producto aporta un peso económico diferente, por ende, el objetivo teórico real es **Maximizar la Utilidad o Contribución Total**.
- **🚨 Falso Amigo 3: "Los minutos que requiere un producto son una limitación / restricción".**
    - _Por qué es falso:_ Los tiempos unitarios de fabricación no son restricciones, son **Parámetros** (tasas tecnológicas). La verdadera "restricción" teórica es la _disponibilidad total del recurso_ (ej. 120 horas de máquina).
- **🚨 Falso Amigo 4: "La palabra 'cantidad' es una unidad válida".**
    - _Por qué es falso:_ Usar la palabra "cantidad" en la definición de la variable la vuelve teóricamente difusa. _Definición estricta de la cátedra:_ Debe tener unidad de medida clara (litros, kg, pesos), ítem, y período de medición.

---

# 4. 🗣️ CÓMO JUSTIFICAR (El "Por qué")

En las evaluaciones teóricas, te pedirán justificar los **Supuestos o Hipótesis del Modelo Lineal**. Aquí tienes el "Por Qué" causal de cada supuesto, extraído textualmente de las explicaciones de la profesora:

**1. Supuesto de Certidumbre:**

- _¿Qué asume?_ Que los parámetros ($c_j, a_{ij}, b_i$) se conocen con certeza matemática exacta.
- _¿Cómo se justifica en un examen?_ Se debe aclarar que, dado que en la realidad esto es casi imposible (porque los recursos y tiempos son estimaciones y pueden ocurrir imprevistos como operarios enfermos), el modelo es una "foto" de un momento. _Por lo tanto_, exige que al finalizar se realice un **Análisis de Post-Optimidad** (o sensibilidad) para ver qué ocurre si esos parámetros cambian.

**2. Supuesto de Divisibilidad:**

- _¿Qué asume?_ Que las variables pueden asumir cualquier valor fraccionario (Ej. fabricar $37.2$ motores).
- _¿Cómo se justifica en un examen?_ Aunque en la vida real haya productos no fraccionables, en la PL pura se permite la fracción. Si la realidad exige enteros estrictos, se debe cambiar a un modelo de _Programación Lineal Entera_. Para la formulación lineal básica, obviamos temporalmente esa restricción.

**3. Supuesto de Proporcionalidad:**

- _¿Qué asume?_ Que no existen las "economías de escala".
- _¿Cómo se justifica en un examen?_ Matemáticamente significa que _todas las variables están elevadas al exponente 1_. Si gano $4 fabricando una unidad, gano $40,000 fabricando 10,000. Los costos y ganancias crecen en proporción directa.

**4. Supuesto de Aditividad:**

- _¿Qué asume?_ Que las contribuciones individuales se suman.
- _¿Cómo se justifica en un examen?_ En la estructura del modelo _sólo intervienen sumas_, prohibiendo matemáticamente cualquier multiplicación entre variables ($x_1 \cdot x_2$). El uso total de recursos es igual a la suma del uso individual de cada producto.

**5. Supuesto de Único Objetivo:**

- _¿Qué asume?_ Que solo se maximiza o minimiza _una_ función $Z$.
- _¿Cómo se justifica en un examen?_ Si una empresa busca maximizar beneficios Y simultáneamente minimizar contaminación ambiental de forma directa, no puede usar PL básica. Deberá recurrir a _Modelos Multi-Objetivo_.