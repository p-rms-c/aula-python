def maior_produto(sequencia):
  """
  Encontra o conjunto de 5 dígitos consecutivos na sequência que gera o maior produto.

  Args:
    sequencia: Uma sequência de dígitos.

  Returns:
    O conjunto de 5 dígitos consecutivos na sequência que gera o maior produto.
  """

  maior_produto = 0
  maior_conjunto = []
  for i in range(len(sequencia) - 4):
    prod = int(sequencia[i]) * int(sequencia[i + 1]) * int(sequencia[i + 2]) * int(sequencia[i + 3]) * int(sequencia[i + 4])
    if prod > maior_produto:
      maior_produto = prod
      maior_conjunto = [sequencia[i], sequencia[i + 1], sequencia[i + 2], sequencia[i + 3], sequencia[i + 4]]

  return maior_conjunto

sequencia = input('Digite uma sequência de números: ')

resultado = maior_produto(sequencia)

print(resultado)
