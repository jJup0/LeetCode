"""
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers
i such that:
- 1 <= i <= n
- The decimal representation of i * i can be partitioned into contiguous
  substrings such that the sum of the integer values of these substrings equals i.

Constraints:
- 1 <= n <= 1000
"""

from functools import cache


class Solution:
    # make methods class methods so we can cache them because leetcode usually creates a new object for each call
    @classmethod
    @cache
    def punishmentNumber(cls, n: int) -> int:
        """
        Complexity without caching:
            Time: O(n * n)
            Space: O(n)
        Complexity if n-1 cached:
            Time: O(n)
            Cache Space: O(n)
            Call space: O(log(n))
        """
        if n == 1:
            return 1

        if cls._can_patition_into(n * n, n):
            return n * n + cls.punishmentNumber(n - 1)
        return cls.punishmentNumber(n - 1)

    @classmethod
    def _can_patition_into(cls, digits: int, target: int) -> bool:
        """
        Returns true iff digits can be partitioned such that the sum of its partitions equals target.
        Complexity:
            Time: O(n)
            Space: O(log(n))
        """
        if target < 0:
            # impossible to sum to
            return False
        if digits == target:
            # trivially true
            return True

        # split into only two partitions but do so recursively
        first_partition = digits
        second_partition = 0
        # power of 10 for the current digit we are on
        power_of_10 = 1
        while first_partition:
            # remove last digits from first partition and include in second partition
            first_partition, curr_digit = divmod(first_partition, 10)
            second_partition += curr_digit * power_of_10
            # check if first partition can be recursively partitioned to meet remainder of target
            if cls._can_patition_into(first_partition, target - second_partition):
                return True
            power_of_10 *= 10
        return False
