# put your python code here
seq = str(input()).split()
number = int(input())

solution_indexes = []


for i in range(len(seq)):
    if int(seq[i]) == number:
        solution_indexes.append(str(i))

if len(solution_indexes) == 0:
    print(f'not found')
else:
    solution = ' '.join(solution_indexes)
    print(f'{solution}')

