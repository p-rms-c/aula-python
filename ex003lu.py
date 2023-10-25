def confere_palindromo():
    frase = input('Digite o que deseja saber se é um palíndromo: ')
    c = ''

    for i in range(len(frase)):
        c = c + frase[len(frase) - 1 - i]
    
    print(c + ': ')
    
    if frase == c:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')

confere_palindromo()