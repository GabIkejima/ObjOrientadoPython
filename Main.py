class Main:
    pass

from Cliente import Cliente
from Conta import Conta


cliente_1 = Cliente("Gabriel", "21", "1194444-2222")
conta_1 = Conta(cliente_1.nome, 0000, 35)

#print("Cliente:", cliente_1.nome, "\nIdade:", cliente_1.idade, "\nTelefone:", cliente_1.get_tel())
print("Titular:",conta_1.titular, "\nID:", conta_1.id ,"\nSaldo:", conta_1.get_saldo())
print(conta_1.set_saldo(-100))

