class Recipe:
    def __init__(self, name, ingredients, products, energy):
        self.name = name
        self.ingredients = ingredients
        self.products = products
        self.energy = energy

    def __str__(self):
        return 'Recipe of ' + self.name \
               + ':\n' + str(self.ingredients) \
               + '\n' + str(self.products) \
               + '\n' + str(self.energy)
