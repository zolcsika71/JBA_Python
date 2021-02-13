import random
import sys

GAME_SIZE = 3
MATRIX_SIZE = GAME_SIZE + 2
MATRIX_LENGTH = MATRIX_SIZE - 1


def rnd(n, b=0):
    return int(round(random.random() * (b - n) + n, 0))


def get_game_mode():
    game_mode_ = str(input('Input command: ')).split(' ')

    if game_mode_[0] == 'exit'\
            or (len(game_mode_) == 3
                and game_mode_[0] == 'start'
                and game_mode_[1] in ['user', 'easy']
                and game_mode_[2] in ['user', 'easy']):

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

    def __setitem__(self, index, char):
        self.matrix[index] = char

    def __getitem__(self, index):
        return self.matrix[index]

    # define test table
    # def init_table(self):
    #     line_ = 'XO_XXOOXX'
    #     x = 1
    #     y = 1
    #
    #     for char in line_:
    #         if char == '_':
    #             char = ' '
    #         self[x][y] = char + ' '
    #         if y == GAME_SIZE:
    #             y = 1
    #             x += 1
    #         else:
    #             y += 1

    def print(self):
        for row in range(MATRIX_SIZE):
            for column in range(MATRIX_SIZE):
                print(self[row][column], end='')
            print('\r')

    def user_move(self, user_char):

        try:
            x, y = map(int, input('Enter the coordinates:').split())
            user_input_ = [str(x), str(y)]
            # check if it is in '123'
            if all(char in '123' for char in user_input_):
                # check if cell is not occupied
                if self.matrix[int(user_input_[0])][int(user_input_[1])] == '  ':
                    self.matrix[int(user_input_[0])][int(user_input_[1])] = user_char + ' '
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

    def ai_move(self, ai_char, level='easy'):
        if level == 'easy':
            # check empty cells
            empty_cells = []

            for row in range(1, MATRIX_LENGTH):
                for column in range(1, MATRIX_LENGTH):
                    if self.matrix[row][column] == '  ':
                        empty_cells.append([row, column])

            target_cell = empty_cells[rnd(0, len(empty_cells) - 1)]
            self.matrix[target_cell[0]][target_cell[1]] = ai_char + ' '

            print('Making move level "easy"')

        else:
            print('This level is not defined')

    def winner(self):

        def count_result(result_):
            if all(char[0] == 'X' for char in result_):
                return 'X'
            elif all(char[0] == 'O' for char in result_):
                return 'O'
            else:
                return False

        def get_results():
            results_array = []

            # get column[i] from 2D array
            def column(i):
                return [row_[i] for row_ in self]

            for row in range(1, MATRIX_LENGTH):
                # row
                results_array.append(self[row][1:-1])
                # column
                results_array.append(column(row)[1:-1])

            # diagonal 1
            results_array.append([self[row][row] for row in range(1, MATRIX_LENGTH)])

            # diagonal 2
            results_array.append([self[row][MATRIX_LENGTH - row] for row in range(1, MATRIX_LENGTH)])

            for result in results_array:
                return_value = count_result(result)
                if return_value:
                    return return_value

            return False

        return get_results()

    def table_full(self):

        game_table = [(self[row][1:-1]) for row in range(1, MATRIX_LENGTH)]

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


game_mode = False

while not game_mode:
    game_mode = get_game_mode()

if game_mode[0] == 'exit':
    sys.exit()

table = Matrix(MATRIX_SIZE)
players = [[game_mode[1], 'X'], [game_mode[2], 'O']]
end_game = False

table.print()

while True:

    for player in players:

        if player[0] == 'user':
            while not table.user_move(player[1]):
                table.user_move(player[1])
        else:
            table.ai_move(player[1])

        table.print()

        if table.get_game_state():
            end_game = True
            break

    if end_game:
        break
