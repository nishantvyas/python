"""
Fizz Buzz - Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""

def print_fizzbuzz(start=1, end=10):
    """

    :param start:
    :param end:
    :return:
    """

    for i in range(start,end+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def print_fizzbuzz_2(start=1, end=10):
    """

    :param start:
    :param end:
    :return:
    """
    for i in range(start, end+1):
        string = ""

        if i % 3 == 0:
            string = f"{string}Fizz"
        if i % 5 == 0:
            string = f"{string}Buzz"
        if i % 3 !=0 and i % 5 !=0:
            string = f"{i}"
        print(string)

if __name__ == "__main__":
    """
    """
    print_fizzbuzz(1,20)
    print_fizzbuzz_2(1,20)

