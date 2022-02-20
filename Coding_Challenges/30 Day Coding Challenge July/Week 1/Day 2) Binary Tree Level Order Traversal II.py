# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        def traverseBT(node, depth):
            if not node:
                return
            if depth >= len(retVal):
                retVal.append([node.val])
            else:
                retVal[depth].append(node.val)
            traverseBT(node.left, depth+1)
            traverseBT(node.right, depth+1)
        retVal = []
        traverseBT(root, 0)
        return retVal.reverse()
