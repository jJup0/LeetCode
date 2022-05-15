from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return the sum of values of its deepest leaves.
    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        1 <= Node.val <= 100
    """

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # track deepest depth, and sum at that depth
        deepest = -1
        res = 0

        def dfs(node, depth):
            # constraint: number of nodes > 0, no need to check for null

            # check for null in parent to avoid function call
            has_child = False
            if node.left:
                dfs(node.left, depth + 1)
                has_child = True
            if node.right:
                dfs(node.right, depth + 1)
                has_child = True

            # go in post order to avoid unnecessary checks for depth
            if not has_child:
                nonlocal deepest, res
                # if node deeper than deepest so far, reset res and update deepest
                if depth > deepest:
                    deepest = depth
                    res = node.val
                # if depth equal to deepest, add it to summ
                elif depth == deepest:
                    res += node.val

        # go through tree in post order to calculate res
        dfs(root, 0)
        return res
