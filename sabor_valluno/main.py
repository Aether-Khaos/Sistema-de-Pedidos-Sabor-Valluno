from restaurante import (
    Restaurante, Cliente,
    Producto, RefrescoNatural, Gaseosa, BebidaEnvasada, Combo,
    PedidoDelivery, PedidoLocal, PedidoParaLlevar,
    PagoEfectivo, PagoQr, PagoTarjeta,
)

if __name__ == "__main__":
    r = Restaurante()

    # --- Productos ---
    lomo   = Producto("Lomo saltado", 22.0)
    arroz  = Producto("Arroz con pollo", 18.0)
    chicha = RefrescoNatural("Chicha morada", 6.0)
    inca   = Gaseosa("Inca Kola", 5.0)
    agua   = BebidaEnvasada("Agua mineral", 4.0)

    r.registrar_producto(lomo)
    r.registrar_producto(arroz)
    r.registrar_producto(chicha)
    r.registrar_producto(inca)
    r.registrar_producto(agua)

    # --- Combo ---
    combo = Combo("Combo Criollo", descuento=15)
    combo.agregar_producto_combo(lomo, 1)
    combo.agregar_producto_combo(chicha, 1)
    r.registrar_producto(combo)

    r.mostrar_menu()

    # --- Clientes ---
    c1 = Cliente("Ana Torres", "987654321")
    c2 = Cliente("Luis Pérez", "12345")   # inválido a propósito
    r.registrar_cliente(c1)
    r.registrar_cliente(c2)

    # --- Pedido Delivery ---
    pago1 = PagoTarjeta(comision=5)
    pd = PedidoDelivery(0, c1, pago1, zona="B",
                        direccion="Av. Lima 123", pedido_minimo=30)
    pd.asignar_producto(lomo, 2)
    pd.asignar_producto(chicha, 1)
    r.registrar_pedido(pd)
    pd.cambiar_estado("EN_PREPARACION")
    pd.pagar()

    # --- Pedido Local ---
    pago2 = PagoEfectivo(monto_recibido=50)
    pl = PedidoLocal(0, c1, pago2, numero_mesa=4)
    pl.asignar_producto(combo, 1)
    pl.asignar_producto(inca, 2)
    r.registrar_pedido(pl)
    pl.pagar()

    # --- Pedido Para Llevar ---
    pago3 = PagoQr("TX-998877")
    pv = PedidoParaLlevar(0, c1, pago3, costo_envase=1.5)
    pv.asignar_producto(arroz, 1)
    pv.asignar_producto(agua, 2)
    r.registrar_pedido(pv)
    pv.pagar()

    # --- Reporte ---
    r.generar_reporte()