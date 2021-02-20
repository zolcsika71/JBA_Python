class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # define your methods here
    def __iadd__(self, centimeters):
        self.height += centimeters
        return self

    def __isub__(self, centimeters):
        self.height -= centimeters
        return self
