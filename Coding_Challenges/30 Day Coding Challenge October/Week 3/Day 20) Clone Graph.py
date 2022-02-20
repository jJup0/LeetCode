# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
from collections import defaultdict


class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        def helper(curNode, _neighbors, depth):
            # print("depth:", depth, "|", curNode.val, [n.val for n in _neighbors])
            print(curNode.val)
            for neighbor in _neighbors:
                if neighbor.val in done[curNode.val]:
                    print(f"val {neighbor.val} in done {done[curNode.val]}")
                    continue
                done[curNode.val].add(neighbor.val)
                newNeighbor = helper(Node(neighbor.val), neighbor.neighbors, depth + 1)
                if newNeighbor:
                    curNode.neighbors.append(newNeighbor)
            return curNode

        done = defaultdict(set)
        ret = helper(Node(root.val), root.neighbors, 0)
        return ret
