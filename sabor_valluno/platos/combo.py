from modelos.producto import Producto
from platos.producto_combo import ProductoCombo


class Combo(Producto):
    _DESCUENTO_FIJO_CENTAVOS = 500  # Bs 5

    def __init__(self, nombre, producto_combo):
        super().__init__(nombre)
        self._descuento = 5  # Porcentaje de la variante F
        self._producto_combo = []

        for componente in producto_combo:
            self.agregar_producto_combo(componente)

        if sum(componente.cantidad for componente in self._producto_combo) < 2:
            raise ValueError("El combo debe contener al menos dos unidades de producto.")

        self.calcular_precio()  # Comprueba que el precio final sea positivo.

    @property
    def descuento(self):
        return self._descuento

    @property
    def producto_combo(self):
        return tuple(self._producto_combo)

    @property
    def precio_base(self):
        return round(sum(componente.calcular_subtotal() for componente in self._producto_combo), 2)

    def agregar_producto_combo(self, componente):
        if not isinstance(componente, ProductoCombo):
            raise TypeError("Agrega un ProductoCombo con su producto y cantidad.")

        if self._formaria_ciclo(componente.producto):
            raise ValueError("Un combo no puede contenerse directa ni indirectamente.")

        componente.calcular_subtotal()
        self._producto_combo.append(componente)

    def _formaria_ciclo(self, producto):
        pendientes = [producto]
        visitados = set()

        while pendientes:
            actual = pendientes.pop()
            if actual is self:
                return True
            if id(actual) in visitados:
                continue

            visitados.add(id(actual))
            for componente in getattr(actual, "producto_combo", ()):
                pendientes.append(componente.producto)

        return False

    def calcular_precio(self):
        base_centavos = round(self.precio_base * 100)
        porcentaje_a_cobrar = 100 - self.descuento

        # El 50 redondea medio centavo hacia arriba al dividir entre 100.
        con_rebaja = (base_centavos * porcentaje_a_cobrar + 50) // 100
        total_centavos = con_rebaja - self._DESCUENTO_FIJO_CENTAVOS

        if total_centavos <= 0:
            raise ValueError("El descuento dejaría el combo con un precio de cero o menos.")

        return total_centavos / 100

    def esta_disponible(self, dia):
        return all(componente.esta_disponible(dia) for componente in self._producto_combo)

    def contar_platos(self):
        return sum(componente.contar_platos() for componente in self._producto_combo)