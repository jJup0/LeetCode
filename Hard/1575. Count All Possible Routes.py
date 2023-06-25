from functools import cache


class Solution:
    """
    You are given an array of distinct positive integers locations where
    locations[i] represents the position of city i. You are also given integers
    start, finish and fuel representing the starting city, ending city, and the
    initial amount of fuel you have, respectively.

    At each step, if you are at city i, you can pick any city j such that j != i
    and 0 <= j < locations.length and move to city j. Moving from city i to
    city j reduces the amount of fuel you have by |locations[i] - locations[j]|.
    Please notice that |x| denotes the absolute value of x.

    Notice that fuel cannot become negative at any point in time, and that you
    are allowed to visit any city more than once (including start and finish).

    Return the count of all possible routes from start to finish. Since the
    answer may be too large, return it modulo 10^9 + 7.

    Constraints:
    - 2 <= locations.length <= 100
    - 1 <= locations[i] <= 10^9
    - All integers in locations are distinct.
    - 0 <= start, finish < locations.length
    - 1 <= fuel <= 200
    """

    def countRoutes(
        self, locations: list[int], start: int, finish: int, starting_fuel: int
    ) -> int:
        return self.count_routes_early_break(locations, start, finish, starting_fuel)

    def count_routes_original(
        self, locations: list[int], start: int, finish: int, starting_fuel: int
    ) -> int:
        """Simple dp approach, memozie ways for to end at location *j* with *i* fuel remaining. (~1700 ms)
        n = len(locations), m = starting_fuel
        O(m * n^2) / O(n^2 + n * m)     time / space complexity
            space complexity can be reduce to O(n * m) without asymptotic time complexity loss.
        """
        location_count = len(locations)
        MOD = 10**9 + 7

        diff_from_loc_to_loc = [[0] * location_count for _ in range(location_count)]
        for i, loc1 in enumerate(locations):
            for j in range(i + 1, location_count):
                loc2 = locations[j]
                dist = abs(loc1 - loc2)
                diff_from_loc_to_loc[i][j] = dist
                diff_from_loc_to_loc[j][i] = dist

        # memoization array: dp[fuel][loc] = ways to reach location loc with fuel remaining
        dp = [[0] * location_count for _ in range(starting_fuel + 1)]
        # starting at start location == 1 way to reach with maximum fuel
        dp[starting_fuel][start] = 1

        # start with max fuel, and iterate down
        for fuel in range(starting_fuel, -1, -1):
            # iterate through all starting locations at current remaining fuel
            for loc1, ways in enumerate(dp[fuel]):
                # if there are no ways to reach current location with current fuel, skip
                if ways == 0:
                    continue
                # iterate through all destinations
                for loc2 in range(location_count):
                    if loc1 == loc2:
                        continue
                    fuel_left = fuel - diff_from_loc_to_loc[loc1][loc2]
                    if fuel_left < 0:
                        continue
                    # if fuel left to drive to destination, add to ways
                    dp[fuel_left][loc2] = (dp[fuel_left][loc2] + ways) % MOD

        return sum(dp[f][finish] for f in range(starting_fuel + 1)) % MOD

    def count_routes_alternative_1(
        self, locations: list[int], start: int, finish: int, fuel: int
    ) -> int:
        # taken and modified from someone elses submission (~1700 ms)

        N = len(locations)
        MOD = 10**9 + 7

        @cache
        def ways_to_finish(i: int, fuel: int) -> int:
            """Calculates number of ways to reach finish starting at i with fuel left.

            Constraints:
            - fuel >= 0
            - 0 <= i < len(locations)
            """
            res = 0

            # if currently at finish, then one extra way of reaching finish
            # but continue with fuel left
            if i == finish:
                res += 1

            for j in range(N):
                if j == i:
                    continue

                fuel_left = fuel - abs(locations[i] - locations[j])
                # only recurse if any fuel remaining
                if fuel_left >= 0:
                    res += ways_to_finish(j, fuel_left)

            return res % MOD

        return ways_to_finish(start, fuel)

    def count_routes_early_break(
        self, locations: list[int], start: int, finish: int, starting_fuel: int
    ) -> int:
        # taken and modified from someone elses submission (~1000 ms)
        MOD = 10**9 + 7

        edge_map: list[list[tuple[int, int]]] = [[] for _ in range(len(locations))]
        n = len(locations)
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(locations[i] - locations[j])
                if cost <= starting_fuel:
                    edge_map[i].append((cost, j))
                    edge_map[j].append((cost, i))

        for distances in edge_map:
            distances.sort()

        @cache
        def dfs(i: int, fuel: int) -> int:
            ways = int(i == finish)
            for next_cost, next_node in edge_map[i]:
                fuel_remaining = fuel - next_cost
                if fuel_remaining < 0:
                    # since our edges are sorted we can exit early
                    break
                ways += dfs(next_node, fuel_remaining)
            return ways % MOD

        return dfs(start, starting_fuel) % MOD
