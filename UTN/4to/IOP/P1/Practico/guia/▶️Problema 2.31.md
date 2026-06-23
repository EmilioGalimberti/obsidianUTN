Problema 2.31
Fruits SA, produce jugos concentrados de frutos rojos como arándanos, frutillas
frambuesas, moras, etc. En este momento está preparando la producción de
concentrado de ==arándanos y frambuesas==.
Para la elaboración de estos concentrados utiliza una ==máquina destiladora especial
que puede trabajar 30 hs a la semana==. Una vez procesada la fruta y obtenido el
concentrado, este se almacena en ==dos tanques de enfriamiento con una capacidad
de 650 lts cada uno== y posteriormente se fracciona y congela.
La ==máquina destiladora tiene capacidad para procesar 60 lt. de pulpa de arándanos==
por hora, ==pero sólo 50 lt. de pulpa de frambuesas==. El ==costo del lt. de pulpa de
arándanos es de $12== y debido a que se pierde el 35% del agua al destilarse, ==se vende
a $50==. En tanto que, en el caso de la ==frambuesa, el costo es de $15== y se comercializa
a ==$45==, ya que se pierde el 25 % en el proceso de destilación.


a) Formule un modelo de programación lineal para determinar el número de litros de pulpa de frutas que deberán destilarse semanalmente para maximizar el beneficio total.
b) Resuelva gráficamente.
c) Resuelva utilizando algún software.
d) Escriba un informe para Fruits SA, indicando la solución óptima y toda otra
información que crea conveniente

---

# a) 4. Desafío Productivo Complejo: Problema "Fruits SA" (58:44 - 1:24:10)
![[{39554C17-6C30-4E47-865F-D6D3DD61E80E}.png]]

==objetivo:== 
Maximizar el Beneficio Total semanal


==def de variables:==
x_i = litros de pulpa tipo i a procesar  

x1= litros de pulpa de arandanos a destilar por semana
x2= litros de pulpa de frambuesa a destilar por semana

---
- **Punto Crítico 1: Selección de las Variables** La profesora explicó que en procesos con transformaciones físicas, las [[Variables de Decisión]] pueden definirse de dos maneras válidas:
    1. _Como Input:_ "Litros de pulpa a procesar".
    2. _Como Output:_ "Litros de concentrado a producir". deberias aplicar los factores de pérdida (rendimiento del 65% y 75%) en el cálculo de la función objetivo y en las restricciones de los tanques.
---
==RESTRICCIONES
* como maximo 650 LTS X1
* como maximo 650 LTS X2


y para la restricicon de la maquina que dice
Maquina destiladora dispone de 30 horas semanales, y puede procesa 60 lits  pulpa de arandanos por hora y 50 litrs de pulpa de frambues por hora
* nos quedaria asi: 1/60 x1​+1/50 ​x2​≤30.

**Punto Crítico 2: Velocidad de la Máquina vs. Horas Disponibles** El dato indicaba procesamiento de 60 litros/hora, pero el límite semanal de la máquina era de 30 horas.

>[!tip] Metodología de Formulación (Inversión de Tasas) Cuando el límite del lado derecho (Recurso Disponible) está en horas, los coeficientes tecnológicos que acompañan a las variables de producción deben obligatoriamente expresarse en **horas por unidad**. Para ello, se invierte la tasa de velocidad (1 / Velocidad). _Ejemplo Fruits SA:_ En lugar de usar 60, se usa 1/60 (horas que tarda en procesar un litro).
>La restricción queda:1/60 x1​+1/50 ​x2​≤30.

---
>[!question] Pregunta 4: Transformación de Tasas de Procesamiento **Alumno:** En el problema de la destiladora de jugos, el alumno no sabía cómo relacionar la restricción de "30 horas totales" disponibles con el dato de que la máquina procesa "60 litros por hora" de pulpa. **Respuesta de la Profesora:** Introdujo el concepto de **inversión de la velocidad de procesamiento**. Como las variables están definidas en "litros de pulpa" y el límite está en "horas", se requiere calcular _"cuántas horas demora por litro"_. Un alumno dedujo correctamente que es la inversa: si procesa 60 litros en 1 hora, demora 1/60 horas por litro. Así, la ecuación correcta fue formulada como 601​x1​+501​x2​≤30.


>[!question] Pregunta 5: Temporalidad en las Restricciones de Capacidad **Alumno:** En un cuestionario del aula virtual, surgió la duda de si la capacidad de los tanques de 650 litros era reutilizable o era un límite estricto temporal. **Respuesta de la Profesora:** Instruyó a los alumnos a analizar el "período de análisis" del sistema completo. Dado que la máquina destiladora trabaja bajo una restricción de "30 horas semanales", todo el lote de producción y la capacidad de almacenamiento (650 litros) se evalúa como una limitación _semanal_.

---

planteo pl

contribucion total: 

(BENEFICIO) x1 -> (0,65 RENDIMIENTO)* 50(Precio) * X1 - 12(COSTO) * X1
(BENEFICIO) x1=20,5 x1

(BENEFICIO) x2 -> (0,75 RENDIMIENTO)* 45(Precio) * X2 - 15(COSTO) * X2
(BENEFICIO) x2=18,75 x2

y ahora si:
max z= 20,5 * x1+18,75 * x2

S.A
0,65x1<= 650 (lts capacidad tanque)  
0,75 x2 <= 650 (lts capacidad tanque)
1/60 x1​+1/50 ​x2​≤30. (hs. maq destiladora)
x1;x2 >= 0

![[{64941307-7DD7-4C20-ADCF-CB502B4A262D}.png]]
# Preguntas UV

### ¿Cuál de las siguientes afirmaciones representa al objetivo del problema?
- [ ] a. Maximizar Ingresos Totales
- [ ] b. Maximizar el Beneficio Total semanal
- [ ] c. Minimizar los costos de la fabricación semanal de los productos
- [ ] d.Minimizar el desperdicio de los recursos
- [ ] e. Maximizar la producción semanal de los concentrados de fruta
- [ ] f. Minimizar el uso de los recursos
#### rta
Maximizar el Beneficio Total semanal

### Las variables pueden definirse como:
- [ ] a. x1 = litros de concentrado de arándonos a producir semanalmente
      x2 = litros de concentrado de frambuesa a producir semanalmente
- [ ] b. x1 = pulpa de arándonos a destilar semanalmente y x2 = pulpa de frambuesa a destilar semanalmente
- [ ] c. xi = unidades de la pulpa i a destilar semanalmente
- [ ] d. xi = pulpa de fruta i a destilar
- [ ] e. xi = pulpa de fruta i
- [ ] f. x1 = litros de pulpa de arándonos a destilar semanalmente
      x2 = litros de pulpa de frambuesa a destilar semanalmente
- [ ] g. x1 = arándonos
      x2 = frambuesa

#### rta
Las respuestas correctas son: 
x1 = litros de pulpa de arándonos a destilar semanalmente  
x2 = litros de pulpa de frambuesa a destilar semanalmente, 

x1 = litros de concentrado de arándonos a producir semanalmente  
x2 = litros de concentrado de frambuesa a producir semanalmente

### ¿Cuál/cuáles de las siguientes afirmaciones corresponden a restricciones del problema?
- [ ] a. La producción de concentrado de frutas no debe superar los 1300 litros semanales
- [ ] b. La capacidad máxima de almacenamiento es de 1300 litros
- [ ] c. Se pueden producir no más de 650 litros de concentrado de arándanos por semana
- [ ] d. La producción de Pulpa de Frambuesa no debe superar los 650 litros por semana
- [ ] e. La capacidad máxima de destilado es de 30 de horas semanales
- [ ] f. Se pueden producir no más de 650 litros de concentrado de frutas
#### rta
Respuesta correcta

Las respuestas correctas son: Se pueden producir no más de 650 litros de concentrado de arándanos por semana, La capacidad máxima de destilado es de 30 de horas semanales

### Cuál/Cuáles de las siguientes funciones representan restricciones del problema
- [ ] a. 0,65  x1 ≥  650
- [ ] b. 1/60 x1 + 1/50 x2 ≤ 30
- [ ] c. 0,65 x1 + 0,75 x2 ≤ 1300
- [ ] d. 0,65  x1 = 650
- [ ] e. 0,65  x1 ≤ 650
- [ ] f. 60 x1 + 50 x2 ≤ 30
#### rta
Las respuestas correctas son: 0,65  x1 ≤ 650, 
1/60 x1 + 1/50 x2 ≤ 30