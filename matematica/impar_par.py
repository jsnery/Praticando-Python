from resources import clear
clear()
numero = input('Digite um numero: ')
floatNumero = None
while True:
    try:
        floatNumero = float(numero)
        break
    except ValueError:
        clear()
        print('Isso não é um numero!\n')
        numero = input('Digite um numero: ')

print(f'O Numero {numero} é:\n')
print('Par' if (floatNumero % 2) == 0 else 'Impar')