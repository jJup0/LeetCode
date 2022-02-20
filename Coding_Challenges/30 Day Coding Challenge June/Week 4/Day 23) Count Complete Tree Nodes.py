# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        goleft = False
        curNode = root
        prevs = []
        depth = 0
        nodeCount = 0
        visitedPaths = set()
        calcedDepth = False

        while True:
            curPathID = ''
            while curNode:
                if calcedDepth:
                    depth += 1
                prevs.append(curNode)
                curNode = curNode.left if goleft else curNode.right
                curPathID += 'l' if goleft else 'r'
            calcedDepth = True
            goleft = False if len(prevs) == depth else True

            if curPathID in visitedPaths:
                # do something like change last l to r
                break
            else:
                visitedPaths.add(curPathID)

            for _ in range(len(prevs)//2):
                prevs.pop()
            curNode = prevs.pop()
        nodeCount = 2**(depth-1) - 1 + curPathID  # covert path string to location on tree
        return nodeCount


class decentSolution:
    def countNodes(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return
            self.nodeCount += 1
            helper(node.left)
            helper(node.right)
        self.nodeCount = 0
        helper(root)
        return self.nodeCount
