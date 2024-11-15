from __future__ import annotations
from single_linked_list import SingleLinkedList


class HashNode:

    def __init__(self, key, value=None) -> None:
        self.key, self.value = key, value

    def __eq__(self, other: HashNode) -> bool:
        return self.key == other.key


class HashTable:
    """
    Example 1
    >>> hash_table = HashTable()
    >>> hash_table.insert("key1", "value1")
    >>> hash_table.insert("key2", "value2")
    >>> hash_table.find("key1")
    'value1'
    >>> hash_table.find("key2")
    'value2'
    >>> hash_table.remove("key1")
    >>> hash_table.find("key1") is None
    True

    """

    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._table = [SingleLinkedList() for _ in range(self._size)]

    def insert(self, key, value):
        index = self._hash(key)
        self._table[index].insert(HashNode(key, value))

    def _hash(self, key):
        return hash(key) % self._size

    def find(self, key):
        index = self._hash(key)
        node = self._table[index].find(HashNode(key))
        if node:
            return node.value  # type: ignore
        return None

    def remove(self, key):
        index = self._hash(key)
        self._table[index].remove(HashNode(key))
