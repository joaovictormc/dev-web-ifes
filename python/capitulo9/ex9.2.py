def calcular_media(lista_numeros):
    try:
        if not lista_numeros:
            raise ValueError("A lista está vazia. Não é possível calcular a média.")
        
        total = sum(lista_numeros)
        media = total / len(lista_numeros)
        return media
    except TypeError:
        raise ValueError("A lista contém valores não numéricos.")

try:
    numeros = [10, 20, 30, 40, 50]
    media = calcular_media(numeros)
    print("A média dos números é:", media)

    lista_vazia = []
    media_vazia = calcular_media(lista_vazia)
    print("A média da lista vazia é:", media_vazia)
    
    lista_com_string = [10, 20, '30', 40, 50]
    media_string = calcular_media(lista_com_string)
    print("A média da lista com string é:", media_string)
except ValueError as ve:
    print(ve)
