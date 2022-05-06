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



#BinaryTreeCreator IS THE CLASS THAT DOES ALL THE CALCULATION
#AND STRING MANIPULATION RELATED TO MAKING THE EXPRESSION PROVIDED
#BY THE USER INTO A TREE AND THEN PRINTING THE TREE WITH CORRECT FORMAT

class BinaryTreeCreator:

    #INITIALIZES ALL THE VARIABLES THAT WILL BE NEEDED A LOT FOR THE TASK
    def __init__(self, binaryTreeStr):
      self.defualtOperators = ['/', '*', '+', '-']
      self.acceptedNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      self.otherSymbol = ['(', ')']
      self.allSubStrings = self.defualtOperators + self.acceptedNums + self.otherSymbol
      self.binaryTreeStr = str(binaryTreeStr.replace(' ', ''))

    #LEVELS OF TREE CHECKS TO SEE WHAT LEVEL OF THE BINARY TREE THE OPERATOR OR NUMBER WILL BE
    def levelsOfTree(self,inputAray):
      bracketCount = 0
      levelsOfTreeArray = []
      
      #GOES THROUGH EACH STRING
      #IF THE STRING IS A BRACKET bracketCount WILL BE 
      #INCREASED OR DECREASED BY ONE FOR (, ), ACCORDINGLY
      #IF A OPERATOR OR NUMBER SPOTTED IT IS APPENDED INTO levelsOfTreeArray
      #IT IS APPENDED IN FORMAT [OPERATOR/NUMBER,LEVEL IN TREE, INDEX IN STRING TO LOCATE OPERATOR] 
      for i in range(0,len(inputAray)):
        if inputAray[i] == "(" :
          bracketCount += 1

        elif inputAray[i] == ")" :
          bracketCount -= 1

        #CHECKS IF NUMBER / OPERATOR
        if (inputAray[i] in self.defualtOperators) or (inputAray[i] in self.acceptedNums):
          levelsOfTreeArray.append([inputAray[i],bracketCount,i+1])

      return(levelsOfTreeArray) #RETURNS THE FULL LIST OF TREE

    #ENSURES STRING IS VALID; RETURNS TRUE / FALSE
    def validSubStrings(self):
        #MAKES A CLONE OF STRING FOR LOCAL USE
        currentStr = copy.copy(self.binaryTreeStr)
        isValidSubStrings = None
        #GOES THROUGH EACH CHARECTER IN STRING, IF ITS ACCEPTED SUBSTRING THEN REMOVES IT
        #IDEA IS THAT EVERTHING SHOULD BE GONE AFTER TRAVERSING, IF THERE IS LEFT OVER
        #THEN THERE IS AN INVALID CHARECTER 
        for x in range(0,len(self.allSubStrings)):
            currentStr = currentStr.replace(self.allSubStrings[x], '')

            if currentStr == '':
                isValidSubStrings = True

            else:
                isValidSubStrings = False
        return(isValidSubStrings)


    #ENSURES OPERAND : OPERATOR COUNT IS VALID; RETURNS TRUE / FALSE
    def validOperand(self):
      #MAKES A CLONE OF STRING FOR LOCAL USE
        currentStr = copy.copy(self.binaryTreeStr)
        isValiddOperand = None
        
        numCounter = 0
        operatorCounter = 0

        #COUNTS TOTAL NUMBERS AND TOTAL OPERATORS IN STRING
        #IF OPERATOR COUNT IS ONE MORE THAN NUMBER COUNT THEN ITS VALID 
        for i in range(0,len(currentStr)):
            if currentStr[i] in self.defualtOperators:
                operatorCounter +=1
            if currentStr[i] in self.acceptedNums:
                numCounter +=1
       
        #(operatorCounter > 0) and (numCounter > 1) TO ENSURE 
        #JUST ONE NUMBER ISN'T GOING TO BR ACCEPTED
        if ((operatorCounter+1) == numCounter) and (operatorCounter > 0) and (numCounter > 1):
           isValiddOperand = True
        else:
           isValiddOperand = False
        
        return isValiddOperand
        
    #ENSURES BRACKET NUMBER IS VALID; RETURNS TRUE / FALSE
    def validBrackets(self):
      #JUST COUNTS OUT TOTAL CLOSING AND OPENING BRACKETS
        isValidBrackets = None
        #MAKES A CLONE OF STRING FOR LOCAL USE
        currentStr = copy.copy(self.binaryTreeStr)
        openBracket = currentStr.count("(")
        closeBracket = currentStr.count(")")
        #IF THE DIFFERENCE OF BOTH NUMBER IS 0 THEN THERE IS
        #NO BRACKET MISMATCH 
        if openBracket != closeBracket:
            isValidBrackets = False
        else:
            isValidBrackets = True

        return(isValidBrackets)


    #CALLS ALL THE STRING VALIDATING METHODS AND PRESENTS RESULTS
    def validateString(self):

      #CALLS METHODS
        isValidSubStrings = self.validSubStrings()
        isValidBrackets = self.validBrackets()
        isValidOperand = self.validOperand()

      #IF A FALSE IS RETURNED THEN THERE IS AN OUTPUT EXPLAINING WHAT IS WRONG
        if isValidBrackets == False:
            print("Not a valid expression, bracket mismatched")
        if isValidSubStrings == False:
            print("Not a valid expression, unrecognised charecters")
        if isValidOperand == False:
            print("Not a valid expression, operator missing.") 
      #RETURNS ALL VALUES SO ITS CLEAR TO SEE WHAT PROBLEM IS
        return isValidSubStrings, isValidBrackets, isValidOperand

    #ADDS ALL THE ELEMENTS ONE BY ONE TO THE TREE RECURSIVELY
    def addToTree(self,workinglevelsOfTreeArray):
      #THIS VARIABLE IS LOADED WITH A SMALL NUMBER TO ALLOW THE FOR LOOP TO WORK PROPERLY#
      #IF IT WAS LOADED WITH NONE OR ZERO THEN IT WOULDNT WORK AS IT WOULD TRY TO COMPARE
      #THE NONE VALUE TO AN INT  
      minBracketDepth = workinglevelsOfTreeArray[0][1]
      
      for i in range(0,len(workinglevelsOfTreeArray)):
        #FINDS THE SMALLEST NUMBER OR BRACKETS TO TRAVERSE TILL AN EXPRESSION AND NUMBER IS FOUND
        if workinglevelsOfTreeArray[i][1] <= minBracketDepth:
          minBracketDepth = workinglevelsOfTreeArray[i][1]
         
      #USES NESTED IF STATEMENT TO DECIDE IF THE CURRENT INDEX IS A NUMBER OR A NUMBER
      #THE NUMBER TO THE LEFT IS SAVED TO LEFT AND VICE VERSA, IF A SYMBOL IS FOUND THEN IT CALLS ITSELF
      #RECURSIVLY AND KEEPS GOING UNTILL NUMBERS AND SYMBOLS ARE FOUND 
      for y in range(0,len(workinglevelsOfTreeArray)):
          if (workinglevelsOfTreeArray[y][1] == minBracketDepth) & (workinglevelsOfTreeArray[y][0] in self.defualtOperators):
            node = Node(workinglevelsOfTreeArray[y][0])
            # A QUICK EXAMPLE BELOW
            # [1,2,3,4,5] MAKES INTO [1,2],[4,5] MAKES 3 THE ROOT NODE
            if workinglevelsOfTreeArray[y-1][1] == minBracketDepth:
              node.left = Node(workinglevelsOfTreeArray[y-1][0])

            else:
              leftArray = workinglevelsOfTreeArray[:(y)]
              node.left = self.addToTree(leftArray)


            if workinglevelsOfTreeArray[y+1][1] == minBracketDepth:
              node.right = Node(workinglevelsOfTreeArray[y+1][0])

            else:
              rightArray = workinglevelsOfTreeArray[(y+1):]
              node.right = self.addToTree(rightArray)

            #END OF RECUSION WHERE EVERTHING CAN BE SAVED
            return node
            break
          
    #CO-ORDINATES ALL THE MEHODS NEEDED TO MAKE A BINARY TREE FROM VALID EXPRESSION     
    def main(self):
        #ENSURES THAT THE STRING IS VALID SO IT CAN CONTINUE
        isValidSubStrings, isValidBrackets,  isValidOperand = False, False,  False
        #KEEPS ASKING TILL A VALID STRING INPUTTED
        #IF ANY OF THE THREE CHECKS COME BACK FALSE THEN IT CAN'T ESCAPE WHILE LOOP
        while (isValidSubStrings == False) or (isValidBrackets == False) or (isValidOperand == False):
            #THIS IS USEFUL TO BREAK OUT IF AN INPUT IS VALID IT WILL ENSURE THAT ITS POSSIBLE TO CHECK AGAIN
            isValidSubStrings, isValidBrackets, isValidOperand = self.validateString()
            if (isValidSubStrings == False) or (isValidBrackets == False) or (isValidOperand == False):
                experessionIn = ("("+str(input(" \n\nINCORRECT INPUT, PLEASE ENTER YOUR EXPRESSION CORRECTLY: "))+")")
                self.binaryTreeStr = experessionIn

        #MAKES THE STRING INTO LIST STRIPPING THE FIRST SET
        #OF BRACKETS TO MAKE EASIER TO MANIPULATE AND WORK WITH
        workingInputList = list(self.binaryTreeStr[1:-1])
        expressionTree = self.addToTree(self.levelsOfTree(workingInputList))
        #JUST FOR FORMATTING AND AESTHETICS
        clearConsoleMessage(str("                         ANSWER \n                        --------- \n THE ANSWER TO YOUR EXPRESSION "+str(self.binaryTreeStr)+" IS: "+str(evaluateTree(expressionTree))+""""""))
        print(""" BINARY TREE:""")
        #SHOWS TREE IN TERMINAL
        treeToTerminal(expressionTree,0)
        #JUST FOR FORMATTING AND AESTHETICS
        print("------------------------------------------------------------")
        #SERIALIZES THE TREE FOR FUTURE USE
        saveTree(expressionTree)
        
        


#IF FILE IS IMPORTED THEN IT WONT AUTOMATICALLY RUN MAIN
if __name__ == "__main__":
  menu()
