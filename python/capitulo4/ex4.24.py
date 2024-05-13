from datetime import datetime

oito_horas_manha = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

tres_horas_tarde = datetime.now().replace(hour=15, minute=0, second=0, microsecond=0)

diferenca = tres_horas_tarde - oito_horas_manha

diferenca_em_horas = diferenca.total_seconds() / 3600

print(f"A diferença entre os dois horários é de {diferenca_em_horas} horas.")
