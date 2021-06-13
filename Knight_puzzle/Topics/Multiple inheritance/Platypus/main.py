class Animal:
    def __init__(self, name):
        self.name = name
        print("Created an Animal")


# create the rest of the classes here
class Mammal(Animal):
    def __init__(self, name):
        print("Created a Mammal")
        super().__init__(name)


class Reptile(Animal):
    def __init__(self, name):
        print("Created a Reptile")
        super().__init__(name)


class Platypus(Mammal, Reptile):
    def __init__(self, name):
        print("Created a Platypus")
        super().__init__(name)


# p = Mammal('Zoller')
