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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        For each subtree, calculate the longest path taken through the subtree root.
        Return the maximum of all these paths.
        O(total_nodes) / O(depth of root)     time / space complexity
        """

        def get_depth_and_update_diameter(node: TreeNode | None) -> int:
            nonlocal diameter
            if not node:
                return 0

            l = get_depth_and_update_diameter(node.left)
            r = get_depth_and_update_diameter(node.right)

            diameter = max(diameter, l + r)
            return max(l, r) + 1

        diameter = 0
        get_depth_and_update_diameter(root)
        return diameter
