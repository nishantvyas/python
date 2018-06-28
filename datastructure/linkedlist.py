"""
Testing LinkedList
Every node will have data (integer value) and address to the next node.
LinkedList will have the size of the list.
"""

import sys

class node():
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

    def insert(self,data):
        """
        method to insert data in linkedlist.
        :param data:
        :return:
        """
        try:

            ## Create a new node with given data
            newnode = node(data)

            #First check if the size of linkedlist is zero then this will be first/root node.
            if not self.size == 0:
                newnode.nextnode = self.rootnode

            ##Increase the size of linked list
            self.size += 1

            ##assign the rootnode to newly created node
            self.rootnode = newnode

        except:
            print("Unexpected Error: " )
            raise

    def remove(self,data):
        """

        :param data:
        :return:
        """
        try:
            if self.size == 0:
                print("No nodes in list")
            else:
                currnode = self.rootnode

                if currnode.nextnode:
                    while currnode.nextnode:
                        tempnode = currnode.nextnode
                        if tempnode.data == data:
                            currnode.nextnode = tempnode.nextnode
                        elif not tempnode.nextnode:
                            break
                        else:
                            currnode = tempnode.nextnode
                else:
                    if currnode.data == data:
                        self.rootnode = None

                self.size -= 1
                print("Node is removed")
                print("Nodes left in list are")
                self.traverse()

        except:
            print("Unexpected Error: ")
            raise


    def search(self, data):
        """

        :param data:
        :return:
        """
        pass

    def traverse(self):
        """
        method with traverse thru the link list and print all data value
        :return:
        """
        try:

            currnode = self.rootnode

            if self.size == 0:
                print("No nodes in list")
            else:
                ##loop thru each node until last node and print the data
                while currnode.nextnode:
                    print(currnode.data)
                    currnode = currnode.nextnode
                #print the data of last node
                print(currnode.data)
        except:
            print("Unexpected Error: ")
            raise

if __name__ == "__main__":
    """
    """
    mylinklist = linkedList()
    mylinklist.insert(10)
    mylinklist.insert(20)
    mylinklist.insert(30)
    mylinklist.insert(40)
    mylinklist.insert(50)
    mylinklist.insert(10)
    #print(mylinklist.listsize())
    #mylinklist.traverse()
    mylinklist.remove(10)
    mylinklist.remove(50)
    mylinklist.remove(30)
    mylinklist.remove(40)
    mylinklist.remove(20)
    mylinklist.remove(10)