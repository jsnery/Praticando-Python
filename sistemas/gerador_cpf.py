from resources import clear
from random import randint
clear()

cpf = randint(100000000, 999999999)
novoCPF = str(cpf)
digito = None
while True:
    total = 0
    for i, n in enumerate(reversed(novoCPF), 2):
        total += i * int(n)

    digito = 0 if (total % 11) < 2 else 11 - (total % 11)
    novoCPF += str(digito)

    if len(novoCPF) == 11:
        break

print('O CPF GERADO FOI: ', novoCPF)