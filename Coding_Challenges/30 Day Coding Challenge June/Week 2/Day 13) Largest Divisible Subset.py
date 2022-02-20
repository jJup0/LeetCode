class Solution:
    def largestDivisibleSubset(self, nums: [int]) -> [int]:
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((divSubSet+[n] for divSubSet in dp if (divSubSet == []) or n % divSubSet[-1] == 0), key=len))  # n will always be bigger than last item in a div subset
        return max(dp, key=len)
