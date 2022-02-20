# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def increasingBST(self, root: TreeNode) -> TreeNode:
    #     nodes = []
    #     def dfs(root):
    #         if root:
    #             dfs(root.left)
    #             nodes.append(root.val)
    #             dfs(root.right)
    #     dfs(root)
    #     res = dummy = TreeNode()
    #     for val in nodes:
    #         dummy.right = TreeNode(val)
    #         dummy = dummy.right
    #     return res.right

    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        if (root is None):
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
