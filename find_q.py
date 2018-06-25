"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

import math

def find_q(var_D=1):
    """

    :param var_D:
    :return:
    """
    var_C = 50
    var_H = 30
    return round(math.sqrt((2 * var_C * var_D)/ var_H))

if __name__ == "__main__":

    #input_number = "100,150,180"
    input_number = [x for x in input("Enter the string of numbers separated by comma:").split(',')]
    result_list = []
    for number in input_number:
        result_list.append(find_q(int(number)))

    print(result_list)