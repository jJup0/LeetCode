"""
Given the root of a binary tree, return the postorder traversal of its nodes'
values.

Constraints:
- The number of the nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Follow up iterative. Keep set of visited node and append node values at second visit.
        O(n) / O(n)     time / space complexity
        """
        if root is None:
            return []

        visited: set[TreeNode] = set()
        stack: list[TreeNode] = [root]
        res: list[int] = []
        while stack:
            node = stack.pop()
            if node in visited:
                res.append(node.val)
                continue

            # append node to stack again, at next visit add node value
            visited.add(node)
            stack.append(node)

            # add children for postorder traversal to stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
