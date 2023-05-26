class Category:
    name = ''

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):

        if len(self.name) % 2 != 0 :
            outputLine = '*' * int((30 - len(self.name)) / 2  ) + self.name + '*' * int((30 - len(self.name)) / 2 + 1) + '\n'
        else:
            outputLine = '*' * int((30 - len(self.name)) / 2) + self.name + '*' * int((30 - len(self.name)) / 2) + '\n'
        print(len(outputLine))

        for transaction in self.ledger:
            desc = transaction['description']
            amnt = transaction['amount']

            if len(desc) >= 23:
                outputLine += desc[:24]
                if len(str(amnt)) >= 7:
                    outputLine += amtn[:8]
                else:
                    if '.' in str(amnt):
                        outputLine += ' ' * ( 7 - len(str(amnt)) ) + str(amnt)
                    else:
                        outputLine += ' ' * ( 4 - len(str(amnt)) ) + str(amnt) + '.00'

                outputLine += '\n'

            else:
                outputLine += desc + ' ' * ( 23 - len(desc) )
                if len(str(amnt)) >= 7:
                    outputLine += amtn[:8]
                else:
                    if '.' in str(amnt):
                        outputLine += ' ' * ( 7 - len(str(amnt) ))
                    else:
                        outputLine += ' ' * ( 4 - len(str(amnt)) ) + str(amnt) + '.00'
                outputLine += '\n'

        outputLine += "Total: " + str(self.get_balance())
        return outputLine

    def deposit(self, amount, description = ''):
        self.ledger.append({ "amount" : amount, "description" : description })

    def withdraw(self, amount, description = ''):
        
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({ "amount" : - amount, "description" : description })
            return True
        
    def get_balance(self):
        sum = 0
        for trans in self.ledger:
            sum += int(trans['amount'])
        return sum
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            if isinstance(category, Category):
                self.withdraw(amount, f"Transfer to {category.name}")
                category.deposit(amount, f"Transfer from {self.name}")
                return True
            else:
                return False
        else:
            return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False
    
    

food = Category("Food")
food.deposit( 100, 'Initial deposit')
food.withdraw( 50, 'Buy out')

grocery = Category("Grocery")
grocery.deposit(30, "Initial deposit")
grocery.transfer(30, food)

print(food)
print(grocery)


def create_spend_chart(categories):
    pass