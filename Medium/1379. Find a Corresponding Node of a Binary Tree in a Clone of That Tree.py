# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        # target used nonlocally
        def dfs(root, cloned_root):
            # if root == None, return None
            if not root:
                return None
            # if root == target, return cloned root, passing it along to caller
            if root == target:
                return cloned_root

            # if dfs with left original and left copy returns node, return it
            # otherwise return dfs from right node
            return dfs(root.left, cloned_root.left) or dfs(root.right, cloned_root.right)

        # dfs through tree to find target
        return dfs(original, cloned)
