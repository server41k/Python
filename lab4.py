# a*b/(c**d)/(e-(f**g))
def main():
    s = input()
    stroka = ''
    temps = ''
    for o in range(counter(s)):
        open_bracket, close_bracket = findbrackets(s)
        for i in range(open_bracket+1, close_bracket):
            stroka = stroka+s[i]
        for i in range(0, open_bracket):
            temps = temps+s[i]
        temps = temps+str(solution(stroka))
        for i in range(close_bracket+1, len(s)):
            temps = temps+s[i]
        s = temps
        stroka = ''
        result = temps
        temps = ''
    temp = ['' for j in range(len(s))]
    num = ['' for j in range(len(s))]
    counte = 0
    for j in range(len(result)):
        if result[j] in ('-', '+', '/', '*'):
            temp[counte] = result[j]
            counte = counte+1
        else:
            num[counte] = num[counte]+result[j]
    print(num[0])
    for i in range(counte+1):
        print(num[i])
        print(temp[i])


def counter(s):
    temp = 0
    while s.find('(') != -1:
        a = s.find('(')
        s = s[:a]+s[a+1:]
        temp = temp+1
    return temp


def solution(str):
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
    op = str[op]
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
            print("Error dividing on zero")
            exit
    return res


def findbrackets(s):
    a = s.find('(')
    b = s.find(')')
    return a, b


main()
