def compare(numerator, denominator):

    return f'{denominator != 0 and numerator / denominator == 0.5}'


a = int(input())
b = int(input())

print(compare(a, b))
