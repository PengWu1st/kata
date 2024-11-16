
import unittest


def binary_search(arr: list, value):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == value:
            return m
        elif arr[m] > value:
            r = m - 1
        else:
            l = m + 1
    return -1


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 5), 4)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 8)
        self.assertEqual(binary_search(arr, 10), -1)
