from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    """
    Given the root of a binary tree, return the maximum width of the given tree.

    The maximum width of a tree is the maximum width among all levels.

    The width of one level is defined as the length between the end-nodes (the
    leftmost and rightmost non-null nodes), where the null nodes between the
    end-nodes that would be present in a complete binary tree extending down
    to that level are also counted into the length calculation.

    It is guaranteed that the answer will in the range of a 32-bit signed integer.

    Constraints:
        The number of nodes in the tree is in the range [1, 3000].
        -100 <= Node.val <= 100
    """

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # levels[i] = [lowest_x_coordinate_for_depth_i, highest_x_coordinate_for_depth_i]
        levels: list[list[int]] = []

        def preorder(root: TreeNode, depth: int, x_coord: int):
            if depth == len(levels):
                # if at new deepest level, this node is the leftmost node
                levels.append([x_coord, x_coord])

            # else this is the rightmost node for the current depth so far
            levels[depth][1] = x_coord

            # recurse to child nodes
            child_depth = depth + 1
            # left childs x coordinate is double that of its parent
            left_child_x = x_coord << 1
            if root.left:
                preorder(root.left, child_depth, left_child_x)
            if root.right:
                preorder(root.right, child_depth, left_child_x + 1)

        # traverse starting from root at depth 0 and any x-coordinate
        preorder(root, 0, 0)
        # get largest width of all levels
        return max(most_right - most_left for most_left, most_right in levels) + 1
