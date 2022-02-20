class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) >> 1  # same as "//2"
            num = nums[mid]
            if target > num:
                lo = mid + 1
            elif target < num:
                hi = mid - 1
            else:
                return mid
        return lo if (lo < len(nums) and nums[lo] == target) else -1
