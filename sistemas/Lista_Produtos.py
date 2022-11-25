from copy import deepcopy
from resources import clear
import os, copy

def ordenar(x):
    if os.path.exists(NomeListaCompras):
        os.remove(NomeListaCompras)
    listaComprasNomes = copy.deepcopy(sorted(listaCompras, key=lambda i: i[x]))
    listaComprasTXT = open(NomeListaCompras, 'a')
    for i in listaComprasNomes:
        print(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']:.2f} | Preço Total: {i['precoFinal']:.2f}")
        listaComprasTXT.write(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']:.2f} | Preço Total: {i['precoFinal']:.2f}\n")
    listaComprasTXT.close()

# Criando lista de compras ordenadas
listaCompras = []
op = None
while True:
    clear()
    produto = input('Digite o Nome do produto: ')

    while True:
        try:
            quantidade = int(input('Digite a quantidade de compra: '))
            break
        except ValueError as error:
            clear()
            print(f'{error.__class__.__name__}: A Quantidade deve ser um numero Interio\n')

    while True:
        try:
            preco = float(input('Digite o Preço do produto: R$'))
            break
        except ValueError as error:
            clear()
            print(f'{error.__class__.__name__}: O Preço deve conter apenas numeros\n')

    organizandoPorduto = {'produto': produto, 'quantidade': quantidade, 'preco': preco, 'precoFinal': float(preco)*int(quantidade)}

    listaCompras.append(organizandoPorduto)

    op = input('\nDeseja continuar? [s]im ').lower()

    if op == 's':
        continue
    else:
        break

clear()
NomeListaCompras = input('Digite o Nome para a sua lista de compras: ')
clear()
NomeListaCompras += '.txt'
listaComprasTXT = open(NomeListaCompras, 'a')
for i in listaCompras:
    print(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']:.2f} | Preço Total: {i['precoFinal']:.2f}")
    listaComprasTXT.write(f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']:.2f} | Preço Total: {i['precoFinal']:.2f}\n")

listaComprasTXT.close()
print('\nLista de Compras Gerada com sucesso!\n')

op = input('Deseja oredena-la? [s]im ').lower()

if op == 's':
    clear()
    op = input('Escolha uma opção:\n\n1) Nome\n2) Quantidade\n3) Preço\n4) Preço Final\n\nDigite aqui: ')

    while not op.isnumeric():
        clear()
        op = input('Opçõa invalida!\n\nEscolha uma opção:\n\n1) Nome\n2) Quantidade\n3) Preço\n4) Preço Final\n\nDigite aqui: ')
    
    while int(op) > 4 or int(op) < 0:
        clear()
        op = input('Opçõa invalida!\n\nEscolha uma opção:\n\n1) Nome\n2) Quantidade\n3) Preço\n4) Preço Final\n\nDigite aqui: ')

    if int(op) == 1:
        ordenar('produto')
    elif int(op) == 2:
        ordenar('quantidade')
    elif int(op) == 3:
        ordenar('preco')
    elif int(op) == 4:
        ordenar('precoFinal')

else:
    print('Bye Bye')