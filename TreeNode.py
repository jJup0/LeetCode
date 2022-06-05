import random
from collections import deque
from random import shuffle
from typing import Any, List, Optional


class TreeNode:

    @staticmethod
    def from_structure(list: Optional[List[Any]]):
        if not list:
            return None

        val_queue = deque(list)
        list = None

        root = TreeNode(val_queue.popleft())
        node_queue = deque((root,))
        while val_queue:
            node = node_queue.popleft()

            if not val_queue:
                break

            left_val = val_queue.popleft()
            if left_val:
                node.left = TreeNode(left_val)
                node_queue.append(node.left)

            if not val_queue:
                break

            right_val = val_queue.popleft()
            if right_val:
                node.right = TreeNode(right_val)
                node_queue.append(node.right)

        return root

    @staticmethod
    def fromList(list: Optional[List[Any]]):
        if not list:
            return None

        res = TreeNode(list[0])
        for val in list[1:]:
            res.add_node(val)
        return res

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

    def in_order_str(self) -> str:
        def helper(root):
            nonlocal sofar
            if not root:
                return
            helper(root.left)
            sofar.append(root.val)
            helper(root.right)

        sofar = []
        helper(self)
        return str(sofar)

    def pre_order_str(self) -> str:
        def helper(root):
            nonlocal sofar
            if not root:
                return
            sofar.append(root.val)
            helper(root.left)
            helper(root.right)

        sofar = []
        helper(self)
        return str(sofar)

    def add_node(self, val: Any):
        if val < self.val:
            if self.left:
                self.left.add_node(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.add_node(val)
            else:
                self.right = TreeNode(val)


if __name__ == "__main__":
    null = None
    random.seed(1)
    l = list(range(1, 20))
    random.shuffle(l)
    x = TreeNode.fromList(l)
