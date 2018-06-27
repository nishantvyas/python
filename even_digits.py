"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def allEvenDigits(numberasString):
    """
    This functions finds if all digits of a number is even or not.
    :param number:
    :return boolean:
    """
    if isinstance(numberasString,int):
        numberasString = str(numberasString)

    for digit in numberasString:
        if not int(digit) % 2 == 0:
            return False

    return True


if __name__ == "__main__":
    """
    """

    ## Code to check if given number has all even digits
    
    number = 200
    if allEvenDigits(str(number)):
        print(f"{number} has all even digits")
    else:
        print(f"{number} does NOT have all even digits")