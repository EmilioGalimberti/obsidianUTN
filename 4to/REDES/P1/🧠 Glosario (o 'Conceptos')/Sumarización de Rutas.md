padre: [[CIDR]]

---
## 5. Optimización: [[Sumarización de Rutas]] (Supernetting)

Como derivado del **[[CIDR]]**, el profesor explicó cómo los routers acortan sus tablas de enrutamiento.

[[CIDR]] (Classless Inter-Domain Routing) permite distribuir direcciones IP geográficamente para facilitar la sumarización o supernetting, que implica ajustar la máscara de subred.

* Subnetting: Se alarga la máscara al desplazarla hacia la derecha, creando subredes más pequeñas.
* Supernetting: La máscara se achica al desplazarla hacia la izquierda, opuesto a subnetting

El administrador de red configura el router para la Sumarización de rutas, donde una dirección de resumen cubre múltiples direcciones IP al identificar bits coincidentes. Esto simplifica el enrutamiento, por ejemplo, la dirección 201.3.32.0/20 abarca todas las IP con los primeros 20 bits iguales.
*  En lugar de publicar múltiples redes pequeñas, el **[[Router]]** busca los bits coincidentes (hacia la izquierda) y publica una única "súper red" que las abarca a todas. Al sumarizar, la máscara se acorta (ej. de un /24 pasa a un /20). Esto reduce drásticamente el tamaño de las tablas de enrutamiento y agiliza el procesamiento

> [!question] ¿Por qué es necesario este proceso? La profesora utilizó una analogía: _"Si los invito a una cena, necesitan mi dirección. Si no la publico, nadie llega"_. Un router debe publicar ("enseñar") las redes que conoce al siguiente router. Si no se resume, enviaría tres renglones distintos; al sumarizar, envía un solo renglón, aliviando las tablas de enrutamiento del proveedor

### Metodología: [[Sumarización de Rutas]]
> [!note] El Algoritmo de Cálculo (Corte de Bits) El objetivo es encontrar una única **[[Dirección IP]]** que abarque múltiples redes.
> 1.Se identifican las direcciones a resumir y se ubica el octeto "conflictivo" (el que cambia).
> 2. Se pasan a binario y se comparan bit a bit de izquierda a derecha.
> 3.Se realiza el "corte" exactamente en el punto donde los bits dejan de coincidir.
> 4.Los bits coincidentes se copian tal cual (y definen la nueva máscara), mientras que todos los bits a la derecha del corte se ponen en cero.
### Ejemplos:
> [!note] Lógica de Cálculo de Sumarización
> Nueva_Mascara=Bits_Coincidentes_Consecutivos 
> 
> El algoritmo consiste en pasar los octetos conflictivos a binario, comparar bit a bit de izquierda a derecha y realizar un "corte" en el punto exacto donde los bits dejan de coincidir. Todos los bits a la derecha del corte se convierten en 0, y la cantidad de bits a la izquierda define el nuevo prefijo
#### ejemplo 1 
El profesor planteó un escenario donde un **[[Router]]** tiene conectadas tres redes físicas diferentes de **[Clase C]** y necesita publicarlas hacia el **[ISP]** local sin saturar las tablas de enrutamiento.
- **Redes Originales:**
    - `201.3.38.0 /24`
    - `201.3.40.0 /24`
    - `201.3.42.0 /24`
	![[{D868D4BF-6B46-4078-80E9-FCD38DA3F006}.png]]
- **Paso 1: Identificar el octeto conflictivo y pasar a binario.** El primer y segundo octeto (`201.3`) son idénticos. El conflicto está en el tercer octeto.
    - 38 → `0 0 1 0 0 1 1 0`
    - 40 → `0 0 1 0 1 0 0 0`
    - 42 → `0 0 1 0 1 0 1 0`
    ![[{CE978FC1-9DA8-45C8-8D65-EB3BD9C784D0}.png]]
- **Paso 2: Encontrar el punto de coincidencia.** El profesor hizo comparar a la clase bit a bit. Se observa que los primeros **4 bits** del tercer octeto (`0 0 1 0`) son exactamente iguales en las tres direcciones. A partir del quinto bit, ya son diferentes.
- **Paso 3: Calcular la nueva [[Dirección IP]] y el nuevo Prefijo.**
    - Se suman los bits coincidentes totales: 8 (primer octeto) + 8 (segundo octeto) + 4 (tercer octeto) = 20 **bits coincidentes**. Por lo tanto, el nuevo prefijo es **/20**.
    - Al rellenar con ceros el resto del tercer octeto, el valor binario `00100000` se convierte en 32 en decimal.
    - **Resultado Final:** El router publica una única ruta resumida: **201.3.32.0 /20**. -> DIRECCION IP DE RESUMEN
    ![[{DD302EDE-D9F3-47B9-A24E-E135F0E1A81F}.png]]
		**201.3.32.0 /20**. -> DIRECCION IP DE RESUMEN -> ABARCA A TODAS AQUEAS QUE EMPIEZEN CON LOS PRIMEROS 20 BITS IGUAES


>[!note] Un router debe publicar ("enseñar") las redes que conoce al siguiente router
![[{B834C59C-50E2-448D-9898-683DCA235899}.png]]

#### que pasa con el siguieente router? Segundo Nivel de Resumen (ISP hacia Internet)
Para demostrar la escalabilidad de la red, la profesora avanzó al siguiente salto: un **[[ISP]]** de nivel 2 recibe la ruta resumida anterior y necesita agruparla con otras para enviarla hacia la red troncal (backbone) mundial

**Redes a Sumarizar (Todas /20):**
- `201.3.32.0 /20`
- `201.3.48.0 /20`
- `201.3.96.0 /20`
	![[{BB72AB00-390B-42BE-B070-0A0D7322A2AD}.png]]
* ***Cálculo y Resultado:** Al comparar los bits en binario de 32, 48 y 96, se detecta que la coincidencia es mucho menor. Solo coinciden hasta el **bit número 17**. Al realizar el corte en el bit 17 y poner el resto en ceros, la dirección resultante que se publica hacia Internet es una "súper red" masiva: **201.3.0.0 /17**
	![[{B1F917F4-429A-4B92-A6DB-3C377F4F2A37}.png]]

>[!tip] Tip de Desempeño y Velocidad en la Troncal La profesora hizo gran énfasis en el impacto de la máscara: a medida que nos acercamos a la troncal de Internet, **la máscara se va reduciendo** (de /24 a /20, y luego a /17). Esto es vital para la velocidad de procesamiento: un router central masivo solo necesita leer los primeros 17 bits del paquete para saber hacia dónde encaminarlo, sin perder tiempo analizando los 32 bits completos

Esto se aplica a nivel ISP, donde se leen más bits a medida que se acerca al destino, buscando un enrutamiento geográfico eficiente y minimizando la lectura de bits. La máscara se reduce en la troncal de Internet. Esto es válido tanto para IPv4 como para IPv6.
### ---

Tabla de Variación de la Máscara

| Tecnología                         | Modificación de la [Máscara de Subred]          | Efecto en la Tabla del Router                             |
| ---------------------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| **Subnetting**                     | Se desplaza hacia la **derecha** (se alarga).   | Aumenta la cantidad de renglones (rutas específicas).     |
| **Supernetting**<br>(sumarizacion) | Se desplaza hacia la **izquierda** (se acorta). | Reduce los renglones (resume múltiples rutas en una sola) |
