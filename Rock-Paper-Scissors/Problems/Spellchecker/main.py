dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word_input = str(input())
result = 'Incorrect'


for word in dictionary:
    if word == word_input:
        result = 'Correct'

print(result)
