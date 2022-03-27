from typing import List
class Solution:
    # constraint nums is sorted
    def search(self, nums: List[int], target: int) -> int:
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
            
        # assert lo == hi
        # if lo/hi is in bounds of the array and the number at nums[lo] is the target return the index
        # otherwise the number is not in the array so return -1
        return lo if (lo < len(nums) and nums[lo] == target) else -1