# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: 2 - Bag
# Description: This program uses the Dynamic array
# in order to make useful command that is useful
# for the bag data structure

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of bag in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag
        """
        self.da.append(value)
        return

    def remove(self, value: object) -> bool:
        """
        Removes an element in the bag
        """

        # looks through the whole length and remove at a certain index
        for num in range(self.da.length()):
            if self.da.get_at_index(num) == value:
                self.da.remove_at_index(num)                # remove the number
                return True
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of element in the bag that
        matches the value
        """

        count = 0
        for pos in range(self.da.length()):
            if self.da.get_at_index(pos) == value:      # finds the value at certain index
                count += 1

        return count

    def clear(self) -> None:
        """
        clear the contents in the bag
        """
        for pos in range(self.da.length()):
            self.da.remove_at_index(0)              # remove at certain index
        return

    def size(self) -> int:
        """
        returns the number of element currently in the bag
        """
        return self.da.length()

    def equal(self, second_bag: object) -> bool:
        """
        returns true when the bag are equal, if not then
        return false
        """

        # Copying the first and second bag in order to modify this later
        first_holder = DynamicArray()
        second_holder = DynamicArray()
        for num in range(self.da.length()):
            first_holder.append(self.da.get_at_index(num))

        for num in range(second_bag.da.length()):
            second_holder.append(second_bag.da.get_at_index(num))

        # sorting the copy of the first and second bag
        first_holder.sort()                                # sort first bag
        first_len = first_holder.length()                  # first bag length
        second_holder.sort()                               # sort second bag
        second_len = second_holder.length()                # second bag

        # if both bags are empty, return true
        if first_len == 0 and second_len == 0:
            return True

        # if all the elements are the same, return True, else return false
        if first_len == second_len:
            for num in range(first_len):
                if first_holder.get_at_index(num) != second_holder.get_at_index(num):
                    return False
            return True

        return False





# BASIC TESTING
if __name__ == "__main__":
    pass

    # # add example 1
    # bag = Bag()
    # print(bag)
    # values = [10, 20, 30, 10, 20, 30]
    # for value in values:
    #     bag.add(value)
    # print(bag)

    # # remove example 1
    # bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(bag)
    # print(bag.remove(7), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)

    # # count example 1
    # bag = Bag([1, 2, 3, 1, 2, 2])
    # print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    # # clear example 1
    # bag = Bag([1, 2, 3, 1, 2, 3])
    # print(bag)
    # bag.clear()
    # print(bag)

    # # size example 1
    # bag = Bag([10, 20, 30, 40])
    # print(bag.size(), bag.remove(30), bag.size())
    # bag.clear()
    # print(bag.size())

    # equal example 1
    bag1 = Bag([1, 2, 3, 4, 5, 6])
    bag2 = Bag([6, 5, 4, 3, 2, 1])
    bag3 = Bag([1, 2, 3, 4, 5])
    bag_empty = Bag()
    #
    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")
