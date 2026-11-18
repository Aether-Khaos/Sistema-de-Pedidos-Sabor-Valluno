
# REGLAS GENERALES DE DESARROLLO — SABOR VALLUNO

## 1. AUTORIDAD Y ALCANCE DEL PROYECTO

Este documento establece las reglas obligatorias que deben respetarse durante todo el desarrollo del Sistema de Pedidos Sabor Valluno.

El desarrollo se realizará progresivamente, clase por clase y archivo por archivo. Cada fragmento de código debe integrarse con lo que ya existe, respetando la arquitectura y las funcionalidades implementadas anteriormente.

### 1.1. Fuentes de autoridad

Se deben respetar las siguientes fuentes en este orden:

1. **Diagrama UML del proyecto:** es la arquitectura de referencia. Define las clases, nombres, atributos, métodos, visibilidad, herencia, relaciones y responsabilidades.
2. **Documento original del proyecto:** establece los requisitos funcionales, las reglas de negocio, las restricciones y los comportamientos obligatorios.
3. **Variante F:** sustituye los valores correspondientes de las reglas base 3, 4 y 5.
4. **Este README:** establece las restricciones de implementación, calidad, compatibilidad y comportamiento de la IA.

No se debe modificar una fuente para acomodarla a otra.

### 1.2. Regla de fidelidad

- No inventar clases, atributos, métodos, relaciones ni funcionalidades.
- No cambiar nombres definidos en el diagrama UML.
- No modificar la arquitectura para proponer una alternativa que la IA considere mejor.
- No implementar funcionalidades que no hayan sido solicitadas o que no estén contempladas en el proyecto.
- No asumir reglas de negocio que no estén especificadas.
- No sustituir la variante F por las reglas generales del documento.
- No eliminar requisitos existentes por simplificar el código.
- No generar código ficticio, clases vacías, métodos sin implementación o funcionalidades simuladas.

Si existe una contradicción, ambigüedad o información insuficiente, se debe señalar exactamente el problema y solicitar aclaración antes de tomar una decisión que afecte la arquitectura o las reglas de negocio.

---

## 2. RESTRICCIONES TECNOLÓGICAS

- Lenguaje: Python 3.
- Aplicación: consola.
- Paradigma obligatorio: Programación Orientada a Objetos.
- No utilizar frameworks.
- No utilizar librerías externas.
- No instalar dependencias.
- No utilizar bibliotecas de terceros.
- No introducir herramientas o tecnologías adicionales.
- No utilizar persistencia JSON, bases de datos ni otros mecanismos de almacenamiento que no hayan sido solicitados expresamente.

### 2.1. Imports permitidos

La única importación permitida es la necesaria para implementar las clases abstractas:
solo se permite la importacion de la carpta y archivo ruta para complementar al codigo
```python
from abc import ABC, abstractmethod
```
se rige y prohibe explicitamente el uso de librerias de python para implementar funcionalidad, todo debe ser codigo construido desde cero
No importar otros módulos, incluidos módulos de la biblioteca estándar.

No utilizar `dataclasses`, `typing`, `Protocol`, `Enum` ni mecanismos que requieran importaciones adicionales.

Se permiten las funciones y construcciones nativas de Python.

---

## 3. PROGRAMACIÓN ORIENTADA A OBJETOS OBLIGATORIA

Todo el código debe desarrollarse utilizando los cuatro pilares de la POO.

### 3.1. Abstracción

Las siguientes clases deben ser abstractas:

- `Producto`
- `Pedido`
- `MetodoPago`

Deben heredar de `ABC` y declarar sus contratos mediante `@abstractmethod`.

Reglas:

- No se deben instanciar directamente las clases abstractas.
- Las subclases deben implementar los métodos abstractos correspondientes.
- No se deben crear abstracciones adicionales que no estén contempladas en el diagrama.
- No se deben convertir las clases abstractas en clases concretas para evitar implementar sus métodos.

### 3.2. Encapsulación

Todos los atributos del modelo deben ser protegidos o privados.

Reglas:

- Utilizar atributos protegidos o privados.
- Acceder a los atributos mediante propiedades `@property`.
- Utilizar setters cuando corresponda.
- Validar los valores antes de modificar los atributos.
- Evitar modificaciones directas desde otras clases.
- No exponer listas internas que permitan modificar el estado de un objeto sin validación.
- La lista de productos de un pedido solo puede modificarse mediante los métodos correspondientes.
- Las validaciones deben encontrarse en la clase responsable de proteger el dato.

No utilizar atributos públicos para evitar implementar encapsulación.

### 3.3. Herencia

Respetar estrictamente las jerarquías y relaciones del diagrama UML.

Reglas:

- Utilizar herencia únicamente donde esté definida en el diagrama.
- Las subclases deben utilizar `super().__init__()` cuando corresponda.
- Los atributos comunes deben permanecer en la clase que corresponda según el UML.
- No duplicar atributos heredados.
- Las subclases deben incorporar únicamente sus atributos y comportamientos propios.
- Mantener las relaciones de herencia originales.
- El proyecto debe conservar al menos nueve subclases, conforme al requisito original.

No crear jerarquías paralelas ni cambiar la herencia para resolver un problema de implementación.

### 3.4. Polimorfismo

El comportamiento específico de cada clase debe resolverse mediante sus métodos correspondientes.

Se deben utilizar los métodos sobrescritos para:

- `calcular_precio()`
- `esta_disponible(dia)`
- `contar_platos()`
- `calcular_cargos()`
- `procesar_pago()`

Reglas obligatorias:

- No utilizar `isinstance()` para identificar tipos de productos o pedidos.
- No utilizar `type()` para identificar clases.
- No utilizar cadenas de `if/elif` para distinguir tipos de objetos.
- No implementar comportamientos específicos mediante comparaciones de nombres de clases.
- No crear condicionales que sustituyan métodos polimórficos.
- Las clases deben resolver su propio comportamiento mediante sus métodos.

El subtotal de un pedido debe calcularse recorriendo sus elementos y utilizando sus métodos, sin identificar manualmente el tipo de cada elemento.

Los combos deben calcular su precio recorriendo sus productos y llamando a `calcular_precio()`.

Los combos pueden contener otros combos. Los cálculos deben funcionar con cualquier nivel de anidamiento válido.

El conteo de platos debe considerar también los platos contenidos dentro de combos anidados.

El cálculo de envases debe considerar los platos que se encuentren dentro de combos y combos anidados.

---

## 4. ARQUITECTURA Y DIAGRAMA UML

El código debe corresponder con el diagrama UML proporcionado por el usuario.

### 4.1. Clases y responsabilidades

Se deben respetar las clases del diagrama, entre ellas:

- `Restaurante`
- `Cliente`
- `Producto`
- `Plato`
- `Combo`
- `ProductoCombo`
- `DetallePedido`
- `Pedido`
- `PedidoLocal`
- `PedidoDelivery`
- `PedidoParaLlevar`
- `MetodoPago`
- `PagoEfectivo`
- `PagoQr`
- `PagoTarjeta`
- Las clases concretas de productos y bebidas representadas en el diagrama.

### 4.2. Métodos y atributos

- Mantener los nombres originales del diagrama.
- Mantener las responsabilidades asignadas a cada clase.
- No trasladar métodos de una clase a otra sin autorización.
- No agregar atributos porque parezcan convenientes.
- No eliminar atributos porque parezcan redundantes.
- No cambiar la firma de los métodos existentes.
- No modificar las relaciones entre clases.
- No cambiar la visibilidad establecida.
- No introducir clases auxiliares que alteren la arquitectura.

Los métodos deben implementarse en la clase a la que pertenecen según el UML.

Si un método requiere colaboración de otra clase, debe utilizar sus métodos y responsabilidades existentes.

### 4.3. Regla de correspondencia UML-código

El código y el diagrama deben mantenerse sincronizados.

Si se solicita implementar una clase, se debe utilizar su estructura UML como referencia.

Si se solicita modificar una clase, no se deben modificar automáticamente las demás.

Si una modificación realmente exige actualizar otra clase o una relación, se debe explicar la dependencia y señalar qué cambios mínimos son necesarios.

No rediseñar el diagrama para justificar una implementación diferente.

---

## 5. REGLAS DE NEGOCIO — VARIANTE F

Todos los montos se expresan en bolivianos (Bs) y deben manejarse con dos decimales en los resultados monetarios.

### 5.1. Productos

El menú contempla:

- Platos: silpancho, pique macho, chicharrón y sopa de maní.
- Bebidas: refrescos naturales y gaseosas.
- Combos.

Los productos deben respetar las clases y relaciones definidas en el UML.

### 5.2. Bebidas

- Cada bebida tiene un precio por vaso.
- El precio de una jarra equivale a tres veces el precio del vaso.

### 5.3. Combos — Variante F

- Un combo debe contener al menos dos productos.
- Puede contener platos, bebidas y otros combos.
- No puede contenerse a sí mismo.
- Debe calcular su precio a partir de los precios de sus componentes.
- Se aplica un descuento del 5 % más Bs 5 fijos.
- No se deben utilizar precios escritos manualmente para simular el contenido de un combo.
- Los combos anidados deben calcularse correctamente.
- La disponibilidad de un combo depende de la disponibilidad de todos sus componentes.

No inventar condiciones adicionales para aplicar el descuento.

### 5.4. Disponibilidad — Variante F

- La sopa de maní solamente está disponible los lunes y jueves.
- La disponibilidad debe consultarse mediante `esta_disponible(dia)`.
- Un combo solamente está disponible cuando todos sus componentes están disponibles.
- No aplicar la regla base del chicharrón disponible únicamente los domingos, porque la variante F sustituye las reglas de disponibilidad correspondientes.

No inventar restricciones de días para otros productos.

### 5.5. Pedidos locales

- No tienen cargos adicionales.
- La mesa debe estar comprendida entre la 1 y la 15.
- Una mesa no puede tener dos pedidos abiertos simultáneamente.

### 5.6. Pedidos para llevar

- Se cobra Bs 2 por envase por cada plato.
- Los platos dentro de combos también generan cargos por envase.
- Los platos dentro de combos anidados también deben contabilizarse.
- Las bebidas no generan cargos por envase.
- El cálculo debe realizarse utilizando los métodos de las clases correspondientes.

### 5.7. Pedidos delivery

Zonas y costos de envío:

| Zona | Costo |
|---|---:|
| Cercado | Bs 8 |
| Quillacollo | Bs 15 |
| Sacaba | Bs 15 |
| Vinto | Bs 20 |

Reglas de la variante F:

- El pedido mínimo es Bs 30.
- El envío es gratuito cuando el subtotal alcanza Bs 100.
- El envío gratuito se aplica a todas las zonas.
- Si el subtotal no alcanza Bs 100, se cobra el costo correspondiente a la zona.
- No aplicar el umbral de envío gratuito de las reglas base.

### 5.8. Estados del pedido

Los estados válidos son:

`REGISTRADO → EN_PREPARACION → LISTO → ENTREGADO`

Reglas:

- Solo se puede cancelar un pedido desde `REGISTRADO`.
- Solo se pueden agregar productos mientras el pedido esté en `REGISTRADO`.
- Solo se pueden quitar productos mientras el pedido esté en `REGISTRADO`.
- No se permiten transiciones de estado inválidas.
- Una transición inválida debe generar una excepción.
- Los cambios de estado deben realizarse mediante los métodos correspondientes.

### 5.9. Métodos de pago

**Pago en efectivo**

- El monto recibido debe cubrir el total.
- Se debe calcular el cambio.
- El método debe implementar el comportamiento definido en el UML.

**Pago QR**

- Debe registrar un código de transacción de exactamente 10 dígitos.
- Debe validar el código antes de aceptar el pago.

**Pago con tarjeta**

- Se aplica una comisión del 3 % a cargo del cliente.
- La comisión debe calcularse mediante el método correspondiente.

**Restricción de delivery**

- Los pedidos delivery solo aceptan efectivo o QR.
- No se debe permitir el pago con tarjeta para delivery.

### 5.10. Validaciones generales

- El precio de un producto debe ser mayor que cero.
- La cantidad de un producto en un pedido debe estar entre 1 y 20.
- El teléfono del cliente debe tener exactamente 8 dígitos.
- El teléfono debe comenzar con 6 o 7.
- Los datos deben validarse antes de modificar el estado de los objetos.
- Las validaciones deben estar implementadas en las clases responsables.

### 5.11. Retraso en delivery

Se considera retrasado un pedido que se entrega después de transcurridos más de 60 minutos desde su registro.

La compensación consiste en devolver el costo del envío.

Reglas:

- Exactamente 60 minutos no se considera retraso.
- Más de 60 minutos sí se considera retraso.
- La devolución corresponde al costo del envío.
- Si el envío fue gratuito, la devolución es Bs 0.
- No inventar penalizaciones, porcentajes ni compensaciones adicionales.

---

## 6. REQUISITOS FUNCIONALES

El sistema debe permitir las siguientes operaciones:

1. Registrar productos y combos.
2. Mostrar el menú disponible según el día.
3. Registrar clientes y validar sus teléfonos.
4. Registrar pedidos locales, para llevar y delivery.
5. Agregar y quitar productos mientras el pedido esté registrado.
6. Mostrar el detalle del pedido.
7. Calcular subtotal, descuentos, cargos y total.
8. Cambiar el estado del pedido respetando las transiciones válidas.
9. Procesar pagos y mostrar el comprobante.
10. Generar un reporte de ventas del día por tipo de pedido.
11. Mostrar los tres productos más vendidos.

Estas funcionalidades deben implementarse utilizando las clases y métodos establecidos en el UML.

No crear módulos, servicios o funcionalidades adicionales para resolver operaciones que ya corresponden a las clases existentes.

---

## 7. SOLID — OBLIGATORIO

Aplicar los cinco principios SOLID sin alterar la arquitectura UML.

### S — Single Responsibility Principle

Cada clase debe tener una responsabilidad definida.

- No mezclar responsabilidades de productos, pedidos, pagos y gestión del restaurante.
- No introducir lógica de pagos dentro de productos.
- No introducir lógica de productos dentro de los métodos de pago.
- No concentrar toda la lógica del sistema en `Restaurante`.
- Mantener las responsabilidades asignadas por el diagrama.

### O — Open/Closed Principle

El código debe permitir extender comportamientos sin modificar innecesariamente las clases existentes.

- Utilizar herencia y polimorfismo.
- Evitar condicionales por tipo.
- Las clases existentes deben funcionar con nuevas implementaciones compatibles.
- No duplicar lógica para incorporar comportamientos equivalentes.

No crear abstracciones adicionales que no estén autorizadas por el UML.

### L — Liskov Substitution Principle

Las subclases deben poder utilizarse donde se espera su clase padre sin romper el comportamiento.

- Respetar los contratos de los métodos heredados.
- Mantener las validaciones y restricciones correspondientes.
- No cambiar arbitrariamente los resultados esperados de los métodos.
- No eliminar comportamientos heredados necesarios.

### I — Interface Segregation Principle

Las clases no deben depender de métodos que no les corresponden.

- Mantener los contratos abstractos definidos en el UML.
- No agregar métodos innecesarios a las clases abstractas.
- No obligar a una subclase a implementar comportamientos ajenos a su responsabilidad.

### D — Dependency Inversion Principle

Las dependencias deben respetar las abstracciones existentes.

- Utilizar `MetodoPago` como contrato para los métodos de pago.
- Evitar dependencias innecesarias entre clases concretas.
- Mantener las relaciones definidas por el UML.
- No introducir contenedores de dependencias, frameworks ni mecanismos externos.

---

## 8. CLEAN CODE — OBLIGATORIO

El código debe ser legible, sencillo, consistente y fácil de mantener.

Reglas:

- Nombres de clases en `PascalCase`.
- Nombres de métodos y atributos en `snake_case`.
- Identificadores en español.
- Métodos pequeños y con una responsabilidad clara.
- Evitar código duplicado.
- Evitar bloques de código innecesariamente extensos.
- Evitar anidamientos excesivos.
- Evitar variables innecesarias.
- Evitar números mágicos cuando representen reglas de negocio.
- Evitar comentarios que repitan literalmente lo que hace el código.
- No utilizar comentarios en inglés.
- No agregar documentación excesiva o artificial.
- No implementar soluciones innecesariamente complejas.
- No utilizar trucos o construcciones avanzadas que dificulten la comprensión.
- Utilizar excepciones claras cuando una operación no sea válida.
- No ocultar errores mediante excepciones genéricas.
- No utilizar `pass` para simular funcionalidades implementadas.
- No dejar métodos incompletos.

El código debe ser comprensible y explicable por un estudiante que está aprendiendo POO.

---

## 9. COMPATIBILIDAD Y MANTENIBILIDAD DEL CÓDIGO

Esta sección es obligatoria para todos los cambios futuros.

El código debe poder ampliarse, corregirse y modificarse sin romper las funcionalidades que ya funcionan.

### 9.1. Compatibilidad hacia atrás

Cuando se agregue, elimine o modifique código:

- Mantener funcionando las clases existentes.
- Mantener las firmas de los métodos existentes, salvo que el usuario solicite cambiarlas.
- Mantener los nombres y contratos públicos.
- No eliminar atributos o métodos que otras clases utilicen.
- No cambiar el comportamiento de métodos existentes sin justificación y autorización.
- No modificar archivos ajenos a la solicitud.
- No duplicar implementaciones existentes.
- No introducir dependencias innecesarias entre clases.

Una modificación debe preservar el comportamiento anterior que no haya sido solicitado cambiar.

### 9.2. Cambios mínimos y controlados

Cuando se solicite un cambio:

1. Identificar exactamente qué clase y método deben modificarse.
2. Revisar qué otras clases utilizan ese comportamiento.
3. Identificar las dependencias afectadas.
4. Realizar el cambio más pequeño que resuelva la solicitud.
5. Mantener intacto el código que no necesita modificarse.
6. Actualizar únicamente las partes dependientes que realmente lo requieran.
7. Verificar que las funcionalidades anteriores continúen operando.

No aprovechar una solicitud pequeña para reorganizar todo el proyecto.

### 9.3. Agregar funcionalidades

Al agregar una nueva funcionalidad:

- Reutilizar las clases y métodos existentes.
- Respetar los contratos y las relaciones.
- No duplicar responsabilidades.
- No introducir clases innecesarias.
- No cambiar reglas de negocio existentes.
- No modificar resultados de operaciones anteriores.
- Mantener el polimorfismo.
- Comprobar que las funcionalidades anteriores sigan funcionando.

### 9.4. Eliminar funcionalidades

Cuando se solicite eliminar algo:

- Identificar sus dependencias.
- Comprobar si otras clases lo utilizan.
- No dejar referencias rotas.
- No eliminar métodos o atributos compartidos sin revisar sus consumidores.
- Adaptar únicamente las dependencias que resulten afectadas.
- Mantener operativas las funcionalidades restantes.

Si eliminar un elemento puede romper una funcionalidad existente, explicar el impacto antes de realizar cambios que contradigan el alcance solicitado.

### 9.5. No romper código funcional

Está prohibido solucionar un problema introduciendo otro.

No se debe:

- Corregir una clase rompiendo otra.
- Cambiar la firma de un método sin actualizar sus dependencias.
- Duplicar métodos para evitar corregir el original.
- Crear implementaciones alternativas que generen comportamientos inconsistentes.
- Eliminar validaciones para hacer que una operación funcione.
- Desactivar pruebas para ocultar errores.
- Cambiar reglas de negocio para conseguir que una prueba pase.

---

## 10. DESARROLLO PROGRESIVO POR CLASE

El proyecto se desarrollará por partes. Cada solicitud del usuario determinará exactamente qué se debe implementar.

### 10.1. Alcance de cada solicitud

Cuando se solicite una clase:

- Implementar únicamente la clase solicitada.
- Respetar su posición en el UML.
- Implementar sus atributos y métodos correspondientes.
- Aplicar encapsulación, herencia, abstracción y polimorfismo cuando corresponda.
- Implementar sus validaciones y reglas de negocio.
- Considerar la compatibilidad con las clases existentes.
- No generar automáticamente el resto del proyecto.

No adelantar clases que todavía no hayan sido solicitadas.

### 10.2. Dependencias

Si una clase necesita interactuar con otra que todavía no está implementada:

- Utilizar únicamente los contratos y métodos definidos en el UML.
- No inventar una implementación ficticia de la otra clase.
- No crear clases temporales.
- No crear objetos simulados para aparentar que la funcionalidad está completa.
- Señalar qué dependencia debe existir para que la integración funcione.

### 10.3. Código solicitado

Cuando el usuario solicite código, entregar:

1. El nombre del archivo al que corresponde.
2. La clase completa cuando se solicite implementar o actualizar una clase.
3. Los imports permitidos y estrictamente necesarios.
4. Una explicación breve de las responsabilidades y decisiones importantes.
5. Las dependencias reales que necesita para integrarse.

No entregar fragmentos incompletos cuando se haya solicitado la clase completa.

No repetir todo el proyecto cuando solo se haya solicitado una clase.

---

## 11. PRUEBAS Y VERIFICACIÓN

El código debe verificarse progresivamente.

Se requieren al menos ocho pruebas mediante `assert`, según el documento original.

Las pruebas deben contemplar:

- Validación de precios.
- Validación de cantidades.
- Validación del teléfono.
- Validación del código QR.
- Cálculo de precios de productos.
- Cálculo de combos con la variante F.
- Combos que contienen otros combos.
- Conteo de platos dentro de combos anidados.
- Cálculo de envases para pedidos para llevar.
- Cálculo de cargos de delivery.
- Validación del pedido mínimo.
- Restricciones de los métodos de pago.
- Transiciones de estado.
- Compensación por retraso de delivery.

Reglas:

- No inventar resultados esperados.
- Calcular los resultados conforme a las reglas de negocio.
- No modificar el código para ocultar fallos de las pruebas.
- No eliminar pruebas que detecten errores reales.
- Comprobar que las modificaciones no rompan los comportamientos anteriores.

Las pruebas deben ejecutarse sin librerías externas.

---

## 12. PROHIBICIONES ABSOLUTAS

No realizar ninguna de las siguientes acciones sin autorización:

- Rediseñar el UML.
- Cambiar la arquitectura del proyecto.
- Crear clases adicionales.
- Cambiar la herencia.
- Cambiar nombres de clases, atributos o métodos.
- Agregar librerías o dependencias.
- Crear funcionalidades no solicitadas.
- Inventar reglas de negocio.
- Utilizar reglas de variantes diferentes a F.
- Utilizar `isinstance()` o `type()` para resolver el polimorfismo.
- Resolver comportamientos mediante condicionales por tipo.
- Duplicar lógica existente.
- Crear clases ficticias o temporales.
- Crear métodos vacíos o simulados.
- Eliminar validaciones.
- Modificar código funcional sin necesidad.
- Reescribir archivos completos cuando solo se necesita un cambio localizado.
- Entregar código que dependa de implementaciones inexistentes.
- Afirmar que el código funciona si no se ha verificado.

---

## 13. PROTOCOLO OBLIGATORIO DE RESPUESTA DE LA IA

Antes de generar o modificar código, la IA debe interpretar la solicitud y respetar las siguientes reglas.

### 13.1. Interpretación

Identificar:

- Qué clase o archivo se está solicitando.
- Qué responsabilidad tiene según el UML.
- Qué atributos y métodos le corresponden.
- Qué reglas de negocio debe cumplir.
- Qué clases existentes utiliza.
- Qué restricciones técnicas se aplican.

### 13.2. Implementación

- Generar únicamente lo solicitado.
- Aplicar los cuatro pilares de la POO.
- Aplicar SOLID y Clean Code.
- Mantener la arquitectura.
- Mantener la compatibilidad.
- Evitar código innecesario.
- No asumir información faltante.

### 13.3. Verificación

Antes de entregar el código, comprobar:

- Que no se haya cambiado el UML.
- Que no se hayan inventado elementos.
- Que se hayan respetado los nombres.
- Que se hayan aplicado las validaciones.
- Que se hayan utilizado los métodos polimórficos.
- Que no se hayan agregado imports prohibidos.
- Que no se hayan roto contratos existentes.
- Que no se hayan modificado reglas de negocio.
- Que el código pueda integrarse con las clases existentes.

### 13.4. Cuando exista un problema

Si la solicitud no puede implementarse respetando estas reglas:

1. No improvisar una solución.
2. No cambiar silenciosamente la arquitectura.
3. Explicar cuál es la incompatibilidad.
4. Identificar las clases o métodos afectados.
5. Proponer el cambio mínimo necesario.
6. Esperar autorización cuando el cambio altere el UML, las reglas de negocio o el alcance solicitado.

### 13.5. Regla final

La IA es una herramienta de asistencia para implementar el proyecto, no la responsable de rediseñarlo.

Debe ejecutar las instrucciones del usuario respetando este documento, el diagrama UML y las reglas de negocio.

**Prioridad absoluta: fidelidad al diseño, cumplimiento de las reglas, código funcional, compatibilidad entre clases y mantenimiento sin romper funcionalidades existentes.**

No agregar más de lo solicitado. No quitar lo que debe permanecer. No inventar lo que no está definido.
### Estructura de carpetas a seguir explicitamente
restaurante_app/
│
├── main.py                    # Punto de entrada de la aplicación / Orquestador
│
├── modelos/                   # Clases principales del dominio
│   |
│   ├── restaurante.py         # Clase Restaurante
│   ├── cliente.py             # Clase Cliente
│   └── producto.py            # Clase Producto
│
├── pedidos/                   # Módulo de gestión de pedidos y herencia
│   |
│   ├── pedido.py              # Superclase Pedido
│   ├── pedido_local.py        # Hereda de Pedido
│   ├── pedido_delivery.py     # Hereda de Pedido
│   ├── pedido_para_llevar.py  # Hereda de PedidoDelivery
│   └── detalle_pedido.py      # Clase DetallePedido
│
├── platos/                    # Módulo de platos / menú y herencia
│   |
│   ├── plato.py               # Superclase Plato
│   ├── refresco_natural.py    # Hereda de Plato
│   ├── bebida_preparada.py    # Hereda de Plato
│   ├── gaseosa.py             # Hereda de Plato
│   ├── combo.py               # Clase Combo
│   └── producto_combo.py      # Clase ProductoCombo
│
└── pagos/                     # Módulo de pasarela de pagos y herencia
    |
    ├── metodo_pago.py         # Superclase MetodoPago
    ├── pago_efectivo.py       # Hereda de MetodoPago
    ├── pago_qr.py             # Hereda de MetodoPago
    └── pago_tarjeta.py        # Hereda de MetodoPago