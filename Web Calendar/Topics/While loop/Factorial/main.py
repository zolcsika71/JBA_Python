import sys

n = int(input())

factorial = 1
counter = 1

if n == 0:
    factorial = 0
else:
    while n >= counter:
        factorial = factorial * counter
        counter += 1

print(factorial)
