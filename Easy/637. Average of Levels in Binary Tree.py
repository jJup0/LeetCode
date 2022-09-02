from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given the root of a binary tree, return the average value of the nodes on each level in the
    form of an array. Answers within 10-5 of the actual answer will be accepted.
    Constraints:
        The number of nodes in the tree is in the range [1, 104].
        -2^31 <= Node.val <= 2^31 - 1
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # sums and node counts for each level of the tree
        sums = []
        counts = []

        # sums up value and node counts in entire tree
        def sum_levels(node, depth):
            # if a new deepest node has been reached, append to sums and counts
            if depth == len(sums):
                sums.append(node.val)
                counts.append(1)
            else:
                # otherwise update previous entries
                sums[depth] += node.val
                counts[depth] += 1

            # apply to left and right child
            if node.left:
                sum_levels(node.left, depth + 1)
            if node.right:
                sum_levels(node.right, depth + 1)

        # sum levels starting from root with depth 0
        sum_levels(root, 0)

        # calculate averages for each level
        return [sum_ / count for sum_, count in zip(sums, counts)]
