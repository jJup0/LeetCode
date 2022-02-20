# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        curnode = root
        while curnode:  # find node
            if curnode.val == key:
                break
            prevNode = curnode
            if key > curnode.val:
                curnode = curnode.right
            else:
                curnode = curnode.left
        else:
            return root  # val not found

        if curnode == root:                                     # add dummy node before root if root is target
            prevNode = TreeNode(None, root)

        targetIsRightBranch = True if prevNode.right == curnode else False

        # delete node
        if curnode.right and curnode.left:                      # if two branches, we need to redistribute
            lowestNode, prev = curnode.right, curnode.right  # find lowest value node in right branch
            while lowestNode.left:
                prev = lowestNode
                lowestNode = lowestNode.left

            curnode.val = lowestNode.val        # 'deleting' by changing val to lowest right branch value
            if lowestNode == prev:              # if right branch is actually leaf
                curnode.right = lowestNode.right
            else:
                prev.left = lowestNode.right
        else:  # else we just attach one branch or None
            filledBranch = curnode.right if curnode.right else curnode.left  # either right, left or none
            if targetIsRightBranch:
                prevNode.right = filledBranch
            else:
                prevNode.left = filledBranch
        return root if curnode != root else prevNode.left  # if root was target, return dummy parent
