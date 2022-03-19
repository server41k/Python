def main():
    mas = [10, 2, 3, 1, 22]
    ask = ''
    print('*добавление элемента в конец списка(last)\nдобавление элемента на определенную позицию(pos)\nудаление элемента по индексу и по ключу(remove)\nразмер списка(len)\nсортировка по убыванию и возрастанию(sort)\nвывод на экран элементов списка(print)\nвыход(exit)*\nВведите операцию: ')
    while ask != 'exit':
        ask = input()
        if ask == 'last':
            last(mas)
        if ask == 'pos':
            mas = pos(mas)
        if ask == 'remove':
            mas = rem(mas)
        if ask == 'len':
            lenght()
        if ask == 'sort':
            mas.sort()
        if ask == 'print':
            print(mas)


def last(mas):
    print(mas[len(mas)-1])


def pos(mas):
    mas[int(input("Введите позицию: "))] = input('Введите значение: ')
    return mas


def rem(mas):
    del mas[int(input('Введите индекс'))]
    return mas


def lenght(mas):
    print(len(mas))


main()
# добавление элемента в конец списка
# добавление элемента на определенную позицию
# удаление элемента по индексу и по ключу
# размер списка
# сортировка по убыванию и возрастанию
# вывод на экран элементов списка
# выход
