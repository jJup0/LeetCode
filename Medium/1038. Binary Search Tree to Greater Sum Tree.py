"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such
that every key of the original BST is changed to the original key plus the sum
of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the
  node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val <= 100
- All the values in the tree are unique.
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        O(n) / O(depth_of_root)     time / space complexity
        """
        self.larger_node_sum = 0
        self._reverse_order_bst_to_gst(root)
        return root

    def _reverse_order_bst_to_gst(self, root: TreeNode) -> None:
        """
        Iterate through bst in reverse order, tracking cumulative
        sum of all nodes visited so far, and increase current
        node's value by this sum.
        """
        if root.right:
            self._reverse_order_bst_to_gst(root.right)
        self.larger_node_sum += root.val
        root.val = self.larger_node_sum
        if root.left:
            self._reverse_order_bst_to_gst(root.left)
