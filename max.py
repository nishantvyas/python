"""
Function to find max of any type of number input
"""

import math

def my_max(*args):

    unpacked_number_list = []

    for num in args:
        if isinstance(num,list):
            for i in num:
                unpacked_number_list.append(i)
        elif isinstance(num, tuple):
            for i in num:
                unpacked_number_list.append(i)
        elif isinstance(num,int):
            unpacked_number_list.append(num)
        elif isinstance(num,float):
            unpacked_number_list.append(num)
        elif isinstance(num,str):
            continue
        else:
            continue

    max_number = max(unpacked_number_list)
    print(f"Max number of given input {args} is {max_number}")

if __name__ == "__main__":
    """
    """
    ###some test cases
    my_max(10,20)
    my_max(30,10)
    my_max(-5,5)
    my_max(0,0)
    my_max(-10,0)
    my_max(4,5,6,7,8,9)
    my_max([1,2,3])
    my_max([44,55],(66,77),99,-10,99.99)