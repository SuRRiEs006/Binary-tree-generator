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
    

# class BinaryTree(object):
#     def __init__(self, root):
#       self.root = Node(root)

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
        
        if (inputAray[i] in self.defualtOperators) or (inputAray[i] in self.acceptedNums):
          levelsOfTreeArray.append([inputAray[i],bracketCount,i+1])

      return(levelsOfTreeArray)

    
    def addToTree(self,workinglevelsOfTreeArray):
      minBracketDepth = workinglevelsOfTreeArray[0][1]
      

      for i in range(0,len(workinglevelsOfTreeArray)):
        #print(workinglevelsOfTreeArray)
        if workinglevelsOfTreeArray[i][1] <= minBracketDepth:
          minBracketDepth = workinglevelsOfTreeArray[i][1]
      #print(minBracketDepth)   


      for y in range(0,len(workinglevelsOfTreeArray)):
          if (workinglevelsOfTreeArray[y][1] == minBracketDepth) & (workinglevelsOfTreeArray[y][0] in self.defualtOperators):
            print(workinglevelsOfTreeArray[y][0])
            node = Node(workinglevelsOfTreeArray[y][0])

            if workinglevelsOfTreeArray[y-1][1] == minBracketDepth:
              print('Left ->',workinglevelsOfTreeArray[y-1][0])
              node.left = Node(workinglevelsOfTreeArray[y-1][0])
            else:
              leftArray = workinglevelsOfTreeArray[:(y)]
              node.left = self.addToTree(leftArray)
              #print(leftArray)
              


            if workinglevelsOfTreeArray[y+1][1] == minBracketDepth:
              print('Right ->',workinglevelsOfTreeArray[y+1][0])
              node.right = Node(workinglevelsOfTreeArray[y+1][0])
            else:
              rightArray = workinglevelsOfTreeArray[(y+1):]
              node.right = self.addToTree(rightArray)
              #print(rightArray)
            return node
            break
          

      

    def breakupStatement(self):
        workingInputList = list(self.binaryTreeStr[1:-1])
       # startingLevelOfTree = self.levelsOfTree(workingInputList)
       # print(workinglevelsOfTreeArray)
      
        # if len(workinglevelsOfTreeArray) > 0:
        #   lowestVal = len(workinglevelsOfTreeArray)
        #   for l in range (0,len(workinglevelsOfTreeArray)):
        #     if workinglevelsOfTreeArray[l][1] <= lowestVal:
        #       lowestVal = workinglevelsOfTreeArray[l][1]
              



        print(self.addToTree(self.levelsOfTree(workingInputList)).left.left.value)
        
        



        
tree = []

statementOne = BinaryTreeCreator("((((5+2) *(2-1))/((2+9)+((7-2)-1))) *8) ")

(((2*(3+2))+5)/2)


(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)


[['2', 2, 3], ['*', 2, 4], ['3', 3, 6], ['+', 3, 7], ['2', 3, 8], ['+', 1, 11], ['5', 1, 12], ['/', 0, 14], ['2', 0, 15]]

statementOne.breakupStatement()










[['5', 2, 3], ['+', 2, 4], ['2', 2, 5], ['*', 1, 7], ['2', 2, 9], 
['-', 2, 10], ['1', 2, 11], ['/', 0, 14], ['2', 2, 17], ['+', 2, 18], ['9', 2, 19], 
['+', 1, 21], ['7', 3, 24], ['-', 3, 25], ['2', 3, 26], ['-', 2, 28], ['1', 2, 29], ['*', 0, 32], ['8', 0, 33]]





