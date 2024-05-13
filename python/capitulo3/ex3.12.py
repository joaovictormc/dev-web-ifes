def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

soma_primos = sum(num for num in range(1, 101) if eh_primo(num))

print(f"A soma de todos os números primos de 1 a 100 é: {soma_primos}")
