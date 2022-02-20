import math


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        best = -100000000000
        sumsofar = 0

        for i in nums:
            sumsofar += i
            best = max(sumsofar, best)
            sumsofar = max(sumsofar, 0)

        return best

# import time
# def maxSubArray(self, nums: [int]) -> int:
#     def calcSubArray(nums: [int]):
#         time.sleep(1)
#         print('New Deep: ', end='')
#         print(nums)
#         results = []
#         curStart, curEnd = 0, len(nums)-1
#         while curStart != curEnd:
#             curSum = 0
#             for i in range(curStart, curEnd+1):
#                 curSum += nums[i]
#             results.append(curSum)
#             print('start, end: ', end='')
#             print(curStart, curEnd)
#             if nums[curEnd] > nums[curStart]:
#                 print('Nice')
#                 curStart += 1
#             elif nums[curEnd] < nums[curStart]:
#                 print('Nice2')
#                 curEnd -= 1
#             else:
#                 print('nums ', end='')
#                 print(nums[curEnd], nums[curStart])
#                 print(nums[curStart:curEnd+1])
#                 results += calcSubArray(nums[curStart+1:curEnd + 1])  # remove start
#                 print('Ready for next split')
#                 results += calcSubArray(nums[curStart:curEnd])  # remove end
#         return results
#     finalResults = calcSubArray(nums)
#     finalResults.sort()
#     print(finalResults)
#     print(finalResults[-1])
#     return(finalResults[-1])
