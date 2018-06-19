"""
Generate i*i dictionary. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""

def square(number=1):
    """

    :param number:
    :return:
    """
    return number**2

def gen_dict(number=1):
    """

    :param number:
    :return:
    """
    square_dict={}
    for i in range (1,number+1):
        square_dict[i]=square(i)

    return square_dict

if __name__ == "__main__":
    """
    """
    print(gen_dict(3))
    print(gen_dict(8))