"""
Given the root of a binary tree, return the leftmost value in the last row of
the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode | None" = None,
            right: "TreeNode| None" = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def pre_order(node: TreeNode, level: int):
            nonlocal first_val_of_level
            if level == len(first_val_of_level):
                first_val_of_level.append(node.val)
            level += 1
            if node.left:
                pre_order(node.left, level)
            if node.right:
                pre_order(node.right, level)

        first_val_of_level: list[int] = []
        pre_order(root, 0)
        return first_val_of_level[-1]
