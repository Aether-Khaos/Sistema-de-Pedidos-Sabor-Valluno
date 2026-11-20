from abc import ABC, abstractmethod


class Producto(ABC):
    _DIAS_SEMANA = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El producto debe tener un nombre.")
        self._nombre = nombre.strip()

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("El precio debe ser numérico.")
        precio = round(valor, 2)
        if not 0 < precio < float("inf"):
            raise ValueError("El precio debe ser positivo al expresarlo en centavos.")
        self._precio_base = precio

    @staticmethod
    def _normalizar_dia(dia):
        if not isinstance(dia, str):
            return ""
        dia = dia.strip().lower()
        return {"miercoles": "miércoles", "sabado": "sábado"}.get(dia, dia)

    @abstractmethod
    def calcular_precio(self):
        raise NotImplementedError

    @abstractmethod
    def esta_disponible(self, dia):
        raise NotImplementedError

    @abstractmethod
    def contar_platos(self):
        raise NotImplementedError