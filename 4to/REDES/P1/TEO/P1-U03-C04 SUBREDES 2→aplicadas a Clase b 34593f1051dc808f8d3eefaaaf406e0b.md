
ip- Clase 4 RIN I 16-Apr I Teórico I Direccionamiento IPv4: Parte 3 [![](https://www.youtube.com/s/desktop/70bc5332/img/favicon_144x144.png)Clases Virtuales UTNRIN I 16-Apr I Teórico I Direccionamiento IPv4: Parte 3](https://youtu.be/e8fRLbclVp4?si=JpKBeKUepXQ7AAa4)​

# P1-U03-C04 SUBREDES →aplicadas a Clase b

A continuación, se detalla el esquema cronológico de la clase, estructurado según el orden en el que el profesor fue desarrollando los temas:

#### **1. Introducción y Repaso de Subredes (Clase B) (0:00 - 6:37)**

En esta clase el foco principal del direccionamiento práctico se centró en las redes de **Clase B**, cuya máscara por defecto es `/16` (con 16 bits para red y 16 bits disponibles para hosts)

![{2DE17C2F-57F8-484B-9B93-C5339A669CF8}.png](2DE17C2F-57F8-484B-9B93-C5339A669CF8.png)

> **Creación de subredes (Clase B):** Consiste en pedir "bits prestados" de la porción de host (del tercer y/o cuarto byte) para crear nuevas subredes. Se calcula la cantidad de subredes con la fórmula $2^n$ (donde *n* son los bits prestados) y los hosts válidos con $2^n−2$ (donde *n* son los bits que quedan para hosts)
> 

![{87E02DEF-D0D2-4ABE-A636-BBA9E86BC9CC}.png](87E02DEF-D0D2-4ABE-A636-BBA9E86BC9CC.png)

- Pregunta: CUANTOS HOST podemos tener en la red 180.5.0.0/16?
    
    hosts válidos con $2^n−2$ (donde *n* son los bits que quedan para hosts)
    
    al no tener subredes, permiten direccionar hasta 65.534 hosts ($2^{16}−2$)
    

![{D0734887-D034-407F-84C5-3F734B19EFC1}.png](D0734887-D034-407F-84C5-3F734B19EFC1.png)

#### **2. Máscaras de Subred en Clase B (6:37 - 9:42)**

- Explica que la máscara por defecto de una red Clase B es `/16` (o `255.255.0.0`).

![{C08E22B2-C7BE-4318-ABEF-144AE564E272}.png](C08E22B2-C7BE-4318-ABEF-144AE564E272.png)

- Muestra cómo el valor del tercer y/o cuarto byte de la máscara va cambiando (tomando valores como `224`, `248`, `192`, etc.) a medida que se encienden los bits que se toman prestados para subredes.

![{FC281B82-D27C-4216-B49F-35E5C70B2EC6}.png](FC281B82-D27C-4216-B49F-35E5C70B2EC6.png)

#### **3. Cálculo de Direcciones y Rangos (9:42 - 19:42)**

- Plantea un ejemplo tomando 4 bits prestados y enumera las direcciones de las primeras subredes (Subred 0 a la 9).
- Explica paso a paso cómo calcular el rango de direcciones IP válidas para la "Subred 2", determinando su límite inferior y superior, así como su dirección de broadcast.

CALCULO DE DIRECCIONES DE SUBREDES:

![{50F1603D-AF66-44B9-AA09-2293C866BFCA}.png](50F1603D-AF66-44B9-AA09-2293C866BFCA.png)

la direccion de la subred 0 coincide con la direccion de la red , pero notar que las diferencian las mascaras

<aside>
💡

solo la mascara puede distinguir una direccion de red contra una direccion de subred

</aside>

y porque es barra 20? porque tengo /16 de la mascara por defecto y se pidieron 4 prestados 16+4=/20

Basicamente: vamos calculando todas las combinaciones posibles, y vamos pasandolas de binario a decimal

![{6CF0285E-D23C-422A-998C-9072AC06A860}.png](6CF0285E-D23C-422A-998C-9072AC06A860.png)

![{B9B105AF-1BE9-4089-85B8-69653480799B}.png](B9B105AF-1BE9-4089-85B8-69653480799B.png)

![{8E651719-D55A-40A6-B408-F95D31E8A592}.png](8E651719-D55A-40A6-B408-F95D31E8A592.png)

y asi seguriamos hasta la subred 15

<aside>
💡

los valores en rojo, por ejemplo 0110 → dan 6 y es el numero de la subred

</aside>

---

RANGO DE CADA SUBRED: POR EJEMPLO DE LA SUBRED 2

![{926C54D4-A48C-4396-A186-C188C4444BB4}.png](926C54D4-A48C-4396-A186-C188C4444BB4.png)

para hallar el rango de ip validas vamos jugando y cambiondo los 0 por 1

EL RANGO SERIA $2^{12}-2$ =4094 → rango de ips validas

<aside>
💡

**El cálculo de los límites del rango en la Clase B (Error típico):** Advierte con mucho énfasis ("cuidado") sobre un error muy común de los alumnos al calcular el rango de direcciones IP válidas. Alerta que los estudiantes suelen hacer variar únicamente el último byte, olvidando que en las redes Clase B también hay que hacer variar los bits del tercer byte., SUELEN OLVIDARSE que deben agrupar obligatoriamente de a 8 bits y sumar los valores posicionales de ambos bytes afectados.El profesor resalta que "esto es lo más complicado que puede llegar a tener en una subred clase B".

</aside>

#### **4. Ejercicio Práctico calculo de subredes clase b - Parte 1 (19:42 - 25:23)**

- El profesor da a los alumnos la IP `140.9.0.0/26` para que calculen individualmente: bits prestados, máxima cantidad de subredes, cantidad de IPs válidas por subred y el total general de IPs.

![{3E60BB1F-7FC3-4E65-A718-D028CD21EDBB}.png](3E60BB1F-7FC3-4E65-A718-D028CD21EDBB.png)

- Canitdad de bits que se pidieron prestados
    
    para saber cuantos bits se prestaron, primero identifcar la mascara por defecto que con el primer byte es 140 por tanto es clase → B que por defecto /16
    
    entonces /26-/16=10 → SE PRESTARON 10 bits
    
    ---
    
    <aside>
    💡
    
    - Al corregir, enfatiza que el paso fundamental para evitar errores es **determinar primero a qué clase pertenece la IP**, ya que al ser Clase B, su máscara base es 16 y la resta correcta de los bits es $26 - 16 = 10$ bits prestados.
    </aside>
    
- Cantidad maxima de subredes
    
    se calcula como 2^n → siendo n las cantidad de bits que se prestaron
    
    2^10=1024 → cantidad maxima de subredes
    
- Cantida maxima de direcciones ip validas por subred
    
    ![{CC36826F-1F80-4DA3-84C6-4969D021AD79}.png](CC36826F-1F80-4DA3-84C6-4969D021AD79.png)
    
    62 cantidad ip valida por c/u de las subredes
    
- cantidad total de direcciones de ip validas
    
    ![{673FA315-BABD-4790-B196-E60CFDC2EE2D}.png](673FA315-BABD-4790-B196-E60CFDC2EE2D.png)
    

#### **5. Ejercicio Práctico - Parte B: Cálculo Directo de Subred (25:23 - 35:16)**

- Pide a la clase calcular todos los parámetros (dirección de red, máscara, rango y broadcast) específicamente para la **Subred 10**.

![{CA6EC1DB-C8E1-475C-90B9-D1E81CAE2E36}.png](CA6EC1DB-C8E1-475C-90B9-D1E81CAE2E36.png)

- DIRECCION DE LA SUBRED:
    
    Primeor pasamos el numero 10 a binario
    
    <aside>
    💡
    
    - Enseña una técnica rápida: convertir el número de la subred a binario (el 10 es `1010`) y ubicarlo directamente en la porción de bits prestados acomodándolo de derecha a izquierda. Esto evita tener que hacer todas las combinaciones previas desde la subred 0.
    </aside>
    
    ![teniniendo solo en cuenta los bytes de host](16806224-43D8-451A-AED9-0254C35CA04D.png)
    
    teniniendo solo en cuenta los bytes de host
    
    Nos faltaria pasarla a decimal para tener la direccion de red:
    
    140.9.2.128 direccion de SUBRED 10 en decimal
    
    ![{99E9C47F-CFBF-4B6A-B29E-A01110F2F75B}.png](99E9C47F-CFBF-4B6A-B29E-A01110F2F75B.png)
    
- mascara de subred:
    
    TODAS DEBEN TENER LA MISMA MASCARA POR LO TANTO SERIA
    
    /26
    
    que en binario seria
    
    11111111.1111.1111.10000000
    
    ![faltaria pasarla a decimal](aa5bbbf4-bbaf-41c0-9fb5-0c6daa016d69.png)
    
    faltaria pasarla a decimal
    
- rango de direcciones validas es
    
    2^n-2 → 2^6-2 = 62
    
- direccion de brodcast
    
    00000010.10111111
    
    ![{722D00E0-E9ED-4108-8584-48BC2748E3E2}.png](722D00E0-E9ED-4108-8584-48BC2748E3E2.png)
    

<aside>
💡

Todo esto teniendo solo en cuenta los dos ultimos bytes que son los que cambian

</aside>

#### **6. Resolución de Problemas en una Topología (35:16 - 48:36) (NO LO HICE, PRACTICAR)**

![{C909E43D-A84D-418D-BC2B-78C2CBFC5786}.png](C909E43D-A84D-418D-BC2B-78C2CBFC5786.png)

---

El profesor planteó un escenario práctico con una topología compuesta por dos redes locales (LAN 1 y LAN 2) interconectadas, donde los alumnos debían identificar y analizar dos problemas de conectividad específicos:

- **1. Problema de la Máquina C (Sin conectividad en la LAN 1)**
    - **El planteo:** Se presentó la **Máquina A** (con IP `180.5.67.100`) y la **Máquina C** (con IP `180.5.80.200`), ambas configuradas teóricamente para la LAN 1, compartiendo la misma máscara (`255.255.240.0`) y el mismo Gateway o Puerta de Enlace (`180.5.64.1`). El problema consistía en que la Máquina C no lograba comunicarse con ninguna otra máquina de su propia red.
    - **La demostración y resolución:** A simple vista los números parecían cercanos, pero el profesor utilizó la **operación AND booleana** para demostrar la falla.
        
        > ***Operación AND booleana:** Es un cálculo lógico bit a bit (multiplicación binaria) que se realiza entre una dirección IP y su máscara de subred para descubrir matemáticamente la dirección de subred exacta a la que pertenece un dispositivo. Es fundamental para resolver problemas de conectividad.*
        > 
        
        <aside>
        💡
        
        REcomendacion: pasar a binario solo los bytes conflictos, en esta caso al ser clase B, lo unicos que van a cambiar son los ultimos 2
        
        </aside>
        
        - Al calcular la subred de la Máquina C (comparando su IP `180.5.80.200/20` con la máscara), descubrió que pertenecía a la **subred `180.5.80.0` (Subred 5)**.
            
            ![{74C78F7D-E681-411C-A3D4-69B81F8FF35F}.png](74C78F7D-E681-411C-A3D4-69B81F8FF35F.png)
            
        - Al calcular la subred del Gateway (`180.5.64.1/20`), determinó que este pertenecía a la **subred `180.5.64.0` (Subred 4)**.
            
            ![{46EB27A1-CEC3-48B7-AA00-FE0E2B581D6D}.png](46EB27A1-CEC3-48B7-AA00-FE0E2B581D6D.png)
            
    - **Conclusión del error:** El problema físico era nulo (los cables y equipos funcionaban), pero a nivel lógico **la Máquina C tenía asignada una IP que la ubicaba en una subred completamente distinta** a la de su Gateway y a la de la Máquina A. Al estar fuera de rango, quedaba sin ningún tipo de conectividad, ni siquiera local
- **2. Problema de la Máquina D (Sin conectividad fuera de la LAN 2)**
    - **El planteo:** En la LAN 2, la **Máquina D** tenía asignada la IP `180.5.47.100` y la **Máquina F** la IP `180.5.47.200`. La diferencia radicaba en la configuración de sus puertas de enlace: la Máquina F tenía el Gateway correcto (`180.5.32.1`), mientras que a la Máquina D se le había configurado el Gateway `180.5.33.1`. El problema de la Máquina D era que sí podía comunicarse con los equipos de su propia red, pero no podía salir hacia otras redes.
    - **La resolución:** El profesor explicó que la dirección IP de la Máquina D y su máscara eran totalmente correctas, motivo por el cual **lograba conectarse con la Máquina F dentro del mismo switch local** (su LAN).
    - **Conclusión del error:** Su problema radicaba netamente en un **Gateway mal configurado**. Al tener registrada una dirección incorrecta como puerta de salida (`180.5.33.1` en lugar de la verdadera que era `.32.1`), la máquina perdía toda posibilidad de conectarse hacia internet u otras subredes.

<aside>
💡

A partir de estos ejemplos, el profesor remarcó como conclusión fundamental que **todas las máquinas de un área deben pertenecer lógicamente a la misma subred** y deben compartir siempre la misma máscara y el mismo Gateway.

</aside>

![{F4C513EC-DC69-4449-8829-A3A36A58E227}.png](F4C513EC-DC69-4449-8829-A3A36A58E227.png)

#### **7. Conclusiones Finales sobre Subredes (48:36 - 51:55)**

- Establece reglas fundamentales: todas las máquinas de un área departamental deben pertenecer a la misma subred, compartir la misma máscara y tener el mismo Gateway por defecto.
- Reitera que sin un Gateway bien configurado, un equipo queda aislado en su propia LAN.

![{B632E4F7-4988-405B-9741-B0ED5174561F}.png](B632E4F7-4988-405B-9741-B0ED5174561F.png)

---

<aside>
💡

PRACTICAR PASAR DE BINARIO A DECIMAL

</aside>