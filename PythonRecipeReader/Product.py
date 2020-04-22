class Product:
    def __init__(self, type, name, temperature=None, amount=None, amount_min=None, amount_max=None, probability=None):
        self.type = type
        self.name = name
        self.temperature = temperature
        self.amount = amount
        self.amount_min = amount_min
        self.amount_max = amount_max
        self.probability = probability

    def __str__(self):
        amount = ''
        if self.amount is None:
            amount = str(self.amount_min) + ' .. ' + str(self.amount_max)
        else:
            amount = str(self.amount)
        return self.name \
            + ':\n\t\t\ttype: ' + str(self.type) \
            + '\n\t\t\tamount: ' + amount
