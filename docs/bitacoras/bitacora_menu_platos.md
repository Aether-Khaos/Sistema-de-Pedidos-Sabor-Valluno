# Bitácora – Menú y Platos (Jerarquía)

## Jerarquía implementada
Plato (ABC)
├── Producto
├── RefrescoNatural
├── BebidaEnvasada
│ └── Gaseosa
└── Combo ──◊ ProductoCombo ──→ Plato


## Clases
- **Plato** (abstracta): `nombre`, `precio_base`, `calcular_precio()`
  (abstracto), `esta_disponible()`, `costar_platos()`.
- **Producto**: precio = `precio_base`.
- **RefrescoNatural**: precio = `precio_base × 1.10`.
- **BebidaEnvasada**: precio = `precio_base`.
- **Gaseosa** (hereda de BebidaEnvasada): precio = `precio_base × 1.05`.
- **Combo**: `descuento`, `producto_combo` (lista de `ProductoCombo`),
  `agregar_producto_combo()`; precio = `suma(ProductoCombo.subtotal) × (1 − descuento/100)`.
- **ProductoCombo**: `producto`, `cantidad`, `calcular_subtotal()`,
  `esta_disponible()`, `costar_platos()`.

## Decisiones
| Decisión | Motivo |
|---|---|
| `Plato` como `ABC` con `calcular_precio` abstracto | Fuerza a cada subclase a definir su precio. |
| `Gaseosa` hereda de `BebidaEnvasada` | Modela la relación del diagrama. |
| `Combo.esta_disponible()` recorre sus `ProductoCombo` | Coherencia: si un ítem no está disponible, el combo tampoco. |
| `costar_platos()` se mantiene en toda la jerarquía | Cumple el contrato del modelo. |