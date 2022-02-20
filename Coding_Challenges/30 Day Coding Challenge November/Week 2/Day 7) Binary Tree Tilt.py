# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            self.res += abs(l-r)
            return root.val + l + r
        self.res = 0
        dfs(root)
        return self.res
