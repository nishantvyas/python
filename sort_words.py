"""
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
def sortWords(string):
    """

    :param string:
    :return:
    """
    input_list = [x for x in string.split(',')]
    input_list.sort()
    return input_list

if __name__ == "__main__":
    """
    """
    input_string = "without,hello,bag,world"
    print(','.join(sortWords(input_string)))