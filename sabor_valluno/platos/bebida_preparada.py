from modelos.producto import Producto


class Bebida(Producto):
    _VASOS_POR_JARRA = 3

    def __init__(self, nombre, precio_vaso):
        super().__init__(nombre)
        self.precio_vaso = precio_vaso

    @property
    def precio_vaso(self):
        return self.precio_base

    @precio_vaso.setter
    def precio_vaso(self, valor):
        self.precio_base = valor

    def calcular_precio(self):
        return self.precio_vaso

    def precio_jarra(self):
        return round(self.precio_vaso * self._VASOS_POR_JARRA, 2)

    def esta_disponible(self, dia):
        return self._normalizar_dia(dia) in self._DIAS_SEMANA

    def contar_platos(self):
        return 0