def importar_modulo(nome_modulo):
    try:
        modulo = __import__(nome_modulo)
        print("O módulo '{}' foi importado com sucesso.".format(nome_modulo))
    except ModuleNotFoundError:
        print("O módulo '{}' não foi encontrado.".format(nome_modulo))
    finally:
        print("Operação finalizada.")

importar_modulo("numpy")
importar_modulo("módulo_inexistente")
