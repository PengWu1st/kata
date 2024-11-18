
from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # type: ignore


def reverse_linked_list_recursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    p = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return p


def reverse_linked_list_recursive_v2(head: ListNode) -> ListNode:
    def helper(prev, current):
        if not current:
            return prev
        next_node = current.next
        current.next = prev
        return helper(current, next_node)
    return helper(None, head)  # type: ignore


class TestReverseLinkedList(TestCase):

    def test_reverse_linked_list(self) -> None:
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head = reverse_linked_list(head)
        assert head.val == 5
        assert head.next
        assert head.next.val == 4
        assert head.next.next.val == 3
        assert head.next.next.next.val == 2
        assert head.next.next.next.next.val == 1

    def test_reverse_linked_list_recursive(self) -> None:
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head = reverse_linked_list_recursive(head)
        assert head.val == 5
        assert head.next
        assert head.next.val == 4
        assert head.next.next.val == 3
        assert head.next.next.next.val == 2
        assert head.next.next.next.next.val == 1

    def test_reverse_linked_list_recursive_v2(self) -> None:
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head = reverse_linked_list_recursive_v2(head)
        assert head.val == 5
        assert head.next
        assert head.next.val == 4
        assert head.next.next.val == 3
        assert head.next.next.next.val == 2
        assert head.next.next.next.next.val == 1
