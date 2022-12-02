class Cliente:
    def __init__(self, nome, idade, tel):

        self._nome = nome
        self.idade = idade
        self.tel = tel


    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome