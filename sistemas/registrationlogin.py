import sqlite3
from pathlib import Path
from os import system
from sys import platform

__all__ = ['registration_login_sys']

def clear():
    match platform:
        case 'win32' | 'cygwin':
            return system('cls')
        case _:
            return system('clear')

def create_database(cls):
    DIR = Path(__file__).parent / 'data'
    DIR.mkdir() if not DIR.exists() else ...
    DBDIRECTORY = DIR / 'database.db'
    
    def creation(self, user, password):
        self._user = user
        self._password = password
        self.database = sqlite3.connect(DBDIRECTORY)
        self.cursor = self.database.cursor()             
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user TEXT UNIQUE, password TEXT)')
        
    cls.__init__ = creation
    return cls

@create_database
class LoginSystem:
    
    @property   
    def registration(self) -> bool:
        user = self._user
        password = self._password
        try:
            if user == '' or password == '' or user.isspace() or password.isspace():
                return False
            self.cursor.execute(f'INSERT INTO users(user, password) VALUES ("{user}","{password}")')
            self.database.commit()
            return True
        except sqlite3.Error:
            return False
        
    @property    
    def login(self) -> bool:
        user = self._user
        password = self._password
        
        self.cursor.execute('SELECT user,password FROM users')
        for users in self.cursor.fetchall():
            if user == users[0] and password == users[1]:
                return True
            
        return False
    
def registration_login_sys():
    clear()
    user = None
    password = None
    system_ = LoginSystem

    while True:
        option = input('1) Registration\n2) Login\n\nType Here: ')
        match option:
            case '1':  # Registration
                clear()
                user = input('User: ')
                password = input('Password: ')
                if system_(user, password).registration:
                    clear()
                    print('Registration Success!\n')
                    continue
                clear()
                print('Registration Failed!\n')
            case '2':  # Login
                clear()
                user = input('User: ')
                password = input('Password: ')
                
                if system_(user, password).login:
                    clear()
                    print('Login Success')
                    break
                
                clear()
                print('Login Failed\n')
            case _:    # does not exist in option
                clear()
                print('No Understand you option! Try Again!\n')
            
