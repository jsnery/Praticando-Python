from resources import clear


def hangman_game():
    def bonecoVidas():
        if vidas == 6:
            print(f'''\
    _____
    |     | Restam {vidas} vidas!
    |     
    |              O
    |             /|\ 
   _|________     / \ 
    ''')
        if vidas == 5:
            print(f'''\
    _____      
    |     | Restam {vidas} vidas!
    |     O
    |        
    |             /|\ 
   _|________     / \ 
    ''')
        elif vidas == 4:
            print(f'''\
    _____
    |     | Restam {vidas} vidas!
    |     O
    |     |
    |             / \ 
   _|________     / \ 
    ''')
        elif vidas == 3:
            print(f'''\
    _____
    |     | Restam {vidas} vidas!
    |     O
    |    /|
    |               \ 
   _|________     / \ 
    ''')
        elif vidas == 2:
            print(f'''\
    _____
    |     | Restam {vidas} vidas!  
    |     O
    |    /|\ 
    |
   _|________     / \ 
    ''')
        elif vidas == 1:
            print(f'''\
    _____
    |     | Restam {vidas} vidas!
    |     O
    |    /|\ 
    |      \ 
   _|________     / 
    ''')
        elif vidas == 0:
            print(f'''\
    _____
    |     |    VOCÊ PERDEU!
    |     O
    |    /|\     
    |    / \ 
   _|________
    ''')

    clear()
    palavra = input('Digite a palavra desejada: ').upper()

    check_Palavra = not palavra.isalpha()
    resultado = ['_' for i in palavra]
    resultadoTexto = "".join(resultado)
    letrasTestadas = set()
    vidas = 6

    while check_Palavra:  # Verificando se é uma Palavra
        clear()
        palavra = input('Digite a palavra desejada: ').upper()

    bonecoVidas()
    print(resultadoTexto, '\n')
    while True:  # Estrutura do Jogo
        letraChute = input('Digite uma letra: ').upper()

        if not letraChute.isalpha():
            clear()
            print('Isso não é uma letra!\n')
            bonecoVidas()
            print(resultadoTexto, '\n')
            continue

        if not len(letraChute) == 1:
            clear()
            print('Digite apena uma letra!\n')
            bonecoVidas()
            print(resultadoTexto, '\n')
            continue

        if letraChute in letrasTestadas:
            clear()
            print('Essa letra já foi chutada!\n')
            bonecoVidas()
            print(resultadoTexto, '\n')
            continue
        letrasTestadas.add(letraChute)

        if letraChute not in palavra:
            clear()
            print('Essa letra não pertence a palavra!')
            vidas -= 1
            if vidas == 0:
                bonecoVidas()
                break
            bonecoVidas()
            print(resultadoTexto, '\n')
            continue

        clear()
        print(f'Letra "{letraChute}" Encontrada!')
        bonecoVidas()
        for i, letra in enumerate(palavra):
            if letraChute == letra:
                resultado[i] = letra

        resultadoTexto = "".join(resultado)
        print(resultadoTexto, '\n')

        if resultadoTexto == palavra:
            clear()
            print('''\
    _____
    |     |    PARABÊNS!
    |     
    |             \O/
    |              |
   _|________     / \ 
    ''')
            print(f'A palavra é : {resultadoTexto}')
            break
