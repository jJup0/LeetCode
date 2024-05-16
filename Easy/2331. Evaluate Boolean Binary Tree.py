"""
You are given the root of a full binary tree with the following properties:
- Leaf nodes have either the value 0 or 1, where 0 represents False and 1
  represents True.
- Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean
  OR and 3 represents the boolean AND.

The evaluation of a node is as follows:
- If the node is a leaf node, the evaluation is the value of the node, i.e.
  True or False.
- Otherwise, evaluate the node's two children and apply the boolean operation
  of its value with the children's evaluations.

Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 3
- Every node has either 0 or 2 children.
- Leaf nodes have a value of 0 or 1.
- Non-leaf nodes have a value of 2 or 3.
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
    def evaluateTree(self, root: TreeNode) -> bool:
        """
        O(size_of_root) / O(depth_of_root)  time / space complexity
        """
        match root.val:
            case 0:
                return False
            case 1:
                return True
            case 2:
                assert root.left and root.right
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            case 3:
                assert root.left and root.right
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            case num:
                raise ValueError(f"root.val must be between 2 and 3, received {num}")
