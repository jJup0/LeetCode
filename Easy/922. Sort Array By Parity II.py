from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idxs = [0, 1]
        i = 0
        while i < n:
            idx_parity = i % 2

            if nums[i] % 2 == idx_parity:
                i += 1
                continue

            idx_anti_parity = not idx_parity
            nums[idxs[idx_anti_parity]], nums[i] = nums[i], nums[idxs[idx_anti_parity]]
            idxs[idx_anti_parity] += 2

        return nums
