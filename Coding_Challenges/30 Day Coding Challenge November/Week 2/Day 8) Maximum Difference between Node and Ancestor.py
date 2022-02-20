# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root, ancestors):
            if not root:
                return 0

            ancestors.append(root.val)
            res1 = dfs(root.left, ancestors)
            res2 = dfs(root.right, ancestors)

            if not (res1 or res2):
                res = max(ancestors) - min(ancestors)
                ancestors.remove(root.val)
                return res

            ancestors.remove(root.val)
            return max(res1, res2)
        return dfs(root, [])


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, hi, lo):
            if not node:
                return hi-lo

            if node.val > hi:
                hi = node.val
            elif node.val < lo:
                lo = node.val

            l = dfs(node.left, hi, lo)
            r = dfs(node.right, hi, lo)

            return max(l, r)

        return dfs(root, root.val, root.val)
