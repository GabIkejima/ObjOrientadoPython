class Conta:
    def __init__(self, titular, id, saldo):
        self.titular = titular
        self.id = id
        self._saldo = saldo

    #Método GET
    def get_saldo(self):
        return self._saldo
    
    #Método SET
    def set_saldo(self, saldo):
        if saldo < 0:
            return ("O valor de saldo não pode ser negativo")
        else:
            self._saldo = saldo

