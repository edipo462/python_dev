

class Conta:
     #Classe representa o Objeto Conta

    def __init__(self, numero, titular, saldo, limite):
         # Selfie é a função construtura de uma classe em python
        print("Construindo objeto...")
        self.numero = numero                            # as entradas da classe sao os atributos da classes
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

# as funções da classe sao os metodos
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        valor_total = self.saldo + self.limite
        if valor > valor_total:

            print ("Saldo insuficiente")
        else:
            self.saldo -= valor