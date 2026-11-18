from metodo_pago import MetodoPago


class PagoQr(MetodoPago):
    """Pago mediante código QR. Valida que el código de transacción
    tenga exactamente 10 dígitos."""

    def __init__(self, pedido, codigo_transaccion):
        super().__init__(pedido)
        self.codigo_transaccion = codigo_transaccion

    @property
    def codigo_transaccion(self):
        return self._codigo_transaccion

    @codigo_transaccion.setter
    def codigo_transaccion(self, valor):
        if not self.validar_codigo(valor):
            raise ValueError(
                "El código de transacción debe tener exactamente 10 dígitos numéricos"
            )
        self._codigo_transaccion = str(valor)

    def validar_codigo(self, codigo):
        """Valida que el código tenga exactamente 10 dígitos numéricos."""
        if codigo is None:
            return False
        codigo_str = str(codigo)
        if len(codigo_str) != 10:
            return False
        return codigo_str.isdigit()

    def procesar_pago(self):
        """Procesa el pago QR tras validar el código de transacción."""
        if not self.validar_codigo(self._codigo_transaccion):
            raise ValueError("Código de transacción inválido")
        return True