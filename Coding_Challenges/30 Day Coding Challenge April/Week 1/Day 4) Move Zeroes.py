class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        totalzeroes = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                totalzeroes += 1
            else:
                i += 1
        for x in range(totalzeroes):
            nums.append(0)
