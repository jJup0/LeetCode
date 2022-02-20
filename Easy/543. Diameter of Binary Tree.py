class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = 0

        def dfs(node):
            nonlocal d
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            d = max(d, l+r)
            return max(l, r)+1

        dfs(root)
        return d
