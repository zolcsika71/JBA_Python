from itertools import combinations_with_replacement
import random as rnd
import numpy as np


class Dominoes:

    def __init__(self):
        self.stock = []
        self.computer_stock = []
        self.player_stock = []
        self.snake = []
        self.current_player = None
        self.winner = None

    def run(self):
        self.make_stocks()
        self.play()
        while self.game_state():
            self.play()

        self.display()
        print('Status: The game is over. ', end='')
        if self.winner == 'player':
            print('You won!')
        elif self.winner == 'computer':
            print('The computer won!')
        else:
            print("It's a draw!")

    def play(self):
        self.display()
        if self.current_player == 'player':
            self.player_input()
        else:
            self.computer_input()

    def player_input(self, display=True):
        if display:
            print("\nStatus: It's your turn to make a move. Enter your command.")

        idx = input()

        if idx.lstrip("-").isdigit():
            idx = int(idx)
            if (self.current_player == 'player' and len(self.player_stock) >= abs(idx)) \
                    or (self.current_player == 'computer' and len(self.computer_stock) >= abs(idx)):
                self.manage_snake(idx)
            else:
                print('Invalid input. Please try again.')
                self.player_input(False)

        else:
            print('Invalid input. Please try again.')
            self.player_input(False)

    def computer_input(self, display=True):
        if display:
            input("\nStatus: Computer is about to make a move. Press Enter to continue...")

        max_scores_idx = self.count_scores()

        domino_found = False

        for idx in max_scores_idx:
            if not self.manage_snake(idx):
                if self.manage_snake(-idx):
                    domino_found = True
                    break
            else:
                domino_found = True
                break

        if not domino_found:
            self.manage_snake(0)

    def count_scores(self):
        scores = []
        for idx in range(len(self.computer_stock)):
            domino = self.computer_stock[idx]
            score = self.domino_score(domino)
            scores.append({'idx': idx, 'score': score})

        scores = sorted(scores, key=lambda k: k['score'], reverse=True)
        max_scores_idx_ = [domino['idx'] + 1 for domino in scores]

        return max_scores_idx_

    def domino_score(self, domino_):
        all_dominoes = self.snake + self.computer_stock
        count = [row.count(domino_[0]) for row in all_dominoes]
        score = sum(count)
        count = [row.count(domino_[1]) for row in all_dominoes]
        score += sum(count)
        return score

    def make_stocks(self):
        numbers = [0, 1, 2, 3, 4, 5, 6]
        pairs = list(combinations_with_replacement(numbers, 2))
        self.stock = [list(element) for element in pairs]
        self.computer_stock = []
        self.player_stock = []
        rnd.shuffle(self.stock)
        for i in range(7):
            self.computer_stock.append(self.stock.pop())
            self.player_stock.append(self.stock.pop())

        self.manage_first_snake()

    def manage_first_snake(self):
        computer_max = None
        player_max = None

        computer_doubles = np.array([domino for domino in self.computer_stock if domino[0] == domino[1]])

        if len(computer_doubles) > 0:
            computer_max = np.max(computer_doubles)

        player_doubles = np.array([domino for domino in self.player_stock if domino[0] == domino[1]])

        if len(player_doubles) > 0:
            player_max = np.max(player_doubles)

        if computer_max is None and player_max is None:
            self.make_stocks()

        # get snake
        elif computer_max is None:
            self.add_first_snake('player', player_max)
        elif player_max is None:
            self.add_first_snake('computer', computer_max)
        elif player_max > computer_max:
            self.add_first_snake('player', player_max)
        elif computer_max > player_max:
            self.add_first_snake('computer', computer_max)

    def add_first_snake(self, player, max_score):
        self.current_player = player
        if player == 'player':
            idx = self.player_stock.index([max_score, max_score])
        else:
            idx = self.computer_stock.index([max_score, max_score])

        self.add_to_snake(idx, False)

    def manage_snake(self, idx):
        if idx < 0:
            idx = abs(idx) - 1
            legal_move = self.fit_to_snake(idx)
            if legal_move:
                self.add_to_snake(idx)
        elif idx > 0:
            idx = idx - 1
            legal_move = self.fit_to_snake(idx, False)
            if legal_move:
                self.add_to_snake(idx, False)
        else:
            legal_move = True
            if len(self.stock) > 0:
                rnd.shuffle(self.stock)
                if self.current_player == 'player':
                    self.player_stock.append(self.stock.pop())
                else:
                    self.computer_stock.append(self.stock.pop())
            self.change_player()

        if not legal_move:
            if self.current_player == 'player':
                print('Illegal move. Please try again.')
                self.player_input(False)
            else:
                return False

        else:
            return True

    def fit_to_snake(self, idx, insert=True):
        if self.current_player == 'player':
            array = self.player_stock
        elif self.current_player == 'computer':
            array = self.computer_stock
        else:
            return False

        domino = array[idx]

        if insert:
            if self.snake[0][0] == domino[0]:
                domino = domino[::-1]
                array[idx] = domino
                return True
            elif self.snake[0][0] == domino[1]:
                return True

        else:
            if self.snake[-1][1] == domino[1]:
                domino = domino[::-1]
                array[idx] = domino
                return True
            elif self.snake[-1][1] == domino[0]:
                return True

        return False

    def add_to_snake(self, idx, insert=True):
        if self.current_player == 'player':
            domino = self.player_stock.pop(idx)
        else:
            domino = self.computer_stock.pop(idx)

        if insert:
            self.snake.insert(0, domino)
        else:
            self.snake.append(domino)

        self.change_player()

    def game_state(self):
        if len(self.player_stock) == 0:
            self.winner = 'player'
            return False
        elif len(self.computer_stock) == 0:
            self.winner = 'computer'
            return False
        else:
            return self.game_state_snake()

    def game_state_snake(self):
        if len(self.snake) > 1:
            starter = self.snake[0][0]
            end = self.snake[-1][1]
            if end == starter:
                count = [row.count(starter) for row in self.snake]
                count = sum(count)
                if count >= 8:
                    self.winner = 'draw'
                    return False

        return True

    def change_player(self):
        if self.current_player == 'player':
            self.current_player = 'computer'
        else:
            self.current_player = 'player'

    def display(self):
        print('=' * 70)
        print(f'Stock size: {len(self.stock)}')
        print(f'Computer pieces: {len(self.computer_stock)}\n')
        self.print_snake()
        self.print_player()

    def print_player(self):
        print('\n')
        print(f'Your pieces:')
        for idx in range(len(self.player_stock)):
            print(f'{idx + 1}: {self.player_stock[idx]}')

    def print_snake(self):
        snake_length = len(self.snake)
        if snake_length <= 6:
            for snake in self.snake:
                print(f'{snake}', end='')
        else:
            for i in range(3):
                print(f'{self.snake[i]}', end='')
            print('...', end='')
            for i in range(snake_length - 3, snake_length):
                print(f'{self.snake[i]}', end='')


if __name__ == "__main__":
    dominoes = Dominoes()
    dominoes.run()
