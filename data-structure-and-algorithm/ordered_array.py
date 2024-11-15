
from unittest import TestCase


class OrderedArray:

    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._array = [0] * self._size
        self._length = 0

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
