def decifrar_mensagem(mensagem_codificada):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    decodificador = {alfabeto[i]: alfabeto[i - 1] for i in range(len(alfabeto))}

    
    def decifrar_letra(letra):
        if letra.isalpha():  
            return decodificador[letra]
        return letra

    
    if not mensagem_codificada:
        return ''

    
    return decifrar_letra(mensagem_codificada[0].lower()) + decifrar_mensagem(mensagem_codificada[1:])

mensagem_codificada = "b cdefghijklmnopqrstuvwxyz a"
mensagem_decifrada = decifrar_mensagem(mensagem_codificada)
print(mensagem_decifrada)
