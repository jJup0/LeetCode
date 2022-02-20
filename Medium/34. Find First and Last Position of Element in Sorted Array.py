class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                break
        else:
            return [-1, -1]
        while nums[lo] != target:
            lo += 1
        while nums[hi] != target:
            hi -= 1
        return [lo, hi]
