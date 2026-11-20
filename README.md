# Proyecto Integrador POO – Sistema de Pedidos Sabor Valluno
### Integrantes
- Rosales Quispe Alex
- Callisaya Huanca Isai
- Jhoel Cortez Jimenez 


## Reglas de Negocio y Variante Asignada

El sistema implementa las reglas de negocio estipuladas para el restaurante, adaptadas a la variante de reglas asignada por sorteo:

1. **Productos:** Menú compuesto por platos típicos (Silpancho, Pique Macho, Chicharrón, Sopa de Maní), bebidas (vasos y jarras) y combos.
2. **Combos:** Compuestos por 2 o más productos con un porcentaje de descuento predefinido y restricciones de disponibilidad en función de sus componentes.
3. **Cargos y Tipos de Pedido:**
   - **Local:** Requiere mesa (1-15) sin duplicidad de pedidos activos. Sin recargos adicionales.
   - **Para Llevar:** Cargo adicional por envase por cada plato (incluyendo los internos en combos).
   - **Delivery:** Cálculo de envío por zona con umbrales de envío gratuito y pedido mínimo.
4. **Estados del Pedido:** Flujo controlado (`REGISTRADO` $\rightarrow$ `EN_PREPARACION` $\rightarrow$ `LISTO` $\rightarrow$ `ENTREGADO`). Cancelaciones y modificaciones permitidas exclusivamente en estado `REGISTRADO`.
5. **Pagos:** Procesamiento seguro a través de Efectivo, QR y Tarjeta con validación de montos, códigos de transacción y comisiones correspondientes.
