# Enunciado
Dado el siguiente programa lineal:
Max z = 2 x1 +3 x2

Sujeto a:
4 x1 + 2 x2 ≤ 20
2 x1 + 4 x2 ≤ 16
x1 + x2 ≤ 15
x1 ≥ 0, x2 ≥ 0


a) Grafique las inecuaciones del modelo;
b) Identifique con letras las soluciones básicas en el gráfico y arme una tabla con los
valores
c) Identifique con letras las soluciones posibles básicas en el gráfico:
d) Identifique el polígono de soluciones posibles;
e) Grafique la función objetivo (a modo de ejemplo podría usar z=12 o z=0 o ambas)
f) Identifique hacia donde maximiza la función
g) Identifique el punto que hace máximo el valor de z
h) ¿Cuál es la solución óptima?
i) Seleccione el método que utilizó o como calculó el valor de los valores de las
variables en la solución óptima:
i. ( ) sustitución;
ii. ( ) igualación;
iii. ( ) Cramer;
iv. ( ) usando las coordenadas del gráfico;
v. ( ) a ojo en el gráfico;
vi. ( ) software o calculadora.
vii. ( ) sustitución, igualación o Cramer es indistinto


## a y d)
A)
Se detalla el paso a paso para delimitar el área de trabajo válida.

- **Restricción de No Negatividad:** Circunscribe el gráfico exclusivamente al primer cuadrante, ya que las [[Variables de Decisión]] deben ser $\geq 0$.
- **Trazado de Inecuaciones:** Se grafica cada [[Restricción]] asumiéndola temporalmente como una igualdad para encontrar las intersecciones con los ejes (anulando $x_1$ y luego $x_2$).
![[{F773EC83-2B75-4876-AD1B-BAC136BF4367}.png|131]]
![[{CF106BC1-02C3-4FC6-9487-0EB23F54BEFA}.png]]
![[{A3CE7E52-93D0-4FEE-90D0-FF9FFAD0AF77}.png|355]]

- **Identificación de Semiplanos:** Se utiliza un "punto de prueba" (frecuentemente el origen $(0,0)$ o un punto como $(2,2)$) para verificar hacia qué lado de la recta se cumple la inecuación original.
![[{1FC13917-F35F-410E-B4C1-489823CD5276}.png]]

lo mismo con el resto de las restricciones ....

- **Intersección:** La superposición de todos los semiplanos válidos genera la [[Región Factible]] o [[Poliedro de Soluciones]].
- ![[{85194BD9-B641-4436-AFBD-B2A57BB7FC41}.png]]
![[{A429859E-EFF9-4C0A-BE1D-DBE56D0DCE2A}.png]]
---


> [!question] Pregunta Frecuente en Clase _¿El poliedro de soluciones factibles puede ser un conjunto cóncavo o tener áreas separadas?_ Falso. El profesor aclaró que la región común de soluciones siempre debe ser un [[Polígono Convexo]]. Si tomas dos puntos cualesquiera dentro del área, la línea que los une debe estar completamente dentro de ese polígono.

## B y c)
B y c)

El segundo bloque se centró en la teoría detrás de los puntos de intersección del gráfico y cómo predecir su cantidad máxima sin necesidad de graficar.

> [!note] Fórmula del Número Máximo de Soluciones Básicas $$ C = \frac{n!}{m!(n-m)!} $$ _(Donde $n$ es el número total de variables, incluyendo las de holgura, y $m$ es el número de restricciones no se incluye la de no negativadad)_.


|Tipo de Solución|Ubicación Gráfica|Característica Principal|
|:--|:--|:--|
|**[[Soluciones Básicas]]**|Todas las intersecciones de rectas (incluyendo ejes).|No todas respetan la no negatividad. En el ejemplo: 10 soluciones.|
|**[[Soluciones Posibles Básicas]]**|Exclusivamente en los vértices del [[Poliedro de Soluciones]].|Verifican todas las restricciones simultáneamente. En el ejemplo: Solo 4 soluciones.|

en nuestro ejemplo n=5 y m=3
$$C = \frac{5!}{2!(5-2)!}=10$$ en la calculadora x! es el factorial

SOLUCIONES BASICAS: (10)
![[{C7D56DCC-18FA-4EDC-BC29-575F3A7166F3}.png]]

SOLUCIONES POSIBLES BASICAS (4) -> SUBCONJUNTO DE SOLUCIONES BASICAS
![[{11AC18B2-5039-490E-84AC-7C4A5E5A47DC}.png]]

---
### ANALISIS DE SOLUCIONES
![[{51C6D5E7-326A-43CF-AE43-54573A10AF6A}.png]]

## g)
G)
Una vez graficadas las restricciones, el profesor explicó cómo encontrar el punto óptimo. La clave es asignarle a la [[Función Objetivo]] ($Z$) un valor arbitrario (ej: $Z=12$ o $Z=0$) para poder trazar su pendiente en el plano.
![[{06330AED-B83B-4352-BA2E-45A1B4797DA3}.png]]
![[{E28E9558-7348-47DB-93B2-AB47FC3AD20B}.png|258]]

- **Desplazamiento:** Al ser un caso de [[Maximización]], la recta se desplaza paralelamente **alejándose del origen** hasta tocar el último vértice del polígono de soluciones.
	- **En [[Minimización]]:** La recta se desplaza en sentido contrario, **acercándose hacia la izquierda/origen**, buscando el punto de contacto de menor valor.

![[{7BD96D93-C8B2-41D1-AF97-048577817E39}.png]]

- **Cálculo Exacto:** Una vez identificado visualmente el vértice óptimo, se debe resolver el sistema de ecuaciones de las dos rectas que se cruzan en ese punto mediante métodos algebraicos (Igualación, Sustitución o Cramer).
![[{B394858B-DEC0-4B6D-A8C8-957D9ADC8758}.png]]
![[{64E83311-1B98-4DEE-9A7D-7CFCBB416596}.png]]
> [!danger] Trampa de Parcial: El cálculo "a ojo" El profesor fue tajante: NUNCA se deben estimar los valores de las variables "a ojo" mirando la escala del gráfico. Una vez identificado el vértice óptimo visualmente, debes usar el [[Método de Igualación]] o el [[Método de Sustitución]] con el sistema de ecuaciones de las dos rectas que se cruzan para hallar el valor algebraico exacto.


El último tema crucial fue cómo introducir las variables adicionales para convertir el modelo gráfico (inecuaciones) en un modelo estandarizado (ecuaciones), que es la base para el futuro [[Método Simplex]].

- En inecuaciones $\leq$: Se suma una [[Variable de Holgura]] ($+S_i$) para igualar el recurso consumido con el disponible.
- En inecuaciones $\geq$: Se resta una [[Variable de Excedente]] ($-S_i$) para quitar el exceso sobre el requisito mínimo.

> [!danger] Error Crítico de Examen: Confusión de Signos Las variables NUNCA pueden ser negativas. Una violación a la [[Restricción de No Negatividad]] anula directamente el examen. El profesor aclaró que la [[Variable de Excedente]] en sí misma siempre es $\geq 0$. El signo "menos" en la ecuación es meramente una _operación algebraica_ del modelo para restar esa cantidad positiva.

### solucion

Y POR ultimo para hallar el vector solucion nos falta encontrar el valor de las variables de holgura

para encontrarlo remplazamos x1,x2 en las ecucaiones
![[{BAF2977A-7BF2-4D0C-B5EA-D083D4303A44}.png]]

![[{67B40F9E-92EB-44B2-9F3C-9DB97A6C8A0B}.png]]