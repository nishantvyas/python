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

    def traverse(self,type="inorder"):
        """
        tree traverse
        :return:
        """
        self.btree_list = []

        if self.root_node:
            if type == "inorder":
                self.traverse_inorder(self.root_node)
            elif type == "preorder":
                self.traverse_preorder(self.root_node)
            elif type == "postorder":
                self.traverse_postorder(self.root_node)
            else:
                print("unknown type of ordering")

            return self.btree_list
        else:
            print("No nodes in tree")
            return

    def traverse_inorder(self, root_node):
        """
        inorder traverse: left, root, right and so on
        :param root_node:
        :return :
        """
        ##left
        if root_node.left_child:
            self.traverse_inorder(root_node.left_child)

        ##root
        self.btree_list.append(root_node.data)

        ##right
        if root_node.right_child:
            self.traverse_inorder(root_node.right_child)


    def traverse_preorder(self, root_node):
        """
        preorder traverse: root, left, right and so on
        :param root_node:
        :return :
        """
        ##root
        self.btree_list.append(root_node.data)

        ##left
        if root_node.left_child:
            self.traverse_preorder(root_node.left_child)

        ##right
        if root_node.right_child:
            self.traverse_preorder(root_node.right_child)

    def traverse_postorder(self, root_node):
        """
        postorder traverse: left, right, root and so on
        :param root_node:
        :return :
        """

        ##left
        if root_node.left_child:
            self.traverse_postorder(root_node.left_child)

        ##right
        if root_node.right_child:
            self.traverse_postorder(root_node.right_child)

        ##root
        self.btree_list.append(root_node.data)

    def getMinValue(self):
        """

        :return:
        """
        self.min_value = None

        if self.root_node:
            self.findMin(self.root_node)

        return self.min_value

    def findMin(self, node):
        """

        :param root_node:
        :return:
        """
        if node.left_child:
            self.findMin(node.left_child)
        else:
            self.min_value = node.data

    def getMaxValue(self):
        """

        :return:
        """
        self.max_value = None

        if self.root_node:
            self.findMax(self.root_node)

        return self.max_value

    def findMax(self, node):
        """

        :param root_node:
        :return:
        """
        if node.right_child:
            self.findMax(node.right_child)
        else:
            self.max_value = node.data

    def removeNode(self, data, node):
        """

        :param data:
        :param node:
        :return:
        """

        if not node:
            return node;

        if data < node.data:
            node.left_child = self.removeNode(data, node.left_child);
        elif data > node.data:
            node.right_child = self.removeNode(data, node.right_child);
        else:

            if not node.left_child and not node.right_child:
                print("Removing a leaf node...");
                del node;
                return None;

            if not node.left_child:  # node !!!
                print("Removing a node with single right child...");
                tempNode = node.right_child;
                del node;
                return tempNode;
            elif not node.right_child:  # node instead of self
                print("Removing a node with single left child...");
                tempNode = node.left_child;
                del node;
                return tempNode;

            print("Removing node with two children....");
            tempNode = self.getPredecessor(node.left_child);  # self instead of elf  + get predecessor
            node.data = tempNode.data;
            node.left_child = self.removeNode(tempNode.data, node.left_child);

        return node;  # !!!!!!!!!!!!

    def getPredecessor(self, node):

        if node.right_child:
            return self.getPredeccor(node.right_child);

        return node;

    def remove(self, data):
        if self.root_node:
            self.root_node = self.removeNode(data, self.root_node);


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
    print(new_tree.traverse(type="inorder"))
    print(new_tree.traverse(type="preorder"))
    print(new_tree.traverse(type="postorder"))

    print(new_tree.getMinValue())
    print(new_tree.getMaxValue())

    ##testing removal
    new_tree.insert(9)
    new_tree.insert(11)
    new_tree.insert(13)
    new_tree.insert(2)

    print(new_tree.traverse(type="inorder"))
    new_tree.remove(7)

    print(new_tree.traverse(type="inorder"))

