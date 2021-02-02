string = str(input())
numbers = [int(char) for char in string]
print(sum(numbers) / len(numbers))
