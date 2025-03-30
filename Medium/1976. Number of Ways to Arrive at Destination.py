"""
You are in a city that consists of n intersections numbered from 0 to n - 1
with bi-directional roads between some intersections. The inputs are generated
such that you can reach any intersection from any other intersection and that
there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where
roads[i] = [u_i, v_i, time_i] means that there is a road between intersections
u_i and v_i that takes time_i minutes to travel. You want to know in how many
ways you can travel from intersection 0 to intersection n - 1 in the shortest
amount of time.

Return the number of ways you can arrive at your destination in the shortest
amount of time. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 200
- n - 1 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 3
- 0 <= u_i, v_i <= n - 1
- 1 <= time_i <= 10^9
- u_i!= v_i
- There is at most one road connecting any two intersections.
- You can reach any intersection from any other intersection.
"""

import heapq
from collections import defaultdict


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        # construct adjacency graph
        adj_graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for a, b, dist in roads:
            adj_graph[a].append((b, dist))
            adj_graph[b].append((a, dist))

        shortest_distance_to_node = [float("inf")] * n
        # ways to get to node with shortest distance
        ways_to_node = [0] * n
        shortest_distance_to_node[0], ways_to_node[0] = (0, 1)
        # prio_queue[i] = (distance from start, node number)
        prio_queue = [(0, 0)]
        while prio_queue:
            dist, node = heapq.heappop(prio_queue)
            if dist > shortest_distance_to_node[n - 1]:
                # no shorter ways to get to end
                break
            shortest_dist_to_node = shortest_distance_to_node[node]
            if dist > shortest_dist_to_node:
                # shorter path has been found to this node, no need to keep exploring
                continue
            if node == n - 1:
                # reached end, no need to explore further
                continue

            # traverse to neighbors
            for neighbor, distance_to_neighbor in adj_graph[node]:
                total_distance_to_neighbor = dist + distance_to_neighbor
                if total_distance_to_neighbor < shortest_distance_to_node[neighbor]:
                    # new shorter distance found, update memoization and add to queue
                    shortest_distance_to_node[neighbor] = total_distance_to_neighbor
                    ways_to_node[neighbor] = ways_to_node[node]
                    heapq.heappush(prio_queue, (total_distance_to_neighbor, neighbor))
                elif total_distance_to_neighbor == shortest_distance_to_node[neighbor]:
                    # add current ways to ways to neighbor
                    ways_to_node[neighbor] = (
                        ways_to_node[neighbor] + ways_to_node[node]
                    ) % MOD

        return ways_to_node[n - 1]
