from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minStart = 0
        accumulative = 0
        for num in nums:
            accumulative += num
            if accumulative < 0:
                minStart = max(minStart, -accumulative)
        return minStart + 1
