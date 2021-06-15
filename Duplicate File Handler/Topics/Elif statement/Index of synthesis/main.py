index = float(input())

if index < 2:
    print('Analytic')
elif 2 <= index <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
