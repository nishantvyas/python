"""
write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

"""
def bin_search_default(list, element):
    """

    :param list:
    :param element:
    :return index:
    """

    return list.index(element)

if __name__ == "__main__":
    """
    """
    list = [2,5,7,9,11,17,222]

    print(bin_search_default(list, 11))