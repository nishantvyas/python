"""
Write a program which can compute the factorial of a given numbers.
The results should be also be printed in a comma-separated sequence on a single line.
"""
def factorial(number=1):
    """

    :param number:
    :return:
    """
    if number == 1:
        factorial_list.append(number)
        return 1
    else:
        factorial_list.append(number)
        return (number * factorial(number-1))

if __name__ == "__main__":
    """
    """
    factorial_list=[]
    print(factorial(3))
    print(factorial_list)
