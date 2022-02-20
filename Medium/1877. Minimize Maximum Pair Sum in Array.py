class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums) - 1
        return max(nums[i] + nums[l-i] for i in range((l+1) // 2))
