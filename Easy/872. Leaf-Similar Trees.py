"""
Consider all the leaves of a binary tree, from left to right order, the values
of those leaves form a leaf value sequence.
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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        leaves2 = []
        self._get_leaves(root1, leaves1)
        self._get_leaves(root2, leaves2)
        return leaves1 == leaves2

    def _get_leaves(self, node: TreeNode, leaves: list[int]):
        """Adds leaves of node in inorder traversal to the given `leaves` parameter.
        i.e. result is stored in `leaves`.
        """
        if node.left:
            self._get_leaves(node.left, leaves)

        is_leaf = not (node.left or node.right)
        if is_leaf:
            leaves.append(node.val)

        if node.right:
            self._get_leaves(node.right, leaves)
