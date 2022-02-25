# a*b/(c**d)/(e-(f**g))
def main():
    s = input()
    findbrackets(s)


def findbrackets(s):
    f[0] = s.find('(')
    f[1] = s.find(')')
    return f


if __name__ == main:
    main()
