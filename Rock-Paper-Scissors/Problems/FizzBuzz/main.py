for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print(f'FizzBuzz')
    elif i % 5 == 0:
        print(f'Buzz')
    elif i % 3 == 0:
        print(f'Fizz')
    else:
        print(f'{i}')
