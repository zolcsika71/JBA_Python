def startswith_capital_counter(names):
    counter = 0
    for name in names:
        if name[0].isupper():
            counter += 1
    return counter

