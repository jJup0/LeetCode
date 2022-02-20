from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0]*(len(nums) + 1)
        dpAbs = [0]*(len(nums))
        lastZero = 0;
        for i, num in enumerate(nums):
            if not num:
                lastZero = i + 1
            curMax = dp[i] * num if dp[i] else num
            dp[i+1] = curMax
            dpAbs[i] = curMax
            if curMax < 0:
                for j in range(lastZero, i+1):
                    if dp[j] < 0:
                        dpAbs[i] = int(curMax/dp[j])
                        break
                    
        return max(dpAbs)