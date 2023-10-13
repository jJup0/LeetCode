class Solution:
    """
    You are given an integer array cost where cost[i] is the cost of i^th step
    on a staircase. Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

    Constraints:
    - 2 <= cost.length <= 1000
    - 0 <= cost[i] <= 999
    """

    def minCostClimbingStairs(self, costs: list[int]) -> int:
        return self.minCostClimbingStairs_look_back(costs)

    def minCostClimbingStairs_regular(self, costs: list[int]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # initialize dp array for best costs with infinity
        dp = [1_000_000] * (len(costs) + 2)

        # can start at first two steps, so they are free
        dp[0] = dp[1] = 0

        for i, cost in enumerate(costs):
            # calculate next cost and update dp
            next_cost = dp[i] + cost
            dp[i + 1] = min(dp[i + 1], next_cost)
            dp[i + 2] = min(dp[i + 2], next_cost)

        return dp[len(costs)]

    def minCostClimbingStairs_o_1_space(self, costs: list[int]) -> int:
        """
        Use ring array for O(1) space complexity.
        O(n) / O(1)     time / space complexity
        """
        INF = 1_000_000
        small_dp = [INF] * 3
        small_dp[0] = small_dp[1] = 0
        for i, cost in enumerate(costs):
            dp_pointer = i % 3
            next_cost = small_dp[dp_pointer] + cost
            # reset the memory to inf
            small_dp[dp_pointer] = INF
            # "calculate" dp pointers
            dp_pointer_inc = (dp_pointer + 1) % 3
            dp_pointer_inc_inc = (dp_pointer + 2) % 3
            # update dp
            small_dp[dp_pointer_inc] = min(small_dp[dp_pointer_inc], next_cost)
            small_dp[dp_pointer_inc_inc] = min(small_dp[dp_pointer_inc_inc], next_cost)
        return small_dp[len(costs) % 3]

    def minCostClimbingStairs_look_back(self, costs: list[int]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        if len(costs) == 1:
            return costs[0]

        # dp[i] stores minimum to jump from step i
        dp = [0 for _ in range(len(costs))]
        dp[0] = costs[0]
        dp[1] = costs[1]

        for i in range(2, len(costs)):
            dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])
