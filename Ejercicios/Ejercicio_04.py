
class CuentaBancaria:
    def __init__(self, saldo_inicial = 0):
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if monto > self.saldo:
            print("No hay suficiente dinero para realizar la operación")
        else:
            self.saldo -= monto
    
    def mostrar_saldo(self):
        print("Saldo actual: ", self.saldo)


cuenta1 = CuentaBancaria(1000)

cuenta1.mostrar_saldo()
cuenta1.depositar(500)
cuenta1.mostrar_saldo()
cuenta1.retirar(200)
cuenta1.mostrar_saldo()
cuenta1.retirar(2000)

