from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort numbers and go through pairs from both ends
        nums.sort()

        # index of larger number
        j = len(nums) - 1
        res = 0

        for i, small in enumerate(nums):
            # while smallest remaining number and largest remaining number are bigger than k,
            # reduce index j, to find nums[j] so that hopeflly small + nums[j] == k
            while (i < j) and (small + nums[j] > k):
                j -= 1

            # if indexes cross, break
            if i >= j:
                break

            # assert small + nums[j] <= k, if they are exactly equal,
            # increment res and "remove" num at index j by decrementing j
            if small + nums[j] == k:
                res += 1
                j -= 1

        return res
