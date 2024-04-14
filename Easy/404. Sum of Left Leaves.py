"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child
of another node.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -1000 <= Node.val <= 1000
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        O(n) / O(depth(root))   time / space complexity
        """
        return self._sumOfLeftLeaves(root, False)

    def _sumOfLeftLeaves(self, node: TreeNode, is_left: bool) -> int:
        res = 0
        is_leaf = True
        # add sum of children left leaves
        if node.left:
            res += self._sumOfLeftLeaves(node.left, True)
            is_leaf = False
        if node.right:
            res += self._sumOfLeftLeaves(node.right, False)
            is_leaf = False

        if is_leaf and is_left:
            # add self if leaf and left node
            res += node.val

        return res
