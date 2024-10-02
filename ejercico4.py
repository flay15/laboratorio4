class Termostato:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def aumentar(self, grados):
        self.temperatura += grados

    def disminuir(self, grados):
        self.temperatura -= grados

    def mostrar_temperatura(self):
        print(f"La temperatura actual es: {self.temperatura}°C.")

# Ejemplo de uso
termostato = Termostato(25)
termostato.mostrar_temperatura()  # La temperatura actual es 25°C.
termostato.aumentar(5)
termostato.mostrar_temperatura()  # La temperatura actual es 30°C.
