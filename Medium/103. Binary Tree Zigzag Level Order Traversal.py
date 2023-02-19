from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
    (i.e., from left to right, then right to left for the next level and alternate between).

    Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -100 <= Node.val <= 100
    """

    def zigzagLevelOrder(self, root: TreeNode) -> list[deque[int]]:
        """
        Traverse through levels in preorder, appending to list of nodes of current level.
        O(n) / O(n)     time / space complexity
        """
        def preorder_zigzag(curr_node: TreeNode, level: int):
            nonlocal zigzag_order

            if not curr_node:
                return

            if level >= len(zigzag_order):
                # add new deque to return list if level has never been visited
                zigzag_order.append(deque())

            # append to either left or right of current nodes in level,
            # depending on if the current level is even or odd
            if level % 2:
                zigzag_order[level].appendleft(curr_node.val)
            else:
                zigzag_order[level].append(curr_node.val)

            # traverse in preorder with incremented level
            preorder_zigzag(curr_node.left, level + 1)
            preorder_zigzag(curr_node.right, level + 1)

        # return variable
        zigzag_order = []
        # build zigzag order from root, starting at level 0
        preorder_zigzag(root, 0)
        return zigzag_order
