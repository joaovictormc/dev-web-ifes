distancia = float(input("Digite a distância percorrida (em metros): "))
tempo = float(input("Digite o tempo gasto (em segundos): "))
aceleracao = float(input("Digite a aceleração (em metros por segundo ao quadrado): "))

velocidade_inicial = (distancia - (0.5 * aceleracao * tempo**2)) / tempo

velocidade_final = velocidade_inicial + aceleracao * tempo

print(f"A velocidade inicial é: {velocidade_inicial:.2f} m/s")
print(f"A velocidade final é: {velocidade_final:.2f} m/s")
