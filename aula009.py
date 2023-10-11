frutas = ['morango', 'laranja', 'uva', 'banana', 'banana', 'abacaxi']
frutas[1] = 'melancia'

numeros_da_sorte = [30, 4, 8, 15, 16, 23, 4]

frutas.extend(numeros_da_sorte)
frutas.append('limão')
frutas.insert(1, 'mamao')
frutas.remove('limão')
frutas.pop()
print(frutas.index('uva'))
print(frutas.count('banana'))
#frutas.sort()  ---não funciona com int e str

frutas2 = frutas.copy()

print(frutas2)