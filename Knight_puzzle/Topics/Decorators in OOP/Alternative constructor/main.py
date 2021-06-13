class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_string(cls, data):
        name, email = data.split('-')
        return cls(name, email)
