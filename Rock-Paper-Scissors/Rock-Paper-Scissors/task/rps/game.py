import random
import sys


def rnd(n, b=0):
    return int(round(random.random() * (b - n) + n, 0))


def get_player_name():
    name = str(input('Enter your name: '))
    print(f'Hello, {name}')
    return name


def get_player_init_score(name):

    file = open('rating.txt', 'r')

    for line in file:
        record = line.split(' ')
        if record[0].rstrip() == name:
            file.close()
            return int(record[1])
        else:
            file.close()
            return 0


def get_player_input(solutions, player_init_score, player_score):
    while True:
        solution = str(input())
        if solution == '!exit':
            print(f'Bye!')
            sys.exit()
        elif solution == '!rating':
            print(f'Your rating: {get_player_all_score(player_init_score, player_score)}')
        elif solution not in solutions:
            print(f'Invalid input')
        else:
            return solution


def get_rules():
    rules = str(input()).split(',')
    if len(rules) == 1:
        rules = ['rock', 'paper', 'scissors']

    print("Okay, let's start")

    return rules


def get_result(my_index, player_index, solutions_length_):

    better_solution_length = solutions_length_ // 2
    player_wins = False
    draw = my_index == player_index

    if not draw:
        for i in range(1, better_solution_length + 1):
            if player_index == (my_index + i) % solutions_length_:
                player_wins = True

    # player wins
    if player_wins:
        return 100
    # draw
    elif draw:
        return 50
    else:
        return 0


def get_player_all_score(player_init_score, player_score):
    return player_init_score + player_score


def print_result(my_solution, current_score):
    # player wins
    if current_score == 100:
        print(f'Well done. The computer chose {my_solution} and failed')
    # draw
    elif current_score == 50:
        print(f'There is a draw ({my_solution})')
    # me wins
    else:
        print(f'Sorry, but the computer chose {my_solution}')


def run():
    player_name = get_player_name()
    solutions = get_rules()
    solutions_length = len(solutions)
    player_init_score = get_player_init_score(player_name)
    player_score = 0

    while True:
        player_input = get_player_input(solutions, player_init_score, player_score)

        if player_input is not None:

            player_solution_index = solutions.index(player_input)
            my_solution_index = rnd(solutions_length - 1)

            player_current_score = get_result(my_solution_index, player_solution_index, solutions_length)
            player_score += player_current_score
            print_result(solutions[my_solution_index], player_current_score)


run()









