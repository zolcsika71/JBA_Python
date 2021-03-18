import sqlite3
from random import randint as rnd

DROP_TABLE = 'DROP TABLE IF EXISTS card;'

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);
"""

ADD_CARD = 'INSERT INTO card (number, pin) VALUES (?, ?);'

DELETE_CARD = 'DELETE FROM card WHERE number=?;'

GET_CARD_BY_NUMBER = 'SELECT * FROM card WHERE number=?;'

GET_BALANCE = 'SELECT balance FROM card WHERE number=?;'

UPDATE_BALANCE = 'UPDATE card SET balance = ? WHERE number = ?;'

CLOSE_ACCOUNT = 'DELETE FROM card WHERE number = ?;'

MAIN_MENU_PROMPT = """
1. Create an account
2. Log into account
0. Exit
"""

ACCOUNT_MENU_PROMPT = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""


class BankingSystem:
    def __init__(self):
        self.connection = sqlite3.connect('card.s3db')
        self.drop_table()
        self.create_table()
        self.main_menu()

    def drop_table(self):
        with self.connection:
            self.connection.execute(DROP_TABLE)

    def create_table(self):
        with self.connection:
            self.connection.execute(CREATE_TABLE)

    def add_card(self, number, pin):
        with self.connection:
            self.connection.execute(ADD_CARD, (number, pin))

    def get_card_by_number(self, number):
        with self.connection:
            return self.connection.execute(GET_CARD_BY_NUMBER, (number,)).fetchone()

    def update_balance(self, number, balance):
        with self.connection:
            self.connection.execute(UPDATE_BALANCE, (balance, number))

    def get_balance(self, number):
        with self.connection:
            return self.connection.execute(GET_BALANCE, (number,)).fetchone()

    def delete_card(self, number):
        with self.connection:
            self.connection.execute(DELETE_CARD, (number,))

    @staticmethod
    def generate_luhn(digits):
        digits = [int(digit) for digit in digits]

        for i in range(len(digits)):
            if i % 2 == 0:
                digits[i] *= 2
                if digits[i] > 9:
                    digits[i] -= 9

        sum_digits = sum(digits)
        rounded_sum_digits = (sum_digits + 9) // 10 * 10

        return str(rounded_sum_digits - sum_digits)

    def main_menu(self):

        while (user_main_input := input(MAIN_MENU_PROMPT)) != '0':

            # create account
            if user_main_input == '1':
                self.prompt_add_card()

            # log in to account
            elif user_main_input == '2':
                self.prompt_login_to_account()

        exit()

    def account_menu(self, card_number):
        while (user_account_input := input(ACCOUNT_MENU_PROMPT)) != '0':

            # get balance
            if user_account_input == '1':
                balance = self.get_balance(card_number)
                print(f'Balance: {balance[0]}\n')

            # update balance
            elif user_account_input == '2':
                balance = self.get_balance(card_number)
                self.update_balance(card_number, balance[0] + int(input('Enter income:\n')))
                print('Income was added!')

            # transfer money
            elif user_account_input == '3':
                self.transfer(card_number)

            # delete account
            elif user_account_input == '4':
                self.delete_card(card_number)
                print('The account has been closed!')
                self.main_menu()

            elif user_account_input == '5':
                self.main_menu()

        exit()

    # create and add card to the DB
    def prompt_add_card(self):
        account_number = '400000' + str(rnd(100000000, 999999999))
        checksum = self.generate_luhn(account_number)
        card_number = account_number + checksum
        pin = format(rnd(0000, 9999), '04d')
        print('Your card has been created\nYour card number:\n')
        print(f'{card_number}')
        print('Your card PIN:')
        print(pin + '\n')
        self.add_card(card_number, pin)

    # login to account
    def prompt_login_to_account(self):
        card_number = input('Enter your card number:\n')
        card_pin = input('Enter your PIN:\n')
        card = self.get_card_by_number(card_number)
        if card is not None and card_pin == card[2]:
            print('\nYou have successfully logged in!\n')
            self.account_menu(card_number)
        else:
            print('Wrong card number or PIN!')
            self.main_menu()

    def transfer(self, card_number):
        print('Transfer')

        transfer_card_number = None

        while not self.check_card_number(transfer_card_number):
            transfer_card_number = input('Enter card number:\n')

        transfer_amount = int(input('Enter how much money you want to transfer:\n'))
        balance = self.get_balance(card_number)

        if balance[0] < transfer_amount:
            print('Not enough money!')
        else:
            print('Success!')
            balance = self.get_balance(transfer_card_number)
            self.update_balance(transfer_card_number, balance[0] + transfer_amount)
            balance = self.get_balance(card_number)
            self.update_balance(card_number, balance[0] - transfer_amount)

    def check_card_number(self, transfer_card_number):

        if transfer_card_number is None:
            return False

        card_number = transfer_card_number[:-1]
        valid_luhn_number = self.generate_luhn(card_number)

        if valid_luhn_number != transfer_card_number[-1]:
            print('Probably you made a mistake in the card number. Please try again!')
            return False

        card = self.get_card_by_number(transfer_card_number)

        if card is not None:
            return True
        else:
            print('Such a card does not exist.')
            return False


BankingSystem()
