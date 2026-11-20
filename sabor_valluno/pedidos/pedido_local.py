from .pedido import Pedido


class PedidoLocal(Pedido):

    def __init__(self, numero, cliente, numero_mesa, fecha_registro=None):
        super().__init__(numero, cliente, fecha_registro)
        self._numero_mesa = None
        self.numero_mesa = numero_mesa

    @property
    def numero_mesa(self):
        return self._numero_mesa

    @numero_mesa.setter
    def numero_mesa(self, valor):
        try:
            es_valido = 1 <= valor <= 15 and valor == int(valor)
        except TypeError:
            es_valido = False
        if not es_valido:
            raise ValueError("El número de mesa debe ser un entero entre 1 y 15.")
        self._numero_mesa = int(valor)

    def calcular_cargos(self):
        return 0.0