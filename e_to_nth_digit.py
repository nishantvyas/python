'''
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

'''
import math

def e(precision=2):

    """
    > n = 4
    > p = math.e
    > '{0:.{1}f}'.format(p, n)
    > '2.7182'
    the nested {1} takes the second argument, the current value of n, and applies it as specified (here, to the "precision" part of the format --
    number of digits after the decimal point), and the outer resulting {0:.4f} then applies.
    """

    return '{number:.{digits}f}'.format(number=math.e, digits=precision)

if __name__ == "__main__":

    my_e = e(precision=10)
    print(my_e)