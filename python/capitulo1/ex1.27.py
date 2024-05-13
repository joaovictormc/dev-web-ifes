valor_inicial = float(input("Digite o valor inicial do investimento: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em porcentagem): ")) / 100
num_meses = int(input("Digite o número de meses que o valor ficou investido: "))

valor_final = valor_inicial * ((1 + taxa_juros) ** num_meses)

print(f"O valor final do investimento após {num_meses} meses é: R$ {valor_final:,.2f}")
