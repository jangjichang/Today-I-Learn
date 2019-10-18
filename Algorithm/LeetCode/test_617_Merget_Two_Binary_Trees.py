import pytest_watch
import itertools

t1, t2 = [1, 3, 2, 5], [2, 1, 3, 'null', 4, 'null', 7]
output = [3, 4, 5, 5, 4, 'null', 7]


def test_simple():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    output = TreeNode(3)
    output.left = TreeNode(4)
    output.right = TreeNode(5)
    output.left.left = TreeNode(5)
    output.left.right = TreeNode(4)
    output.right.right = TreeNode(7)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    s = Solution()
    a = s.mergeTrees(tree1, tree2)

    # output = TreeNode(3)
    # output.left = TreeNode(4)
    # output.right = TreeNode(5)
    # output.left.left = TreeNode(5)
    # output.left.right = TreeNode(4)
    # output.right.right = TreeNode(7)
