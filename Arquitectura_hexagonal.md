---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit:
type: TEO
zk_type: permanent
status: in-progress
date: 2026-08-15
source:
tags:
---
---

### 2. ¿Por qué se basa en la Arquitectura Hexagonal?

La Arquitectura Hexagonal (también conocida como Puertos y Adaptadores, creada por Alistair Cockburn) busca que el núcleo de tu aplicación (tu servicio y reglas de negocio) esté completamente aislado del
mundo exterior (bases de datos, frameworks, APIs de terceros, etc.).

Se llama "hexagonal" no por tener 6 lados literales, sino para representar que tiene múltiples puntos de conexión divididos fundamentalmente en dos lados:

![[Pasted image 20260815143221.png]]
──────
### 3. Los dos lados en detalle

#### A. Lado Conductor / Primario ("Quien le pide algo al servicio")

• Quiénes son: Los clientes externos (un usuario desde el navegador, una app móvil, un comando por consola o un mensaje en una cola).
• Cómo interactúan: Llegan al servicio a través de un Adaptador de Entrada (por ejemplo, un controlador HTTP) que transforma la petición externa en una llamada comprensible para el servicio.

#### B. Lado Conducido / Secundario ("De quién se vale el servicio para resolver la tarea")

• Quiénes son: Los recursos externos que el servicio necesita para completar su trabajo (la base de datos para guardar información, MercadoPago/Stripe para cobrar, Twilio/SendGrid para mandar un SMS o
email).
• Cómo interactúan: El servicio define qué necesita mediante un Puerto (una interfaz), y la infraestructura le provee un Adaptador de Salida (el código específico para SQL, Mongo, Stripe, etc.).
──────
### 4. Ejemplo concreto: ServicioDePagos

Imagina que un usuario realiza una compra:

1. Lado del cliente (Entrada):
  • El usuario pulsa "Pagar" en la app móvil.
  • El controlador HTTP recibe el JSON y llama al ServicioDePagos.procesar(monto, tarjeta).
2. El Servicio (Centro):
  • Valida si el monto es positivo.
  • Comprueba si la cuenta está activa.
  • Aplica descuentos o impuestos (reglas de negocio).
3. Lado de los proveedores (Salida):
  • El servicio se vale de una pasarela de cobro externa (ej. Stripe) para debitar el dinero.
  • Se vale de la base de datos (ej. PostgreSQL) para registrar el recibo.
  • Se vale de un servicio de email para enviar la factura.

──────
### ¿Cuáles son las ventajas de esta arquitectura?

• Independencia tecnológica: Si mañana cambias de base de datos (de PostgreSQL a MongoDB) o de pasarela de pagos (de Stripe a PayPal), la lógica del Servicio no cambia en absoluto; solo reemplazas el
adaptador de salida.
• Facilidad para hacer pruebas (Tests): Puedes probar tu servicio simulando (mockeando) la base de datos o las APIs externas sin tener que conectarte a internet ni depender de un servidor real.
• Mantenibilidad: Cada parte del sistema tiene una responsabilidad única y bien delimitada.



---
