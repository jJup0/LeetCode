"""
There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
integer array edges, where each edges[i] = [u_i, v_i] denotes a bi-directional
edge between vertex u_i and vertex v_i. Every vertex pair is connected by at
most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source
to vertex destination.

Given edges and the integers n, source, and destination, return true if there
is a valid path from source to destination, or false otherwise.

Constraints:
- 1 <= n <= 2 * 10^5
- 0 <= edges.length <= 2 * 10^5
- edges[i].length == 2
- 0 <= u_i, v_i <= n - 1
- u_i!= v_i
- 0 <= source, destination <= n - 1
- There are no duplicate edges.
- There are no self edges.
"""


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        neighbors: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        seen: set[int] = set()
        to_visit = [source]
        while to_visit:
            node = to_visit.pop()
            print(f"{node=}")
            for neighbor in neighbors[node]:
                if neighbor in seen:
                    continue
                if neighbor == destination:
                    return True
                seen.add(neighbor)
                to_visit.append(neighbor)
        return False
