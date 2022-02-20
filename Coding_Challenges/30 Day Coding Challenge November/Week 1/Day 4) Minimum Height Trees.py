# minimum height will be determined by the "hardest to reach" nodes == outermost nodes
class Solution:
    def findMinHeightTrees(self, n, edges):
        graph = [set() for _ in range(n)]                           #basically a defaultdict, but n is known so this works well
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        outerNodes = [i for i in range(n) if len(graph[i]) < 2]      #all nodes that can only be reached directyl through 1 other node, == outermost nodes 
        next_oN = []                                                 #next outmost nodes
        while True:
            for node in outerNodes:
                for connection in graph[node]:
                    graph[connection].remove(node)
                    if len(graph[connection]) == 1:                 #new outermost node
                        next_oN.append(connection)

            if not next_oN:
                return outerNodes

            next_oN, outerNodes = [], next_oN
