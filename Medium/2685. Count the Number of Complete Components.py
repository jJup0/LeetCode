"""
You are given an integer n. There is an undirected graph with n vertices,
numbered from 0 to n - 1. You are given a 2D integer array edges where
edges[i] = [a_i, b_i] denotes that there exists an undirected edge connecting
vertices a_i and b_i.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path
between any two vertices, and no vertex of the subgraph shares an edge with a
vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between
every pair of its vertices.

Constraints:
- 1 <= n <= 50
- 0 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 2
- 0 <= a_i, b_i <= n - 1
- a_i!= b_i
- There are no repeated edges.
"""

from collections import Counter


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def union(self, x: int, y: int):
        self.parent[self.find(x)] = self.find(y)

    def find(self, x: int):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        """

        Complexity:
            Time: O(n + m)
            Space: O(n)
        """
        # find connected connected components
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)

        # get number of nodes and edges in each connected component
        component_node_count: Counter[int] = Counter(uf.find(i) for i in range(n))
        component_edge_count: Counter[int] = Counter(uf.find(edge[0]) for edge in edges)

        # fully connected subgraph of i nodes needs (i * (i - 1) // 2) edges
        # sum up all components that fulfill this property
        return sum(
            component_edge_count[parent] == (node_count * (node_count - 1) // 2)
            for parent, node_count in component_node_count.items()
        )
