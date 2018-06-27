"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def checkEvenDigits(string):
    """
    This functions finds if all digits of a number is even or not.
    :param number:
    :return boolean:
    """
    if isinstance(string,int):
        string = str(string)

    for digit in string:
        if not int(digit) % 2 == 0:
            return False

    return True


if __name__ == "__main__":
    """
    """

    ## Code to check if given number has all even digits
    """
    number = 200
    if checkEvenDigits(str(number)):
        print(f"{number} has all even digits")
    else:
        print(f"{number} does NOT have all even digits")
    """

    ##find all numbers between 1000 and 2000 with all even digits
    all_even_digits = []
    min_range = 1000
    max_range = 2600

    for number in range(min_range,max_range):
        if checkEvenDigits(number):
            all_even_digits.append(number)

    print(f"List of all event digits between {min_range} and {max_range}")
    print(all_even_digits)
