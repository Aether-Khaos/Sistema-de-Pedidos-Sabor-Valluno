class DetallePedido:

    def __init__(self, producto, cantidad):
        self._producto = None
        self._cantidad = 0
        self.producto = producto
        self.cantidad = cantidad

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, valor):
        if valor is None:
            raise ValueError("El producto no puede ser None.")
        self._producto = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        try:
            es_valida = 1 <= valor <= 20 and valor == int(valor)
        except TypeError:
            es_valida = False
        if not es_valida:
            raise ValueError("La cantidad debe ser un entero entre 1 y 20.")
        self._cantidad = int(valor)

    def calcular_subtotal(self):
        return round(self._producto.calcular_precio() * self._cantidad, 2)

    def contar_platos(self):
        return self._producto.contar_platos() * self._cantidad
