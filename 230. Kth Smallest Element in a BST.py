# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary search tree, and an integer k, return the kth smallest value
# (1-indexed) of all the values of the nodes in the tree.


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # constraint: 1 <= k <= n <= 10000 (where n is number of nodes in tree)
        res = -1
        more_than_n = 10001
        # k is 1-indexed
        k -= 1

        # returns the amount of nodes smaller than node, plus nodes in right subtree
        def inorder(node, smaller_nodes):
            nonlocal res

            # if node == None, return smaller nodes
            # if result has been found then smaller_nodes == more_than_n,continuing the early return chain
            # (not necessary for correctness, but good for performance)
            if not node or res != -1:
                return smaller_nodes

            # update count after passing through all nodes in left child
            smaller_nodes = inorder(node.left, smaller_nodes)

            # if amount of nodes smaller than left child + node in right subtree of left child is equal to k,
            # then this node is the kth smallest
            if smaller_nodes == k:
                res = node.val
                # return very large value to exit early and prevent further calls (performance)
                return more_than_n

            # update count after passing through all nodes in right child, +1 because self is smaller
            return inorder(node.right, smaller_nodes + 1)

        # call helper function with 0 previous smaller nodes
        inorder(root, 0)
        return res

    # def old_kthSmallest(self, root: TreeNode, k: int) -> int:
    #     ret = None

    #     def dfs(node, count):
    #         nonlocal ret

    #         if (ret != None) or not(node):
    #             return count + 1
    #         count = dfs(node.left, count)
    #         if count == k:
    #             ret = node.val
    #         count = dfs(node.right, count)
    #         if count == k:
    #             ret = node.val
    #         return count

    #     dfs(root, 0)
    #     return ret
