"""
Testing LinkedList
Every node will have data (integer value) and address to the next node.
LinkedList will have the size of the list.
"""
class linkedNode():
    """
    template for each node
    """

    #initialise each new node with data as incoming argument and load the value for nextnode address
    def __init__(self, data):
        self.data = data
        self.nextnode = None

class linkedList():
    """
    Base class for holindg the linkedlist.
    Methods:
        insert
        remove
        size
        search
        traverse
    """
    def __init__(self):
        """
        at initialization size is zero and no one is root node.
        """
        self.size = 0
        self.rootnode = None

    def listsize(self):
        """
        Size of the linkedlist
        :return number:
        """
        return self.size


if __name__ == "__main__":
    """
    """
    mylinklist = linkedList()
    print(mylinklist.listsize())