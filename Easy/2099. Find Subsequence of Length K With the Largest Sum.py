"""
You are given an integer array nums and an integer k. You want to find a
subsequence of nums of length k that has the largest sum.

Returnany such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= nums.length
"""

import heapq
from collections import Counter


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        Make counter of largest nums and append to result if num in counter.
        Decrement each time number is added to result.

        Complexity:
            Time: O(n * log(k))
            Space: O(k)
        """
        largest_unused_nums = Counter(heapq.nlargest(k, nums))
        res: list[int] = []
        for num in nums:
            if largest_unused_nums.get(num, 0):
                res.append(num)
                largest_unused_nums[num] -= 1
        return res
