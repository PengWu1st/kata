
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


def binary_search_left(arr: list, value):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < value:
            l = m + 1
        elif arr[m] > value:
            r = m - 1
        else:
            if m == 0 or arr[m - 1] != value:
                return m
            r = m - 1
    return -1


def lower_bound(arr: list, value):
    # find index i, such that arr[i] >= value
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < value:
            l = m + 1
        else:
            r = m
    return l


def upper_bound(arr: list, value):
    # find index i, such that arr[i] > value
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= value:
            l = m + 1
        else:
            r = m
    return l


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 5), 4)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 8)
        self.assertEqual(binary_search(arr, 10), -1)

    def test_lower_bound(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(lower_bound(arr, 5), 4)
        self.assertEqual(lower_bound(arr, 1), 0)
        self.assertEqual(lower_bound(arr, 9), 8)
        self.assertEqual(lower_bound(arr, 10), 9)

    def test_lower_bound_2(self):
        arr = [1, 2, 2, 2, 5, 6, 7, 8, 9]
        self.assertEqual(lower_bound(arr, 2), 1)

    def test_upper_bound(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(upper_bound(arr, 5), 5)
        self.assertEqual(upper_bound(arr, 1), 1)
        self.assertEqual(upper_bound(arr, 9), 9)
        self.assertEqual(upper_bound(arr, 10), 9)

    def test_upper_bound_2(self):
        arr = [1, 2, 2, 2, 5, 6, 7, 8, 9]
        self.assertEqual(upper_bound(arr, 2), 4)
