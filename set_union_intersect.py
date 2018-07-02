"""
Set intersection and Union.
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.

"""

def set_union(listObj1, listObj2):
    """
    
    :param listObj1: 
    :param listObj2: 
    :return: 
    """
    return set(listObj1) | set(listObj2)

def set_intersect(listObj1, listObj2):
    """
    
    :param listObj1: 
    :param listObj2: 
    :return: 
    """
    return set(listObj1) & set(listObj2)


if __name__ == "__main__":
    """
    """
    list1 = [1,3,6,78,35,55]
    list2 = [12,24,35,24,88,120,155]

    print(set_intersect(list1,list2))
    print(set_union(list1,list2))