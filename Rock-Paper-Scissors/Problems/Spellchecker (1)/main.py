dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']


words = input().split()

found = False

for word in words:
    if word not in dictionary:
        print(word)
        found = True

if not found:
    print("OK")












