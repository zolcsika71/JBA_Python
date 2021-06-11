prime_numbers = []

for number in range(2, 1000):
    if any([number % i == 0 for i in range(2, number - 1)]):
        continue
    else:
        prime_numbers.append(number)


