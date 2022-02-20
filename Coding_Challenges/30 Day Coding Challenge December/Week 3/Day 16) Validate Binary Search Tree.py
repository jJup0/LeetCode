# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, minVal=float('-inf'), maxVal=float('inf')) -> bool:
        if not root:
            return True
        currVal = root.val
        if currVal > minVal and currVal < maxVal:
            return self.isValidBST(root.left, minVal, currVal) and self.isValidBST(root.right, currVal, maxVal)
        return False
