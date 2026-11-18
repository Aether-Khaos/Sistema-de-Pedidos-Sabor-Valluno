# Bitácora – Módulo de Clientes y Pedidos

## Clases implementadas
- **Cliente**: `nombre`, `telefono`, `validar_telefono()`.
- **Pedido** (abstracta): `#numero`, `#cliente`, `#detalle`, `#estado`,
  `#fecha_registro`, `#metodo_pago`; métodos `asignar_producto`,
  `quitar_producto`, `calcular_subtotal`, `calcular_total`,
  `cambiar_estado`, `cancelar`, `gestionar_detalle`.
- **DetallePedido**: `producto`, `cantidad`, `calcular_subtotal()`,
  `costar_platos()`.

## Decisiones de diseño
| Decisión | Justificación |
|---|---|
| `Pedido` es **abstracta** (`ABC`) | Cada tipo de pedido define su propio `calcular_cargos()`. |
| Atributos `#` (protegidos) se representan con nombre normal (convención Python) | El diagrama usa `#` para protected; Python no fuerza visibilidad. |
| `calcular_subtotal` en `Pedido` delega en cada `DetallePedido` | Única fuente de verdad del cálculo por línea. |
| `calcular_total` = subtotal + `calcular_cargos()` | El cargo varía por especialización. |
| `fecha_registro` usa `datetime.now()` | Marca temporal automática al crear el pedido. |

## Flujo típico
1. `Cliente.validar_telefono()` → `True/False`.
2. `Pedido.asignar_producto(producto, cantidad)` crea un `DetallePedido`.
3. `Pedido.calcular_subtotal()` recorre el detalle.
4. `Pedido.calcular_total()` añade cargos del tipo concreto.
5. `Pedido.cambiar_estado(...)` / `cancelar()` modifican el estado.