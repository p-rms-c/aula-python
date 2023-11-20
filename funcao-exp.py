def func_exponencial(base, expoente):
    result = 1
    for index in range(expoente):
        result = result * base
    return result

print(func_exponencial(3, 4))