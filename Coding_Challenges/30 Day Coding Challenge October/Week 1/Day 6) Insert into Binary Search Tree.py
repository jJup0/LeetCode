# Definition for a binary tree node.
class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root):
            if val > root.val:
                if root.right:
                    helper(root.right)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    helper(root.left)
                else:
                    root.left = TreeNode(val)
        if not root:
            return TreeNode(val)
        helper(root)
        return root
