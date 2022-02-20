import math


class experimentalSolution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        res = 0
        ones = 0
        resetOnes = False
        prev_multipliers = [1]
        for n in nums:
            new_multipliers = []
            if n == 1:
                ones += 1
                new_multipliers = prev_multipliers
            else:
                for m in reversed(prev_multipliers):
                    if (product := n * m) < k:
                        new_multipliers.append(product)
                    else:
                        resetOnes = True
                        break

            res += len(new_multipliers) * math.factorial(ones)-1
            if resetOnes:
                ones = 0
                resetOnes = False

            prev_multipliers = new_multipliers + [1]
            print(f"{str(new_multipliers).ljust(30)}+{len(new_multipliers)} -> {res}")
        return res


class safeandslowSolution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        res = 0
        ones = 0
        prev_multipliers = [1]
        for n in nums:
            new_multipliers = []
            if n == 1:
                ones += 1
                new_multipliers += prev_multipliers
                # res += (len(new_multipliers)+1) * ones
            else:
                for m in reversed(prev_multipliers):
                    if (product := n * m) < k:
                        new_multipliers.append(product)

            res += len(new_multipliers)
            prev_multipliers = new_multipliers + [1]
            # print(f"{str(new_multipliers).ljust(20)}+{len(new_multipliers)} -> {res}")
        return res


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        product = 1
        for r, n in enumerate(nums):  # steadily go through nums, with n being the rightmost for current subarray
            product *= n
            while l < r and product >= k:  # if l == r, then n > k so break, or if the subbarray is valid
                product /= nums[l]  # shrink subarray from left side and divide current product
                l += 1
            if product < k:
                res += r-l+1  # add len of current valid subarray to result
        return res
