from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree, return the same tree where every subtree (of the given tree)
    not containing a 1 has been removed.
    A subtree of a node node is node plus every node that is a descendant of node.
    Constraints:
        The number of nodes in the tree is in the range [1, 200].
        Node.val is either 0 or 1.
    """

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if tree is empty, pruned version is also empty
        if not root:
            return None

        # replace children trees with pruned versions
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # return root if either child exists, which is only possible if they contain a 1
        # or root itself has value 1, else return None, pruning node from its parent
        return root if (root.left or root.right or root.val) else None
