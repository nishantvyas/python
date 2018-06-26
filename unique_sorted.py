"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

"""

def printListString(listObj):
    """
    This function prints the data in list line by line
    :param listObj:
    :return:
    """
    print(" ".join(listObj))

def uniqueWords(stringObj):
    """
    This function takes text string as input and returns the string of unique words
    :param stringObj:
    :return:
    """
    returnListObj = []
    inputListObj = [x for x in stringObj.split()]
    for i in range(0,len(inputListObj)):
        if not inputListObj[i] in returnListObj:
            returnListObj.append(inputListObj[i])

    return returnListObj

def sortWords(listObj):
    """
    This function takes list of words as input and returns the sorted list
    :param listObj:
    :return:
    """
    listObj.sort()
    return listObj

if __name__ == "__main__":
    """
    """
    inputList = []
    print("Enter text to be sorted on unique words:")
    while True:
        stringObj = input()
        if stringObj:
            inputList = sortWords(uniqueWords(stringObj))
        else:
            break
    printListString(inputList)
