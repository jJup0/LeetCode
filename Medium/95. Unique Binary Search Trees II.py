from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode" | None = None,
            right: "TreeNode" | None = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    """
    Given an integer n, return all the structurally unique BST's (binary search
    trees), which has exactly n nodes of unique values from 1 to n. Return the
    answer in any order.

    Constraints:
    - 1 <= n <= 8
    """

    def generateTrees(self, n: int) -> list[TreeNode] | list[None]:
        return self._generate_trees(1, n + 1)

    def _generate_trees(
        self, start_inlc: int, stop_exlc: int
    ) -> list[TreeNode] | list[None]:
        """Recursively generates all structurally unique subtrees for custom ranges.
        O(4^n) / O(4^n)     time / space complexity
        Args:
            start_inlc (int): Starting value, inclusive.
            stop_exlc (int): Stop value, exclusive.
        """
        # if there are no values left to insert, there are no trees,
        # so return list with just None
        if stop_exlc == start_inlc:
            return [None]

        # if there is only one value from which to construct the tree, return that node
        if stop_exlc - start_inlc == 1:
            return [TreeNode(start_inlc)]

        res: list[TreeNode] = []
        for root_val in range(start_inlc, stop_exlc):
            # iterate through all nodes and place them as the root node
            # then generate all possible left and right subtrees
            left_subtrees = self._generate_trees(start_inlc, root_val)
            right_subtrees = self._generate_trees(root_val + 1, stop_exlc)
            for left in left_subtrees:
                for right in right_subtrees:
                    # create all possible trees by combining different left and right subtrees
                    res.append(TreeNode(root_val, left, right))
        return res
