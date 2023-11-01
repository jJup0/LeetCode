"""
Given the root of a binary search tree (BST) with duplicates, return all the
mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to
  the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal
  to the node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Follow up: Could you do that without using any extra space? (Assume that the implicit
stack space incurred due to recursion does not count).
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode" | None = None,
            right: "TreeNode" | None = None,
        ):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        return self.findMode_no_extra_space(root)

    def findMode_simple(self, root: TreeNode) -> list[int]:
        """
        O(n) / O(n)     time / space
        """

        def dfs(root: TreeNode | None):
            nonlocal val_counter
            if root is None:
                return
            val_counter[root.val] = val_counter.get(root.val, 0) + 1
            dfs(root.left)
            dfs(root.right)

        val_counter: dict[int, int] = dict()
        dfs(root)
        count_for_mode = max(val_counter.values())
        return [val for val, count in val_counter.items() if count == count_for_mode]

    def findMode_no_extra_space(self, root: TreeNode):
        """
        Solution to follow up.
        O(n * average_depth_of_nodes) / O(log(n))    time / space complexity
        """

        def find_mode_count(node: TreeNode, add_to_result: bool):
            """
            Traverses a subtree starting at node, finding out how
            many times the mode occurs or adding modes to `modes` list.

            Args:
                node (TreeNode): Root of the subtree to traverse.
                add_to_result (bool):
                  If true, add node values to the result list if they are the mode,
                  else simply update `mode_count`.
            """
            nonlocal mode_count, modes
            val_count = 1
            # find mode count
            if node.left:
                # for left child, traverse only to right neighbors,
                # unless child also has node.val as its value
                val_count += count_self_and_right(node.left, node.val)
            if node.right:
                # for right child, traverse only to left neighbors,
                # unless child also has node.val as its value
                val_count += count_self_and_left(node.right, node.val)
            if val_count >= mode_count:
                mode_count = val_count
                # append to list of modes if required
                if add_to_result:
                    modes.append(node.val)

            # dfs to children to find their node counts
            if node.left:
                find_mode_count(node.left, add_to_result)
            if node.right:
                find_mode_count(node.right, add_to_result)

        def count_self_and_right(node: TreeNode, val: int) -> int:
            """Returns the amount of nodes in a subtree that have the given val."""
            val_count = 0
            if node.val == val:
                val_count = 1
                if node.left:
                    val_count += count_self_and_right(node.left, val)
            if node.right:
                val_count += count_self_and_right(node.right, val)
            return val_count

        def count_self_and_left(node: TreeNode, val: int) -> int:
            """Analogous to count_self_and_right()."""
            val_count = 0
            if node.val == val:
                val_count = 1
                if node.right:
                    val_count += count_self_and_left(node.right, val)
            if node.left:
                val_count += count_self_and_left(node.left, val)
            return val_count

        # first find how often mode occurs
        mode_count = 1
        find_mode_count(root, False)

        # then add to result list
        modes: list[int] = []
        find_mode_count(root, True)
        return modes
