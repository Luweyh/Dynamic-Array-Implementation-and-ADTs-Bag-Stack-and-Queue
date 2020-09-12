# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: 2 - Dynamic Array
# Description: This program represent a dynamic array that
# has its own python specific feature that is manually built.
# It also has other methods that is not directly a python
# command but can be useful for the array such as is_empty()
# or slice(). The program builds on each other by calling other
# methods that acts as a python command


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/"+ str(self.capacity)
        out += " " + str(self.data[:self.size])
        return out

    def resize(self, new_capacity: int) -> None:
        """
        resize the capacity only if it is positive and greater
        than the size
        """
        if new_capacity >= 0 and new_capacity > self.size:

            # update the capacity
            self.capacity = new_capacity

            new_array = [None] * self.capacity      # None filling the array
            count = 0

            # make a new array that fills up only to the size. (remove's the extra Nones)
            for pos in range(self.size):
                new_array[pos] = self.data[pos]
                count += 1

            # find the size difference between capacity and current size
            size_diff = new_capacity - self.size

            # None fill the arrays by the difference
            for num in range(count, size_diff):
                new_array[num] = None

            self.data = new_array

        return

    def append(self, value: object) -> None:
        """
        Appends an element to the end of the array. It doubles
        the array size when it is filled
        """

        # Increase capacity when full and then append
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
            self.data[self.size] = value
            self.size += 1

        # Append the value
        else:
            self.data[self.size] = value
            self.size += 1

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        insert a value at a certain index in the array
        """

        # validates to see if inserting work
        if index > self.size or index < 0:
            raise DynamicArrayException

        old_array = self.data                       # create an array for storage
        self.data = [None] * self.capacity
        self.size += 1

        # double capacity when it is full
        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        for pos in range(self.size):

            # when the index is found, insert the value
            if pos == index:
                old_spot = old_array[index]
                self.data[index] = value
                self.data[index+1] = old_spot

            # inputting the old value that is AFTER the index
            elif pos > index and pos < self.size:
                self.data[pos+1] = old_array[pos]

            # inputing the old value that is BEFORE the index
            else:
                self.data[pos] = old_array[pos]

        return

    def get_at_index(self, index: int) -> object:
        """
        returns the value from a specific index
        """
        return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        removes at a specific index. also reduces capacity
        when capacity is 4x larger than size
        """

        if index >= self.size or index < 0:
            raise DynamicArrayException

        # reduce twice amount of  current element if size is 1/4 of capacity
        if self.size < (self.capacity/4):
            self.capacity = self.size * 2

            # capacity can't be less than 10
            if self.size * 2 < 10:
                self.capacity = 10

        new_array = [None] * self.capacity

        # removing at a certain index
        pos_2 = 0
        for pos in range(self.size):
            if pos == index:
                self.size -= 1

            else:
                new_array[pos_2] = self.data[pos]
                pos_2 += 1

        self.data = new_array
        # self.size -= 1

        return

    def is_empty(self) -> bool:
        """
        Returns true if there are no elements in the array,
        otherwise returns false
        """

        if self.size == 0:      # empty when the size is 0
            return True

        return False

    def length(self) -> int:
        """
        Finds the number of elements in the array
        """

        return self.size

    def slice(self, start_index: int, quantity: int) -> object:
        """
        Slices the array by having a starting index and a quantity to
        tell when it to stop
        """

        # validation to check to see if slice can work
        if start_index < 0 or quantity > self.size or (start_index + quantity) > self.size:
            raise DynamicArrayException

        new_array = DynamicArray()

        # slices at a start_index and ends at the quantity
        for num in range(self.length()):
            if num in range(start_index, start_index + quantity):
                new_array.append(self.get_at_index(num))

        return new_array

    def reverse(self) -> None:
        """
        Reverses the array
        """
        back_pos = self.size - 1       # the backwards position in the array

        # iterate through half the size
        for pos in range(int(self.size/2)):
            old_val = self.data[pos]                        # save old value
            self.data[pos] = self.data[back_pos]            # front becomes end
            self.data[back_pos] = old_val                   # end becomes front
            back_pos -= 1

        return

    def sort(self) -> None:
        """
        Sorts the array
        """
        for num in range(self.size):                # iterating through how many elements in array

            # iteration for swapping elements
            for pos in range(self.size - 1):
                if self.data[pos] > self.data[pos + 1]:
                    temp_pos = self.data[pos]                   # save old position
                    self.data[pos] = self.data[pos + 1]         # left element becomes right
                    self.data[pos + 1] = temp_pos               # right element becomes left

        return

    def merge(self, another_list: object) -> None:
        """
        Merges another list to the dynamic array
        """

        # iterate through length of the list and then append the list
        for num in range(another_list.length()):
            self.append(another_list.get_at_index(num))

        return


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # resize - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.resize(10)
    # print(da.size, da.capacity, da.data)
    # da.resize(2)
    # print(da.size, da.capacity, da.data)
    # da.resize(0)
    # print(da.size, da.capacity, da.data)

    # resize - example 2
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # # append - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)
    # #
    # # append - example 2
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)

    # # append - example 3
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.size)
    # print(da.capacity)

    # # insert_at_index - example 1
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # # insert_at_index example 2
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)

    # insert at index example 3
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Can not insert value", value, "at index", index)
    # print(da)

    # # get_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50])
    # print(da)
    # for i in range(4, -1, -1):
    #     print(da.get_at_index(i))

    # get_at_index example 2
    # da = DynamicArray([100, 200, 300, 400, 500])
    # print(da)
    # for i in range(-1, 7):
    #     try:
    #         print("Index", i, ": value", da.get_at_index(i))
    #     except Exception as e:
    #         print("Index", i, ": exception occured")
    #
    # remove_at_index - example 1
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    # remove_at_index - example 2
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    # remove_at_index - example 3
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                      # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)

    # # is_empty - example 1
    # da = DynamicArray()
    # print(da.is_empty(), da)
    # da.append(100)
    # print(da.is_empty(), da)
    # da.remove_at_index(0)
    # print(da.is_empty(), da)

    # # length - example 1
    # da = DynamicArray()
    # print(da.length())
    # for i in range(10000):
    #     da.append(i)
    # print(da.length())
    # for i in range(9999, 5000, -1):
    #     da.remove_at_index(i)
    # print(da.length())

    # # slice example 1
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")

    # # slice example 2
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOUCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")

    # # merge example 1
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)

    # # merge example 2
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)

    # # reverse example 1
    # da = DynamicArray([4, 5, 6, 7, 8, 9])
    # print(da)
    # da.reverse()
    # print(da)
    # da.reverse()
    # print(da)

    # # reverse example 2
    # da = DynamicArray()
    # da.reverse()
    # print(da)
    # da.append(100)
    # da.reverse()
    # print(da)

    # # sort example 1
    # da = DynamicArray([1, 10, 2, 20, 3, 30, 4, 40, 5])
    # print(da)
    # da.sort()
    # print(da)
