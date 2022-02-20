class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        prevSums, result, countSum = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            countSum += num and 1 or -1  # if num is 1 add one, if num is 0 subtract 1
            if countSum in prevSums:
                result = max(result, i - prevSums[countSum])
            else:
                prevSums[countSum] = i
        return result
