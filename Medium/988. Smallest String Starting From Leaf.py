"""
You are given the root of a binary tree where each node has a value in the
range [0, 25] representing the letters'a' to'z'.

Return the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.
- For example,"ab" is lexicographically smaller than"aba".

A leaf of a node is a node that has no children.

Constraints:
- The number of nodes in the tree is in the range [1, 8500].
- 0 <= Node.val <= 25
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
    def smallestFromLeaf(self, root: TreeNode) -> str:
        return self._smallest_from_leaf(root, "")

    def _smallest_from_leaf(self, node: TreeNode, curr_str: str) -> str:
        """
        Naive implementation.
        O(n*log(n)) / O(n)   time / space complexity
        """

        as_char = chr(node.val + ord("a"))
        curr_str = as_char + curr_str
        if not node.left and not node.right:
            return curr_str
        res = chr(255)
        if node.left:
            res = min(res, self._smallest_from_leaf(node.left, curr_str))
        if node.right:
            res = min(res, self._smallest_from_leaf(node.right, curr_str))
        return res
