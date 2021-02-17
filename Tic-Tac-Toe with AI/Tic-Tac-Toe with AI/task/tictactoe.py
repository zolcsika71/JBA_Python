import random
import sys

DEBUG = False
GAME_SIZE = 3
MATRIX_SIZE = GAME_SIZE + 2
MATRIX_LENGTH = MATRIX_SIZE - 1


def rnd(n, b=0):
    return int(round(random.random() * (b - n) + n, 0))


def get_game_mode():
    game_mode_ = str(input('Input command: ')).split(' ')

    if game_mode_[0] == 'exit' \
            or (len(game_mode_) == 3
                and game_mode_[0] == 'start'
                and game_mode_[1] in ['user', 'easy', 'medium']
                and game_mode_[2] in ['user', 'easy', 'medium']):

        return game_mode_
    else:
        print('Bad parameters!')
        return False


class Matrix:

    def __init__(self, size_):
        self.size = size_
        self.matrix = []
        for row in range(self.size):
            self.matrix.append([
                '| ' if (column == 0 or column == MATRIX_LENGTH) and row != 0 and row != MATRIX_LENGTH
                else '--' if column < MATRIX_LENGTH and (row == 0 or row == MATRIX_LENGTH)
                else '-' if row == 0 or row == MATRIX_LENGTH else '  ' for column in range(self.size)
            ])

        if DEBUG:
            self.init_table()

    def __getitem__(self, index):
        return self.matrix[index]

    # define test table
    def init_table(self):
        line_ = '_OO_XO_XX'
        x = 1
        y = 1

        for char in line_:
            if char == '_':
                char = ' '
            self[x][y] = char + ' '
            if y == GAME_SIZE:
                y = 1
                x += 1
            else:
                y += 1

    def print(self):
        for row in range(MATRIX_SIZE):
            for column in range(MATRIX_SIZE):
                print(self[row][column], end='')
            print('\r')

    def empty_cell(self, coords):
        return self.matrix[int(coords[0])][int(coords[1])] == '  '

    def make_move(self, coords, char):
        cell = self.matrix[int(coords[0])][int(coords[1])]
        if cell == '  ':
            self.matrix[int(coords[0])][int(coords[1])] = char + ' '
            return True
        else:
            print(f'cell {int(coords[0])}, {int(coords[1])} is already occupied')
            print(self.matrix[int(coords[0])][int(coords[1])])
            return False

    def user_action(self, user_char):

        try:
            x, y = map(int, input('Enter the coordinates:').split())
            user_input = [str(x), str(y)]
            # check if it is in '123'
            if all(char in '123' for char in user_input):
                # check if cell is not occupied
                coords = [int(user_input[0]), int(user_input[1])]
                if self.empty_cell(coords):
                    self.make_move(coords, user_char)
                    return True
                else:
                    print('This cell is occupied! Choose another one!')
                    return False
            else:
                print('Coordinates should be from 1 to 3!')
                return False
        except ValueError:
            print('You should enter numbers!')
            return False

    def ai_action(self, level, ai_char):

        def easy_ai_action():

            def get_all_empty_cells():
                # check empty cells
                empty_cells_ = []

                for row in range(1, MATRIX_LENGTH):
                    for column in range(1, MATRIX_LENGTH):
                        if self.empty_cell([row, column]):
                            empty_cells_.append([row, column])

                return empty_cells_

            empty_cells = get_all_empty_cells()

            target_cell = empty_cells[rnd(0, len(empty_cells) - 1)]
            target = [target_cell[0], target_cell[1]]
            self.make_move(target, ai_char)

            print('Making move level "easy"')

        def medium_ai_action():

            results_array = self.get_result_array(True)
            action_made = False

            def user_char():
                if ai_char == 'X':
                    return 'O'
                else:
                    return 'X'

            def count_chars(list_):
                dict_ = {}
                for j in set(list_):
                    dict_[j] = list_.count(j)

                return dict_

            def make_move(type_index, array_index, empty_cell_index):
                # check rows
                if type_index == 0:
                    target = [array_index + 1, empty_cell_index]
                    return self.make_move(target, ai_char)
                # check columns
                elif type_index == 1:
                    target = [empty_cell_index, array_index + 1]
                    return self.make_move(target, ai_char)
                # check diagonals
                elif type_index == 2:
                    if array_index == 0:
                        target = [empty_cell_index, empty_cell_index]
                    else:
                        target = [empty_cell_index, array_index]

                    return self.make_move(target, ai_char)

            def win_or_block(dict_, type_index, array_index, empty_cell_index, char):

                if char + ' ' in dict_ and '  ' in dict_ and dict_[char + ' '] == 2 and dict_['  '] == 1:
                    # try make a move
                    return make_move(type_index, array_index, empty_cell_index)

            def action_can_be_made(results_index):

                for j in range(len(results_array[results_index])):
                    current_array = results_array[results_index][j]
                    dict_ = count_chars(current_array)
                    try:
                        empty_cell_index = current_array.index('  ') + 1
                    except ValueError:
                        return False

                    # check moves
                    for char in [ai_char, user_char()]:
                        if win_or_block(dict_, results_index, j, empty_cell_index, char):
                            if char == ai_char:
                                print('win moves made')
                            else:
                                print('block moves made')
                            return True

                return False

            for i in range(len(results_array)):
                if action_can_be_made(i):
                    action_made = True
                    print('Making move level "medium"')
                    break

            if not action_made:
                easy_ai_action()

        if level == 'easy':
            easy_ai_action()
        if level == 'medium':
            medium_ai_action()

    def get_result_array(self, separated=False):

        # get column[i] from 2D array
        def column(i):
            return [row_[i] for row_ in self]

        rows = []
        columns = []
        for row in range(1, MATRIX_LENGTH):
            rows.append(self[row][1:-1])
            columns.append(column(row)[1:-1])

        diagonals = [
            [self[row][row] for row in range(1, MATRIX_LENGTH)],
            [self[row][MATRIX_LENGTH - row] for row in range(1, MATRIX_LENGTH)]
        ]

        if not separated:
            temp_array = []
            temp_array.extend(rows)
            temp_array.extend(columns)
            temp_array.extend(diagonals)

            return temp_array

        else:
            return [rows, columns, diagonals]

    def winner(self):

        def count_result(result_):
            if all(char[0] == 'X' for char in result_):
                return 'X'
            elif all(char[0] == 'O' for char in result_):
                return 'O'
            else:
                return False

        def get_results():

            results_array = self.get_result_array()

            for result in results_array:
                return_value = count_result(result)
                if return_value:
                    return return_value

            return False

        return get_results()

    def table_full(self):

        # get the sub matrix (the real table)
        game_table = [(self[row][1:-1]) for row in range(1, MATRIX_LENGTH)]

        # get elements from sub matrix
        elements = [cell for row in game_table for cell in row]

        return all(True if element in ['X ', 'O '] else False for element in elements)

    def get_game_state(self):
        winner = self.winner()
        table_full = self.table_full()
        if winner:
            print(f'{winner} wins')
            return True
        elif table_full:
            print('Draw')
            return True
        else:
            return False


class Game:

    def __init__(self):
        self.table = Matrix(MATRIX_SIZE)
        self.players = []
        self.end_game = False

    def init(self):
        game_mode = False
        while not game_mode:
            game_mode = get_game_mode()

        if game_mode[0] == 'exit':
            sys.exit()

        # init players [[player, player_char]]
        self.players = [[game_mode[1], 'X'], [game_mode[2], 'O']]

        # print init table
        self.table.print()

    def play(self):
        while True:

            for player in self.players:

                if player[0] == 'user':
                    # player action
                    while not self.table.user_action(player[1]):
                        self.table.user_action(player[1])
                else:
                    # ai action
                    self.table.ai_action(player[0], player[1])

                self.table.print()

                # True if game over and prints the result
                if self.table.get_game_state():
                    self.end_game = True
                    break

            if self.end_game:
                break


tic_tac_toe = Game()

tic_tac_toe.init()
tic_tac_toe.play()
