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

    for recipename in prr.recipes:
        print(prr.recipes[recipename])


if __name__ == "__main__":
    main()