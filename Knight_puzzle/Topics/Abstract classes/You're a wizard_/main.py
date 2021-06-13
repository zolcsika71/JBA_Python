from abc import ABC, abstractmethod


def sing_song():
    print("No songs for me!")


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def do_spell(self):
        ...


# create a Wizard
class Wizard(Player):
    def fight(self):
        print('Fight')

    def do_spell(self):
        print('Spell')
