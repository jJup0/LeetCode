# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said
    to be pseudo-palindromic if at least one permutation of the node values in the path is a
    palindrome.
    Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
    Constraints:
        The number of nodes in the tree is in the range [1, 10^5].
        1 <= Node.val <= 9
    """

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # result variable and parity bitmap, to track parity count of nodes
        parity = 0

        # helper function which does exactly what pseudoPalindromicPaths does, just with a nonlocal
        # bitmap and result variable; prefer to not change method signature by adding default
        # parameter [0]*10 bitmap
        def inorder(node: TreeNode) -> int:
            nonlocal parity
            res = 0
            # change parity of node value in bitmap
            parity ^= 1 << node.val

            # if node is a leaf and total parity has maximum one bit set, meaning at most one value
            # has odd parity pseudo palindrome is possible
            if not(node.left or node.right):
                res += parity == 0 or (parity & (parity-1) == 0)
                # alternatively: res += parity.bit_count() <= 1
            else:
                # if node has children, traverse inorder
                if node.left:
                    res += inorder(node.left)
                if node.right:
                    res += inorder(node.right)

            # undo parity change before returning
            parity ^= 1 << node.val
            return res

        return inorder(root)

    def pseudoPalindromicPaths_arr(self, root: TreeNode) -> int:
        """
        Around same performance as bitmap
        """
        parity = [0] * 10

        def inorder(node):
            if not node:
                return 0

            parity[node.val] ^= 1

            if not(node.left or node.right) and sum(parity) <= 1:
                parity[node.val] ^= 1
                return 1

            res = inorder(node.left) + inorder(node.right)

            parity[node.val] ^= 1
            return res

        return inorder(root)

    def pseudoPalindromicPaths_2000_all_local(self, root: TreeNode) -> int:
        """
        For some reason much slower.
        """
        def inorder(node: TreeNode, parity) -> int:
            res = 0
            parity ^= 1 << node.val
            if not(node.left or node.right):
                res += parity == 0 or (parity & (parity-1) == 0)
            else:
                if node.left:
                    res += inorder(node.left, parity)
                if node.right:
                    res += inorder(node.right, parity)
            return res

        return inorder(root, 0)

    def pseudoPalindromicPaths_2000ms_nonlocal(self, root: TreeNode) -> int:
        """
        For some reason much slower.
        """
        res = parity = 0

        def inorder(node: TreeNode) -> None:
            nonlocal res, parity
            parity ^= 1 << node.val

            if not(node.left or node.right):
                res += parity == 0 or (parity & (parity-1) == 0)
            else:
                if node.left:
                    inorder(node.left)
                if node.right:
                    inorder(node.right)

            parity ^= 1 << node.val

        inorder(root)
        return res
