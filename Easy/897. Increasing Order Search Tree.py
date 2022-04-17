# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        # create a dummy node and curr node to construct the new tree
        dummy = curr = TreeNode()

        def inorder(node):
            nonlocal curr

            if not node:
                return

            # disconnect left tree node to avoid cycle in increasingBST
            left = node.left
            node.left = None

            # to go in order go to left node first
            inorder(left)

            # add the node to as right child of the curr node/pointer
            curr.right = node
            # make curr its right child
            curr = curr.right

            # go through the right child in order
            inorder(node.right)

        # go through the tree inorder and construct the increasingBST
        inorder(root)

        # return the child child of the dummy
        return dummy.right  # type: ignore
