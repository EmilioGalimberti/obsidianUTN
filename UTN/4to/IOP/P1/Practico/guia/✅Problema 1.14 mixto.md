# Enunciado
Una empresa desea planificar su producción para la próxima semana. Esta empresa produce un producto envasado en tres tamaños diferentes: ==de 120 gramos, de 200 gr. y de 360 gr==. En la bodega dispone de ==3 toneladas del producto a envasar==. 
No puede producir más de él, debido a que requiere de un proceso de cocción lento. El otro insumo para el envasado son los envases vacíos de cada tipo. Hoy se tienen ==3000 envases de 120 gr==; ==2000 de 200 gr==. y ==1500 de 360 gr==. 

La única máquina que posee la empresa trabaja ==20 horas al día== de ==lunes a viernes==; ==12 horas los sábados== y ==8 horas los domingos==. Para envasar los productos ==se requiere de 1 minuto para el envase de 120 gr==; ==2 minutos para el de 200 gr==; y ==4 minutos para el de 360 gr.==
Se tiene comprometida ==una venta de 300 unidades de envases de 200 gr a un conocido supermercado==. Cada unidad del envase de ==120 gr. genera un ingreso neto de $25==; el de ==200 gr. un ingreso neto de $50==; el de ==360 gr. un ingreso neto de $110.==

a) Formule el modelo matemático que permita realizar la planificación de producción
b) Si un proveedor le ofrece envases de 120 gr. vacíos a un precio de $1 cada uno, describa lo que haría para determinar si le conviene comprarlos o no

# a)
objetivo: Maximizar el Ingreso Total por la elaboración y venta del producto en envases de 120g, 200g y 360g para la próxima semana.

>[!danger] Trampa Teórica: Beneficio vs. Ingreso Al leer que la empresa "desea planificar su producción", el error del 90% de los alumnos es definir el objetivo como "Maximizar la producción" o "Maximizar el Beneficio". La profesora fue tajante: como el enunciado proporciona el **[[Ingreso Neto]]** ($25, $50, $110) y no detalla los costos de fabricación de la pulpa, es imposible calcular beneficios

definicion de variables:
No podemos usar la palabra "cantidad" ni "gramos a envasar", ya que los gramos son parámetros fijos del envase, no la incógnita. La empresa no fabrica los envases, solo los rellena.
- x1​: [[Unidades de envase]] de 120 gr a rellenar semanalmente.
- x2​: [[Unidades de envase]] de 200 gr a rellenar semanalmente.
- x3​: [[Unidades de envase]] de 360 gr a rellenar semanalmente.

restricciones:
	**Disponibilidad de Pulpa:** Tenemos 3 toneladas, pero los coeficientes están en gramos. 3 toneladas = 3,000,000 gramos
1. Cantidad de envases
	1. **Disponibilidad de Envases Vacíos:** El stock actual limita cuánto podemos rellenar de cada tipo.
2. Cantidad de horas que trabaja la máquina envasadora.
	1. **Capacidad de la Máquina:** Trabaja 20hs (lun-vie) + 12hs (sab) + 8hs (dom) = 120 horas semanales. Como los tiempos unitarios están en minutos, multiplicamos 120⋅60=7200 minutos de disponibilidad total
3. la venta comprometida de los envases de 200gr

>[!question] Pregunta de Examen: ¿El tiempo de envasado es una restricción? Durante la clase, muchos alumnos marcaron "1 minuto, 2 minutos, 4 minutos" como restricciones. La profesora corrigió esto: **esos son [[Parámetros]]**, no restricciones. La verdadera restricción limitante son las 120 horas totales de la máquina

max z =25 x1 + 50 x2 + 110 x3

SA
0,120x1+0,200x2+0,360x3 <= 3000 (disponibilidad de producto en kg)
1/60 x_1+2/60 x2 + 4/60 x3  <= 120   (horas maquina lunes a dominfo)
x1 <= 3000 (envases de 120 gr)
x2<= 2000 (envases de 200 gr)
x3<= 1500 (envases de 360 gr)
x2 >= 300 (300 unidades de 200gr comprometidas)

x1;x2;x3>=0 (Condicioˊn de No Negatividad)

![[{8C43A4A6-61F5-4DB8-938B-B38CD6A4E51C}.png]]

# preguntas UV
### ¿Cuál de las siguientes afirmaciones representa al objetivo del problema?
- [ ] Minimizar el uso de los recursos.
- [ ] Maximizar el Ingreso Total por la elaboración y venta del producto en envases de 120g, 200g y 360g para la próxima semana.
- [ ] Maximizar la producción en envases de 120g, 200g y 360g para la próxima semana.
- [ ] Maximizar el Ingreso Total por la elaboración del producto para la próxima semana.
- [ ] Maximizar el Beneficio Total por la elaboración y venta del producto en envases de 120g, 200g y 360g para la próxima semana.
#### rta
Maximizar el Ingreso Total por la elaboración y venta del producto en envases de 120g, 200g y 360g para la próxima semana.

### ¿Cuál/cuáles de las siguientes afirmaciones corresponden a restricciones del problema?
- [ ] Cantidad mínima de unidades de 200g a envasar.
- [ ] Cantidad de horas que trabaja la máquina envasadora.
- [ ] Demanda máxima de envases de 200g comprometida a un supermercado.
- [ ] Minutos que se requieren para envasar el producto en cada uno de los envases.
- [ ] Se pueden utilizar al menos 120 hs de máquina envasadora.
- [ ] Disponibilidad de envases vacíos de cada tipo.
- [ ] Se dispone de 3 toneladas de producto a envasar.
#### rta
- [ ] Cantidad mínima de unidades de 200g a envasar.
- [ ] Cantidad de horas que trabaja la máquina envasadora.
- [ ] Disponibilidad de envases vacíos de cada tipo.
- [ ] Se dispone de 3 toneladas de producto a envasar.




### Las variables pueden definirse como:
- [ ] X1 = gramos de producto a envasar en tamaño de 120g para la próxima semana
      X2 = gramos de producto a envasar en tamaño de 200g para la próxima semana
      X3 = gramos de producto a envasar en tamaño de 360g para la próxima semana
- [ ] X1 = unidades de envases de 120g a producir para la próxima semana
      X2 = unidades de envases de 200g a producir para la próxima semana
      X3 = unidades de envases de 360g a producir para la próxima semana
- [ ] X1 = producto de 120g a fabricar semanalmente
      X2 = producto de 200g a fabricar semanalmente
      X3 = producto de 360g a fabricar semanalmente 
- [ ] Xi = unidades del producto i a producir para la próxima semana.
- [ ] X1 = unidades del producto a producir en envases de 120g para la próxima semana
      X2 = unidades del producto a producir en envases de 200g para la próxima semana
      X3 = unidades del producto a producir en envases de 360g para la próxima semana
#### rta
X1 = unidades del producto a producir en envases de 120g para la próxima semana

X2 = unidades del producto a producir en envases de 200g para la próxima semana

X3 = unidades del producto a producir en envases de 360g para la próxima semana


### ¿Cuál/Cuáles de las siguientes funciones representan restricciones del problema?
- [ ] 120X1 + 200X2 + 360X3 ≤ 3
- [ ] 1 X1  + 2 X2 + 4 X3 ≤ 2.400
- [ ] 0,120X1 + 0,200X2 + 0,360X3  ≤ 3.000
- [ ] 1 X1 + 2 X2 + 4 X3 ≤ 7.200
- [ ] X1 ≥ 3.000
- [ ] X2 = 300
- [ ] X2 ≥ 300
#### rta
0,120X1 + 0,200X2 + 0,360X3  ≤ 3.000
X2 ≥ 300

1 X1 + 2 X2 + 4 X3 ≤ 7.200 

(ESTA ESTA PASADA A MINUTOS son las 120horas x60= 7200 minutos)

### Si un proveedor le ofrece envases de 120 gr. vacíos a un precio de $1 cada uno, describa lo que haría para determinar si le conviene comprarlos o no.
#### rta
agg una nueva variable x4, que es la cantidad de envases a comprar, esta variable yo la podria agg en la restriccion 

x1 <= 3000+x4

tendriamos los 3000 envases + los que compremos

esto vemos como cambia la produccion por lo tanto el Ingreso Total

y tambien tenemos que tener en cuenta el costo de estos envases
esto lo hacemos en la funcion objetivo

Max (Z)= 25X1+50X2+110X3- 1X4
### El modelo de programación lineal del problema analizado queda formulado en forma: ___ y ___
#### rta
explicita y 