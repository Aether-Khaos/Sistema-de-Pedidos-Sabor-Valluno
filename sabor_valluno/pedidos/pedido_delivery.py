from datetime import datetime
from .pedido import Pedido


class PedidoDelivery(Pedido):

    _TARIFAS_ZONA = {
        "Cercado": 8.0,
        "Quillacollo": 15.0,
        "Sacaba": 15.0,
        "Vinto": 20.0,
    }
    _MONTO_ENVIO_GRATIS = 100.0
    _MINUTOS_MAXIMOS = 60

    def __init__(self, numero, cliente, zona, direccion,
                 pedido_minimo=30.0, fecha_registro=None):
        super().__init__(numero, cliente, fecha_registro)
        self._zona = None
        self._direccion = None
        self._pedido_minimo = 30.0
        self._retraso = False

        self.zona = zona
        self.direccion = direccion
        self.pedido_minimo = pedido_minimo

    @property
    def zona(self):
        return self._zona

    @zona.setter
    def zona(self, valor):
        if valor is None:
            raise ValueError("La zona no puede ser None.")
        zona = str(valor).strip().capitalize()
        if zona not in self._TARIFAS_ZONA:
            raise ValueError(
                "Zona inválida. Zonas válidas: " + ", ".join(self._TARIFAS_ZONA)
            )
        self._zona = zona

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        if valor is None or str(valor).strip() == "":
            raise ValueError("La dirección no puede estar vacía.")
        self._direccion = str(valor).strip()

    @property
    def pedido_minimo(self):
        return self._pedido_minimo

    @pedido_minimo.setter
    def pedido_minimo(self, valor):
        try:
            es_valido = valor > 0
        except TypeError:
            es_valido = False
        if not es_valido:
            raise ValueError("El pedido mínimo debe ser un número mayor que 0.")
        self._pedido_minimo = round(float(valor), 2)

    @property
    def retraso(self):
        return self._retraso

    def validar_pedido_minimo(self):
        if self.calcular_subtotal() >= self._pedido_minimo:
            return True
        raise ValueError(
            f"El pedido no alcanza el mínimo de Bs {self._pedido_minimo:.2f} para delivery."
        )

    def calcular_cargos(self):

        if self._retraso or self.calcular_subtotal() >= self._MONTO_ENVIO_GRATIS:
            return 0.0
        return self._TARIFAS_ZONA[self._zona]

    def cambiar_estado(self, nuevo_estado, fecha_entrega=None):
        super().cambiar_estado(nuevo_estado)
        if self._estado == "ENTREGADO":
            if fecha_entrega is None:
                fecha_entrega = datetime.now()
            minutos = (fecha_entrega - self._fecha_registro).total_seconds() / 60
            self._retraso = minutos > self._MINUTOS_MAXIMOS

    def pagar(self, metodo_pago):
        self.validar_pedido_minimo()
        if metodo_pago is None:
            raise ValueError("Debe indicar un método de pago.")
        if not metodo_pago.permite_delivery:
            raise ValueError("Este método de pago no está permitido para delivery.")
        super().pagar(metodo_pago)