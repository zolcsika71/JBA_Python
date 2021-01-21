def closest_higher_mod_5(x):
    while True:
        reminder = x % 5
        if reminder == 0:
            return x
        x += 1
