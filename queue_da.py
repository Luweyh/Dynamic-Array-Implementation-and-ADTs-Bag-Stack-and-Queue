# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: 2 - Queue
# Description: This program uses the dynamic array to make
# a Queue ADT class. This class has useful command such as
# enqueu, dequeue, is_empty, and size.

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def enqueue(self, value: object) -> None:
        """
        adds a new value to the end of the queue
        """
        self.da.append(value)
        return

    def dequeue(self) -> object:
        """
        removes and return value at the beginning
        of the queue
        """

        # if the queue is empty
        if self.da.length() == 0:
            raise QueueException

        first_val = self.da.get_at_index(0)     # finds the first val
        self.da.remove_at_index(0)              # removes val at first index

        return first_val

    def is_empty(self) -> bool:
        """
        checks to see if the queue is empty
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        returns the number of elements in the queue
        """
        return self.da.length()


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # enqueue example 1
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)

    # # dequeue example 1
    # q = Queue()
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    # for i in range(6):
    #     try:
    #         print(q.dequeue())
    #     except Exception as e:
    #         print("No elements in queue", type(e))

    # # is_empty example 1
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(10)
    # print(q.is_empty())
    # q.dequeue()
    # print(q.is_empty())
    #
    # # size example 1
    # q = Queue()
    # print(q.size())
    # for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    # print(q.size())