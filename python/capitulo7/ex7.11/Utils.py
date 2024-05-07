from datetime import datetime

def exibir_data_hora():
    agora = datetime.now()
    print("Data e Hora Atuais:", agora.strftime("%d/%m/%Y %H:%M:%S"))
