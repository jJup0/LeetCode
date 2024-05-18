"""
You are given the root of a binary tree with n nodes where each node in the
tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node
to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one
coin.

Constraints:
- The number of nodes in the tree is n.
- 1 <= n <= 100
- 0 <= Node.val <= n
- The sum of all Node.val is n.
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
    def distributeCoins(self, root: TreeNode) -> int:
        """
        n := total nodes, m := depth of tree
        O(n) / O(m)     time / space complexity
        """
        self.res = 0
        self._distribute_coins(root)
        return self.res

    def _distribute_coins(self, node: TreeNode) -> int:
        # coins needed/extra coins of current subtree, every coin
        # needs 1 so subtract 1 from root node's coins
        coin_balance = node.val - 1
        # get coin balance of children
        if node.left:
            coin_balance += self._distribute_coins(node.left)
        if node.right:
            coin_balance += self._distribute_coins(node.right)

        # simply add the current coin balance to the result
        # see this as a request of -coin_balance from the current node to its parent
        # all other coin movements are already handled by children
        self.res += abs(coin_balance)
        return coin_balance
