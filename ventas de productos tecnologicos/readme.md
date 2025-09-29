# Proyecto Tienda MVC con Strategy (Python)

Este proyecto es un ejemplo sencillo de cómo aplicar la **arquitectura MVC (Modelo - Vista - Controlador)** junto con el **patrón de diseño Strategy** en Python.

La aplicación funciona en **consola** y permite:
- Ver una lista de productos con precios reales aproximados.
- Seleccionar un producto por su ID.
- Aplicar diferentes tipos de descuento mediante el patrón Strategy:
  - **Sin descuento**
  - **10% de descuento**
  - **Descuento fijo de $500**

---

##  Cómo ejecutar

1. Clonar el proyecto o copiar los archivos en una carpeta.
2. Abrir una terminal en la carpeta raíz.
3. Ejecutar:

```bash
python main.py

Como funciona 
🔹 main.py punto de entrada de la aplicación,contiene el menú interactivo para el usuario.
Permite listar productos, elegir un producto y aplicar un descuento.

models/product.py define la clase Producto, que representa un producto con: id,name,precio

repositories/product_repository.py simula una base de datos en memoria con productos reales y precios.

Métodos:
list_all(): devuelve todos los productos.
get_by_id(id): devuelve un producto por ID.

controllers/product_controller.py contiene la lógica de negocio,usa el repositorio para obtener productos.
Aplica los Strategy de descuento mediante el DiscountContext.
Envía los datos a la Vista para mostrarlos.

views/product_view.py encargada de mostrar la información en consola.

Métodos:
show_products(): imprime lista de productos.
show_product(): imprime detalle de un producto con el precio final.

services/strategies.py define el patrón Strategy:
DiscountStrategy: interfaz base (abstracta).
NoDiscount: no aplica descuento.
PercentageDiscount: aplica un porcentaje de descuento (ej: 10%).
FixedDiscount: aplica un descuento fijo en pesos (ej: $500).

services/discount_context.py
Clase DiscountContext que utiliza una estrategia de descuento, permite cambiar la estrategia en tiempo de ejecución con set_strategy().
Aplica el descuento con apply_discount().
