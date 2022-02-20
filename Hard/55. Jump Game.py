class Solution:
    def canJump(self, nums: [int]) -> bool:
        maxJump = 0
        for num in nums[:-1]:
            maxJump = max(maxJump, num)
            if not maxJump:
                return False
            maxJump -= 1
        return True
