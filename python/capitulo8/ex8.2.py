class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

meu_retangulo = Retangulo(5, 3)

area_retangulo = meu_retangulo.area()

print("A área do retângulo é:", area_retangulo)
