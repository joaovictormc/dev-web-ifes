nome = input("Digite seu nome: ")
salario_bruto = float(input("Digite o valor do seu salário bruto: R$ "))
valor_imposto = float(input("Digite o valor do imposto: R$ "))

salario_liquido = salario_bruto - valor_imposto

print(f"{nome} tem um salário líquido de R$ {salario_liquido:,.2f}.")