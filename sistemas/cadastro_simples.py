from resources import clear
from pathlib import Path
from sys import exit

def registration_system():
    clear()
    usersReg = []
    x = False
    
    FILEDIR = Path(__file__).parent / 'recursos/userpass.txt'

    while True:
        while True:
            user = input('User: ')
            psw = input('Password: ')
            validation = user.isspace() or psw.isspace() or not bool(user) or not bool(psw)
            match validation:
                case True:
                    clear()
                    print('Invalid user or password! Try Again!\n')
                    continue
                case _:
                    break

        with FILEDIR.open('a+') as file:
            file.write(f'\n{user} {psw}')

        register = {'user': user, 'psw': psw}
        usersReg.append(register)

        clear()
        print('Registration List:\n')
        for i in usersReg:
            print(f"User:{i['user']} | Password:{i['psw']}\n")

        while True:
            op = input('Press [E]xit or [C]ontinue: ')
            
            match op.lower():
                case 'e' | 'exit':
                    x = True
                    break
                case 'c' | 'continue':
                    break
                case _:
                    print('No understand what you typed!\n ')
                    
        if x is True:
            clear()
            break
                    
            
if __name__ == '__main__':
    registration_system()