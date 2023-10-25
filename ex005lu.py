nome = input('Digite seu nome: ')
sexo = input('Sexo: ')
idade = int(input('Idade: '))


if sexo == 'masculino' and idade < 25:
    print(nome)
    print('ACEITO')
else:
    print('NÃO ACEITA')