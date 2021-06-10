from operator import attrgetter
from math import floor


class Animal:
    def __init__(self, name='', price=0):
        self.name = name
        self.price = price
        self.ratio = None


class Solve:
    def __init__(self, animals_, money_):
        self.animals = animals_
        self.money = money_
        self.best_ratio = None
        self.best_candidate = Animal()

    def count_animal_ratio(self):
        for animal in self.animals:
            animal.ratio = self.money / animal.price

    def find_best(self):
        self.animals = [x for x in self.animals if x.ratio >= 1]
        if len(self.animals) > 1:
            self.best_candidate = min(self.animals, key=attrgetter('ratio'))
        elif len(self.animals) == 1:
            self.best_candidate = self.animals[0]

    def print_result(self):
        if self.best_candidate.ratio is None:
            print(f'None')
            return
        elif int(self.best_candidate.ratio) > 1 and self.best_candidate.name != 'sheep':
            self.best_candidate.name = self.best_candidate.name + 's'

        print(f'{int(self.best_candidate.ratio)} {self.best_candidate.name}')

    def run(self):
        self.count_animal_ratio()
        self.find_best()
        self.print_result()


chicken = Animal('chicken', 23)
goat = Animal('goat', 678)
pig = Animal('pig', 1296)
cow = Animal('cow', 3848)
sheep = Animal('sheep', 6769)

animals = [chicken, goat, pig, cow, sheep]

money = int(input())

result = Solve(animals, money)

result.run()











