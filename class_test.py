"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class TestClass():
    """

    """
    def __init__(self):
        """

        """
        textObj = "default text"

    def getString(self):
        """

        :return:
        """
        self.textObj = input("Enter your string input:")

    def printString(self):
        """

        :return:
        """
        print(f"Your string is, {self.textObj.upper()}")

if __name__ == "__main__":
    """
    """
    string1 = TestClass()
    string1.getString()
    string1.printString()