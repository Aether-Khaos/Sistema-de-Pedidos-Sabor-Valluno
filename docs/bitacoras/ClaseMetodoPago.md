### se hizo uso del readme Reglas junto al como se encuentra el diagrama UML 
- se tuvo que aclarar que debe revisar la estructura de archivos en el readme de la clase MetodoPago
Jerarquía de Métodos de Pago
MetodoPago (Clase Base / Superclase)

    Métodos (Funciones):

        + procesar_pago

    Herencia: De esta clase heredan PagoEfectivo, PagoQr y PagoTarjeta.

PagoEfectivo (Hereda de MetodoPago)

    Atributos / Métodos:

        monto_recibido

        + procesar_pago

        + redondo_total

        + calcular_cambio

PagoQr (Hereda de MetodoPago)

    Atributos / Métodos:

        codigo_transaccion

        + procesar_pago

        + validar_codigo

PagoTarjeta (Hereda de MetodoPago)

    Atributos / Métodos:

        comision

        + procesar_pago

        + calcular_comision

