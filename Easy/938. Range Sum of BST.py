"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low,
high].

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        O(n) / O(depth(root))   time / space complexity
        """
        def helper(node: TreeNode) -> int:
            mysum = 0
            if node.left and node.val > low:
                mysum += helper(node.left)
            if node.right and node.val < high:
                mysum += helper(node.right)
            if low <= node.val <= high:
                mysum += node.val
            return mysum

        return helper(root)
