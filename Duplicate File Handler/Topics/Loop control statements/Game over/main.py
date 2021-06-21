scores = input().split()
# put your python code here

correct = 0
incorrect = 0

for result in scores:
    if result == 'C':
        correct += 1
    else:
        incorrect += 1

    if incorrect == 3:
        break

print('You won' if incorrect < 3 else 'Game over')
print(f'{correct}')
