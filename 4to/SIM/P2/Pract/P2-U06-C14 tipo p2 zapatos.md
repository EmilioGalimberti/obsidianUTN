¡Hola! Como tu Tutor Académico de Élite, he analizado detalladamente la transcripción de esta última clase de simulación, la cual es una verdadera mina de oro. El profesor resolvió un modelo de parcial complejo ("El caso de los Zapatos"), que integra **[[Sistemas Secuenciales]]**, **[[Bloqueos]]** por falta de espacio, **[[Ecuaciones Diferenciales]]** (Runge-Kutta) y el temido método de **[[Box-Muller]]**.

A continuación, te presento la estructura metodológica definitiva, las fórmulas aplicadas y las peores "trampas" en las que el profesor remarcó que los alumnos suelen equivocarse.

---

# Guía de Resolución Definitiva: Sistemas Secuenciales con Bloqueos ("Caso Zapatos")

## 1. Planteo del Modelo y Diseño del [[Vector de Estado]]

En este tipo de parciales, el sistema está dividido en etapas estrictas y zonas de espera (buffers) con capacidad limitada.

### Clasificación de Servidores y Estados

|Servidor / Etapa|Características y Restricciones|Estados del Servidor|
|:--|:--|:--|
|**[[Servidor 1: Desarme]]**|Tiene una cola previa infinita.|`Libre`, `Desarmando`, `Bloqueado`|
|**[[Servidor 2: Armado]]**|Su cola previa admite **máximo 2 lugares**. Si se llena, el Servidor 1 se bloquea.|`Libre`, `Armando`, `Bloqueado`|
|**[[Servidor 3: Terminado]]**|Tiene 2 equipos con 2 lugares cada uno (capacidad de procesar 4 zapatos a la vez). **No tiene cola**. Si se llena, el Servidor 2 se bloquea.|`Libre`, `Ocupado` (por cada box)|

> [!danger] TRAMPA DE ESTADOS: "Esperando Atención" vs "Bloqueado" El profesor fue muy incisivo con el etiquetado de los estados. Si el zapato termina de ser desarmado pero la cola siguiente está llena, el zapato no está "Esperando atención" en la cola; está atrapado dentro de la máquina. El estado correcto de la entidad es **`[[Desarmado Finalizado]]`** y el servidor queda **`[[Bloqueado]]`**.

---

## 2. Diagrama Lógico de Flujo y Bloqueos

El siguiente diagrama ilustra cómo debes avanzar los objetos en tu planilla y en qué momento debes bloquear a los servidores anteriores:

```
graph TD
    A[Llegada de Zapato] --> B(Cola Infinita)
    B --> C[Servidor 1: Desarme]
    C --> D{¿Cola Armado < 2 lugares?}
    D -- SI --> E[Pasar a Cola de Armado]
    D -- NO --> F[Servidor 1 pasa a BLOQUEADO]
    E --> G[Servidor 2: Armado]
    G --> H{¿Hay lugar en Boxes de Terminado?}
    H -- SI --> I[Pasar a Servidor 3 Sub i]
    H -- NO --> J[Servidor 2 pasa a BLOQUEADO]
    I --> K[Resolucion por Ecuacion Diferencial]
    K --> L[Salida del Sistema]
```

_(Conceptos relacionados: [[Restricción de Capacidad]], [[Bloqueo en Cascada]], [[Vector de Estado]])_

---

## 3. Fórmulas Matemáticas y Generación de Variables

El parcial exigía dominar cuatro métodos distintos de generación en un solo ejercicio.

> [!danger] TRAMPA MORTAL 1: Confundir Tasa con Media El enunciado decía "Llegan a una tasa exponencial de 8 por hora". **El error letal:** Poner 8 en la fórmula. "8 por hora es un lambda, es una frecuencia... no es una media de 8 minutos". **Solución:** Calcular la inversa ($\frac{1}{\lambda}$). $60 \text{ min} / 8 = 7.5 \text{ minutos de media}$.

> [!note] Fórmulas Generadoras Aplicadas **[[Llegada al Sistema]] ([[Distribución Exponencial]]):** $$X = -7.5 \cdot \ln(1 - RND)$$
> 
> **Tiempo de Desarme ([[Distribución Uniforme]] entre 1 y 10):** $$X = 1 + RND \cdot (10 - 1)$$

> [!note] Fórmula: [[Método de Box-Muller]] (Para el Armado) El armado seguía una [[Distribución Normal]] de media 8 y desviación 5. Se usan **dos** RNDs para generar **dos** variables. **Primer Valor (Coseno):** $$N_1 = 8 + 5 \cdot \left( \sqrt{-2 \cdot \ln(RND_1)} \cdot \cos(2\pi \cdot RND_2) \right)$$ **Segundo Valor (Seno):** $$N_2 = 8 + 5 \cdot \left( \sqrt{-2 \cdot \ln(RND_1)} \cdot \sin(2\pi \cdot RND_2) \right)$$

> [!danger] TRAMPA MORTAL 2: Quemar Randoms en Box-Muller "Acá cometen el error, nunca hicimos un ejercicio con la distribución normal...". Al usar Box-Muller sacas dos números aleatorios para el primer zapato. **No los descartes**. Debes arrastrarlos y guardarlos en memoria, porque cuando llegue el _segundo_ zapato a armar, usarás esos **mismos dos números exactos** aplicados en la fórmula del Seno.

---

## 4. Tips de Metodología de Parcial

El profesor brindó estrategias para no volverse loco en Excel y ahorrar tiempo:

> [!tip] Tip de Parcial: Tablas Pre-calculadas de [[Runge-Kutta]] Para la última etapa (Terminado), el tiempo se calcula con una ecuación diferencial. Como el equipo puede tener 1 o 2 zapatos a la vez, había que usar fórmulas distintas. **Atajo del profe:** "No arman la tabla para cada zapato. Hacen una tabla sola vez para 1 zapato (da 2.9 min) y otra tabla para 2 zapatos (da 8.6 min). Luego usan esos mismos valores siempre para todo el vector".

> [!tip] Tip de Parcial: ¿Qué pasa si me quedo sin números Random? Si decides usar [[Método de Convolución]] para la Normal en lugar de Box-Muller, consumirás 12 números de golpe y te quedarás sin tabla rápido. **Solución Oficial:** "Si te quedaste sin números, reinicias la serie. Arrancas por el primer número manteniendo la secuencia. Esa regla vale para finales, parciales y para todo".

---

## 5. Preguntas Relevantes en Clase y Cosas a Evitar

> [!danger] TRAMPA DE ESTADÍSTICA: Calcular promedios a los "Zapatos Iniciales" El sistema arrancaba con 4 zapatos ya adentro. **El error:** Cuando esos 4 zapatos salen, sumar su tiempo al acumulador de `[[Tiempo Promedio de Permanencia]]`. **La Realidad:** "No los puedo incluir en esta estadística porque el enunciado no me dice a qué hora llegaron... me falta el dato de la hora de llegada. A estos cuatro los ignoro para esa estadística".

> [!question] Dudas de los Alumnos: Asumir Hora Cero **Alumno (Lucas):** "Profe, como no sabía a qué hora llegaron los iniciales, yo tomé que su hora de llegada era Cero ($0$) para poder calcularles el tiempo. ¿Está mal?" **Respuesta del Profesor:** "No estaría del todo mal... es válido porque es un defecto del enunciado no darte esos valores. En tu caso sí tienes que contarlos si les acumulaste el tiempo, pero si yo lo encuentro en el parcial, no te lo contaré como mal".

> [!question] Diferencias Matemáticas **Alumno:** "Profe, a mí la Normal con Convolución me dio 13.75 y a usted con Box-Muller le dio 4.60. ¡Hay mucha diferencia!" **Respuesta del Profesor:** "Obvio que no te van a dar igual el primer número. No te preocupes. Si vos sumaste los 12, le restaste 6, multiplicaste por la desviación y sumaste la media, está correcto. A la larga, con miles de números, los histogramas de ambos métodos tienden a ser iguales, pero individualmente son distintos".