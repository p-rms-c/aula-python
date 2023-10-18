def verifica_cpf():
    cpf_usuario = input('Digite seu cpf \n')
        

    x = cpf_usuario.split('.')
    y = cpf_usuario.split('-')

    if len(cpf_usuario) == 14 and len(x) == 3 and len(y) == 2:
        print('cpf válido')
    else: 
        print('cpf inválido')

verifica_cpf()