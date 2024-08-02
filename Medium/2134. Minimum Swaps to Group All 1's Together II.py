"""
A swap is defined as taking two distinct positions in an array and swapping the
values in them.

A circular array is defined as an array where we consider the first element and
the last element to be adjacent.

Given a binarycircular array nums, return the minimum number of swaps required
to group all 1's present in the array together at any location.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Move a sliding window across the circular array with the size sum(nums).
        Amount of swaps needed is the amount of zeros in the sliding window.
        O(n) / O(1)     time / space complexity
        """
        n = len(nums)
        # total amount of ones in array
        ones_count = sum(nums)
        # current amount of ones in sliding window
        curr_sum = sum(nums[i] for i in range(ones_count))
        # minimum number of swaps
        res = ones_count - curr_sum

        for i in range(ones_count, n + ones_count):
            # slide window one to the right
            curr_sum -= nums[i - ones_count]
            curr_sum += nums[i % n]
            # update result if zeros in sliding window are minimum so far
            swaps_needed = ones_count - curr_sum
            res = min(res, swaps_needed)

        return res
