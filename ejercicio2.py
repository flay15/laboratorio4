class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}.")

# Ejemplo de uso
cuenta = CuentaBancaria("Ana", 500)
cuenta.mostrar_saldo()  # Saldo actual: 500.
cuenta.depositar(200)
cuenta.mostrar_saldo()  # Saldo actual: 700.
cuenta.retirar(1000)  # Saldo insuficiente.
