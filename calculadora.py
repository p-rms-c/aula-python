num1 = float(input('Digite um número: '))
op = input('Digite o operador: ')
num2 = float(input('Digite outro número: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op =='*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('Operador inválido ou não definido! \n'
          'Use apenas (+, -, *, /)')
    





