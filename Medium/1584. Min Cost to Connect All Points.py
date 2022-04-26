import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # result variable
        cost = 0

        # constraint: -10^6 <= xi, yi <= 10^6
        max_int = 2 << 30

        n = len(points)

        # smallest distance to any previous point
        shortest_dist = [max_int for _ in range(n)]

        # vertex 0 will virtually connect to nothing at first iteration of prims algorithm
        shortest_dist[0] = 0

        # construct edges between all vertices in O(n^2) time and space
        edges = [[0]*n for _ in range(n)]
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1:], start=i + 1):
                distance = abs(x1 - x2) + abs(y1 - y2)
                edges[i][j] = distance
                edges[j][i] = distance

        # construct a set tracking remaining nodes in O(n) time and space
        remaining = set(i for i in range(n))

        # use version of prims algorithm with n iterations
        while remaining:
            # find the vertex with the smallest distance to any previous vertex in O(n) time
            v = -1
            smallest_edge = max_int + 1
            for i in remaining:
                if shortest_dist[i] < smallest_edge:
                    v = i
                    smallest_edge = shortest_dist[i]

            remaining.remove(v)
            cost += smallest_edge

            # update shortest dist of all remaining nodes in O(n) time
            vw_distances = edges[v]
            for w in remaining:
                distance = vw_distances[w]
                if (distance < shortest_dist[w]):
                    shortest_dist[w] = distance

        return cost

    def minCostConnectPointsStolen(self, points: List[List[int]]) -> int:
        max_int = 2 << 30
        graph = [[max_int, x, y] for (x, y) in points]
        graph[0][0] = 0
        cost = 0
        while graph:
            dist, x, y = heapq.heappop(graph)
            cost += dist
            for neighbor in graph:
                old_dist, neighbor_x, neighbor_y = neighbor
                dist_to_curr = abs(x-neighbor_x) + abs(y-neighbor_y)
                if dist_to_curr < old_dist:
                    neighbor[0] = dist_to_curr
            heapq.heapify(graph)
        return cost
