from copy import deepcopy
from resources import clear
import os

def ordenar(x):
    if os.path.exists(nomeLista_Txt):
        os.remove(nomeLista_Txt)
    listaComprasNomes = sorted(deepcopy(listaCompras), key=lambda i: i[x])
    listaComprasTXT = open(nomeLista_Txt, 'a')
    listaComprasTXT.write(f'{tituloLista_Txt}\n\n')
    for i in listaComprasNomes:
        print(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']: ^8.2f} | Preço Total: {i['precoFinal']:,.2f}")
        listaComprasTXT.write(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']: ^8.2f} | Preço Total: {i['precoFinal']:,.2f}\n")
    listaComprasTXT.close()

# Criando lista de compras ordenadas
listaCompras = []
escolhaOpcao = None

while True:
    clear()
    item = input('Digite o Nome do produto: ')

    while True: # Insira a quantidade
        try:
            qnt = int(input('Digite a quantidade de compra: '))
            break
        except ValueError as error:
            clear()
            print(f'{error.__class__.__name__}: A Quantidade deve ser um numero Interio\n')

    while True: # Insira o Preço
        try:
            preco = float(input('Digite o Preço do produto: R$').replace(',', '.'))
            break
        except ValueError as error:
            clear()
            print(f'{error.__class__.__name__}: O Preço deve conter apenas numeros\n')

    dictProdutos = {'produto': item, 'quantidade': qnt, 'preco': preco, 'precoFinal': preco*qnt}

    listaCompras.append(dictProdutos)

    escolhaOpcao = input('\nDeseja continuar? [s]im ').lower()

    if escolhaOpcao == 's':
        continue
    else:
        break

clear()

nomeLista_Txt = input('Nomeie o arquivo: ').replace(' ', '-')
tituloLista_Txt = input('Digite o Titulo da lista: ')

clear()

nomeLista_Txt += '.txt'
lista_Txt = open(nomeLista_Txt, 'a')
lista_Txt.write(f'{tituloLista_Txt}\n\n')
for i in listaCompras:
    print(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']: ^8.2f} | Preço Total: {i['precoFinal']:,.2f}")
    lista_Txt.write(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']: ^8.2f} | Preço Total: {i['precoFinal']:,.2f}\n")

lista_Txt.close()

print('\nLista de Compras Gerada com sucesso!\n')

escolhaOpcao = input('Deseja oredena-la? [s]im ').lower()

if escolhaOpcao == 's':
    clear()
    escolhaOpcao = input('Escolha uma opção:\n\n1) Nome\n2) Quantidade\n3) Preço\n4) Preço Final\n\nDigite aqui: ')

    while not escolhaOpcao.isnumeric() or int(escolhaOpcao) > 4 or int(escolhaOpcao) < 0:
        clear()
        escolhaOpcao = input('Opçõa invalida!\n\nEscolha uma opção:\n\n1) Nome\n2) Quantidade\n3) Preço\n4) Preço Final\n\nDigite aqui: ')
    
    if int(escolhaOpcao) == 1:
        ordenar('produto')
    elif int(escolhaOpcao) == 2:
        ordenar('quantidade')
    elif int(escolhaOpcao) == 3:
        ordenar('preco')
    elif int(escolhaOpcao) == 4:
        ordenar('precoFinal')
