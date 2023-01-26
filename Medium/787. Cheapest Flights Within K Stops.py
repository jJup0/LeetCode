from collections import defaultdict


class Solution:
    """
    There are n cities connected by some number of flights. You are given an array flights where
    flights[i] = [from_i, to_i, price_i] indicates that there is a flight from city from_i to city
    toi with cost price_i.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst
    with at most k stops. If there is no such route, return -1.

    Constraints:
        1 <= n <= 100
        0 <= flights.length <= (n * (n - 1) / 2)
        flights[i].length == 3
        0 <= from_i, to_i < n
        from_i != to_i
        1 <= pricei <= 10^4
        There will not be any multiple flights between two cities.
        0 <= src, dst, k < n
        src != dst
    """

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        """
        O(n^2) / O(n^2)     time / space complexity
        """

        # double dict for sparse graphs
        source_to_dest_and_price = defaultdict(dict)
        for source, destination, prev_price in flights:
            source_to_dest_and_price[source][destination] = prev_price

        # aritificial infinity (according to constraints)
        inf = (K + 1) * 10_000

        # dp array to track cheapest way to get to destination, within current max stops
        cheapest_flights_cost_from_src = [inf] * n
        cheapest_flights_cost_from_src[src] = 0

        for _ in range(K+1):
            # iterate over all possible previous destinations
            for new_source, prev_price in enumerate(cheapest_flights_cost_from_src.copy()):
                if prev_price > inf:
                    continue

                # update dp array if flying to new_source and then to dest is cheaper
                for dest, flight_price in source_to_dest_and_price[new_source].items():
                    cheapest_flights_cost_from_src[dest] = min(cheapest_flights_cost_from_src[dest], prev_price + flight_price)

        # if destination can be reached, return cheapest cost
        if cheapest_flights_cost_from_src[dst] < inf:
            return cheapest_flights_cost_from_src[dst]

        # destination not reachable
        return -1
