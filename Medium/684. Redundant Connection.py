"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n,
with one additional edge added. The added edge has two different vertices
chosen from 1 to n, and was not an edge that already existed. The graph is
represented as an array edges of length n where edges[i] = [a_i, b_i] indicates
that there is an edge between nodes a_i and b_i in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n
nodes. If there are multiple answers, return the answer that occurs last in the
input.

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= a_i < b_i <= edges.length
- a_i!= b_i
- There are no repeated edges.
- The given graph is connected.
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Remove leaf nodes from the graph until there are no more leaf nodes.
        The graph that remains is a cycle, any of its edges can be removed.
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # create adjacency list for graph
        adj_list: list[set[int]] = [set() for _ in range(len(edges) + 1)]
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        # is_in_cycle[i] = True iff after recursively removing leaf nodes node `i` remains
        is_in_cycle = [True] * (len(edges) + 1)
        leaves = [
            node for node, neighbors in enumerate(adj_list) if len(neighbors) == 1
        ]
        # remove leaves from graph, until there are no more leaf nodes
        while leaves:
            leaf_node = leaves.pop()
            is_in_cycle[leaf_node] = False
            for neighbor in adj_list[leaf_node]:
                adj_list[neighbor].discard(leaf_node)
                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)

        # find last edge which is adjacent to two nodes in the cycle
        for a, b in reversed(edges):
            if is_in_cycle[a] and is_in_cycle[b]:
                return [a, b]
        raise ValueError("Invalid Input")
