from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    You are given the root of a binary search tree (BST), where the values of exactly two
    nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
    Constraints:
        The number of nodes in the tree is in the range [2, 1000].
        -2^31 <= Node.val <= 2^31 - 1
    """

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # traverses the tree in order. If one were to print out the nodes, the first node to be swapped larger than
        # its successor, and the second node smaller than its predecessor
        def in_order(root: Optional[TreeNode]):
            nonlocal pred_node
            nonlocal first_node
            nonlocal second_node
            if (not root):
                return

            in_order(root.left)

            # If this node is smaller than its predecessor there are two cases to consider:
            if (root.val <= pred_node.val):
                # If first node has been found, this is the second node to be swapped
                if first_node:
                    second_node = root
                else:
                    # If first element has not been found, predecessor is node to be swapped
                    first_node = pred_node
                    second_node = root

            pred_node = root

            in_order(root.right)

        pred_node: TreeNode = TreeNode(float('-inf'))
        first_node: Optional[TreeNode] = None
        second_node: Optional[TreeNode] = None

        # In order traversal to find the two nodes to be swapped
        in_order(root)

        assert(first_node and second_node)  # typing assertion

        # swap the values of the two nodes
        first_val = first_node.val
        first_node.val = second_node.val
        second_node.val = first_val
