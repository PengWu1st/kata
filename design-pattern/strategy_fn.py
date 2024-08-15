import random
from typing import Callable


def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quicksort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


SortFn = Callable[[list[int]], list[int]]


def context(strategy: SortFn, arr: list[int]) -> list[int]:
    data = [item * 2 + random.randint(-10, 10) for item in arr]

    return strategy(data)


def main():
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    print(context(bubble_sort, arr))
    print(context(quicksort, arr))


if __name__ == "__main__":
    main()
