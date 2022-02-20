class Solution:
    def singleNumber(self, nums):
        total_sum = sum(nums)
        unique_sum = sum(set(nums))
        return (3 * unique_sum - total_sum) // 2
