class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        low, high = 0, len(nums)-1
        while high > low:
            mid = (high + low) >> 1
            # if at "odd" index, since 0 indexed, but technically even index, decrement
            if mid % 2:
                mid -= 1
            # if numbers next to each other are the same, then the single number is further ahead
            if nums[mid] != nums[mid+1]:
                high = mid
            else:
                low = mid + 2
        return nums[high]
