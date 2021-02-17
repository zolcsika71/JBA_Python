def tallest_people(**people):
    max_value = max(people.values())
    max_dict_array = [{k: v} for k, v in people.items() if v == max_value]
    max_dict_array.sort(key=lambda d: list(d.keys()))

    for person in max_dict_array:
        for k, v in person.items():
            print(f'{k} : {v}')

