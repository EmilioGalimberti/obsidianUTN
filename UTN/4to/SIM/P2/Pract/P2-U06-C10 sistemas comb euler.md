¡Hola! Como tu Tutor Académico de Élite, he analizado detalladamente la nueva transcripción. Esta clase es un punto de inflexión fundamental, ya que introduce la **[[Simulación Combinada]]**, donde los clásicos sistemas de eventos discretos se mezclan con variables continuas que deben resolverse mediante ecuaciones diferenciales y el método de **[[Integración de Euler]]** (como el cadete que recorre distancias o los alumnos que escriben líneas de código).

A continuación, te presento la estructura definitiva de resolución, las fórmulas y las trampas críticas en las que el profesor hizo mayor énfasis para no reprobar.

# Guía Avanzada: Resolución de [[Sistemas Combinados]] (Discreto + Continuo)

## 1. Estructura de Resolución y Planteo Previo

En estos ejercicios, el tiempo de los eventos no sale directamente de una fórmula estadística simple, sino que depende de **cuánto tiempo le toma a una variable continua alcanzar un objetivo** (ej. llegar a 400 líneas de código o recorrer 162 metros).

### A. Construcción del Modelo Dual

Debes manejar dos espacios de trabajo simultáneos en tu Excel:

1. **El [[Vector de Estado]]:** La grilla principal que ya conoces, donde avanza el [[Reloj del Sistema]].
2. **Las Tablas de [[Integración de Euler]]:** Mini-tablas auxiliares ubicadas a un costado donde calculas numéricamente el avance de la variable continua renglón a renglón hasta superar el valor objetivo.

|Tipo de Tabla Euler|Cuándo utilizarla (Estructura Estratégica)|Conceptos Clave|
|:--|:--|:--|
|**[[Tabla Estática]]**|Cuando la ecuación diferencial es la misma para todas las entidades (ej. la velocidad de la moto del cadete). Haces la tabla una sola vez, la extiendes hasta el límite máximo posible, y la usas como consulta para todos los clientes.|[[Ecuación Diferencial Constante]]|
|**[[Tabla Dinámica]]**|Cuando la velocidad o tasa cambia por cada entidad (ej. cada alumno tiene un factor $k$ de velocidad de programación distinto). Creas una celda de referencia para $k$. Cada vez que llega un alumno nuevo, cambias el $k$, la tabla se recalcula sola, y anotas el resultado a mano.|[[Reutilización de Tabla]], [[Variable Paramétrica]]|

### B. Flujo Lógico de un Evento Combinado

```
graph TD
    A[Ocurre Evento: Inicia Tarea Continua] --> B[Obtener Atributos de la Entidad]
    B --> C[Ir a Tabla de Euler correspondiente]
    C --> D[Iterar h hasta superar el Valor Objetivo]
    D --> E[Obtener el valor de Tiempo de Integracion]
    E --> F[CONVERTIR unidad de integracion a unidad del Reloj]
    F --> G[Sumar al Reloj Actual y generar Evento Futuro]
```

_(Conceptos relacionados: [[Paso de Integración ($h$)]], [[Equivalencia de Tiempo]], [[Valor Objetivo]])_

---

## 2. Fórmulas Matemáticas Críticas

Además de los clásicos generadores uniformes y exponenciales, aquí es obligatorio aplicar la fórmula de Euler de primer orden en tus tablas auxiliares.

> [!note] Fórmulas Base: [[Integración Numérica de Euler]] Para avanzar cada renglón en tu mini-tabla, usas el [[Paso de Integración ($h$)]]:
> 
> **Próximo valor del Tiempo ($t_{i+1}$):** $$ t_{i+1} = t_{actual} + h $$
> 
> **Próximo valor de la Variable de Estado ($y_{i+1}$):** $$ y_{i+1} = y_{actual} + h \cdot y'_{actual} $$ *(Donde $y'_{actual}$ es el resultado de la ecuación diferencial evaluada en ese instante)*.

> [!note] Fórmula Obligatoria: [[Equivalencia de Tiempo]] Si el enunciado dice que $1$ unidad de integración equivale a $10$ minutos en el sistema real: $$ Tiempo_Vector = Tiempo_Euler \times Factor_Equivalencia $$ _(Ej. Si Euler indica $0.4$, el tiempo real es $0.4 \times 10 = 4$ minutos)_.

---

## 3. Tips de Parcial (Atajos y Metodología)

El profesor regaló varias metodologías "de oro" para ahorrar tiempo valioso en el Excel durante el parcial:

> [!tip] Tip de Parcial: El criterio para definir el tamaño de $h$ Si el enunciado no te da el valor del [[Paso de Integración ($h$)]], ¿cuál eliges? **Regla del Profesor:** Inicia con $h = 0.1$. Si al superar el objetivo (ej. 400 líneas) te pasaste de largo por un valor muy grande, **achica el $h$ (ej. a $0.01$)**. El objetivo de excelencia es que el error o "pasada de largo" sea **menor al $2%$ del valor objetivo** (ej. para 400, no pasarte de 408). Como Excel hace el cálculo arrastrando celdas, no te cuesta nada hacer 140 líneas en lugar de 14.

> [!tip] Tip Metodológico: Generar en el momento exacto (Ahorro de columnas) En el caso del cadete, ¿cuándo saco el número aleatorio de la distancia del domicilio? ¿Cuando el cliente llama o cuando el cadete sale? **Respuesta Oficial:** Genera la distancia **justo en el instante en que el cadete está por salir**. Si lo haces cuando el cliente llama, estarás obligado a crear una nueva columna de [[Atributo]] para guardar ese valor en la memoria del vector durante varios renglones hasta que llegue el cadete. Generarlo "Just-in-Time" ahorra columnas críticas.

> [!tip] Tip Metodológico: Apagar llegadas sin usar eventos Si el negocio cierra a las 18:45 (minuto 60 de simulación), no gastes una columna entera creando un evento `Fin_Llegadas`. Simplemente avanza normalmente y, en el instante en que generes una `Próxima Llegada` que resulte ser **mayor a 60**, la tachas, dejas la celda en blanco y no generas más.

---

## 4. 🚨 Trampas Mortales y Errores a "Tener Cuidado"

El profesor detuvo la clase específicamente para remarcar que los siguientes errores descuentan muchísimos puntos en los finales y parciales:

> [!danger] TRAMPA MORTAL 1: Fallar en la [[Equivalencia de Tiempo]] **"Es un error que se suele presentar en los parciales finales y es algo que baja muchos puntos."** **El error:** Tu tabla de Euler dice que superaste el objetivo en $t = 1.5$. Agarras ese $1.5$ y lo sumas directamente al reloj de tu vector de estado. **La realidad:** El enunciado suele indicar (como en el Ejercicio de los Alumnos) que $1$ unidad de integración de Euler = $1$ Hora. Si tu reloj general está en Minutos, sumar $1.5$ significa sumar "1 minuto y medio", cuando en realidad debías multiplicar $1.5 \times 60 = 90$ minutos. **NUNCA bajes el valor de Euler crudo al vector sin verificar la unidad.**.

> [!danger] TRAMPA MORTAL 2: Equivocarse en las [[Condiciones Iniciales]] No asumas automáticamente que las variables de Euler arrancan en 0.
> 
> - En el Cadete, la distancia inicial ($D_0$) era $0$ porque recién salía de la empresa.
> - En el Alumno Programador, las líneas de código iniciales ($L_0$) eran **$50$**, porque el enunciado decía que arrancaba con un proyecto ya empezado. Si ponías un 0 en el $y_{actual}$ inicial de tu tabla de Euler, la ecuación diferencial ($k \cdot L$) daba permanentemente 0 y la simulación colapsaba por completo.

> [!danger] TRAMPA TEÓRICA: Predecir el futuro (Cancelar eventos antes de tiempo) Al calcular el tiempo que un alumno demora en programar, te das cuenta de que va a terminar a las 19:45, pero el examen cierra 19:30. **Error gravísimo:** Como sabes que no va a llegar, decides tachar su evento de inmediato. **Regla de Oro:** **No puedes cancelar eventos de antemano basándote en el futuro.** El evento de `[[Fin de Programación]]` debe quedar activo en el Excel. Recién en la línea de tiempo donde ocurre el evento maestro absoluto (`[[Fin de Examen]]` a las 19:30), bajas ese valor al reloj y es **ahí mismo** donde debes tachar y destruir los eventos que no alcanzaron a concretarse. "No sería como anticiparse a lo que suceda... está mal".