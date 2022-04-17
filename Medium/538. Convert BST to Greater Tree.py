from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # prev_greater contains the sum of all the values greater than the one of this node
        # which came from parent nodes
        def get_sum_and_modify(node: Optional[TreeNode], prev_greater: int):
            # if node == None, return 0
            if not node:
                return 0

            # make a copy of the current node value
            prev_val = node.val

            # modify the right tree first, as it is independent of the left tree, just pass on prev_greater
            sum_right = get_sum_and_modify(node.right, prev_greater)

            # make the current node into a "greater-tree node"
            node.val += prev_greater + sum_right

            # get modify the left child tree, where prev_greater is node.val as it is the sum of all values
            # greater than its left child
            sum_left = get_sum_and_modify(node.left, node.val)

            # return the sum of the sub tree
            return prev_val + sum_left + sum_right

        # call helper function on root node, starting with 0 as the sum of previous nodes that are greater
        get_sum_and_modify(root, 0)
        return root
