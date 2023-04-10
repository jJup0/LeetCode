from typing import List


class Solution:
    """
    Given an array of integers nums which is sorted in ascending order, and an
    integer target, write a function to search target in nums. If target exists,
    then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Constraints:
        1 <= nums.length <= 10^4
        -10^4 < nums[i], target < 10^4
        All the integers in nums are unique.
        nums is sorted in ascending order.
    """

    def search(self, nums: list[int], target: int) -> int:
        # lo and hi represent lower and higher boundary of where the number could be
        lo = 0
        hi = len(nums)
        # while these boundaries form a valid interval
        while lo < hi:
            # calculate the middle position between the boundaries
            mid = (lo + hi) >> 1
            # if the number at that position is smaller, then set lo as mid + 1, as any number at a lower
            # index than mid can not be the target, as nums[mid] is already too small
            if nums[mid] < target:
                lo = mid + 1
            else:
                # else set high as the new middle, do not subtract 1, because here nums[mid] could be equal to target
                hi = mid

        # if lo/hi is in bounds of the array and the number at nums[lo] is the target return the index
        if lo < len(nums) and nums[lo] == target:
            return lo
        # otherwise the number is not in the array so return -1
        return -1
