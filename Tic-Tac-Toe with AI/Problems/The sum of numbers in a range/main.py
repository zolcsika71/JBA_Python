def range_sum(numbers, start, end):
    return sum(number for number in numbers if start <= number <= end)


input_numbers = [int(x) for x in input().split()]

a, b = map(int, input().split())

print(range_sum(input_numbers, a, b))
