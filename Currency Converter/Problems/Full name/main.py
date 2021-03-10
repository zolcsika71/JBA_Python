f1 = open('name.txt')
f2 = open('surname.txt')
f3 = open('full_name.txt', 'w')

name = f1.read()
surname = f2.read()

full_name = name + ' ' + surname

f3.write(full_name)

with open('name.txt', 'r') as f1, \
        open('surname.txt', 'r') as f2, \
        open('full_name.txt', 'w') as f3:
    name = f1.read()
    surname = f2.read()
    full_name = name.strip() + ' ' + surname.strip()
    f3.write(full_name)
