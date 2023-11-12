"""
You are given an array routes representing bus routes where routes[i] is a
bus route that the ith bus repeats forever.

- For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels 
  in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you
want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target.
Return -1 if it is not possible.

Constraints:
- 1 <= routes.length <= 500.
- 1 <= routes[i].length <= 10^5
- All the values of routes[i] are unique.
- sum(routes[i].length) <= 10^5
- 0 <= routes[i][j] < 10^6
- 0 <= source, target < 10^6
"""
from collections import defaultdict


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        """
        Could be optimized by only checking busstop "intersections" but somehow beats 99%.
        n := len(routes)
        m := sum(len(r) for r in routes)
        O(n + m) / O(n + m)     time / space complexity
        """

        # mapping from stops to busses
        stop_to_busses: defaultdict[int, list[int]] = defaultdict(list)
        for bus_nr, stops in enumerate(routes):
            for stop in stops:
                stop_to_busses[stop].append(bus_nr)

        curr_bus_stops: set[int] = set((source,))
        visited_busses: set[int] = set()
        visited_bus_stops: set[int] = set()

        for busses_taken in range(len(routes) + 1):
            if not curr_bus_stops:
                # if no new bus stops, break
                break
            if target in curr_bus_stops:
                return busses_taken
            visited_bus_stops.update(curr_bus_stops)
            # visit new bus stops
            new_stops: set[int] = set()
            for bus_stop in curr_bus_stops:
                for bus in stop_to_busses[bus_stop]:
                    if bus in visited_busses:
                        # do not use the same bus twice
                        continue
                    visited_busses.add(bus)
                    new_stops.update(routes[bus])
            # update curr bus stops, but only keep new ones
            curr_bus_stops = new_stops.difference(curr_bus_stops)

        # not possible to reach target from source
        return -1
