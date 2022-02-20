class Solution:
    def search(self, nums: [int], target: int) -> int:
        idx = 0
        while len(nums) > 0:
            mid = len(nums) // 2
            if nums[mid] <= nums[-1]: # pivot is in first half
                if target >= nums[mid] and target <= nums[-1]: # check if the target is in the that half
                    nums = nums[mid:]
                    idx = idx+mid   #since nums is modified, add midpoint to index of the result
                else: # if not, it must be in another half
                    nums = nums[:mid]
            else: # pivot is in second half
                if target >= nums[0] and target <= nums[mid-1]: # check if the target is in the that half
                    nums = nums[:mid]
                else: # if not, it must be in another half
                    nums = nums[mid:] 
                    idx = idx+mid
            if len(nums) == 1:
                if nums[0] == target:
                    return idx
                else:
                    return -1
        return -1

 # since every other number appears exactly twice, by xoring, they will eventually all cancel each other out, even if in a weird order
    def xorSingleNumber(self, nums: [int]) -> int:
        number = 0
        for i in nums:
            number = number ^ i
        return number
