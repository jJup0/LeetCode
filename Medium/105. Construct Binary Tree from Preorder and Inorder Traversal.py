# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    """
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a
    binary tree and inorder is the inorder traversal of the same tree, construct and return the
    binary tree.
    Constraints:
        1 <= preorder.length <= 3000
        inorder.length == preorder.length
        -3000 <= preorder[i], inorder[i] <= 3000
        preorder and inorder consist of unique values.
        Each value of inorder also appears in preorder.
        preorder is guaranteed to be the preorder traversal of the tree.
        inorder is guaranteed to be the inorder traversal of the tree.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder_start_idx, inorder_end_idx):
            # if there are no values left to take out of inorder, return null
            if (inorder_start_idx == inorder_end_idx):
                return None

            # get next value to use from preorder, and construct root
            val = preorder[self.p_idx]
            self.p_idx += 1
            root = TreeNode(val)

            # find where the current value fits in inorder
            inorder_split_idx = inorder.index(val, inorder_start_idx, inorder_end_idx)

            # left children are filled with all values that come before this node in inorder list (by definition)
            # so construct left child with those values
            root.left = helper(inorder_start_idx, inorder_split_idx)

            # apply same principle to right
            root.right = helper(inorder_split_idx + 1, inorder_end_idx)

            # return the constructed tree
            return root

        self.p_idx = 0
        return helper(0, len(preorder))

    def buildTreePureRecusion(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Same algorithm as above, might be easier to understand. More expensive due to list slices.
        """
        # if there are no values left, return null
        if not preorder:
            return None

        # get next value to use from preorder, and construct root
        val = preorder[0]
        root = TreeNode(val)

        # find where the current value fits in inorder
        inorder_split_idx = inorder.index(val)

        # left children are filled with all values that come before this node in inorder list (by definition)
        # so construct left child with those values
        root.left = self.buildTreePureRecusion(preorder[1:inorder_split_idx+1], inorder[:inorder_split_idx])

        # apply same principle to right
        root.right = self.buildTreePureRecusion(preorder[inorder_split_idx + 1:], inorder[inorder_split_idx + 1:])

        # return the constructed tree
        return root
