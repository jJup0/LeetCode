"""
There are numBottles water bottles that are initially full of water. You can
exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of
water bottles you can drink.

Constraints:
- 1 <= numBottles <= 100
- 2 <= numExchange <= 100
"""


class Solution:
    def numWaterBottles(self, full_bottles: int, num_exchange: int) -> int:
        """
        O(log(n)) / O(1)    time / space complexity
        """
        empty_bottles = 0
        res = 0
        while full_bottles:
            # drink full bottles, converting them to empty bottles
            res += full_bottles
            # convert as many empty bottles to full bottles
            full_bottles, empty_bottles = divmod(
                full_bottles + empty_bottles, num_exchange
            )
        return res
