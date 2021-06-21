number = 0
counter = 0
while True:
    data = input()
    if data == '.':
        break
    else:
        number += int(data)
        counter += 1

print(f'{number / counter}')
