---
aliases:
subject: IOP
year: "4"
exam: PARCIAL2
unit: "6"
type: Transcripcion
zk_type: resources
status: done
date: 2026-08-18
source:
  - https://www.youtube.com/watch?v=792vQP_069M&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=25
  - https://www.youtube.com/watch?v=omgVCc7Kev0&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=26
tags:
---
---
0:00

0 segundos

es importante que los red axis men porque sería la estructura sobre la cual nosotros vamos trabajando y vieron que

0:08

8 segundos

luego los algoritmos damos como por entendidos esos conceptos básicos

0:15

15 segundos

yo ahora se los voy a nombrar de nuevo pero sin entrar en detalle que cada uno solamente para refrescar qué conceptos

0:24

24 segundos

son los que ustedes sí o sí tienen que tener luego vemos el algoritmo de árbol de expansión y árbol de expansión mínima

0:33

33 segundos

que ustedes ya lo han estado trabajando con la profesora carignano y me dijo también que han trabajado con el

0:41

41 segundos

algoritmo de la ruta más corta que es el algoritmo de dijkstra el que nosotros

0:48

48 segundos

estudiamos es el de dix luego de ver estos dos algoritmos ideal

0:55

55 segundos

aplicarlos a algunos problemas vamos a trabajar con redes de flujo de costo

1:01

1 minuto y 1 segundo

mínimo y redes de flujo de costo máximo en redes de flujo máximo y redes de

1:07

1 minuto y 7 segundos

flujo de costo mínimo en las redes el flujo de costos mínimos los problemas que nosotros estudiamos

1:15

1 minuto y 15 segundos

son los de transporte transbordo y asignación que los resolvemos con modelos lineales si no

1:22

1 minuto y 22 segundos

vamos a ver los algoritmos en transporte hay un algoritmo específico en transbordo y en la asignación también

1:33

1 minuto y 33 segundos

esos algoritmos nosotros no los estudiamos hay uno el de transporte y el de asignación que ustedes van a ver que

1:40

1 minuto y 40 segundos

está en el libro de teórico pero nosotros solamente estudiamos los problemas lineales que se utilizan para

1:48

1 minuto y 48 segundos

resolver esos problemas entonces lo que vamos a hacer es ir analizando diferentes problemas

1:56

1 minuto y 56 segundos

viendo cómo se configura el modelo lineal para cada uno de esos casos nosotros ya hemos visto

2:04

2 minutos y 4 segundos

programación lineal programación entera programación binaria bueno entonces vamos a ir viendo cómo es la estructura

2:11

2 minutos y 11 segundos

de esos problemas lineales y cómo aplicarlos a diferentes problemas si eso es lo que vemos en esta unidad de

2:18

2 minutos y 18 segundos

modelos de redes como ustedes ya han visto la parte teórica yo simplemente podría refrescar

2:27

2 minutos y 27 segundos

el tema o sea lo voy a traer de vuelta y vamos a hacer ejercitación lo que más me interesa es que ustedes resuelvan

2:35

2 minutos y 35 segundos

problemas que algunos ya han resuelto el lunes con la profesora carignano pero que sigamos resolviendo problemas que es

2:43

2 minutos y 43 segundos

lo que nos da práctica en la resolución bueno como conceptos en teoría de redes

2:51

2 minutos y 51 segundos

nosotros ahora cambiamos si la simbología cambiamos los términos con

2:59

2 minutos y 59 segundos

los que vamos a trabajar y es parte importante del estudio de la unidad que ustedes se dejan guiar y sen con los

3:08

3 minutos y 8 segundos

elementos que vamos a usar y con los nombres de cada cosa por ejemplo si

3:14

3 minutos y 14 segundos

hablamos de arcos y de nodos bueno ustedes podrían decir es el punto y la

3:21

3 minutos y 21 segundos

flecha que lo conecta bueno pero tienen nombres específicos siendo se funden se familiaricen con la anotación y por la

3:29

3 minutos y 29 segundos

definición de cada uno de estos elementos y con el nombre correcto que le tenemos que dar bueno

3:37

3 minutos y 37 segundos

arcos incidentes hacia el exterior de un vértice arcos incidentes perdón hacia el exterior de un vértice hartos incidentes

3:46

3 minutos y 46 segundos

hacia el interior de un vértice como es la anotación cómo se encuentran esto mismo lo van a ver en el libro de

3:55

3 minutos y 55 segundos

teórico definido a través de un conjunto gama siempre olvides lo mismo nos está dando el conjunto d

4:03

4 minutos y 3 segundos

de los arcos los arcos incidentes hacia el interior o al

4:10

4 minutos y 10 segundos

exterior pero con un conjunto que está conformado por los vértices entonces son

4:18

4 minutos y 18 segundos

distintas formas de mostrar lo mismo lo que nos va a estar diciendo de si las actividades por ejemplo llegan a un

4:25

4 minutos y 25 segundos

vértice o salen de un vértice con diferentes formas de escribirlo esto les va a ser muy útil también para la parte

4:32

4 minutos y 32 segundos

teórica porque hay desarrollos teóricos que se hacen sobre la base del conjunto gamma y

4:39

4 minutos y 39 segundos

otros se hacen sobre la definición de arco hibbert entonces bueno es

4:48

4 minutos y 48 segundos

importante que los reflejen estos conocimientos y que los repasan

4:55

4 minutos y 55 segundos

con respecto a los caminos a todo lo que es camino longitud de camino su camino

5:01

5 minutos y 1 segundo

valor del camino estos conceptos nosotros los podemos tener por los arcos

5:08

5 minutos y 8 segundos

o por los vértices por los arcos es cuando vemos la sucesión de arcos de la red y

5:16

5 minutos y 16 segundos

analizando un camino a través de los arcos que forman el trayecto nosotros podemos determinar la longitud y el

5:25

5 minutos y 25 segundos

valor del camino estos son dos conceptos que se les confunden mucho luego al

5:32

5 minutos y 32 segundos

analizarlo al definir los algoritmos entonces acá les marco por ejemplo estos dos conceptos longitud y valor de un

5:39

5 minutos y 39 segundos

camino que es importante que los tengan en cuenta y que los diferencia el valor del camino es sumar el valor de los

5:49

5 minutos y 49 segundos

arcos que componen ese camino mientras que la longitud es el número de arcos que lo forman entonces van a haber

5:57

5 minutos y 57 segundos

pues este tema se los voy a recordar cuando veamos por ejemplo cpm o perder la unidad siguiente

6:04

6 minutos y 4 segundos

y que ahí confunden mucho lo que es longitud con camino entonces por ejemplo

6:10

6 minutos y 10 segundos

dicen la longitud del árbol de expansión mínima ahora en los algoritmos que vamos a ver ahora

6:18

6 minutos y 18 segundos

354 pesos bueno eso está mal porque la longitud es la cantidad de arcos que

6:27

6 minutos y 27 segundos

conforman un camino nosotros lo que determinamos es el valor que el valor es la suma de los arcos que componen un

6:36

6 minutos y 36 segundos

traste un camino un árbol si a eso le llamamos valor entonces por eso aunque por ahí digan

6:44

6 minutos y 44 segundos

bueno es lo mismo no nos tenemos que familiarizar con los términos aprenderlos para no confundirlos

6:53

6 minutos y 53 segundos

lo mismo todos estos conceptos los tenemos si nosotros analizamos una red por los vértices entonces también vamos

7:01

7 minutos y 1 segundo

a tener un camino por los vértices y la longitud y el valor del camino por los verdes entonces todos estos conceptos

7:10

7 minutos y 10 segundos

importantes que los recupere y luego el teorema de optimi that de que

7:17

7 minutos y 17 segundos

fue definido por berman ganaba el maní calaba entonces el en este

7:25

7 minutos y 25 segundos

teorema es sobre el cual se basan casi todos los algoritmos que nosotros analizamos en

7:33

7 minutos y 33 segundos

estas dos unidades entonces bueno es importante que lo tengan porque si bien no estudiamos la demostración del teorema es el sustento o la base de los

7:42

7 minutos y 42 segundos

algoritmos que vemos pues no es importante que tengan en cuenta cuando una red es dirigida o no

7:50

7 minutos y 50 segundos

dirigida por ejemplo en el caso del algoritmo de dijkstra trabajamos con una red no dirigida entonces quiere decir

7:58

7 minutos y 58 segundos

que es una red como ésta que tienen acá sí donde no tenemos flechas la flecha lo que me indica la dirección que la

8:07

8 minutos y 7 segundos

actividad o lo que representa este arco va desde el nodo 4 al nodo 5 si entonces

8:13

8 minutos y 13 segundos

en este caso no tenemos una dirección definida

8:21

8 minutos y 21 segundos

bueno el tema de los ciclos porque en los algoritmos decimos que no tiene que haber ciclos entonces que tengan

8:28

8 minutos y 28 segundos

presente que es y cuando una red es conexa o cuando no es konex quien me

8:36

8 minutos y 36 segundos

puede contar bueno no no me van a contar nada por qué

8:44

8 minutos y 44 segundos

vamos a comenzar ahora si no tienen ninguna duda estos todos estos conceptos ya los han

8:53

8 minutos y 53 segundos

estado viendo y analizando así que bueno creería que no hay dudas es así

9:01

9 minutos y 1 segundo

sí sí fracción bien lo importante es que tengan presente y marquen sus apuntes

9:08

9 minutos y 8 segundos

que cuáles son los conceptos que tienen que saber si es bueno luego de eso nos

9:15

9 minutos y 15 segundos

metemos en el tema de árbol si no es lo mismo árbol que árbol de expansión qué

9:21

9 minutos y 21 segundos

árbol de expansión mínima si entonces árbol es una subred conexa que no

9:28

9 minutos y 28 segundos

contiene ciclos entonces esa

9:36

9 minutos y 36 segundos

ese árbol esa subred si puede ser una

9:42

9 minutos y 42 segundos

parte de todo el grafo original y nosotros podemos tener un árbol con un

9:51

9 minutos y 51 segundos

sector conexo de la red si ahora un árbol de expansión le agrega la característica para que sea de expansión

9:59

9 minutos y 59 segundos

que llega a todos los nodos del grafo original oa todos los nodos de la red que estamos analizando si entonces árbol

10:08

10 minutos y 8 segundos

podría tener muchos árbol de expansión ya tiene la particularidad de que tiene que llegar a todos los nodos y el árbol

10:17

10 minutos y 17 segundos

de expansión mínima le suma la característica de que es el

10:24

10 minutos y 24 segundos

de menor valor entonces en este caso por ejemplo la red

10:31

10 minutos y 31 segundos

esta red que ustedes ven acá no es conexa y una de las características de un árbol de expansión es que sea konex

10:39

10 minutos y 39 segundos

en este caso por ejemplo el problema que tiene es que tiene un ciclo bueno no tiene que tener ciclo para que sea un

10:46

10 minutos y 46 segundos

árbol de expansión tiene que ser una red conexas con n 2 y n menos una arista sin ciclos

10:54

10 minutos y 54 segundos

y al decir con n nodos quiere decir que llega a todos los nodos de la red

11:01

11 minutos y 1 segundo

si a esto le agregamos como objetivo que minimiza el valor de las ligaduras incluidas en la red entonces vamos a

11:10

11 minutos y 10 segundos

estar teniendo un árbol de expansión digna esto de nuevo es un detalle que se los

11:19

11 minutos y 19 segundos

marcó porque es pregunta de examen final teórico cuál es el objetivo del árbol de expansión si ustedes hablan con

11:27

11 minutos y 27 segundos

compañeros que han cursado en otros años van a saber que es una pregunta de

11:34

11 minutos y 34 segundos

examen el objetivo que se persigue con el árbol de expansión mínima

11:42

11 minutos y 42 segundos

entonces apunten el objetivo para también después vamos a hacer en forma comparativa

11:48

11 minutos y 48 segundos

vamos a ver el objetivo del algoritmo de la ruta más corta que muchas veces como

11:56

11 minutos y 56 segundos

que parecería que es lo mismo y nos sirve o lo que es el objetivo que tiene cada uno de los algoritmos es diferente

12:06

12 minutos y 6 segundos

bueno procedimiento para encontrar el árbol de expansión mínima repasemos el primer paso es seleccionar

12:16

12 minutos y 16 segundos

un nodo de la red puede ser cualquier nodo entonces de todos los nodos que tienen

12:24

12 minutos y 24 segundos

la red lo que generalmente hacemos es graficar los nodos solos y sin las

12:31

12 minutos y 31 segundos

aristas originales tener como base en la red original pero volver a copiar todos los nodos porque si lo hacemos sobre la

12:40

12 minutos y 40 segundos

misma red por ahí se pueden generar confusiones entonces volvemos a escribir todos los nodos de la red si y a partir

12:49

12 minutos y 49 segundos

de eso elegimos un nodo en el cual vamos a comenzar y elegimos una arista que conecte dos

12:56

12 minutos y 56 segundos

nodos cualquiera si en principio para encontrar el árbol de expansión

13:03

13 minutos y 3 segundos

mínima si lo que tenemos que hacer es buscar la arista de menor valor a partir del nodo que hemos seleccionado como

13:11

13 minutos y 11 segundos

inicio si estuviéramos tratando de armar un árbol de expansión común si podemos elegir cualquiera de las aristas que

13:20

13 minutos y 20 segundos

salen de ese nodo entonces una vez que yo conecte dos nodos a través de una arista me queda un

13:28

13 minutos y 28 segundos

conjunto que es esos dos nodos que son los nuevos conectados y el conjunto de los nodos no conectados que son todos

13:36

13 minutos y 36 segundos

los que quedan afuera esos dos nudos conectados son los primeros nodos que forman el árbol de

13:44

13 minutos y 44 segundos

expansión si elegí la arista de menor valor va a ser el primer arco o el primer la primera arista que forme parte

13:52

13 minutos y 52 segundos

del árbol de expansión mmm bueno a partir de ahí lo que tenemos que hacer es ir agregando aristas entonces

14:01

14 minutos y 1 segundo

lo que vamos a hacer es ver cómo conectar el conjunto de nodos

14:09

14 minutos y 9 segundos

conectados con el conjunto no conectado a través de una arista y siempre vamos a

14:15

14 minutos y 15 segundos

tener el criterio de elegir la arista de menor valor si hay empate en las aristas que podríamos elegir en la mínima si hay

14:24

14 minutos y 24 segundos

empate podemos elegir cualquiera que va a pasar si ante un empate yo elijo una

14:33

14 minutos y 33 segundos

arista o o 'el viejo' otra que es lo que va a cambiar va a cambiar algo o no el extremo de

14:41

14 minutos y 41 segundos

ustedes y por ahí tenemos un árbol de expansión

14:49

14 minutos y 49 segundos

mínima distinto y podemos en frente a una red obtener diferentes árboles de

14:57

14 minutos y 57 segundos

expansión porque por ejemplo si tengo tengo un

15:05

15 minutos y 5 segundos

nudo que para cualquiera de los dos lados vale 5 por ejemplo

15:12

15 minutos y 12 segundos

pero si va a 1 el siguiente vale 6 o al otro el siempre vale 2

15:20

15 minutos y 20 segundos

si elige ir es el nodo que sale para 136 y ese camino nos lo va

15:28

15 minutos y 28 segundos

a seguir más porque elegir otro camino me estoy haciendo lío yo vengo a

15:38

15 minutos y 38 segundos

127 mundo y a partir de ahí salen dos aristas de valor 5 y qué pasa si elijo

15:46

15 minutos y 46 segundos

una elijo la otra pone el que sea ahí ve qué pasa si elijo a qué pasa si elijo b las dos valen 5

15:55

15 minutos y 55 segundos

si yo elijo a y después de poder elegir otro o sea

16:02

16 minutos y 2 segundos

puedo continuar el camino pero ese camino válido de 210

16:09

16 minutos y 9 segundos

y tengo otro camino que es que a partir de la que elija voy a

16:17

16 minutos y 17 segundos

tener que ir dirigiendo la menor de los que estén conectados con los dos no pueden estar sí porque le

16:24

16 minutos y 24 segundos

decimos que se conectan a través de una sola arista bueno podrías dar o no pero en principio

16:35

16 minutos y 35 segundos

vamos a decir que no va a estar o sea que el hijo 1 o el hijo lo que pasa si

16:42

16 minutos y 42 segundos

son excluyentes o sea si el hijo 1 al ser un árbol y si el hijo otro se hace un árbol

16:49

16 minutos y 49 segundos

esos árboles van a ser diferentes o van a ser iguales son iguales

16:59

16 minutos y 59 segundos

y pasamos a los conceptos básicos de eso

17:07

17 minutos y 7 segundos

que le dije recién que tenían que tener bien presente en que van a ser igual

17:17

17 minutos y 17 segundos

en el valor mínimo del árbol de expansión si entonces el valor mínimo

17:24

17 minutos y 24 segundos

del árbol de expansión va a ser igual porque voy a estar buscando el mínimo árbol posible lo que va a pasar es que

17:33

17 minutos y 33 segundos

el dibujo de los árboles pueden ser diferentes y eso pasa puede pasar

17:42

17 minutos y 42 segundos

entonces podríamos tener dos árboles de expansión mínima si lo podemos tener

17:50

17 minutos y 50 segundos

sí los dos van a ser de valor mínimo pero su forma va a ser diferente

17:58

17 minutos y 58 segundos

y estamos de acuerdo en eso podría ser también profe

18:06

18 minutos y 6 segundos

y también el conjunto de aristas que conforme o sea un árbol o el otro sea distinto

18:14

18 minutos y 14 segundos

también claro el conjunto de aristas probablemente va a ser diferente porque es si yo te digo que es excluyente

18:21

18 minutos y 21 segundos

elegir uno o elegir o




---
https://www.youtube.com/watch?v=omgVCc7Kev0&list=PLYZrqm_pzRul0t_2QKU2kdHDwGkKblutk&index=26

0:03

3 segundos

el conjunto de aristas probablemente va a ser diferente porque yo te digo que es excluyente elegir uno o elegir otro

0:11

11 segundos

entonces por ahí sí si uno de ustedes elige a y el otro

0:20

20 segundos

elige p bueno van a tener con formaciones de árboles diferentes pero el valor es el mismo entonces en ese

0:28

28 segundos

caso vamos a tener dos árboles de expansión mínima que van a dar el mismo valor

0:38

38 segundos

bueno eso sí puede ocurrir e yo tenía un ejemplo pero no me acuerdo

0:47

47 segundos

si es un ejercicio de la guía ya mientras ustedes trabajen voy a ver si lo encuentro porque me acuerdo que lo

0:56

56 segundos

sabía dar en el presencial solíamos trabajar con eso bueno porque la presencialidad también

1:05

1 minuto y 5 segundos

teníamos el plus que por ahí los hacía pasar el pizarrón a resolver algo y entonces ahí mostrábamos los dos árboles diferentes así que voy a ver si es uno

1:14

1 minuto y 14 segundos

que esté en la guía o si no se los voy a pasar también para que lo haga bien

1:20

1 minuto y 20 segundos

entonces entonces tenemos claro cómo es el

1:28

1 minuto y 28 segundos

algoritmo vamos a trabajar con el problema 19 si primero vamos a hacer un ejercicio que

1:36

1 minuto y 36 segundos

les voy a pedir que ustedes colaboren que lo hagamos entre todos porque la idea es refrescar el tema es profundizar

1:43

1 minuto y 43 segundos

el tema y después nos vamos a dividir en grupo para que ustedes trabajen con otro problema

1:51

1 minuto y 51 segundos

y después hacemos una puesta en común bueno el problema 19 de la guía dice considerando el siguiente grafo y los

2:00

2 minutos

valores asociados a sus arcos en contra del árbol en el punto b dice en contra del árbol de expansión mínima en cada

2:08

2 minutos y 8 segundos

grado porque el problema 19 tiene dos grafos tiene este que yo les estoy

2:14

2 minutos y 14 segundos

mostrando y tiene otro más pequeño con menos aristas entonces bueno

2:22

2 minutos y 22 segundos

nosotros vamos a empezar trabajando con este grafo y vamos a calcular primero que todo el

2:30

2 minutos y 30 segundos

árbol de expansión le propongo que primero hagamos un árbol de expansión y luego hagamos

2:40

2 minutos y 40 segundos

un árbol de expansión mínima sí entonces a ver díganme ya lo han resuelto este

2:47

2 minutos y 47 segundos

ejercicio bien

2:57

2 minutos y 57 segundos

esto bien a ver algunos traten de ir cambiando el

3:06

3 minutos y 6 segundos

que participa así no es uno solo el que el que lo hace yo no lo veo porque estoy mirando esta pantalla así que traten de

3:14

3 minutos y 14 segundos

ir cambiando hacéis muchas cosas distintas díganme en qué vértice quieren que comencemos que no sea el 1 empecemos por

3:24

3 minutos y 24 segundos

otro diferente el cuadro del zinc

3:31

3 minutos y 31 segundos

el 4 dijeron primero bueno vamos a conversar con él 4

3:42

3 minutos y 42 segundos

con el 4 primero vamos a hacer un árbol de expansión entonces

3:48

3 minutos y 48 segundos

un árbol de expansión simple no un árbol de expansión mínimo si entonces si nosotros solo quisiéramos hacer un árbol

3:56

3 minutos y 56 segundos

de expansión podemos tomar cualquier arista sí que salga de este nodo origen

4:06

4 minutos y 6 segundos

así y por ejemplo yo voy a empezar diciendo que el primer nodo que voy a

4:12

4 minutos y 12 segundos

conectar es el nodo 3 y entonces acá tengo el primer la primera arista y

4:19

4 minutos y 19 segundos

tenemos el nodo 3 y el nodo 4 conectados y los restantes nodos no conectan van a ver ustedes que se puede ir haciendo una

4:28

4 minutos y 28 segundos

tabla donde ponemos los nodos conectados en una columna y los que están no conectados en la otra la columna de

4:37

4 minutos y 37 segundos

nodos conectados va aumentando hasta que estén todos los nodos y la de nodos no conectados va disminuyendo hasta que no

4:45

4 minutos y 45 segundos

quede ninguno esto es lo que nos permite es ver cómo se hizo el proceso como fuimos conectando a partir de que nos fuimos

4:54

4 minutos y 54 segundos

con ésta bueno ahora estamos tenemos dos nodos conectados cual podríamos conectar a

5:01

5 minutos y 1 segundo

todos estos al con cáritas que podríamos conectar al conjunto de los no conectados

5:09

5 minutos y 9 segundos

yo creo que el profe que podemos hacer un anillo para no equivocarnos es conectar el 52 porque se puede ser uno de la red

5:18

5 minutos y 18 segundos

a ver el 8 el liberal el 2 seguiríamos para no equivocarnos

5:26

5 minutos y 26 segundos

vamos haciendo así un anillo entre todos los de afuera y hasta conectar el equipo que no tiene bueno pero tenemos nosotros

5:35

5 minutos y 35 segundos

vamos de a uno si ahora tenemos los conectados y los no conectados entonces fue lo que propones es que ahora

5:42

5 minutos y 42 segundos

conectemos por ejemplo el 2 con el 1 así voy así con el anillo

5:51

5 minutos y 51 segundos

bueno ahora conecto el 1 con el 6

6:00

6 minutos

sans el 5 y el 5 el 7

6:05

6 minutos y 5 segundos

acá del 6 al 5 tengo tengo aristas siempre obviamente tenemos

6:14

6 minutos y 14 segundos

que ver que en la red original esté esa arista

6:20

6 minutos y 20 segundos

luego del 7 al 8 luego del 8 al 9

6:30

6 minutos y 30 segundos

profe sí en

6:40

6 minutos y 40 segundos

expansión claro porque vas a tener un ciclo acá

6:48

6 minutos y 48 segundos

y acá pongo esta arista fíjate que acá tenemos un ciclo por si

6:56

6 minutos y 56 segundos

entonces no puede haber si nosotros tenemos 3 5 7 9 12 si decía que la red

7:05

7 minutos y 5 segundos

tiene 12 tiene menos una aristas o sea que tenemos que tener para que sea un

7:12

7 minutos y 12 segundos

árbol de expansión 3 578 aristas y 92 si

7:19

7 minutos y 19 segundos

está bien y qué pasa si yo

7:25

7 minutos y 25 segundos

sigo entusiasmada con cerrar el anillo con esto estos dos giucich ahí hay un

7:34

7 minutos y 34 segundos

ciclo hasta la misma cantidad de aristas o sea que eso no lo puedo hacer bueno y

7:42

7 minutos y 42 segundos

díganme cuál sería el valor de este árbol de expansión

7:58

7 minutos y 58 segundos

cómo hacemos para determinar el valor del árbol de expansión 47

8:04

8 minutos y 4 segundos

es como los valores de cada arco a

8:12

8 minutos y 12 segundos

1551 y estamos en problemas

8:19

8 minutos y 19 segundos

hopkins 7 1 unos 10

8:27

8 minutos y 27 segundos

51 y quien tiene a alguien había dicho recién otro valor

8:36

8 minutos y 36 segundos

bueno 51 si están de acuerdo porque vamos suman 28 y 7 15 19 27

8:46

8 minutos y 46 segundos

34 41 43 ahora son millones 53

8:53

8 minutos y 53 segundos

viviendo 15 19 27 34 40 43 53 bien

9:04

9 minutos y 4 segundos

98 este 9 ha

9:12

9 minutos y 12 segundos

quedado ha quedado mal nos falta en alguna arista valor están

9:19

9 minutos y 19 segundos

todos vamos parece se habrá quedado cuando lo copien

9:27

9 minutos y 27 segundos

cuando ve el grafo media de quedaba algo mal hay el 9 hasta entonces este es un árbol de

9:36

9 minutos y 36 segundos

expansión tenemos todos los nodos de la red conectados si con este valor 53

9:45

9 minutos y 45 segundos

no hemos seguido el procedimiento de elegir en la menor arista si entonces no

9:52

9 minutos y 52 segundos

es un árbol de expansión mínima entonces ahora si volvemos al problema pero ahora para construir un árbol de expansión

10:01

10 minutos y 1 segundo

mínima vamos a empezar nuevamente en el vértice 4 para ver la diferencia

10:07

10 minutos y 7 segundos

en el nodo 4 pero ahora

10:13

10 minutos y 13 segundos

vamos a elegir para conectar la arista de menor valor

10:21

10 minutos y 21 segundos

entonces nos ponemos acá en el este también acá estamos en el nodo 4 que es el

10:31

10 minutos y 31 segundos

inicio si lo tenemos que conectar a algunos de los otros vértices con algunas de estas tres hay tres aristas

10:38

10 minutos y 38 segundos

que salen hacia el exterior del vértice 4 entonces tenemos que elegir la menor

10:45

10 minutos y 45 segundos

si tenemos 7 14 y 9 como habíamos visto antes 7 es la menor

10:54

10 minutos y 54 segundos

estaríamos empezando con la menor al bien ahora tenemos tres y cuatro nodos conectados los otros desconectados y

11:03

11 minutos y 3 segundos

tenemos que ver con qué aristas se pueden conectar para eso es como que

11:10

11 minutos y 10 segundos

tendríamos que ver supóngase que hacemos así

11:18

11 minutos y 18 segundos

circulamos el sol bueno estos son los dos conectados entonces tenemos que ver todas las

11:26

11 minutos y 26 segundos

aristas que salen de cualquiera de los dos de ellos tenemos esta de 9 14 42 y 8

11:35

11 minutos y 35 segundos

cuál sería la arista que vamos a seleccionar

11:45

11 minutos y 45 segundos

5 3 y 5 así que el valor sería 2 si entonces ahora

11:53

11 minutos y 53 segundos

lo que tendríamos sí esta completa

12:02

12 minutos y 2 segundos

tenemos en estos tres nodos con estados y los otros desconecta sí

12:10

12 minutos y 10 segundos

entonces bueno ahora tenemos que ver con cuál de las aristas que salen de estos tres nodos podemos conectar

12:20

12 minutos y 20 segundos

algunos de los otros venga acá tenemos este es el conjunto de los conectados y este de los no conecta tenemos una

12:27

12 minutos y 27 segundos

arista del valor 8 otra de valor 76

12:35

12 minutos y 35 segundos

14 y 9 cuál sería la arista con la que vamos a

12:40

12 minutos y 40 segundos

conectar el siguiente logro el de 4 el de 4 que conecta tres con ocho

12:51

12 minutos y 51 segundos

sí bueno ahora tenemos estos cuatro nodos conectados y tenemos que ver acá

12:59

12 minutos y 59 segundos

tenemos que empezar a tener cuidado de no tratar de no considerar alguna arista por ejemplo que esté uniendo dos nodos

13:07

13 minutos y 7 segundos

conectados si por ejemplo está de 14 y tiene 4 con 8 no es una de las aristas que vamos a considerar las que podemos

13:16

13 minutos y 16 segundos

considerar es ésta que de valor 9 está en el valor 10 está de valor 3

13:24

13 minutos y 24 segundos

7 y esta de 8 si esas son las aristas que podemos considerar cuál vamos a elegir

13:33

13 minutos y 33 segundos

para conectar al nodo 7 en el cielo

13:40

13 minutos y 40 segundos

me traiciona el subconsciente el 3 está bien ahora seguimos cuál es la

13:49

13 minutos y 49 segundos

próxima 7 con el 6 el 7 con el ser muy bien que van de valor

14:00

14 minutos

bien cual sí fíjense que ahora tenemos estas que

14:06

14 minutos y 6 segundos

están acá 8 y 11 8 estas 3 y tenemos

14:12

14 minutos y 12 segundos

estas 2 9 y 10 si vamos a elegir de 3 261 bien cual

14:22

14 minutos y 22 segundos

quieren elegir soy con una de 3 a 2 a 1

14:30

14 minutos y 30 segundos

6 a 1 ahora me quedan 4

14:36

14 minutos y 36 segundos

y 8 para conectar al nodo 2 y 9 y 10 con esto

14:46

14 minutos y 46 segundos

bueno ven que aquí por ejemplo bueno vamos a terminar este nos faltaría una más

14:53

14 minutos y 53 segundos

que sería conectar este nodo entre 9 y 10 conectamos con él

15:02

15 minutos y 2 segundos

si era esta decisión no me acordaba el difunto era el que tenía dos bueno

15:10

15 minutos y 10 segundos

cuál es el valor desde árbol de expansión qué es mínimo

15:24

15 minutos y 24 segundos

también media 38 8 pero a mí también

15:31

15 minutos y 31 segundos

38 y haber 8 y 4 12

15:36

15 minutos y 36 segundos

13 16 20 22 29

15:45

15 minutos y 45 segundos

y 9 sí

15:53

15 minutos y 53 segundos

de ese valor sí bueno

15:59

15 minutos y 59 segundos

veamos ahora por ejemplo si nosotros acá donde teníamos el empate

16:07

16 minutos y 7 segundos

si en lugar de elegir esta arista hubiéramos elegido ésta

16:15

16 minutos y 15 segundos

si se acuerdan que acá teníamos un empate entre estas 2 esta la vamos a dejar porque total

16:24

16 minutos y 24 segundos

sabemos qué va el tema se había presentado acá donde teníamos dos conos bueno si yo acá el hijo está

16:34

16 minutos y 34 segundos

8 la siguiente va a ser 4 o sea esta arista va a estar sido así

16:43

16 minutos y 43 segundos

cuál es el valor de este árbol los 19 21 25

16:51

16 minutos y 51 segundos

34 37 38 si el valor es el mismo y es el mínimo valor pero fíjense que el dibujo

17:00

17 minutos

es diferente si profesor bueno perfecto entonces

17:11

17 minutos y 11 segundos

podemos tener árboles de expansión mínima diferentes lo importante es que sea el

17:19

17 minutos y 19 segundos

menor valor bueno ahora lo que vamos a hacer es dividirnos

17:28

17 minutos y 28 segundos

en grupos yo voy a armar los grupos que se van a ir a los grupos que quieran con los que estén

17:37

17 minutos y 37 segundos

acostumbrados a trabajar y vamos a resolver el problema 18

17:44

17 minutos y 44 segundos

en el problema 18 les dice considerando el siguiente grafos los valores asociados en sus arcos

17:52

17 minutos y 52 segundos

encuentra el árbol de expansión mínima les pide en el punto a entonces lo que les voy a pedirte es que escriban en un

18:01

18 minutos y 1 segundo

word en lo que sea en el grupo en el recurso que ustedes les guste más usar que escriban los nodos que escriben el

18:11

18 minutos y 11 segundos

árbol y después me va a compartir plantas de algún grupo para mostrarme cuál es el árbol que

18:18

18 minutos y 18 segundos

quedó configurado está claro si profe bueno yo les voy a decir a ver

18:27

18 minutos y 27 segundos

el grupo que estaba en tal sala muestre cómo quedó el árbol de expansión y ahí

18:33

18 minutos y 33 segundos

vemos si están de acuerdo o no

18:45

18 minutos y 45 segundos

bueno no sé por qué ahora

19:13

19 minutos y 13 segundos

igual deja elegir profundos le dejé elegir yo les finalice todos los bienes porque me daba en que estaban

19:22

19 minutos y 22 segundos

separados palencia y esperen que lo estoy haciendo nuevo

19:30

19 minutos y 30 segundos

pero no sé por qué sección de grupos en curso no sé por qué estaba configurado

19:39

19 minutos y 39 segundos

diferente y no me dejó bueno se hace en un segundo que ya se está terminando

19:47

19 minutos y 47 segundos

podría repuso finalizar pero les da un tiempito para que vuelvan

19:54

19 minutos y 54 segundos

así lo puedo volver a configurar

20:43

20 minutos y 43 segundos

bueno cómo les fue

20:49

20 minutos y 49 segundos

bien profe bueno algún voluntario que quiera combatir pantalla y mostrarme era

20:58

20 minutos y 58 segundos

el problema 18 no sé por qué quedó de como he configurado el chat y no les

21:06

21 minutos y 6 segundos

podía mandar por el chat a decir pero bueno algunos me preguntan bien algún voluntario que comparta

21:13

21 minutos y 13 segundos

pantalla

21:26

21 minutos y 26 segundos

a se ve sí no

21:40

21 minutos y 40 segundos

bueno llegamos a un árbol mínimo de valor 26 y aquí esta noche aquí la

21:48

21 minutos y 48 segundos

explicó desde el punto a digamos empezaron en el vértice

21:57

21 minutos y 57 segundos

9 bueno de este lado teníamos para ir a él

22:04

22 minutos y 4 segundos

bien encontraron muchos empates o se fue definiendo bien fue definido

22:14

22 minutos y 14 segundos

sólo si teníamos valores mínimos siempre a calcular con 2 primero habíamos encontrado uno que

22:22

22 minutos y 22 segundos

tenía valor 27 ahora tendremos cabeza pero está habíamos hecho ve con se creó varias

22:31

22 minutos y 31 segundos

cinco y se con él y nos dimos cuenta que mira mejor que con él me ha bajado el 27

22:40

22 minutos y 40 segundos

26 6 por ahí cuando vieron en este por ejemplo están como más cruzados los

22:46

22 minutos y 46 segundos

vértices entonces por ahí al uno se confunde de las aristas que están

22:52

22 minutos y 52 segundos

disponibles y bueno puede pasar que estas cosas que tome una que no es la mínima entonces bueno siempre

23:00

23 minutos

revisarlo y el punto b

23:09

23 minutos y 9 segundos

es el mismo árbol pero el vélez pedía no el vélez pedía el camino de valor mínimo si

23:19

23 minutos y 19 segundos

sigue la ruta más corta bueno eso lo vamos a ver después la próxima clase vamos a trabajar con algunos ejercicios

23:27

23 minutos y 27 segundos

con es hoy me quería ser entrar más que todo en árbol de expansión para que me digan si tenían dudas o si iba surgiendo

23:36

23 minutos y 36 segundos

algo que se les complicó de árbol de expansión por eso dice que me mostrará

23:44

23 minutos y 44 segundos

ahora lo vamos a ver la semana próxima bueno vamos a trabajar con árbol de expansión y con un algoritmo de disco la

23:53

23 minutos y 53 segundos

ruta más corta e de juego partido ustedes como

24:02

24 minutos y 2 segundos

recordemos que la información que nos da el árbol de expansión es el menor valor

24:11

24 minutos y 11 segundos

que puede ser en tiempo en distancia de acuerdo al valor que está asignado a cada arista cada arco si los arcos no

24:20

24 minutos y 20 segundos

siempre indican distancias y también podrían indicar tiempo para llegar de un punto al otro o costos y entonces lo que

24:29

24 minutos y 29 segundos

nos estaría dando el menor valor ya sea en dinero en tiempo en distancia para conectar todos

24:39

24 minutos y 39 segundos

los nodos de la red si es importante que graben ese concepto que grabé en el objetivo

24:46

24 minutos y 46 segundos

y el procedimiento del algoritmo porque yo no quiero trabajar los dos métodos al mismo tiempo o sea en el

24:54

24 minutos y 54 segundos

teórico los ámbitos a los dos han trabajado con los dos porque tenían más tiempo yo hoy me quiero centrar en el árbol de expansión y que la semana

25:02

25 minutos y 2 segundos

próxima nos concentremos en el algoritmo de dijkstra porque los años que hace que yo vengo dando clase veo que los

25:10

25 minutos y 10 segundos

entienden perfecto a los dos métodos les queda claro y les parecen muy simples pero cuando llegamos a las evaluaciones

25:19

25 minutos y 19 segundos

parciales o finales uno les pide por ejemplo indique los pasos del algoritmo

25:26

25 minutos y 26 segundos

del árbol de expansión y nombran los pasos del árbol de la ruta más corta si

25:34

25 minutos y 34 segundos

entonces mezclan los temas por eso yo quiero fijar bien uno y que la semana siguiente fijemos bien el de

25:43

25 minutos y 43 segundos

la ruta más corta que trabajemos solo pones trabajando personalizado sobre un método uno lo grababa bastante mejor

25:52

25 minutos y 52 segundos

bueno hay otros ejercicios que pueden hacer de árbol por ejemplo está el

25:59

25 minutos y 59 segundos

problema 16 que tienen también una red y en la cual

26:06

26 minutos y 6 segundos

tienen que determinar el árbol de expansión y les dejo de tarea es el problema 16

26:15

26 minutos y 15 segundos

haganlo y la semana que viene si llegaran a tener alguna duda lo podemos ver también

26:24

26 minutos y 24 segundos

bueno la semana que viene ya también vamos a tener las notas vamos a poder ver si alguno tiene dudas

26:32

26 minutos y 32 segundos

de axel de recuperación bien algunos de los que se sumaron

26:41

26 minutos y 41 segundos

después que volvieron como más tarde de las salas alguno tiene dudas con respecto al árbol de expansión o la

26:49

26 minutos y 49 segundos

resolución que hicieron no no nosotros ahí hemos vuelto tarde

26:57

26 minutos y 57 segundos

porque estábamos intentando hacer el punto de vista bueno si quieren adelante lo hice como

27:06

27 minutos y 6 segundos

yo sé que ya lo han visto el tema si quieren vayan haciéndolo como tareas la semana próxima vamos a trabajar más en

27:15

27 minutos y 15 segundos

detalle sobre ese método si pueden entrar les doy un consejo por ahí ustedes les parece muy intenso mi

27:23

27 minutos y 23 segundos

existencia hágase un resumen pongan el objetivo y los pasos separados en un archivo en una hoja

27:32

27 minutos y 32 segundos

de cada uno de los métodos y la experiencia a mí me indica que después

27:39

27 minutos y 39 segundos

se les mezclan los dos métodos cuando tienen la evaluación confunden si no se dan cuenta si hay que aplicar uno

27:48

27 minutos y 48 segundos

hay que aplicar el otro confunden los pasos si entonces por eso estamos hincapié en este a darse un resumen

27:55

27 minutos y 55 segundos

agregar un archivo con los pasos si algo que les ayude a identificarlos bien bueno chicos

28:04

28 minutos y 4 segundos

nos volvemos a encontrar el próximo miércoles para

28:10

28 minutos y 10 segundos

para continuar con esta unidad 6 perfecto muchas gracias perfecto profe

28:18

28 minutos y 18 segundos

nos vemos y nos vemos la semana próxima nos vemos pronto buenos hermanos dale

28:26

28 minutos y 26 segundos

gracias igualmente ustedes