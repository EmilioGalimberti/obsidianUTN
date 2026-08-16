---
aliases:
  - DSI-PRACTICO-PARCIAL2
subject: DSI
year: "3"
exam: PARCIAL2
unit:
type: PRACTICO
zk_type: permanent
status: in-progress
date: 2026-08-15
source:
  - https://app.notion.com/p/practico-p2-20593f1051dc80649623d8a247cd7a74
tags:
---
---

Entrada: 
* Modelo de Requerimientos
	* Requerimientos funcionales
	* modelo de cu
* Requesistos no funcionales
	* Lista de rnf
	* ERS
## 1. Detectar RNFS Siginificativos para la arquitectura
Estos es principalmente para darnos "pilares" sobre lo que vamos a construir el disenio y cosas que vamos a tener en cuenta a lo largo de todo el disenio, y principalmente la vamos a ver en la vista de dise;o y la vista de despliegue

Los RNF son cruciales porque definen la "forma" y las restricciones del sistema. Debes identificar cuáles son significativos para la arquitectura (SPA).

1.¿**Cómo identificar un RNF significativo?** Hazte estas preguntas: *(donde lo veo impactado?)*
    1. Decision sobre que lenguaje
    2. BD→ Relacion → Construcion de componentes ORM
    3. Aplicacion de patrones Arquitectonicos como:
        1. Messaging
        2. broker
        3. pub/sub
    4. Aspectos de hardware

2.**¿Me obliga a desarrollar un componente específico?** *(donde lo veo impactado?)*
- Ejemplo: "El sistema debe enviar notificaciones por WhatsApp". Esto te obliga a crear un componente
    `NotificadorWhatsApp` y un `IntegradorWhatsAppAPI`.

3.**¿Define una comunicación específica con otro sistema o hardware?** *(donde lo veo impactado?)*
    - **Interfaz de Software:** "Usar una API externa de Google Maps". Requiere un componente adaptador para esa API.
    - **Interfaz de Hardware:** "Conectarse a una balanza industrial por puerto serie". Requiere un componente que aplique patrones como Broker para manejar esta comunicación de bajo nivel.
    - **Cuidado:** Un lector de códigos de barras generalmente no es una interfaz de hardware compleja, ya que suele funcionar como un teclado. No requiere un diseño especial.
4. **¿Define la tecnología base del sistema?** *(donde lo veo impactado?)*
    - Ejemplo: "El sistema debe ser una *tecnología web*" o "debe usar una base de datos PostgreSQL". Esto define la estructura fundamental de tu despliegue.

### Ejemplos


| Nombre                                                                                                        | descripcion                                                    | spa        | porque?                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *lenguaje de programacion*<br><br>Tencologia web<br><br>modulo o tencologia mobile                            |                                                                | si<br><br> | Me lleva a tomar una desicion arquitectonica: porque me dice como todo mi sistema debe responder a una tecnologia en particular                                                                                                     |
| *Base de Datos*                                                                                               |                                                                | SI         | ORM<br>**aca falta lo de bd shadow no me acuerdo como era, es mas para el despliegue**                                                                                                                                              |
| *Comunicacion con algun externo*<br><br><br>(**interfaz con externo, integracion)<br>o broker (REPASAR)**<br> | 🔻google maps<br>🔻 whatsapp<br>🔻mail<br>🔻 sms<br>🔻hardware | SI         | Debe construirse un [[Componentes\|Componente]] de<br>software para gestionar la importación de los datos de diferentes tipos de formatos <br>* registrados en los distintos Monitores.<br>* notif via sms<br>* tecnologias<br><br> |
| notificaciones push                                                                                           |                                                                | SI         | componente que permita resolver                                                                                                                                                                                                     |
| claves de incriptacion<br><br>*librerias externas*                                                            |                                                                | si         | Se deben desarrollar<br>algoritmos de<br>encriptación                                                                                                                                                                               |
| Despliegue en la nube<br><br>*hardware*                                                                       |                                                                | Si<br>     | Se deberá hacer uso del<br>patrón **Multiple Service<br>Per Host**  o puede ser tambien **SINGLE service per host**                                                                                                                 |
| seguridad usuario                                                                                             |                                                                | SI         | MODULO ESPECIAL                                                                                                                                                                                                                     |
| visualizacion de reportes e inforems                                                                          |                                                                | NO         | OJO ACA generalmente NO,<br><br>ahora en el ej de campo si diria que se conecta con google maps para mostrarlo en google maps SI SERIA SPA e implica un desarrollo arquitectonico<br>**broker**                                     |
| diferentes tipo de exploradores<br><br>tipos de archivos                                                      |                                                                | NO         |                                                                                                                                                                                                                                     |
| Exportación<br>de Reportes a<br>PDF y Excel                                                                   |                                                                | NO         | si tu lenguaje lo soporta                                                                                                                                                                                                           |
| comunicacion mediante vpn                                                                                     |                                                                | no         | Tengo que hacer algo en mi sistema para poder resolver este rnf? NO                                                                                                                                                                 |

---
# Vista arquitectonica de la funcionalidad
![[Pasted image 20260815152058.png|454]]
aca debo cumplir primero todos los de abajo, asociarles los rnfs spa y si nos sobran rnfs spa lo resolvemos con el paso 5

* diagrama de cu
	* +
* Justificacion de eleccion
## 2. Eleccion y Justifiacion 
---

### Criterios de Selección (en orden sugerido):

1. **Un ABMC Complejo(4):** Elige un Alta, Baja, Modificación y Consulta que sea representativo y complejo. Generalmente, manejan información de definición (ej: lotes, tipos de suelo, clientes). No elijas el más simple.
    1. La justificación debe incluir aspectos como: manejo de ingreso de datos, verificaciones, registro, conexión y acceso a la base de datos, algoritmos básicos, diseño de interfaz y experiencia de usuario
*POR EJEMPLO:*

|     |     |
| --- | --- |
|     |     |
2. **Una Transacción Significativa(1):** La más compleja y representativa del negocio (ej: "planificar misión", "registrar llamada"). Implica procesamiento, intercambio de datos y es más compleja que un ABMC.
    1. Justificación: Manejo de base de datos (commits y rollbacks), algoritmos complejos de programación, manejo de RERS y logs. Esto sentará las bases para otras transacciones
*POR EJEMPLO*

|     |     |
| --- | --- |
|     |     |
3. **Reporte(1) y/o Estadística(1):** Selecciona un caso de uso de cada uno, si existen. La forma de resolverlos es distinta a las transacciones.
    1. Justificación: Implica filtrar, ordenar, paginar, calcular sobre datos, generar nueva información, visualización y acceso a la base de datos
    2. algoritmos eficientes de manejo de gran volumen de datos, cálculos, paginación y visualización
*POR EJEMPLO*

|     |     |
| --- | --- |
|     |     |
3. **Proceso Masivo y/o Automático**(1 o 2)**:** Un caso de uso que se dispare por tiempo (sin actor) o que procese un gran volumen de datos.
    1. Justificación: Manejo de procesamiento masivo de datos, impacto en la performance y disponibilidad del sistema, elaboración de datos e indexaciones en la base de datos
    2. procesamiento masivo, performance del sistema, definición de hilos de procesador, ejecución temporal
>[!danger] PAra el tema de procesos automaticoas hay que tener cuidado que aunque dega que no aplica ningun actor no significa que sea automatico, ya que este puede ser abstracto
como sabes que un cu es abstracto y cuando extiende de otro? REPASAR TODO SOBRE DIAGRAMA DE CUhttps://www.youtube.com/watch?v=fJa3cshrFWs



*POR EJEMPLO*

|     |     |
| --- | --- |
|     |     |
4. **Manejo de Sesión:** Generalmente "Iniciar Sesión", para resolver el acceso según perfiles.
    1. Justificación: Resuelve el acceso al sistema, administración de usuarios, acceso según perfiles y permisos, y requerimientos de seguridad
*POR EJEMPLO*

|     |     |
| --- | --- |
|     |     |
5. **Resolución de RNF:** Si un RNF no está cubierto por los casos anteriores, agrega un caso de uso específico para resolverlo. Si un caso de uso ya elegido lo resuelve, simplemente asócialo.
*POR EJEMPLO*

|     |     |
| --- | --- |
|     |     |



## 3. Vista de CU o funcionalidad
----

- **Sistemas Externos:** Servicios como `Correo`, `GPS` o `Google Maps` deben aparecer como **actores secundarios**.
- **Actor Tiempo (NO AGREGARLO):** Si un proceso es automático, **no lleva actor**. (ojo que puede ser abstracto si no tiene actor)
- **Herencia:** Solo los actores humanos heredan de "Usuario". Un sistema externo o un dispositivo de hardware (ej: Sismógrafo) no lo hace.

*EJEMPLO*

### recordatorio del teo (IGUAL DSP SACARLO DE ACA)
- Vista de Casos de Uso o funcionalidad: Solo muestra los casos de uso que yo coinsidero que son significativas para la arquitectura  
    describen el comportamiento del sistema tal y como es percibido por los usuarios finales,  
    analistas y encargados de pruebas
    - Representaciones:
        - Estática: Diagrama de casos de uso.
        - Dinámica: Diagrama de secuencia o de comunicaciones.
    - importancia: Actúa como base para las demás vistas y representa los requerimientos funcionales clave
# DUDAS
- Para **identificar si son complejos**, leer la descripcion del cu, por ejemplo suelen tener otras clases asociadas haciendolos mas complejos.
- Si tenemos dos abmc o transacciones a la primera transaccion la consideramos un poco mas compleja que la segunda, pero esta segunda transaccion le podes asociar mas rnf, con cual nos quedamos?
    - Mejor elegir complejo y dsp agrar mas cu
- Si es automatico no lleva actor (atento de que si no tiene actor tambien podria ser un cu abstracto) y si es abstracto extenderlo del cu que sea mas parecido