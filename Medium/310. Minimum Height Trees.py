# minimum height will be determined by the "hardest to reach" nodes == outermost nodes
class Solution:
    def findMinHeightTrees(self, n, edges):
        #basically a defaultdict graph, but n is known, and nodes are 0..n so list comprehension works well
        graph = [set() for _ in range(n)]           
        
        #all nodes that can only be reached directly through 1 other node, == outermost nodes 
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        # go through graph by circling in from all outer nodes, basically removing them from the graph
        # and checking which nodes are now outer nodes
        outer_nodes = [i for i in range(n) if len(graph[i]) < 2]      
        new_outer_nodes = []                                                 #next outmost nodes
        while True:
            for node in outer_nodes:
                for connection in graph[node]:
                    graph[connection].remove(node)
                    if len(graph[connection]) == 1:                 #new outermost node
                        new_outer_nodes.append(connection)
            
            # if whole graph is deleted, return the nodes that were outer nodes in this iteration
            if not new_outer_nodes:
                return outer_nodes

            # next iteration with nodes that became outermost nodes in this iteration
            outer_nodes = new_outer_nodes
            new_outer_nodes = []
            
            