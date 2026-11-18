# Proyecto Integrador POO – Sistema de Pedidos Sabor Valluno

<p align="center">
  <b>Asignatura:</b> Programación Orientada a Objetos<br>
  <b>Estudiante:</b> @Roy<br>
  <b>Fecha:</b> 3 de Noviembre, 2026<br>
  <b>Tecnología:</b> Python 3 (Aplicación de consola, biblioteca estándar)
</p>

---

## 📋 Descripción General

El **Sistema de Pedidos Sabor Valluno** es una aplicación de consola desarrollada en Python 3 que modela y gestiona la operativa de un restaurante de comida típica cochabambina. El proyecto aplica rigurosamente los **cuatro pilares de la Programación Orientada a Objetos (POO)**: Encapsulación, Herencia, Polimorfismo y Abstracción, utilizando exclusivamente la biblioteca estándar de Python (incluyendo el módulo `abc`).

### 🎯 Competencias Evidenciadas
- **Modelado UML:** Estructura coherente mediante diagramas de clases (v1 y v2) sincronizados con el código fuente.
- **Encapsulación y Validación:** Protección del estado de los objetos mediante propiedades y validaciones estrictas de reglas de negocio.
- **Herencia y Polimorfismo:** Especialización de comportamiento sin recurrir a condicionales por tipo (`isinstance`, `type()`, o `if/elif`), incorporando un objeto compuesto (`Combo`) capaz de contener otros combos.
- **Abstracción:** Definición de contratos claros mediante clases abstractas (`ABC` y `@abstractmethod`).

---

## 🏛️ Estructura del Repositorio

```text
SaborValluno/
│
├── modelo/
│   ├── __init__.py
│   ├── productos.py     # Jerarquía de Productos (Platos, Bebidas, Combos)
│   ├── pedidos.py       # Jerarquía de Pedidos (Local, Para Llevar, Delivery) y Estados
│   ├── pagos.py         # Jerarquía de Métodos de Pago (Efectivo, QR, Tarjeta)
│   └── clientes.py      # Gestión y validación de Clientes
│
├── docs/
│   ├── diagrama_v1.png  # Diagrama inicial hecho en aula
│   ├── diagrama_v2.png  # Diagrama final actualizado
│   ├── bitacora_ia.md   # Registro de uso de inteligencia artificial
│   └── acta_consultas.md# Registro de consultas al cliente (docente)
│
├── restaurante.py       # Clase gestora principal (menú, clientes, pedidos)
├── main.py              # Interfaz de usuario por consola
├── pruebas.py           # Casos de prueba automatizados con assert
└── README.md            # Documentación del proyecto
```

---

## 🚀 Guía de Instalación y Ejecución

### Requisitos Previos
- Tener instalado **Python 3.8** o superior.
- Tener instalado **Git**.

### Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/sabor-valluno.git
cd sabor-valluno
```

### Ejecutar la Aplicación
Para iniciar el menú interactivo de la consola:
```bash
python main.py
```

### Ejecutar las Pruebas Unitarias
Para verificar el correcto funcionamiento del sistema y las reglas de negocio (mínimo 8 casos de prueba con `assert`):
```bash
python pruebas.py
```

---

## ⚙️ Reglas de Negocio y Variante Asignada

El sistema implementa las reglas de negocio estipuladas para el restaurante, adaptadas a la variante de reglas asignada por sorteo:

1. **Productos:** Menú compuesto por platos típicos (Silpancho, Pique Macho, Chicharrón, Sopa de Maní), bebidas (vasos y jarras) y combos.
2. **Combos:** Compuestos por 2 o más productos con un porcentaje de descuento predefinido y restricciones de disponibilidad en función de sus componentes.
3. **Cargos y Tipos de Pedido:**
   - **Local:** Requiere mesa (1-15) sin duplicidad de pedidos activos. Sin recargos adicionales.
   - **Para Llevar:** Cargo adicional por envase por cada plato (incluyendo los internos en combos).
   - **Delivery:** Cálculo de envío por zona con umbrales de envío gratuito y pedido mínimo.
4. **Estados del Pedido:** Flujo controlado (`REGISTRADO` $\rightarrow$ `EN_PREPARACION` $\rightarrow$ `LISTO` $\rightarrow$ `ENTREGADO`). Cancelaciones y modificaciones permitidas exclusivamente en estado `REGISTRADO`.
5. **Pagos:** Procesamiento seguro a través de Efectivo, QR y Tarjeta con validación de montos, códigos de transacción y comisiones correspondientes.

---

## 🛠️ Buenas Prácticas y Control de Versiones

- **Commits Frecuentes:** Historial de desarrollo distribuido a lo largo de las semanas de entrega.
- **Trazabilidad:** Inclusión de bitácora de IA (`docs/bitacora_ia.md`) y acta de consultas formales con el docente (`docs/acta_consultas.md`).