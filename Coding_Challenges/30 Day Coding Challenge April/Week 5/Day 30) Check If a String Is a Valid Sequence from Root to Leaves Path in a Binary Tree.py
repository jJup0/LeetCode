# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: [int]) -> bool:
        def helper(node, remainingArr):
            if self.retVal or not(remainingArr or node):
                return
            if node.val == remainingArr[0]:
                if len(remainingArr) == 1 and not(node.left or node.right):
                    self.retVal = True
                    return
                helper(node.left, remainingArr[1:])
                helper(node.right, remainingArr[1:])

        self.retVal = False
        helper(root, arr)
        return self.retVal
