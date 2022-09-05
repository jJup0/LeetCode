from collections import deque
from typing import List

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


class Solution:
    """
    Given an n-ary tree, return the level order traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal, each group of
    children is separated by the null value (See examples).
    Constraints:
        The height of the n-ary tree is less than or equal to 1000
        The total number of nodes is between [0, 10^4]
    """

    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        # result variable
        level_order = []

        # nodes in current level
        curr_level = [root]

        # nodes in next level
        next_level = []

        # while nodes exist, bfs explore the tree
        while curr_level:
            # add all children of current level nodes to next level, and replace them with their values in the list
            for i, node in enumerate(curr_level):
                next_level.extend(node.children)
                curr_level[i] = node.val

            # add all values of current level nodes to result
            level_order.append(curr_level)

            # prepare node lists for next iteration
            curr_level = next_level
            next_level = []

        return level_order
