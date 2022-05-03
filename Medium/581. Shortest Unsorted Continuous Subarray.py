from typing import List


class Solution:
    """
    Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray
    in ascending order, then the whole array will be sorted in ascending order.
    Return the shortest such subarray and output its length.
    Constraints:
        1 <= nums.length <= 10^4
        -10^5 <= nums[i] <= 10^5
    """

    def findUnsortedSubarray(self, nums: List[int]) -> int:

        # end index for which subarray has to be sorted
        sort_end_idx = -1

        # maximum value so far
        max_val = nums[0]
        # minimum value *after* non decreasing start of list
        min_val = 100_000

        # iterate over tail of nums list
        for i, num in enumerate(nums[1:], start=1):
            # if the value is smaller than the biggest so far, the array has to be sorted at least until i
            if num < max_val:
                # if the number is the smallest encountered, update
                if num < min_val:
                    min_val = num
                sort_end_idx = i
            else:
                # otherwise this value is the biggest value so far by definition
                max_val = num

        # if the array is already sorted, sort_end_idx will be -1, so return 0
        if sort_end_idx == - 1:
            return 0

        # otherwise find the first value that min_val is larger equal to, from that index the subarray has to be sorted
        start_switch = 0
        while min_val >= nums[start_switch]:
            start_switch += 1

        # plus 1 to include both ends of the interval
        return sort_end_idx - start_switch + 1
