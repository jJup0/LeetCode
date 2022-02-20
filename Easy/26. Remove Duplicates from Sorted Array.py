class firstSolution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        prev = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == prev:
                del nums[i]
            else:
                prev = nums[i]
                i += 1
        return len(nums)


class SolutionIdk(object):  # duplicates are replaced, because actual return is the first next_i_to_replace'th values in nums
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        prev_n = nums[0]
        next_i_to_replace = 1
        for i in range(len(nums)):
            if nums[i] != prev_n:
                nums[next_i_to_replace] = nums[i]
                next_i_to_replace += 1
                prev_n = nums[i]
        return next_i_to_replace

class delSolution:
    def removeDuplicates(self, nums: [int]) -> int:
        lastnum = None
        i = 0
        while i < len(nums):
            if nums[i] == lastnum:
                del nums[i]
            else:
                i += 1
                lastnum = nums[i]
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        uniquePos = 0
        for curPos in range(1, len(nums)):
            if nums[uniquePos] != nums[curPos]:
                curPos += 1
                nums[uniquePos] = nums[curPos]

        return uniquePos+1

