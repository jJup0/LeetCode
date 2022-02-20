# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.biggest = -2**31

        def helper(node):
            if not(node):
                return 0
            lsMax = max(helper(node.left), 0)
            rsMax = max(helper(node.right), 0)
            total = node.val + lsMax + rsMax
            self.biggest = max(total, self.biggest)
            # return total #not this because it's really badly explained and youre only allowed two paths which meet at the root
            return max(lsMax, rsMax) + node.val
        helper(root)
        return self.biggest
