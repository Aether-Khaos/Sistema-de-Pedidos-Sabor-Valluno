from .pedido import Pedido


class PedidoParaLlevar(Pedido):

    def __init__(self, numero, cliente, costo_envase=2.0, fecha_registro=None):
        super().__init__(numero, cliente, fecha_registro)
        self._costo_envase = 2.0
        self.costo_envase = costo_envase

    @property
    def costo_envase(self):
        return self._costo_envase

    @costo_envase.setter
    def costo_envase(self, valor):
        try:
            es_valido = valor > 0
        except TypeError:
            es_valido = False
        if not es_valido:
            raise ValueError("El costo de envase debe ser un número mayor que 0.")
        self._costo_envase = round(float(valor), 2)

    def calcular_cargos(self):
        return round(self.contar_platos() * self._costo_envase, 2)