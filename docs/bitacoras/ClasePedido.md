### Se hizo uso de las reglas del proyecto (Variante F) junto con la estructura del diagrama UML para la jerarquía de Pedido
- Callisaya Isai — Fecha: 19/11/2026 — Herramientas: Gemini y Claude Sonnet 5.5
- Definición del prompt base (Variante F): Se estructuró un prompt detallado a partir del diagrama UML y las reglas de la Variante F (envase para llevar de Bs 2.00 por plato, envío gratis desde Bs 100.00 en todas las zonas, pedido mínimo de Bs 30.00 y compensación por retraso mayor a 60 minutos), solicitando el código separado por clases, aplicando abstracción (`ABC`), encapsulación con `@property`, herencia y polimorfismo sin `isinstance()`.
- Revisión de reglas de transición de estados: Se consultó a Claude sobre la necesidad del diccionario `_TRANSICIONES_VALIDAS` dentro de `Pedido(ABC)` (*"¿Es necesario colocar las transiciones validas?"*), confirmando que se mantiene para controlar el flujo estricto (`REGISTRADO` → `EN_PREPARACION` → `LISTO` → `ENTREGADO` y cancelación solo desde `REGISTRADO`) mediante excepciones `ValueError`.
- Aclaración de estructura de archivos e importaciones en VS Code: Se tuvo que aclarar que cada clase se está implementando en un archivo `.py` independiente dentro de una carpeta `pedidos/` en Visual Studio Code (y no todas en un solo archivo). Debido a esto, se movieron las importaciones (`from abc import ABC, abstractmethod` y `from datetime import datetime`) únicamente al archivo de la clase `Pedido` y se verificaron las importaciones relativas entre archivos para su correcta ejecución.

Jerarquía de Pedidos

DetallePedido (Clase de Composición)

    Atributos / Métodos:

        producto
        cantidad
        + calcular_subtotal
        + contar_platos

Pedido (Clase Base Abstracta / Superclase)

    Atributos / Métodos:

        # numero
        # cliente
        # detalle
        # estado
        # fecha_registro
        # metodo_pago
        + agregar_producto
        + quitar_producto
        + calcular_subtotal
        + contar_platos
        + calcular_cargos (abstracto)
        + calcular_total
        + cambiar_estado
        + cancelar
        + pagar
        + mostrar_detalle

    Herencia: De esta clase heredan PedidoLocal, PedidoParaLlevar y PedidoDelivery.

PedidoLocal (Hereda de Pedido)

    Atributos / Métodos:

        numero_mesa
        + calcular_cargos

PedidoParaLlevar (Hereda de Pedido)

    Atributos / Métodos:

        costo_envase
        + calcular_cargos

PedidoDelivery (Hereda de Pedido)

    Atributos / Métodos:

        zona
        direccion
        pedido_minimo
        + calcular_cargos
        + validar_pedido_minimo
        + pagar
