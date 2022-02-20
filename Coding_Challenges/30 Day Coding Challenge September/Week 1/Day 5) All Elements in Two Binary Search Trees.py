# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> [int]:
        allElements = []

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            allElements.append(node.val)
            dfs(node.right)

        dfs(root1)
        dfs(root2)
        return sorted(allElements)
