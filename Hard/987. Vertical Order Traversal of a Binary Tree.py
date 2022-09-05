# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    """
    Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
    For each node at position (row, col), its left and right children will be at positions
    (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
    The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each
    column index starting from the leftmost column and ending on the rightmost column. There may
    be multiple nodes in the same row and same column. In such a case, sort these nodes by their
    values.
    Return the vertical order traversal of the binary tree.
    Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        0 <= Node.val <= 1000
    """

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        nodes_with_position = []

        # traverse tree in preorder, adding nodes and their positions to the nonlocal list
        def preorder(node, row, col):
            if not node:
                return
            nodes_with_position.append((col, row, node.val))
            preorder(node.left, row + 1, col - 1)
            preorder(node.right, row + 1, col + 1)
        preorder(root, 0, 0)

        # sort the nodes, first by column, then by row, and then by value
        nodes_with_position.sort()

        # result variable
        res = []

        # previous column value (choose any value above 0 to assert that
        # nodes_with_position[0][0] != prev_col)
        prev_col = 1

        # iterate through nodes, grouping them by column, vertical order is already present by sorting
        for node in nodes_with_position:
            # if a new column is encountered, add an empty list to the result
            if node[0] != prev_col:
                res.append([])
                prev_col = node[0]

            # add node value to the most recent column
            res[-1].append(node[2])

        return res
