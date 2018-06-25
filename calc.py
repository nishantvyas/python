"""
simple calculator
"""

operators = ['+','-','*','/']

def getInput():
    return input(">")

def inputTextToList(text=None):
    """

    :param text:
    :return:
    """
    inputTextListObj = []
    for charcter in text.strip():
        inputTextListObj.append(charcter)

    return inputTextListObj

if __name__ == "__main__":

    print("Type EOF to end the session.")
    print('*' * 30)

    while True:
        compute = getInput()
        if compute == "EOF":
            break

