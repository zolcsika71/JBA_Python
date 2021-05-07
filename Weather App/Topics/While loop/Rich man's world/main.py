deposit = int(input())
counter = 0

while deposit <= 700000:
    deposit += deposit * 7.1 / 100
    counter += 1

print(counter)
