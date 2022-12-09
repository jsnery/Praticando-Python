from resources import clear
from sistemas import registration_system, cpf_generator, product_list, login_system, cpf_validator
from matematica import imparpar
from games import hangman_game

options_msg = f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n\
3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n\
6) Gerador de CPF\n7) Gerador de Lista de Compras\n\nDigite aqui: '
       
while True:
    op = input(options_msg)
    
    match op:
        case '1':
            hangman_game()
        case '2':
            imparpar()
        case '3':
            registration_system()
        case '4':
            login_system()
        case '5':
            cpf_validator()
        case '6':
            cpf_generator()
        case '7':
            product_list()
        case _:
            clear()
            print('Opção Invalida!\n')

