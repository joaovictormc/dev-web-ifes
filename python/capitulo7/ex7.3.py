def inverter_linha(linha):
    return linha[::-1]

def inverter_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:     linhas = arquivo_entrada.readlines()

    linhas_invertidas = [inverter_linha(linha) for linha in linhas]

    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.writelines(linhas_invertidas)

arquivo_entrada = 'entrada.txt'
arquivo_saida = 'saida.txt'

inverter_arquivo(arquivo_entrada, arquivo_saida)

print("Conteúdo invertido do arquivo '{}' foi salvo em '{}'.".format(arquivo_entrada, arquivo_saida))
