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
    
 




def create_spend_chart(categories):
    percentArray = []
    for instance in categories:
        sum = 0
        for record in instance.ledger:
            if record['amount'] < 0 :
                sum += float(-record['amount'])
        
        percentArray.append(sum)
    totalExp = reduce( lambda a, b: a + b, percentArray)
    weightedArray = list((map(lambda a: floor(a / totalExp * 10),  percentArray)))

    resultString = ''
    resultString += 'Percentage spent by category\n'
    resultArray = []
    resultArray.append(resultString)

    
    for i in range(11):
        
        resultString = ''
        barValue = str(10 - i)
        if len(barValue) != 1:
            resultString += barValue + '0|'
        elif int(barValue) == 0:
            resultString += '  ' + barValue + '|'
        else:
            resultString += ' ' + barValue + '0|'

        for j in range(len(weightedArray)):
   
            if weightedArray[j] >= float(barValue):
                resultString +=  ' o '
            else:
                resultString += '   '

        resultString +=' \n'
        resultArray.append(resultString)
    
    
    resultArray.append('    ----------\n')

    arrayCategoryOut = {}
    for i in range(len(categories)):

        arrayCategoryOut[categories[i].name] = weightedArray[i]

    titleLength = 0
    for k in categories:
        if len(k.name) > titleLength:
            titleLength = len(k.name)

    arrayCategoryOut = list(arrayCategoryOut)

    for i in range(titleLength ):
        resultString = ' ' * 3
        for j in range(len(arrayCategoryOut)):
            
            if len(arrayCategoryOut[j]) - 1 >= i:
                resultString += '  ' + arrayCategoryOut[j][i]
            else:
                resultString += '   '
           
        resultArray.append(resultString + "  \n")

    result = ''
    for i in range(len(resultArray)):
        result += resultArray[i]

    result = result.rstrip('\n')
    return result



