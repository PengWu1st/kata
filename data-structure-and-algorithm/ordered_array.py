
from unittest import TestCase


class OrderedArray:

    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._array = [0] * self._size
        self._length = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        for i in range(self._length):
            yield self._array[i]

    def get(self, index: int) -> int:
        return self._array[index]

    def search(self, value: int) -> int:
        low = 0
        high = self._length - 1
        while low <= high:
            mid = (low + high) // 2
            if self._array[mid] == value:
                return mid
            elif self._array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def insert(self, value: int) -> None:
        if self._length >= self._size:
            self._resize()
        low = 0
        high = self._length - 1
        while low <= high:
            mid = (low + high) // 2
            if self._array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

        for i in range(self._length, low, -1):
            self._array[i] = self._array[i - 1]
        self._array[low] = value
        self._length += 1

    def remove(self, value: int) -> None:
        index = self.search(value)
        if index == -1:
            return
        for i in range(index, self._length - 1):
            self._array[i] = self._array[i + 1]
        self._length -= 1

    def _resize(self) -> None:
        self._size *= 2
        new_array = [0] * self._size
        for i, n in enumerate(self._array):
            new_array[i] = n
        self._array = new_array


def merge_two_ordered_array(array1: OrderedArray, array2: OrderedArray) -> OrderedArray:
    result = OrderedArray(len(array1) + len(array2))
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1.get(i) < array2.get(j):
            result.insert(array1.get(i))
            i += 1
        else:
            result.insert(array2.get(j))
            j += 1
    while i < len(array1):
        result.insert(array1.get(i))
        i += 1
    while j < len(array2):
        result.insert(array2.get(j))
        j += 1
    return result


class TestOrderedArray(TestCase):

    def test_init(self) -> None:
        ordered_array = OrderedArray()
        assert ordered_array._size == 10
        assert ordered_array._array == [0] * 10
        assert ordered_array._length == 0

    def test_insert(self) -> None:
        ordered_array = OrderedArray()
        ordered_array.insert(1)

        ordered_array.insert(4)
        ordered_array.insert(2)
        ordered_array.insert(3)
        assert ordered_array.get(0) == 1
        assert ordered_array.get(1) == 2
        assert ordered_array.get(2) == 3
        assert ordered_array.get(3) == 4

    def test_remove(self) -> None:
        ordered_array = OrderedArray()
        ordered_array.insert(1)
        ordered_array.insert(2)
        ordered_array.insert(3)
        ordered_array.insert(4)

        ordered_array.remove(2)
        assert ordered_array.get(0) == 1
        assert ordered_array.get(1) == 3
        assert ordered_array.get(2) == 4

    def test_search(self) -> None:
        ordered_array = OrderedArray()
        ordered_array.insert(1)
        ordered_array.insert(2)
        ordered_array.insert(3)
        ordered_array.insert(4)

        assert ordered_array.search(2) == 1
        assert ordered_array.search(5) == -1

    def test_merge_two_ordered_array(self) -> None:
        ordered_array1 = OrderedArray()
        ordered_array1.insert(1)
        ordered_array1.insert(3)
        ordered_array1.insert(5)

        ordered_array2 = OrderedArray()
        ordered_array2.insert(2)
        ordered_array2.insert(4)
        ordered_array2.insert(6)

        result = merge_two_ordered_array(ordered_array1, ordered_array2)
        assert list(result) == [1, 2, 3, 4, 5, 6]
