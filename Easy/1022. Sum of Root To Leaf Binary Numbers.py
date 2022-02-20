# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevVal: int):
            if not root:
                return
            newVal = (prevVal << 1) + root.val
            if root.left or root.right:
                dfs(root.left, newVal)
                dfs(root.right, newVal)
            else:
                self.retVal += newVal
        self.retVal = 0
        dfs(root, 0)
        return self.retVal