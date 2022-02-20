# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node):
            if not node:
                return 0
            mysum = 0
            if node.left and node.val > low:
                mysum += helper(node.left)
            if node.right and node.val < high:
                mysum += helper(node.right)
            if low <= node.val and node.val <= high:
                mysum += node.val
            return mysum
        
        return helper(root)