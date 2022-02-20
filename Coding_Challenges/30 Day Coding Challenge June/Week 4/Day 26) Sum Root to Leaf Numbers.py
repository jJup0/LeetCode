# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(prevleafval: int, node: TreeNode):
            if not node:
                return
            prevleafval = prevleafval * 10 + node.val
            if not (node.left or node.right):
                self.total += prevleafval
                return
            helper(prevleafval, node.left)
            helper(prevleafval, node.right)
        self.total = 0
        helper(0, root)
        return self.total
