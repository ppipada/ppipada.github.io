from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

def insert_complete(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Insert `val` into the first available spot to maintain completeness.

    Time:  O(n) worst-case per insertion
    Space: O(width of tree) due to queue
    """
    new_node = TreeNode(val)
    if root is None:
        return new_node

    q = deque([root])
    while q:
        node = q.popleft()

        if node.left is None:
            node.left = new_node
            return root
        else:
            q.append(node.left)

        if node.right is None:
            node.right = new_node
            return root
        else:
            q.append(node.right)

    return root  # logically unreachable
