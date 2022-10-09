# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    """
    Given the root of a Binary Search Tree and a target number k, return true if there exist two
    elements in the BST such that their sum is equal to the given target.
    """
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        traverse entire tree, storing node.val in a set. For each node it is checked if
        k - node.val is in the set of "seen" nodes.
        O(n) / O(n)     time / space complexity
        """
        
        seen = set()
        
        # returns findTarget(node, k)
        def preorder(node: Optional[TreeNode]):
            if not node:
                return False
            
            # if this node and a previous node sum up to k return True
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            return preorder(node.left) or preorder(node.right)
        
        return preorder(root)
