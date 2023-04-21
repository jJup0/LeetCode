class Solution:
    """
    There is a group of n members, and a list of various crimes they could commit.
    The ith crime generates a profit[i] and requires group[i] members to participate
    in it. If a member participates in one crime, that member can't participate in
    another crime.

    Let's call a profitable scheme any subset of these crimes that generates at least
    minProfit profit, and the total number of members participating in that subset of
    crimes is at most n.

    Return the number of schemes that can be chosen. Since the answer may be very
    large, return it modulo 10^9 + 7.

    Constraints:
        1 <= n <= 100
        0 <= minProfit <= 100
        1 <= group.length <= 100
        1 <= group[i] <= 100
        profit.length == group.length
        0 <= profit[i] <= 100
    """

    def profitableSchemes(
        self, n: int, min_profit: int, group: list[int], profit: list[int]
    ) -> int:
        """
        Dynamic programming solution.
        O(n * min_profit * len(group)) / O(n * min_profit)  time / space complexity
        """
        n_inc = n + 1
        min_profit_inc = min_profit + 1
        MOD = 10**9 + 7

        # dynamic programming matrix; people_by_profit[i][j] equals ways make j
        # profit with i people. in case of j == minProfit, then people_by_profit[i][j]
        # equals ways to make *at least* j profit with i people
        people_by_profit = [[0] * (min_profit_inc) for _ in range(n_inc)]
        # there is 1 way to make 0 profit with 0 people
        people_by_profit[0][0] = 1

        # iterate through crimes
        for curr_g, curr_p in zip(group, profit):
            # set an empty temporary dp matrix, technically only needed
            # for people_by_profit[i][-1]
            people_by_profit_temp = [[0] * (min_profit_inc) for _ in range(n + 1)]
            # iterate through previous ways to make profit
            for prev_g in range(n_inc - curr_g):
                for prev_p in range(min_profit_inc):
                    total_g = curr_g + prev_g
                    total_p = min(curr_p + prev_p, min_profit)
                    # *additional* new ways to make prev_p + curr_p profit with prev_g + curr_g people =
                    # ways to make prev_p profit with prev_g people
                    people_by_profit_temp[total_g][total_p] = (
                        people_by_profit_temp[total_g][total_p]
                        + people_by_profit[prev_g][prev_p]
                    ) % MOD
            # apply updates from temporary dp array to regular dp matrix
            for g in range(curr_g, n_inc):
                for p in range(min_profit_inc):
                    people_by_profit[g][p] = (
                        people_by_profit[g][p] + people_by_profit_temp[g][p]
                    ) % MOD

        # sum up ways to make at least minProfit profit
        res = 0
        for g in range(n_inc):
            res = (res + people_by_profit[g][-1]) % MOD
        return res
