from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree, construct a string consisting of parenthesis and integers
    from a binary tree with the preorder traversal way, and return it.
    Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship
    between the string and the original binary tree.
    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -1000 <= Node.val <= 1000
    """

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        # get string representations of child nodes
        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)
        # if right child is not empty include both
        if right_str:
            return f"{root.val}({left_str})({right_str})"
        # if only left child is non-empty, do not include right
        elif left_str:
            return f"{root.val}({left_str})"
        # if node is leaf, return value as string
        else:
            return str(root.val)
