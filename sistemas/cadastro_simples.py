from resources import clear

usersReg = []

while True:
    clear()
    user = input('Digite seu usuário: ')
    psw = input('Digite sua senha: ')

    validation = user.isspace() or psw.isspace() or not bool(user) or not bool(psw)

    while validation:
        clear()
        print('Usuáŕio e/ou Senha invalido(s)!\n')
        user = input('Digite seu usuário: ')
        psw = input('Digite sua senha: ')

    dadosExternos = open('sistemas/recursos/userpass.txt', 'a')
    dadosExternos.write(f'\n{user} {psw}')
    dadosExternos.close()

    register = {'user': user, 'psw': psw}
    usersReg.append(register)

    clear()
    print('Lista de Registro:\n')
    for i in usersReg:
        print(f"Usuário:{i['user']}\nSenha:{i['psw']}\n")

    op = input('Press [E] and [Enter] for Exit')

    if op.lower() == 'e':
        break
    
