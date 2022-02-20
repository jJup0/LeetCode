"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def dfs(node: 'Node') -> None:
            if not node:
                return

            if not (node.val in self.newNodes):
                self.newNodes[node.val] = Node(node.val)
                for n in node.neighbors:
                    dfs(n)

        def connectNeighbors(node: 'Node'):
            if not (node.val in self.visited):
                self.visited.add(node.val)
                self.newNodes[node.val].neighbors = [self.newNodes[neighbor.val] for neighbor in node.neighbors]
                for neighbor in node.neighbors:
                    connectNeighbors(neighbor)

        return self.cloneGraphStolen(node)

        if not node:
            return None

        self.newNodes = dict()
        self.visited = set()
        dfs(node)
        connectNeighbors(node)
        return self.newNodes[1]

    # mine was slow first two times, turns out not really
    # heavyly changed and optimized

    def cloneGraphStolen(self, node: 'Node') -> 'Node':
        def dfs(node):
            copy_node = Node(node.val)
            newNodes[node.val] = copy_node

            copy_node.neighbors = [newNodes[neighbor.val] if (neighbor.val in newNodes) else dfs(neighbor) for neighbor in node.neighbors]

            return copy_node

        newNodes = dict()
        return dfs(node) if node else None
