numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

def eh_par(num):
    return num % 2 == 0

numeros_pares = list(filter(eh_par, numeros))

print("Números pares:", numeros_pares)
