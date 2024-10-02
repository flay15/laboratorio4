class Temporizador:
    def __init__(self, tiempo_restante):
        self.tiempo_restante = tiempo_restante

    def iniciar(self):
        print(f"Temporizador iniciado. Tiempo restante: {self.tiempo_restante} segundos.")

    def pausar(self):
        print(f"Temporizador pausado. Tiempo restante: {self.tiempo_restante} segundos.")

    def mostrar_tiempo(self):
        print(f"Tiempo restante: {self.tiempo_restante} segundos.")

# Ejemplo de uso
temporizador = Temporizador(60)
temporizador.iniciar()  # Temporizador iniciado. Tiempo restante: 60 segundos.
temporizador.mostrar_tiempo()
temporizador.pausar()  # Temporizador pausado. Tiempo restante: 60 segundos.
