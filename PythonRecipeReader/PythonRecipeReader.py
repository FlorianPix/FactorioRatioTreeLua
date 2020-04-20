import os
import json
from Recipe import Recipe

"""
Keys:

enabled :: boolean [R]	If this recipe prototype is enabled by default (enabled at the beginning of a game).
name :: string [R]	Name of the recipe.
localised_name :: LocalisedString [R]	Localised name of the recipe.
localised_description :: LocalisedString [R]	
category :: string [R]	Category of the recipe.
ingredients :: array of Ingredient [R]	Ingredients for this recipe.
products :: array of Product [R]	The results of this recipe.
main_product :: Product [R]	The main product of this recipe, nil if no main product is defined.
hidden :: boolean [R]	Is the recipe hidden?
hidden_from_flow_stats :: boolean [R]	Is the recipe hidden from flow statistics (item/fluid production statistics)?
hidden_from_player_crafting :: boolean [R]	Is the recipe hidden from player crafting?
always_show_made_in :: boolean [R]	Should this recipe always show "Made in" in the tooltip?
energy :: double [R]	Energy required to execute this recipe.
order :: string [R]	Order string.
group :: LuaGroup [R]	Group of this recipe.
subgroup :: LuaGroup [R]	Subgroup of this recipe.
request_paste_multiplier :: uint [R]	The multiplier used when this recipe is copied from an assembling machine to a requester chest.
overload_multiplier :: uint [R]	Used to determine how many extra items are put into an assembling machine before it's considered "full enough".
allow_as_intermediate :: boolean [R]	If this recipe is enabled for the purpose of intermediate hand-crafting.
allow_intermediates :: boolean [R]	If this recipe is allowed to use intermediate recipes when hand-crafting.
show_amount_in_title :: boolean [R]	If the amount is shown in the recipe tooltip title when the recipe produces more than 1 product.
always_show_products :: boolean [R]	If the products are always shown in the recipe tooltip.
emissions_multiplier :: double [R]	The emissions multiplier for this recipe.
allow_decomposition :: boolean [R]	Is this recipe allowed to be broken down for the recipe tooltip "Total raw" calculations?
valid :: boolean [R]	Is this object valid?
help() → string	All methods, and properties that this object supports.


Relevant Keys:

name :: string [R]	Name of the recipe.
ingredients :: array of Ingredient [R]	Ingredients for this recipe.
products :: array of Product [R]	The results of this recipe.
main_product :: Product [R]	The main product of this recipe, nil if no main product is defined.
energy :: double [R]	Energy required to execute this recipe.


Relevant Keys for Products and Ingredients:

Ingredients
type :: string: "item" or "fluid".
name :: string: Prototype name of the required item or fluid.
amount :: double: Amount of the item or fluid.
minimum_temperature :: double (optional): The minimum fluid temperature required. Has no effect if type is '"item"'.
maximum_temperature :: double (optional): The maximum fluid temperature allowed. Has no effect if type is '"item"'.
catalyst_amount :: uint or double (optional): How much of this ingredient is a catalyst.

Products
type :: string: "item" or "fluid".
name :: string: Prototype name of the result.
amount :: double (optional): Amount of the item or fluid to give. If not specified, amount_min, amount_max and probability must all be specified.
temperature :: double (optional): The fluid temperature of this product. Has no effect if type is '"item"'.
amount_min :: uint or double (optional): Minimal amount of the item or fluid to give. Has no effect when amount is specified.
amount_max :: uint or double (optional): Maximum amount of the item or fluid to give. Has no effect when amount is specified.
probability :: double (optional): A value in range [0, 1]. Item or fluid is only given with this probability; otherwise no product is produced.
catalyst_amount :: uint or double (optional): How much of this product is a catalyst.
"""


def main():
    os.chdir("..\\Recipes")
    recipe_file_names = os.listdir()
    # open recipes (json files)
    recipe_dict = {}
    keys = []
    with open("recipe.json") as json_file:
        data = json.load(json_file)
        for key in data.keys():
            keys.append(key)
        recipe_dict.update(data)
    recipes = []
    for key in keys:
        recipe = recipe_dict[key]
        r_o = Recipe(recipe['name'], recipe['ingredients'], recipe['products'], recipe['energy'])
        recipes.append(r_o)

    for recipe in recipes:
        print(recipe)


if __name__ == "__main__":
    main()
