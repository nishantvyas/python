"""
Reverse a String - Enter a string and the program will reverse it and print it out.
"""

def reverse_string(string=None):
    return string[::-1]

def is_pelindrome(string=None):
    if string == string[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    """
    """

    print(reverse_string("Nishant"))
    print(reverse_string("Hello World!"))
    print(reverse_string("madam"))

    print(is_pelindrome("madam"))
    print(is_pelindrome("nishant"))