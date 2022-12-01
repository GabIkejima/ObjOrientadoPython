class Cliente:
    def __init__(self, nome, idade, tel):

        self.nome = nome
        self.idade = idade
        self._tel = tel

    #Método GET
    def get_tel(self):
        return self._tel     

    #Método SET
    def set_tel(self, tel):
        self._tel = tel