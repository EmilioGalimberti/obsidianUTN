¡Hola de nuevo! Como tu Tutor Académico de Élite, he analizado la última transcripción. Esta clase marca un salto importante en la complejidad del modelado, introduciendo **múltiples objetos temporales interactuando al mismo tiempo**, **servidores de capacidad infinita** y **colas con prioridad de atención**.

A continuación, te presento la guía estructural definitiva, las fórmulas, y las advertencias críticas ("trampas") en las que el profesor hizo especial énfasis.

# Guía de Resolución Avanzada: Sistemas Complejos y Múltiples Entidades

## 1. El Planteo Previo: Anatomía del Nuevo [[Vector de Estado]]

Cuando el sistema deja de ser una simple "línea de espera", debes modificar cómo estructuras tus columnas.

- **Separación de [[Objetos Temporarios]]:** Si una entidad genera a otra (ej. un Cliente compra y genera un Artículo, o una Persona deja un Aviso), **no debes agruparlos en la misma sección de columnas**. Como tienen ciclos de vida diferentes y la relación no siempre es 1 a 1 (un cliente puede generar 2 avisos), debes armar un bloque de columnas para "Clientes" y otro bloque totalmente separado para "Artículos/Avisos".
- **Columnas de [[Eventos Sub i]]:** El subíndice no se usa solo cuando hay varios empleados. Se utiliza para representar la **capacidad de procesamiento simultáneo**. Por ejemplo, si el furgón puede repartir 4 paquetes a la vez, debes crear 4 columnas de `Fin_Reparto_sub_i`. Si un sistema informático procesa infinitos avisos, debes crear múltiples columnas de `Fin_Clasificación_sub_i`.
- **Gestión de la [[Cola con Prioridad]]:** Cuando hay entidades VIP (ej. artículos al contado vs. artículos a crédito), no puedes meterlos en la misma cola. Estás obligado a crear dos columnas de espera independientes: `Cola de Contado` y `Cola de Crédito`.

## 2. Dinámica de Simulación y Flujo Lógico

El motor lógico para procesar prioridades múltiples (como el ejercicio del furgón de reparto) sigue este esquema algorítmico:

```
graph TD
    A[Llega el Furgon a la Base] --> B{¿Hay articulos en Cola Contado?}
    B -- SI --> C[Cargar articulos al Contado hasta llenar cupo]
    B -- NO --> D{¿Hay 4 o mas articulos en Cola Credito?}
    D -- SI --> E[Cargar 4 articulos a Credito]
    D -- NO --> F[Furgon queda Libre en la base]
    C --> G[Pasar estado a Siendo Repartido]
    E --> G
    G --> H[Generar eventos Fin Reparto Sub i para CADA UNO]
```

_Conceptos relacionados al gráfico:_ `[[Servidor]]`, `[[Prioridad de Atención]]`, `[[Iteración de Simulación]]`.

> [!question] Pregunta Lógica de Simulación **Profesor:** Si tengo 5 artículos al contado esperando, y el furgón solo puede llevar 4, ¿cuáles elijo para cargar? **Respuesta del Profesor:** Debes elegir estrictamente los 4 que tengan la `[[Hora de Creación]]` más baja. Es decir, te basas en el atributo de antigüedad para respetar el orden lógico de llegada.

## 3. Fórmulas Matemáticas Requeridas

Las fórmulas para generar eventos siguen siendo las clásicas, pero debes estar atento a qué variable te pide el enunciado:

> [!note] Fórmulas Generadoras de Variables Aleatorias **[[Distribución Uniforme]]** (Usada para tiempos de atención y llegadas en el Ejercicio 16): $$X = A + RND \times (B - A)$$
> 
> **[[Distribución Exponencial Negativa]]** (Usada para llegadas en el Ejercicio 24 de los avisos): $$X = -Media \times \ln(1 - RND)$$

---

## 4. 🚨 Advertencias Críticas y "Trampas" de Parcial

El profesor dedicó gran parte de la clase a explicar errores letales que anulan el ejercicio completo:

> [!danger] TRAMPA MORTAL 1: Agrupar Tiempos de Procesamiento Si un furgón sale a entregar 4 paquetes y cada uno demora 10 minutos, **el instinto es multiplicar $10 \times 4 = 40$ y crear un solo evento de 40 minutos. ESTO ES UN ERROR GRAVE**. El profesor explicó dos motivos:
> 
> 1. Si el tiempo fuera una distribución estadística (ej. uniforme), agrupar matemáticamente destruye la aleatoriedad. Debes calcular la fórmula independientemente para cada paquete.
> 2. Las estadísticas exigen conocer el tiempo promedio de entrega. Si agrupas todo en 40 minutos, no sabrás la hora exacta en que se entregó el primer paquete ni el segundo, arruinando las `[[Medidas de Desempeño]]`. **Debes generar un evento separado para cada artículo.**

> [!danger] TRAMPA MORTAL 2: Inventar el "Evento Fantasma" En el ejercicio de los avisos, el cliente va a la caja a pagar. La trampa es intentar crear un evento llamado "Fin de Pago en Caja". **Regla de Oro:** Si el enunciado **no te da el tiempo ni la distribución estadística** que demora una actividad, **no puedes simularla**. Como no sabes cuánto demora en pagar, simplemente acumulas el dinero de forma instantánea en el momento en que se recepciona el aviso, sin crear ningún evento futuro.

> [!danger] TRAMPA TEÓRICA: El [[Servidor de Capacidad Infinita]] En el caso del sistema informático que clasifica avisos de forma ilimitada, **no existe la cola**. Cualquier aviso que llega pasa inmediatamente al estado `[[Siendo Clasificado]]`. El servidor siempre está en estado `Disponible`, por lo que el profesor indica que ni siquiera hace falta crearle una columna de estado en el Excel.

---

## 5. Tips de Metodología de Parcial

Finalmente, el profesor dejó recomendaciones técnicas para armar el Excel en el examen:

> [!tip] Tip de Excel: La [[Reutilización de Columnas]] (Búfer) Para simular el servidor de capacidad infinita, no puedes dibujar infinitas columnas de eventos. El profe recomienda armar unas 10 o 15 columnas `Fin_Clasificación_sub_i`. A medida que un aviso termina, su columna queda vacía; puedes reutilizarla como si fuera un "búfer circular" para meter los tiempos de los nuevos avisos que van llegando, sin necesidad de alargar el Excel infinitamente hacia la derecha.

> [!tip] Tip de Logística: RNDs Pre-cargados Los alumnos se quejaron de que en el primer parcial perdieron muchísimo tiempo copiando los números aleatorios. El profesor confirmó que para el próximo examen considerarán **entregar un archivo adjunto con los valores aleatorios ya cargados** en celdas, para que solo tengan que referenciarlos y evaluar puramente su velocidad de razonamiento lógico.