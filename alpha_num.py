"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

"""
def countAlphaNumeric(string):
    """

    :param string:
    :return:
    """
    count_alpha = 0
    count_numbers = 0

    for char in string:
        if char.isdigit():
            count_numbers += 1
        elif char.isalpha():
            count_alpha += 1

    print(f"LETTERS {count_alpha}")
    print(f"DIGITS {count_numbers}")


if __name__ == "__main__":
    """
    """
    countAlphaNumeric("Hello World! 123")