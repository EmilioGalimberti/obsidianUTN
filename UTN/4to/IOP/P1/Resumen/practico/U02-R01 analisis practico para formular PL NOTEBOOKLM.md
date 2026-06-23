¡Entendido! Activando protocolo de Ingeniería Inversa de Exámenes. Como tu Tutor Académico de Élite, he cruzado los datos de las transcripciones de clase, los comentarios de las profesoras Claudia Carignano y Claudia Pérez, y las advertencias que hicieron sobre exámenes pasados.

El resultado es este documento táctico, diseñado en sintaxis Obsidian para que lo integres directamente a tu bóveda de estudio.

---

# 1. 🚨 RADAR DE PARCIAL (Alta Prioridad)

En esta sección decodificamos el comportamiento del examen y los criterios de evaluación que las profesoras remarcaron explícitamente y que no aparecen en la bibliografía tradicional.

- **El "Todo o Nada" del Planteo:** La profesora fue categórica al advertir que en la [[Programación Lineal]], _"si el planteo está mal todo lo otro va a estar mal"_. No hay puntos intermedios. Debes enfocarte obsesivamente en formular bien antes de calcular.
- **Múltiple Choice Penalizado (Trampa de UV):** En las evaluaciones estructuradas y parciales teóricos, **las respuestas incorrectas restan puntos**. La profesora advirtió explícitamente: _"las que están mal les va a restar en un parcial"_. Regla de oro: No adivines por descarte; si marcas 2 bien y 2 mal, tu puntaje será 0.
- **El Recuperatorio "Pisa" la Nota:** Cuidado con querer subir nota. Si te sacaste un 6 y vas al recuperatorio para llegar a la promoción, _"la reemplaza, la pisa"_. Si te sacas un 2 en el recuperatorio, quedas libre.
- **Objetivo Económico vs. Físico:** En los cuestionarios, la trampa clásica es poner "Maximizar la producción". Esto suele ser incorrecto. Si el problema da costos o ingresos, la meta real es maximizar la [[Utilidad Total]] o el [[Ingreso Neto]], ya que cada producto aporta un valor monetario diferente.
- **Clasificación de Modelos por Signos:** Evaluado de cajón. Para que un problema sea de [[Forma Canónica]] de Maximización, **todas** las inecuaciones deben ser $\le$. El profesor aclaró: _"con que una restricción ya no sea menor o igual... ya se considera mixta"_.

---

# 2. 🛠 METODOLOGÍA DE RESOLUCIÓN (Paso a Paso)

La cátedra exige un orden procedimental inquebrantable para formular un [[Modelo Matemático]].

```
graph TD
    A[Inicio: Leer y comprender el problema real] --> B[1. Traduccion verbal del Objetivo y Limitaciones]
    B --> C[2. Definicion anatomica de Variables de Decision]
    C --> D[3. Construccion matematica de la Funcion Objetivo]
    D --> E[4. Planteo de Restricciones y Analisis Dimensional]
    E --> F[5. Estandarizacion y Cierre de No Negatividad]
```

_Conceptos vinculados:_ [[Variables de Decisión]], [[Restricciones Estructurales]], [[Condición de No Negatividad]].

### Algoritmo de Formulación Estricta

**Paso 1: Traducción Verbal.** Escribir _"literalmente con palabras"_ qué se quiere lograr y cuáles son las limitaciones. _"No subestimen estos pasos"_.

**Paso 2: Definición de las [[Variables de Decisión]] ($x_j$).** Toda variable debe tener tres componentes obligatorios para ser aprobada:

1. _Unidad de Medida:_ (Ej. Unidades, Litros, Pesos).
2. _Ítem / Acción:_ (Ej. de motores tipo 1 a fabricar).
3. _Período de tiempo:_ (Ej. mensualmente).

**Paso 3: Formulación de la [[Función Objetivo]] ($Z$).** Asignar los parámetros de rentabilidad o costo a las variables sumándolos entre sí por el principio de [[Aditividad]].

> [!note] Fórmula de la Función Objetivo $$Max Z = c_1 x_1 + c_2 x_2 + \dots + c_n x_n$$

**Paso 4: Planteo de [[Restricciones Estructurales]].** Traducir los límites físicos. **Regla de Estandarización:** Al armar la inecuación, _"del lado derecho tienen que estar todo lo que sea constante y del lado izquierdo todo lo que sea variable"_. (Ej. $x_1 \ge x_2$ se debe escribir $x_1 - x_2 \ge 0$).

**Paso 5: Cierre del Modelo.** Asegurar el dominio matemático.

> [!note] Condición de No Negatividad $$x_j \ge 0 \quad \forall j$$

---

# 3. ⚠️ ZONA DE PELIGRO (Errores Comunes)

Aquí es donde caen la mayoría de los alumnos. Las profesoras revelaron los aplazos más frecuentes:

> [!danger] La Trampa Mortal de la Palabra "Cantidad" Usar la palabra "cantidad" para definir una variable (Ej. "Cantidad de dinero" o "Cantidad de motores") es considerado **un error gravísimo**. La profesora frenó la clase para sentenciar: _"cantidad no es una unidad a la cual está medida"_. Utiliza siempre la unidad exacta: _Pesos a invertir, Unidades a producir, Litros a procesar_.

> [!danger] Confusión Fatal: "Positivo" vs "No Negativo" En los exámenes choice, aparece la opción "las variables deben ser positivas". **INCORRECTO.** Anula el ejercicio. _"La no negatividad quiere decir mayor o igual a 0, no quiere decir positivo... el 0 no es positivo ni negativo"_. Exigir positividad estricta ($>0$) te obliga a producir siempre e invalida todo el modelo.

> [!danger] Confundir un [[Parámetro]] con una [[Restricción Limitante]] En el problema de los envases, marcar "los minutos de envasado" como una restricción te resta puntos. Los tiempos unitarios son **parámetros** (coeficientes tecnológicos). La verdadera limitación es la _disponibilidad total_ de horas que tiene la máquina.

---

# 4. 💡 TIPS PRÁCTICOS "DE TRINCHERA"

### 🎯 Atajos de Formulación

- **Diccionario de Traducción de Signos:** Utiliza esta tabla rápida para no fallar en las inecuaciones.

|Frase Textual del Examen|Signo Matemático a Usar|Justificación|
|:--|:--|:--|
|_"Como máximo", "No más de", "Hasta", "Dispone de"_|$\le$|Limitación de recurso o capacidad.|
|_"Como mínimo", "Al menos", "Por lo menos"_|$\ge$|Satisfacción de demanda o piso de producción.|
|_"Exactamente", "Se equilibró"_|$=$|Condición de equilibrio estricto.|

- **El Truco del [[Análisis Dimensional]]:**

> [!question] ¿Dudas si puedes sumar peras con manzanas? Un alumno preguntó si se podían mezclar "dinero y unidades de casa" en la misma restricción. La profesora respondió que **SÍ**. Si multiplicas un Costo ($/Unidad$) por la Variable ($Unidades$), las unidades físicas se simplifican (se tachan) y te quedan netamente "$Pesos$", validando que es matemáticamente correcto compararlo contra un Presupuesto (Límite Derecho en Pesos).
    
### 💻 Consejos Logísticos Críticos

- **Zoom Institucional Obligatorio:** _"tienen que entrar con cuenta institucional"_. Si entras con tu Gmail normal o como "Invitado", irás a sala de espera y **perderás tiempo valioso de parcial**.
- **Baja Automática del Aula Virtual:** Ojo si dejas la materia para el final del semestre. _"La matriculación caduca a los 60 días sin actividad"_. Ingresa semanalmente a Moodle para no ser enviado al grupo de inactivos.