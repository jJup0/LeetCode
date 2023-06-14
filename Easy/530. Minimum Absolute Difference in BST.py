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
    Given the root of a Binary Search Tree (BST), return the minimum absolute difference
    between the values of any two different nodes in the tree.

    Constraints:
    - The number of nodes in the tree is in the range [2, 10^4].
    - 0 <= Node.val <= 10^5
    """

    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        Build sorted list by in-order traversal of BST.
        Check for minimum distance in sorted list
        O(n) / O(n)  time / space complexity
        """

        nums: list[int] = []

        def in_order(n: TreeNode | None):
            if n is None:
                return
            in_order(n.left)
            nums.append(n.val)
            in_order(n.right)

        in_order(root)

        prev = -100_000
        res = 100_000
        for num in nums:
            res = min(res, num - prev)
            prev = num
        return res
