name = input()


def normalize(name_):
    replace_char = {
        'é': 'e',
        'ë': 'e',
        'á': 'a',
        'å': 'a',
        'œ': 'oe',
        'æ': 'ae'
    }

    new_name = ''

    for char in name_:
        for key in replace_char.keys():
            if key == char:
                new_name = name_.replace(char, replace_char[key])

    return new_name


print(normalize(name))
