import os

def renomear_arquivo(nome_arquivo):
    nome, extensao = os.path.splitext(nome_arquivo)

    novo_nome = nome + "_renomeado" + extensao

    os.rename(nome_arquivo, novo_nome)

    return novo_nome

nome_arquivo = input("Digite o nome do arquivo a ser renomeado: ")

if os.path.exists(nome_arquivo):
    novo_nome_arquivo = renomear_arquivo(nome_arquivo)
    print("O arquivo foi renomeado para:", novo_nome_arquivo)
else:
    print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
