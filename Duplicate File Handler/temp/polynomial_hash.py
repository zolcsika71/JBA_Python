import string
import random

input_text = 'ABCD'
text_array = []

a = 3
m = 13
uppercase_letters = string.ascii_uppercase
hash_dict = {}
hash_text_dict = {}
counter = 1
powered = 0
hash_result = 0
continued = True

for letter in uppercase_letters:
    hash_dict[letter] = counter
    counter += 1

while continued:

    text = ''.join(random.sample(input_text, len(input_text)))

    for letter in text:
        hash_result += hash_dict[letter] * pow(a, powered)
        powered += 1

    hash_result = hash_result % m

    for key, value in hash_text_dict.items():
        if value == hash_result:
            print(text, key)
            continued = False
            break

    hash_text_dict[text] = hash_result

    powered = 0
    hash_result = 0
