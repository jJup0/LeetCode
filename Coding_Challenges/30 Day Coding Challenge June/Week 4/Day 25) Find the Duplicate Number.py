import collections


class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        c = collections.Counter(nums)
        return [num for num, freq in c.items() if freq > 1][0]
