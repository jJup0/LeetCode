from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        for val in nums:
            if not val:
                res = max(res, streak)
                streak = 0
            else:
                streak += 1

        return max(res, streak)
