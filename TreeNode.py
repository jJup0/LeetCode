from collections import deque
from typing import Any, List, Optional


class TreeNode:

    @staticmethod
    def fromList(list: Optional[List[Any]]):
        if not list:
            return None

        val_queue = deque(list)
        list = None

        root = TreeNode(val_queue.popleft())
        node_queue = deque((root,))
        while val_queue:
            node = node_queue.popleft()

            left_val = val_queue.popleft()
            if left_val:
                node.left = TreeNode(left_val)
                node_queue.append(node.left)

            right_val = val_queue.popleft()
            if right_val:
                node.right = TreeNode(right_val)
                node_queue.append(node.right)

        return root

    def __init__(self, val: Any = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        l = []
        node_stack = deque((self, ))
        while node_stack:
            node = node_stack.popleft()
            if not node:
                l.append(None)
                continue

            l.append(node.val)
            node_stack.append(node.left)
            node_stack.append(node.right)

        i = 0   # to ignore unbound warning
        for i in range(len(l)-1, -1, -1):
            if l[i]:
                break
        return str(l[:i+1])
