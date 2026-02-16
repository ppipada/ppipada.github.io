from collections import defaultdict
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root):
    if not root: return []
    q = deque([(root, 0)])
    first = {}
    while q:
        node, depth = q.popleft()
        if depth not in first:
            first[depth] = node.val
        if node.left: q.append((node.left, depth + 1))
        if node.right: q.append((node.right, depth + 1))
    return [first[d] for d in sorted(first)]


def right_view(root):
    if not root: return []
    q = deque([(root, 0)])
    last = {}
    while q:
        node, depth = q.popleft()
        last[depth] = node.val
        if node.left: q.append((node.left, depth + 1))
        if node.right: q.append((node.right, depth + 1))
    return [last[d] for d in sorted(last)]


def top_view(root):
    """First node encountered at each horizontal distance (hd)."""
    if not root: return []
    q = deque([(root, 0)])  # node, hd
    seen = {}
    while q:
        node, hd = q.popleft()
        if hd not in seen:
            seen[hd] = node.val
        if node.left: q.append((node.left, hd - 1))
        if node.right: q.append((node.right, hd + 1))
    return [seen[h] for h in sorted(seen)]


def bottom_view(root):
    """Last node encountered at each horizontal distance (hd)."""
    if not root: return []
    q = deque([(root, 0)])
    seen = {}
    while q:
        node, hd = q.popleft()
        seen[hd] = node.val
        if node.left: q.append((node.left, hd - 1))
        if node.right: q.append((node.right, hd + 1))
    return [seen[h] for h in sorted(seen)]
