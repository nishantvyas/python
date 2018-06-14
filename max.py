"""
Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""

def my_max(number1, number2):
    if number1 > number2:
        print(f"{number1} is larger than {number2}")
    elif number1 < number2:
        print(f"{number2} is larger than {number1}")
    elif number1 == number2:
        print(f"{number1} is equal to {number2}")
    else:
        print("Something wrong with numbers")

if __name__ == "__main__":

    ###some test cases
    my_max(10,20)
    my_max(30,10)
    my_max(-5,5)
    my_max(0,0)
    my_max(-10,0)