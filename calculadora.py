while True:
    n1 = input('Digite o primeiro número: ')

    n2 = input('Digite o segundo número: ')

    op = input('Digite a operação que deseja fazer(+, -, *, /): ')

    res = ''
    num_1_float = 0
    num_2_float = 0

    numeros_validos = None

    try:
           num_1_float = float(n1)
           num_2_float = float(n2)
           numeros_validos = True
    except:
           numeros_validos = None

    if numeros_validos is None:
           print('Um ou ambos os números digitados são inválidos.')
           continue

    operadores_permitidos = '+-*/'

    if op not in operadores_permitidos:
           print('Operador inválido')
           continue
    
    if len(op) > 1:
           print('Digite apenas um operador.')
           continue

    if (op == '+'):
            
            res = num_1_float + num_2_float

    elif(op == '-'):
            res = num_1_float - num_2_float

    elif(op == '*'):
            res = num_1_float * num_2_float

    elif(op == '/'):
            res = num_1_float / num_2_float
    else:
           print('Não deveria chegar aqui...')

    print(f'O resultado é: ', res)
            
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break