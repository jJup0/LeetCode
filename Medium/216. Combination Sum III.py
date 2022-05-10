from collections import deque
from typing import List


class Solution:

    """
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
        Only numbers 1 through 9 are used.
        Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
    Constraints:
        2 <= k <= 9
        1 <= n <= 60
    """

    # problem could be generalized to any maximum "digit" not just 9

    def __init__(self):
        # calculate prefix sum once
        self.smallest_possible = [0] * 10
        for i in range(1, 10):
            self.smallest_possible[i] = self.smallest_possible[i-1] + i

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # use helper function to avoid default values
        # recursive with the extra parameter highest_allowed, which species the highest
        # digit allowed to still be used in the combination
        def helper(k, n, highest_allowed):

            # if only one digit is left, return a list of a list of the remaining value
            if k == 1 and n <= highest_allowed:
                return [[n]]

            res = []
            # go through remaining allowed values from highest to lowest
            # O(k)
            for new_val in range(highest_allowed, 0, -1):
                # if adding val to the combination so far still makes it possible to complete the sequence
                if n-new_val >= self.smallest_possible[k-1]:
                    # recursively find combinations with one less digit, n-new_val total goal sum
                    # and only values from 1 to new_val-1
                    new_combs = helper(k-1, n-new_val, new_val-1)
                    # append new_val to all the combinations
                    # O(?)
                    for comb in new_combs:
                        comb.append(new_val)
                    # add the new combinations to the result
                    res.extend(new_combs)

            return res

        # case of n is too small for k is taken care of in helper, and doesnt trigger a recurance so in O(1) or O(k),
        # but perform a check if the n is even reachable with the allowed digits, if not instantly return (only for performance)
        # O(k)
        if (sum(range(9-k, 10)) < n):
            return []
        return helper(k, n, 9)
