class Conta:
    def __init__(self, titular, id, saldo):
        self.titular = titular
        self.id = id
        self.saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            if valor == 1:
                print("Saque de 1 real realizado com sucesso")
            else:
                print("Saque de", valor, "reais realizado com sucesso")
        else:
            print("Saldo insuficiente")
    
    def deposito(self, valor):
        self.saldo += valor
        if valor == 1:
            print("Depósito de 1 real realizado com sucesso")
        else:
            print("Depósito de", valor, "reais realizado com sucesso")

    def extrato(self):
        print("Cliente: ",self.titular,"\nSaldo atual: ", self.saldo)