"""
Given the root of a binary tree, return the number of nodes where the value of
the node is equal to the average of the values in its subtree.

Note:
- The average of n elements is the sum of the n elements divided by n and rounded
  down to the nearest integer.
- A subtree of root is a tree consisting of root and all of its descendants.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 1000
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
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        self.descendants_same_res = 0
        self._average_of_subtree_helper(root)
        return self.descendants_same_res

    def _average_of_subtree_helper(self, node: TreeNode | None) -> tuple[int, int]:
        """Returns tuple of size of subtree and sum of nodes of subtree."""
        if not node:
            return 0, 0

        l_count, l_sum = self._average_of_subtree_helper(node.left)
        r_count, r_sum = self._average_of_subtree_helper(node.right)

        # sum up node count and value sum
        subtree_count = 1 + l_count + r_count
        subtree_sum = node.val + l_sum + r_sum

        # increment descendants_same_res if node is same as average of its subtree
        if subtree_sum // subtree_count == node.val:
            self.descendants_same_res += 1

        return subtree_count, subtree_sum
