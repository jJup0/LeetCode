from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # top item on stack will always be leftmost node that has not been iterated over
        self.node_stack = []
        # append entire left arm of root to stack
        while root:
            self.node_stack.append(root)
            root = root.left

    def next(self) -> int:
        # pop item from the stack
        node = self.node_stack.pop()
        # it will be left most not yet returned, so store its value as answer
        res = node.val

        # add its right child and that childs entire left arm to stack
        node = node.right
        while node:
            self.node_stack.append(node)
            node = node.left

        # ignore if original popped node had a left child, it has already been iterated over
        return res

    def hasNext(self) -> bool:
        # if there is a node on the stack then there is a next value
        return bool(self.node_stack)


#     # initial version, slightly slower due to recursion
#     def __init__recur(self, root: Optional[TreeNode]):
#         # initialize stack with root node only
#         self.node_stack = [root]

#     def next_recur(self) -> int:
#         # pop item from the stack
#         node = self.node_stack.pop()

#         # if it has a right child, append it to the stack, and remove it as a child
#         if node.right:
#             self.node_stack.append(node.right)
#             node.right = None

#         # if is has a left child, add node itself to the stack, remove the left child as a child
#         # then append the left child, and finally call next() again to get continue iteration over left child
#         if node.left:
#             self.node_stack.append(node)
#             self.node_stack.append(node.left)
#             node.left = None
#             return self.next()
#         else:
#             # if there is no left child, then this is the next value to return
#             return node.val
