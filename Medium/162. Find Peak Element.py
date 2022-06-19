from typing import List


class Solution:
    """
    A peak element is an element that is strictly greater than its neighbors.
    Given an integer array nums, find a peak element, and return its index.
    If the array contains multiple peaks, return the index to any of the peaks.
    You may imagine that nums[-1] = nums[n] = -∞.
    You must write an algorithm that runs in O(log n) time.
    Constraints:
        1 <= nums.length <= 1000
        -2^31 <= nums[i] <= 2^31 - 1
        nums[i] != nums[i + 1] for all valid i.
    """

    def findPeakElement(self, nums: List[int]) -> int:
        # if only one element, or first element is peak, return 0
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        # if last element is peak return last index
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        # since if len(nums) == 2, one of the above would apply
        # len(nums) >= 3 means nums[mid] will always have neighbors
        assert len(nums) >= 3

        # perform binary search
        # invariant nums[lo] > nums[lo-1] and nums[hi] > nums[hi+1] meaning a peak has to be somewhere between [lo; hi]
        lo = 1
        hi = len(nums) - 2
        while lo <= hi:
            # get middle index
            mid = (lo + hi) >> 1

            # get values of middle and its neighbors
            mid_val = nums[mid]

            # if nums[mid-1] > nums[mid], then hi := mid-1 make invariant stay true
            if nums[mid-1] > mid_val:
                hi = mid - 1

            # if nums[mid+1] > nums[mid], then lo := mid+1 make invariant stay true
            elif nums[mid+1] > mid_val:
                lo = mid + 1

            # if neither neighbor of nums[mid] is larger than nums[mid], nums[mid] is a peak
            else:
                return mid

        # constraint stating that numbers are unique means there must be a peak
        assert False
