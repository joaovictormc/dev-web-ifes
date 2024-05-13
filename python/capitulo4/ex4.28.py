from datetime import datetime, timedelta

instante_atual = datetime.now()

instante_futuro = instante_atual + timedelta(days=10)

if instante_atual < instante_futuro:
    print("O instante atual é anterior ao instante futuro.")
else:
    print("O instante atual não é anterior ao instante futuro.")
