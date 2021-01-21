# read sums.txt
file = open('sums.txt', 'r')

for line in file:
    operands = line.split(' ')
    print(f'{int(operands[0]) + int(operands[1])}')

file.close()
