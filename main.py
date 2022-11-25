from resources import clear
from sistemas import Sistemas
from matematica import Matematica
from games import Games


op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n6) Gerador de CPF\n7) Gerador de Lista de Compras\n\nDigite aqui: ')
       
while True:
    try:
        intOp = int(op)
        if intOp > 7 or intOp < 1:
            clear()
            print('Opção Invalida!\n')
            op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n6) Gerador de CPF\n7) Gerador de Lista de Compras\n\nDigite aqui: ')
            continue
        break
    except ValueError:
        clear()
        print('Você não digitou um numero inteiro!\n')
        op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n6) Gerador de CPF\n7) Gerador de Lista de Compras\n\nDigite aqui: ')
            
if op == '1':
    Games(1)
elif op == '2':
    Matematica(2)
elif op == '3':
    Sistemas(3)
elif op == '4':
    Sistemas(4)
elif op == '5':
    Sistemas(5)
elif op == '6':
    Sistemas(6)
elif op == '7':
    Sistemas(7)
    
print('Finalizado')