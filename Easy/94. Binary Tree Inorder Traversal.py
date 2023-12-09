"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import TYPE_CHECKING, Optional

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        return self.inorderTraversal_iterative(root)

    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> list[int]:
        """
        Simulate stack.
        O(n) / O(height(root))  time / space complexity
        """
        if not root:
            return []
        node_stack = [root]
        res: list[int] = []
        while node_stack:
            node = node_stack.pop()
            left_child = node.left
            if left_child:
                node.left = None
                node_stack.append(node)
                node_stack.append(left_child)
            else:
                res.append(node.val)
                right_child = node.right
                if right_child:
                    node_stack.append(right_child)
        return res

    def inorderTraversal_recursive_n_squared(
        self, root: Optional[TreeNode]
    ) -> list[int]:
        if not root:
            return []
        ret = self.inorderTraversal_recursive_n_squared(root.left)
        ret.append(root.val)
        ret.extend(self.inorderTraversal_recursive_n_squared(root.right))
        return ret
