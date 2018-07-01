"""
 write a program which prints all permutations of [1,2,3]

"""
import itertools

def permutations(listObj):
    """

    :param listObj:
    :return list of tuples:
    """
    return list(itertools.permutations(listObj))

if __name__ == "__main__":
    """
    """
    input_list = [1,2,3]
    print(permutations(input_list))