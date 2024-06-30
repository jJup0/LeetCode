"""
Alice and Bob have an undirected graph of n nodes and three types of edges:
- Type 1: Can be traversed by Alice only.
- Type 2: Can be traversed by Bob only.
- Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [type_i, u_i, v_i] represents a
bidirectional edge of type type_i between nodes u_i and v_i, find the maximum
number of edges you can remove so that after removing the edges, the graph can
still be fully traversed by both Alice and Bob. The graph is fully traversed by
Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and
Bob cannot fully traverse the graph.
"""


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))
        self.disjoint_set_count = n

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Joins node x and y together. Returns true if they are already connected,
        meaning the edge can be removed and false otherwise meaning the edge is necessary.
        """
        xparent = self.find(x)
        yparent = self.find(y)
        if xparent == yparent:
            # the two nodes are already connected, this edge is not required
            return True

        # nodes are not connected yet, this edge is required
        self.parent[xparent] = yparent
        self.disjoint_set_count -= 1
        return False

    def fully_connected(self) -> bool:
        return self.disjoint_set_count == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        """
        Build the graph edge by edge, prioritizing type 3 edges, removing
        all edges that do not connect two disjoint forests.
        O(n + m) / O(n)     time / space complexity
        """
        alice = UnionFind(n)
        bob = UnionFind(n)
        result = 0

        for edge_type, u, v in edges:
            if edge_type == 3:
                # add type 3 edge "keep decision" only once to result
                result += alice.union(u, v)
                bob.union(u, v)

        for edge_type, u, v in edges:
            if edge_type == 1:
                result += alice.union(u, v)
            if edge_type == 2:
                result += bob.union(u, v)

        if alice.fully_connected() and bob.fully_connected():
            return result
        return -1
