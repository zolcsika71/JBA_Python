# write your code here
import random


class BillSplitter:
    def __init__(self):
        self.number_of_guests = int(input("Enter the number of friends joining (including you):\n"))
        self.lucky_guest = None
        if self.number_of_guests > 0:
            guests_ = []
            print(f'\nEnter the name of every friend (including you), each on a new line:')
            for i in range(self.number_of_guests):
                guests_.append(input())
            self.guests = {name: 0 for name in guests_}
            self.bill = int(input('\nEnter the total bill value:\n'))
            self.lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
            self.run()
        else:
            print('\nNo one is joining for the party')

    def get_lucky_guest(self):
        if self.lucky_feature == 'Yes':
            guests_keys = list(self.guests.keys())
            self.lucky_guest = random.choice(guests_keys)
            print(f'\n{self.lucky_guest} is the lucky one!')
        else:
            print(f'\nNo one is going to be lucky')

    def split_bill(self):
        if self.lucky_feature == 'Yes':
            amount = round(self.bill / (self.number_of_guests - 1), 2)
            self.guests = {key: (amount if key != self.lucky_guest else 0) for key in self.guests}
        else:
            amount = round(self.bill / self.number_of_guests, 2)
            self.guests = {name: amount for name in self.guests}

    def run(self):
        self.get_lucky_guest()
        self.split_bill()
        print(f'\n{self.guests}')


bill = BillSplitter()
