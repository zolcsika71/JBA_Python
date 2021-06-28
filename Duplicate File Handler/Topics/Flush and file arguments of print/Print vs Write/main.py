numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
numbers_string = str(numbers)

with open('file_with_list.txt', 'w+') as f:
    f.write(numbers_string)
