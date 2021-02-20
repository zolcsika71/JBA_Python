import random
import sys
from collections import Counter

GAME_SIZE = 3
MATRIX_SIZE = GAME_SIZE + 2
MATRIX_LENGTH = MATRIX_SIZE - 1


def rnd(n, b=0):
    return int(round(random.random() * (b - n) + n, 0))


class Table:

    def __init__(self, table):
        self.table = table
        self.table_coords = \
            {
                '11': 0,
                '12': 1,
                '13': 2,
                '21': 3,
                '22': 4,
                '23': 5,
                '31': 6,
                '32': 7,
                '33': 8
            }

    def write_table(self, coords, char):
        if self.empty_cell(coords):
            self.table[self.table_coords[coords]] = char
            return True
        else:
            print(f'cell {(coords[0])}, {(coords[1])} is already occupied with {self.read_table(coords)}')
            return False

    def read_table(self, coords):
        return self.table[self.table_coords[coords]]

    def empty_cell(self, coords):
        return self.table[self.table_coords[coords]] == ' '

    def empty_cells_indexes(self):
        return [cell for cell in range(len(self.table)) if self.table[cell] == ' ']

    def table_full(self):
        return all(cell != ' ' for cell in self.table)

    def table_array(self):

        rows = [
            [self.table[0], self.table[1], self.table[2]],
            [self.table[3], self.table[4], self.table[5]],
            [self.table[6], self.table[7], self.table[8]]
        ]
        columns = [
            [self.table[0], self.table[3], self.table[6]],
            [self.table[1], self.table[4], self.table[7]],
            [self.table[2], self.table[5], self.table[8]]

        ]
        diagonals = [
            [self.table[0], self.table[4], self.table[8]],
            [self.table[2], self.table[4], self.table[6]]
        ]

        return [rows, columns, diagonals]


class Player(Table):

    def __init__(self, name, char, table):
        super().__init__(table)
        self.name = name
        self.char = char
        self.function_calls = 0

    def play(self):
        if self.name == 'user':
            self.user_action()
        else:
            self.ai_action()

    def opponent_char(self):
        if self.char == 'X':
            return 'O'
        else:
            return 'X'

    def winning(self, player, display=False):
        for lines in self.table_array():
            for line in lines:
                if all(char == player for char in line):
                    if display:
                        print(f'{player} wins')
                    return True

        return False

    def game_state(self):
        if self.table_full():
            print('Draw')
            return True

        return self.winning(self.char, True)

    def user_action(self):
        try:
            x, y = map(int, input('Enter the coordinates:').split())
            user_input = [str(x), str(y)]
            # check if it is in '123'
            if all(char in '123' for char in user_input):
                # check if cell is not occupied
                coords = str(user_input[0]) + str(user_input[1])
                if not self.write_table(coords, self.char):
                    self.user_action()
            else:
                print('Coordinates should be from 1 to 3!')
                self.user_action()
        except ValueError:
            print('You should enter numbers!')
            self.user_action()

    def ai_action(self):

        def easy_ai_action():
            empty_cells = self.empty_cells_indexes()
            target_cell = empty_cells[rnd(0, len(empty_cells) - 1)]
            self.table[target_cell] = self.char
            print('Making move level "easy"')

        def medium_ai_action():

            def make_move(type_index_, array_index_, empty_cell_index_):
                # check rows
                if type_index_ == 0:
                    coords = str(array_index_ + 1) + str(empty_cell_index_)
                    return self.write_table(coords, self.char)
                # check columns
                elif type_index_ == 1:
                    coords = str(empty_cell_index_) + str(array_index_ + 1)
                    return self.write_table(coords, self.char)
                # check diagonals
                elif type_index_ == 2:
                    if array_index_ == 0:
                        coords = str(empty_cell_index_) + str(empty_cell_index_)
                    else:
                        coords = str(empty_cell_index_) + str(MATRIX_LENGTH - empty_cell_index_)

                    return self.write_table(coords, self.char)

            def ai_move():
                chars = [self.char, self.opponent_char()]
                table_array = self.table_array()

                for type_index in range(len(table_array)):
                    for array_index in range(len(table_array[type_index])):
                        char_counter = dict(Counter(table_array[type_index][array_index]))
                        for char in chars:
                            if char in char_counter \
                                    and ' ' in char_counter \
                                    and char_counter[char] == 2 \
                                    and char_counter[' '] == 1:
                                empty_cell_index = table_array[type_index][array_index].index(' ') + 1
                                if make_move(type_index, array_index, empty_cell_index):
                                    print('Making move level "medium"')
                                    return True

                return False

            return ai_move()

        def hard_ai_action():

            ai_player = self.char
            hu_player = self.opponent_char()

            def minimax(player):

                self.function_calls += 1

                empty_cells_indexes = self.empty_cells_indexes()

                if self.winning(hu_player):
                    return {'score': -10}
                elif self.winning(ai_player):
                    return {'score': 10}
                elif self.table_full():
                    return {'score': 0}

                moves = []

                for index in empty_cells_indexes:

                    move = {'index': index}

                    # player move to an empty cell
                    self.table[index] = player

                    if player == ai_player:
                        result = minimax(hu_player)
                        move['score'] = result['score']
                    else:
                        result = minimax(ai_player)
                        move['score'] = result['score']

                    # reset cell
                    self.table[index] = ' '

                    moves.append(move)

                best_move = None

                if player == ai_player:
                    best_score = -10000
                    for i in range(len(moves)):
                        if moves[i]['score'] > best_score:
                            best_score = moves[i]['score']
                            best_move = i
                else:
                    best_score = 10000
                    for i in range(len(moves)):
                        if moves[i]['score'] < best_score:
                            best_score = moves[i]['score']
                            best_move = i

                return moves[best_move]

            best_spot = minimax(ai_player)

            self.table[best_spot['index']] = ai_player

            print(f'Making move level "hard" fc: {self.function_calls}')

        if self.name == 'easy':
            easy_ai_action()
        elif self.name == 'medium':
            if not medium_ai_action():
                easy_ai_action()
        else:
            hard_ai_action()


class Matrix(Table):

    def __init__(self, size_, table):
        super().__init__(table)
        self.size = size_
        self.matrix = []
        for row in range(self.size):
            self.matrix.append([
                '| ' if (column == 0 or column == MATRIX_LENGTH) and row != 0 and row != MATRIX_LENGTH
                else '--' if column < MATRIX_LENGTH and (row == 0 or row == MATRIX_LENGTH)
                else '-' if row == 0 or row == MATRIX_LENGTH else '  ' for column in range(self.size)
            ])

    def __getitem__(self, index):
        return self.matrix[index]

    def update_table(self):
        x = 1
        y = 1

        for char in self.table:
            self[x][y] = char + ' '
            if y == GAME_SIZE:
                y = 1
                x += 1
            else:
                y += 1

    def print(self):
        self.update_table()
        for row in range(MATRIX_SIZE):
            for column in range(MATRIX_SIZE):
                print(self[row][column], end='')
            print('\r')


class Game(Matrix):

    def get_game_mode(self):
        game_mode_ = str(input('Input command: ')).split(' ')

        if game_mode_[0] == 'exit' \
                or (len(game_mode_) == 3
                    and game_mode_[0] == 'start'
                    and game_mode_[1] in ['user', 'easy', 'medium', 'hard']
                    and game_mode_[2] in ['user', 'easy', 'medium', 'hard']):

            return game_mode_
        else:
            print('Bad parameters!')
            self.get_game_mode()

    table = [' ' for i in range(GAME_SIZE ** 2)]

    def __init__(self, size_):
        super().__init__(size_, Game.table)
        game_mode = Game.get_game_mode(self)

        if game_mode is None:
            sys.exit()

        self.player_1 = Player(game_mode[1], 'X', self.table)
        self.player_2 = Player(game_mode[2], 'O', self.table)
        self.players = [self.player_1, self.player_2]
        self.end_game = False

        self.print()

    def play(self):
        while True:

            for player in self.players:
                player.play()

                self.print()

                # True if game over
                if player.game_state():
                    self.end_game = True
                    break

            if self.end_game:
                break


tic_tac_toe = Game(MATRIX_SIZE)
tic_tac_toe.play()
