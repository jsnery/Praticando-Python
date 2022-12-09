from copy import deepcopy
from pathlib import Path
from resources import clear

def product_list():
    def ordenar(x):
        if FILEDIR.exists():
            FILEDIR.unlink()
        list_sort_key = sorted(deepcopy(buy_list), key=lambda i: i[x])
        with FILEDIR.open('a+') as file:
            file.write(f'{list_title}\n\n')
            for i in list_sort_key:
                list_data = f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']: ^8.2f} | Preço Total: {i['precoFinal']:,.2f}\n"
                file.write(list_data)

    # Criando lista de compras ordenadas
    buy_list = []
    options = None
    x = False

    while True:
        clear()
        item_name = input('Digite o Nome do produto: ')

        while True: # Insira a quantidade
            try:
                item_quantity = int(input('Digite a quantidade de compra: '))
                break
            except ValueError as error:
                clear()
                print(f'{error.__class__.__name__}: A Quantidade deve ser um numero Interio\n')

        while True: # Insira o Preço
            try:
                item_price = float(input('Digite o Preço do produto: R$').replace(',', '.'))
                break
            except ValueError as error:
                clear()
                print(f'{error.__class__.__name__}: O Preço deve conter apenas numeros\n')

        products_dict = {'produto': item_name, 'quantidade': item_quantity, 'preco': item_price, 'precoFinal': item_price*item_quantity}

        buy_list.append(products_dict)
        
        while True:
            options = input('\nAdd more items, [y]es or [n]ot?\n')
            
            match options.lower():
                case 'y' | 'yes' | 'yet' | 'yup':
                    break
                case 'n' | 'no' | 'not':
                    x = True
                    break
                case _:
                    clear()
                    print('No understand what you typed! ')
                    
        if x is True:
            break

    clear()

    list_name = input('Nomeie o arquivo: ').replace(' ', '-')
    list_title = input('Digite o Titulo da lista: ')

    FILEDIR = Path(__file__).parent / f'recursos/{list_name}.txt'

    clear()

    with FILEDIR.open('a+') as file:
        file.write(f'{list_title}\n\n')
        for i in buy_list:
            list_data = f"Produto: {i['produto']: ^15} | Unidades: {i['quantidade']:0>3} | Preço Unitário: {i['preco']: ^8.2f} | Preço Total: {i['precoFinal']:,.2f}\n"
            print(list_data)
            file.write(list_data)

    print('\nSuccess genered buy list!\n')

    while True:
        options = input('Wish sort? [y]es [n]ot ')
        
        match options.lower():
            case 'y' | 'yes' | 'yet' | 'yup':
                clear()
                while True:
                    options = input('Try option:\n\n1) Nome\n2) Quantidade\n3) Preço\n4) Preço Final\n\nDigite aqui: ')

                    match options.lower():
                        case '1':
                            ordenar('produto')
                            break
                        case '2':
                            ordenar('quantidade')
                            break
                        case '3':
                            ordenar('preco')
                            break
                        case '4':
                            ordenar('precoFinal')
                            break
                        case _:
                            clear()
                            print('No understand what you typed! ')
                            
            case 'n' | 'no' | 'not':
                clear()
                break
            case _:
                clear()
                print('No understand what you typed!\n')
                    
                    
            
