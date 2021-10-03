import math

a = int(input())

print(round(math.exp(a / (math.exp(a) + 1)), 2))
