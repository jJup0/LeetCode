from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree and two integers val and depth, add a row of nodes with value
    val at the given depth depth.
    Note that the root node is at depth 1.
    The adding rule is:
        Given the integer depth, for each not null tree node cur at the depth depth - 1, create two
            tree nodes with value val as cur's left subtree root and right subtree root.
        cur's original left subtree should be the left subtree of the new left subtree root.
        cur's original right subtree should be the right subtree of the new right subtree root.
        If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with
            value val as the new root of the whole original tree, and the original tree is the new
            root's left subtree.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        The depth of the tree is in the range [1, 10^4].
        -100 <= Node.val <= 100
        -10^5 <= val <= 10^5
        1 <= depth <= the depth of tree + 1
    """

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        O(n) / O(log(n))    time / space complexity
        """
        # if not a node, return None
        if not root:
            return None

        # special case, add whole tree as left child of val
        if depth == 1:
            return TreeNode(val, root)

        if depth == 2:
            # at "remaining" depth of 2, need to add row below root
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, None, root.right)
        else:
            # if depth > 2, traverse down to children
            self.addOneRow(root.left, val, depth - 1)
            self.addOneRow(root.right, val, depth - 1)
        return root

    def addOneRow_with_helper(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # same code but using a helper function
        def helper(node, d):
            if not node:
                return
            if d == depth:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            else:
                helper(node.left, d + 1)
                helper(node.right, d + 1)

        if depth == 1:
            return TreeNode(val, root)

        helper(root, 2)
        return root
