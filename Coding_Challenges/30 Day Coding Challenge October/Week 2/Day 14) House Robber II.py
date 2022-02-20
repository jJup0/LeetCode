class Solution:
    def rob(self, nums):
        if len(nums) < 3:
            return max(nums)

        prev, curr = 0,0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        end = curr
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr - end
