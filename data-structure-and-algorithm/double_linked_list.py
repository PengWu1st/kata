from typing import Any


class Node:
    def __init__(self, val: Any = None):
        self.val = val
        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self) -> str:
        return f"Node(val={self.val}, next={self.next}, prev={self.val})"


class DoubleLinkedList:
    """
    >>> dl = DoubleLinkedList()
    >>> dl
    None->None
    >>> dl.append(Node(1))
    >>> dl
    None->1->None
    >>> dl.append(Node(2))
    >>> dl
    None->1->2->None
    >>> dl.remove(dl.head.next)
    >>> dl
    None->2->None
    """

    def __init__(self):
        self.head = Node()
        self.end = Node()
        self.head.next = self.end
        self.end.prev = self.head

    def append(self, node: Node):
        prev_node, next_node = self.end.prev, self.end
        if prev_node:
            prev_node.next = node
        next_node.prev = node
        node.prev, node.next = prev_node, next_node

    def remove(self, node: Node):
        prev_node, next_node = node.prev, node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def pop(self):
        result = self.head.next
        if self.head.next:
            self.remove(self.head.next)
        return result

    def __repr__(self) -> str:
        p = self.head
        nodes = []
        while p:
            nodes.append(str(p.val))
            p = p.next
        return '->'.join(nodes)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
