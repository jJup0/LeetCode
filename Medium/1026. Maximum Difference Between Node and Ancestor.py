"""
Given the root of a binary tree, find the maximum value v for which there exist
different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any
child of a is an ancestor of b.

Constraints:
- The number of nodes in the tree is in the range [2, 5000].
- 0 <= Node.val <= 10^5
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode | None" = None,
            right: "TreeNode | None" = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
        O(n) / O(depth(root))   time / space complexity
        """
        self.res = 0
        self._dfs_find_max_diff(root)
        return self.res

    def _dfs_find_max_diff(self, node: TreeNode) -> tuple[int, int]:
        """
        Gets minimum and maximum descendant values, calculates difference
        and updates result variable if difference is largest yet.
        """
        min_child = max_child = node.val
        if node.left:
            minl, maxl = self._dfs_find_max_diff(node.left)
            min_child = min(min_child, minl)
            max_child = max(max_child, maxl)
        if node.right:
            minr, maxr = self._dfs_find_max_diff(node.right)
            min_child = min(min_child, minr)
            max_child = max(max_child, maxr)

        self.res = max(self.res, node.val - min_child, max_child - node.val)
        return min(node.val, min_child), max(node.val, max_child)
