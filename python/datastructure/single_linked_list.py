from typing import Any


class Node:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None
    
    def __repr__(self) -> str:
        return f"Node({self.val})"


class SingleLinkedList:
    """
    Example 1
    >>> sll = SingleLinkedList()
    >>> sll.insert(1)
    >>> sll.find(1)
    Node(1)
    """

    def __init__(self) -> None:
        self.head = None

    def insert(self, val: Any) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def find(self, val: Any) -> Node | None:
        p = self.head
        
        while p:
            if p.val == val:
                return p
            p = p.next
    
