"""
You are given two 0-indexed strings source and target, both of length n and
consisting of lowercase English letters. You are also given two 0-indexed
character arrays original and changed, and an integer array cost, where cost[i]
represents the cost of changing the character original[i] to the character
changed[i].

You start with the string source. In one operation, you can pick a character x
from the string and change it to the character y at a cost of z if there exists
any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using
any number of operations. If it is impossible to convert source to target,
return -1.

Note that there may exist indices i, j such that original[j] == original[i] and
changed[j] == changed[i].

Constraints:
- 1 <= source.length == target.length <= 10^5
- source, target consist of lowercase English letters.
- 1 <= cost.length == original.length == changed.length <= 2000
- original[i], changed[i] are lowercase English letters.
- 1 <= cost[i] <= 10^6
- original[i]!= changed[i]
"""

import heapq


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        costs: list[int],
    ) -> int:
        """
        Construct conversion graph and perform dijkstra search for cheapest conversion.
        m := size of the alphabet (in this case 26)
        O(n * m * log(m)) / O(m^2)  time / space complexity
        """

        def dijkstra(source: str, target: str) -> int | None:
            """
            O(m * log(m)) / O(m)    time / space complexity
            """
            nonlocal graph, dp_shortest_path, INT_INF
            if source == target:
                # no need to convert, free
                return 0

            if target in dp_shortest_path[source]:
                # previously calculated
                return dp_shortest_path[source][target]

            # regular dijkstra
            visited: set[str] = set()
            priority_queue = [(0, source)]
            while priority_queue:
                cost, char = heapq.heappop(priority_queue)
                if char in visited:
                    # shorter path to `char` already explored
                    continue

                # add current cost to dp
                dp_shortest_path[source][char] = cost

                if char == target:
                    # found target
                    return cost

                # add neighbors to queue
                visited.add(char)
                for neighbor, cost_to_neighbor in graph[char].items():
                    if neighbor in visited:
                        continue
                    heapq.heappush(priority_queue, (cost + cost_to_neighbor, neighbor))

            # no way to convert source to target
            return None

        INT_INF = 1_000_000_000

        # construct graph for converting chars
        graph: dict[str, dict[str, int]] = {
            chr(char_ord): {} for char_ord in range(ord("a"), ord("z") + 1)
        }
        for a, b, cost in zip(original, changed, costs):
            graph[a][b] = min(cost, graph[a].get(b, INT_INF))

        # dynamic programming for shortest path between two nodes
        dp_shortest_path: dict[str, dict[str, int]] = {k: {} for k in graph}

        # find cheapest conversion for each letter
        total_cost = 0
        for source_char, target_char in zip(source, target):
            cost = dijkstra(source_char, target_char)
            if cost is None:
                # no way to convert letter, return -1
                return -1
            total_cost += cost
        return total_cost
