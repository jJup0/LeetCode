# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def bfs(depth):
            newStack = []
            while self.stack:
                curNode = self.stack.pop()
                if not (curNode.left or curNode.right):
                    return depth
                if curNode.left:
                    newStack.append(curNode.left)
                if curNode.right:
                    newStack.append(curNode.right)
            self.stack = newStack
            return bfs(depth + 1)

        if not root:
            return 0
        self.stack = [root]
        return bfs(1)

# apparantly fast but it isnt
# import sys
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         if not (root.left or root.right):
#             return 1
#         res = sys.maxsize
#         if root.left:
#             res = min(res, self.minDepth(root.left))
#         if root.right:
#             res = min(res, self.minDepth(root.right))
#         return res + 1
