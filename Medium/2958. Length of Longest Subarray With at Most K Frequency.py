"""
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less
than or equal to k.

Return the length of the longestgood subarray ofnums.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        i = 0
        freq: dict[int, int] = {}
        max_len = 0
        for j, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            while freq[num] > k:
                freq[nums[i]] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
        return max_len
