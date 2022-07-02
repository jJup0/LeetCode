from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
    two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
    a node to be a descendant of itself).”
    Constraints:
        The number of nodes in the tree is in the range [2, 10^5].
        -10^9 <= Node.val <= 10^9
        All Node.val are unique.
        p != q
        p and q will exist in the tree.
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # result variable
        lca = None

        # returns 1 if p if child or self, 2 if q is child or self, 3 if both, 0 if neither
        def helper(root: Optional['TreeNode']) -> int:
            nonlocal lca

            # if null or res lowest commmon ancestor found, return 0
            if (not root) or lca:
                return 0

            # set result code if current is p or q
            result_code = 0
            if root == p:
                result_code += 1
            elif root == q:
                result_code += 2

            # check if left and right child contain p and q
            result_code += helper(root.left)
            result_code += helper(root.right)

            # if this node and all its ancestors include p and q, update res,
            # but only if not set so that "higher" ancestors do not override res
            if result_code == 3:
                lca = lca or root

            # return code, to pass up to parents
            return result_code

        # call helper on root node
        helper(root)
        assert lca != None  # type check
        return lca
