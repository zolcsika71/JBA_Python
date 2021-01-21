# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
print(f'{len(file.readlines())}')
file.close()
