class Ingredient:
    def __init__(self, type, name, amount):
        self.type = type
        self.name = name
        self.amount = amount

    def __str__(self):
        return '\t' + self.name \
            + ':\n\t\t\ttype: ' + str(self.type) \
            + '\n\t\t\tamount: ' + str(self.amount)
