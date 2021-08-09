def leiaInteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Digite um número inteiro.\033[m')
            continue
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            h = float(input(msg))
        except (TypeError):
            print('\033[31mErro: Digite um valor real.\033[m' + str(TypeError))
            continue
        else:
            return h


def linha(tam=42):
    return '\033[1;33m-\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[1;34m          Lanches da Quarentena \033[m')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInteiro('\033[1;36mDigite sua opção: \033[m')
    return opc

def menuCliente(lista):
    cabeçalho('Clientes')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInteiro('\033[1;36mDigite sua opção: \033[m')
    return opc

def menuProduto(lista):
    cabeçalho('Combos')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInteiro('\033[1;36mDigite sua opção: \033[m')
    return opc

def menuPedidos(lista):
    cabeçalho('Pedidos')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInteiro('\033[1;36mDigite sua opção: \033[m')
    return opc