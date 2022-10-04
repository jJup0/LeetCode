from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root
    to-leaf path such that adding up all the values along the path equals targetSum.
    A leaf is a node with no children.

    Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -1000 <= Node.val <= 1000
        -1000 <= targetSum <= 1000
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # a tree without nodes cannot sum up to the targetSum
        if not root:
            return False

        # reduce the target sum by the current nodes value
        targetSum -= root.val

        # if either path down the left or right child sums up to targetSum, then return True
        if self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum):
            return True

        # otherwise if this node is a leaf node and the target sum has been reached return true,
        # else false
        return (not(root.left or root.right)) and (targetSum == 0)
