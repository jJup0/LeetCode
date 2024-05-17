"""
Given a binary tree root and an integer target, delete all the leaf nodes with
value target.

Note that once you delete a leaf node with value target, if its parent node
becomes a leaf node and has the value target, it should also be deleted (you
need to continue doing that until you cannot).

Constraints:
- The number of nodes in the tree is in the range [1, 3000].
- 1 <= Node.val, target <= 1000
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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode | None:
        """
        n := total nodes, m := depth of tree
        O(n) / O(m)     time / space complexity
        """
        self.target = target
        dummy = TreeNode(0, root)
        self._remove_leaf_nodes(dummy)
        return dummy.left

    def _remove_leaf_nodes(self, node: TreeNode) -> bool:
        is_leaf = True
        if node.right:
            should_delete = self._remove_leaf_nodes(node.right)
            if should_delete:
                node.right = None
            else:
                is_leaf = False
        if node.left:
            should_delete = self._remove_leaf_nodes(node.left)
            if should_delete:
                node.left = None
            else:
                is_leaf = False
        if is_leaf and node.val == self.target:
            return True
        return False
