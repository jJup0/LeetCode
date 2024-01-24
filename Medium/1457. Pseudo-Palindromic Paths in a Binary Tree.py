"""
Given a binary tree where node values are digits from 1 to 9. A path in the
binary tree is said to be pseudo-palindromic if at least one permutation of the
node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf
nodes.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 9
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode | None" = None,
            right: "TreeNode | None" = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        return self.pseudoPalindromicPaths_bitmap(root)

    def pseudoPalindromicPaths_bitmap(self, root: TreeNode) -> int:
        """
        O(n) / O(depth(root))     time / space complexity
        """

        def inorder(node: TreeNode) -> int:
            """Traverses tree and sums up pseudo-palindromic paths.
            Modifies non-local variable `parity`.

            Args:
                node (TreeNode): Current treenode in inorder traversal.

            Returns:
                int: Number of pseudo palindromic paths, for trees with `root`
                  as the root node, after traversing all subtrees to the
                  left of and in node.
            """
            nonlocal parity, res
            # change parity of node value in bitmap
            parity ^= 1 << node.val

            # if node is a leaf and total parity has maximum one bit set, meaning at most one value
            # has odd parity pseudo palindrome is possible
            if not (node.left or node.right):
                res += parity == 0 or (parity & (parity - 1) == 0)
                # equal to: res += parity.bit_count() <= 1
            else:
                # if node has children, traverse
                if node.left:
                    inorder(node.left)
                if node.right:
                    inorder(node.right)

            # undo parity change before returning
            parity ^= 1 << node.val
            return res

        # parity bitmap, to track parity count of nodes
        parity = 0
        res = 0
        return inorder(root)

    def pseudoPalindromicPaths_arr(self, root: TreeNode) -> int:
        """
        Around same performance as bitmap
        """
        parity = [0] * 10

        def inorder(node: TreeNode | None) -> int:
            if not node:
                return 0

            parity[node.val] ^= 1

            if not (node.left or node.right) and sum(parity) <= 1:
                parity[node.val] ^= 1
                return 1

            res = inorder(node.left) + inorder(node.right)

            parity[node.val] ^= 1
            return res

        return inorder(root)
