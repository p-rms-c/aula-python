import re

def substitui_letra():
    palavra_frase = input('Digite um texto: ')
    l1 = input('Digite qual letra vai ser substituída: ')
    l2 = input('Digite a letra que vai substituir: ')

    nova_frase = re.sub(l1, l2, palavra_frase)
    print(nova_frase)

substitui_letra()