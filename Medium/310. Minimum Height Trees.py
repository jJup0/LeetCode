"""
A tree is an undirected graph in which any two vertices are connected by
exactly one path. In other words, any connected graph without simple cycles is
a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
where edges[i] = [a_i, b_i] indicates that there is an undirected edge between
the two nodes a_i and b_i in the tree, you can choose any node of the tree as
the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h) ) are
called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path
between the root and a leaf.

Constraints:
- 1 <= n <= 2 * 10^4
- edges.length == n - 1
- 0 <= a_i, b_i < n
- a_i!= b_i
- All the pairs (a_i, b_i) are distinct.
- The given input is guaranteed to be a tree and there will be no repeated edges.
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        O(n + m) / O(n + m)     time / space complexity
        """
        # basically a defaultdict graph, but n is known, and nodes are 0..n so list comprehension works well
        graph: list[set[int]] = [set() for _ in range(n)]

        # all nodes that can only be reached directly through 1 other node, == outermost nodes
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        # go through graph by circling in from all outer nodes, basically removing them from the graph
        # and checking which nodes are now outer nodes
        outer_nodes = [i for i in range(n) if len(graph[i]) <= 1]
        new_outer_nodes: list[int] = []  # next outmost nodes
        while True:
            for node in outer_nodes:
                for connection in graph[node]:
                    graph[connection].remove(node)
                    if len(graph[connection]) == 1:  # new outermost node
                        new_outer_nodes.append(connection)

            # if whole graph is deleted, return the nodes that were outer nodes in this iteration
            if not new_outer_nodes:
                return outer_nodes

            # next iteration with nodes that became outermost nodes in this iteration
            outer_nodes = new_outer_nodes
            new_outer_nodes = []
