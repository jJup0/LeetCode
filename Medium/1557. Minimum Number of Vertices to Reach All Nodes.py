class Solution:
    """
    Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and
    an array edges where edges[i] = [fromi, toi] represents a directed edge from
    node fromi to node toi.

    Find the smallest set of vertices from which all nodes in the graph are
    reachable. It's guaranteed that a unique solution exists.

    Notice that you can return the vertices in any order.

    Constraints:
        2 <= n <= 10^5
        1 <= edges.length <= min(10^5, n * (n - 1) / 2)
        edges[i].length == 2
        0 <= from_i, to_i < n
        All pairs (from_i, to_i) are distinct.
    """

    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        """Find all sources of the DAG. These are needed to reach all other nodes."""
        sources = [1] * n
        for _, to_n in edges:
            sources[to_n] = 0
        return [node for node, is_source in enumerate(sources) if is_source]
