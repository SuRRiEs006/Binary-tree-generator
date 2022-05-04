#####REFERENCES####
'''
- find function (https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes)

'''

#######IMPORT######
import copy

#######CODE#######

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
      self.root = Node(root)

class BinaryTreeCreator:
    def __init__(self, binaryTreeStr):
      self.defualtOperators = ['/', '*', '+', '-']
      self.acceptedNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      self.otherSymbol = ['(', ')']
      self.allSubStrings = self.defualtOperators + self.acceptedNums + self.otherSymbol
      #print(self.allSubStrings)
      self.binaryTreeStr = str(binaryTreeStr.replace(' ', ''))
      print("lol")

    def bracketMatching(self, string):
        openBracketIndexSaver = []
        sortingArray = []
        unsortedIndexArray = []
        completeArray = []

        for i in range(0,len(string)):
            if string[i] == '(':
                openBracketIndexSaver.append(i)
                sortingArray.append(i)
            elif string[i] == ')':
                unsortedIndexArray.append( [ openBracketIndexSaver.pop(),i ])


        for x in range(0,len(sortingArray)):
            for y in range(0,len(unsortedIndexArray)):
                if unsortedIndexArray[y][0] == sortingArray[x]:
                    completeArray.append(unsortedIndexArray[y])
                    break
        return(completeArray)



    def levelsOfTree(self,inputAray):
      bracketCount = 0
      levelsOfTreeArray = []
      
      for i in range(0,len(inputAray)):

        if inputAray[i] == "(" :
          bracketCount += 1
        elif inputAray[i] == ")" :
          bracketCount -= 1
        
        if inputAray[i] in self.defualtOperators:
          levelsOfTreeArray.append([inputAray[i],bracketCount,i+1])

      return(levelsOfTreeArray)

    def surroundingChar(self,charIndex):
        #DB = DELETE BOTH SIDE BRACKETS
        #DR = DELETE ONLY BRACKET TO RIGHT
        #DL = DELETE ONLY BRACKET TO LEFT
        #FR = FINAL REMOVING OF BRACKETS EG (3+2)
        if (self.binaryTreeStr[charIndex-1] in self.otherSymbol) & (self.binaryTreeStr[charIndex+1] in self.otherSymbol):
            nextStep = "DB"
        elif (self.binaryTreeStr[charIndex-1] in self.acceptedNums) & (self.binaryTreeStr[charIndex+1] in self.acceptedNums):
            nextStep = "FR"
        elif (self.binaryTreeStr[charIndex-1] in self.acceptedNums) & (self.binaryTreeStr[charIndex-1] in self.otherSymbol):
            nextStep = "DR"
        elif (self.binaryTreeStr[charIndex-1] in self.otherSymbol) & (self.binaryTreeStr[charIndex+1] in self.acceptedNums):
            nextStep = "DL"
        else:
            print("SOMETHING IS VERRYY VERYY WRONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return nextStep

    def breakupStatement(self):
        workingInputList = list(self.binaryTreeStr[1:-1])
        workinglevelsOfTreeArray = self.levelsOfTree(workingInputList)
        print(workinglevelsOfTreeArray)
      
        if len(workinglevelsOfTreeArray) > 0:
          lowestVal = len(workinglevelsOfTreeArray)
          for l in range (0,len(workinglevelsOfTreeArray)):
            if workinglevelsOfTreeArray[l][1] <= lowestVal:
              lowestVal = workinglevelsOfTreeArray[l][1]

        if lowestVal == 0 :
          found = False
          indexSearch = len(workinglevelsOfTreeArray)-1
          while found == False:
            print(workinglevelsOfTreeArray[indexSearch][1])
            if workinglevelsOfTreeArray[indexSearch][1] == 0:
              found = True
              print(workinglevelsOfTreeArray[indexSearch])
            indexSearch -=1
        print(self.surroundingChar(workinglevelsOfTreeArray[indexSearch][2]))

        


statementOne = BinaryTreeCreator("(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)")

(((2*(3+2))+5)/2)


((5+2)*(2-1))/((2+9)+((7-2)-1))*8



statementOne.breakupStatement()