class ProductoCombo:
    def __init__(self, producto, cantidad):
        metodos = ("calcular_precio", "esta_disponible", "contar_platos")
        if not all(callable(getattr(producto, metodo, None)) for metodo in metodos):
            raise TypeError("El componente debe ser un producto del menú.")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad < 1:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")

        self._producto = producto
        self._cantidad = cantidad

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    def calcular_subtotal(self):
        return round(self.producto.calcular_precio() * self.cantidad, 2)

    def esta_disponible(self, dia):
        return self.producto.esta_disponible(dia)

    def contar_platos(self):
        return self.producto.contar_platos() * self.cantidad