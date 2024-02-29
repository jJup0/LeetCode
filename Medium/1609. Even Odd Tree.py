"""
A binary tree is named Even-Odd if it meets the following conditions:
- The root of the binary tree is at level index 0, its children are at level
index 1, their children are at level index 2, etc.
- For every even-indexed level, all nodes at the level have odd integer values
in strictly increasing order (from left to right).
- For every odd-indexed level, all nodes at the level have even integer values
in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd,
otherwise return false.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^6
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
    def isEvenOddTree(self, root: TreeNode) -> bool:
        """
        O(n) / O(depth of root)     time / space complexity
        """

        def pre_order(node: TreeNode, level: int) -> bool:
            nonlocal prev_val_at_level
            node_val = node.val
            val_is_odd = node_val % 2
            level_is_odd = level % 2
            if level_is_odd == val_is_odd:
                return False
            if level == len(prev_val_at_level):
                prev_val_at_level.append(node_val)
            else:
                if level_is_odd:
                    if node_val >= prev_val_at_level[level]:
                        return False
                else:
                    if node_val <= prev_val_at_level[level]:
                        return False

                prev_val_at_level[level] = node.val

            is_even_odd_tree = True
            level += 1
            if node.left:
                is_even_odd_tree &= pre_order(node.left, level)
            if node.right:
                is_even_odd_tree &= pre_order(node.right, level)
            return is_even_odd_tree

        prev_val_at_level: list[int] = []
        return pre_order(root, 0)
