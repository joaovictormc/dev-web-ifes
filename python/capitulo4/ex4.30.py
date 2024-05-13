from datetime import datetime

instante_atual = datetime.now()

numero_semana = instante_atual.isocalendar()[1]

print(f"O número da semana do ano é: {numero_semana}")
