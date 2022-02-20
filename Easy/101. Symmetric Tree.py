# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node, lvl):
            if not node:
                rows[lvl].append(None)
                return
            rows[lvl].append(node.val)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)

        rows = defaultdict(list)
        dfs(root, 0)
        for vals in rows.values():
            if vals != vals[::-1]:
                return False
        return True
