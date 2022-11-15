# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        O(log(n)^2) / O(log(n))     time / space complexity
        """

        def height(node: Optional[TreeNode]):
            # finds the height of a complete tree
            # O(log(n)) / O(1)  time / space complexity
            h = -1
            while node:
                node = node.left
                h += 1
            return h

        # base case: empty tree has 0 nodes
        if not root:
            return 0

        h = height(root)

        if height(root.right) == h-1:
            # if height of right child is equal to height_of_root-1, then the left child is a full
            # tree with 2**(h-1) - 1 nodes (add one to count root). A non full subtree can only
            # exist in the right subtree.
            return (1 << h) + self.countNodes(root.right)
        else:
            # else the right child is a full tree, with height h-2, with a total of 2**(h-2) - 1
            # nodes. A non full subtree can only exist in the left subtree.
            return (1 << h-1) + self.countNodes(root.left)
