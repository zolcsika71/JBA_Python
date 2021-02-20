def number_of_frogs(year):
    return 120 if year == 1 else 2 * (number_of_frogs(year - 1) - 50)
