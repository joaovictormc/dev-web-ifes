class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade em estoque:", self.quantidade_estoque)


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, quantidade_estoque, imposto):
        super().__init__(nome, preco, quantidade_estoque)
        self.imposto = imposto

    def preco_final(self):
        return self.preco * (1 + self.imposto / 100)


produto_importado = ProdutoImportado("Notebook", 2500, 5, 10)

print("Dados do produto importado:")
produto_importado.mostrar_dados()

print("Preço final do produto com imposto:", produto_importado.preco_final())
