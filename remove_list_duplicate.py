"""
write a program to print this list after removing all duplicate values with original order reserved.
With a given list [12,24,35,24,88,120,155,88,120,155], output should be
[12,24,35,88,120,155]

"""

def remove_list_duplicates(list):
    """

    :param list:
    :return list:
    """
    return_list = []
    for iteration in range(len(list)):
        if not list[iteration] in return_list:
            return_list.append(list[iteration])

    return return_list

if __name__ == "__main__":
    """
    """
    my_list = [12,24,35,24,88,120,155,88,120,155]
    print(remove_list_duplicates(my_list))