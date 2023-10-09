import bisect


class Solution:
    """
    Given an array of integers nums sorted in non-decreasing order, find the
    starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - nums is a non-decreasing array.
    - -10^9 <= target <= 10^9
    """

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return self.searchRange_implemented(nums, target)

    def searchRange_bisect(self, nums: list[int], target: int) -> list[int]:
        """
        O(n*log(n)) / O(1)  time / space complexity
        """
        l = bisect.bisect_left(nums, target)
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        r = bisect.bisect_right(nums, target, lo=l) - 1
        return [l, r]

    def searchRange_implemented(self, nums: list[int], target: int) -> list[int]:
        """
        O(n*log(n)) / O(1)  time / space complexity
        """
        # find starting position using binary search
        lo_lo, lo_hi = 0, len(nums) - 1
        while lo_lo <= lo_hi:
            mid = (lo_lo + lo_hi) // 2
            if nums[mid] < target:
                lo_lo = mid + 1
            else:
                lo_hi = mid - 1

        # if target not in nums, return [-1,-1]
        if lo_lo >= len(nums) or nums[lo_lo] != target:
            return [-1, -1]

        # find ending position again using binary search
        hi_lo = lo_lo
        hi_hi = len(nums) - 1
        while hi_lo <= hi_hi:
            mid = (hi_lo + hi_hi) // 2
            if nums[mid] == target:  # can compare using ==
                hi_lo = mid + 1
            else:
                hi_hi = mid - 1
        return [lo_lo, hi_hi]
