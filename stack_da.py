# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: 2 - Stack
# Description: This program uses the dynamic array
#  in order to make useful python command to identify
# stuff for the stack


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def push(self, value: object) -> None:
        """
        adds a new element to the top of the stack
        """
        self.da.append(value)
        return

    def pop(self) -> object:
        """
        remove the top element from the stack
        """

        # if the stack is empty raise exception
        if self.da.length() == 0:
            raise StackException

        # finds the last index
        last_index = self.da.get_at_index(self.da.length() - 1)

        # remove the last element
        self.da.remove_at_index(self.da.length() - 1)

        return last_index

    def top(self) -> object:
        """
        returns the top element of the stack
        """

        # stack cant be empty
        if self.da.length() == 0:
            raise StackException

        # finds the last index
        last_index = self.da.get_at_index(self.da.length() - 1)

        return last_index

    def is_empty(self) -> bool:
        """
        Checks to see if there are elements in the stack
        """

        return self.da.is_empty()

    def size(self) -> int:
        """
        finds the number of elements in the stack
        """
        return self.da.length()




# BASIC TESTING
if __name__ == "__main__":
    pass

    # # push example 1
    # s = Stack()
    # print(s)
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s)

    # # pop example 1
    # s = Stack()
    # try:
    #     print(s.pop())
    # except Exception as e:
    #     print("Exception:", type(e))
    #
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    #
    # for i in range(6):
    #     try:
    #         print(s.pop())
    #     except Exception as e:
    #         print("Exception:", type(e))

    # # top example 1
    # s = Stack()
    # try:
    #     s.top()
    # except Exception as e:
    #     print("No elements in stack", type(e))
    # s.push(10)
    # s.push(20)
    # print(s)
    # print(s.top())
    # print(s.top())
    # print(s)

    # # is_empty example 1
    # s = Stack()
    # print(s.is_empty())
    # s.push(10)
    # print(s.is_empty())
    # s.pop()
    # print(s.is_empty())

    # # size example 1
    # s = Stack()
    # print(s.size())
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s.size())
