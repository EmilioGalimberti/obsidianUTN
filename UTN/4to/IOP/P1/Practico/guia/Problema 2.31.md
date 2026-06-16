Problema 2.31
Fruits SA, produce jugos concentrados de frutos rojos como arándanos, frutillas
frambuesas, moras, etc. En este momento está preparando la producción de
concentrado de arándanos y frambuesas.
Para la elaboración de estos concentrados utiliza una máquina destiladora especial
que puede trabajar 30 hs a la semana. Una vez procesada la fruta y obtenido el
concentrado, este se almacena en dos tanques de enfriamiento con una capacidad
de 650 lts cada uno y posteriormente se fracciona y congela.
La máquina destiladora tiene capacidad para procesar 60 lt. de pulpa de arándanos
por hora, pero sólo 50 lt. de pulpa de frambuesas. El costo del lt. de pulpa de
arándanos es de $12 y debido a que se pierde el 35% del agua al destilarse, se vende
a $50. En tanto que, en el caso de la frambuesa, el costo es de $15 y se comercializa
a $45, ya que se pierde el 25 % en el proceso de destilación.


a) Formule un modelo de programación lineal para determinar el número de litros
de pulpa de frutas que deberán destilarse semanalmente para maximizar el
beneficio total.
b) Resuelva gráficamente.
c) Resuelva utilizando algún software.
d) Escriba un informe para Fruits SA, indicando la solución óptima y toda otra
información que crea conveniente

---
4. Desafío Productivo Complejo: Problema "Fruits SA" (58:44 - 1:24:10)

Se plantea un problema de destilación de jugos concentrados (Arándanos y Frambuesas) no incluido en la guía oficial, con el fin de evaluar procesos con pérdida de materia prima (mermas).

- **Punto Crítico 1: Selección de las Variables** La profesora explicó que en procesos con transformaciones físicas, las [[Variables de Decisión]] pueden definirse de dos maneras válidas:
    1. _Como Input:_ "Litros de pulpa a procesar".
    2. _Como Output:_ "Litros de concentrado a producir". _Decisión:_ Se optó por formular desde el _Input_ (x1​, x2​), aplicando los factores de pérdida (rendimiento del 65% y 75%) en el cálculo de la función objetivo y en las restricciones de los tanques.
- **Punto Crítico 2: Velocidad de la Máquina vs. Horas Disponibles** El dato indicaba procesamiento de 60 litros/hora, pero el límite semanal de la máquina era de 30 horas.

[!tip] Metodología de Formulación (Inversión de Tasas) Cuando el límite del lado derecho (Recurso Disponible) está en horas, los coeficientes tecnológicos que acompañan a las variables de producción deben obligatoriamente expresarse en **horas por unidad**. Para ello, se invierte la tasa de velocidad (1 / Velocidad). _Ejemplo Fruits SA:_ En lugar de usar 60, se usa 1/60 (horas que tarda en procesar un litro).

---
3. Modelado de Procesos Productivos con [[Mermas]] y Conversión de Tasas

El problema adicional **"Fruits SA" (Concentrado de Jugos)** introdujo dos conceptos avanzados de producción real que no estaban en los problemas anteriores.

- **Pérdida de Material (Rendimiento):** Al destilar la pulpa, se evaporaba agua (35% en arándanos y 25% en frambuesas). La profesora explicó que las variables podían definirse como el _input_ (litros de pulpa a procesar) o el _output_ (litros de jugo a producir). Al elegir el _input_, se debió multiplicar la variable por su tasa de rendimiento (0.65 y 0.75 respectivamente) en la [[Función Objetivo]] para reflejar el volumen real vendido.
- **Inversión de Velocidades:** La máquina procesaba a una velocidad de 60 litros/hora, pero el límite disponible estaba en horas (30 horas).

[!tip] Metodología Clave: Inversión de Tasas Si el [[Lado Derecho]] de tu restricción está en "Horas", los coeficientes de las variables deben ser "Horas por unidad". Para lograrlo, debes invertir la velocidad de procesamiento: si procesa 60 litros por hora, demora 1/60 horas por litro. La restricción queda: 601​x1​+501​x2​≤30.

---
[!question] Pregunta 4: Transformación de Tasas de Procesamiento **Alumno:** En el problema de la destiladora de jugos, el alumno no sabía cómo relacionar la restricción de "30 horas totales" disponibles con el dato de que la máquina procesa "60 litros por hora" de pulpa. **Respuesta de la Profesora:** Introdujo el concepto de **inversión de la velocidad de procesamiento**. Como las variables están definidas en "litros de pulpa" y el límite está en "horas", se requiere calcular _"cuántas horas demora por litro"_. Un alumno dedujo correctamente que es la inversa: si procesa 60 litros en 1 hora, demora 1/60 horas por litro. Así, la ecuación correcta fue formulada como 601​x1​+501​x2​≤30.


[!question] Pregunta 5: Temporalidad en las Restricciones de Capacidad **Alumno:** En un cuestionario del aula virtual, surgió la duda de si la capacidad de los tanques de 650 litros era reutilizable o era un límite estricto temporal. **Respuesta de la Profesora:** Instruyó a los alumnos a analizar el "período de análisis" del sistema completo. Dado que la máquina destiladora trabaja bajo una restricción de "30 horas semanales", todo el lote de producción y la capacidad de almacenamiento (650 litros) se evalúa como una limitación _semanal_.