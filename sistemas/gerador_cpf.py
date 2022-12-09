from resources import clear
from random import randint

def cpf_generator():
    clear()
    cpf = randint(100000000, 999999999)
    new_cpf = str(cpf)
    digit = None
    while True:
        total = 0
        for i, n in enumerate(reversed(new_cpf), 2):
            total += i * int(n)

        digit = 0 if (total % 11) < 2 else 11 - (total % 11)
        new_cpf += str(digit)

        if len(new_cpf) == 11:
            break

    print('O CPF GERADO FOI: ', new_cpf)
    
if __name__ == '__main__':
    cpf_generator()