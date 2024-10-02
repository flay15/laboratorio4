class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"El producto {producto} no está en el carrito.")

    def mostrar_productos(self):
        if self.productos:
            print("Productos en el carrito:", self.productos)
        else:
            print("El carrito está vacío.")

# Ejemplo de uso
carrito = CarritoDeCompras()
carrito.agregar_producto("Manzanas")
carrito.mostrar_productos()  # Productos en el carrito: ['Manzanas']
carrito.eliminar_producto("Manzanas")
carrito.mostrar_productos()  # El carrito está vacío.
