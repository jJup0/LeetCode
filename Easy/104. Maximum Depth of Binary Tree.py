# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, lvl):
            if not root:
                return
            self.maxLvl = max(self.maxLvl, lvl)
            dfs(root.left, lvl+1)
            dfs(root.right, lvl+1)
        self.maxLvl = 0
        dfs(root, 1)
        return self.maxLvl
