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
        self.parents: dict[int, TreeNode] = {root.val: root}
        self.start = start
        self.root: TreeNode
        queue = [start]
        infected: set[int] = set([start])

        round = 0
        while queue:
            rounds += 1
            new_queue = []
            for node in queue:
                infected.add(node)
                parent = self.parents[node]
                if parent.val not in infected:
                    new_queue.add(parent.val)

        return rounds

    def _get_parents_and_find_root(self, node: TreeNode):
        if node.val == self.start:
            self.root = node
        if node.left:
            self.parents[node.left.val] = node
            self._get_parents_and_find_root(node.left)
        if node.right:
            self.parents[node.right.val] = node
            self._get_parents_and_find_root(node.right)
