from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
    the sum of the node values in the path equals targetSum. Each path should be returned as a list
    of the node values, not node references.
    A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a
    node with no children.
    Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -1000 <= Node.val <= 1000
        -1000 <= targetSum <= 1000
    """

    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        # helper function sums up paths, and appends value paths to res if root is a leaf node and
        # the target sum is met
        def helper(root: TreeNode, curr_sum: int, past: List[int]) -> None:
            # add current value to past values
            curr_sum += root.val
            past.append(root.val)

            # if node is leaf, check current sum
            if not (root.left or root.right):
                if curr_sum == target_sum:
                    paths.append(past.copy())
            else:
                # continue path with children
                if root.left:
                    helper(root.left, curr_sum, past)
                if root.right:
                    helper(root.right, curr_sum, past)

            # remove value from past values list
            past.pop()
            curr_sum -= root.val

        # result vairbale
        paths = []
        
        # ensure root not None
        if root:
            helper(root, 0, [])
        return paths
