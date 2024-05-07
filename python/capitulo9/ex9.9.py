def read_file(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
    finally:
        arquivo.close()

read_file("exemplo.txt")
