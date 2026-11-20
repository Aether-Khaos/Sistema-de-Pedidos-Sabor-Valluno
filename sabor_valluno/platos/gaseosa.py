from platos.bebida_preparada import Bebida


class Gaseosa(Bebida):
    def calcular_precio(self):
        return super().calcular_precio()

    def esta_disponible(self, dia):
        return super().esta_disponible(dia)

    def contar_platos(self):
        return super().contar_platos()