'''
<var>.isdecimal()   -> O isdecimal() método retorna True se todos os caracteres forem decimais (0-9). (elevados ² crejeitados)
<var>.isnumeric()   -> O isnumeric() método retorna True se todos os caracteres forem numéricos (0-9) (elevados ² contam), caso contrário, False.                                 
<var>.isdigit()     -> O isdigit() método retorna True se todos os caracteres forem dígitos, caso contrário, False. (elevados ² contam)
<var>.isalfnum()    -> O isalnum() método retorna True se todos os caracteres forem alfanuméricos, ou seja, letra do alfabeto (az) e números (0-9).
<var>.isalpha()     -> O isalpha() método retorna True se todos os caracteres forem letras do alfabeto (a-z).
<var>.isupper()     -> O isupper() método retorna True se todos os caracteres estiverem em maiúsculas, caso contrário, False.
<var>.islower()     -> O islower() método retorna True se todos os caracteres estiverem em minúsculo, caso contrário, False.
<var>.isspace()     -> O isspace() método retorna True se todos os caracteres em uma string forem espaços em branco, caso contrário, False.
<var>.istitle()     -> O istitle() método retorna True se todas as palavras em um texto começam com uma letra maiúscula, E o restante da palavra são letras minúsculas, caso contrário, False.
<var>.sqrt()        -> O sqrt() método retorna a raiz quadrada de um número. (import math)

round(<var>) ->  Arredonda para o inteiro mais próximo
ceil(<var>)  ->  Arredonda para cima
floor(<var)  ->  Arredonda para baixo
trunc(<var>) ->  Separa a parte inteira

'''
import os
os.system('clear')

def g(n, c=1): # vetorial
    return c if n==1 else g(n-1, c*n)

# def f(n):
#     return 1 if n==1 else n*f(n-1)

print(g(3))
# print(f(3))