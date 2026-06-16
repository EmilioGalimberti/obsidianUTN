https://www.youtube.com/watch?v=eZraxYlQiCU&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=16

## 1. Repaso Inicial:

- **Apertura Teórica:** cómo se relacionan las variables entre el [[Problema Primal]] y el [[Problema Dual]].
![[{9A860ABD-33C9-4952-9EA4-7F59B293F9F8}.png]]


- **Igualdad de Objetivos:** Se recuerda mediante el [[Teorema Fundamental de la Dualidad]] que, en el punto óptimo, los valores de la [[Función Objetivo]] de ambos problemas son matemáticamente iguales.
![[{199FC2A5-9776-4EDB-AE4F-B62F71725ED5}.png]]
>[!note]- **[[Teorema Fundamental de la Dualidad]]**: 
>Dicta que si el problema primal tiene una solución óptima, el problema dual también la tiene, y el valor de la [[Función Objetivo]] en ambos es exactamente igual. En cualquier punto que no sea el óptimo, el valor del máximo siempre será menor que el valor del mínimo.


---
El profesor dedicó un bloque significativo a diferenciar tajantemente las dos interpretaciones que posee una [[Variable Dual]] ($y_i$), advirtiendo que confundirlas es un error frecuente en las evaluaciones.

- **[[Significado Matemático]]:** Indica estrictamente la cantidad en que se incrementa la [[Función Objetivo]] ($Z$) ante un incremento unitario en el [[Lado Derecho]] ($b_i$) de su restricción asociada.
> [!note] Expresión Matemática del Incremento $$ \Delta Z = \Delta b_i \times y_i $$
- **[[Significado Económico]]:** Dependiendo del contexto, representa la valoración interna, el [[Precio Sombra]] de un recurso, o el valor máximo que la empresa está dispuesta a pagar por adquirir una unidad adicional de dicho recurso.
![[{CEB9DAD4-1108-46C3-9F27-7D9996FC4077}.png]]


> [!danger] Trampa de Parcial 1: Confusión de Significados Duales El profesor remarcó fuertemente esto: _"es importante que los tengan presentes porque muchas veces en los exámenes le pedimos el significado económico y nos hablan solo del incremento en la función Z"_,. **El Error:** Cuando se pide el [[Significado Económico]] de una [[Variable Dual]], el alumno suele dar la definición del [[Significado Matemático]]. El significado económico requiere hablar del [[Precio Sombra]] o la "valoración interna" que tiene un recurso específico para la empresa (cuánto está dispuesta a pagar por una unidad extra),. El matemático se limita a decir "cuánto incrementa Z",.




## 2. Aplicación Práctica: Dualidad Canónica en Fábrica de Pinturas (Min 5:45 - 15:29)

![[{CFF12D9C-8542-4D52-8FBA-18E0240EF90A}.png]]
- **Planteo del Problema:** Se retoma un ejercicio anterior de maximización (Fábrica de Pinturas) con inecuaciones $\le$, identificándolo como un modelo de [[Forma Canónica]].


- **Reglas de Transformación:** El profesor guía la construcción del dual:
    1) El número de [[Variables Principales]] dicta el número de restricciones duales (3 variables $\rightarrow$ 3 restricciones).
    2) Los valores del [[Lado Derecho]] original pasan a ser los coeficientes de la nueva función.
	    1) ![[{7154A03E-F764-4203-ACC3-3CC4892B1BDD}.png]]
    3) El problema dual tendra tanta restricciones como variables tenga el primal; una por cada variable
    4) las columnas del primal pasan a ser los coeficientes de las restricciones del dual, es decir A=PRIMAL A^T=DUAL (la transpuesta)
    5) Los coeficientes de la [[Función Objetivo]] pasan a ser los valores del [[Lado Derecho]] del dual.
	    1) ![[{5CD1A9E9-B8A9-4EE3-B24E-8E7A6F7DE086}.png]]
	6) ARMAR LOS SIGNOS DE LAS RESTRICIONES:
		1) ![[{75FE4E4E-C245-49B6-B9E1-7EB204316FE7}.png]]
>[!tip] La Regla de la Normalidad Para saber si una restricción es canónica, recuerda los formatos estándar: si el problema es de **[[Maximización]]**, lo canónico o normal es tener restricciones de ≤. Si el problema es de **[[Minimización]]**, lo canónico es ≥.

| Atributo en la [[Restricción]] Original | Condición del Problema                                  | Signo de la [[Variable Dual]] Resultante   |                                                 |
| --------------------------------------- | ------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| **[[Restricción Canónica]]**            | Respeta la naturaleza del modelo (ej. ≥ para un Mínimo) | **[[Variable No Negativa]]** (≥0).         | si es canoncico en maximo tmb lo sera en minimo |
| **[[Restricción No Canónica]]**         | Contradice el modelo (ej. ≤ para un Mínimo)             | **[[Variable No Positiva]]** (≤0).         |                                                 |
| **[[Restricción de Igualdad]]**         | Ecuación estricta (=)                                   | **[[Variable Sin Restricción de Signo]]**. |                                                 |
>[!tip] La Regla de la Normalidad Para saber si una restricción es canónica, recuerda los formatos estándar: si el problema es de **[[Maximización]]**, lo canónico o normal es tener restricciones de ≤. Si el problema es de **[[Minimización]]**, lo canónico es ≥.

>[!danger] Omisión de Restricción de Signos El profesor notó que muchos alumnos escribían bien las inecuaciones pero se olvidaban de definir el signo de las variables (y1​≥0, etc.) al final del planteo. Advirtió que **"si no escriben esta última parte, todo el planteo está mal"**

## QUE SIGNIFICAN LAS VARIABLES DUALES?
recordar: 

variables de holgura:


* significado matematico de las variables duales:
	* y_1=
		* lo que aumenta la funcion objetivo (contribucion a las utilidades) ante un aumento unitario de las Hs de maquina mezcladora
			* Actualmente tengo 10 hs, si yo aumento en una unidad es decir 11hs la funcion objetivo aumentara en y1

* significado economico de las variables duales
	* y_1=
		* es el valor interno de las hs maquina mezcladora 
		* precio sombra de las maquinas mezcladora
		* maximo precio que estaria dispuesto a pagar por obtener 1hs mas de maq mezcladora
![[{82673E8B-5F1E-4675-9E61-1EDB7E4CDCA6}.png]]
## 3. Extracción de Variables Duales desde Simplex (Min 15:29 - 18:13)

- **Lectura Directa:** El profesor explica cómo obtener los valores de las [[Variables Duales]] sin plantear el dual, leyendo directamente la tabla óptima del primal.
- **Ubicación Analítica:** Los valores se extraen de la fila de evaluación $C_j - Z_j$, en las columnas correspondientes a las [[Variables de Holgura]] iniciales
- El teorema dicta que si una variable principal es positiva, su variable de holgura asociada en el problema opuesto es forzosamente nula (cero).
> [!danger] Condición Estricta del Teorema El profesor alertó que la regla de "si una es positiva, la otra es nula" se cumple **única y exclusivamente en la tabla óptima**. Si intentas aplicar esta regla en las tablas intermedias de resolución del algoritmo Simplex, cometerás un error grave.

![[{FBEF1AB5-880C-47CB-A344-E2D6C3229609}.png]]

en este caso son positivos porque estamos en un problema de maximo canonico y sus variables duales son >=0


En un mixto tenemos que tener cuidado que signo asumen las variables en el dual

## 4. Metodología para la Dualidad Mixta (Min 18:13 - 34:53) ==REVISAR PARA HACER UNA MECMOTECNIA==
![[{10791995-CBA1-4313-BC9E-2581F766F1D4}.png|552]]

Para plantear el modelo dual cuando existen inecuaciones mezcladas, el profesor desaconsejó estudiar tablas de memoria y enseñó a deducir los signos mediante la regla de la "normalidad" o canonicidad.

### regla memotecnica de gemini
#### 1. Entender qué es "Normal" (Sensato)

Pensá en la lógica detrás de los problemas que modelás:

- **En un problema de MÁXIMO (ej. maximizar ganancias):**
    
    - Lo "Normal" es que fabriques cantidades positivas de productos $\rightarrow$ **Variables $\geq 0$**
        
    - Lo "Normal" es que estés limitado por un tope de horas o materiales $\rightarrow$ **Restricciones $\leq$**
        
- **En un problema de MÍNIMO (ej. minimizar costos de una dieta):**
    
    - Lo "Normal" es que compres cantidades positivas de alimentos $\rightarrow$ **Variables $\geq 0$**
        
    - Lo "Normal" es que debas cumplir con un requerimiento mínimo de vitaminas $\rightarrow$ **Restricciones $\geq$**
        

#### 2. La Regla Mnemotécnica de los 3 Pasos

Sabiendo qué es lo normal para cada objetivo, la tabla se reduce a esto:

- 🟢 **Lo NORMAL genera lo NORMAL:**
    
    - Una variable de Max $\geq 0$ (Normal) genera una restricción de Min $\geq$ (Normal).
        
    - Una restricción de Max $\leq$ (Normal) genera una variable de Min $\geq 0$ (Normal).
        
- 🔴 **Lo RARO genera lo RARO:**
    
    - Una variable de Max $\leq 0$ (Rara) genera una restricción de Min $\leq$ (Rara).
        
    - Una restricción de Max $\geq$ (Rara) genera una variable de Min $\leq 0$ (Rara).
        
- 🔵 **Lo RÍGIDO genera lo LIBRE (y viceversa):**
    
    - Una restricción con un $=$ (Súper rígida) genera una variable "Sin restricción / S/restric" (Totalmente libre).
        
    - Una variable "Sin restricción" genera una restricción con $=$.
        

#### 3. El "Truco Visual" (Para zafar en un parcial)

Si estás en medio de un examen y te da un blanco mental, hay un atajo puramente visual mirando tu tabla:

- **De Variables a Restricciones (La mitad de arriba de tu foto):** El signo **SE COPIA**.
    
    - Si la variable mira a la derecha ($\geq 0$), la restricción mira a la derecha ($\geq$).
        
    - Si la variable mira a la izquierda ($\leq 0$), la restricción mira a la izquierda ($\leq$).
        
- **De Restricciones a Variables (La mitad de abajo de tu foto):** El signo **SE INVIERTE**.
    
    - Si la restricción mira a la izquierda ($\leq$), la variable se da vuelta y mira a la derecha ($\geq 0$).
        
    - Si la restricción mira a la derecha ($\geq$), la variable se da vuelta y mira a la izquierda ($\leq 0$).

### regla notebook
Para recordar los signos en la **[[Dualidad Mixta]]**, el profesor aconseja no memorizar tablas complejas, sino aplicar la regla lógica de la **[[Restricción Canónica]]**. Esta regla vincula de forma sencilla la "normalidad" del elemento original con el signo del elemento dual.

> [!tip] Regla Práctica del Profesor para Dualidad Mixta En lugar de estudiar la tabla de memoria, fíjate siempre en la normalidad del modelo. La regla de oro que debes grabar es: **"no negativa es canónica, no positiva es no canónica, sin restricción de signo es igualdad"**.

### 1. De Restricciones (Primal) a Variables (Dual)

El signo de cada **[[Variable Dual]]** depende directamente del sentido de la **[[Restricción]]** que le da origen:

- **[[Restricción Canónica]]**: Si la restricción respeta la normalidad del modelo ($\le$ en **[[Maximización]]** o $\ge$ en **[[Minimización]]**), origina una **[[Variable No Negativa]]** ($\ge 0$).
- **[[Restricción No Canónica]]**: Si la restricción contradice el objetivo ($\ge$ en **[[Maximización]]** o $\le$ en **[[Minimización]]**), origina una **[[Variable No Positiva]]** ($\le 0$).
- **[[Igualdad]]**: Toda restricción de ($=$) origina una variable **[[Sin Restricción de Signo]]** (puede ser positiva, negativa o nula).

### 2. De Variables (Primal) a Restricciones (Dual)

La lógica se aplica a la inversa para definir el sentido de las restricciones del **[[Problema Dual]]** basándose en el signo de las variables de decisión del **[[Problema Primal]]**:

|Signo de la Variable Primal|Tipo de Restricción Dual Generada|
|:--|:--|
|**[[Variable No Negativa]]** ($\ge 0$)|Genera una **[[Restricción Canónica]]**|
|**[[Variable No Positiva]]** ($\le 0$)|Genera una **[[Restricción No Canónica]]**|
|Variable **[[Sin Restricción de Signo]]**|Genera una restricción de **[[Igualdad]]** ($=$)|

> [!danger] Trampa de Parcial: Confundir los Signos de Variables Es un error muy grave ponerle signo negativo ($-$) a una variable dual cuando proviene de un problema puramente canónico. Recuerda que "no positivo" ($\le 0$) significa incluir el cero, no simplemente "negativo".

### Resumen Visual de la Regla

```
graph TD
    A[Analisis del Elemento Primal] --> B{Cumple la condicion Canonica?}

    B -->|Si es Canonico| C[Genera Elemento Dual Normal/Positivo]
    C --> D[Variable >= 0 o Restriccion Canonica]

    B -->|No es Canonico| E[Genera Elemento Dual Inverso/Negativo]
    E --> F[Variable <= 0 o Restriccion No Canonica]

    B -->|Es una Igualdad o Sin Restriccion| G[Genera Elemento Dual Libre]
    G --> H[Variable Sin Restriccion o Restriccion de Igualdad]
```

_Conceptos Relacionados:_ [[Dualidad Mixta]], [[Restricción Canónica]], [[Variable No Negativa]], [[Problema Primal]], [[Problema Dual]].
## **Actividad en el Aula Virtual:** Los alumnos resuelven el Problema 4b de la guía en tiempo real.
![[{874963E8-9029-42F0-89A0-08A0E52815D8}.png]]
### 1ero cantidad de restricciones y cantidad de signos
1. Tipo de Optimización (**[min**)
	1. Se transforma en max
2. por cada ristriccion en el primal es una variable en la funcion objetivo del dual
	1. ==restriciones primal: 4
	2. ==variables principales dual: 4
3. Cantidad de **[[Variables Principales]]** (xj​) en el primal es una restriccion en el dual
	1. ==variables princpales primal: 2
	2. ==restricciones dual: 2
4. los Coeficientes del **[[Valor del Lado Derecho]]** (bi​) del primal (6;10,5;6;2) se conviernten en **[[Coeficientes de la Función Objetivo]]** (cj​) del dual
	1. ==max G = 6y1+10,5y2+6y3+2y2
5.  obtemos la tranpuesta del problema pirmal al que sta SA es decir
	1. ==-3y1+1y2-y3-0,6y4   
	2. ==2y1+y2+3y3+y4
6. **[[Coeficientes de la Función Objetivo]]** (cj​) del primal se convierte en los coeficientes del VALOR DEL LADO DERECHO (b_i) dual
	1. -3y1+1y2-y3-0,6y4       ==1
	2. 2y1+y2+3y3+y4            ==2
7. ==(NOS FIJAMOS EN EL SIGNO DE LA RISTRICCION X1)==  
8. ==(NOS FIJAMOS EN EL SIGNO DE LA RISTRICCION S/N)== si es sin signo  corresponde a una =
	1. 1. -3y1+1y2-y3-0,6y4   <=    1
	2. 2y1+y2+3y3+y4      =  2
9. Y ahora los signos para las variables duales  (==NOS FIJAMOS EN LAS DESIGUALDADES DE LAS RESTRICCIONES)
	1. PARA LOS PROBLEMAS DE MINMO LOS SIGNOS QUEDAN IGUALES
		1. y1 <= 0
	2. lo mismo para y2
		1. y2 <= 0
	3. para y3 la restricciones es >= por lo tanto 
		1. y3 >= 0
	4. para y4 es una = por lo tanto
		1. y4  S/n

![[{24B4DD19-CAEC-4C74-B55F-B389D9481507}.png]]


## 5. Fundamentos Lógicos del Análisis de Sensibilidad (Min 34:53 - 39:51)

>[!note]- El propósito principal del **[[Análisis de Sensibilidad]]** 
>es poder darle respuestas gerenciales al decisor en el momento, calculando impactos y verificando límites sin necesidad de _"abrir la computadora, modificar el modelo original, agregar variables y volver a iterar el software"_ desde cero.

- El profesor introduce la mecánica de evaluar cambios dentro del [[Intervalo de Sensibilidad]] para evitar recalcular el algoritmo.
### Parámetros Evaluados
* ***[[Variación en Coeficientes de la Función Objetivo]]**: Modificación en las utilidades o costos de los productos.
	*  Si afecta a una **[[Variable No Básica]]** (que vale cero) y está dentro de su intervalo permitido, no cambia nada en absoluto del plan actual.
	- Si afecta a una **[[Variable Básica]]** y está dentro del intervalo, la base (el plan de producción) se mantiene, pero cambia el valor total de Z.
	- si esta fuera del intervalo; resolver nuevamente
	- ![[{51C3EDD9-78C8-4057-B7D4-0A33667F6A69}.png]]
- **[[Variación en el Valor del Lado Derecho]]**: Modificación en la disponibilidad de un recurso. Su impacto depende de su naturaleza:
	- ![[{4B5F73EE-B5C0-45EE-A958-BAFD3CC85720}.png]]
		- - **[[Restricción Limitante]]**: El recurso se agotó (su holgura es cero). Si se altera su disponibilidad (dentro del intervalo permisible), cambiará el valor de las variables del plan de producción y el valor final de Z.
		- **[[Restricción No Limitante]]**: Existe recurso sobrante (holgura >0). Alterar su disponibilidad dentro del intervalo **solo modifica el tamaño del sobrante** (el valor de su variable de holgura), manteniendo intactas las variables principales y la ganancia Z.



```
graph TD
    A[Cambio en Lado Derecho bi] --> B{Dentro del Intervalo?}
    B -->|No| C[Volver a calcular: Cambia la base y Z]
    B -->|Si| D{Es Restriccion Limitante?}
    D -->|No: Holgura > 0| E[Solo se modifica el valor de la holgura]
    D -->|Si: Holgura = 0| F[Cambian valores de las variables basicas y Z]
```

_Conceptos relacionados:_ [[Lado Derecho]], [[Intervalo de Sensibilidad]], [[Restricción Limitante]], [[Restricción No Limitante]].

## 6. Ejercicio Integrador y Debate sobre Toma de Decisiones (Min 39:51 - Final)

- **Trabajo Grupal:** Se asigna el Problema 8 para resolver en salas pequeñas.

![[{F95EAD14-0751-45DF-8DEF-DE78035021EF}.png]]
![[{696796A5-1F78-4625-AF00-7ABB118454C8} 1.png]]
![[{9429B2C5-F993-4CDC-8674-8FC5E9790A03}.png]]
![[{5AB6C8BB-9414-4329-8F7F-8C01853989F4}.png]]
### a)
solucion optima
e=80
s=120
l=0
s1=0
s2=0
s3=320
s4=70

valora de la funcion objetivo = 16440

### b)
- _Falla de 20 motores:_ Al ser una restricción limitante, el profesor demuestra cómo calcular el nuevo valor de la función objetivo multiplicando la reducción por el [[Precio Dual]] (31).


* El cambio queda dentro del intervalo 
	* ![[{5061E77B-B444-40D7-93DD-5A1AF0741B76}.png]]
* y  corresponde a una restriccion limitante   (S1=0)
* esta dentro del intervalo y es una restriccion limitante  por lo tanto la base:
	* no cambia (las  variables que son positivas seguiran siendo positivos y las variables nulas seguiran sinedo nulas)
* PERO LA SOLUCION SI CAMBIA cambiará el valor de las variables del plan de producción
* POR LO TANTO CAMBIARA TAMBIEN EL VALOR FINAL DE Z
* [Z nuevo = Z actual + Delta b * Variable Dual]
	* (16440-(31x20))= 15820

#### ==de donde sale esta formula para calcular el nuevo valor de z

Esa fórmula corresponde al cálculo analítico de actualización de la **[[Función Objetivo]]** dentro del **[[Análisis de Sensibilidad]]**, aplicado específicamente cuando ocurre una variación en el **[[Valor del Lado Derecho]]** (VLD o $b_i$) de una **[[Restricción Limitante]]**.

De hecho, los números de tu consulta provienen textualmente de un ejercicio desarrollado en clase por el profesor, donde se analizaba qué sucedería con la ganancia si, por fallas técnicas, **no se podían utilizar 20 motores**.

##### El Fundamento Teórico

> [!note] Fórmula de Actualización de Z por variación en $b_i$ Según el Teorema Fundamental y la teoría de post-optimidad, el nuevo valor de la función objetivo se calcula de la siguiente manera: $$ Z^{nuevo} = Z^{actual} + \Delta b_i \cdot y_i $$ _(Donde $\Delta b_i$ es el incremento o disminución del recurso, e $y_i$ es la **[[Variable Dual]]** o **[[Precio Sombra]]** asociada a esa restricción)_.

##### Desglose de tu Cálculo

En tu ecuación: $16440 - (31 \times 20) = 15820$, las partes representan lo siguiente:

- **$16440$:** Es el $Z^{actual}$, es decir, el valor actual que tiene la **[[Función Objetivo]]** en el óptimo.
- **$31$ (DUAL PRICE):** Es el valor de la **[[Variable Dual]]** ($y_i$) del recurso "motores". Te indica matemáticamente en cuánto varía la función objetivo por cada unidad de recurso que se modifique.
- **$20$:** Es la variación ($\Delta b_i$). El profesor indicó que "se restan" 20 motores. Como es una pérdida de recursos ($-20$), la regla de signos matemática transforma la suma original en una resta: $16440 + (-20 \times 31)$.
- **$15820$:** Es el $Z^{nuevo}$, el nuevo nivel de utilidades tasado tras sufrir la falla en los motores.

> [!tip] Condición Obligatoria de Uso El profesor advirtió que para poder utilizar este atajo algebraico y no tener que recalcular toda la matriz Simplex, la variación del recurso (la pérdida de los 20 motores) debe estar obligatoriamente **dentro del [[Intervalo de Sensibilidad]]** permitido para ese parámetro.

> [!danger] Atención a la Terminología: Dual Price Tu fórmula dice explícitamente "DUAL PRICE" (Precio Dual). Cuidado en el parcial: en un modelo de **[[Maximización]]**, el Precio Dual y el Precio Sombra son el mismo número. Pero si te enfrentas a un problema de **[[Minimización]]**, ambos conceptos numéricamente tienen signos opuestos. Apégate siempre a utilizar la **[[Variable Dual]]** directa.

##### Esquema Lógico de Aplicación

```
graph TD
    A[Analisis de Sensibilidad] --> B[Falla Tecnica: Disminucion en 20 motores]
    B --> C{¿La reduccion de 20 esta dentro del Intervalo de Sensibilidad?}

    C -->|No| D[Cambia la Base - Recalcular todo el modelo]

    C -->|Si| E[Aplicar Formula de Actualizacion Z]
    E --> F[Z nuevo = Z actual + Delta b * Variable Dual]
    F --> G[16440 + -20 * 31 = 15820]
```

_Conceptos relacionados:_ [[Análisis de Sensibilidad]], [[Valor del Lado Derecho]], [[Restricción Limitante]], [[Variable Dual]], [[Función Objetivo]].

### c)
Dual prices: indica cuanto esta dispuesto a pagar por encima de lo que paga actualemente

por lo tanto en este ejercicio vemos que esta dispuesto a pagar hasta 32$ por encima de lo que paga actualmente, entonces SI conviene comprarla 20
![[{76295AE2-327B-449F-82E5-3C31708182BE}.png]]

Hasta cuantas le conviene comprar?
hasta 80 ![[{01F37CB6-3C47-445C-80B0-E03D8A8C600F}.png]]

cual seria el nuevo valor de la funcion objetivo Z(nuevo)=Zactual+precio dual * (lo maximo de aumento allow incrase)

19000=16440+32x80

> [!question] Debate Crítico en Clase: Ingreso Neto vs. Variación de Z **Contexto:** Se ofrece comprar un insumo adicional pagando $20$ extra sobre el costo actual. El [[Precio Dual]] es $32$ y el límite de compra es $80$ unidades. **Alumno:** _"Yo no entendí muy bien... hice $80 \times 12$ (que es la ganancia de 32 - el recargo de 20)... ¿por qué estaría mal el valor de Z?"_. 
> 
> **Respuesta del Profesor:** El alumno estaba confundiendo la **ganancia de bolsillo** con la **variación matemática de Z**. 
> 
> SIGNIFICADO MATEMATICO
> El [[Significado Matemático]] de la variable dual indica que la función objetivo ($Z$) crecerá rígidamente en $32$ por cada unidad, sin importar cuánto pagaste de tu bolsillo por ella. Es decir, la nueva tabla mostrará un incremento de $80 \times 32$. 
> 
> $$ Z_{nuevo} = Z_{actual} + \Delta b_i \cdot y_i $$ _(Donde $\Delta b_i$ es el incremento o disminución del recurso, e $y_i$ es la **[[Variable Dual]]** o **[[Precio Sombra]]** asociada a esa restricción)_.
> 
> SIGNIFICADO  ECONOMICO
> La ganancia económica real ($80 \times 12$) es una deducción gerencial posterior, pero matemáticamente el modelo reportará el aumento usando los $32$ completos.

#### explicacion del calculo
La fórmula es la ecuación fundamental que establece la bibliografía ("Apoyo Cuantitativo a las Decisiones") para calcular el nuevo valor de $Z$ cuando se modifica la disponibilidad de un recurso que corresponde a una **[[Restricción Limitante]]**.

> [!note] Fórmula Matemática de Actualización del Funcional $$ Z_{nuevo} = Z_{actual} + \Delta b_i \cdot y_i $$ _(Donde $\Delta b_i$ es el incremento o disminución del recurso, e $y_i$ es la **[[Variable Dual]]** o **[[Precio Sombra]]** asociada a esa restricción)_.

##### Desglose del Cálculo en Clase (El Caso de las Bobinas)

En el ejercicio que desató el debate que mencionas, la empresa evaluaba una oferta de su proveedor para comprar bobinas adicionales, pagando un recargo de $20$ por unidad.

El profesor utilizó la lectura del software para estructurar la ecuación que tú citaste: $19000 = 16440 + 32 \times 80$.

¿De dónde salió cada número en la clase?

1. **$Z_{actual}$ ($16440$):** Era el beneficio máximo que la empresa ya estaba ganando en el reporte óptimo inicial antes de aceptar la oferta.
2. **Precio Dual / $y_i$ ($32$):** Al leer el reporte del software, el profesor identificó que la **[[Variable Dual]]** del recurso "bobinas" era $32$. Es decir, la función objetivo crece rígidamente en $32$ por cada bobina adicional.
3. **Incremento Máximo / $\Delta b_i$ ($80$):** El profesor preguntó _"¿hasta cuántas le conviene comprar?"_. Para responder, miró el **[[Intervalo de Sensibilidad]]** en el reporte de la computadora. La columna de "Incremento Permisible" (allowable increase) marcaba exactamente $80$ unidades. Si se compran más de $80$, la base cambia y el **[[Precio Sombra]]** de $32$ pierde validez.

##### El Origen del Debate Crítico

> [!danger] La Trampa del Alumno (Ingreso Neto vs Variación de Z) El alumno en clase intentó reemplazar la parte de la fórmula $(32 \times 80)$ por $(12 \times 80)$. Su lógica era: _"Si el precio sombra es 32 pero el proveedor me cobra 20 de recargo, mi ganancia real es 12"_.

Aquí es donde el profesor introdujo la diferencia estricta entre el **[[Significado Matemático]]** y la ganancia de bolsillo. El profesor fue tajante: el modelo matemático de **[[Programación Lineal]]** es ciego al recargo de $20$ que pagas por fuera. El impacto directo e inevitable en la tabla Simplex se rige por la fórmula $Z_{nuevo} = Z_{actual} + \Delta b_i \cdot y_i$ usando la **[[Variable Dual]]** pura ($32$).

Por lo tanto, la actualización matemática correcta del software da **$19000$**. La verdadera ganancia "de bolsillo" que le quedará a la empresa es un cálculo económico posterior (gerencial) y por fuera de la matriz Simplex.


### d)
- **[[Costo Reducido]]**: Nos indica la penalización en la función objetivo por forzar la producción de un artículo que el modelo decidió no fabricar. El profesor lo ejemplificó así: _"Si decido fabricar acondicionadores de lujo, la utilidad disminuye en 24... eso sale del costo reducido"_.
- ![[{6039194E-0335-4346-BD66-F69FF8199CA5}.png]]

### E)
No le conviene contratarla;

- _Aumento de recursos inactivos:_ Se explica por qué conseguir horas extra de mano de obra no cambia en absoluto la utilidad, ya que la restricción posee una [[Holgura]] de 320 horas actuales.

En este caso si la cambiariamos estara cambiando un restriccion no limitante
* la base no cambia
* la solucion no cambia
* y la variable de holgura no cambia

ahora si se decidiara cambiar esta restriccion no limitante
![[{FC623D3F-9545-4BAE-9C86-B78C01F850B6}.png]]


# ------ Análisis Estratégico de la Clase: Énfasis del Profesor y Dudas Relevantes


## 1. Alertas Críticas y "Trampas" de Examen


> [!danger] Trampa de Parcial 2: Omisión de Restricciones de Signo en el Dual Al corregir la "Actividad 4" en el aula virtual, el profesor notó un error masivo: plantearon bien las inecuaciones pero olvidaron los signos de las variables. _"En todo problema lineal tenemos que poner la restricción de signo de las variables... si no escriben esta última parte, todo el planteo está mal"_,. **El Error:** Finalizar el armado del [[Problema Dual]] sin especificar si $y_1, y_2 \dots$ son $\ge 0$, $\le 0$ o variables sin restricción.

> [!tip] Tip de Estudio: Definición de Variables El profesor aconsejó practicar arduamente la redacción teórica de las variables: _"Así como cuesta definir las variables de holgura, muchas veces cuesta definir las variables duales. Muchas veces lo pedimos... me fijo en lo que representa la restricción y la función objetivo"_,.

---

## 2. Interacción en Clase: Preguntas Relevantes de los Alumnos

Las intervenciones de los alumnos permitieron al profesor clarificar la lógica deductiva de la [[Dualidad Mixta]] y el verdadero propósito del [[Análisis de Sensibilidad]].

### Duda A: Diferenciación entre Variables en la Interpretación

El profesor preguntó a la clase cómo definirían económicamente a la [[Variable Dual]] $y_1$ (asociada a horas de máquina).

- **Respuesta errónea de un alumno:** _"Correspondería a las horas sin usar en la máquina..."_.
- **Corrección del Profesor:** Eso es la definición estricta de una **[[Variable de Holgura]]**, no de una dual.
- **Respuesta correcta de otro alumno:** _"Sería como el máximo precio que yo estaría dispuesto a pagar por obtener una hora más"_. El profesor validó esto indicando que esa es la valoración interna o [[Precio Sombra]] del recurso.

### Duda B: Deducción de Signos en Dualidad Mixta

Varios alumnos tuvieron problemas para determinar los signos de las nuevas variables ($y_1, y_2$) al plantear el [[Problema Dual]].

> [!question] Pregunta del Alumno _"¿Puede volver a explicar cómo se da cuenta del signo de $y_1$ y $y_2$?"_.

**Respuesta y Metodología del Profesor:** El profesor explicó que hay que mirar los coeficientes y el símbolo de la restricción del [[Problema Primal]] de donde nace esa variable. Se debe evaluar la **canonicidad** de la inecuación:

1. Como el primal es un problema de [[Minimización]], su [[Restricción Canónica]] natural debería ser $\ge$.
2. Sin embargo, la restricción uno es $\le$. Al contradecir la forma canónica (es no canónica), la [[Variable Dual]] que genera debe ser "anormal", es decir, una **[[Variable No Positiva]]** ($\le 0$),.

|Tipo de Modelo Original|Condición de la Restricción|Resultado en la [[Variable Dual]]|
|:--|:--|:--|
|**[[Minimización]]**|Es $\ge$ (Es **[[Canónica]]**)|$y_i \ge 0$|
|**[[Minimización]]**|Es $\le$ (Es **No Canónica**)|$y_i \le 0$|
|Cualquier Modelo|Es $=$ (Es **Igualdad**)|**[[Variable Sin Restricción de Signo]]**|

_(Nota: En la clase un alumno preguntó exactamente por qué $y_4$ no tenía restricción de signo, y el profesor confirmó que era por surgir de una ecuación de igualdad)._

### Duda C: El Debate del Ingreso Neto vs. Variación de Z

Esta fue la interacción más crítica de la clase ("la pregunta del millón", según el profesor), ya que expone un error gravísimo de interpretación en el [[Análisis de Sensibilidad]],.

**Contexto del Ejercicio:** Se ofrece comprar bobinas a $20$ de recargo sobre el costo actual. El reporte indica que la disponibilidad se puede aumentar en 80 unidades. El [[Precio Dual]] arrojado por la máquina es $32$.

> [!question] La Confusión del Alumno _"Yo no entendí muy bien... lo que hice fue multiplicar $80 \times 12$ [la diferencia entre el precio dual 32 y el recargo 20]... no entiendo por qué estaría mal calcular así el nuevo valor de Z"_.

**La Resolución del Profesor:** El alumno estaba confundiendo el **resultado económico real (ganancia neta)** con el **incremento matemático puro** del modelo.

- El [[Significado Matemático]] dicta que por cada unidad extra del [[Lado Derecho]], la [[Función Objetivo]] ($Z$) reportará un aumento rígido igual al [[Precio Dual]] (en este caso, aumentará $32$ por unidad),.
- Si tú lograste pagar el recurso a $20$, la diferencia de $12$ es una ganancia económica tuya, "de bolsillo". Pero matemáticamente, si vuelves a cargar el problema en la computadora cambiando la disponibilidad original por 80 más, el software mostrará que $Z$ creció usando el factor de $2$, porque el software no sabe a cuánto negociaste el nuevo precio por fuera,,.

> [!note] Fórmula del Impacto Matemático Puro $$ \Delta Z = \Delta b_i \times Precio\ Dual $$ _(No se debe restar el costo adicional dentro de esta fórmula matemática)_.

```
graph TD
    A[Oferta: 80 bobinas adicionales] --> B[Analisis Gerencial de Sensibilidad]
    B --> C[Impacto en la Computadora Funcion Z]
    B --> D[Impacto Real en el Bolsillo]

    C --> E[Se aplica el Precio Dual puro]
    E --> F[Incremento Matematico: 80 x 32]

    D --> G[Se deduce el costo adicional pagado]
    G --> H[Incremento Neto Gerencial: 80 x 12]

    H -.->|Aclaracion del Profesor| I[El objetivo del analisis de sensibilidad es tomar esta decision SIN tener que recalcular ni alterar los costos en la matriz original]
```

_Conceptos relacionados:_ [[Análisis de Sensibilidad]], [[Precio Dual]], [[Función Objetivo]], [[Lado Derecho]].

