# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
print(f'{[n for n in my_numbers if n % 2 == 0]}')
