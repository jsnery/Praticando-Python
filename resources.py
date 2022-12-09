from sys import platform
from os import system


def clear():
    match platform:
        case 'win32' | 'cygwin':
            return system('cls')
        case _:
            return system('clear')
