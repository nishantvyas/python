"""
Queue data structure implementation using python list
Following methods of stacks are implemented, enqueue(item), dequeue(), peek()
"""

class queue():
    """
    class implementation of queue data structure
    """
    def __init__(self):
        """
        initialize the objects with empty list
        """
        self.__queue = []
        print("Queue is initialized.")

    def queue_size(self):
        """
        size of the queue
        :return int:
        """
        return len(self.__queue)

    def printQueue(self):
        """

        :return list:
        """
        return self.__queue[::-1]

    def enqueue(self,item):
        """

        :param item:
        :return boolean:
        """
        try:
            self.__queue.append(item)
            return True
        except:
            return False

    def dequeue(self):
        """

        :return item:
        """
        try:
            if self.queue_size() > 0:
                item = self.__queue[0]
                print(f"Item {item} is dequeued. New size of the queue is {self.queue_size()}")
                del self.__queue[0]
                return item
            else:
                print("Queue is empty.")
        except:
            return None

    def peek(self):
        """

        :return item:
        """
        try:
            if self.queue_size() > 0:
                print(f"Item {self.__queue[0]} is peeked.")
                return self.__queue[0]
            else:
                print("Queue is empty.")
        except:
            return None


if __name__ == "__main__":
    """
    """
    myqueue = queue()
    items_list = [22,33,44,55]
    for item in items_list:
        print(f"Item {item} queued. New size of the queue is {myqueue.queue_size()}") if myqueue.enqueue(item) else print("enqueuing failed")
        
    print(myqueue.printQueue())
    myqueue.dequeue()
    print(myqueue.printQueue())
    myqueue.peek()