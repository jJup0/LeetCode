class Solution:
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is
    found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) >> 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
