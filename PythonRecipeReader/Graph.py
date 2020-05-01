from graphviz import Digraph


def draw_recipe(recipe, num):
    dot = Digraph(comment=recipe.name)
    dot.node(recipe.name, label=recipe.name + '\n' + str(recipe.energy) + 's', shape='hexagon')
    for ing in recipe.ingredients:
        dot.subgraph(draw_ingredient(recipe.ingredients[ing]))
        ing_per_second = str(round(recipe.ingredients[ing].amount/recipe.energy, 2)) + '/s'
        dot.edge(ing, recipe.name, label=ing_per_second)
    for pro in recipe.products:
        dot.subgraph(draw_product(recipe.products[pro]))
        if recipe.products[pro].amount is not None:
            pro_per_second = str(round(recipe.products[pro].amount / recipe.energy, 2)) + '/s'
        else:
            average_amount = (recipe.products[pro].amount_min + recipe.products[pro].amount_max)/2
            pro_per_second = str(round(average_amount / recipe.energy, 2)) + '/s'
        dot.edge(recipe.name, pro, label=pro_per_second)
    dot.render('test-output/rec' + str(num) + '.gv')


def draw_ingredient(ingredient):
    dot = Digraph(comment=ingredient.name)
    dot.node(ingredient.name, label=ingredient.name + '\n' + str(ingredient.amount) + 'x', shape='box')
    return dot


def draw_product(product):
    dot = Digraph(comment=product.name)
    if product.amount is not None:
        dot.node(product.name, label=product.name + '\n' + str(product.amount) + 'x', shape='box')
    else:
        average_amount = str((product.amount_min + product.amount_max) / 2)
        dot.node(product.name, label=product.name + '\n' + average_amount + 'x', shape='box')
    return dot
