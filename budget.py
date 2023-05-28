from functools import reduce
from math import floor

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
                outputLine += desc[:23]
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
                        outputLine += ' ' * ( 7 - len(str(amnt) )) + str(amnt)
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
            sum += float(trans['amount'])
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
    
    
"""
food = Category("Food")
food.deposit( 900, 'Initial deposit')
food.withdraw( 45.67, 'Buy out')
food.withdraw( 32, 'Test purchase')

grocery = Category("Grocery")
grocery.deposit( 900, 'Initial deposit')
grocery.withdraw( 120, 'Buy out')

ent = Category("Ent")
ent.deposit( 900, 'Initial deposit')
ent.withdraw( 40, 'Initial ')
ent.withdraw( 300, 'Initial 2')
ent.withdraw( 6, 'Initial 3')
#grocery.deposit(30, "Initial deposit")
#grocery.transfer(30, food)

#print(food)
#print(grocery)
"""
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)




def create_spend_chart(categories):
    percentArray = []
    for instance in categories:
        sum = 0
        for record in instance.ledger:
            if record['amount'] < 0 :
                sum += float(-record['amount'])
        
        percentArray.append(sum)
    print(percentArray)
    totalExp = reduce( lambda a, b: a + b, percentArray)
    print(totalExp)
    print(list((map(lambda a: a / totalExp , percentArray))))
    weightedArray = list((map(lambda a: round(a / totalExp * 10),  percentArray)))
    print(weightedArray)

    resultString = ''
    resultString += 'Percentage spent by category\n'
    resultArray = []
    resultArray.append(resultString)

    
    for i in range(11):
        
        resultString = ''
        barValue = str(10 - i)
        if len(barValue) != 1:
            resultString += barValue + '0|'
        else:
            resultString += ' ' + barValue + '0|'

        if 'o' in resultArray[i] and i != 0:
                resultString += ' o ' * resultArray[i].count('o')

        for j in range(len(weightedArray)):
   
            if weightedArray[j] == float(barValue):
                resultString +=  ' o '
            

        resultString +='\n'
        resultArray.append(resultString)
    
    
    resultArray.append('    ----------\n')

    arrayCategoryOut = {}
    for i in range(len(categories)):

        arrayCategoryOut[categories[i].name] = weightedArray[i]

    titleLength = reduce( lambda a, b: max(a, b), arrayCategoryOut.values())
    print("Lentgh - " + str(titleLength))

    arrayCategoryOut = sorted(arrayCategoryOut.items(), key=lambda x: x[1], reverse=True)
    print(arrayCategoryOut)
    #print(arrayCategoryOut[0][0][0])

    for i in range(titleLength + 1):
        resultString = ' ' * 3
        print("Hey")
        for j in range(len(arrayCategoryOut)):
            
            if len(arrayCategoryOut[j][0]) - 1 >= i :
                print(i)
                print(arrayCategoryOut[j][0][i])

                resultString += '  ' + arrayCategoryOut[j][0][i]
                print("He")
            else:
                resultString += '   '
    
        print(resultString)
        resultArray.append(resultString + "\n")

    result = ''
    for i in range(len(resultArray)):
        result += resultArray[i]
    return result


#print(create_spend_chart([food, ent, grocery]))
print(create_spend_chart([business, food, entertainment]))