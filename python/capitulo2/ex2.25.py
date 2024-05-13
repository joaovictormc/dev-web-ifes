a = float(input("Digite o primeiro número (a): "))
b = float(input("Digite o segundo número (b): "))
operacao = input("Digite a operação aritmética (+, -, * ou /): ")

match operacao:
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*':
        resultado = a * b
    case '/':
        if b != 0:
            resultado = a / b
        else:
            print("Erro: Divisão por zero não é permitida.")
            exit()
    case _:
        print("Operação inválida.")
        exit()

print(f"O resultado de {a} {operacao} {b} é: {resultado}")
