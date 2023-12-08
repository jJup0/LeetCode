"""
Given the root of a binary tree, construct a string consisting of
parenthesis and integers from a binary tree with the preorder traversal
way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one
mapping relationship between the string and the original binary tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -1000 <= Node.val <= 1000
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        # get string representations of child nodes
        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)
        if right_str:
            # if right child is not empty include both
            return f"{root.val}({left_str})({right_str})"
        elif left_str:
            # if only left child is non-empty, do not include right
            return f"{root.val}({left_str})"
        else:
            # if node is leaf, return value as string
            return str(root.val)
