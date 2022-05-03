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

    def levelsOfTree(self,inputAray):
      bracketCount = 0
      levelsOfTreeArray = []
      
      for i in range(0,len(inputAray)):

        if inputAray[i] == "(" :
          bracketCount += 1
        elif inputAray[i] == ")" :
          bracketCount -= 1
        
        if inputAray[i] in self.defualtOperators:
          levelsOfTreeArray.append([inputAray[i],bracketCount,i])

      return(levelsOfTreeArray)
    
    def nextIndexSplit(symbolsArray):
        pass

    def breakupStatement(self):
        workingInputList = list(self.binaryTreeStr)
        workinglevelsOfTreeArray = self.levelsOfTree(workingInputList)
        print(workinglevelsOfTreeArray)
      
        if len(workinglevelsOfTreeArray) > 0:
          lowestVal = len(workinglevelsOfTreeArray)
          for l in range (0,len(workinglevelsOfTreeArray)):
            if workinglevelsOfTreeArray[l][1] <= lowestVal:
              lowestVal = workinglevelsOfTreeArray[l][1]
        
        print(lowestVal)
        

statementOne = BinaryTreeCreator("(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)")

statementOne.breakupStatement()
(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)