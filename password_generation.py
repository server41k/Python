from random import *


def password():
    password_count = int(input("Сколько паролей: "))
    length = int(input("Длинна пароля: "))
    ABCon = int(input("Большие буквы в пароле (1/0): "))
    symbolson = int(input("Символы в пароле (1/0): "))
    chars = ''
    if ABCon == 1:
        chars += 'QWERTYUIOPASDFGHJKLZXCVBNM'
    if symbolson == 1:
        chars += '!#$%&*+-=?@^_'
    chars += 'abcdefghijklmnopqrstuvwxyz'
    chars += '1234567890'
    chars = [i for i in chars]
    for _ in range(password_count):
        for i in range(length):
            print(chars[randint(0, len(chars))], end='')
        print()


password()
