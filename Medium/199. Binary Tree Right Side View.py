from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.
    Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # result variable
        res = []

        # helper function, fills res with right side view, in reverse preorder
        def helper(root, depth):
            if not root:
                return
            # if depth is new deepest, append to res
            if depth == len(res):
                res.append(root.val)
            # traverse right child, then left
            helper(root.right, depth+1)
            helper(root.left, depth+1)

        # apply helper to root
        helper(root, 0)
        return res
