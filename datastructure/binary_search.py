class node():
    """
    template for each node instance
    """
    def __init__(self,data):
        """
        initialize each node with left, right child and data.
        """
        self.right_child = None
        self.left_child = None
        self.data = data

class binarySearch():
    """
    Base class for binary search methods.
    """
    def __init__(self):
        """
        initialize binary search variables.
        """
        self.root_node = None
        self.level = 0

    def insert(self, data):
        """
        insert data in binary tree
        :param data:
        :return:
        """
        ## check if there are any nodes in tree
        if not self.root_node:
            self.root_node = node(data)
        else:
            self.insertNode(self.root_node, data)

    def insertNode(self, root_node, data):
        """
        recursively add node to the correct position in tree
        :param root_node:
        :param data:
        :return:
        """

        if data > root_node.data:
            if root_node.right_child:
                self.insertNode(root_node.right_child, data)
            else:
                child_node = node(data)
                root_node.right_child = child_node
        else:
            if root_node.left_child:
                self.insertNode(root_node.left_child, data)
            else:
                child_node = node(data)
                root_node.left_child = child_node


if __name__ == "__main__":
    """
    Test binary search methods
    """
    new_tree = binarySearch()
    #root node
    new_tree.insert(5)
    #left child
    new_tree.insert(3)
    #left_child
    new_tree.insert(4)
    #right_child
    new_tree.insert(7)
    ### print to see if tree is created.
    print(new_tree.root_node.data)
    print(new_tree.root_node.left_child.data)
    print(new_tree.root_node.left_child.right_child.data)
    print(new_tree.root_node.right_child.data)
