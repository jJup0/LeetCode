# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    """Solution for: 129. Sum Root to Leaf Numbers

    You are given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return the total sum of all root-to-leaf numbers. Test cases are generated
    so that the answer will fit in a 32-bit integer.

    A leaf node is a node with no children.

    Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        0 <= Node.val <= 9
        The depth of the tree will not exceed 10.
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """Calculates sum of root-to-leaf decimal interpretations."""

        def _sumNumbers(curr_node: Optional[TreeNode], prev_num):
            # root-to-none has no valid decimal evaluation, return 0
            if not curr_node:
                return 0

            # decimal evaluation of root to curr_node
            curr_num = prev_num + curr_node.val

            # if leaf node, return previously constructed number + own value
            if not curr_node.left and not curr_node.right:
                return curr_num

            # multiply by ten to shift digits so far one place to the left
            curr_num *= 10
            # return root-to-leaf sums of parents
            return _sumNumbers(curr_node.left, curr_num) + _sumNumbers(
                curr_node.right, curr_num
            )

        return _sumNumbers(root, 0)
