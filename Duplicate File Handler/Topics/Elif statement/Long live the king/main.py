coord_x = int(input())
coord_y = int(input())


def moves(x, y):

    result = 0

    if x - 1 >= 1:
        result += 1
        if y + 1 <= 8:
            result += 1
        if y - 1 >= 1:
            result += 1

    if x + 1 <= 8:
        result += 1
        if y + 1 <= 8:
            result += 1
        if y - 1 >= 1:
            result += 1

    if y - 1 >= 1:
        result += 1

    if y + 1 <= 8:
        result += 1

    print(f'{result}')


moves(coord_x, coord_y)









