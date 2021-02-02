numbers = [int(n) for n in input()]
print(f'{[sum(numbers[:x + 1]) for x in range(len(numbers))]}')



