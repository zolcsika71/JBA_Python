from abc import ABC, abstractmethod


# create Human
class Human(ABC):

    @abstractmethod
    def say_hello(self):
        ...
