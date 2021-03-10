class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return f'Hello, I am {self.name}!'


name = str(input())

john = Person(name)

print(john.greet())

