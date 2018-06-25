"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""

def stringToList(stringObj=None):
    return stringObj.split(',')

def listToTuple(listObj=None):
    return tuple(listObj)

def stringToTuple(stringObj=None):
    return listToTuple(stringToList(stringObj))

if __name__ == "__main__":
    """
    """

    my_string = "34,67,55,33,12,98"
    my_list = stringToList(my_string)
    my_tuple = stringToTuple(my_string)
    print(f"converted {my_string} of type {type(my_string)} to {my_list} of type {type(my_list)}")
    print(f"converted {my_string} of type {type(my_string)} to {my_tuple} of type {type(my_tuple)}")
