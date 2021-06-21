numbers = []

number = int(input())

numbers.append(number)

while sum(numbers) != 0:
    number = int(input())
    numbers.append(number)

result = 0

for number in numbers:
    result += number * number

print(f'{result}')
