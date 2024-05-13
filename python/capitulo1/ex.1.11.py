import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2
comprimento = 2 * math.pi * raio

print(f"A área do círculo é: {area:.2f}")
print(f"O comprimento do círculo é: {comprimento:.2f}")