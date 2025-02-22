"""
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of
this node), then we output the value of this node. If the depth of a node is D,
the depth of its immediate child is D + 1. The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

Constraints:
- The number of nodes in the original tree is in the range [1, 1000].
- 1 <= Node.val <= 10^9
"""

from collections import defaultdict
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


class Solution1:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        """Build list of values and depths and build recursively.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.vals_and_depths = self._convert_traversal_to_values_and_depths(traversal)
        self.vals_and_depths_idx = 0
        dummy = TreeNode(-1)
        self._recover(dummy, -1)
        assert dummy.left
        return dummy.left

    def _convert_traversal_to_values_and_depths(
        self, traversal: str
    ) -> list[tuple[int, int]]:
        index_in_str = 0
        vals_and_depths: list[tuple[int, int]] = []
        while index_in_str < len(traversal):
            value, depth, index_in_str = self._get_next_val_and_depth(
                traversal, index_in_str
            )
            vals_and_depths.append((value, depth))
        # add fake node val and depth as padding to prevent length checks
        vals_and_depths.append((-1, -1))
        return vals_and_depths

    def _get_next_val_and_depth(
        self, traversal: str, index_in_str: int
    ) -> tuple[int, int, int]:
        """
        Starting at `index_in_str` return the value and depth of
        the next node and the index in traversal from where to continue.
        """
        # get depth
        depth = 0
        while traversal[index_in_str] == "-":
            depth += 1
            index_in_str += 1

        # get value
        num_starting_index = index_in_str
        while index_in_str < len(traversal) and traversal[index_in_str] != "-":
            index_in_str += 1
        num = int(traversal[num_starting_index:index_in_str])

        return num, depth, index_in_str

    def _recover(self, parent: TreeNode, depth: int):
        parent.left = self._get_next_node_at_depth(depth)
        if parent.left:
            self._recover(parent.left, depth + 1)

        parent.right = self._get_next_node_at_depth(depth)
        if parent.right:
            self._recover(parent.right, depth + 1)

    def _get_next_node_at_depth(self, depth: int) -> TreeNode | None:
        node_val, node_depth = self.vals_and_depths[self.vals_and_depths_idx]
        if node_depth != depth + 1:
            return None
        self.vals_and_depths_idx += 1
        return TreeNode(node_val)


class Solution2:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        """Iterative approach, store all nodes in a mapping from depth to nodes.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        parent_lvl_map: defaultdict[int, list[TreeNode]] = defaultdict(list)
        # dummy node
        parent_lvl_map[-1] = [TreeNode(-1)]
        depth = 0
        for value_str in traversal.split("-"):
            if value_str == "":
                # empty string means there was another "-", increase depth
                depth += 1
                continue

            node = TreeNode(int(value_str))
            parent_node = parent_lvl_map[depth - 1][-1]
            if not parent_node.left:
                parent_node.left = node
            else:
                parent_node.right = node
            parent_lvl_map[depth].append(node)
            # reset depth to 1 to account for "-" that was removed from splitting
            depth = 1

        # root node is first (and only) node at depth 0
        return parent_lvl_map[0][0]


class Solution(Solution2):
    pass
