from abc import ABC, abstractmethod


class MetodoPago(ABC):
    """Clase abstracta base para los métodos de pago.
    Define el contrato común que deben cumplir todas las formas de pago."""

    def __init__(self, pedido):
        if pedido is None:
            raise ValueError("El pedido asociado al método de pago no puede ser nulo")
        self._pedido = pedido

    @property
    def pedido(self):
        return self._pedido

    @abstractmethod
    def procesar_pago(self):
        """Procesa el pago según la modalidad específica.
        Debe ser implementado por cada subclase concreta."""
        pass