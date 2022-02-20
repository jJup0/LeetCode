# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        # output now contains product of all elements to the left

        multiplier = 1
        # go in reverse to include product of all elements to the right
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= multiplier
            multiplier *= nums[i]
        return output
