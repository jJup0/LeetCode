# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X
    there are no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.
    Constraints:
        The number of nodes in the binary tree is in the range [1, 10^5].
        Each node's value is between [-10^4, 10^4].
    """

    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: TreeNode, max_val: int) -> int:
            # if not a node, then it is not a good node
            if not root:
                return 0

            is_good = 0
            # the node's value is greater equal every node's value from root, update max_val and is_good
            if root.val >= max_val:
                max_val = root.val
                is_good = 1

            # apply child node and return sum of good nodes
            return is_good + helper(root.left, max_val) + helper(root.right, max_val)

        # search for good nodes starting from root
        return helper(root, root.val)
