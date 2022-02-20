# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        nodeStack = [self.left, self.right]
        if self:
            nodeVals = [self.val]
        else:
            return "[]"
        while nodeStack:
            cNode = nodeStack.pop(0)
            if cNode:
                nodeVals.append(cNode.val)
                nodeStack.append(cNode.left)
                nodeStack.append(cNode.right)
            else:
                nodeVals.append(None)
        for i in range(len(nodeVals)-1, -1, -1):
            if nodeVals[i] != None:
                break
        return str(nodeVals[:i+1])


#
# NON FUNCTIONAL
#
class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        def constructTree(croot, lo, hi):
            if lo >= hi:
                return
            mid = (lo+hi)//2
            croot.left = TreeNode(nums[(lo+mid)//2])
            croot.right = TreeNode(nums[(mid+hi)//2])
            constructTree(croot.left, lo, mid-1)
            constructTree(croot.right, mid+1, hi)

        root = TreeNode(nums[len(nums)//2])
        constructTree(root, 0, len(nums))
        return root


x = Solution()
print(x.sortedArrayToBST([0, 1, 2, 4, 5]))
# y = TreeNode(1, TreeNode(2), TreeNode(3))
# print(y)
