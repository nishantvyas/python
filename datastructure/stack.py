"""
Stack datastructure implementation using python list
Following methods of stacks are implemented, push(item), pop(), peek()
"""

class stack():
    """
    class implementation of stack data structure
    """
    def __init__(self):
        """
        initialize the objects with emplty list
        """
        self.__stack = []
        print("Stack is initialized.")

    def stack_size(self):
        """
        size of the stack
        :return int:
        """
        return len(self.__stack)

    def printStack(self):
        """

        :return list:
        """
        return self.__stack[::-1]

    def push(self, item):
        """

        :param item:
        :return boolean:
        """
        try:
            self.__stack.append(item)
            return True
        except:
            return False

    def pop(self):
        """

        :return item:
        """
        try:
            if self.stack_size() > 0:
                ##pop method would do the job too
                item = self.__stack[-1]
                print(f"Item {item} is popped. New size of the stack is {self.stack_size()}")
                del self.__stack[-1]
                return item
            else:
                print("Stack is empty.")
        except:
            return None

    def peek(self):
        """

        :return item:
        """
        try:
            if self.stack_size() > 0:
                print(f"Item {self.__stack[-1]} is peeked.")
                return self.__stack[-1]
            else:
                print("Stack is empty.")
        except:
            return None


if __name__ == "__main__":
    """
    """
    mystack = stack()
    items_list = [22,33,44,55]
    for item in items_list:
        print(f"PUSH: Item {item} pushed to stack. New size of the stack is {mystack.stack_size()}") if mystack.push(item) else print("Item pushed failed")

    print(mystack.printStack())

    poped_item = mystack.pop()
    print(f"Popped item was {poped_item}")

    print(mystack.printStack())

    peeked_item = mystack.peek()
    print(f"Peeked item was {peeked_item}")
