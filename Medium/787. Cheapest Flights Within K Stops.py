"""
There are n cities connected by some number of flights. You are given an array
flights where flights[i] = [from_i, to_i, price_i] indicates that there is a
flight from city from_i to city to_i with cost price_i.

You are also given three integers src, dst, and k, return the cheapest price
from src to dst with at most k stops. If there is no such route, return-1.

Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= from_i, to_i < n
- from_i != to_i
- 1 <= price_i <= 10^4
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst
"""

import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """
        m := len(flights)
        O(m * log(m) + n * k) / O(m + n * k)     time / space complexity
        """

        # double dict for sparse graphs
        flight_prices: defaultdict[int, dict[int, int]] = defaultdict(dict)
        for source, destination, price in flights:
            flight_prices[source][destination] = price

        # queue[i] = (cost, flights_taken, city)
        queue: list[tuple[int, int, int]] = [(0, 0, src)]

        dp = [[1_000_000] * n for _ in range(k + 1)]
        while queue:
            cost, flights_taken, city = heapq.heappop(queue)
            if city == dst:
                return cost
            if flights_taken > k or cost >= dp[flights_taken][city]:
                continue
            dp[flights_taken][city] = cost
            for neighbor, price in flight_prices[city].items():
                heapq.heappush(queue, (cost + price, flights_taken + 1, neighbor))

        return -1
