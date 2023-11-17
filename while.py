# Joguinho de erros e acertos
print('Dica: mora nesta casa \n p.s.: limite de 3 tentativas')
palavra_secreta = 'bianca'
palavra_escolhida = ''
contador = 0
limite = 3
sair = False


while palavra_escolhida != palavra_secreta and not (sair):
    if  contador < limite:
        palavra_escolhida = input('Tente acertar a palavra secreta: ')
        contador += 1
    else:
        sair = True

if sair == True:
    print('Você perdeu!!!')
else:
    print('Parabéns, você venceu!!!')