from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 285 ms
        total = sum(nums)
        if total & 1:
            return False
        target = total//2
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums if (v + n) <= target})
            if target in possible_sums:
                return True
        return False

        # 36 ms, some bithack to emulate knapsack problem I think
        # s = sum(nums)
        # if s & 1:
        # return False
        # bits = 1
        # for n in nums:
        # bits |= bits << n

        # print(bits)

        # sum_half = (s >> 1)
        # return (bits >> sum_half) & 1


