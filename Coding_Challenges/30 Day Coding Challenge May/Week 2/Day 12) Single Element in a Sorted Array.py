class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        low, high = 0, len(nums)-1
        while high > low:
            mid = low + ((high-low)//2)
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid+1]:
                high = mid-2
            else:
                low = mid + 2
        return nums[high]