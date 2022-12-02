class Main:
    pass

from Cliente import Cliente
from Conta import Conta

cliente_1 = Cliente("Gabriel", "21", "1194444-2222")
conta_1 = Conta(cliente_1.get_nome(), 0000, 35)

conta_1.saque(5)
conta_1.saque(1)
conta_1.deposito(500)
conta_1.extrato()

#print("Cliente:", cliente_1.nome, "\nIdade:", cliente_1.idade, "\nTelefone:", cliente_1.tel)
#print("Titular:",conta_1.titular, "\nID:", conta_1.id ,"\nSaldo:", conta_1.saldo)