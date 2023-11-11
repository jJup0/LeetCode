"""
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1.
The edges of the graph are initially represented by the given array edges where
edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from from_i to to_i
with the cost edgeCosti.

Implement the Graph class:
- Graph(int n, int[][] edges) initializes the object with n nodes and the
  given edges.
- addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost].
  It is guaranteed that there is no edge between the two nodes before adding this one.
- int shortestPath(int node1, int node2) returns the minimum cost of a path from
  node1 to node2. If no path exists, return -1. The cost of a path is the sum of
  the costs of the edges in the path.

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= n * (n - 1)
- edges[i].length == edge.length == 3
- 0 <= from_i, to_i, from, to, node1, node2 <= n - 1
- 1 <= edgeCost_i, edgeCost <= 10^6
- There are no repeated edges and no self-loops in the graph at any point.
- At most 100 calls will be made for addEdge.
- At most 100 calls will be made for shortestPath.
"""
import heapq


class Graph:
    """
    Naive Dijkstra implementation without caching any results.
    Beat 83% with no implementation significantly faster.
    """

    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.adj_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for a, b, weight in edges:
            self.adj_list[a].append((b, weight))

    def addEdge(self, edge: list[int]) -> None:
        a, b, weight = edge
        self.adj_list[a].append((b, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        queue: list[tuple[int, int]] = [(0, node1)]
        min_dist = [float("inf")] * self.n
        while queue:
            accu_dist, node = heapq.heappop(queue)
            if min_dist[node] < accu_dist:
                continue
            if node == node2:
                return accu_dist
            for neighbor, dist in self.adj_list[node]:
                new_dist = accu_dist + dist
                if new_dist >= min_dist[neighbor]:
                    continue
                min_dist[neighbor] = new_dist
                heapq.heappush(queue, (accu_dist + dist, neighbor))
        return -1
