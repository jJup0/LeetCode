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
            self.left: "TreeNode | None" = left
            self.right: "TreeNode | None" = right


class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.vals_at_level: list[list[int]] = []
        self._inorder_get_vals(root, 0)
        self._inorder_reverse_vals(root, 0)
        return root

    def _inorder_get_vals(self, node: TreeNode, level: int):
        if level == len(self.vals_at_level):
            self.vals_at_level.append([])
        self.vals_at_level[level].append(node.val)
        if node.left:
            self._inorder_get_vals(node.left, level + 1)
        if node.right:
            self._inorder_get_vals(node.right, level + 1)

    def _inorder_reverse_vals(self, node: TreeNode, level: int):
        if level & 1:
            node.val = self.vals_at_level[level].pop()
        if node.left:
            self._inorder_reverse_vals(node.left, level + 1)
        if node.right:
            self._inorder_reverse_vals(node.right, level + 1)
