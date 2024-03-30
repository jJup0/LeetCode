"""
Given an integer array nums and an integer k, return the number of good
subarrays of nums.

A good array is an array where the number of different integers in that array
is exactly k.
- For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i], k <= nums.length
"""


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        O(n^2) / O(n)     time / space complexity
        """
        # occurance counts of each number in the sliding window
        num_counts: dict[int, int] = {}
        # unique numbers in the sliding window
        different_nums = 0
        res = 0
        i = 0
        for j, num in enumerate(nums):
            prev_count = num_counts.get(num, 0)
            num_counts[num] = prev_count + 1
            if prev_count == 0:
                # new number, increase different nums count
                different_nums += 1

            if different_nums > k:
                # too many unique numbers, shrink sliding window
                for i in range(i, j):
                    num_counts[nums[i]] -= 1
                    if num_counts[nums[i]] == 0:
                        different_nums -= 1
                        break
                i += 1

            if different_nums == k:
                # THIS PART MAY BE OPTIMIZED FOR LINEAR/SUPERLINEAR TIME
                # find index at which the sliding window starts
                sliding_window_start = i
                for sliding_window_start in range(i, j + 1):
                    num_counts[nums[sliding_window_start]] -= 1
                    if num_counts[nums[sliding_window_start]] == 0:
                        break
                # undo subtracting the counts
                for sliding_window_start in range(i, sliding_window_start + 1):
                    num_counts[nums[sliding_window_start]] += 1
                # update result with the sliding window diff
                res += sliding_window_start - i + 1

        return res

    def brute_force_subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Used only for testing the actual function.
        O(n^3) / O(n)     time / space complexity
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if len(set(nums[i : j + 1])) == k:
                    res += 1
        return res
