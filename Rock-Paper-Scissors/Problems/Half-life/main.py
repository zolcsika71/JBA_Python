initial = int(input())
final = int(input())
half_counter = 0

while initial >= final:
    initial = initial / 2
    half_counter += 1

print(f'{half_counter * 12}')
