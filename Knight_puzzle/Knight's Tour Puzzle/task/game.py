import time

MOVE_OFFSETS = (
    (-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2),
)


class Cell:
    def __init__(self, char, positions):
        self.current = False
        self.visited = False
        self.char = char
        self.knight_pos = positions


class Board:
    def __init__(self, dimension_):
        self.column = dimension_[0]
        self.row = dimension_[1]
        self.cell_size = len(str(self.column * self.row))
        self.board = {}

    @staticmethod
    def position(col, row):
        return str(col) + str(row)

    def init_board(self):
        for row in range(1, self.row + 1):
            for column in range(1, self.column + 1):
                positions = set([pos for pos in self.legal_moves_from(column, row)])
                self.board[self.position(column, row)] = Cell(self.format_char('_'), positions)

    def legal_moves_from(self, col, row):
        for row_offset, col_offset in MOVE_OFFSETS:
            move_row, move_col = row + row_offset, col + col_offset
            if 1 <= move_row <= self.row and 1 <= move_col <= self.column:
                yield self.position(move_col, move_row)

    def format_char(self, char):
        if char == '_':
            return '_' * self.cell_size
        else:
            return ' ' * (self.cell_size - len(char)) + char

    def write_current(self, curr_pos, next_pos=None):
        if next_pos is None:
            self.board[curr_pos].current = True
            self.board[curr_pos].char = self.format_char('X')
        else:
            self.board[next_pos].current = True
            self.board[curr_pos].current = False
            self.board[curr_pos].visited = True

            self.board[curr_pos].char = self.format_char('*')
            self.board[next_pos].char = self.format_char('X')

    def manage_knights(self, curr_pos, next_pos=None):
        if next_pos is None:
            self.write_knights(curr_pos)
        else:
            self.write_knights(curr_pos, '_')
            self.write_knights(next_pos)

    def possible_moves(self, position, length=True):
        positions = self.board[position].knight_pos
        possible_moves = set([move for move in positions
                              if not self.board[move].current
                              and not self.board[move].visited])
        if length:
            return len(possible_moves)
        else:
            possible_moves = sorted(possible_moves, key=lambda x: len(self.board[x].knight_pos))
            return possible_moves

    def write_knights(self, position, char=None):
        for pos in self.board[position].knight_pos:
            if not self.board[pos].current and not self.board[pos].visited:
                if char is not None:
                    self.board[pos].char = self.format_char(char)
                else:
                    self.board[pos].char = self.format_char(str(self.possible_moves(pos)))

    def border_line(self):
        if self.cell_size == 1:
            print(' ' + '-' * (self.column * (self.cell_size + 1) + 3))
        else:
            print(' ' * (self.cell_size - 1) + '-' * (self.column * (self.cell_size + 1) + 3))

    def print_board(self):

        # upper border line
        self.border_line()

        for row in range(self.row, 0, - 1):
            # print rows number
            if self.row >= 10 > row:
                print(f' {row}| ', end='')
            else:
                print(f'{row}| ', end='')

            # print table
            for column in range(1, self.column + 1):
                print(f'{self.board[self.position(column, row)].char} ', end='')

            print('|', end='')
            print('\r')

        # lower border line
        self.border_line()

        # print column number
        print(' ' * 2 if self.row < 10 else ' ' * 3, end='')
        for i in range(1, self.column + 1):
            if i < 10:
                print(' ' * self.cell_size, end='')
            else:
                print(' ' * (self.cell_size - 1), end='')

            print(f'{i}', end='')


class Game(Board):
    def __init__(self):
        self.next = None
        self.moves = 0
        self.dimension = self.get_dimension()
        super().__init__(self.dimension)
        self.board_size = self.row * self.column
        self.current = self.get_starter()
        self.type = self.get_game_type()

    def run(self):
        if not self.type:
            self.run_computer()
        else:
            if self.run_computer(True):
                self.run_player()

    def run_computer(self, check=False):
        self.init_board()
        self.board[self.current].char = self.format_char('1')
        self.board[self.current].visited = True
        start = time.time()
        have_solution = self.find_solution(self.current, 2)
        if have_solution:
            if not check:
                print("Here's the solution!")
                self.print_board()
            else:
                return True
        else:
            print('No solution exists!')

        end = time.time()

        print(f'\n{end - start}')

    def find_solution(self, position, counter):
        knight_positions = self.possible_moves(position, False)
        if counter < self.board_size + 1:
            for k_pos in knight_positions:
                self.board[k_pos].char = self.format_char(str(counter))
                self.board[k_pos].visited = True
                if self.find_solution(k_pos, counter + 1):
                    return True
                self.board[k_pos].char = self.format_char('_')
                self.board[k_pos].visited = False

            return False

        return True

    def run_player(self):
        self.init_board()
        self.write_current(self.current)
        self.manage_knights(self.current)
        self.print_board()
        while True:
            if self.next is not None and self.possible_moves(self.next) == 0:
                break
            self.next = self.get_player()
            self.write_current(self.current, self.next)
            self.manage_knights(self.current, self.next)
            self.current = self.next
            self.print_board()

        if self.column * self.row == self.moves:
            print('\n\nWhat a great tour! Congratulations!')
        else:
            print('\n\nNo more possible moves!')
            print(f'Your knight visited {self.moves} squares!')

    def valid_data(self, data, pos_check=False, possible_check=False):
        # number of data
        if len(data) != 2:
            return False
        # is it number
        elif not data[0].isdigit() or not data[1].isdigit():
            return False
        # is it negative
        elif int(data[0]) < 1 or int(data[1]) < 1:
            return False
        # is it in dimension
        if pos_check:
            if int(data[0]) > self.dimension[0] or int(data[0]) < 1 \
                    or int(data[1]) > self.dimension[1] or int(data[1]) < 1:
                return False
        # is it in possible moves
        if possible_check:
            data = self.position(data[0], data[1])
            if data not in self.board[self.current].knight_pos \
                    or self.board[data].current or self.board[data].visited:
                return False

        return True

    def get_dimension(self):

        dimension = input('Enter your board dimensions:').split()
        if self.valid_data(dimension):
            return [int(dim) for dim in dimension]
        else:
            print('Invalid dimensions!')
            return self.get_dimension()

    def get_game_type(self):
        game_type = input('Do you want to try the puzzle? (y/n):')
        if game_type == 'y':
            return True
        elif game_type == 'n':
            return False
        else:
            print('Invalid option')
            return self.get_game_type()

    def get_starter(self):
        self.moves += 1
        move = input("Enter the knight's starting position:").split()
        if self.valid_data(move, True):
            return self.position(move[0], move[1])
        else:
            print('Invalid position!')
            return self.get_starter()

    def get_player(self, first_time=True):
        self.moves += 1
        move = input("\n\nEnter your next move:" if first_time else "Invalid move! Enter your next move:").split()
        if self.valid_data(move, True, True):
            return self.position(move[0], move[1])
        else:
            return self.get_player(False)


if __name__ == '__main__':
    knight = Game()
    knight.run()
