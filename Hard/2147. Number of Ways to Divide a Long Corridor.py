"""
Along a long library corridor, there is a line of seats and decorative plants.
You are given a 0-indexed string corridor of length n consisting of letters 'S'
and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another
to the right of index n - 1. Additional room dividers can be installed. For each
position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can
be installed.

Divide the corridor into non-overlapping sections, where each section has exactly
two seats with any number of plants. There may be multiple ways to perform the
division. Two ways are different if there is a position with a room divider
installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very
large, return it modulo 109 + 7. If there is no way, return 0.

Constraints:
- n == corridor.length
- 1 <= n <= 10^5
- corridor[i] is either 'S' or 'P'.
"""


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        Count plants in between pairs of sofas and multiply.
        O(n) / O(1)     time / space complexity
        """
        total_seats = corridor.count("S")
        if total_seats % 2 or total_seats == 0:
            # impossible to find separations if odd number of sofas or no sofas
            return 0

        MOD = 10**9 + 7
        result = 1
        # index of the last second sofa in a sofa pair
        prev_sofa_idx: int | None = None
        # start after the first sofa
        for i in range(corridor.index("S") + 1, len(corridor)):
            if corridor[i] == "S":
                if prev_sofa_idx is None:
                    # we found the second sofa in a sofa pair
                    prev_sofa_idx = i
                else:
                    # we found a new first sofa in a sofa pair
                    # update result by multiplying result so far by the amount
                    # of different ways of separating this new sofa pair from
                    # the previous one
                    positions_in_between = i - prev_sofa_idx
                    result = (result * (positions_in_between)) % MOD
                    # reset previous second sofa index
                    prev_sofa_idx = None

        return result
