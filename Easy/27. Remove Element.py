def originalRemoveElement(self, nums: [int], val: int) -> int:
    remainingLength = len(nums)
    nums.sort()
    found = False
    i = 0
    while i < remainingLength:
        if (found == True and nums[i] != val):
            return remainingLength
        if (nums[i] == val):
            found = True
            del nums[i]
            remainingLength -= 1
        else:
            i += 1
    return remainingLength


# class Solution:
#     def removeElement(self, nums: [int], val: int) -> int:
#         i = 0
#         while i < len(nums):
#             if nums[i] == val:
#                 del nums[i]
#             else:
#                 i +=
#         return len(nums)
