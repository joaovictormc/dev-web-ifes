class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)


class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Endereço:", self.endereco)

cliente1 = Cliente("João", 30, "Rua XYZ, 123")

cliente1.mostrar_dados()
