from typing import TYPE_CHECKING, Literal, Optional

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    """
    You are given the root of a binary tree.

    A ZigZag path for a binary tree is defined as follow:

        Choose any node in the binary tree and a direction (right or left).
        If the current direction is right, move to the right child of the current node;
            otherwise, move to the left child.
        Change the direction from right to left or from left to right.
        Repeat the second and third steps until you can't move in the tree.
        Zigzag length is defined as the number of nodes visited - 1.
            (A single node has a length of 0).

    Return the longest ZigZag path contained in that tree.

    Constraints:
        The number of nodes in the tree is in the range [1, 5 * 10^4].
        1 <= Node.val <= 100
    """

    def longestZigZag(self, root: TreeNode) -> int:
        PLEFT, PRIGHT = 0, 1

        def helper(root: Optional[TreeNode], parent: int, score: int) -> int:
            if not root:
                return score

            res = 0
            if parent == PLEFT:
                l = helper(root.left, PRIGHT, score + 1)
                r = helper(root.right, PLEFT, 0)
                res = max(res, l, r)
            elif parent == PRIGHT:
                l = helper(root.left, PRIGHT, 0)
                r = helper(root.right, PLEFT, score + 1)
                res = max(res, l, r)
            return res

        # simulate root as a subtree, once as a left, once as a right node
        l = helper(root, PLEFT, -1)
        r = helper(root, PRIGHT, -1)
        return max(l, r)
