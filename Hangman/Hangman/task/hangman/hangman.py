# Write your code here
import random
import sys


class Game:

    first_run = True

    def __init__(self):
        self.answers = ['python', 'java', 'kotlin', 'javascript']
        self.answer = list(random.choice(self.answers))
        self.answer_masked = ['-' for i in range(len(self.answer))]
        self.lives = 8
        self.letters_tried = []
        self.letter = None

        if Game.first_run:
            print('H A N G M A N')

    def menu(self):
        menu = None

        while menu != 'exit' and menu != 'play':
            menu = str(input('Type "play" to play the game, "exit" to quit: '))

        if menu == 'play':
            if Game.first_run:
                Game.first_run = False
            else:
                Game.__init__(self)

            self.play()

        elif menu == 'exit':
            sys.exit()

    def get_input(self):

        print(f'{"".join(self.answer_masked)}')
        letter_ = str(input('Input a letter:'))

        if len(letter_) > 1:
            print('You should input a single letter\n')
            self.get_input()
        elif not (letter_.islower() and letter_.isalpha()):
            print('Please enter a lowercase English letter\n')
            self.get_input()
        else:
            self.letter = letter_

    def letter_tried(self, letter_found):
        if self.letter in self.letters_tried:
            print("You've already guessed this letter")
        else:
            self.letters_tried.append(self.letter)
            if not letter_found:
                self.lives -= 1
                print(f'lives: {self.lives}')

    def letter_found(self):

        letter_found = False

        for j in range(len(self.answer)):
            if self.answer[j] == self.letter:
                self.answer_masked[j] = self.letter
                letter_found = True

        if not letter_found:
            print(f"That letter doesn't appear in the word")

        return letter_found

    def play(self):

        while self.lives > 0:

            print()

            self.get_input()
            self.letter_tried(self.letter_found())

            # check if wins in game
            if '-' not in self.answer_masked:
                print('You guessed the word!')
                print('You survived!\n')
                self.menu()

        # check if wins in end_game
        if '-' not in self.answer_masked:
            print('You guessed the word!')
            print('You survived!\n')
        else:
            print('You lost!\n')

        self.menu()


hangman = Game()
hangman.menu()
