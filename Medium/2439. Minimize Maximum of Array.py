import math


class Solution:
    """
    You are given a 0-indexed array nums comprising of n non-negative integers.

    In one operation, you must:
        Choose an integer i such that 1 <= i < n and nums[i] > 0.
        Decrease nums[i] by 1.
        Increase nums[i - 1] by 1.
        Return the minimum possible value of the maximum integer of nums
        after performing any number of operations.

    Constraints:
        n == nums.length
        2 <= n <= 10^5
        0 <= nums[i] <= 10^9
    """

    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        Iterate through the array and perform "the operation" on the current
        index until it is no longer the highest value in the array so far.
        O(n) / O(1)     time / space complexity
        """
        max_val = 0
        # "capacity" of array entries up until now, i.e. how much entries in
        # nums[:i] can be increased by so that all entries have the same value
        unused_capacity = 0
        for i, num in enumerate(nums):
            diff = num - max_val
            if diff > 0:
                # if the current value is larger than all values that came before
                unused_capacity -= diff
                # perform "the operation" on the current index, and all other
                # indices before that and use up the "unused capacity"
                if unused_capacity < 0:
                    # if the capacity does not suffice, then the maximum value of
                    # the array so far increases to the sum of values so far
                    # divided by the amount of values so far
                    needed = -unused_capacity
                    res_increase = math.ceil(needed / (i + 1))
                    max_val += res_increase
                    unused_capacity += (i + 1) * res_increase
            else:
                # else the the current value can be "stocked up" to the largest
                # value so far when a larger value is encountered in the future
                unused_capacity += -diff
        return max_val
