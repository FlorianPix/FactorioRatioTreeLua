import os
import json
from PythonRecipeReader import PythonRecipeReader


def main():
    os.chdir("..\\Recipes")
    recipe_file_names = os.listdir()
    # open recipes (json files)
    recipe_dict = {}
    keys = []
    prr = PythonRecipeReader()
    with open("recipe.json") as json_file:
        data = json.load(json_file)
        for key in data.keys():
            keys.append(key)
        recipe_dict.update(data)
    for key in keys:
        recipe = recipe_dict[key]
        prr.add_recipe(recipe)

    add_recipes_for_ingredients(prr)

    for recipe_name in prr.recipes:
        print(prr.recipes[recipe_name])


def add_recipes_for_ingredients(prr):
    """
    For every recipe look at the ingredients.
    For every ingredient search what recipes exist that have this ingredient as a product.
    Add these recipes to the ingredients dict of recipes.
    :param prr:
    """
    for recipe_name in prr.recipes:
        for ingredient in prr.recipes[recipe_name].ingredients:
            prr.recipes[recipe_name].ingredients[ingredient].add_recipes(prr.search_recipes_by_name(ingredient))


if __name__ == "__main__":
    main()
