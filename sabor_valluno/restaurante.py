"""
Sistema de Restaurante - Implementación del diagrama orientado a objetos.
Cumple estrictamente el modelo: Fachada, Clientes/Pedidos, Pedidos
especializados, Menú/Platos (jerarquía) y Métodos de Pago.
"""

from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# 1. MÓDULO DE CLIENTES Y PEDIDOS
# ============================================================

class Cliente:
    def __init__(self, nombre: str, telefono: str):
        self.nombre = nombre
        self.telefono = telefono

    def validar_telefono(self) -> bool:
        """Valida que el teléfono tenga al menos 7 dígitos numéricos."""
        return self.telefono.isdigit() and len(self.telefono) >= 7

    def __str__(self):
        return f"Cliente({self.nombre}, {self.telefono})"


class DetallePedido:
    def __init__(self, producto, cantidad: int):
        self.producto = producto          # Instancia de Plato/Producto/Combo
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        return self.producto.calcular_precio() * self.cantidad

    def costar_platos(self) -> float:
        return self.calcular_subtotal()

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} = {self.calcular_subtotal():.2f}"


class Pedido(ABC):
    """Clase base de pedidos (especializada por tipo de pedido)."""

    def __init__(self, numero: int, cliente: Cliente, metodo_pago):
        self.numero = numero
        self.cliente = cliente
        self.detalle: list[DetallePedido] = []
        self.estado = "REGISTRADO"
        self.fecha_registro = datetime.now()
        self.metodo_pago = metodo_pago

    # ---- Gestión de detalle ----
    def asignar_producto(self, producto, cantidad: int = 1):
        self.detalle.append(DetallePedido(producto, cantidad))

    def quitar_producto(self, producto):
        self.detalle = [d for d in self.detalle if d.producto is not producto]

    def gestionar_detalle(self) -> list:
        return self.detalle

    # ---- Cálculos ----
    def calcular_subtotal(self) -> float:
        return sum(d.calcular_subtotal() for d in self.detalle)

    def calcular_total(self) -> float:
        return self.calcular_subtotal() + self.calcular_cargos()

    # ---- Estado ----
    def cambiar_estado(self, nuevo_estado: str):
        self.estado = nuevo_estado

    def cancelar(self):
        self.estado = "CANCELADO"

    # ---- Abstracto: cada tipo de pedido define sus cargos ----
    @abstractmethod
    def calcular_cargos(self) -> float:
        ...

    def __str__(self):
        return (f"Pedido#{self.numero} [{self.estado}] "
                f"subtotal={self.calcular_subtotal():.2f} "
                f"total={self.calcular_total():.2f}")


# ============================================================
# 3. TIPOS DE PEDIDOS (ESPECIALIZACIÓN)
# ============================================================

class PedidoDelivery(Pedido):
    def __init__(self, numero, cliente, metodo_pago,
                 zona: str, direccion: str, pedido_minimo: float):
        super().__init__(numero, cliente, metodo_pago)
        self.zona = zona
        self.direccion = direccion
        self.pedido_minimo = pedido_minimo

    def calcular_cargos(self) -> float:
        # Cargo por delivery según zona
        recargos = {"A": 3.0, "B": 5.0, "C": 8.0}
        return recargos.get(self.zona.upper(), 10.0)

    def validar_pedido_minimo(self) -> bool:
        return self.calcular_subtotal() >= self.pedido_minimo

    def pagar(self) -> bool:
        if not self.validar_pedido_minimo():
            print(f"⚠ Pedido#{self.numero}: no alcanza el mínimo "
                  f"({self.pedido_minimo:.2f})")
            return False
        return self.metodo_pago.procesar_pago(self.calcular_total())


class PedidoLocal(Pedido):
    def __init__(self, numero, cliente, metodo_pago, numero_mesa: int):
        super().__init__(numero, cliente, metodo_pago)
        self.numero_mesa = numero_mesa

    def calcular_cargos(self) -> float:
        # Servicio de mesa (10% del subtotal)
        return round(self.calcular_subtotal() * 0.10, 2)


class PedidoParaLlevar(Pedido):
    def __init__(self, numero, cliente, metodo_pago, costo_envase: float):
        super().__init__(numero, cliente, metodo_pago)
        self.costo_envase = costo_envase

    def calcular_cargos(self) -> float:
        # Envase por cada ítem del detalle
        return self.costo_envase * len(self.detalle)


# ============================================================
# 4. MENÚ Y PLATOS (JERARQUÍA)
# ============================================================

class Plato(ABC):
    """Clase base abstracta de la jerarquía de productos del menú."""

    def __init__(self, nombre: str, precio_base: float, disponible: bool = True):
        self.nombre = nombre
        self.precio_base = precio_base
        self._disponible = disponible

    @abstractmethod
    def calcular_precio(self) -> float:
        ...

    def esta_disponible(self) -> bool:
        return self._disponible

    def costar_platos(self) -> float:
        return self.calcular_precio()

    def __str__(self):
        return f"{self.nombre} (S/ {self.calcular_precio():.2f})"


class Producto(Plato):
    """Producto simple del menú."""

    def calcular_precio(self) -> float:
        return self.precio_base


class RefrescoNatural(Plato):
    def __init__(self, nombre, precio_base, disponible=True):
        super().__init__(nombre, precio_base, disponible)

    def calcular_precio(self) -> float:
        # Refresco natural: precio base + 10% por servicio
        return round(self.precio_base * 1.10, 2)


class BebidaEnvasada(Plato):
    def calcular_precio(self) -> float:
        return self.precio_base


class Gaseosa(BebidaEnvasada):
    def calcular_precio(self) -> float:
        # Gaseosa: precio base + impuesto (5%)
        return round(self.precio_base * 1.05, 2)


class ProductoCombo:
    """Ítem interno de un combo."""

    def __init__(self, producto: Plato, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        return self.producto.calcular_precio() * self.cantidad

    def esta_disponible(self) -> bool:
        return self.producto.esta_disponible()

    def costar_platos(self) -> float:
        return self.calcular_subtotal()


class Combo(Plato):
    def __init__(self, nombre, descuento: float, disponible=True):
        super().__init__(nombre, 0.0, disponible)
        self.descuento = descuento                 # porcentaje 0-100
        self.producto_combo: list[ProductoCombo] = []

    def agregar_producto_combo(self, producto: Plato, cantidad: int = 1):
        self.producto_combo.append(ProductoCombo(producto, cantidad))

    def calcular_precio(self) -> float:
        subtotal = sum(pc.calcular_subtotal() for pc in self.producto_combo)
        return round(subtotal * (1 - self.descuento / 100), 2)

    def esta_disponible(self) -> bool:
        if not self.producto_combo:
            return False
        return all(pc.esta_disponible() for pc in self.producto_combo)

    def costar_platos(self) -> float:
        return self.calcular_precio()


# ============================================================
# 5. MÉTODOS DE PAGO
# ============================================================

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        ...


class PagoEfectivo(MetodoPago):
    def __init__(self, monto_recibido: float):
        self.monto_recibido = monto_recibido

    def redondear_total(self, monto: float) -> float:
        # Redondeo a múltiplos de 0.10
        return round(monto, 1)

    def calcular_cambio(self, monto: float) -> float:
        return round(self.monto_recibido - self.redondear_total(monto), 2)

    def procesar_pago(self, monto: float) -> bool:
        total = self.redondear_total(monto)
        if self.monto_recibido < total:
            print(f"✗ Efectivo insuficiente: faltan {total - self.monto_recibido:.2f}")
            return False
        print(f"✓ Pago en efectivo OK. Cambio: {self.calcular_cambio(monto):.2f}")
        return True


class PagoQr(MetodoPago):
    def __init__(self, codigo_transaccion: str):
        self.codigo_transaccion = codigo_transaccion

    def validar_codigo(self) -> bool:
        return len(self.codigo_transaccion) >= 6

    def procesar_pago(self, monto: float) -> bool:
        if not self.validar_codigo():
            print("✗ Código QR inválido")
            return False
        print(f"✓ Pago QR OK por S/ {monto:.2f} (código {self.codigo_transaccion})")
        return True


class PagoTarjeta(MetodoPago):
    def __init__(self, comision: float):
        self.comision = comision       # porcentaje 0-100

    def calcular_comision(self, monto: float) -> float:
        return round(monto * self.comision / 100, 2)

    def procesar_pago(self, monto: float) -> bool:
        total_cobrado = monto + self.calcular_comision(monto)
        print(f"✓ Pago con tarjeta OK. Total cobrado: S/ {total_cobrado:.2f} "
              f"(comisión S/ {self.calcular_comision(monto):.2f})")
        return True


# ============================================================
# 1. CLASE PRINCIPAL (FACHADA)
# ============================================================

class Restaurante:
    def __init__(self):
        self.productos: list[Plato] = []
        self.clientes: list[Cliente] = []
        self.pedidos: list[Pedido] = []
        self._siguiente_pedido = 1

    # ---- Registro ----
    def registrar_producto(self, producto: Plato):
        self.productos.append(producto)
        print(f"+ Producto registrado: {producto}")

    def registrar_cliente(self, cliente: Cliente) -> bool:
        if not cliente.validar_telefono():
            print(f"✗ Cliente {cliente.nombre}: teléfono inválido")
            return False
        self.clientes.append(cliente)
        print(f"+ Cliente registrado: {cliente}")
        return True

    def registrar_pedido(self, pedido: Pedido):
        if pedido.cliente not in self.clientes:
            print("✗ Cliente no registrado")
            return False
        pedido.numero = self._siguiente_pedido
        self._siguiente_pedido += 1
        self.pedidos.append(pedido)
        print(f"+ Pedido registrado: {pedido}")
        return True

    # ---- Consultas ----
    def mostrar_menu(self):
        print("\n===== MENÚ DEL RESTAURANTE =====")
        for p in self.productos:
            estado = "✓" if p.esta_disponible() else "✗"
            print(f" [{estado}] {p}")
        print("================================\n")

    def generar_reporte(self):
        print("\n========== REPORTE GENERAL ==========")
        print(f"Clientes registrados : {len(self.clientes)}")
        print(f"Productos en menú    : {len(self.productos)}")
        print(f"Pedidos registrados  : {len(self.pedidos)}")
        total = 0.0
        for p in self.pedidos:
            print(f"  - {p}")
            if p.estado != "CANCELADO":
                total += p.calcular_total()
        print(f"Total facturado (no cancelados): S/ {total:.2f}")
        print("=====================================\n")