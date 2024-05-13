numero = int(input("Digite um número para verificar se é primo: "))

eh_primo = True

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            eh_primo = False
            break
else:
    eh_primo = False

if eh_primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
