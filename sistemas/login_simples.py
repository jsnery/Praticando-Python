
nome = None
senha = None
dictDeRegistro = None
usersReg = []

dadosExternos = open('sistemas/recursos/userpass.txt', 'r')
dadosExternosUsuario = dadosExternos.readlines()

for dados in dadosExternosUsuario:
    nome, senha = dados.split()
    dictDeRegistro = {'user': nome, 'psw': senha}
    usersReg.append(dictDeRegistro)

dadosExternos.close()

user = input('Digite seu usuário: ')
psw = input('Digite sua senha: ')

validation = user.isspace() or psw.isspace() or not bool(user) or not bool(psw)

while validation:
    print('Usuáŕio e/ou Senha invalido(s)!\n')
    user = input('Digite seu usuário: ')
    psw = input('Digite sua senha: ')

for dados in usersReg:
    if user == dados['user'] and psw == dados['psw']:
        print("Entrou com sucesso!")
        break

else:
    print('Usuario não encontrado!')