def calcular_fatorial(numero):
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")
