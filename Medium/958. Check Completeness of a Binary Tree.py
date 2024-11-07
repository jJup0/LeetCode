"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can
have between 1 and 2h nodes inclusive at the last level h.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 1 <= Node.val <= 1000
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
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.level_node_count = [0]
        self._get_level_heights(root, 0)
        # check for incomplete intermediate levels
        for depth, count in enumerate(self.level_node_count[:-1]):
            if count != (1 << depth):
                return False

        # self.last_level[i] = True if there is a node at the ith
        # possible position on the last level, else False
        self.last_level = [False] * (1 << (len(self.level_node_count) - 1))
        self._get_node_pos_last_level(root, 0, 0)

        # check if last level is filled from left to right
        last_val = True
        for val in self.last_level:
            if val and not last_val:
                return False
            last_val = val
        return True

    def _get_level_heights(self, root: TreeNode, depth: int) -> None:
        if depth == len(self.level_node_count):
            # new deepest level reached
            self.level_node_count.append(0)

        self.level_node_count[depth] += 1
        # recurse to children
        if root.left:
            self._get_level_heights(root.left, depth + 1)
        if root.right:
            self._get_level_heights(root.right, depth + 1)

    def _get_node_pos_last_level(
        self, root: TreeNode, depth: int, node_pos: int
    ) -> None:
        # recurse to children
        if root.left:
            self._get_node_pos_last_level(root.left, depth + 1, node_pos)
        if root.right:
            right_node_pos = node_pos + (1 << (len(self.level_node_count) - depth - 2))
            self._get_node_pos_last_level(root.right, depth + 1, right_node_pos)

        if depth == len(self.level_node_count) - 1:
            # mark index as true if this node on is on the last level
            self.last_level[node_pos] = True
