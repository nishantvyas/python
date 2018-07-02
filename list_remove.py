"""
Write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
- By using list comprehension
- By using list native remove method
"""

def list_remove_native(listObj, item):
    """

    :param listObj:
    :param item:
    :return listObj:
    """

    while True:
        if item in listObj:
            listObj.remove(item)
        else:
            break

    return listObj

def list_remove_fast(listObj, item):
    """

    :param listObj:
    :param item:
    :return listObj:
    """

    return [x for x in listObj if x!=24 ]

if __name__ == "__main__":
    """
    """
    my_list = [12,24,35,24,88,120,155]
    print(list_remove_native(my_list, 24))
    print(list_remove_fast(my_list, 24))