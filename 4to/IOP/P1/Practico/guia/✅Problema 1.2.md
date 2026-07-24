Industrias Veidile provee de máquinas y motores de alto rendimiento a diferentes
fábricas automotrices de la región centro de nuestro país. Actualmente, ==fabrica dos
tipos de motores: M1 y M2==. Un estudio detallado de costos y precios ha permitido
calcular que se obtiene una ==utilidad de $ 100 por cada unidad del primero y $ 120
por cada una del segundo==. Además, debe considerarse que, durante la fabricación de
estos motores, los recursos principales son las ==horas de proceso de maquinado,
armado y montaje requeridas por cada unidad==. Dispone semanalmente de ==480, 600
y 540 hs de cada proceso respectivamente==. Para fabricar un motor ==M1 se necesitan
4 hs de maquinado, 5 de armado y 12 de montaje==. Por otro lado, un motor ==M2
requerirá 8 hs de maquinado, 6 de armado y 8 de montaje==. Considerando una
demanda creciente e insatisfecha de sus productos, puede asumir que todo lo que
produzca será vendido. Por ello, hasta tener la posibilidad de ampliar la planta, un
plan de producción ineficiente significaría un costo de oportunidad importante.

U2
a) Formule el objetivo de la gerencia respecto a este problema.
b) Describa las variables de decisión.
c) Plantee un programa lineal que optimice las utilidades.

---
d) Proponga una solución no factible y justifique por que debería ser descartada.
e) Proponga dos soluciones factibles y descríbalas, indicando el valor de las variables
y la utilidad total obtenida.
f) Resuelva el programa lineal a fin de obtener la solución óptima.
g) Compare las soluciones obtenidas en el punto e) con la solución óptima obtenida
en el punto f.
h) ¿Existe alguna solución degenerada en el problema?
i) Realice la combinación lineal convexa entre la solución óptima y una de las
soluciones del punto e).

---
# u2

a) Formule el objetivo de la gerencia respecto a este problema.
	Maximizar la Utilidad Total semanal por la producción y venta de motores tipo M1 y M2

>[!danger] Trampa de Examen (Objetivo Físico vs. Económico) Es un error común indicar que el objetivo es "maximizar la producción". La profesora advirtió que no es lo mismo maximizar la suma de unidades físicas que maximizar la utilidad, ya que cada motor aporta un valor monetario diferente ($100 vs $120). Al tener datos de costos e ingresos, el objetivo real siempre es económico.


b) Describa las variables de decisión. 
	*  x1 = unidades de Motores tipo 1 a fabricar semanalmente y
	* x2 = unidades de Motores tipo 2 a fabricar semanalmente
	* o
	* xj = unidades de Motores tipo j a fabricar semanalmente para j =1, 2
	
>[!note] Las variables representan las incógnitas que el modelo matemático debe determinar para alcanzar el objetivo. Para que estén correctamente definidas según los criterios de la cátedra, deben poseer una anatomía estricta de tres partes: unidad de medida, ítem/acción y período de tiempo

>[!danger] Trampa de Parcial (El uso de la palabra "Cantidad") Jamás definas la variable como "Cantidad de motores M1". La cátedra penaliza este error conceptual porque _"cantidad no es una unidad a la cual está medida"_ y vuelve difusa a la variable. Usa siempre la métrica exacta: **Unidades**.

c) Plantee un programa lineal que optimice las utilidades.
	max z = 100 x1 + 120 x2
	s.a
	 4x1+8x2<= 480 (hs proceso de maquinado)
	 5x1​+6x2​≤600(Horas de Armado)
	 12x1+8x2<= 540 (hs de montaje)
	 x1;x2>=0 (NO NEGATIVIDAD)


>[!question]- De acuerdo con la restricción de No Negatividad, los valores de las variables de todo programa lineal deben ser positivas.?
>
>Falso
>
>No negatividad esta incluido el cero, por lo tanto esa es una variable no positiva

>[!tip] Tip Metodológico (El "Tachado") Al multiplicar el requerimiento de 4 Horas/Unidad por la variable medida en Unidades, la palabra "Unidades" se simplifica (se tacha) y el término resultante queda puramente en **Horas**. Esto coincide perfectamente con el límite derecho de 480 Horas, validando matemáticamente tu inecuación

![[{1C3E7E5F-3166-4AA9-BC3C-0B51B074E2CA}.png|505]]
![[Pasted image 20260615164101.png|504]]


# PREGUNTAS EN LA UV DE ESTE PROBLEMA
### ¿Cuál de las siguientes afirmaciones representa al objetivo del problema?
- [ ] Maximizar el Ingreso Total anual por la elaboración de los productos
- [ ] Maximizar la Utilidad Total semanal por la producción y venta de motores M1 y M2 
- [ ] Minimizar el uso de los recursos
- [ ] Maximizar la producción semanal de motores M1 y M2
- [ ] Maximizar el Ingreso Total por la producción y venta semanal de motores M1 y M2
#### rta
Maximizar la Utilidad Total semanal por la producción y venta de motores M1 y M2
###  Las variables pueden definirse como:
- [ ] xj = unidades de Motores tipo j a fabricar semanalmente para j =1, 2
- [ ] xi = Motor tipo Mi
- [ ] x1 = Motores  M1 y x2 = Motores M2
- [ ] x1 = unidades de Motores tipo 1 a fabricar semanalmente y x2 = unidades de Motores tipo 2 a fabricar semanalmente
- [ ] xi = Motores tipo  i a fabricar semanalmente
- [ ] x1 = Motores tipo 1 a fabricar semanalmente y x2 = Motores tipo 2 a fabricar semanalmente
- [ ] x1 = cantidad de Motores tipo 1 a fabricar semanalmente y x2 = cantidad de Motores tipo 2 a fabricar semanalmente
#### rta
x1 = unidades de Motores tipo 1 a fabricar semanalmente y

x2 = unidades de Motores tipo 2 a fabricar semanalmente

xj = unidades de Motores tipo j a fabricar semanalmente para j =1, 2icar semanalmente para j =1, 2


### ¿Cuál/cuáles de las siguientes afirmaciones corresponden a restricciones del problema?
- [ ] Se deben utilizar 480 hs de maquinado
- [ ] Se deben utilizar al menos 540 hs de montaje
- [ ] Se pueden utilizar no más de 480 hs de maquinado
- [ ] Como máximo se pueden utilizar 540 hs de montaje
- [ ] Se pueden utilizar hasta de 600 hs de armado
- [ ] Se pueden utilizar como mínimo 600 hs de armado
#### rta
Se pueden utilizar hasta de 600 hs de armado
Como máximo se pueden utilizar 540 hs de montaje

Se pueden utilizar no más de 480 hs de maquinado

### Si x1 y x2 representan a las variables del problema entonces, matemáticamente el objetivo del problema se escribe como:
- [ ] max 100 M1 + 120 M2  
- [ ] min 100 x1 + 120 x2
- [ ] min 480 (x1 + x2) + 540 (x1 + x2) + 600 (x1 + x2)
- [ ] max 100 x1 + 120 x2
- [ ] max 100 (7) x1 + 120 (7) x2
- [ ] max 100 (7) M1 + 120 (7) M2
#### rta
max 100 x1 + 120 x2

### ¿Cuál/Cuáles de las siguientes funciones representan restricciones del problema?
- [ ] 4 x1 + 8 x2 ≤ 480
- [ ] 6 M1 + 5 M2≤ 600
- [ ] 4 x1 + 8 x2 = 480
- [ ] 12 x1 + 8 x2 ≤ 540
- [ ] 12 x1 + 8 x2≥540
- [ ] 4 x1 + 8 x2  ≥ 480
- [ ] 5 x1 + 6 x2 = 600
#### rta
4 x1 + 8 x2 ≤ 480
12 x1 + 8 x2 ≤ 540

### De acuerdo con la restricción de No Negatividad, los valores de las variables de todo programa lineal deben ser positivas.
true 
false
#### rta
FALSO

### El modelo de programación lineal del problema analizado queda formulado en forma: __ y ___

explicita y canonica