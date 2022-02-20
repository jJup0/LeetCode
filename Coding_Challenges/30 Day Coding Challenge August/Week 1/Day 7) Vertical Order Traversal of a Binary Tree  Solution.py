# # Definition for a binary tree node.
# from collections import defaultdict
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right


class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        vertDict = defaultdict(list)
        nodeQueue = [(root, 0)]
        curY = 0
        while nodeQueue:
            next_nodeQueue = []
            for curnode, curX in nodeQueue:
                vertDict[curX].append((curY, curnode.val))
                if curnode.left:
                    next_nodeQueue.append((curnode.left, curX-1))
                if curnode.right:
                    next_nodeQueue.append((curnode.right, curX+1))
            curY += 1
            nodeQueue = next_nodeQueue

        res = [sorted(vertDict[k]) for k in sorted(vertDict.keys())]
        return [[val for _, val in r] for r in res]

#         vertDict = defaultdict(list)
#         nodeQueue = [(root, 0)]
#         donestack = []
#         while nodeQueue:
#             next_nodeQueue = []
#             # curnode, curX = nodeQueue.pop(0)
#             for curnode, curX in nodeQueue:
#                 if curnode:
#                     vertDict[curX].append(curnode.val)
#                     next_nodeQueue.append((curnode.left, curX-1))
#                     next_nodeQueue.append((curnode.right, curX+1))
#             nodeQueue = next_nodeQueue
#         return [values for _, values in sorted(vertDict.items(), key=lambda x: x[0])]
