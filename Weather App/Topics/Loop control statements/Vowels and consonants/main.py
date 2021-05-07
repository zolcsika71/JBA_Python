vowels = 'aeiou'

for char in input():
    if char.isalpha():
        if char in vowels:
            print('vowel')
        else:
            print('consonant')
    else:
        break
