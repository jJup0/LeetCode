"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge from
node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node
if every possible path starting from that node leads to a terminal node (or
another safe node).

Return an array containing all the safe nodes of the graph. The answer should
be sorted in ascending order.

Constraints:
- n == graph.length
- 1 <= n <= 10^4
- 0 <= graph[i].length <= n
- 0 <= graph[i][j] <= n - 1
- graph[i] is sorted in a strictly increasing order.
- The graph may contain self-loops.
- The number of edges in the graph will be in the range [1, 4 * 10^4].
"""


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """
        Mark all sink nodes as safe, virtually remove them from the graph,
        and check if their incoming neighbors are now new sink nodes.
        Repeat until no new sink nodes are found.
        Complexity:
            Time: O(n + m)
            Space: O(n + m)
        """
        # construct the reverse graph
        reverse_graph: list[list[int]] = [[] for _ in range(len(graph))]
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)

        # for each node, keep track of its unsafe neighbors
        unsafe_neighbors_count = [len(neighbors) for neighbors in graph]
        # nodes without outgoing edges are automatically safe
        safe_nodes = [i for i, neighbors in enumerate(graph) if not neighbors]

        # iterate through safe nodes; note that nodes are appended to
        # this list during iteration
        for sink in safe_nodes:
            for reverse_neighbor in reverse_graph[sink]:
                # decrement unsafe node count of reverse neighbor and add to
                # safe nodes list if it has no more unsafe neighbors
                unsafe_neighbors_count[reverse_neighbor] -= 1
                if unsafe_neighbors_count[reverse_neighbor] == 0:
                    safe_nodes.append(reverse_neighbor)

        # not needed, just for optimal time complexity instead of using safe_nodes.sort()
        node_is_safe = [False] * len(graph)
        for safe_node in safe_nodes:
            node_is_safe[safe_node] = True
        safe_nodes = [i for i, safe in enumerate(node_is_safe) if safe]
        return safe_nodes

    def eventualSafeNodes_cycles(self, graph: list[list[int]]) -> list[int]:
        """
        Different approach, for each graph DFS with memoization if the node is
        part of a cycle, if it is, then not all path leads to a terminal node.

        Complexity:
            Time: O(n + m)
            Space: O(n)
        """

        def is_part_of_cycle(curr_node: int) -> bool:
            """Detects cycles in given graph"""
            nonlocal graph, safe, visited
            # if already visited, return previous safety value
            if visited[curr_node]:
                return safe[curr_node]

            # mark as visited
            visited[curr_node] = True
            # mark as unsafe temporarily, so when recursively visiting neighbors
            # and coming back to this node, a cycle is detected
            # all nodes "on the way" are also marked and left and unsafe when a
            # cycle is detected
            safe[curr_node] = False
            for neighbor in graph[curr_node]:
                neighbor_safe = is_part_of_cycle(neighbor)
                # if any neighbor is in a cycle, this node is unsafe
                if not neighbor_safe:
                    return False

            # after traversing through all neighbors, mark
            # as safe again, if no cycle detected
            safe[curr_node] = True
            return True

        n = len(graph)
        # store which nodes have been visited, and which are safe
        safe = [True] * n
        visited = [False] * n

        # detect cycles starting from each node in the graph
        for i in range(n):
            is_part_of_cycle(i)

        # return nodes which are not in cycles
        return [i for i, s in enumerate(safe) if s]
