def morning(func):
    def wrapper(arg):
        func(arg)
        print('Good morning, ' + arg)

    return wrapper



