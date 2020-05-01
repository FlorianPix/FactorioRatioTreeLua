import os
import sys
import json
import pickle
from PythonRecipeReader import PythonRecipeReader
import Graph


def main():
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'
    prr = None
    if os.path.exists('prr.pkl'):
        with open('prr.pkl', 'rb') as load_this:
            prr = pickle.load(load_this)
    else:
        print('No PRR Object available, importing recipes from json.')
        prr = create_fill_and_save_prr()
        print('Building Database: Done')

    # Example of searching a recipe
    while(True):
        searched_name = input()
        if searched_name == '':
            break
        search_result = prr.search_recipes_by_name(searched_name)[searched_name]
        if search_result:
            i = 0
            for recipe in search_result:
                Graph.draw_recipe(recipe, i)
                i += 1
            print('Rendered ' + str(i) + ' graphs.')
        else:
            print('Couldn\'t find this recipe.')


def create_fill_and_save_prr():
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
    os.chdir("..\\PythonRecipeReader")
    sys.setrecursionlimit(10000)
    with open('prr.pkl', 'wb') as output:
        pickle.dump(prr, output, -1)
    sys.setrecursionlimit(1000)
    return prr


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
