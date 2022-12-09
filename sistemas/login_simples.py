from resources import clear
from pathlib import Path

def login_system():
    FILEDIR = Path(__file__).parent / f'recursos/userpass.txt'
    username = None
    password = None
    data_users_create = None
    list_data_users = []

    with FILEDIR.open('r') as file:
        user_data = file.readlines()

        for dados in user_data:
            username, password = dados.split()
            data_users_create = {'user': username, 'psw': password}
            list_data_users.append(data_users_create)

    clear()
    user = input('Digite seu usuário: ')
    password = input('Digite sua senha: ')

    validation = user.isspace() or password.isspace() or not bool(user) or not bool(password)

    while validation:
        clear()
        print('Usuário e/ou Senha invalido(s)!\n')
        user = input('Digite seu usuário: ')
        password = input('Digite sua senha: ')

    for dados in list_data_users:
        if user == dados['user'] and password == dados['psw']:
            print("\nEntrou com sucesso!")
            break

    else:
        print('\nUsuario não encontrado!')