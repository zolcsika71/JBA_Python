a = float(input())
b = float(input())
operator = str(input())

if operator == '+':
    print(a + b)
if operator == '-':
    print(a - b)
if operator == '/':
    if b == 0:
        print('Division by 0!')
    else:
        print(a / b)
if operator == '*':
    print(a * b)
if operator == 'mod':
    if b == 0:
        print('Division by 0!')
    else:
        print(a % b)
if operator == 'pow':
    print(pow(a, b))
if operator == 'div':
    if b == 0:
        print('Division by 0!')
    else:
        print(a // b)
