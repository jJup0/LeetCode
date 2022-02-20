class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= multiplier
            multiplier *= nums[i]
        return output


class cheatSolution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        retArr = []
        count = 1
        ignoreFirstZeroCount = 1
        hadZero = False
        for num in nums:
            count *= num
            if not num:
                if hadZero:
                    return [0] * len(nums)
                hadZero = True
            else:
                ignoreFirstZeroCount *= num
        for num in nums:
            if num:
                retArr.append(int(count/num))
            else:
                retArr.append(int(ignoreFirstZeroCount))
        return retArr
