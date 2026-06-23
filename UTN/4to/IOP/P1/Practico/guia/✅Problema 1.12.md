Problema 1.12
Un constructor va a edificar dos tipos de viviendas prefabricadas: con uno o dos
dormitorios. ==Dispone de 6 millones de pesos== y el costo de una vivienda de 2
dormitorios es de 500 mil pesos== mientras que las de un dormitorio cuestan 350 mil
pesos.== El ==número de casas de dos dormitorios deberán ser al menos del 35% del total
fabricado== y ==el de un dormitorio del 25% por lo menos==. Para mantener la seguridad
del negocio a realizar, la ==inversión en viviendas de dos dormitorios no deberá superar
los 4,5 millones==, y la ==inversión en casas de un dormitorio podrá llegar sólo a un límite
máximo del 70% de la inversión total realizada.==
Si cada casa de dos dormitorios se vende a 850 mil pesos y cada una de un dormitorio
a 550 mil pesos, ¿Cuántas casas de cada tipo debe construir para ==obtener el beneficio
máximo==?

# U2
objetivo verbal

- **Identificación del Objetivo:** **maximizar el [[Beneficio Total]]** obtenido a partir de la construcción y venta de las viviendas tipo 1 (un dormitorio) y tipo 2 (dos dormitorios).

> [!danger] Trampa Teórica: Beneficio vs. Ingreso Muchos alumnos confunden ingresos con beneficios. La profesora aclaró en clase que, al tener el precio de venta y el costo de fabricación, el modelo debe apuntar a la ganancia neta (la diferencia entre ambos)

definicion de variables
Siguiendo las reglas estrictas de la cátedra para la formulación, las variables no pueden definirse simplemente como "cantidad de casas". Debemos asignarles la unidad física exacta
* x_1=Unidades de viviendas de un dormitorio tipo 1 a construir
* x_2=Unidades de viviendas de dos dormitorio tipo 2 a construir

restricciones verbal
* Dispone de 6 millones de pesos
* numero de la viviendas de dos dos dormitorios debera ser al menos del 0,35 del total fabricado
* numero de viviendas de uno dormitorioa deberan ser al menos 0,25 del total
* La inversion de viviendas de dos dormotiros no debera superar los 4,5millones
* La inversion de viviendas de un dormitorio podra ser como maximo 0,7 de la inversion total


planteo de pl

para sacar el beneficio y plantear el objetivo debemos hacer (precio venta - costo)

x_1   (550-350)=200 -> BENEFICIO de x1

x_2  (850-500)= 350 -> BENEFICIO de x2

MAX z= 200x_1+350 x_2

S.A
350.000(COSTO)* x1+500.000(costo)* x2 <= 6.000.000
x2>= 0,35( x1+x2)
x1>= 0,25(x1+x2)
500.000(costo) * x2 <= 4.500.000
350.000(COSTO)* x1 <= 0,7 * (350.000(COSTO)* x1+500.000(costo)* x2 )

x1;x2>= 0



>[!question] Pregunta : Estructura de las Restricciones Proporcionales **Alumno:** En el problema de construcción de viviendas, un alumno planteó si la restricción de porcentaje (25% del total fabricado) debía escribirse ya despejada con las constantes a la derecha para que fuera correcta. 
>**Respuesta de la Profesora:** Aclaró que, para el momento inicial de _formular_ el modelo y que sea legible por un humano, es perfectamente correcto (y deseable) plantearla lógicamente como x1​≥0.25(x1​+x2​). Sin embargo, confirmó que _para resolverlo_ matemáticamente después, el alumno debe aplicar propiedad distributiva y pasar las variables a la izquierda.


>[!question] Pregunta de Clase: Confusión con el Análisis Dimensional Un alumno se confundió al ver que en una restricción se mezclaban "unidades de casas" y "pesos". 
>
>Respuesta de la Profesora:_ Explicó que al multiplicar el costo (Pesos/Casa) por la variable (Casas), las unidades de "casa" se simplifican matemáticamente, resultando netamente en "Pesos". Esto hace que el lado izquierdo de la ecuación sea perfectamente coherente con el límite de presupuesto (Lado Derecho).![[{3CDC19D7-4B23-416E-82C2-C2EB7E1498C9}.png]]

---

> [!danger] Confusión Frecuente _"Recuerden por favor que no negatividad quiere decir mayor o igual a 0 no quiere decir positivo recuerden la diferencia"_. Exigir que una variable sea positiva excluye el valor cero, lo cual alteraría el conjunto de soluciones factibles en la [[Programación Lineal]].
