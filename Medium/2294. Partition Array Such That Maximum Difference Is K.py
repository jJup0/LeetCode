"""
You are given an integer array nums and an integer k. You may partition nums
into one or more subsequences such that each element in nums appears in exactly
one of the subsequences.

Return the minimum number of subsequences needed such that the difference
between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 0 <= k <= 10^5
"""


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        """
        Sort nums and greedily put consecutive numbers in the same subsequence
        until the current number more than `k` greater than the smallest number
        in the current subsequence.

        Complexity:
            Time: O(n * log(n))
            Space: O(sort())
        """
        nums.sort()
        res = 1
        window_min = nums[0]
        for num in nums:
            if window_min + k < num:
                res += 1
                window_min = num
        return res
