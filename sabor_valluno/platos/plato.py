from modelos.producto import Producto


class Plato(Producto):
    def __init__(self, nombre, precio_base):
        super().__init__(nombre)
        self.precio_base = precio_base

        nombre_menu = " ".join(self.nombre.lower().split()).replace("í", "i")
        if nombre_menu == "sopa de mani":
            self._dias_disponible = ("lunes", "jueves")
        else:
            self._dias_disponible = self._DIAS_SEMANA

    @property
    def dias_disponible(self):
        return self._dias_disponible

    def calcular_precio(self):
        return self.precio_base

    def esta_disponible(self, dia):
        return self._normalizar_dia(dia) in self.dias_disponible

    def contar_platos(self):
        return 1