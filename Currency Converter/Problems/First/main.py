# read test_file.txt
file = open('test_file.txt', 'r', encoding='utf-16')
print(file.readlines()[0])
file.close()
