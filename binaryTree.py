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
          
          
      

    def main(self):
        workingInputList = list(self.binaryTreeStr[1:-1])
        expressionTree = self.addToTree(self.levelsOfTree(workingInputList))
        print(evaluateTree(expressionTree))
        treeToTerminal(expressionTree,0)
        
        
def evaluateTree(expressionTree):
  answer = 0
  if expressionTree.value == "*":
    answer =  float(evaluateTree(expressionTree.left)) * float(evaluateTree(expressionTree.right))
  elif expressionTree.value == "/":
    answer =  float(evaluateTree(expressionTree.left)) / float(evaluateTree(expressionTree.right))
  elif expressionTree.value == "+":
    answer =  float(evaluateTree(expressionTree.left)) + float(evaluateTree(expressionTree.right))
  elif expressionTree.value == "-":
    answer =  float(evaluateTree(expressionTree.left)) - float(evaluateTree(expressionTree.right))
  else:
    answer=expressionTree.value
  return(answer)
  

def treeToTerminal(expressionTree,indentNumber):


  if expressionTree.left != None:
    treeToTerminal(expressionTree.left,indentNumber+1)

  print(str(indentNumber*'  '),expressionTree.value)
  if expressionTree.right != None:

    treeToTerminal(expressionTree.right,indentNumber+1)
    







statementOne = BinaryTreeCreator("(((2*(3+2))+5)/2)")


(((2*(3+2))+5)/2)
((((5+2) *(2-1))/((2+9)+((7-2)-1))) *8)

(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)


statementOne.main()
