
cor_semaforo = input("Digite a cor atual do semáforo (verde, amarelo ou vermelho): ").lower()

match cor_semaforo:
    case 'verde':
        print("Prossiga")
    case 'amarelo':
        print("Prepare-se para parar")
    case 'vermelho':
        print("Pare")
    case _:
        print("Cor inválida")
