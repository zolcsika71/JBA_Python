# create the planets.txt
file = open('planets.txt', 'w', encoding='utf-8')
planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n']

file.writelines(planets)

file.close()
