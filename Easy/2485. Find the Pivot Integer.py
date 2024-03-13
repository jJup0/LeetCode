"""
Given a positive integer n, find the pivot integerx such that:
- The sum of all elements between 1 and x inclusively equals the sum of all
  elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is
guaranteed that there will be at most one pivot index for the given input.

Constraints:
- 1 <= n <= 1000
"""

import math


class Solution:

    def pivotInteger(self, n: int) -> int:
        return self.pivotInteger_o_1(n)

    def pivotInteger_o_1(self, n: int) -> int:
        """
        O(1) / O(1)     time / space complexity
        """
        sum_1_to_n = (n * (n + 1)) // 2  # sum(range(n))

        # we need to find x such that sum(range(x)) == sum(range(x, n+1))
        # also note that sum(range(x)) + sum(range(x, n+1)) - x == sum(range(n))
        # therfore we know that sum(range(x)) >= sum(range(n)) / 2 and sum(range(x)) ~= sum(range(n)) / 2
        # so we find the smallest x for which sum(range(x)) >= sum(range(n)) / 2,
        # and check if it a pivot integer
        half_sum = sum_1_to_n / 2
        # approximate the inverse function of (n * (n + 1)) / 2
        potential_pivot = math.floor((half_sum * 2) ** 0.5)

        # calculate the two sums of ranges for the candidate for x
        sum_1_to_x = potential_pivot * (potential_pivot + 1) // 2
        sum_x_to_n = sum_1_to_n - sum_1_to_x + potential_pivot
        # if the sums are equal return x
        if sum_1_to_x == sum_x_to_n:
            return potential_pivot
        # else candidate was false, return -1
        return -1

    def pivotInteger_o_n(self, n: int) -> int:
        """
        Intuitive simple solution
        O(n) / O(1)     time / space complexity
        """
        sum_1_to_x = 0
        sum_x_to_n = (n * (n + 1)) // 2
        for x in range(1, n + 1):
            sum_1_to_x += x
            sum_x_to_n -= x - 1
            if sum_1_to_x == sum_x_to_n:
                return x
            if sum_1_to_x > sum_x_to_n:
                break
        return -1
