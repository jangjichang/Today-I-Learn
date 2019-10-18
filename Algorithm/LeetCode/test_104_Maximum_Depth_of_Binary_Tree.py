import pytest_watch

input = [1, 2, 'null', 3, 'null', 'null', 'null', 4]
output = 3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test_simple():
    assert solution(input) == output


def node_count(root):
    """
    트리의 노드 수를 반환하는 함수
    """
    if not root:
        return 0
    else:
        return 1 + node_count(root.left) + node_count(root.right)


def maxDepth(root):
    """
    트리의 깊이를 반환하는 함수
    """
    if not root:
        return 0
    return 1+ max(maxDepth(root.left), maxDepth(root.right))


def solution(input):
    pass

if __name__ == "__main__":
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)

    print(maxDepth(root))