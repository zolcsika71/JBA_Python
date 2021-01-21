income = int(input())
tax_percent = 0

if income >= 132407:
    tax_percent = 28
elif income >= 42708:
    tax_percent = 25
elif income >= 15528:
    tax_percent = 15
else:
    tax_percent = 0

print(f'The tax for {income} is {tax_percent}%. That is {int(round(income / 100 * tax_percent))} dollars!')


