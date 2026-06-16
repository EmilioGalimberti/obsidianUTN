# Guía de Resolución Definitiva: [[Sistemas Secuenciales Combinados]] con Bloqueos y Restricciones de Capacidad

He procesado la última resolución del profesor correspondiente al modelo del "Taller de Reparación de Vehículos". Este es un ejercicio de nivel superior porque integra **[[Sistemas Combinados]]** (Ecuaciones Diferenciales), **[[Zonas de Buffer Restringidas]]** y el complejo método de **[[Box-Muller]]**.

A continuación, la estructura metodológica, fórmulas y las peores trampas en las que caen los alumnos durante los exámenes.

---

## 1. Planteo del Modelo y Diseño Estructural

El sistema tiene tres estaciones secuenciales: Inspección, Reparación y Armado. La dificultad radica en cómo los objetos se mueven (o se atascan) entre ellas.

|Componente|Elemento en el Modelo|Lógica Crítica de Modelado|
|:--|:--|:--|
|**[[Eventos]]**|Llegada, Fin Inspección, Fin Reparación, Fin Armado Sub $i$|El armado tiene 4 espacios (2 equipos que atienden 2 autos cada uno). Se modelan con índices simples (1, 2, 3, 4) en lugar de subíndices compuestos para ahorrar tiempo visual.|
|**[[Objetos Permanentes]]**|Inspección, Reparación, Armado|**Crucial:** Deben tener tres estados obligatorios: `[[Libre]]`, `[[Ocupado]]` y `[[Bloqueado]]`.|
|**[[Colas y Buffers]]**|Cola Inicial, Buffer Intermedio 1, Buffer Intermedio 2|La cola de Inspección es infinita. El buffer antes de Reparación es de **máximo 2 lugares**. El buffer antes de Armado es de **0 lugares**.|

### Diagrama Lógico de Flujo y Bloqueos

```
graph TD
    A[Llegada de Vehiculo] --> B(Cola Infinita)
    B --> C[Inspeccion]
    C --> D{¿Buffer Reparacion < 2?}
    D -- SI --> E[Pasar a Buffer Reparacion]
    D -- NO --> F[Servidor Inspeccion pasa a BLOQUEADO]
    E --> G[Reparacion]
    G --> H{¿Hay lugar en Armado?}
    H -- SI --> I[Pasar a Armado Sub i]
    H -- NO --> J[Servidor Reparacion pasa a BLOQUEADO]
    I --> K[Resolucion por Euler]
    K --> L[Fin Armado / Destruccion]
```

_(Conceptos relacionados: [[Restricción de Capacidad]], [[Cuello de Botella]], [[Vector de Estado]])_

---

## 2. Fórmulas Matemáticas Obligatorias

El profesor aplicó generadores específicos para cada etapa, incluyendo un método que suele causar reprobados masivos.

> [!note] Fórmula: Transformación de Tasas a Tiempos (Llegadas) El enunciado dice "tasa exponencial de 8 vehículos por hora". **Cálculo:** $\lambda = 8/60 \rightarrow Media = 7.5$ minutos por vehículo. $$X = -7.5 \cdot \ln(1 - RND)$$

> [!note] Fórmula: [[Método de Box-Muller]] (Tiempos Normales de Reparación) El tiempo de reparación es una [[Distribución Normal]] de media 8 y desviación 5. Este método consume **dos** números aleatorios ($RND_1$ y $RND_2$) para generar **dos** valores normales ($N_1$ y $N_2$).
> 
> **Primer Auto Reparado:** $$N_1 = \mu + \sigma \cdot \left( \sqrt{-2 \cdot \ln(RND_1)} \cdot \cos(2\pi \cdot RND_2) \right)$$ **Segundo Auto Reparado:** $$N_2 = \mu + \sigma \cdot \left( \sqrt{-2 \cdot \ln(RND_1)} \cdot \sin(2\pi \cdot RND_2) \right)$$

---

## 3. 🚨 Trampas Mortales y Errores Frecuentes

El profesor se detuvo explícitamente a remarcar errores graves ("los he visto mucho a lo largo de mi experiencia docente") que anulan el ejercicio:

> [!danger] TRAMPA MORTAL 1: Quemar Randoms en Box-Muller **El peor error:** El alumno calcula el primer tiempo de reparación extrayendo dos Randoms y usando la fórmula del "Coseno". Cuando llega el **siguiente** auto a reparar, el alumno extrae **dos Randoms nuevos**. **Lo correcto:** ¡Falso! Para el segundo auto debes usar **los mismos dos Randoms originales**, pero aplicándolos en la segunda fórmula (la del "Seno"). Solo debes sacar Randoms nuevos cada dos reparaciones.

> [!danger] TRAMPA MORTAL 2: Ignorar el estado `[[Bloqueado]]` Si el auto termina de inspeccionarse, pero los 2 lugares del buffer siguiente están llenos, **el servidor de inspección no puede quedar Libre ni Ocupado**. Pasa al estado `[[Bloqueado]]`. El profesor aclaró que debes acumular el tiempo que el servidor pasa en este estado, porque las máquinas o empleados inmovilizados cuestan dinero.

> [!danger] TRAMPA ESTADÍSTICA: Promediar las [[Condiciones Iniciales]] El sistema arranca con 4 autos ya adentro (algunos a medio armar o medio reparar). **El error:** Cuando esos autos salen del sistema, sumarlos al "Tiempo Promedio de Permanencia". **Lo correcto:** Es imposible saber su tiempo de permanencia porque **no tienes su hora de llegada**. Cuando estos autos iniciales se van, simplemente bórralos del sistema y **no los cuentes para las estadísticas de tiempos**.

---

## 4. Tips y Atajos de Metodología de Parcial

El profesor brindó estrategias para ganar valiosos minutos en el Excel:

> [!tip] Tip Metodológico: La Reutilización de Tablas de [[Euler]] En este ejercicio, el tiempo de armado se calcula con Ecuaciones Diferenciales que varían según si el equipo atiende 1 auto o 2 autos. **El atajo:** No hagas una tabla de Euler cada vez que llega un auto. Haz **una sola tabla estática** para la ecuación de 1 auto (ej. da 4.77 mins) y **otra tabla** para la ecuación de 2 autos (ej. da 9.09 mins). Luego, simplemente consulta esas dos tablas y copia el valor directamente en el vector sin volver a integrar.

> [!tip] Tip de Diseño: Fracciones en Condiciones Iniciales Si el enunciado dice "un auto termina su reparación en 50 segundos" pero todo tu Excel está en Minutos, no te compliques con reglas de tres constantes. Anota el valor decimal: $50 / 60 = 0.83$ minutos.

> [!question] Dudas de Lógica en Clase: Asignación de Servidores Paralelos **Alumno:** Si salen autos de Reparación y hay varios boxes de Armado libres, ¿a cuál lo mando?. **Respuesta Oficial:** Si el enunciado no da una regla explícita (como "mandar al que tenga menos cola"), **lo mandas a cualquiera**. El profesor confirmó: "arbitrariamente lo envío al box 4 porque se me ocurre... elegí cualquiera de los 4 libres". Siempre anota a qué box lo mandaste para no perder el rastro cuando ocurra el Fin de Atención.