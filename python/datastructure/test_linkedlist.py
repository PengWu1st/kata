
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def test_double_linkedlist_node():
    node = Node(1)
    assert node.data == 1
    assert node.next is None
    assert node.prev is None
    

class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)
        current.next.prev = current

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        current.prev = Node(data)
        current.prev.next = current
        self.head = current.prev

    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_after(self, data, after_data):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == after_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def insert_before(self, data, before_data):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == before_data:
                new_node = Node(data)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                current.prev = new_node
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next