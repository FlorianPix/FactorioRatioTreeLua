class Ingredient:
    def __init__(self, type, name, amount, minimum_temperature=None, maximum_temperature=None):
        self.type = type
        self.name = name
        self.amount = amount
        self.minimum_temperature = minimum_temperature
        self.maximum_temperature = maximum_temperature
        self.recipes = {}

    def add_recipes(self, recipes):
        """
        Add dict of recipes to self.recipes
        :param recipes:
        """
        self.recipes.update(recipes)

    def print_recipes(self):
        ret = ''
        for recipe in self.recipes:
            if isinstance(self.recipes[recipe], list):
                for r in self.recipes[recipe]:
                    if ret is '':
                        ret = str(r.name)
                    else:
                        ret = ret + ', ' + str(r.name)
            else:
                ret = ret + self.recipes[recipe].name
        return ret

    def __str__(self):
        return '\t' + self.name \
            + ':\n\t\t\ttype: ' + str(self.type) \
            + '\n\t\t\tamount: ' + str(self.amount) \
            + '\n\n\t\t\tRecipes:\n\t\t\t\t' + self.print_recipes()
