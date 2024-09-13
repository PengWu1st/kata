"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:
"""
from double_linked_list import DoubleLinkedList, Node


class LRUCache:

    """
    Example 1:
    >>> lru_cache = LRUCache(2)
    >>> lru_cache.put(1, 10)
    >>> lru_cache.get(1)
    10
    >>> lru_cache.put(2, 20)
    >>> lru_cache.put(3, 30)
    >>> lru_cache.get(2)
    20
    >>> lru_cache.get(1)
    -1
    """

    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.cap = capacity
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.dll.remove(node)
            self.dll.append(node)
            return node.val[1]

    def put(self, key: int, value: int) -> None:
        node = Node((key, value))
        self.dll.append(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            node = self.dll.pop()
            if node:
                self.cache.pop(node.val[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
