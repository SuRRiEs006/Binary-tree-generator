#####REFERENCES####
'''
- find function (https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes)

'''
#######IMPORT######
import copy

#######CODE#######

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

class BinaryTree:

    def __init__(self, binaryTreeStr):

        self.defualtOperators = ['/','*','+','-']
        self.acceptedNums = ['1','2','3','4','5','6','7','8','9']
        self.otherSymbol = ['(',')']
        self.allSubStrings = self.defualtOperators+self.acceptedNums+self.otherSymbol
        print(self.allSubStrings)
        self.binaryTreeStr = str(binaryTreeStr.replace(' ', ''))

    def validSubStrings(self):
        currentStr = copy.copy(self.binaryTreeStr)
        isValidSubStrings = None
        for x in range(0,len(self.allSubStrings)):

            currentStr = currentStr.replace(self.allSubStrings[x], '')
            if currentStr == '':
                isValidSubStrings = True
            else:
                isValidSubStrings = False
                
        return(isValidSubStrings)

    def validBrackets(self):
        isValidBrackets = None
        currentStr = copy.copy(self.binaryTreeStr)
        openBracket = currentStr.count("(")
        closeBracket = currentStr.count(")")

        if openBracket != closeBracket:
            isValidBrackets = False
        else:
            isValidBrackets = True
        
        return(isValidBrackets)

    def validOperand(self):
        pass


    def validateString(self):
        print(12)
        currentStr = copy.copy(self.binaryTreeStr)

        isValidSubStrings = self.validSubStrings()
        isValidBrackets = self.validBrackets()

        # for i in range(0,len(self.defualtOperators)):
        #     currentStr = currentStr.replace(self.defualtOperators[i], '.')

        # operators = currentStr.count(".")
        
        if isValidBrackets == False:
            print("Not a valid expression, bracket mismatched")

        print(isValidSubStrings, isValidBrackets, currentStr)

        print(self.arrayFormation())
    
    def arrayFormation(self):
        preCurrentStr = copy.copy(self.binaryTreeStr)

        currentArray = [char for char in preCurrentStr]
        openBracketIndex = find(preCurrentStr, '(')
        closeBracketIndex = find(preCurrentStr, ')')

        newArray = []
        for p in range(0,len(openBracketIndex)):
            
            endOfBracket = closeBracketIndex[(len(openBracketIndex)-1)-p]
            startOfBracket = openBracketIndex[p]

            newArray = newArray + [currentArray[startOfBracket:endOfBracket]]
            
            print(newArray)
        print(openBracketIndex,closeBracketIndex)
        
        

    def constructTree():
        pass

treeStr1 = BinaryTree("(((2*(3+2))+5)/2)")

treeStr1.validateString()