import random

participantes = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana"]

sorteio = {}

while len(sorteio) < len(participantes):
    for nome in participantes:
        possiveis_escolhas = [p for p in participantes if p != nome and p not in sorteio.values()]
        if possiveis_escolhas:
            sorteio[nome] = random.choice(possiveis_escolhas)
        else:
            sorteio = {}
            break

for pessoa, amigo_secreto in sorteio.items():
    print(f"{pessoa} tirou {amigo_secreto}")
