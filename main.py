from resources import clear

op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n\nDigite aqui: ')

while True:
    try:
        intOp = int(op)
        if intOp > 2 or intOp < 1:
            clear()
            print('Opção Invalida!\n')
            op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n\nDigite aqui: ')
            continue
        break
    except ValueError:
        clear()
        print('Você não digitou um numero inteiro!\n')
        op = input(f'Escolha uma opção:\n\n1) Jogo da Forca:\n2) Impar ou Par\n\nDigite aqui: ')

if op == '1':
    from games import hangmangame
    hangmangame
elif op == '2':
    from matematica import impar_par
    impar_par