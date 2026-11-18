# Bitácora – Fachada `Restaurante`

## Responsabilidades
- `registrar_producto(producto)` → añade a `self.productos`.
- `registrar_cliente(cliente)` → valida teléfono antes de añadir.
- `registrar_pedido(pedido)` → verifica cliente registrado y asigna
  número correlativo (`_siguiente_pedido`).
- `mostrar_menu()` → imprime disponibilidad.
- `generar_reporte()` → totales, conteos y facturación (excluye cancelados).

## Atributos internos
- `productos: list[Plato]`
- `clientes: list[Cliente]`
- `pedidos: list[Pedido]`
- `_siguiente_pedido: int` (autoincremental)

## Integración con el resto del modelo
Restaurante
├── registra → Cliente (valida teléfono)
├── registra → Plato (Producto | RefrescoNatural | BebidaEnvasada | Combo)
└── registra → Pedido (Delivery | Local | ParaLlevar)
└── usa → MetodoPago (Efectivo | Qr | Tarjeta)

## Salida esperada del reporte
- Nº de clientes, productos y pedidos.
- Por pedido: número, estado, subtotal y total.
- Facturación total de pedidos no cancelados.