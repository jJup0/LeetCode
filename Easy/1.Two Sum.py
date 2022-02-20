# mine:
class firstSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for i in range(x+1, len(nums)):
                if nums[x] + nums[i] == target:
                    return [x, i]


# one pass hash table
class Solution(object):
    def twoSum(self, nums, target):
        numsDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsDict:
                return [numsDict[complement], i]
            numsDict[nums[i]] = i
