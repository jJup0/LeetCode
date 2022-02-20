# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetsum: int) -> int:
        def traverseBT(curNode, prevSum):
            if not curNode:
                return
            currSum = prevSum + curNode.val
            if currSum - targetsum in rec:
                self.retVal += rec[currSum - targetsum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            traverseBT(curNode.left, currSum)
            traverseBT(curNode.right, currSum)
            rec[currSum] -= 1

        self.retVal = 0
        rec = {0: 1}
        traverseBT(root, 0)
        return self.retVal
