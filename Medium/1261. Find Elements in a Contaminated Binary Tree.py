"""
Given a binary tree with the following rules:
1.  root.val == 0
2. For any treeNode:
  1. If treeNode.val has a value x and treeNode.left!= null, then
     treeNode.left.val == 2 * x + 1
  2. If treeNode.val has a value x and treeNode.right!= null, then
     treeNode.right.val == 2 * x + 2

Now the binary tree is contaminated, which means all treeNode.val have been
changed to -1.

Implement the FindElements class:
- FindElements(TreeNode* root) Initializes the object with a contaminated
  binary tree and recovers it.
- bool find(int target) Returns true if the target value exists in the
  recovered binary tree.

Constraints:
- TreeNode.val == -1
- The height of the binary tree is less than or equal to 20
- The total number of nodes is between [1, 10^4]
- Total calls of find() is between [1, 10^4]
- 0 <= target <= 10^6
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


class FindElements:
    def __init__(self, root: TreeNode):
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # values that exist in the tree
        tree_values: set[int] = set()
        root.val = 0
        # dfs stack of nodes to check
        nodes = [root]
        while nodes:
            node = nodes.pop()
            tree_values.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                nodes.append(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                nodes.append(node.right)
        self.vals = tree_values

    def find(self, target: int) -> bool:
        """
        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return target in self.vals
