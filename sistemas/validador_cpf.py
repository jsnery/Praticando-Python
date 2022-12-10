from resources import clear

def cpf_validator():
    clear()
    cpf = input('Digite um CPF: ').replace('-','.').replace('.','')
    novoCPF = cpf[:9]
    digito = None
    while True:
        total = 0
        for i, n in enumerate(reversed(novoCPF), 2):
            total += i * int(n)

        digito = 0 if (total % 11) < 2 else 11 - (total % 11)
        novoCPF += str(digito)

        if len(novoCPF) == 11:
            break

    if (novoCPF[0] * 11) == cpf:
        print("\nCPF INVALIDO!\n")
    elif novoCPF != cpf:
        print("\nCPF INVALIDO!\n")
    else:
        print('\nCPF VÁLIDO!\n')