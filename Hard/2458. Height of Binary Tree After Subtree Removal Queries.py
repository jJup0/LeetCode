"""
You are given the root of a binary tree with n nodes. Each node is assigned a
unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query
you do the following:
- Remove the subtree rooted at the node with the value queries[i] from the
  tree. It is guaranteed that queries[i] will not be equal to the value of the root.

Return an array answer of size m where answer[i] is the height of the tree
after performing the ith query.

Note:
- The queries are independent, so the tree returns to its initial state after
  each query.
- The height of a tree is the number of edges in the longest simple path from
  the root to some node in the tree.

Constraints:
- The number of nodes in the tree is n.
- 2 <= n <= 10^5
- 1 <= Node.val <= n
- All the values in the tree are unique.
- m == queries.length
- 1 <= m <= min(n, 10^4)
- 1 <= queries[i] <= n
- queries[i]!= root.val
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
    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
        """
        Complexity:
            Time:  O(n + m)
            Space: O(n)
        """
        # self.node_to_height_and_level[i] = (height of node i, distance from root to node i)
        self.node_to_height_and_level: dict[int, tuple[int, int]] = {}
        # self.level_to_two_deepest[i] =
        #   (depth of second deepest node at level i, depth of deepest node at level i)
        self.level_to_two_deepest: list[tuple[int, int]] = []
        self._get_height_and_map_nodes(root, 0)

        return [self._get_height_of_pruned_tree(node_val) for node_val in queries]

    def _get_height_and_map_nodes(self, node: TreeNode | None, level: int) -> int:
        """Returns height of `node` and fills `self.node_to_height_and_level`

        If node has no children, depth = 0.

        Args:
            node (TreeNode | None): Current node.
            level (int): Level of current node, i.e. distance from root.

        Returns:
            int: Height of node.

        Complexity (when called with root):
            Time:  O(n)
            Space: O(n)
        """
        if not node:
            return -1
        if level == len(self.level_to_two_deepest):
            # new deepest level reached, append to levels
            self.level_to_two_deepest.append((-1, -1))

        # get children heights
        children_height = max(
            self._get_height_and_map_nodes(node.left, level + 1),
            self._get_height_and_map_nodes(node.right, level + 1),
        )
        height = children_height + 1

        # update maximum heights at level if necessary
        second_highest, highest = self.level_to_two_deepest[level]
        if height > highest:
            self.level_to_two_deepest[level] = (highest, height)
        elif height > second_highest:
            self.level_to_two_deepest[level] = (height, highest)

        self.node_to_height_and_level[node.val] = (height, level)
        return height

    def _get_height_of_pruned_tree(self, node_val_to_prune: int) -> int:
        """
        Returns the height of the root of the tree after removing the node with the given value.
        O(1) / O(1)     time / space complexity
        """
        depth_of_node, level = self.node_to_height_and_level[node_val_to_prune]
        two_maxes = self.level_to_two_deepest[level]
        deepest_at_level = max(two_maxes)
        if deepest_at_level == depth_of_node:
            return min(two_maxes) + level
        return deepest_at_level + level
