from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).
    Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000
    """

    # not mentioned in the question, by the levels should be in the format of a 2d list
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # result variable
        levels = []

        # traverses the tree in pre-order, appending to non-local levels list
        def helper(root, depth):
            # if depth has never been reached, append new level to levels
            if depth == len(levels):
                levels.append([root.val])
            else:
                # else append to existing list
                levels[depth].append(root.val)

            # check for not none before function call for performance
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)

        # if root is not None, call helper function with root
        if root:
            helper(root, 0)
        return levels
