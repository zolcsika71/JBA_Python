# create the hierarchy here
class Animal:
    pass


class FlyingAnimal(Animal):
    pass


class SwimmingAnimal(Animal):
    pass


class WalkingAnimal(Animal):
    pass


class Duck(FlyingAnimal, SwimmingAnimal, WalkingAnimal):
    pass
