# Bitácora – Tipos de Pedidos (Especialización)

## Clases implementadas
- **PedidoDelivery**: `zona`, `direccion`, `pedido_minimo`;
  `calcular_cargos()`, `validar_pedido_minimo()`, `pagar()`.
- **PedidoLocal**: `numero_mesa`; `calcular_cargos()`.
- **PedidoParaLlevar**: `costo_envase`; `calcular_cargos()`.

## Reglas de negocio aplicadas
| Tipo | Cálculo de cargos |
|---|---|
| Delivery | Tarifa por zona: A=3, B=5, C=8, otra=10 |
| Local | 10 % del subtotal (servicio de mesa) |
| Para llevar | `costo_envase × número de ítems` |

## Validaciones
- `PedidoDelivery.validar_pedido_minimo()` compara el subtotal con
  `pedido_minimo`. `pagar()` la invoca antes de cobrar.
- Los tres tipos heredan `cambiar_estado` y `cancelar` de `Pedido`.

## Observaciones
- `pagar()` solo está explícito en `PedidoDelivery` según el diagrama;
  en local/para llevar se usa `metodo_pago.procesar_pago(total)` directamente.