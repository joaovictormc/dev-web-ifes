import re

cpf = input("Digite um CPF no formato DDD.DDD.DDD-DD: ")

padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

if re.match(padrao_cpf, cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF não está no formato correto.")
