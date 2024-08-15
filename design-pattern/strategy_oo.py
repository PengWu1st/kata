from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import random


class SortStrategy(ABC):
    @abstractmethod
    def execute(self, arr: list[int]) -> list[int]:
        pass


class BubbleSort(SortStrategy):
    def execute(self, arr: list[int]) -> list[int]:
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSort(SortStrategy):
    def execute(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.execute(left) + middle + self.execute(right)


class Context:
    def __init__(self, strategy: SortStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        self.strategy = strategy

    def execute(self, arr: list[int]) -> list[int]:
        data = [item * 2 + random.randint(-10, 10) for item in arr]
        return self.strategy.execute(data)


def main():
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    context = Context(BubbleSort())
    print(context.execute(arr))
    context.set_strategy(QuickSort())
    print(context.execute(arr))
