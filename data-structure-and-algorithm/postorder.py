import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    if not root:
        return []
    stack, result = [], []
    last = None
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            peek = stack[-1]
            if peek.right and last != peek.right:
                root = peek.right
            else:
                result.append(peek.val)
                last = stack.pop()
    return result


class TestPostorderTraversal(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(postorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(postorderTraversal(root), [1])

    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(postorderTraversal(root), [2, 1])

    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(postorderTraversal(root), [2, 3, 1])

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(postorderTraversal(root), [4, 5, 2, 6, 7, 3, 1])


if __name__ == '__main__':
    unittest.main()
