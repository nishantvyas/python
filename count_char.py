"""
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

"""

def count_char(string):
    """

    :param string:
    :return dict:
    """
    char_dict = {}
    for char in string:
        if char_dict.get(char) is not None:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

if __name__ == "__main__":
    """
    """
    input_string = "abcdefgabc"
    #print(count_char(input_string))
    for k,v in count_char(input_string).items():
        print(f"{k}, {v}")