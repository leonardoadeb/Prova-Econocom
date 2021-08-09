from Lib2.Interface import *


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mNão foi possível ler essa lista!\033[m')
    else:
        print(a.read())
    finally:
        a.close()


def cadastrarCliente(arqCliente, nome='desconhecido', número=000000000):
    try:
        a = open(arqCliente, 'at')
    except:
        print('\033[31mOcorreu um erro na exibição dessa lista :(\033[m')
    else:
        try:
            a.write(f'{nome} - {número}\n')
        except:
            print('\033[31mOcorreu um erro no cadastro :(\033[m')
        else:
            print(f'\033[32mNovo cadastro de {nome} concluído\033[m')
            a.close()


def cadastrarProduto(arqProduto, nomeCombo='desconhecido', valor=0):
    try:
        a = open(arqProduto, 'at')
    except:
        print('\033[31mErro no cadastro do produto :(\033[m')
    else:
        try:
            a.write(f'{nomeCombo} - R${valor}\n')
        except:
            print('\033[31mOcorreu um erro no cadastro :(\033[m')
        else:
            print(f'\033[32mNovo combo {nomeCombo} no valor de R${valor} adicionado\033[m')
            a.close()

def anotarPedido(arqPedido, nomePedido='desconhecido', comboPedido='desconhecido', valorPedido=0):
    try:
        a = open(arqPedido, 'at')
    except:
        print('\033[31mErro ao anotar pedido :(\033[m')
    else:
        try:
            a.write(f'{nomePedido} - {comboPedido} - R${valorPedido}\n')
        except:
            print('\033[31mOcoreu um erro ao anotar o pedido :(\033[m')
        else:
            print(f'\033[32mO pedido de {nomePedido} de {comboPedido} no valor de R${valorPedido} foi anotado com sucesso!\033[m')
            a.close()

def NumeroDePedidos(numeroPedidos):
    with open('listadepedidos.txt') as p:
        print(sum(1 for linha in p))
