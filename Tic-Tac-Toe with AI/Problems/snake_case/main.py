word = str(input())

result_array = [char if char.islower() else '_' + char.lower() for char in word]

result_string = ''.join(map(str, result_array))

if result_string[0] == '_':
    result_string = result_string[1:]


print(f'{result_string}')
