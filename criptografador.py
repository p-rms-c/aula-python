def cripto(frase):
    tradutor = ''
    for letra in frase:
        if letra in 'aA':
            tradutor = tradutor + '@'
        elif letra in 'eE':
            tradutor = tradutor + '3'
        elif letra in 'iI':
            tradutor = tradutor + 'l'
        elif letra in 'oO':
            tradutor = tradutor + '0'
        elif letra in 'uU':
            tradutor = tradutor + 'v'
        elif letra in 'bB':
            tradutor = tradutor + '6'
        elif letra in 'cC':
            tradutor = tradutor + '('
        else:
            tradutor = tradutor + letra
    return tradutor

print(cripto(input('Digite sua frase: ')))