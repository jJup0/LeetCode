"""
You are given the root of a binary tree with unique values, and an integer
start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:
- The node is currently uninfected.
- The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
- Each node has a unique value.
- A node with a value of start exists in the tree.
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


class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        self.val_to_neighbors: defaultdict[int, list[int]] = defaultdict(list)
        self._populate_neighbors(root)

        infected: set[int] = set()
        minutes_passed = -1
        queue = [start]
        while queue:
            minutes_passed += 1
            new_queue: list[int] = []
            for val in queue:
                infected.add(val)
                for neighbor in self.val_to_neighbors[val]:
                    if neighbor not in infected:
                        new_queue.append(neighbor)
            queue = new_queue
        return minutes_passed

    def _populate_neighbors(self, node: TreeNode):
        if node.left:
            self.val_to_neighbors[node.val].append(node.left.val)
            self.val_to_neighbors[node.left.val].append(node.val)
            self._populate_neighbors(node.left)
        if node.right:
            self.val_to_neighbors[node.val].append(node.right.val)
            self.val_to_neighbors[node.right.val].append(node.val)
            self._populate_neighbors(node.right)
