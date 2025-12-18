### Descripción del Caso
Este programa es una simulación de un sistema de ventas del mundo real. He modelado el proceso en el que un cliente interactúa con productos de una tienda. El desarrollo se basa en la Programación Orientada a Objetos (POO) para organizar la lógica de la siguiente manera:

*   **Clase `Producto`**: Actúa como el molde para cualquier artículo de la tienda. Define atributos esenciales como el nombre y el precio, y permite obtener una ficha técnica del artículo.

*   **Clase `CarritoDeCompras`**: Representa el contenedor de la compra del usuario. Su función principal es gestionar una lista de objetos, permitiendo añadir múltiples unidades y realizar el cálculo automático del presupuesto total.

# Definimos la clase 'Producto' para representar los artículos que la tienda vende.
class Producto:
    def __init__(self, nombre, precio):
        # Constructor de la clase Producto.
        # Inicializa un producto con un nombre y un precio.
        self.nombre = nombre
        self.precio = precio

    def obtener_info(self):
        # Método para obtener la información del producto.
        # Devuelve una cadena con el nombre y el precio del producto.
        return f"{self.nombre} (Precio: ${self.precio:.2f})\n"

# Definimos la clase 'CarritoDeCompras' para gestionar los productos que un cliente desea comprar.
class CarritoDeCompras:
    def __init__(self):
        # Constructor de la clase CarritoDeCompras.
        # Inicializa un carrito vacío como una lista de productos.
        self.productos = []

    def agregar_producto(self, producto, cantidad=1):
        # Método para añadir un producto al carrito.
        # Añade el producto la cantidad de veces especificada.
        for _ in range(cantidad):
            self.productos.append(producto)
        print(f"'{producto.nombre}' ha sido añadido al carrito. Cantidad: {cantidad}")

    def calcular_total(self):
        # Método para calcular el precio total de todos los productos en el carrito.
        total = sum(producto.precio for producto in self.productos)
        return total

    def mostrar_carrito(self):
        # Método para mostrar todos los productos actualmente en el carrito y su total.
        if not self.productos:
            print("El carrito de compras está vacío.")
            return

        print("\n--- Contenido del Carrito de Compras ---")
        # Contar la ocurrencia de cada producto para mostrarlo de forma más limpia
        productos_contados = {}
        for p in self.productos:
            productos_contados[p.nombre] = productos_contados.get(p.nombre, {'producto': p, 'cantidad': 0})
            productos_contados[p.nombre]['cantidad'] += 1

        for item_data in productos_contados.values():
            producto = item_data['producto']
            cantidad = item_data['cantidad']
            print(f"  - {cantidad} x {producto.nombre} (c/u: ${producto.precio:.2f})")

        print(f"----------------------------------------")
        print(f"Total a pagar: ${self.calcular_total():.2f}")
        print(f"----------------------------------------")

# --- Simulación de la Tienda y el Carrito de Compras ---

print("¡Bienvenido a nuestra tienda virtual!")

# Creamos instancias de la clase Producto para los artículos disponibles.
camiseta = Producto("Camiseta", 10.00)
pantalon = Producto("Pantalón", 20.00)

# Mostramos la información de los productos individuales.
print("\n--- Productos Disponibles ---")
print(camiseta.obtener_info())
print(pantalon.obtener_info())

# Creamos una instancia de la clase CarritoDeCompras para un cliente.
mi_carrito = CarritoDeCompras()

# El cliente añade productos a su carrito.
print("\n--- Añadiendo productos al carrito ---")
mi_carrito.agregar_producto(camiseta, 2) # Añadir 2 camisetas
mi_carrito.agregar_producto(pantalon, 1) # Añadir 1 pantalón

# El cliente decide ver el contenido de su carrito y el total.
mi_carrito.mostrar_carrito()

print("\n¡Gracias por tu compra!")
