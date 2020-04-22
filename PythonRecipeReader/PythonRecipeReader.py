from Recipe import Recipe
from Ingredient import Ingredient
from Product import Product

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


class PythonRecipeReader:
    def __init__(self):
        self.recipes = {}
        self.ingredients = {}
        self.products = {}

    def add_recipe(self, recipe):
        """
        Takes the given dict recipe, creates a Recipe() from it and adds it to self.recipes
        also adds all ingredients that aren't yet in self.ingredients to that.
        The same applies to products.
        :param recipe: A dictionary for a single recipe
        :return:
        """

        ingredients = {}
        for ingredient in recipe['ingredients']:
            # check if ingredient already exist
            potential_new_ingredient = self.ingredient_exists(ingredient)
            if potential_new_ingredient is None:
                # if ingredient does not already exist create a new Ingredient() from ingredient dictionary
                # and add it to ingredients
                ing = Ingredient(ingredient['type'],
                                 ingredient['name'],
                                 ingredient['amount'])
                self.ingredients[ingredient['name']] = ing
                ingredients[ingredient['name']] = ing
            else:
                # if ingredient does already exist take that ingredient object and add it to ingredients
                ingredients[ingredient['name']] = potential_new_ingredient
        products = {}
        for product in recipe['ingredients']:
            # check if product already exist
            potential_new_product = self.product_exists(product)
            if potential_new_product is None:
                # if product does not already exist create a new Product() from product dictionary
                # and add it to products
                pro = None
                if 'amount' in product.keys():
                    pro = self.products[product['name']] = Product(product['type'],
                                                                   product['name'],
                                                                   amount=product['amount'])
                else:
                    pro = self.products[product['name']] = Product(product['type'],
                                                                   product['name'],
                                                                   amount_min=product['amount_min'],
                                                                   amount_max=product['amount_max'])
                self.products[product['name']] = pro
                products[product['name']] = pro
            else:
                # if product does already exist take that product object and add it to products
                products[product['name']] = potential_new_product
        # create new Recipe() and add it to self.recipes
        r_o = Recipe(recipe['name'],
                     ingredients,
                     products,
                     recipe['energy'])
        self.recipes[recipe['name']] = r_o

    def ingredient_exists(self, ingredient):
        """
        Used to prohibit the creation of multiple ingredient objects of the same ingredient.
        Checks if an ingredient with the same name already exists in der ingredients dict.
        :param ingredient:
        :return ingredient or None: existing ingredient or None if the ingredient does not yet exist
        """
        for existing_ingredient in self.ingredients:
            if ingredient['name'] is existing_ingredient:
                return ingredient
        return None

    def product_exists(self, product):
        """
            Used to prohibit the creation of multiple product objects of the same product.
            Checks if an ingredient with the same name already exists in der ingredients dict.
            :param product:
            :return product or None: existing product or None if the product does not yet exist
            """
        for existing_product in self.products:
            if product['name'] is existing_product:
                return product
        return None
