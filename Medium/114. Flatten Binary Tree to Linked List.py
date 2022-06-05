from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, flatten the tree into a "linked list":
    The "linked list" should use the same TreeNode class where the right child pointer points
    to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.
    Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -100 <= Node.val <= 100
    """

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        O(1) space
        """
        if not root:
            return
        right_child = root.right
        root.right = self.flatten(root.left)
        root.left = None

        tail = root
        while tail.right:
            tail = tail.right

        tail.right = self.flatten(right_child)
        return root  # type: ignore
