import copy
string = '(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)'


def bracketMatching(self, string):
    openBracketIndexSaver = []
    sortingArray = []
    unsortedIndexArray = []
    completeArray = []

    for i in range(0,len(string)):
        print(string[i])
        if string[i] == '(':
            openBracketIndexSaver.append(i)
            sortingArray.append(i)
        elif string[i] == ')':
            print(openBracketIndexSaver)
            unsortedIndexArray.append( [ openBracketIndexSaver.pop(),i ])


    for x in range(0,len(sortingArray)):
        for y in range(0,len(unsortedIndexArray)):
            if unsortedIndexArray[y][0] == sortingArray[x]:
                completeArray.append(unsortedIndexArray[y])
                break






print(completeArray)


print(unsortedIndexArray)





# [(1, 35), (2, 14), (3, 7), (9, 13), (16, 32), (17, 21), (23, 31), (24, 28)]