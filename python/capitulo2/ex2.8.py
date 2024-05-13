data_texto = input("Digite uma data no formato dd/mm/aaaa: ")


if len(data_texto) == 10 and data_texto[2] == '/' and data_texto[5] == '/':
    dia = int(data_texto[0:2])
    mes = int(data_texto[3:5])
    ano = int(data_texto[6:10])

    if 1 <= dia <= 31 and 1 <= mes <= 12 and 1 <= ano <= 9999:
        print("A data digitada está no formato correto.")
    else:
        print("A data digitada não está no formato correto.")
else:
    print("A data digitada não está no formato correto.")
