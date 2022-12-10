from resources import clear
from pathlib import Path

def login_system():
    clear()
    FILEDIR = Path(__file__).parent / f'recursos/userpass.txt'
    username = None
    password = None
    data_users_create = None
    list_data_users = []
    validation = False

    with FILEDIR.open('r') as file:
        user_data = file.readlines()

        for dados in user_data:
            username, password = dados.split()
            data_users_create = {'user': username, 'psw': password}
            list_data_users.append(data_users_create)
    
    while True:
        user = input('Digite seu usuário: ')
        password = input('Digite sua senha: ')
        validation = user.isspace() or password.isspace() or not bool(user) or not bool(password)
        match validation:
            case True:
                clear()
                print("Você precisa digitar um usuário e senha!\n")
                continue
            case _:
                break

    for dados in list_data_users:
        if user == dados['user'] and password == dados['psw']:
            clear()
            print("Entrou com sucesso!\n")
            break

    else:
        clear()
        print('Usuario não encontrado!\n')