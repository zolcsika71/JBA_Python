file = open('test.txt', 'r')

for line in file:
    print(f'{line[0]}')

file.close()



