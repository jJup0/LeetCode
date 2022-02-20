# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        def insert(root):
            if val > root.val:
                if root.right:
                    insert(root.right)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    insert(root.left)
                else:
                    root.left = TreeNode(val)

        insert(root)
        return root
