pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

pasta_ingredients = pasta.split(',')
apple_pie_ingredients = apple_pie.split(',')
ratatouille_ingredients = ratatouille.split(',')
chocolate_cake_ingredients = chocolate_cake.split(',')
omelette_ingredients = omelette.split(',')


class Recipes:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def find_ingredients(self, ingredient):
        for ingredient_ in self.ingredients:
            # print(ingredient_)
            if ingredient_.strip() == ingredient:
                print(f'{self.name} time!')


pasta_recipe = Recipes('pasta', pasta_ingredients)
apple_pie_recipe = Recipes('apple pie', apple_pie_ingredients)
ratatouille_recipe = Recipes('ratatouille', ratatouille_ingredients)
chocolate_cake_recipe = Recipes('chocolate cake', chocolate_cake_ingredients)
omelette_recipe = Recipes('omelette', omelette_ingredients)

input_ingredient = str(input())

pasta_recipe.find_ingredients(input_ingredient)
apple_pie_recipe.find_ingredients(input_ingredient)
ratatouille_recipe.find_ingredients(input_ingredient)
chocolate_cake_recipe.find_ingredients(input_ingredient)
omelette_recipe.find_ingredients(input_ingredient)





