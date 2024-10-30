x = """
You may recall that an array arr is a mountain array if and only if:
- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] <... < arr[i - 1] < arr[i]
  - arr[i] > arr[i + 1] >... > arr[arr.length - 1]

Given an integer array nums, return the minimum number of elements to
remove to make nums a mountain array.

Constraints:
- 3 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
- It is guaranteed that you can make a mountain array out of nums.
"""
from typing import Iterable

from sortedcontainers import SortedList


class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        # get longest increasing and decreasing monotone subsequences
        increasing = self._get_increasing(nums)
        decreasing = reversed(self._get_increasing(reversed(nums)))

        # using longest monotone subsequences, find longest mountain
        longest_mountain = max(
            inc + dec + 1
            for inc, dec in zip(increasing, decreasing)
            # only counts as mountain if there are smaller numbers on each side of the number
            if inc and dec
        )

        return len(nums) - longest_mountain

    def _get_increasing(self, nums: Iterable[int]) -> list[int]:
        """Gets right side length for mountain peaks in a list of numbers.

        Computes the length of the longest strictly increasing subsequence up to each
        index for elements smaller than the current number.

        Args:
            nums (list[int]): Arbitrary list of numbers.

        Returns:
            list[int]: A list `l` where `l[i]` = the length of the longest strictly
                monotone increasing subsequence l[:i] for numbers smaller than nums[i].

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        increasing: list[int] = []
        prevs = SortedList()
        j: int
        num2: int
        for i, num in enumerate(nums):
            res = -1
            for num2, j in prevs:  # type: ignore # unknown
                if num2 >= num:
                    break
                if increasing[j] > res:
                    res = increasing[j]
            prevs.add((num, i))  # type: ignore # unknown
            increasing.append(res + 1)

        return increasing
