from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # if there is nothing to trim, return nothing
        if not root:
            return None

        # if the value of the node is less than low, all left children will also
        # have a value less than low, so the trimmed version of this node is the
        # trimmed version of the right child node
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # analogous for if the value is greater than high
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # otherwise the node remains in the tree, replace the children of the current node
        # with their trimmed versions and return the new (sub-)tree
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
