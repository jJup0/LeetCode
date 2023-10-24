"""
Given the root of a binary tree, return an array of the largest value in
each row of the tree (0-indexed).

Constraints:
- The number of nodes in the tree will be in the range [0, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode" | None = None,
            right: "TreeNode" | None = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        """
        O(n) / O(depth(root))   time / space complexity
        """
        largest_at_level: list[int] = []

        def dfs(node: TreeNode, level: int):
            nonlocal largest_at_level
            node_val = node.val
            if level >= len(largest_at_level):
                largest_at_level.append(node_val)
            elif node_val > largest_at_level[level]:
                largest_at_level[level] = node_val

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        if root:
            dfs(root, 0)
        return largest_at_level
