from functools import cache


class Solution:
    """
    You are given two 0-indexed integer arrays, cost and time, of size n representing
    the costs and the time taken to paint n different walls respectively. There are
    two painters available:
    - A paid painter that paints the ith wall in time[i] units of time and takes
      cost[i] units of money.
    - A free painter that paints any wall in 1 unit of time at a cost of 0. But
      the free painter can only be used if the paid painter is already occupied.

    Return the minimum amount of money required to paint the n walls.

    Constraints:
    - 1 <= cost.length <= 500
    - cost.length == time.length
    - 1 <= cost[i] <= 10^6
    - 1 <= time[i] <= 500
    """

    def paintWalls(self, costs: list[int], times: list[int]) -> int:
        return self.paintWalls_faster(costs, times)

    def paintWalls_time_painted_dp(self, costs: list[int], times: list[int]) -> int:
        """
        O(2^n) / O(2^n)   time / space complexity ?
        """
        postfix_times = times.copy()

        for i in range(len(postfix_times) - 2, -1, -1):
            postfix_times[i] += postfix_times[i + 1]

        INF = 1_000_000_000

        @cache
        def find_min_paint(index: int, time_painted: int) -> int:
            """
            Find minimum cost for walls[index:] given, that `time_painted` was previously
            spent by the paid worker, without the free worker using up that time.

            Args:
                index (int): Index from which to find minimum paint cost.
                time_painted (int): Previous time painted.

            Returns:
                int: Minimum paint cost.
            """
            if index == len(costs):
                # finished painting, if free painter was not abused, return 0 else infinity
                return 0 if time_painted >= 0 else INF

            if time_painted >= len(costs) - index:
                # if the free painted can be used for the remaining walls, return 0
                return 0

            if -time_painted > postfix_times[index]:
                # if the free painter was already abused too much in the past,
                # and can no longer be compensated, return infinity
                return INF

            free_painter_for_curr_wall = find_min_paint(index + 1, time_painted - 1)
            paid_painter_for_curr_wall = costs[index] + find_min_paint(
                index + 1, time_painted + times[index]
            )
            return min(free_painter_for_curr_wall, paid_painter_for_curr_wall)

        return find_min_paint(0, 0)

    def paintWalls_faster(self, costs: list[int], times: list[int]) -> int:
        """
        O(n^2) / O(n)   time / space complexity
        """
        INF = 1_000_000_000

        n = len(costs)
        # dp[i] = minimum cost to paint any i walls
        dp = [INF] * (n + 1)
        dp[0] = 0

        for cost, time in zip(costs, times):
            # iterate through i in reverse order, so that dp array is not contaminated
            # in current iteration, i.e. that are written are not read again until the
            # next (cost, time) pair
            for j in range(n, 0, -1):
                # if it is cheaper to pay to paint the current wall and use the
                # free painter for the remaining j-time-1 walls, then update dp[j]
                prev_wall_index = max(j - time - 1, 0)
                dp[j] = min(dp[j], dp[prev_wall_index] + cost)

        # return cost to paint any n walls (all walls)
        return dp[n]
