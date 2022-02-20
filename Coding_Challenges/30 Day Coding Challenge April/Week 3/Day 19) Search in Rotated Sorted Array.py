class Solution:
    def search(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:  # turning point in first half
                if target < nums[mid] and target >= nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            else:  # turning point in second half
                if target > nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
