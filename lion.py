def main():
    randomnum = 1
    Africanlion = lion('African lion')
    Africanlion.roar()
    Asianlion = lion('Asian lion')
    Asianlion.roar()
    WildDogy = dogy('Wild Dogy')
    WildDogy.bark()
    newhero = hero()
    newhero.findanimal('African Lion')


class dogy:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name}: gav-gav')
        print()


class lion:
    def __init__(self, name):
        self.name = name

    def roar(self):
        print(f'{self.name}: Rrrrrrr')


class hero:
    def __init__(self):
        self

    def findanimal(self):


main()
