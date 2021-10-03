import string

text = 'ACCD'

a = 3
m = 13
uppercase_letters = string.ascii_uppercase
hash_dict = {}
hash_text_dict = {}
counter = 1
powered = 0
hash_result = 0

for letter in uppercase_letters:
    hash_dict[letter] = counter
    counter += 1

for letter in text:
    hash_result += hash_dict[letter] * pow(a, powered)
    powered += 1

hash_result = hash_result % m

print(hash_result)
