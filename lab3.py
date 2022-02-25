from decimal import DivisionByZero


def main():
    try:
        a1 = int(input())
    except:
        print('Error')
        exit
    op = input()
    if op not in ('-', '+', '/', '*'):
        print('Error')
        exit
    try:
        a2 = int(input())
    except:
        print('Error')
        exit
    if op == '+':
        res = a1+a2
    elif op == '-':
        res = a1-a2
    elif op == '*':
        res = a1*a2
    elif op == '/':
        try:
            res = a1/a2
        except DivisionByZero:
            print("Error")
            exit
    print(a1, op, a2, '=', res)


def sub():
    str = input("Введите выражение: ")
    if str.find("/") != -1:
        op = str.find("/")
        exit
    elif str.find("*") != -1:
        op = str.find("*")
        exit
    elif str.find("+") != -1:
        op = str.find("+")
        exit
    elif str.find("-") != -1:
        op = str.find("-")
        exit
    try:
        a1 = int(str[0: op])
        a2 = int(str[op+1:])
    except:
        print('Error')
        exit
    op = str[op]  # '/'
    if op == '+':
        res = a1+a2
    elif op == '-':
        res = a1-a2
    elif op == '*':
        res = a1*a2
    elif op == '/':
        try:
            res = a1/a2
        except:
            print("Error")
            exit
    print(a1, op, a2, '=', res)


if input('1 или 2: ') == "1":
    main()
else:
    sub()
