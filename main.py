from resources import clear

op = input(f'Escolha uma opção:\n\n1) Games:\n\nDigite aqui: ')

if op == '1':
    from games import hangmangame
    hangmangame