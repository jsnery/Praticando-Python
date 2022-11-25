from resources import clear
from sistemas import cadastro_simples, login_simples, gerador_cpf, validador_cpf
from matematica import impar_par
from games import hangmangame


op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n6) Gerador de CPF\n\nDigite aqui: ')

while True:
    try:
        intOp = int(op)
        if intOp > 6 or intOp < 1:
            clear()
            print('Opção Invalida!\n')
            op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n6) Gerador de CPF\n\nDigite aqui: ')
            continue
        break
    except ValueError:
        clear()
        print('Você não digitou um numero inteiro!\n')
        op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n3) Cadastro Simples\n4) Tela de Login\n5) Validador de CPF\n6) Gerador de CPF\n\nDigite aqui: ')

if op == '1':
    hangmangame
elif op == '2':
    impar_par
elif op == '3':
    cadastro_simples
elif op == '4':
    login_simples
elif op == '5':
    validador_cpf
elif op == '6':
    gerador_cpf
    
print('Finalizado')