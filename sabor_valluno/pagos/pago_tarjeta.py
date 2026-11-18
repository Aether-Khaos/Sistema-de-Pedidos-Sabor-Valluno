from metodo_pago import MetodoPago


class PagoTarjeta(MetodoPago):
    """Pago con tarjeta. Aplica una comisión del 3% a cargo del cliente.
    No está permitido para pedidos tipo delivery."""

    def __init__(self, pedido):
        super().__init__(pedido)
        self._comision = 0.03  # 3%

    @property
    def comision(self):
        return self._comision

    @comision.setter
    def comision(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("La comisión debe ser numérica")
        if valor < 0 or valor > 1:
            raise ValueError("La comisión debe estar entre 0 y 1")
        self._comision = float(valor)

    def calcular_comision(self):
        """Calcula y retorna la comisión del 3% sobre el total del pedido."""
        total = self._pedido.calcular_total()
        return round(total * self._comision, 2)

    def procesar_pago(self):
        """Procesa el pago con tarjeta aplicando la comisión.
        Rechaza el pago si el pedido es tipo delivery."""
        if self._pedido.__class__.__name__ == "PedidoDelivery":
            raise ValueError(
                "Los pedidos delivery no aceptan pago con tarjeta"
            )
        total = self._pedido.calcular_total()
        comision = self.calcular_comision()
        total_con_comision = round(total + comision, 2)
        return total_con_comision