number = int(input())
word = input()

# write a condition for plurals
if number == 0 or number > 1:
    word = word + 's'

print(number, word)
