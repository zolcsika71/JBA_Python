def exception_check(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('The Error!')


