"""
There are n cities numbered from 0 to n-1. Given the array edges where
edges[i] = [from_i, to_i, weight_i] represents a bidirectional and weighted
edge between cities from_i and to_i, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through
some path and whose distance is at most distanceThreshold, If there are
multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the
sum of the edges' weights along that path.

Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 3
- 0 <= from_i < to_i < n
- 1 <= weight_i, distanceThreshold <= 10^4
- All pairs (from_i, to_i) are distinct.
"""

import heapq


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distance_threshold: int
    ) -> int:
        """
        Dijkstra from each city to find reachable cities.
        O(n^2 * log(n)) / O(m)    time / space complexity
        """
        self.n = n
        self.distance_threshold = distance_threshold
        # construct adjacency graph
        self.graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for a, b, dist in edges:
            self.graph[a].append((b, dist))
            self.graph[b].append((a, dist))

        # get reachable cities
        cities_reachable: list[int] = [self._get_reachable_cities(i) for i in range(n)]
        res_city, _ = min(
            enumerate(cities_reachable),
            key=lambda idx_reachable: (idx_reachable[1], -idx_reachable[0]),
        )
        return res_city

    def _get_reachable_cities(self, starting_city: int):
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        INF = 1_000_000
        # visited cities and their distance
        visited: dict[int, int] = {}
        # priority queue of (distance_to_city, city_index)
        queue: list[tuple[int, int]] = [(0, starting_city)]
        while queue:
            # get closest neighbor
            total_dist, city = heapq.heappop(queue)
            if visited.get(city, INF) <= total_dist:
                # already visited with close distance
                continue
            visited[city] = total_dist
            # visit neighbors
            for neighbor, dist_to_neighbor in self.graph[city]:
                new_dist = total_dist + dist_to_neighbor
                if (
                    new_dist > self.distance_threshold
                    or visited.get(neighbor, INF) <= new_dist
                ):
                    # too far, or already visited
                    continue
                heapq.heappush(queue, (new_dist, neighbor))

        # amount of reachable cities given distance_threshold
        return len(visited)
