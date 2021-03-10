# work with these variables

eugene = set(input().split())
rose = set(input().split())

booth = eugene | rose

result_eugene = booth - rose

result_rose = booth - eugene

result = result_rose | result_eugene

print(result)
