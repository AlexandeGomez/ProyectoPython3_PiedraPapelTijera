
def iguales(respuestas, opcion):
    if(respuestas[0]==opcion[0] and respuestas[1]==opcion[1]):
        return True
    return False

def evalua_ganador(respuestas):
    if(iguales(respuestas, ['piedra','piedra'])):
        return ['empate','empate']
    elif(iguales(respuestas, ['piedra','papel'])):
        return ['perdiste', 'ganaste']
    elif(iguales(respuestas, ['piedra','tijera'])):
        return ['ganaste', 'perdiste']

    elif(iguales(respuestas, ['papel','piedra'])):
        return ['ganaste', 'perdiste']
    elif(iguales(respuestas, ['papel','papel'])):
        return ['empate','empate']
    elif(iguales(respuestas, ['papel','tijera'])):
        return ['perdiste', 'ganaste']

    elif(iguales(respuestas, ['tijera','piedra'])):
        return ['perdiste', 'ganaste']
    elif(iguales(respuestas, ['tijera','papel'])):
        return ['ganaste', 'perdiste']
    elif(iguales(respuestas, ['tijera','tijera'])):
        return  ['empate','empate']