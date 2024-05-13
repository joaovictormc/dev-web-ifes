cpf = input("Digite um número de CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    print("O CPF digitado é válido.")
else:
    print("O CPF digitado é inválido.")
