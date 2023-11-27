def criptografar(frase):
    mensagem = ''

    for i in frase:
        mensagem = mensagem + chr(ord(i) + 5)
    return mensagem

def descriptografar(mensagem):
    frase = ''

    for i in mensagem:
        frase = frase + chr(ord(i) - 5)
    return frase

resposta_usuario = 1

while resposta_usuario == 1:
    user_input = (input('Digite o que deseja criptografar: '))
    palavra_criptografada = criptografar(user_input)
    print(palavra_criptografada)

    resposta_usuario = (int(input('Deseja criptografar algo mais? \n Sim - 1 \n Não - 2 \n')))

print('Tchauzinho!')
