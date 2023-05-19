from typing import Literal


class Solution:
    """
    There is an undirected graph with n nodes, where each node is numbered between
    0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes
    that node u is adjacent to. More formally, for each v in graph[u], there is an
    undirected edge between node u and node v. The graph has the following properties:

      - There are no self-edges (graph[u] does not contain u).
      - There are no parallel edges (graph[u] does not contain duplicate values).
      - If v is in graph[u], then u is in graph[v] (the graph is undirected).
      - The graph may not be connected, meaning there may be two nodes u and v
          such that there is no path between them.

    A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

    Return true if and only if it is bipartite.

    Constraints:
        graph.length == n
        1 <= n <= 100
        0 <= graph[u].length < n
        0 <= graph[u][i] <= n - 1
        graph[u] does not contain u.
        All the values of graph[u] are unique.
        If graph[u] contains v, then graph[v] contains u.
    """

    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        O(n + m) / O(n)     time / space complexity
        """

        def dfs(node: int, set_value: Literal[-1] | Literal[1]):
            """DFS traverses through neighbors, partitioning them.
            Returns true if bipartite was partitioning successful, false otherwise.
            """
            nonlocal graph
            # if node is unvisited, set its value, and dfs to neighbors
            if partition_of_node[node] == 0:
                partition_of_node[node] = set_value
                for neighbor in graph[node]:
                    partitionable = dfs(neighbor, -set_value)
                    if not partitionable:
                        return False
            elif partition_of_node[node] != set_value:
                # if not is visited, but there is a discrepency between expected and
                # actual partition, bipartite partitioning not possible, return false
                return False

            return True

        n = len(graph)
        # -1 <= partition_of_node[i] <= 1. -1 == "left", 0 == unpartitioned/unvisited, 1 == "right"
        partition_of_node = [0] * n

        # loop through all nodes, and start dfs if node has not been partitioned
        for node in range(n):
            if partition_of_node[node] == 0:
                partitionable = dfs(node, 1)
                if not partitionable:
                    return False
        return True
