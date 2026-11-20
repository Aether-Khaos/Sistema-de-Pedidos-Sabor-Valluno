from abc import ABC, abstractmethod
from datetime import datetime
from .detalle_pedido import DetallePedido


class Pedido(ABC):

    _TRANSICIONES_VALIDAS = {
        "REGISTRADO": ["EN_PREPARACION"],
        "EN_PREPARACION": ["LISTO"],
        "LISTO": ["ENTREGADO"],
        "ENTREGADO": [],
        "CANCELADO": [],
    }

    def __init__(self, numero, cliente, fecha_registro=None):
        self._numero = None
        self._cliente = None
        self._detalle = []
        self._estado = "REGISTRADO"
        self._fecha_registro = None
        self._metodo_pago = None

        self.numero = numero
        self.cliente = cliente
        if fecha_registro is None:
            fecha_registro = datetime.now()
        self.fecha_registro = fecha_registro

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if valor is None or str(valor).strip() == "":
            raise ValueError("El número de pedido no puede estar vacío.")
        self._numero = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if valor is None:
            raise ValueError("El pedido debe tener un cliente.")
        self._cliente = valor

    @property
    def detalle(self):
        return tuple(self._detalle)

    @property
    def estado(self):
        return self._estado

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, valor):
        if valor is None:
            raise ValueError("La fecha de registro no puede ser None.")
        self._fecha_registro = valor

    @property
    def metodo_pago(self):
        return self._metodo_pago

    def agregar_producto(self, producto, cantidad):
        if self._estado != "REGISTRADO":
            raise ValueError("Solo se pueden agregar productos a un pedido REGISTRADO.")

        nuevo = DetallePedido(producto, cantidad)
        if not producto.esta_disponible():
            raise ValueError("El producto no está disponible.")

        for item in self._detalle:
            if item.producto == producto:
                item.cantidad = item.cantidad + nuevo.cantidad
                return
        self._detalle.append(nuevo)

    def quitar_producto(self, producto):
        if self._estado != "REGISTRADO":
            raise ValueError("Solo se pueden quitar productos de un pedido REGISTRADO.")

        for item in self._detalle:
            if item.producto == producto:
                self._detalle.remove(item)
                return
        raise ValueError("El producto no existe en el pedido.")

    def calcular_subtotal(self):
        return round(sum(item.calcular_subtotal() for item in self._detalle), 2)

    def contar_platos(self):
        return sum(item.contar_platos() for item in self._detalle)

    @abstractmethod
    def calcular_cargos(self):
        """Cargos adicionales según el tipo de pedido."""

    def calcular_total(self):
        return round(self.calcular_subtotal() + self.calcular_cargos(), 2)

    def cambiar_estado(self, nuevo_estado, fecha_entrega=None):
        nuevo_estado = str(nuevo_estado).strip().upper()
        permitidos = self._TRANSICIONES_VALIDAS[self._estado]
        if nuevo_estado not in permitidos:
            raise ValueError(f"Transición inválida: {self._estado} -> {nuevo_estado}")
        self._estado = nuevo_estado

    def cancelar(self):
        if self._estado != "REGISTRADO":
            raise ValueError("Solo se puede cancelar un pedido REGISTRADO.")
        self._estado = "CANCELADO"

    def pagar(self, metodo_pago):
        if metodo_pago is None:
            raise ValueError("Debe indicar un método de pago.")
        if len(self._detalle) == 0:
            raise ValueError("No se puede pagar un pedido sin productos.")
        if self._estado == "CANCELADO":
            raise ValueError("No se puede pagar un pedido CANCELADO.")
        if self._metodo_pago is not None:
            raise ValueError("El pedido ya fue pagado.")

        metodo_pago.procesar_pago(self.calcular_total())
        self._metodo_pago = metodo_pago

    def mostrar_detalle(self):
        lineas = [
            f"Pedido N° {self._numero}",
            f"Cliente: {self._cliente}",
            f"Estado: {self._estado}",
            "Ítems:",
        ]
        for item in self._detalle:
            lineas.append(
                f"  - {item.producto} x{item.cantidad} = Bs {item.calcular_subtotal():.2f}"
            )
        lineas.append(f"Subtotal: Bs {self.calcular_subtotal():.2f}")
        lineas.append(f"Cargos:   Bs {self.calcular_cargos():.2f}")
        lineas.append(f"TOTAL:    Bs {self.calcular_total():.2f}")
        return "\n".join(lineas)