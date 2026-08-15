---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit:
type: TEO
zk_type: permanent
status: done
date: 2026-08-15
source:
tags:
---
---

### 1. ¿Qué es realmente un "Servicio"?

  En desarrollo de software, un Servicio es un módulo de código encargado de resolver una necesidad o caso de uso del negocio (por ejemplo: CrearPedido, AutenticarUsuario, ProcesarPago).

  #### ¿Por qué cambia respecto a la forma "tradicional"?

  • Forma tradicional (Monolítica / Código espagueti): La interfaz gráfica (o el controlador web) solía mezclarse directamente con las consultas a la base de datos y la lógica del negocio en un solo lugar.
  Si cambiaba la base de datos o la interfaz, se rompía todo.
  • Con Servicios (Modularización): El servicio se vuelve una pieza independiente que encapsula las reglas de negocio. No le importa si quien lo llama es una página web, una app móvil o un proceso
  automático; el servicio solo recibe datos, aplica reglas y devuelve un resultado.


¿En qué arquitectura fundamentalmente se basan los servicios?

El Servicio se basa en una [[Arquitectura_hexagonal]]



---

# es lo mismo /service que microservicios?

### 1. La carpeta services/ en tu MVC Passive View: ¿Es lo mismo?

Sí, exactamente. Esa carpeta representa la Capa de Servicios (Service Layer) de tu aplicación.

En el patrón MVC Passive View:

• View (Vista): Es "pasiva", solo muestra datos y no toma decisiones. Cuando el usuario hace clic, le avisa al Controlador.
• Controller / Presenter: Recibe el evento de la vista, pero no debería contener la lógica pesada del negocio ni saber cómo consultar la base de datos (para no convertirse en un controlador gigante o "fat
controller").
• services/: Es donde colocas las clases o módulos que resuelven los problemas reales:
  • Servicios de Negocio: AuthService (validar contraseñas, sesiones), CartService (calcular totales, descuentos).
  • Servicios Técnicos / Infraestructura: ApiService (hacer llamadas fetch/axios), StorageService (guardar en localStorage).


│ En resumen: En tu proyecto, un servicio es simplemente una clase o archivo de código que encapsula una funcionalidad específica para que tu controlador se mantenga limpio y ordenado.
──────
### 2. ¿Por qué se llaman igual? ¿Es lo mismo que un "Microservicio"?

No son lo mismo, aunque la idea de fondo es similar: ambos son piezas diseñadas para cumplir una función específica.

La diferencia principal está en dónde viven y cómo se ejecutan:

Característica                                            | Servicio (en tu carpeta /services)                                     | Microservicio
-----------------------------------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------
¿Qué es?                                                  | Un archivo / clase de código dentro de tu proyecto.                    | Un programa / servidor independiente completo.
¿Dónde corre?                                             | En el mismo proceso y memoria que el resto de tu app.                  | En su propio servidor, contenedor (Docker) o nube.
¿Cómo se comunica?                                        | Mediante llamadas directas a funciones o métodos: authService.login(). | A través de la red (HTTP, REST, gRPC, WebSockets, colas de mensajes).
Base de datos                                             | Comparte la base de datos de la app.                                   | Suele tener su propia base de datos aislada.
Escala                                                    | Nivel de diseño de código (dentro de un monolito o app).               | Nivel de arquitectura de infraestructura (sistema distribuido).
──────
### 3. Una analogía para no olvidarlo

• Servicio (carpeta de código): Es como un empleado del área de facturación dentro de la misma oficina. Si el recepcionista (Controlador) necesita una factura, se da vuelta y se la pide hablando
directamente con él.
• Microservicio: Es como contratar a una empresa externa de facturación en otro edificio. Para pedirle algo, el recepcionista tiene que hacer una llamada telefónica o enviar un email (petición de red por
HTTP).
──────
### Curiosidad: ¿Cómo se relacionan?

Un microservicio por dentro suele ser una aplicación pequeña que también está organizada con arquitectura hexagonal o MVC, y por lo tanto, ¡un microservicio también suele tener su propia carpeta services/
adentro!