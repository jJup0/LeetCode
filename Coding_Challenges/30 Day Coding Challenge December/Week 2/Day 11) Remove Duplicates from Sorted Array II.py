class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curMax = -10000
        streak = 0
        i = 0
        for j, curr in enumerate(nums):
            if curr == curMax:
                if streak < 2:
                    if i < j:
                        nums[i] = curr
                    i += 1
                streak += 1
            elif curr > curMax:
                curMax = curr
                if i < j:      # swap
                    nums[i] = curr
                streak = 1
                i += 1

        return i
