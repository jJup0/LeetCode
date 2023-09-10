from math import factorial


class Solution:
    """
    Given n orders, each order consist in pickup and delivery services.

    Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

    Since the answer may be too large, return it modulo 10^9 + 7.

    Constraints:
    - 1 <= n <= 500
    """

    def countOrders(self, n: int) -> int:
        return self.countOrders_math(n)

    def countOrders_iterative(self, n: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        MOD = 10**9 + 7
        res = 1
        for prev_deliveries in range(1, n):
            # for x previous deliveries, there are 2x+1 `places` in
            # the delivery order to place P{x+1}
            possible_placements = 2 * prev_deliveries + 1
            # there are n choose 2 ways to place a PX DX pair, plus an extra
            # `possible_placements` ways, for when PX and DX are placed in
            # the same position
            # multiply with previous result, as new pair can be placed in any
            # of the previous permutations
            res *= (
                possible_placements * (possible_placements - 1)
            ) // 2 + possible_placements
            # mod for large answer
            res %= MOD
        return res

    def countOrders_math(self, n: int) -> int:
        """
        O(n) / (O(log((2n)!)) time / space complexity
        """
        MOD = 10**9 + 7
        all_permutations = factorial(2 * n)
        ways_for_incorrect_delivery_orders = 2**n
        return (all_permutations // ways_for_incorrect_delivery_orders) % MOD
