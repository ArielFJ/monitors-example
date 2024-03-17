import threading

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.mutex = threading.Lock()  # Mutex para garantizar exclusión mutua

    def depositar(self, cantidad):
        with self.mutex:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        with self.mutex:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar el retiro.")

    def consultar_saldo(self):
        with self.mutex:
            return self.saldo

# Función para simular transacciones en la cuenta bancaria
def realizar_transacciones(cuenta):
    for _ in range(3):
        cuenta.depositar(100)
        cuenta.retirar(50)

if __name__ == "__main__":
    cuenta = CuentaBancaria()

    # Crear varios hilos para simular transacciones concurrentes
    hilos = []
    for _ in range(2):
        hilo = threading.Thread(target=realizar_transacciones, args=(cuenta,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Mostrar saldo final
    print(f"Saldo final: {cuenta.consultar_saldo()}")
