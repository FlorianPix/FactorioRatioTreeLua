from Ingredient import Ingredient
from Product import Product


class Recipe:
    def __init__(self, name, ingredients, products, energy):
        self.name = name
        self.ingredients = ingredients
        self.products = products
        self.energy = energy

    def __str__(self):
        ingredients = ''
        for ingredient_name in self.ingredients:
            ingredients = ingredients + str(self.ingredients[ingredient_name]) + '\n\n\t'
        products = ''
        for product_name in self.products:
            products = products + str(self.products[product_name]) + '\n\n\t\t'
        return '{ \n\tRecipe:' \
               + '\n\t\t' + self.name \
               + '\n\n\t' + 'Ingredients:\n\t'\
               + ingredients \
               + '\n\t' + 'Products:\n\t\t'\
               + products \
               + '\n\t' + 'Time:\n\t\t' \
               + str(self.energy) + 's\n}\n'
