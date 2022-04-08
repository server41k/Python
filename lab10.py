from re import *


def main():
    s = '''sad asd asfgad g 3457834958@374.34 serverchaush@mail.ru serverchaush@mail.ru          serverchaush@mail.ru
serverchaush@mail.ru somebodysmail@gmail.com дырпзжвалржв еорывор ыре жуфорвол Ц4ег6 496е -;Ц69_"65 г
sdaasd asd as@dasd,.2d ss@mail.ru ksfposdkfpsdfk.@mail.ru google.com
me@mail.google yjvth afjaf apsfdg +79782702019 b 8808055353              and 8223383412                  and 8978270201 +79782702019
223591959 59 195953406630986 14819034 84 239423902923408 +7978123912948914 asdo 8800555 3535d 99113526666
spglsd]g sd]glp] sdgp sdg +94949349494 askdasdkl +228228665282828 8800555353 8 8 868 588 858
'''
    mail(s)
    phone(s)


def phone(s):
    s = s.split()
    l = []
    for i in s:
        searched = fullmatch('[0-9]{10}', i)
        if searched != None:
            l.append(searched.string)
        searched = fullmatch('[+][0-9]{11}', i)
        if searched != None:
            l.append(searched.string)
    print("Номера:")
    print(*l, sep=', ')


def mail(s):
    s = s.split()
    l = []
    for i in s:
        searched = fullmatch(r"[0-9a-zA-Z]+@[a-zA-Z]+.[a-zA-Z]+", i)
        if searched != None:
            l.append(searched.string)
    print("Электронные адреса:")
    print(*l, sep=', ')
