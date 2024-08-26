"""
Given the root of an n-ary tree, return the postorder traversal of its nodes'
values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a Node.
    class Node:
        def __init__(self, val: int, children: list["Node"] | None = None):
            self.val = val
            self.children = children or []


class Solution:
    def postorder(self, root: "Node | None") -> list[int]:
        """
        Follow up iterative. Keep set of visited node and append node values at second visit.
        O(n) / O(n)     time / space complexity
        """
        if not root:
            return []

        visited: set[Node] = set()
        stack: list[Node] = [root]
        res: list[int] = []
        while stack:
            node = stack.pop()
            if node in visited:
                res.append(node.val)
                continue

            # append node to stack again, at next visit add node value
            visited.add(node)
            stack.append(node)

            for node in reversed(node.children):
                stack.append(node)

        return res
