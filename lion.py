def main():


class dogy:
    def __init__(self, name):
        pass

    def bark(self):
        print(f'{self.name}: gav-gav')
        print()


class lion:
    def __init__(self, name):
        self.name = name

    def roar(self):
        print(f'{self.name}: Rrrrrrr')


class hero:
    def findanimal(self, animal):
        animal.roar()


main()
