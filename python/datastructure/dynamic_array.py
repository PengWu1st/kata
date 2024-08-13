"""
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.


Note:

The index i provided to get(int i) and set(int i) is guranteed to be greater than or equal to 0 and less than the number of elements in the array.
"""
from unittest import TestCase

class DynamicArray:

    def __init__(self, capacity: int) -> None:
        self._array = [0]*capacity
        self._cap = capacity
        self._size = 0

    @property
    def capacity(self) -> int:
        return self._cap

    @property
    def size(self) -> int:
        return self._size

    def __setitem__(self, i: int, n: int) -> None:
        self._array[i] = n
    
    def __getitem__(self, i: int) -> int:
        return self._array[i]

    def pushback(self, n: int) -> None:
        if self._size == self._cap:
            self.resize()
        self._array[self._size] = n
        self._size += 1


    def popback(self) -> int:
        self._size -= 1
        return self._array[self._size]

    def resize(self):
        self._cap *= 2
        new_array = [0] * self._cap
        for i, n in enumerate(self._array):
            new_array[i] = n
        self._array = new_array

class TestDynamicArray(TestCase):

    def test_should_raise_exception_if_index_out_of_range(self):
        da = DynamicArray(2)
        self.assertRaises(IndexError, lambda :da[3])

    def test_pushback(self):
        da = DynamicArray(2)
        da.pushback(1)
        self.assertEqual(da[0], 1)

    
    def test_set_and_get(self):
        da = DynamicArray(2)
        da[0] = 1
        self.assertEqual(da[0], 1)

    def test_popback(self):
        da = DynamicArray(2)
        da.pushback(1)
        self.assertEqual(da.popback(), 1)


    def test_example_0(self):
        """
        Example 1:

        Input:
        ["Array", 1, "getSize", "getCapacity"]

        Output:
        [null, 0, 1]
        """
        da = DynamicArray(1)
        self.assertEqual(da.size, 0)
        self.assertEqual(da.capacity, 1)

    def test_example_1(self):
        """
        Example 2:

        Input:
        ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

        Output:
        [null, null, 1, null, 2]
        """
        da = DynamicArray(1)
        da.pushback(1)
        self.assertEqual(da.capacity, 1)
        da.pushback(2)
        self.assertEqual(da.capacity, 2)

    
    def test_example_3(self):
        """
         Example 3:

        Input:
        ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

        Output:
        [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]       
        """

        da = DynamicArray(1)
        self.assertEqual(da.size, 0)
        self.assertEqual(da.capacity, 1)
        da.pushback(1)
        self.assertEqual(da.size, 1)
        self.assertEqual(da.capacity, 1)
        da.pushback(2)
        self.assertEqual(da.size, 2)
        self.assertEqual(da.capacity, 2)
        self.assertEqual(da[1], 2)
        da[1] = 3
        self.assertEqual(da[1], 3)
        self.assertEqual(da.popback(), 3)
        self.assertEqual(da.size, 1)
        self.assertEqual(da.capacity, 2)