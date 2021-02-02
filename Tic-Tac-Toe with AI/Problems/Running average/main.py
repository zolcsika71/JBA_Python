string = str(input())
print([(int(string[i]) + int(string[i + 1])) / 2 for i in range(len(string) - 1)])
