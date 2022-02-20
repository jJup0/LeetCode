from collections import Counter


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        nc = Counter(nums)
        for num, count in nc.items():
            if count > len(nums)/2:
                return num
