"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""
def toUpper(stringObj):
    """

    :param stringObj:
    :return:
    """
    return string.upper()

def printList(listObj):
    """

    :param listObj:
    :return:
    """
    for line in listObj:
        print(line)

if __name__ == "__main__":

    userInputList = []
    print("Enter text to convert:")
    while True:
        string = input()
        if string:
            userInputList.append(toUpper(string))
        else:
            break

    print("Converted Text")
    printList(userInputList)