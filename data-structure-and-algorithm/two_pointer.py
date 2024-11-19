
from typing import Callable


def two_pointers_single_arr(arr: list, condition: Callable) -> list:
    l, r = 0, len(arr) - 1

    while l < r:
        if condition(arr[l], arr[r]):
            l += 1
        else:
            r -= 1
    return arr


def two_pointers_two_arr(arr1: list, arr2: list, condition: Callable, update_ans: Callable) -> int:
    i, j, ans = 0, 0, 0

    while i < len(arr1) and j < len(arr2):
        update_ans(ans, arr1[i], arr2[j])
        if condition(arr1[i], arr2[j]):
            i += 1
        else:
            j += 1

    while i < len(arr1):
        update_ans(ans, arr1[i], None)
        i += 1

    while j < len(arr2):
        update_ans(ans, None, arr2[j])
        j += 1
    return ans
