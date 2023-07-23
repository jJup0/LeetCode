from functools import cache
from typing import TYPE_CHECKING

if TYPE_CHECKING or True:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode | None" = None,
            right: "TreeNode | None" = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    """
    Given an integer n, return a list of all possible full binary trees withnnodes. Each
    node of each tree in the answer must have Node.val == 0.

    Each element of the answer is the root node of one possible tree. You may return the
    final list of trees in any order.

    A full binary tree is a binary tree where each node has exactly 0 or 2 children.

    Constraints:
    - 1 <= n <= 20
    """

    @cache
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        # even counts have no full binary trees
        if n % 2 == 0:
            return []

        # base case
        if n == 1:
            return [TreeNode(0)]

        res: list[TreeNode] = []
        # iterate through all possible distributions of node
        # counts for left and right subtree
        for nodes_for_left_subtree in range(1, n, 2):
            # get all full subtrees for node counts
            left = self.allPossibleFBT(nodes_for_left_subtree)
            right = self.allPossibleFBT(n - nodes_for_left_subtree - 1)

            # combinatorically pair up all possible subtrees
            for l in left:
                for r in right:
                    # construct new treenode from left and right
                    res.append(TreeNode(0, left=l, right=r))

        return res
