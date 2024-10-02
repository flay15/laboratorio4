class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro '{libro}' ha sido agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"El libro '{libro}' ha sido eliminado.")
        else:
            print(f"El libro '{libro}' no está en la biblioteca.")

    def mostrar_libros(self):
        if self.libros:
            print("Libros en la biblioteca:", self.libros)
        else:
            print("No hay libros en la biblioteca.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("El Quijote")
biblioteca.mostrar_libros()  # Libros en la biblioteca: ['El Quijote']
biblioteca.eliminar_libro("El Quijote")
biblioteca.mostrar_libros()  # No hay libros en la biblioteca.
