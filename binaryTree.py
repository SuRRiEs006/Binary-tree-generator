#####REFERENCES####
'''
- find function (https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes)
-https://www.delftstack.com/howto/python/python-clear-console/
'''

#######IMPORT######
import copy
import time
import os
import pickle
#######CODE#######

#FUNTION THAT CLEARS CONSOLE AND PRINTS MESSAGE IN EMPTY CONSOLE
def clearConsoleMessage(message):
  #TOOK NEXT 4 LINES FROM www.delftstack.com/howto/python/python-clear-console/
  #CLEARS CONSOLE
  command = 'clear'
  if os.name in ('nt', 'dos'):  
      command = 'cls'
  os.system(command)
  #PRINTS MESSAGE AS PASSED TO METHOD
  print(message)
  
#INITIALISES THE NODE METHOD FOR RECURSION
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#CALCULATES THE ANSWER TO THE EXPRESSION
def evaluateTree(expressionTree):
  answer = 0
  #LOOKS FOR WHAT OF THE 4 SYMBOLS IS BEING USED AND TAKES EITHER SIDE
  #BECAUSE IT'S RECURSIVE IT ENSURES ONLY AFTER THERE IS A NUMBER ON EACH SIDE THE IF STATEMENT IS REACHED
  #THERE IS NO WAY THERE IS BRACKET ON EITHER SIDE IF AN OPERATOR REACHED
  if expressionTree.value == "*":
    answer =  float(evaluateTree(expressionTree.left)) * float(evaluateTree(expressionTree.right))
  elif expressionTree.value == "/":
    answer =  float(evaluateTree(expressionTree.left)) / float(evaluateTree(expressionTree.right))
  elif expressionTree.value == "+":
    answer =  float(evaluateTree(expressionTree.left)) + float(evaluateTree(expressionTree.right))
  elif expressionTree.value == "-":
    answer =  float(evaluateTree(expressionTree.left)) - float(evaluateTree(expressionTree.right))
  else:
    #END OF RECURSION
    answer=expressionTree.value
  return(answer)
  

#RECURSIVLY OUTPUTS TREE
def treeToTerminal(expressionTree,indentNumber):
  #indentNumber IS THE NUMBER OF INDENTS TO MAKE THE TREE ACCURATE

  #FINDS THE ROOT NODE
  if expressionTree.left != None:
    treeToTerminal(expressionTree.left,indentNumber+1)

  #THIS POINT IS ONLY REACHED AT THE END, WHEN ITS STOPS RECURSING
  print(str(indentNumber*'  '),expressionTree.value)

  #FINDS THE END OF THE BRANCHES OF THE TREE AND THEN STOPS SEARCHING FURTHER
  if expressionTree.right != None:
    treeToTerminal(expressionTree.right,indentNumber+1)


#MAIN MENU THAT CO-ORDINATES THE USER'S INPUTS WITH THE APROPRIATE ACTIONS
def menu():
  #WHILE LOOP ENSURES THAT LOOPS TILL ENDING
  while True:

  ################# JUST TEXT FORMATTED TO LOOK NICE #################
      clearConsoleMessage('''
------------------------------------------------------------
                                                                                                                                                          
                              
  88d8b.d8b. .d8888b. 88d888b. dP    dP 
  88'`88'`88 88ooood8 88'  `88 88    88 
  88  88  88 88.  ... 88    88 88.  .88 
  dP  dP  dP `88888P' dP    dP `88888P'#


  PLEASE SELECT AN OPTION TO CONTINUE:
  A) VISUALIZED AN EXPRESSION
  B) LOAD THE LAST VISUALIZED EXPRESSION  
  C) QUIT
          ''')
  
      menuInput = input("INPUT:  ")
      print("------------------------------------------------------------ \n")
      menuInput = menuInput.lower()
  ######################################################################

  #THE OPTION SELECTED BY THE USER IS PROCESSED THROUGH THE IF STATEMENTS BELOW
      if menuInput == "a":

          #I ADD BRACKETS IN CASE THEY FORGET TO PREVENT MY CODE FROM CRASHING
          experessionIn = ("("+str(input("INPUT YOUR EXPRESSION: "))+")")
          #CREATES BinaryTreeCreator OBJECT AND CALLS MAIN METHOD
          statementOne = BinaryTreeCreator(experessionIn)
          statementOne.main()
          
          #GIVES THE USER TIME TO READ OUTPUT
          input("PRESS ENTER TO CONTINUE... ")

      elif menuInput == "b":
          clearConsoleMessage("YOUR PREVIOUS TREE IS BELOW: \n\n\n")
          #CALLS LOAD TREE METHOD TO RETURN PREVIOUS BINARY TREE AND PRINT TO TERMINAL
          treeToTerminal(loadTree(),0)
          #GIVES THE USER TIME TO READ OUTPUT
          input("\n \n \nPLEASE PRESS ENTER TO GO BACK TO MENU...")
          
      elif menuInput == "c":
          #THANKS USERS BEFORE TERMINATING PROGRAM
          clearConsoleMessage("""THANK YOU FOR USING BINARY TREE MAKER! """)
          quit()

          
      else:
################# JUST TEXT FORMATTED TO LOOK NICE #################
          clearConsoleMessage('''                                                  
------------------------------------------------------------


  .d88b.  888d888 888d888 .d88b.  888d888      d8b 
  d8P  Y8b 888P"   888P"  d88""88b 888P"        Y8P 
  88888888 888     888    888  888 888              
  Y8b.     888     888    Y88..88P 888          d8b 
   "Y8888  888     888     "Y88P"  888          Y8P


  - PLEASE ENSURE THAT YOU PICK BETWEEN OPTIONS A,B,C
  - PLEASE ONLY ONE LETTER IS ENTERED
      ''')
          #GIVES THE USER TIME TO READ OUTPUT
          input("\n \n \nPLEASE PRESS ENTER TO GO BACK TO MENU...")
######################################################################

#USES PICKLE LIBRARY TO SERIALIZE AND SAVE
def saveTree(expressionTree):
  #CREATES FILE, WRITES DATA FROM TREE OBJECT AND CLOSES
  fileOpen = open('LastSaved.pkl', 'wb')
  pk = pickle.Pickler(fileOpen)
  pk.dump(expressionTree)
  fileOpen.close()


#USES PICKLE LIBRARY TO UNPICKLE DATA SAVED IN PKL FILE
def loadTree():
  #PICKLE FILE IS OPENED, DATA IS UNPICKLED AND FILE IS CLOSED
  fileOpen = open('LastSaved.pkl', 'rb')
  pk = pickle.Unpickler(fileOpen)
  newTreeList = pk.load()
  fileOpen.close()
  return newTreeList

class BinaryTreeCreator:
    def __init__(self, binaryTreeStr):
      self.defualtOperators = ['/', '*', '+', '-']
      self.acceptedNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      self.otherSymbol = ['(', ')']
      self.allSubStrings = self.defualtOperators + self.acceptedNums + self.otherSymbol
      self.binaryTreeStr = str(binaryTreeStr.replace(' ', ''))

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
        print(completeArray)
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

    def validOperand(self):
        currentStr = copy.copy(self.binaryTreeStr)
        isValiddOperand = None
        
        numCounter = 0
        operatorCounter = 0

        for i in range(0,len(currentStr)):
            if currentStr[i] in self.defualtOperators:
                operatorCounter +=1
            if currentStr[i] in self.acceptedNums:
                numCounter +=1
       # print(operatorCounter,numCounter)
        if ((operatorCounter+1) == numCounter) and (operatorCounter > 0) and (numCounter > 1):
           isValiddOperand = True
        else:
           isValiddOperand = False
        
        return isValiddOperand
        

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



    def validateString(self):
        
        currentStr = copy.copy(self.binaryTreeStr)

        isValidSubStrings = self.validSubStrings()
        isValidBrackets = self.validBrackets()
        isValidOperand = self.validOperand()

        if isValidBrackets == False:
            print("Not a valid expression, bracket mismatched")
        if isValidSubStrings == False:
            print("Not a valid expression, unrecognised charecters")
        if isValidOperand == False:
            print("Not a valid expression, operator missing.") 

        return isValidSubStrings, isValidBrackets, isValidOperand

    
    def addToTree(self,workinglevelsOfTreeArray):
      minBracketDepth = workinglevelsOfTreeArray[0][1]
      

      for i in range(0,len(workinglevelsOfTreeArray)):

        if workinglevelsOfTreeArray[i][1] <= minBracketDepth:
          minBracketDepth = workinglevelsOfTreeArray[i][1]
         

      for y in range(0,len(workinglevelsOfTreeArray)):
          if (workinglevelsOfTreeArray[y][1] == minBracketDepth) & (workinglevelsOfTreeArray[y][0] in self.defualtOperators):
            #print(workinglevelsOfTreeArray[y][0])
            node = Node(workinglevelsOfTreeArray[y][0])

            if workinglevelsOfTreeArray[y-1][1] == minBracketDepth:
              #print('Left ->',workinglevelsOfTreeArray[y-1][0])
              node.left = Node(workinglevelsOfTreeArray[y-1][0])
            else:
              leftArray = workinglevelsOfTreeArray[:(y)]
              node.left = self.addToTree(leftArray)
              #print(leftArray)
              

            if workinglevelsOfTreeArray[y+1][1] == minBracketDepth:
              #print('Right ->',workinglevelsOfTreeArray[y+1][0])
              node.right = Node(workinglevelsOfTreeArray[y+1][0])
            else:
              rightArray = workinglevelsOfTreeArray[(y+1):]
              node.right = self.addToTree(rightArray)
              #print(rightArray)
            return node
            break
          

    def main(self):
        isValidSubStrings, isValidBrackets,  isValidOperand = False, False,  False
        while (isValidSubStrings == False) or (isValidBrackets == False) or (isValidOperand == False):
            isValidSubStrings, isValidBrackets, isValidOperand = self.validateString()
            if (isValidSubStrings == False) or (isValidBrackets == False) or (isValidOperand == False):
                experessionIn = ("("+str(input(" \n\nINCORRECT INPUT, PLEASE ENTER YOUR EXPRESSION CORRECTLY: "))+")")
                self.binaryTreeStr = experessionIn

            #print(isValidSubStrings, isValidBrackets, currentStr, isValidOperand)
        workingInputList = list(self.binaryTreeStr[1:-1])
        expressionTree = self.addToTree(self.levelsOfTree(workingInputList))
        clearConsoleMessage(str("                         ANSWER \n                        --------- \n THE ANSWER TO YOUR EXPRESSION "+str(self.binaryTreeStr)+" IS: "+str(evaluateTree(expressionTree))+""""""))
        print(""" BINARY TREE:""")
        
        treeToTerminal(expressionTree,0)
        print("------------------------------------------------------------")
        saveTree(expressionTree)
        
        


        
        
        







menu()
