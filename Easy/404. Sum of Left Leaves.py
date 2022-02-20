# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft=False) -> int:
        if not root:
            return 0
        ret = self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
        if (not root.left) and (not root.right) and isLeft:
            ret += root.val
        return ret
