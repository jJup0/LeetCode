# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(node, count):
            if (self.retVal != None) or not(node):
                return count + 1
            count = dfs(node.left, count)
            if count == k:
                self.retVal = node.val
            count = dfs(node.right, count)
            if count == k:
                self.retVal = node.val
            return count
        self.retVal = None
        dfs(root, 0)
        return self.retVal
