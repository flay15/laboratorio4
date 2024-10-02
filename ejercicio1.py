class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.despierto = True

    def dormir(self):
        self.despierto = False

    def despertar(self):
        self.despierto = True

    def mostrar_estado(self):
        estado = "despierto" if self.despierto else "durmiendo"
        print(f"{self.nombre} está {estado}.")

# Ejemplo de uso
persona = Persona("Carlos", 30)
persona.mostrar_estado()  # Carlos está despierto.
persona.dormir()
persona.mostrar_estado()  # Carlos está durmiendo.
