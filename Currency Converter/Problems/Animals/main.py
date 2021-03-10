# read animals.txt
animals_file = open('animals.txt', 'r')
# and write animals_new.txt
new_animals_file = open('animals_new.txt', 'w')

for animal in animals_file:
    new_animals_file.write(animal.rstrip() + ' ')

animals_file.close()
new_animals_file.close()
