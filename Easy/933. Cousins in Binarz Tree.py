# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def traverse(node, parent, depth):
            if not node or (self.xyDict[x][0] and self.xyDict[y][0]):
                return
            if node.val == x:
                self.xyDict[x] = [depth, parent]
            elif node.val == y:
                self.xyDict[y] = [depth, parent]
            traverse(node.left, node, depth+1)
            traverse(node.right, node, depth+1)

        self.xyDict = {x: [None, None], y: [None, None]}
        traverse(root, None, 0)
        return self.xyDict[x][0] == self.xyDict[y][0] and self.xyDict[x][1] != self.xyDict[y][1]
