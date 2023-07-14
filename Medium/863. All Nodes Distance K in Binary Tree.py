from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, x: int):
            self.val = x
            self.left: "TreeNode" | None = None
            self.right: "TreeNode" | None = None


class Solution:
    """
    Given the root of a binary tree, the value of a target node target, and an
    integer k, return an array of the values of all nodes that have a distance k
    from the target node.

    You can return the answer in any order.

    Constraints:
    - The number of nodes in the tree is in the range [1, 500].
    - 0 <= Node.val <= 500
    - All the values Node.val are unique.
    - target is the value of one of the nodes in the tree.
    - 0 <= k <= 1000
    """

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        res_list: list[int] = []

        def dfs(curr_node: TreeNode, distance: int | None = None) -> int | None:
            """Traverses throught the binary tree finding nodes with k distance from the target node.

            If distance is not None, then a parent of curr_node is the target.
            Returns:
                int | None: Distance to the target node, or None if Unknown
            """
            nonlocal res_list, k

            left_child = curr_node.left
            right_child = curr_node.right

            # if parent is target node
            if distance is not None:
                # if distance exactly k, add node to list, and do not visit
                # children, they could only possibly be further away
                if distance == k:
                    res_list.append(curr_node.val)
                    return

                if left_child:
                    dfs(left_child, distance + 1)
                if right_child:
                    dfs(right_child, distance + 1)
                return

            # if the current node is the target, then the
            # current distance to the target node is 0
            if curr_node is target:
                distance = 0
                if k == 0:
                    res_list.append(curr_node.val)
                if left_child:
                    dfs(left_child, distance + 1)
                if right_child:
                    dfs(right_child, distance + 1)
                return distance

            # target node is neither current node nor any ancestor

            # if left child exists, traverse to left child
            if left_child:
                distance = dfs(left_child)
            if distance is None:
                # target is neither ancestor nor in left subtree
                if right_child:
                    distance = dfs(right_child)
                    if distance is not None:
                        # target was in right subtree
                        distance += 1
                        if left_child:
                            # traverse again to left child if exists,
                            # now knowing distance to target
                            dfs(left_child, distance + 1)
            else:
                # if left subtree contains target, this nodes distance
                # is one greater than the childs distance to the target
                distance += 1
                if right_child:
                    dfs(right_child, distance + 1)

            if distance == k:
                res_list.append(curr_node.val)

            return distance

        dfs(root)
        return res_list
