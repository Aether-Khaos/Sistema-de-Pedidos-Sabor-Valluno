# Bitácora – Métodos de Pago

## Clases
- **MetodoPago** (ABC): `procesar_pago(monto)` abstracto.
- **PagoEfectivo**: `monto_recibido`, `redondear_total()`,
  `calcular_cambio()`, `procesar_pago()`.
- **PagoQr**: `codigo_transaccion`, `validar_codigo()`, `procesar_pago()`.
- **PagoTarjeta**: `comision`, `calcular_comision()`, `procesar_pago()`.

## Reglas
| Método | Regla |
|---|---|
| Efectivo | Redondeo a 0.10; falla si `monto_recibido < total`. |
| QR | Código válido si longitud ≥ 6. |
| Tarjeta | Cobra `monto + comisión%`. |

## Observaciones
- El patrón **Strategy** queda implícito: `Pedido` contiene un
  `metodo_pago` y delega `procesar_pago(total)`.
- Cada subclase imprime un mensaje de éxito/fallo para trazabilidad.