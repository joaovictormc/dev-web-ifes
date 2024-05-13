def transformarLista(lista, funcao):
    return [funcao(elemento) for elemento in lista]

def porExtenso(numero):
    nomes = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    return nomes[numero] if 0 <= numero <= 9 else None

numeros = [1, 2, 3, 4, 5]

lista_transformada = transformarLista(numeros, porExtenso)

print(lista_transformada)
