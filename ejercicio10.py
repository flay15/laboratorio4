class Album:
    def __init__(self):
        self.fotos = []

    def agregar_foto(self, foto):
        self.fotos.append(foto)
        print(f"Foto '{foto}' agregada al álbum.")

    def eliminar_foto(self, foto):
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"Foto '{foto}' eliminada del álbum.")
        else:
            print(f"La foto '{foto}' no está en el álbum.")

    def mostrar_fotos(self):
        if self.fotos:
            print("Fotos en el álbum:", self.fotos)
        else:
            print("El álbum está vacío.")

# Ejemplo de uso
album = Album()
album.agregar_foto("Foto1.jpg")
album.agregar_foto("Foto2.jpg")
album.mostrar_fotos()  # Fotos en el álbum: ['Foto1.jpg', 'Foto2.jpg']
album.eliminar_foto("Foto1.jpg")
album.mostrar_fotos()  # Fotos en el álbum: ['Foto2.jpg']
