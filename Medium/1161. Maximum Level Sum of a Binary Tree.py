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
    Given the root of a binary tree, the level of its root is 1,
    the level of its children is 2, and so on.

    Return the smallest level x such that the sum of all the
    values of nodes at level x is maximal.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -10^5 <= Node.val <= 10^5
    """

    def maxLevelSum(self, root: TreeNode) -> int:
        """O(n) / O(n)  time / space complexity"""
        # l_sums[i] is total sum of level i (0-indexed)
        l_sums: list[int] = []

        def preorder(node: TreeNode, level: int):
            nonlocal l_sums
            # if level has never been reached, add to level sums
            if level >= len(l_sums):
                l_sums.append(0)
            l_sums[level] += node.val
            # visit children, with incremented level
            if node.left:
                preorder(node.left, level + 1)
            if node.right:
                preorder(node.right, level + 1)

        # start at root
        preorder(root, 0)
        max_sum = max(l_sums)
        # expected result is 1-indexed, so add 1
        return l_sums.index(max_sum) + 1
