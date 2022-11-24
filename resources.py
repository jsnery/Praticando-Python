from sys import platform
from os import system

def clear():
    if platform == 'linux' or platform == 'darwin':
        return system('clear')
    return system('cls')
