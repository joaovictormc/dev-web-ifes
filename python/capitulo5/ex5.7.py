def contagemRegressiva(n):
    if n < 0:
        return
    print(n)
    if n == 0:
        print("Contagem regressiva finalizada!")
    else:
        contagemRegressiva(n-1)

contagemRegressiva(5)
