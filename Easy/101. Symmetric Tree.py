# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    """
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        """Recursively check if subtrees are symmetric
        O(n) / O(log(n))    time / space complexity
        """
        def check_sym_pair(left: Optional[TreeNode], right: Optional[TreeNode]):
            # if both are None, return True
            if not left and not right:
                return True

            # if one is None, return False
            if not left or not right:
                return False

            # if their values are unequal return false
            if left.val != right.val:
                return False

            # if their inner subtrees are unequal return false
            if not check_sym_pair(left.right, right.left):
                return False

            # finally if none of the above apply, return whether their outer subtrees are symmetric
            return check_sym_pair(left.left, right.right)

        return check_sym_pair(root.left, root.right)
