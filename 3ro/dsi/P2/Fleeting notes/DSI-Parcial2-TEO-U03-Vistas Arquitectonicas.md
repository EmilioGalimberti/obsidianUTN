---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit: "3"
type: TEO
zk_type: fleeting
status: done
date: 2026-07-27
source:
tags:
---
---
# Vistas arquitectonicas

meles:

**Cattaneo:**

https://www.google.com/url?q=https://youtu.be/6qPDQFAiqfk&sa=D&source=editors&ust=1752246945409763&usg=AOvVaw0kxhVVvaY-fAqGTL9gDffp

https://youtu.be/w-jj9QFnnsY

https://www.google.com/url?q=https://youtu.be/zRjNr8pSe1E&sa=D&source=editors&ust=1752246945410292&usg=AOvVaw3GWeAxEGPqd2MPxsS4E4TF

https://youtu.be/E_1N9qTv2M8

---

Estas vistas son fundamentales porque no solo modelan la arquitectura del sistema, sino que también sirven como documentación esencial del mismo. Su creación se basa en los requisitos no funcionales más significativos del proyecto.

- conceptos generales
    
    Para entender las vistas, se definen tres conceptos clave:
    
    - **Modelo:** Es una descripción completa del sistema desde una perspectiva y con un nivel de abstracción determinados.
    - **Punto de vista:** Define teóricamente qué contenido tendrá una vista, su significado y cómo se representará (lenguajes, técnicas de modelado). Especifica qué información es relevante para un interesado particular (stakeholder).
    - **Vista:** Es la representación concreta del sistema desde un punto de vista específico. Se construye seleccionando elementos de uno o varios modelos para mostrar solo la información que le interesa a un stakeholder en particular, ocultando el resto de los detalles. El objetivo principal de una vista es gestionar la complejidad y facilitar la comunicación, destacando que su poder reside tanto en lo que muestra como en lo que estratégicamente oculta.
    
    <aside>
    💡
    
    Las vistas son proyeeciones de un modelo/s para un involucrado en particular y sus intereses
    
    </aside>
    
    ![image.png](image.png)
    

Como No hay un un acuerdo donde todos trabajen con las mismas vistas, se acordo con un nivel de abstraccion mas alto:

# Tipo de vistas

- Es un conjunto o categoria de vistas que pueden ser facilmente conciladas unas con otras
- Las vistas no puden ser conciliadas pertenecen a tipos de vistas diferentes

![image.png](image%201.png)

1. **Vista de Módulo:** Se enfoca en la estructura estática y la organización del código en tiempo de compilaciónDefiniciones de tipos de componetes, puertos y conectores. Un ejemplo de patrón asociado es el patrón en capas (Layered) 
2. **Vista de Ejecución:** contiene vistas de los elementos que se pueden ver en tiempo de ejecucion. Incluye escenariso de funcionalidad, listas de responsabilidad y ensambles de componentes, Muestra las instancias de los componentes (objetos) y cómo interactúan entre sí a través de conectores. Se asocia con patrones de comunicación como Publish-Subscribe o Broker y se puede ilustrar con diagramas de contexto del sistema.
3. **Vista de Distribución:** Detalla cómo el software se despliega en la infraestructura de hardware. Se enfoca en los elementos físicos y su distribución. Está relacionada con patrones de hardware como N-Tier o Map-Reduce y se representa mediante diagramas de distribución.
4. **Vista de Spanning (Transversal):** Aborda aspectos que afectan a toda la arquitectura, como los atributos de calidad (confiabilidad, seguridad, rendimiento, etc.).

El autor destaca la relación entre la **vista de módulo** (donde se definen los tipos de componentes o clases) y la **vista de ejecución** (donde existen las instancias de esos componentes u objetos). Finalmente, concluye que separar las vistas ayuda a analizar problemas de forma aislada, pero es fundamental integrarlas para obtener una comprensión completa de la arquitectura.

<aside>
💡

No todas las vistas que construyamos son significativas para la arquitectura, hay vistas que se trabajan para mostrar una situacion en particular

No todas las vistas son arquitectonicas

Las vistas que veeremos a partir de ahora, son vistas arquitectonicas

</aside>

Nostros vemos estas:

![image.png](image%202.png)

se llama 4+1 Vistas Arquitectonicas

(en verdad son 10 porque todas tienen parte estica y parte dinamica)

- porque estan unidas por los cu?
    
    Estas 4 vistas están unidas por la Vista de Casos de Uso (vista de la funcionalidad) la cual contiene los casos de uso significativos para la arquitectura. 
    
    Básicamente, capturan los requisitos para la arquitectura y, por lo tanto, están relacionados con más de una vista en particular. A partir de la Vista de Casos de
    Uso (vista de la funcionalidad) se van a construir las demás vistas. Con esto se aplica la característica de PUD “Conducido por casos de uso” porque de cada caso de uso, se va derivando la traza con los otros modelos que nos interesa mostrar y evolucionar.
    
- Vista de Casos de Uso o funcionalidad: Solo muestra los casos de uso que yo coinsidero que son significativas para la arquitectura 
describen el comportamiento del sistema tal y como es percibido por los usuarios finales,
analistas y encargados de pruebas
    - Representaciones:
        - Estática: Diagrama de casos de uso.
        - Dinámica: Diagrama de secuencia o de comunicaciones.
    - importancia: Actúa como base para las demás vistas y representa los requerimientos funcionales clave
    - como determinabamos que cu son escenciales para la arquitectura
        
        [2025-07-11 15-12-43.mkv](2025-07-11_15-12-43.mkv)
        

---

ahora el resto de vistas se construyen apartir de la vista de cu, entonces yo despues armo la vista de diseño pero con el foco de que clases son relevantes para la arquitectura, que resuelvan los casos de uso que estan incluidos en la vista funcional

---

- Vista De diseño: describe los elementos significativos de la arquitectura y las
relaciones entre ellos. Describe cómo será provista la funcionalidad del sistema, qué clases, interfaces o colaboraciones  voy a utilizar para darle soporte a la funcionalidad. La vista lógica captura la estructura de la aplicación usando diagramas de clases o equivalentes.
    - Representaciones:
        - Estática: Diagrama de clases, Diagrama de componentes.
        
        ![Diagrama de componentes](image%203.png)
        
        Diagrama de componentes
        
        - Dinámica: Diagrama de secuencia.

- QUE ES UN COMPONENTE?
    
    ES UN TIPO ESPECIAL DE CLASE, pero es unico “fisico” ya que reperesenta una pieza de codigo
    

uml tenia dos diagramas fisicos

diagrama de componetes

diagrama de despliegue

![image.png](image%204.png)

- Que representan los nodos?
    
    Representan hardware, unidades de procesamiento o almacenamiento
    

---

- Vista de implementación (componentes): Esto captura la organización interna de los
componentes de código, normalmente cuando se mantienen en un entorno de desarrollo o herramienta de gestión de la configuración. Describe también las dependencias de los módulos de implementación (código fuente, bibliotecas, componentes de terceros).
    - Estatica: Diagrama de componentes
    - Dinámica: Diagrama de secuencia.
- implemetnacion concepto
    
    es bajar un diseño a un lenguaje de programacion
    

---

- Vista del proceso: se centra en describir la concurrencia y elementos de comunicación de una arquitectura. En las aplicaciones de TI, las principales preocupaciones están describiendo componentes multiproceso o replicados, y los mecanismos de comunicación síncronos o asíncronos utilizados.
- hacen foco en aspecto de req no funcionales asociados a clases activas (las que llevan el hilo conductor de la ejecucion)
    - Representaciones:
    o Estática: Diagrama de componente.
    o Dinámica: Diagrama de secuencia.

---

- Vista física (De despliegue): Esto describe cómo los principales procesos y componentes se asignan al hardware de las aplicaciones. Muestra cómo el software será alojado en los diferentes componentes de hardware. Podría mostrar, por ejemplo, cómo se distribuye la base de datos y los servidores web de una aplicación en varias máquinas servidor.
    - Estatica: Diagrama de despliegue
    - Dinámica: Diagrama de secuencia.

![image.png](image%205.png)

<aside>
💡

Para el tema de diagramas

Estatica: la unica que usa diferente es la de despliegue → diagrama de despliegue

y la de diseño puede usar diagrama de clases o componentes

y despues todas comoponentes

Dinamica: todas diagrama de secuencia, solo la de funcionalidad de secuencia o comunicacion

</aside>

<aside>
💡

agrega meles que no siempre hace falta construir todas estas vistas y que en algunos casos podemos necesitar mas, recomienda la vista de datos donde muestra como se mapea contra base de datos relacionales, o por ejemplo la necesidad de una vista de seguiridad por un rnf significativa para la arquitectura y este seria de tipo transversal

![image.png](image%206.png)

</aside>

---

Ahora relacionado lo de las vistas 4+1 con los tipos de vista

- Vista de modulo
    - Las vistas estaticas
- Vista de ejecucion
    - Las vistas dinamicas
- Vista de Distribucion
    - Vista de Despliegue

![image.png](image%207.png)

<aside>
💡

EN EL PRACTICO SOLO TRABAJOMOS CON VISTAS ESTATICAS Y 3 VISTAS (IGUAL PREGUNTAR)

</aside>

# EJEMPLO DE FANATICOS DEL FUTBOL (monolitico) →(vista funcionalidad, vista de diseño)

Repaso del ej

https://youtu.be/6qPDQFAiqfk?si=iN3I_DBBd6D4_xp-&t=3767

[2025-07-11 16-12-11.mkv](2025-07-11_16-12-11.mkv)

Los patrones arquitectonicos que se eligieron

[2025-07-11 16-18-47.mkv](2025-07-11_16-18-47.mkv)

- 1ero vista funcional y justificacion
    
    <aside>
    💡
    
    1er Artefacto  resultanto de la vista arquitectonica que entragmoas  es esto mas la justificacion
    
    </aside>
    
    ![image.png](image%208.png)
    
    <aside>
    💡
    
    Tiene maso menos el 10% de la totalidad de cu *en verdad son 150 la totatlidad no45)
    
    </aside>
    
    ![image.png](image%209.png)
    
    ![image.png](image%2010.png)
    
    ![image.png](image%2011.png)
    
    ![image.png](image%2012.png)
    
    y ademas de transaccion compleja se muestra que se eligio el cu 40 para resolver el rnf 7 cobro por rapipago y pago facil
    
    <aside>
    💡
    
    La arquitectura no solo se trata de cuestiones no funcionales, porque las cuestiones no funcionales estan implemetnadas en la funcionalidad, no se puede entregar solo entregarle rnf no tiene sentido, entonces simepre todos estos los vemos aplicado en algun caso de uso, funcionalidad
    
    </aside>
    
    ![image.png](image%2013.png)
    
    ![image.png](image%2014.png)
    
    ![image.png](image%2015.png)
    
    ![image.png](image%2016.png)
    
    Cambio esto
    
    ![image.png](image%2017.png)
    
    ![image.png](image%2018.png)
    
    <aside>
    💡
    
    Cuanto esta asi solo es un cu TEMPORAL
    
    </aside>
    
    ![image.png](image%2019.png)
    
- PUEDE PASAR QUE SE ELIJAN CU QUE NO RESUELVAN NINGUN RNF?
    
    [2025-07-11 20-28-59.mkv](2025-07-11_20-28-59.mkv)
    
- COMO UN REPASO:
    
    [2025-07-11 20-30-55.mkv](2025-07-11_20-30-55.mkv)
    

---

- QUE ES UN DIAGRAMA DE COMPONENTES
    
    ![image.png](image%2020.png)
    
    puedo encontrar componentes, susbsitemas, paquetes
    
    - componentes
        
        ![image.png](image%2021.png)
        
        Para uml este es un componente
        
        ![image.png](image%2022.png)
        
        y utiliza la misma notacion para subsistema
        
    
    <aside>
    💡
    
    recordatorio el diagrama de componentes y el diagrama de desplieuge son los unicos dos diagramas fisicos, en el caso del de componentes es codigo, es la representacion fisica de codigo
    
    </aside>
    
    Relaciones:
    
    ![image.png](image%2023.png)
    
    - INTERFACES:
        
        La interfaz es un tipo especial de clase abstracta,
        
        Es una clase que tiene declarado comportamiento vacio, todos sus metodos son abstractos (que solo tienn la firma del metodo y dentro no tienen comportamiento)
        
        todos sus metodos estan declarados pero vacios
        
        La diferencia con la clase abstracta
        
        es que la clase abstracta, en un una relacion de herencia, puedo tener metodos vacios pero tambien puedo tener metodos implementados
        
        Una interfaz siempre debe apárecer asociada algo como en el grafico, porque osino no tiene sentido si aparece sola
        
    - Interfaces provistas y requeridas
        
        ![image.png](image%2024.png)
        
        La -C  es la interfaz requerida, un componente le esta pidiendo servicios a otro comoponentes
        
        el -O es la interfaz provista, por ejemplo el componente producto ofrece el comportamiento que esta provisto en la interfaz Item Code Y el compomente Order necesita ese servicio
        
        <aside>
        💡
        
        El nombre de la interfaz provista debe ser el mismo nombre que la interfaz requerida
        
        - Tambien otra consideracion para las conexiones si estan cercamos la unimos y osino usamos los que son interfaces expuestas que quedansin unir pero deben tener el mismo nobmre
        </aside>
        
- Vista arquitectonica del diseño: Subsistemas y componentes
    
    https://youtu.be/zRjNr8pSe1E?si=I1CZJoEjbFs7e_ON&t=3001
    
    <aside>
    💡
    
    solo deben ir los componentes que yo necesito para resolver las cuestiones arquitectonicas que deje planteada en la vista anterior
    
    Muestar todos los componentes? No, solo muestra representantes
    
    </aside>
    
    1ero patron layered aplicado y explica el tema de la persistencia
    
    - Decision que afecta a toda la arquitectura, no se le asocio un cu
        
        [2025-07-14 09-34-16.mkv](2025-07-14_09-34-16.mkv)
        
    - Para resolver el cu 8. iniciar sesion (este y el anterior casi siempre se resuelven parecidos
        
        ![image.png](image%2025.png)
        
        dentro de gestionUusuarios estos no son los unicos componentes, si no que son los mas importantes por ahora para destacar
        
    - ABM
        
        ![image.png](image%2026.png)
        
    - y ahora para el 20 de diagramar fixture de campeonato
        
        ![image.png](image%2027.png)
        
        ![image.png](image%2028.png)
        
        “El fixture es basicamente el que diseña un campeontao, dice este es mi club, con que club juega, que dia que hora”
        
    - broker
        
        ![image.png](image%2029.png)
        
        El ImportadorMinAmin es el broker, el que va a tomar lo que le da el serviceDataFactory   y lo va a transformar, es el que ofrece el EventoPartido, que despoes en la gestion de campeonato lo va a tomar
        
        El componente EventoPartido → provee la interfaz EventoMinAmin, para dar esa informacion a otro componente que lo requiera
        
    - porque tengo interefaces asociadas a subsistemas o a componentes especificos?
        
        cuando la interfaz esta en el subsistema es porque mas de un componente lo utiliza
        
        y cuando es espeficio es especifico de un componente
        
    
    ![image.png](image%2030.png)
    
    ![image.png](image%2031.png)
    
    ![image.png](image%2032.png)
    
    Importador de cobros ofline es el broker
    
    ![image.png](image%2033.png)
    
    lo pintoo porque no necesita persistencia
    
    ![image.png](image%2034.png)
    
    - Publish and suscribe:
        
        ![image.png](image%2035.png)
        
    
    SOLUCION FINAL
    
    ![image.png](image%2036.png)
    
- QUES UN DIAGRAMA DE DESPLIEGUE
    
    ![image.png](image%2037.png)
    
    ES EL UNICO DIAGRAMA de uml que modela hardware
    
    ![image.png](image%2038.png)
    
    ![image.png](image%2039.png)
    
    ![image.png](image%2040.png)
    
    ![image.png](image%2041.png)
    
    ![image.png](image%2042.png)
    
    el de abajo a la derechae s un diagrama de despliegeu para mostras solo hardware (este no usamos)
    
- VISTA DE DESPLIEGUE
    
    ![image.png](image%2043.png)
    
    ![image.png](image%2044.png)
    
    ![image.png](image%2045.png)
    
    ![image.png](image%2046.png)
    
    Notar que en mos mobile va el subsistema completo, en cambio en lo web al trabajar con cliente livano lo unico que necesita es un broweser (esta pintado de otro color porque no lo contruimos nostros) al igual que el servidor web
    
    - porque el webserver no aparecio en la vista de diseño?
        
        no aparece porque no es algo que construyamos nostoros seguramente ya traigamos algo ya echo cmo un apache etc
        
    
    ![image.png](image%2047.png)
    
    ![image.png](image%2048.png)
    
- vista arquitectonica del despliegue (solo hardware) ESTA NO NOS TOMAN
    
    ![image.png](image%2049.png)
    

<aside>
💡

LOS rnf pueden no darlos para un final por ejemplo

</aside>

# Ejemplo Fanaticos del futbol(micro servicios)

[DSI CONVENCIONES DE MODELADO.pdf](DSI_CONVENCIONES_DE_MODELADO.pdf)




---
# References
## Father
## child