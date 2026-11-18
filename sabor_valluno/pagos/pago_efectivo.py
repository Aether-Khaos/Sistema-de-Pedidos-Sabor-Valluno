from metodo_pago import MetodoPago


class PagoEfectivo(MetodoPago):
    """Pago en efectivo. Valida que el monto cubra el total y calcula el cambio."""

    def __init__(self, pedido, monto_recibido):
        super().__init__(pedido)
        self.monto_recibido = monto_recibido
        self._cambio = 0.0

    @property
    def monto_recibido(self):
        return self._monto_recibido

    @monto_recibido.setter
    def monto_recibido(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El monto recibido debe ser numérico")
        if valor <= 0:
            raise ValueError("El monto recibido debe ser mayor que cero")
        self._monto_recibido = float(valor)

    @property
    def cambio(self):
        return self._cambio

    def redondeo_total(self):
        """Redondea el total del pedido al entero superior para facilitar
        el pago en efectivo."""
        total = self._pedido.calcular_total()
        total_entero = int(total)
        if total > total_entero:
            return total_entero + 1
        return total_entero

    def calcular_cambio(self):
        """Calcula y retorna el cambio a devolver al cliente."""
        total = self._pedido.calcular_total()
        if self._monto_recibido < total:
            raise ValueError("El monto recibido no cubre el total a pagar")
        self._cambio = round(self._monto_recibido - total, 2)
        return self._cambio

    def procesar_pago(self):
        """Procesa el pago en efectivo, validando que el monto cubra el total."""
        total = self._pedido.calcular_total()
        if self._monto_recibido < total:
            raise ValueError("El monto recibido no cubre el total a pagar")
        self._cambio = round(self._monto_recibido - total, 2)
        return self._cambio