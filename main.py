from Lib2.Interface import *
from Lib2.arquivo import *


arqCliente = 'listadeclientes.txt'
arqProduto = 'listadeprodutos.txt'
arqPedido = 'listadepedidos.txt'

while True:
    resposta = menu(['Clientes', 'Combos', 'Pedidos', 'Sair'])
    if resposta == 1:
        resposta = menuCliente(['Ver clientes', 'Cadastrar novo cliente', 'Voltar'])
        if resposta == 1:
            cabeçalho('Clientes Cadastrados')
            lerArq(arqCliente)
        elif resposta == 2:
            cabeçalho('Novo cadastro')
            nome = str(input('Nome: '))
            número = leiaInteiro('Número de telefone: ')
            cadastrarCliente(arqCliente, nome, número)
        elif resposta == 3:
            continue
        else:
            print('Digite uma opção válida.')
    elif resposta == 2:
        resposta = menuProduto(['Ver Combos', 'Cadastrar novo combo', 'Voltar'])
        if resposta == 1:
            cabeçalho('Lista de Combos')
            lerArq(arqProduto)
        elif resposta == 2:
            cabeçalho('Novo Produto')
            nomeCombo = str(input('Nome do Combo: '))
            valor = leiaReal('Valor do Combo: ')
            cadastrarProduto(arqProduto, nomeCombo, valor)
        elif resposta == 3:
            continue
    elif resposta == 3:
        resposta = menuPedidos(['Ver Pedidos', 'Anotar novo pedido', 'Número de pedidos', 'Voltar'])
        if resposta == 1:
            cabeçalho('Lista de Pedidos')
            lerArq(arqPedido)
        elif resposta == 2:
            cabeçalho('Anotar novo pedido')
            nomePedido = str(input('Quem fez o pedido? '))
            comboPedido = str(input('O que foi pedido? '))
            valorPedido = leiaReal('Qual foi o valor da compra? ')
            anotarPedido(arqPedido, nomePedido, comboPedido, valorPedido)
        elif resposta == 3:
            cabeçalho('Número de Pedidos')
            with open('listadepedidos.txt') as p:
                print(sum(1 for linha in p))
        elif resposta == 4:
            continue
    elif resposta == 4:
        print('\033[34mAté logo...')
        break
    else:
        print('\033[31mDigite uma opção válida\033[m')
