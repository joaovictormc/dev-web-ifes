def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


n = int(input("Digite o valor de n: "))


for i in range(1, n + 1):
    print(f"O fatorial de {i} é {fatorial(i)}")
