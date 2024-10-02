class Cafetera:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.nivel_actual = 0

    def llenar(self):
        self.nivel_actual = self.capacidad
        print("La cafetera está llena.")

    def servir(self):
        if self.nivel_actual > 0:
            self.nivel_actual -= 1
            print("Se ha servido una taza de café.")
        else:
            print("No queda café para servir.")

    def mostrar_nivel(self):
        print(f"Quedan {self.nivel_actual} tazas de café disponibles.")

# Ejemplo de uso
cafetera = Cafetera(5)
cafetera.mostrar_nivel()  # Quedan 0 tazas de café disponibles.
cafetera.llenar()
cafetera.mostrar_nivel()  # Quedan 5 tazas de café disponibles.
cafetera.servir()  # Se ha servido una taza de café.
cafetera.mostrar_nivel()  # Quedan 4 tazas de café disponibles.
