"""
You are given a 0-indexed array nums and a non-negative integer k.

In one operation, you can do the following:
- Choose an index i that hasn't been chosen before from the range
  [0, nums.length - 1].
- Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].

The beauty of the array is the length of the longest subsequence consisting of
equal elements.

Return the maximum possible beauty of the array nums after applying the
operation any number of times.

Note that you can apply the operation to each index only once.

A subsequence of an array is a new array generated from the original array by
deleting some elements (possibly none) without changing the order of the
remaining elements.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i], k <= 10^5
"""


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """
        Sort nums and sliding window approach.
        Complexity:
            Time: O(n * log(n))
            Space: O(sort(n))
        """
        nums.sort()
        res = 0
        l = 0
        for r, val in enumerate(nums):
            # increase lower index `l` until nums[l] and nums[r]
            # can be made into the same number by adding/subtracting
            # a value less than/equal to k
            while nums[l] < val - k * 2:
                l += 1
            res = max(res, r - l + 1)
        return res

    def maximumBeauty_sliding_window_hack(self, nums: list[int], k: int) -> int:
        nums.sort()
        # l points not to the current sliding window starting index,
        # but to the index at which a new largest sliding window
        # would be. Avoids max() call at each iteration.
        l = 0
        for num in nums:
            if nums[l] + 2 * k < num:
                l += 1
        return len(nums) - l
