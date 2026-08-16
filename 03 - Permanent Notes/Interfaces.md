---
aliases:
subject: DSI
year: "3"
exam: PARCIAL2
unit:
type: TEO
zk_type: permanent
status: done
date: 2026-08-16
source:
tags:
---
---
Las interfaces se utilizan para especificar las operaciones que proporcionan las clases y los subsistemas de diseño. Una clase del diseño que proporcione una interfaz debe proporcionar también métodos que realicen las operaciones de la interfaz.

Las interfaces constituyen una forma de separar la especificación de la funcionalidad en términos de operaciones de sus implementaciones en términos de métodos. 
Esto hace independiente a cualquier cliente que dependa de la implementación de la interfaz. Podemos sustituir una implementación concreta de una interfaz, como puede ser una clase o un subsistema del diseño, por otra implementación sin tener que cambiar los clientes.


# 1. Separación entre el "Qué" y el "Cómo" (Especificación vs. Implementación)

• La interfaz (Especificación): Solo contiene las firmas de los métodos (nombre, parámetros y tipo de retorno). Define qué se puede hacer, pero no cómo se hace.
• La clase (Implementación): Provee el cuerpo del método con la lógica concreta.

### 2. Contrato de comportamiento

Cuando una clase dice que implementa una interfaz, asume el compromiso obligatorio de proveer código real para cada una de las firmas declaradas en ella.

### 3. Desacoplamiento (Independencia del Cliente)

El "cliente" (la función o clase que usa el servicio) solo necesita conocer la interfaz. No necesita saber qué clase concreta está por detrás ni cómo está construida internamente.

### 4. Polimorfismo y Sustituibilidad

Permite cambiar la implementación en cualquier momento sin romper el código cliente.
──────
### Ejemplo rápido en código:

```java
// 1. Especificación (solo firmas)
interface Notificador {
  enviarMensaje(destinatario: string, mensaje: string): void;
}

// 2. Implementaciones concretas
class NotificadorEmail implements Notificador {
  enviarMensaje(destinatario: string, mensaje: string): void {
	console.log(`Enviando email a ${destinatario}: ${mensaje}`);
  }
}

class NotificadorSMS implements Notificador {
  enviarMensaje(destinatario: string, mensaje: string): void {
	console.log(`Enviando SMS al número ${destinatario}: ${mensaje}`);
  }
}

// 3. Cliente (independiente de la implementación concreta)
class SistemaDeAlertas {
  constructor(private notificador: Notificador) {}

  alertar(usuario: string, texto: string) {
	this.notificador.enviarMensaje(usuario, texto);
  }
}
```

En este ejemplo se cumple todo lo que menciona el texto:

• SistemaDeAlertas (el cliente) no depende de NotificadorEmail ni de NotificadorSMS.
• Puedes sustituir NotificadorEmail por NotificadorSMS (o un mock de pruebas) sin cambiar una sola línea de SistemaDeAlertas.


---

# ¿Por qué el texto dice "proporcionar" en vez de "implementar"?

En los libros de arquitectura y diseño (como en UML), las interfaces se ven como enchufes y tomas de corriente:

Término en diseño (UML / Arquitectura)            | Término en código (Java / C# / TypeScript)       | Ejemplo de nuestro código                        | Rol
---------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------
Proporcionar una interfaz (Provided Interface)    | Implementar (implements Notificador)             | NotificadorEmail, NotificadorSMS                 | Es el Proveedor (ofrece el servicio)
Requerir una interfaz (Required Interface)        | Depender / Usar (constructor(n: Notificador))    | SistemaDeAlertas                                 | Es el Cliente (consume el servicio)
──────
### Explicación con una metáfora cotidiana (El enchufe USB)

1. La interfaz: Es el estándar USB (las dimensiones, pines y reglas de voltaje). La interfaz por sí sola no hace nada, es solo la especificación.
2. La clase que proporciona la interfaz: Tu computadora portátil. Tiene el puerto USB hembra listo para recibir conexiones. La laptop proporciona la interfaz USB al exterior.
3. El cliente que usa la interfaz: Tu mouse o teclado. Solo necesita saber que hay un puerto USB donde conectarse, no le importa qué marca de laptop sea.
──────
### Traducción de la frase a lenguaje de código:

│ Texto original:
│ "Una clase del diseño que proporcione una interfaz debe proporcionar también métodos que realicen las operaciones de la interfaz."

│ Traducido a lo que hacemos al programar:
│ "Una clase que haga implements Notificador está obligada a escribir el código ({ ... }) de todos los métodos definidos en Notificador."

En resumen:

• Proporcionar la interfaz = Ser quien la implementa y ofrece esas operaciones al resto del sistema.