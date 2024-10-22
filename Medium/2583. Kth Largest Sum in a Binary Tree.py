"""
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the
same level.

Return the kth largest level sum in the tree (not necessarily distinct). If
there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from
the root.

Constraints:
- The number of nodes in the tree is n.
- 2 <= n <= 10^5
- 1 <= Node.val <= 10^6
- 1 <= k <= n
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
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        def dfs(node: TreeNode, level: int):
            nonlocal level_sums
            if level == len(level_sums):
                level_sums.append(0)
            level_sums[level] += node.val

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        level_sums = [0]
        dfs(root, 0)
        if k - 1 >= len(level_sums):
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]
