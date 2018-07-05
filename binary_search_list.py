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

def bin_search_new(list, element):
    """

    :param list:
    :param element:
    :return index:
    """

    index = -1
    top_of_list = len(list) - 1
    bottom_of_list = 0

    while top_of_list > bottom_of_list and index == -1:
        mid_of_list = int((top_of_list + bottom_of_list) /2)
        ##print(f"top:{top_of_list}    bottom:{bottom_of_list}    mid:{mid_of_list}")
        if list[mid_of_list] == element:
            index = mid_of_list
            return index
        elif list[mid_of_list] > element:
            top_of_list = mid_of_list
        else:
            bottom_of_list = mid_of_list

    return index

if __name__ == "__main__":
    """
    """
    list = [2,5,7,9,11,17,222]

    ##find the index of element 11 in list
    print(bin_search_default(list, 11))
    print(bin_search_new(list, 11))