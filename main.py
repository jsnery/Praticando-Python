from resources import clear
from sistemas import Sistemas
from matematica import Matematica
from games import Games

options_msg = f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n\
                3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n\
                6) Gerador de CPF\n7) Gerador de Lista de Compras\n\nDigite aqui: '

op = input(options_msg)
       
while True:
    match op:
        case '1':
            Games(1)
        case '2':
            Matematica(2)
        case '3':
            Sistemas(3)
        case '4':
            Sistemas(4)
        case '5':
            Sistemas(5)
        case '6':
            Sistemas(6)
        case '7':
            Sistemas(7)
        case _:
            clear()
            print('Opção Invalida!\n')
            op = input(options_msg)

