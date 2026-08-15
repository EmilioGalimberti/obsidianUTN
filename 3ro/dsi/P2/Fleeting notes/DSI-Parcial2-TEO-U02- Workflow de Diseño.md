---
subject: DSI
year: "3"
exam: PARCIAL2
unit: "2"
zk_type: fleeting
status: done
date: 2026-07-23
tags:
type: TEO
---
---
[08 DSI Intro Diseño.pdf](08_DSI_Intro_Diseo.pdf)

[DSI 3K3 - Diseño - Aspectos que se diseñan -  2024.pptx](DSI_3K3_-_Diseo_-_Aspectos_que_se_disean_-__2024.pptx)

<aside>
💡

ver en la compu de cordoba que esta clase la tengo grabada o pedirla

porque en esta es la ultima clase que da antes del parcial la profe cattano, no la agrega porque profundiza , mucho en artefactos, roles, trazabilidad y me parece que ya no se toma tanto todo eso, igual lo dejo aca para profundizar dsp 

https://www.youtube.com/watch?v=d69ycx_f-Wo

</aside>

https://www.youtube.com/watch?v=Rng8xmqeFek

en el contextod de pud: el diseño empieza una vez finalizado el analisis

es decir que tenemos como entrada al proceso de diseño, un modelo logico, que en nuestro pud es el modelo de analisis

- el analisis solo se habia ocupado del los requerimientos funcionales
- ahora el proposito del diseño es transformar ese modelo logico en un modelo fisico
![[Pasted image 20260727192915.png]]
![[Pasted image 20260727192929.png]]
![image.png](image.png)

![image.png](image%201.png)

---

- definicion de diseño
    
    Es un proceso iterativo que transforma un modelo logico en un modelo fisico, tenienod en cuenta las retricciones del negocio(la tecnologia, la implementacion, aspectos de calidad)
    
    es iterativo este tambien se va ir refinando en el tiempo
	    ![[Pasted image 20260727192940.png]]
	    ![[Pasted image 20260727192949.png]]
    ![image.png](image%202.png)
    
    ![image.png](image%203.png)
---
- proposito del diseño✔
	    ![[Pasted image 20260727193000.png]]
    ![image.png](image%204.png)
    ![[Pasted image 20260727193006.png]]
    ![image.png](image%205.png)

---
- modelo de diseño
    ![[Pasted image 20260727193016.png]]
    ![image.png](image%206.png)
    
- diferencia entre el analisis y el diseño
    ![[Pasted image 20260727193027.png]]
    ![image.png](image%207.png)
    ![[Pasted image 20260727193033.png]]
    se adapta el modelo de analisis a la implementacion
    
    ![image.png](image%208.png)
    
- analisis y diseño en el pud
    ![[Pasted image 20260727193041.png]]
    ![image.png](image%209.png)
    
    antes deciamos que los requerimientos representaban el que y el analisis el como
    
    ahora
    
    el analisis representa el que (porque son la solucion a los requerimientos funcionales) y el diseño el como, (nose dice como desde el punto de viste de RNF escenciales para la arquitectura, vamos a atender ese RF
    

aca seguimos refinnado, es decir incorporamos mas detalles  es decir tiene menos abstraccion

el modelo de diseño es mas detallado que el modelo de analisis y comienza a tener mas cosas en cuenta (retricciones de implementacion, rnf, estructura, tecnologia)

---
se mantiene el analisis separado para hacer implementado en distintac tecnologias, es decir

que para un mismo modelo de analisis puedo plantear distintas dise;os que me resuelvan el problema de maneras diferentes



entonces del dise;o el modelo fisico que tenemos es para algo en particular (por ejemplo una infraestructura)

---
- que aspectos deben diseñarse? →preg de parcial ✔
    ![[Pasted image 20260727193051.png]]
    ![image.png](image%2010.png)
    
    - diseño arquitectonico (este es el principal)
        
        se debe empezar por este y luego sigen los otros, ya que los otros son mas detallados y deben respetar la arquitectura
        ![[Pasted image 20260727193106.png]]
        ![image.png](image%2011.png)
        
        - que hace la arquitectura?
            
            es el modelo que le da repuesta los rnf escenciales para la arquitectura
            
        ![[Pasted image 20260727193115.png]]
        ![image.png](image%2012.png)
        
    - diseño de datos
	    ![[Pasted image 20260727193125.png]]    
        ![image.png](image%2013.png)
        
        diseñamos la persistencia , que de un cambio de paradigma vaya al otro
        ![[Pasted image 20260727193137.png]]
        ![image.png](image%2014.png)
        
    - diseño de procesos
        
        pofundizar lo que iniciamos a nivel de realizacion de cu de analisis para considerar otro aspectos que no teniamos en  cuenta y crear la realizaicon de cu de diseño
        ![[Pasted image 20260727193145.png]]
        ![image.png](image%2015.png)
        ![[Pasted image 20260727193151.png]]
        ![image.png](image%2016.png)
        
    - diseño de Experiencia de usuario
        
        se diseña como se comunican las personas con el software
        ![[Pasted image 20260727193158.png]]
        ![image.png](image%2017.png)
        ![[Pasted image 20260727193206.png]]
        ![image.png](image%2018.png)
        
        presnetacion pechacucha
        
    - diseño de formas de entrada/salida
        ![[Pasted image 20260727193218.png]]
        ![image.png](image%2019.png)
        
        como se ingresa, puede ser un sistema en lote(censos de poblacion), en linea(inscripciones), 
        
        sistema en tiempo real afectan en el ambiente y restricciones en tiempo estricyas
        
        depende del sistema se diseña la forma de entrada
        
    - diseño de los procedimientos manuales
        ![[Pasted image 20260727193227.png]]
        ![image.png](image%2020.png)
        ![[Pasted image 20260727193232.png]]
        ![image.png](image%2021.png)
        
    
    <aside>
    💡
    
    alguna pregunta de parcial puede ser que explique los diseño de cada uno
    
    </aside>
    
- Guia para evaluar un buen diseño
    - El diseño deberá implementar todos los requisitos explícitos del modelo de análisis, y deberán ajustarse a todos los requisitos implícitos que desea el cliente;
    - El diseño deberá ser una guía legible y comprensible para aquellos que generan código y para aquellos que comprueban y consecuentemente, dan soporte al software
    - El diseño deberá proporcionar una imagen completa del software, enfrentándose a los dominios de comportamiento, funcionales y de datos desde una perspectiva de implementación
	   ![[Pasted image 20260727193242.png]] 
    ![image.png](image%2022.png)
    
- DISEÑO como proceso del pud✔
    - PROPOSITO
        - Adquirir una compresión en profundidad de los aspectos relacionados con los
        requerimientos no funcionales y restricciones tecnológicas.
        - Crear una entrada para el workflow de implementación.
        - Descomponer los trabajos de implementación en partes manejables y permitiendo
        la concurrencia entre equipos de desarrollo.
        - Capturar interfaces entre subsistemas.
        - Crear una abstracción de la solución de diseño sin estar restringidos a una
        tecnología. → COMO SERIA ESTO?
    - El rol del Diseño en el Ciclo de Vida Iterativo e Incremental del PUD
        
        Fase de Elaboración
        ▪ Contribuye a una arquitectura estable y robusta
        Fase de Construcción
        ▪ Crear un plano para la implementación
	        ![[Pasted image 20260727193257.png]]
        ![image.png](image%2023.png)
        
    - Trabajadores y artefactos involucrados en el Diseño
	    ![[Pasted image 20260727193307.png]]    
        ![image.png](image%2024.png)
        
    ![[Pasted image 20260727193314.png]]
    ![image.png](image%2025.png)
    
    y esto es entrada tambien?
	![[Pasted image 20260727193324.png]]    
    ![image.png](image%2026.png)
    
    - Diagramas de UML 2.0 en el Diseño
        ![[Pasted image 20260727193334.png]]
        ![image.png](image%2027.png)
        ![[Pasted image 20260727193339.png]]
        ![image.png](image%2028.png)
        




---
# References
## Father
## child
[[WorkFlow DISEÑO]]