"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Constraints:
- The total number of nodes is in the range [0, 10^4].
- The depth of the n-ary tree is less than or equal to 1000.
"""

import typing

if typing.TYPE_CHECKING:
    # Definition for a Node.
    class Node:
        def __init__(
            self, val: int | None = None, children: list["Node"] | None = None
        ):
            self.val = val
            self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)
