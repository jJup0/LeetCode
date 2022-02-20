# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def traverseBT(node, posinrow, depth):
            nodesByDepth[depth].add(posinrow)
            if node.left:
                traverseBT(node.left, posinrow*2, depth+1)
            if node.right:
                traverseBT(node.right, posinrow*2+1, depth+1)

        nodesByDepth = defaultdict(set)
        traverseBT(root, 1, 0)
        retVal = 1
        for nodeset in nodesByDepth.values():
            retVal = max(retVal, max(nodeset) - min(nodeset)+1)
        return retVal
