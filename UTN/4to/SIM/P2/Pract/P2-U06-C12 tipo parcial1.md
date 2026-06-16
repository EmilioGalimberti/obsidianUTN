¡Hola! Como tu Tutor Académico de Élite, he analizado en profundidad la última transcripción. Esta sesión es de altísimo valor estratégico, ya que el profesor resuelve paso a paso un modelo de **Segundo Parcial** (el caso de Tarjeta Naranja/Municipalidad) que combina una [[Simulación Discreta]] con una [[Ecuación Diferencial]] para actualizar resúmenes.

A continuación, te presento la guía metodológica definitiva estructurada en formato Zettelkasten, destacando las fórmulas, los atajos y las "trampas" mortales que descontaron puntos en ese examen.

---

# Guía de Resolución: Parcial Integrador (Colas + Euler/Runge-Kutta)

## 1. Planteo del Modelo y Estructura del [[Vector de Estado]]

Antes de iterar, la metodología estricta exige definir el comportamiento de los [[Objetos Temporarios]] (Clientes) interactuando con los [[Objetos Permanentes]] (Ventanilla de Actualización y Cajas de Pago).

### Clasificación de Entidades y Estados

|Categoría|Elementos del Sistema|Lógica de Modelado|
|:--|:--|:--|
|**[[Eventos]]**|`Llegada`, `Fin Actualización`, `Fin Pago Sub i`|Como hay dos cajas, es obligatorio modelar el fin de pago como **[[Eventos Sub i]]** (Caja 1 y Caja 2).|
|**[[Objetos Permanentes]]**|`Ventanilla Actualización`, `Caja 1`, `Caja 2`|Tienen estados básicos: `[[Libre]]` u `[[Ocupado]]`.|
|**[[Objetos Temporarios]]**|`Cliente`|Sus estados reflejan su etapa: `[[Actualizando Resumen]]`, `[[Esperando Pagar]]`, `[[Pagando Resumen]]`.|
|**[[Colas]]**|Fila de Actualización y Fila de Cajas|El enunciado establece explícitamente que **hay una sola cola para las dos cajas**.|

### Diagrama de Flujo del Cliente

```
graph TD
    A[Llega Cliente al Sistema] --> B{¿Tiene Resumen Vencido?}
    B -- NO: 52% --> C{¿Hay Cola en Cajas?}
    C -- SI --> D[Se va sin pagar]
    C -- NO --> E[Pasa a Cajas]

    B -- SI: 48% --> F{¿Hay Cola en Ventanilla?}
    F -- SI --> G[Se va sin actualizar ni pagar]
    F -- NO --> H[Actualiza Resumen Ecuacion Diferencial]

    H --> I{¿Se queda a pagar? 67%}
    I -- NO --> J[Se retira sin pagar]
    I -- SI --> K[Va a Cola de Cajas SIN importar la longitud]
```

_(Conceptos relacionados: [[Condiciones Lógicas]], [[Probabilidad Acumulada]], [[Destrucción de Entidad]])_

---

## 2. Fórmulas Matemáticas Clave y Atajos

El profesor dedicó un bloque extenso a explicar cómo simular la complejidad del resumen (un valor entre 1 y 4) y cómo transformar el tiempo continuo de la ecuación.

> [!note] Fórmula: [[Distribución Uniforme Continua]] Simplificada Para las llegadas entre 0 y 25 segundos, el extremo $A$ es 0. La fórmula se reduce: $$ X = RND \times 25 $$ _(Porque $A + RND \times (B - A) \rightarrow 0 + RND \times 25$)_.

> [!tip] Atajo de Parcial: Simular [[Distribución Uniforme Discreta]] Si el enunciado pide una variable discreta (ej. complejidad 1, 2, 3 o 4) y quieres evitar hacer una tabla de Montecarlo con 26 intervalos, **usa la fórmula continua sumándole 1 al límite superior y aplicando truncamiento**. $$ X = TRUNCAR(A + RND \times ((B + 1) - A)) $$ _Ejemplo del profe:_ Para opciones entre 1 y 4 $\rightarrow$ $X = TRUNCAR(1 + RND \times 4)$. Esto le da equidad exacta del 25% a cada número entero.

> [!note] Fórmula: [[Equivalencia de Tiempo]] (Ecuaciones Diferenciales) Cuando integras (con Euler o Runge-Kutta) y superas el objetivo, el valor de $t$ obtenido NO son los segundos del reloj. $$ Tiempo_Real = t_Integracion \times 60 $$ _Ejemplo en clase:_ Si la tabla dio 1.10 y la unidad vale 60 segundos, el tiempo de actualización que llevas a tu tabla es $1.10 \times 60 = 66$ segundos.

---

## 3. 🚨 Trampas Mortales ("Cosas a tener cuidado")

El profesor advirtió sobre errores críticos que causan grandes descuentos de puntos en este tipo de parciales:

> [!danger] TRAMPA 1: No calcular las [[Medidas de Desempeño]] Finales **El error más reportado:** Los alumnos hicieron perfectamente las columnas de los `[[Acumuladores]]` y `[[Contadores]]`, llegaron al segundo 100, y entregaron el Excel. **La regla:** "Muchos se han olvidado de hacer el promedio... había que contestar explícitamente". Debes tomar el valor final de tu acumulador, dividirlo por el contador, y **escribir el resultado final** en una celda visible (ej. Promedio: 16.83).

> [!danger] TRAMPA 2: Ignorar a los que "Esperan Cero" Para calcular el **[[Tiempo Promedio de Espera]]**, debes contar obligatoriamente a los clientes que llegan con las cajas vacías y pasan directo. **Por qué importa:** Aunque su espera sea $0$, se suma un cliente más al contador (denominador). "Si yo no lo ignoro y no lo cuento, el promedio de tiempo de espera me va a dar más alto de lo que en realidad fue".

> [!danger] TRAMPA 3: Desorden en la [[Cola]] Múltiple El orden de llegada al sistema **NO ES** el orden de llegada a las cajas. Un cliente que llegó antes puede demorarse actualizando su resumen, mientras que uno que llegó después puede ir directo a pagar. **Solución Obligatoria:** Todos los clientes necesitan un atributo llamado `[[Hora de inicio de espera]]`. Cuando una caja se libere, debe atender al cliente que tenga la hora registrada más baja (el más antiguo), sin importar su número de ID de entidad.

> [!danger] TRAMPA 4: No especificar el [[Servidor]] en uso Cuando hay servidores paralelos (Caja 1 y Caja 2), no puedes poner que el cliente está simplemente "Pagando". **Solución:** Debes anotar en qué caja exacta está (ej. `PR2` o "Pagando en Caja 2"). Si no lo haces, cuando ocurra el evento `Fin Pago Sub 2`, no sabrás a qué cliente de la tabla debes destruir.

---

## 4. Preguntas Relevantes de los Alumnos en Clase

El debate más interesante surgió respecto a la redacción del parcial y los criterios de evaluación:

> [!question] ¿El "tiempo de espera" incluye el tiempo que demoran en cobrarme? **Alumno (Agustín / Ariel):** Plantearon que la redacción ("espera en las cajas") daba a entender que incluía el tiempo de servicio, y que muchos respondieron así. **Respuesta del Profesor:** Aclaró que a nivel estadístico de simulación, el [[Tiempo de Espera]] es **únicamente el lapso que estás en la cola**, finalizando en el instante exacto en que pasas a ser atendido. Prometió avisar a los otros profesores para que tengan piedad al corregir esto si la redacción fue ambigua.

> [!question] Si veo la ventanilla llena y me voy, ¿cuento como "Cliente que se retira sin pagar"? **Alumno:** Preguntó si un cliente que llega a la ventanilla de actualización, la ve llena y se va del sistema (destruyéndose) se debe sumar al contador del inciso B ("Clientes que se retiran sin pagar"). **Respuesta del Profesor:** El profesor argumentó que **no se debe contar**, porque al ser rechazado en la primera etapa, es imposible saber si ese cliente, de haberse quedado a actualizar, hubiera caído en el 33% que se va o en el 67% que sí paga. "Es adelantarme a los hechos". Sin embargo, admitió que el enunciado no era 100% claro y aceptará ambas interpretaciones como válidas.

> [!tip] Tip de Gestión de Parcial: Reutilización de Series RND El profesor remarcó que las series aleatorias que provee el examen **deben respetarse**. Si decides usar el Renglón 1 para Llegadas y el Renglón 2 para Actualizaciones, debes mantener ese orden. No puedes cruzar números de distintas filas. Si te quedas sin números, debes seguir en el renglón que indique el enunciado.