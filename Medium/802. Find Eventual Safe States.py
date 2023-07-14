class Solution:
    """
    There is a directed graph of n nodes with each node labeled from 0 to n - 1.
    The graph is represented by a 0-indexed 2D integer array graph where graph[i]
    is an integer array of nodes adjacent to node i, meaning there is an edge
    from node i to each node in graph[i].

    A node is a terminal node if there are no outgoing edges. A node is a safe
    node if every possible path starting from that node leads to a terminal
    node (or another safe node).

    Return an array containing all the safe nodes of the graph. The answer
    should be sorted in ascending order.

    Constraints:
    - n == graph.length
    - 1 <= n <= 10^4
    - 0 <= graph[i].length <= n
    - 0 <= graph[i][j] <= n - 1
    - graph[i] is sorted in a strictly increasing order.
    - The graph may contain self-loops.
    - The number of edges in the graph will be in the range [1, 4 * 10^4].
    """

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        N = len(graph)
        # store which nodes have been visited, and which are safe
        safe = [True] * N
        visited = [False] * N

        def detect_cycles(curr_node: int):
            """Detects cycles in given graph"""
            nonlocal graph
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
                neighbor_safe = detect_cycles(neighbor)
                # if any neighbor is in a cycle, this node is unsafe
                if not neighbor_safe:
                    return False

            # after traversing through all neighbors, mark
            # as safe again, if no cycle detected
            safe[curr_node] = True
            return True

        # detect cycles starting from each node in the graph
        for i in range(N):
            detect_cycles(i)

        # return nodes which are not in cycles
        return [i for i, s in enumerate(safe) if s]
